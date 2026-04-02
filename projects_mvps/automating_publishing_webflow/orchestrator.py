#!/usr/bin/env python3
"""
Wayground Content Evaluation Pipeline — Orchestrator

Usage:
  python orchestrator.py run          # Evaluate all 37 articles + cluster synthesis + write Sheets
  python orchestrator.py resume       # Resume from last checkpoint (skip already-done articles)
  python orchestrator.py status       # Show current progress
  python orchestrator.py dry-run      # Print prompts for first 3 articles, no Claude calls
  python orchestrator.py single 52    # Evaluate a single article by item number
  python orchestrator.py clusters     # Run cluster synthesis only (articles must be done first)
  python orchestrator.py sheets       # Write results to Google Sheets only (evaluation must be done)
  python orchestrator.py brand-rerun  # Re-run brand evaluation only for articles with brand_eval_failed=True
  python orchestrator.py enhance      # Apply AEO fixes and write enhanced articles locally + Sheets
  python orchestrator.py enhance-single 52  # Enhance a single article by item number
  python orchestrator.py drive-audit  # Audit service account Drive storage (read-only)
  python orchestrator.py enhance-gdocs # Copy originals → apply fixes → transfer ownership
  python orchestrator.py enhance-gdocs-single 52  # Same but for one article

  --- Publishing pipeline ---
  python orchestrator.py improvement-delta        # Step 1: Document what changed per article → Sheets
  python orchestrator.py continuity-check         # Step 2: Structural checks (word count, headings, keywords)
  python orchestrator.py teacher-review           # Step 3: SME/teacher review (10 criteria) → Sheets
  python orchestrator.py webflow-setup            # Step 4: List Webflow collections → find collection IDs
  python orchestrator.py webflow-publish          # Steps 5–6: Publish all articles as drafts to Webflow
  python orchestrator.py webflow-publish --live   # Steps 5–6: Publish live (not just draft)
  python orchestrator.py webflow-publish-single 52        # Test one article (draft)
  python orchestrator.py webflow-publish-single 52 --live # Test one article (live)
  python orchestrator.py webflow-mcp-export     # Build MCP payloads → outputs/webflow_payloads.json (no token needed)

  --- MCP publishing (Claude Code + Webflow MCP) ---
  python orchestrator.py mcp-publish-single 52  # Prepare queue file for article 52, then publish via MCP
  python orchestrator.py mcp-publish            # Prepare + publish all DL articles via MCP
"""
import asyncio
import json
import logging
import sys
import time
from collections import defaultdict
from pathlib import Path

import config
from scripts.spreadsheet_reader import read_articles, ArticleRecord
from scripts.gdocs_fetcher import fetch_doc_text
from scripts.state_manager import (
    load_progress, save_progress, mark_done, mark_failed,
    mark_cluster_done, save_article_result, load_article_result, load_all_article_results
)
from scripts.prompt_builder import (
    load_shared_context, load_agent_definition, make_compact_summary
)
from scripts.claude_runner import evaluate_article, synthesize_cluster
from scripts.response_parser import extract_scores_block, extract_output_block

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# ─── Setup ────────────────────────────────────────────────────────────────────

def setup_dirs():
    config.ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    config.CLUSTERS_DIR.mkdir(parents=True, exist_ok=True)


def load_resources():
    """Load shared context and agent definitions once."""
    shared_context = load_shared_context(config.SHARED_CONTEXT_DIR)
    geo_agent = load_agent_definition(config.AGENTS_DIR, "GEO_EVALUATOR")
    brand_agent = load_agent_definition(config.AGENTS_DIR, "BRAND_REVIEWER")
    cluster_agent = load_agent_definition(config.AGENTS_DIR, "CLUSTER_SYNTHESIZER")
    return shared_context, geo_agent, brand_agent, cluster_agent


# ─── Article Evaluation Phase ─────────────────────────────────────────────────

async def run_article(
    article: ArticleRecord,
    shared_context: str,
    geo_agent: str,
    brand_agent: str,
    semaphore: asyncio.Semaphore,
    state,
    progress_file: Path,
    dry_run: bool = False,
) -> bool:
    """Evaluate a single article. Returns True on success."""
    import aiohttp
    logger.info(f"Starting #{article.item_num}: {article.name!r}")

    # Fetch article text
    async with aiohttp.ClientSession() as session:
        text, fetch_warning = await fetch_doc_text(article.doc_id, session)

    if not text:
        error = fetch_warning or "Empty text returned"
        logger.error(f"  #{article.item_num}: fetch failed — {error}")
        mark_failed(article.item_num, f"fetch_failed: {error}", state)
        save_progress(state, progress_file)
        return False

    if fetch_warning:
        logger.warning(f"  #{article.item_num}: fetch warning — {fetch_warning}")

    if dry_run:
        from scripts.prompt_builder import build_geo_eval_prompt
        system, user = build_geo_eval_prompt(shared_context, geo_agent, article, text)
        print(f"\n{'='*60}")
        print(f"DRY-RUN: Article #{article.item_num} — {article.name}")
        print(f"Text length: {len(text)} chars")
        print(f"--- SYSTEM PROMPT (first 500 chars) ---")
        print(system[:500])
        print(f"--- USER MESSAGE (first 500 chars) ---")
        print(user[:500])
        return True

    # Evaluate
    try:
        result = await evaluate_article(
            article=article,
            text=text,
            fetch_warning=fetch_warning,
            shared_context=shared_context,
            geo_agent_def=geo_agent,
            brand_agent_def=brand_agent,
            semaphore=semaphore,
            geo_model=config.GEO_MODEL,
            brand_model=config.BRAND_MODEL,
            geo_max_tokens=config.MAX_TOKENS_GEO,
            brand_max_tokens=config.MAX_TOKENS_BRAND,
            geo_weights=config.GEO_WEIGHTS,
        )
    except Exception as e:
        logger.error(f"  #{article.item_num}: evaluation failed — {e}")
        mark_failed(article.item_num, str(e), state)
        save_progress(state, progress_file)

        # Save raw error for debugging
        error_path = config.ARTICLES_DIR / f"{article.item_num}-ERROR.txt"
        error_path.write_text(f"Error: {e}\n")
        return False

    # Save result
    save_article_result(result, config.ARTICLES_DIR, article.item_num, article.slug_or_name())
    mark_done(article.item_num, state)
    save_progress(state, progress_file)

    geo = result.get("geo_composite", "?")
    brand = result.get("brand_verdict", "?")
    logger.info(f"  #{article.item_num} done — GEO: {geo}, Brand: {brand}")
    return True


async def run_articles(
    articles: list[ArticleRecord],
    shared_context: str,
    geo_agent: str,
    brand_agent: str,
    state,
    progress_file: Path,
    dry_run: bool = False,
    single_item: str = None,
):
    """Run evaluation for all pending articles (or a single one)."""
    semaphore = asyncio.Semaphore(config.MAX_CONCURRENT_ARTICLES)

    if single_item:
        pending = [a for a in articles if a.item_num == single_item]
        if not pending:
            logger.error(f"Article #{single_item} not found")
            return
    else:
        done_set = set(state.done)
        pending = [a for a in articles if a.item_num not in done_set]

    if not pending:
        logger.info("No pending articles to evaluate.")
        return

    logger.info(f"Evaluating {len(pending)} articles (max {config.MAX_CONCURRENT_ARTICLES} concurrent)...")

    if dry_run:
        # Dry-run: process first 3 sequentially
        for article in pending[:3]:
            await run_article(article, shared_context, geo_agent, brand_agent,
                              semaphore, state, progress_file, dry_run=True)
        return

    # Async batch evaluation
    tasks = [
        run_article(article, shared_context, geo_agent, brand_agent,
                    semaphore, state, progress_file, dry_run=False)
        for article in pending
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    success = sum(1 for r in results if r is True)
    failed = sum(1 for r in results if r is not True)
    logger.info(f"Article evaluation complete: {success} succeeded, {failed} failed")


# ─── Cluster Synthesis Phase ──────────────────────────────────────────────────

async def run_cluster_synthesis(
    articles: list[ArticleRecord],
    shared_context: str,
    cluster_agent: str,
    state,
    progress_file: Path,
):
    """Run cluster and sub-cluster synthesis after all articles are evaluated."""
    semaphore = asyncio.Semaphore(3)  # lighter load for synthesis

    # Group articles by cluster and sub-cluster
    by_cluster = defaultdict(list)
    by_sub = defaultdict(list)

    for article in articles:
        result = load_article_result(config.ARTICLES_DIR, article.item_num)
        if result:
            by_cluster[article.cluster].append(result)
            by_sub[(article.cluster, article.sub_cluster)].append(result)

    all_cluster_results = []

    # Cluster-level synthesis
    for cluster_name, results in sorted(by_cluster.items()):
        key = cluster_name
        if key in state.cluster_done:
            logger.info(f"Cluster '{cluster_name}' already done, loading from disk")
            saved = _load_cluster_result(cluster_name, None)
            if saved:
                all_cluster_results.append(saved)
            continue

        logger.info(f"Synthesizing cluster: {cluster_name} ({len(results)} articles)")
        summaries = [make_compact_summary(r) for r in results]
        try:
            cluster_result = await synthesize_cluster(
                cluster_name=cluster_name,
                sub_cluster_name=None,
                article_summaries=summaries,
                shared_context=shared_context,
                cluster_agent_def=cluster_agent,
                semaphore=semaphore,
                model=config.CLUSTER_MODEL,
                max_tokens=config.MAX_TOKENS_CLUSTER,
            )
            cluster_result["sub_cluster"] = None
            _save_cluster_result(cluster_result, cluster_name, None)
            mark_cluster_done(key, state)
            save_progress(state, progress_file)
            all_cluster_results.append(cluster_result)
            logger.info(f"  {cluster_name}: avg GEO {cluster_result.get('avg_geo_composite', '?')}")
        except Exception as e:
            logger.error(f"  Cluster synthesis failed for {cluster_name}: {e}")

    # Sub-cluster synthesis
    for (cluster_name, sub_cluster_name), results in sorted(by_sub.items()):
        key = f"{cluster_name}/{sub_cluster_name}"
        if key in state.cluster_done:
            saved = _load_cluster_result(cluster_name, sub_cluster_name)
            if saved:
                all_cluster_results.append(saved)
            continue

        logger.info(f"Synthesizing sub-cluster: {key} ({len(results)} articles)")
        summaries = [make_compact_summary(r) for r in results]
        try:
            result = await synthesize_cluster(
                cluster_name=cluster_name,
                sub_cluster_name=sub_cluster_name,
                article_summaries=summaries,
                shared_context=shared_context,
                cluster_agent_def=cluster_agent,
                semaphore=semaphore,
                model=config.CLUSTER_MODEL,
                max_tokens=config.MAX_TOKENS_CLUSTER,
            )
            result["sub_cluster"] = sub_cluster_name
            _save_cluster_result(result, cluster_name, sub_cluster_name)
            mark_cluster_done(key, state)
            save_progress(state, progress_file)
            all_cluster_results.append(result)
            logger.info(f"  {key}: avg GEO {result.get('avg_geo_composite', '?')}")
        except Exception as e:
            logger.error(f"  Sub-cluster synthesis failed for {key}: {e}")

    return all_cluster_results


def _save_cluster_result(result: dict, cluster: str, sub_cluster: str | None):
    config.CLUSTERS_DIR.mkdir(parents=True, exist_ok=True)
    safe = lambda s: s.lower().replace(" ", "-").replace("/", "-") if s else "all"
    fname = f"{safe(cluster)}__{safe(sub_cluster)}.json"
    path = config.CLUSTERS_DIR / fname
    path.write_text(json.dumps(result, indent=2))


def _load_cluster_result(cluster: str, sub_cluster: str | None) -> dict | None:
    safe = lambda s: s.lower().replace(" ", "-").replace("/", "-") if s else "all"
    fname = f"{safe(cluster)}__{safe(sub_cluster)}.json"
    path = config.CLUSTERS_DIR / fname
    if path.exists():
        return json.loads(path.read_text())
    return None


def load_all_cluster_results() -> list[dict]:
    results = []
    for path in sorted(config.CLUSTERS_DIR.glob("*.json")):
        results.append(json.loads(path.read_text()))
    return results


# ─── Sheets Output ────────────────────────────────────────────────────────────

def write_to_sheets(article_results: list[dict], cluster_results: list[dict]):
    if not config.GOOGLE_SERVICE_ACCOUNT_JSON:
        logger.error("GOOGLE_SERVICE_ACCOUNT_JSON not set in .env — cannot write to Sheets")
        return

    from scripts.sheets_writer import write_all_results
    run_metadata = {
        "Run Date": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
        "Total Articles Evaluated": len(article_results),
        "GEO Evaluation Model": config.GEO_MODEL,
        "Brand Evaluation Model": config.BRAND_MODEL,
        "Avg GEO Composite": round(
            sum(r.get("geo_composite", 0) or 0 for r in article_results) / max(len(article_results), 1), 1
        ),
        "Avg QAPEDS Composite": round(
            sum(r.get("qapeds_composite", 0) or 0 for r in article_results) / max(len(article_results), 1), 1
        ),
        "Articles with Brand FAIL": sum(1 for r in article_results if r.get("brand_verdict") == "FAIL"),
        "Articles AIO Ready": sum(1 for r in article_results if r.get("platform_flags", {}).get("aio_ready")),
        "Articles ChatGPT Ready": sum(1 for r in article_results if r.get("platform_flags", {}).get("chatgpt_ready")),
        "Articles Perplexity Ready": sum(1 for r in article_results if r.get("platform_flags", {}).get("perplexity_ready")),
    }

    url = write_all_results(
        service_account_json=config.GOOGLE_SERVICE_ACCOUNT_JSON,
        sheet_name=config.GOOGLE_SHEET_NAME,
        share_email=config.SHARE_EMAIL,
        article_results=article_results,
        cluster_results=cluster_results,
        run_metadata=run_metadata,
        sheet_id=config.GOOGLE_SHEET_ID,
    )
    print(f"\nGoogle Sheet: {url}")


# ─── CLI Commands ─────────────────────────────────────────────────────────────

def cmd_status():
    articles = read_articles(config.XLSX_PATH)
    item_nums = [a.item_num for a in articles]
    state = load_progress(config.PROGRESS_FILE, item_nums)
    print(f"\nPipeline Status")
    print(f"  Total articles: {len(articles)}")
    print(f"  Done:    {len(state.done)}")
    print(f"  Pending: {len(state.pending)}")
    print(f"  Failed:  {len(state.failed)}")
    if state.failed:
        print("\nFailed articles:")
        for num, err in state.failed.items():
            print(f"  #{num}: {err}")
    print(f"\n  Cluster synthesis done: {state.cluster_done}")
    print(f"  Last updated: {state.last_updated or 'never'}")


def cmd_run(resume: bool = False, dry_run: bool = False, single: str = None):
    setup_dirs()
    articles = read_articles(config.XLSX_PATH)
    logger.info(f"Loaded {len(articles)} articles from spreadsheet")

    item_nums = [a.item_num for a in articles]
    state = load_progress(config.PROGRESS_FILE, item_nums)

    if not resume and not single and not dry_run:
        if state.done:
            logger.warning(f"{len(state.done)} articles already evaluated. Use 'resume' to skip them, or delete outputs/progress.json to restart.")

    shared_context, geo_agent, brand_agent, cluster_agent = load_resources()

    # Phase 1: Article evaluation
    asyncio.run(run_articles(
        articles, shared_context, geo_agent, brand_agent, state, config.PROGRESS_FILE,
        dry_run=dry_run, single_item=single,
    ))

    if dry_run or single:
        return

    # Phase 2: Cluster synthesis
    logger.info("Starting cluster synthesis...")
    cluster_results = asyncio.run(run_cluster_synthesis(
        articles, shared_context, cluster_agent, state, config.PROGRESS_FILE,
    ))

    # Phase 3: Write to Sheets
    article_results = load_all_article_results(config.ARTICLES_DIR, [a.item_num for a in articles])
    logger.info(f"Writing {len(article_results)} article results + {len(cluster_results)} cluster results to Sheets")
    write_to_sheets(article_results, cluster_results)

    # Summary
    failed = len(state.failed)
    print(f"\nDone. {len(state.done)}/37 articles evaluated, {failed} failed.")
    if failed:
        print(f"Re-run with 'resume' to retry failed articles.")


def cmd_sheets_only():
    """Write existing results to Sheets without re-evaluating."""
    articles = read_articles(config.XLSX_PATH)
    article_results = load_all_article_results(config.ARTICLES_DIR, [a.item_num for a in articles])
    cluster_results = load_all_cluster_results()
    logger.info(f"Writing {len(article_results)} articles + {len(cluster_results)} clusters to Sheets")
    write_to_sheets(article_results, cluster_results)


def cmd_clusters_only():
    """Run cluster synthesis only (articles must already be evaluated)."""
    setup_dirs()
    articles = read_articles(config.XLSX_PATH)
    state = load_progress(config.PROGRESS_FILE, [a.item_num for a in articles])
    _, _, _, cluster_agent = load_resources()
    shared_context = load_shared_context(config.SHARED_CONTEXT_DIR)

    cluster_results = asyncio.run(run_cluster_synthesis(
        articles, shared_context, cluster_agent, state, config.PROGRESS_FILE,
    ))
    logger.info(f"Cluster synthesis complete: {len(cluster_results)} groups")


async def _rerun_brand_single(
    article: ArticleRecord,
    shared_context: str,
    brand_agent: str,
    semaphore: asyncio.Semaphore,
) -> bool:
    """Re-run brand evaluation only for one article, merging result back into existing JSON."""
    import aiohttp
    from scripts.claude_runner import call_claude
    from scripts.prompt_builder import build_brand_eval_prompt
    from scripts.response_parser import extract_scores_block, extract_output_block, merge_geo_and_brand

    # Load existing result
    existing = load_article_result(config.ARTICLES_DIR, article.item_num)
    if not existing:
        logger.warning(f"  #{article.item_num}: no existing result found, skipping brand rerun")
        return False

    # Fetch text
    async with aiohttp.ClientSession() as session:
        text, fetch_warning = await fetch_doc_text(article.doc_id, session)
    if not text:
        logger.error(f"  #{article.item_num}: fetch failed for brand rerun")
        return False

    # Brand call only
    brand_system, brand_user = build_brand_eval_prompt(shared_context, brand_agent, article, text)
    try:
        async with semaphore:
            brand_raw = await call_claude(brand_system, brand_user, config.BRAND_MODEL, config.MAX_TOKENS_BRAND)
    except Exception as e:
        logger.error(f"  #{article.item_num}: brand rerun call failed: {e}")
        return False

    try:
        brand_scores = extract_scores_block(brand_raw)
        brand_narrative = extract_output_block(brand_raw)
    except Exception as e:
        logger.warning(f"  #{article.item_num}: brand rerun parse still failed: {e}")
        return False

    # Merge brand score back into existing result
    # We need to rebuild the merged result from the existing GEO scores
    # Strip out old brand data first
    existing.pop("brand_eval_failed", None)
    existing.pop("brand_verdict", None)
    existing.pop("brand_issues", None)
    existing.pop("brand_positive_signals", None)
    if "dimensions" in existing and "brand_voice" in existing["dimensions"]:
        del existing["dimensions"]["brand_voice"]

    merged = merge_geo_and_brand(existing, brand_scores, config.GEO_WEIGHTS)
    merged["brand_narrative"] = brand_narrative

    save_article_result(merged, config.ARTICLES_DIR, article.item_num, article.slug_or_name())
    logger.info(f"  #{article.item_num}: brand rerun done — score {brand_scores.get('brand_score')}, verdict {brand_scores.get('verdict')}")
    return True


def cmd_brand_rerun():
    """Re-run brand evaluation for articles where brand_eval_failed=True."""
    articles = read_articles(config.XLSX_PATH)
    article_map = {a.item_num: a for a in articles}

    # Find articles with brand_eval_failed
    failed_brand = []
    for article in articles:
        result = load_article_result(config.ARTICLES_DIR, article.item_num)
        if result and result.get("brand_eval_failed"):
            failed_brand.append(article)

    if not failed_brand:
        logger.info("No articles with brand_eval_failed=True found.")
        return

    logger.info(f"Re-running brand evaluation for {len(failed_brand)} articles...")
    shared_context = load_shared_context(config.SHARED_CONTEXT_DIR)
    _, _, brand_agent, _ = load_resources()
    semaphore = asyncio.Semaphore(config.MAX_CONCURRENT_ARTICLES)

    async def _run_all():
        tasks = [_rerun_brand_single(a, shared_context, brand_agent, semaphore) for a in failed_brand]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        success = sum(1 for r in results if r is True)
        logger.info(f"Brand rerun complete: {success}/{len(failed_brand)} succeeded")

    asyncio.run(_run_all())


ENHANCE_PROGRESS_FILE = config.OUTPUTS_DIR / "enhance_progress.json"


def _load_enhance_progress() -> dict:
    """Load enhance_progress.json → {item_num: {status, doc_url, timestamp}}."""
    if ENHANCE_PROGRESS_FILE.exists():
        with open(ENHANCE_PROGRESS_FILE) as f:
            return json.load(f)
    return {}


def _save_enhance_progress(progress: dict):
    """Atomic write of enhance_progress.json."""
    tmp = ENHANCE_PROGRESS_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(progress, f, indent=2)
    tmp.replace(ENHANCE_PROGRESS_FILE)


def _update_env_folder_id(folder_id: str):
    """Persist GDRIVE_ENHANCED_FOLDER_ID back into .env so subsequent runs reuse the folder."""
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        return
    text = env_path.read_text()
    if "GDRIVE_ENHANCED_FOLDER_ID=" in text:
        import re
        text = re.sub(r"GDRIVE_ENHANCED_FOLDER_ID=.*", f"GDRIVE_ENHANCED_FOLDER_ID={folder_id}", text)
    else:
        text += f"\nGDRIVE_ENHANCED_FOLDER_ID={folder_id}\n"
    env_path.write_text(text)
    logger.info(f"Saved GDRIVE_ENHANCED_FOLDER_ID={folder_id} to .env")


async def _enhance_single_article(
    article: "ArticleRecord",
    article_result: dict,
    enhancer_agent: str,
    enhanced_dir: Path,
    enhance_progress: dict,
    semaphore: asyncio.Semaphore,
):
    """Fetch, enhance, and save one article locally. Updates enhance_progress in place."""
    import aiohttp
    from scripts.claude_runner import enhance_article

    item_num = article.item_num
    name = article_result.get("name", article.item_num)
    slug = article.slug_or_name()

    # Fetch original text
    async with aiohttp.ClientSession() as session:
        text, fetch_warning = await fetch_doc_text(article.doc_id, session)

    if not text:
        logger.error(f"  #{item_num}: fetch failed — skipping enhancement")
        enhance_progress[item_num] = {"status": "failed", "error": "fetch failed", "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        _save_enhance_progress(enhance_progress)
        return

    # Call enhancement agent
    try:
        enhanced_md, changes_log = await enhance_article(
            article_result=article_result,
            article_text=text,
            enhancer_agent_def=enhancer_agent,
            semaphore=semaphore,
            model=config.ENHANCER_MODEL,
            max_tokens=config.MAX_TOKENS_ENHANCER,
        )
    except Exception as e:
        logger.error(f"  #{item_num}: enhancement call failed: {e}")
        enhance_progress[item_num] = {"status": "failed", "error": str(e), "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        _save_enhance_progress(enhance_progress)
        return

    # Save locally as markdown
    filename = f"{item_num}-{slug}-enhanced.md"
    local_path = enhanced_dir / filename
    full_content = enhanced_md
    if changes_log:
        full_content += f"\n\n---\n## Enhancement changes log\n{changes_log}"
    local_path.write_text(full_content, encoding="utf-8")

    # Persist local path into article result JSON
    article_result["enhanced_local_path"] = str(local_path)
    article_result["enhanced_changes_log"] = changes_log
    save_article_result(article_result, config.ARTICLES_DIR, item_num, slug)

    enhance_progress[item_num] = {
        "status": "done",
        "local_path": str(local_path),
        "name": name,
        "changes_log": changes_log,
        "enhanced_md": enhanced_md,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    _save_enhance_progress(enhance_progress)
    logger.info(f"  #{item_num}: enhanced → {filename}")


def _write_enhanced_to_sheets(result_map: dict, enhance_progress: dict, enhanced_dir: Path):
    """Write enhanced article content to 'Enhanced Articles' tab in the existing Google Sheet."""
    if not config.GOOGLE_SERVICE_ACCOUNT_JSON or not config.GOOGLE_SHEET_ID:
        logger.warning("Sheets credentials not configured — skipping sheet write")
        return

    from scripts.sheets_writer import get_sheets_client

    ENHANCED_HEADERS = [
        "Item #", "Article Name", "Cluster", "Sub-Cluster",
        "GEO Score (Pre-Enhancement)", "Brand Verdict",
        "Enhanced Content (Markdown)", "Changes Log",
        "Enhanced At",
    ]

    done_items = {k: v for k, v in enhance_progress.items()
                  if not k.startswith("__") and v.get("status") == "done"}

    if not done_items:
        return

    rows = []
    for item_num, ep in sorted(done_items.items()):
        result = result_map.get(item_num, {})
        enhanced_md = ep.get("enhanced_md", "")
        # Load from file if not cached in progress
        if not enhanced_md:
            lp = ep.get("local_path", "")
            if lp and Path(lp).exists():
                enhanced_md = Path(lp).read_text(encoding="utf-8")

        rows.append([
            item_num,
            result.get("name", ""),
            result.get("cluster", ""),
            result.get("sub_cluster", ""),
            str(result.get("geo_composite", "")),
            result.get("brand_verdict", ""),
            enhanced_md,
            ep.get("changes_log", ""),
            ep.get("timestamp", ""),
        ])

    try:
        import gspread
        gc = get_sheets_client(config.GOOGLE_SERVICE_ACCOUNT_JSON)
        spreadsheet = gc.open_by_key(config.GOOGLE_SHEET_ID)

        try:
            ws = spreadsheet.worksheet("Enhanced Articles")
            spreadsheet.values_clear("'Enhanced Articles'!A2:ZZ")
        except gspread.WorksheetNotFound:
            ws = spreadsheet.add_worksheet(title="Enhanced Articles", rows=200, cols=len(ENHANCED_HEADERS) + 2)
            ws.append_row(ENHANCED_HEADERS, value_input_option="RAW")

        if rows:
            ws.append_rows(rows, value_input_option="RAW")
        logger.info(f"Wrote {len(rows)} enhanced rows to 'Enhanced Articles' tab")
    except Exception as e:
        logger.warning(f"Could not write enhanced tab to Sheets: {e}")


def cmd_enhance(single_item: str | None = None):
    """Apply AEO fixes to evaluated articles and write enhanced versions to Google Drive."""
    if not config.GOOGLE_SERVICE_ACCOUNT_JSON:
        logger.error("GOOGLE_SERVICE_ACCOUNT_JSON not set in .env")
        return

    setup_dirs()
    articles = read_articles(config.XLSX_PATH)
    article_map = {a.item_num: a for a in articles}

    # Load all evaluated results
    all_results = load_all_article_results(config.ARTICLES_DIR, [a.item_num for a in articles])
    result_map = {r["item_num"]: r for r in all_results}

    # Filter scope
    if single_item:
        if single_item not in result_map:
            logger.error(f"No evaluated result found for item #{single_item}")
            return
        to_enhance = [single_item]
    else:
        to_enhance = list(result_map.keys())

    # Skip already-enhanced
    enhance_progress = _load_enhance_progress()
    pending = [n for n in to_enhance if enhance_progress.get(n, {}).get("status") != "done"]

    if not pending:
        logger.info("All articles already enhanced.")
        folder_id = enhance_progress.get("__folder_id__", "")
        if folder_id:
            print(f"\nDrive folder: https://drive.google.com/drive/folders/{folder_id}")
        return

    logger.info(f"Enhancing {len(pending)} articles (skipping {len(to_enhance) - len(pending)} already done)")

    # Load enhancer agent
    enhancer_agent = load_agent_definition(config.AGENTS_DIR, "CONTENT_ENHANCER")

    # Ensure local output dir exists
    enhanced_dir = config.OUTPUTS_DIR / "enhanced"
    enhanced_dir.mkdir(exist_ok=True)

    semaphore = asyncio.Semaphore(config.MAX_CONCURRENT_ENHANCE)

    async def _run_all():
        tasks = []
        for item_num in pending:
            article = article_map.get(item_num)
            result = result_map.get(item_num)
            if not article or not result:
                logger.warning(f"  #{item_num}: missing article record or result — skipping")
                continue
            tasks.append(_enhance_single_article(
                article, result, enhancer_agent,
                enhanced_dir, enhance_progress, semaphore,
            ))
        await asyncio.gather(*tasks, return_exceptions=True)

    asyncio.run(_run_all())

    done_count = sum(1 for n in pending if enhance_progress.get(n, {}).get("status") == "done")
    failed_count = len(pending) - done_count
    logger.info(f"Enhancement complete: {done_count} done, {failed_count} failed")

    # Write enhanced content to a new tab in the existing Google Sheet
    if done_count > 0:
        _write_enhanced_to_sheets(result_map, enhance_progress, enhanced_dir)

    print(f"\nEnhanced files: {enhanced_dir}")
    print(f"Google Sheet (Enhanced Articles tab): https://docs.google.com/spreadsheets/d/{config.GOOGLE_SHEET_ID}")
    if failed_count:
        print(f"Re-run 'python orchestrator.py enhance' to retry {failed_count} failed articles.")


def cmd_drive_audit():
    """Audit service account Drive storage — read-only, no changes made."""
    from scripts.gdocs_writer import get_drive_service, audit_storage

    drive_service = get_drive_service(config.GOOGLE_SERVICE_ACCOUNT_JSON)
    info = audit_storage(drive_service)

    def _fmt(b):
        if b >= 1_073_741_824:
            return f"{b / 1_073_741_824:.2f} GB"
        if b >= 1_048_576:
            return f"{b / 1_048_576:.1f} MB"
        return f"{b / 1024:.1f} KB"

    limit = info["limit_bytes"]
    used = info["used_bytes"]
    free = limit - used if limit else 0

    print(f"\nService account: {info['user_email']}")
    print(f"Storage limit : {_fmt(limit)}")
    print(f"Used          : {_fmt(used)} ({100*used/limit:.1f}%)" if limit else f"Used: {_fmt(used)}")
    print(f"Free          : {_fmt(free)}")
    print(f"\nTop files by size ({len(info['files'])} shown):")
    for f in info["files"][:20]:
        size = int(f.get("size", 0))
        print(f"  {_fmt(size):>10}  {f['mimeType'].split('.')[-1]:<20}  {f['name'][:60]}")


def _process_gdoc_single(
    article: "ArticleRecord",
    article_result: dict,
    drive_service,
    docs_service,
    folder_id: str,
    enhanced_dir: Path,
    gdoc_progress: dict,
):
    """Copy original doc → apply fixes → transfer ownership. Synchronous (one at a time)."""
    from scripts.spreadsheet_reader import extract_doc_id
    from scripts.gdocs_writer import (
        copy_doc, apply_text_replacements, append_aeo_section, transfer_ownership
    )
    from scripts.md_to_docx import extract_structural_additions, build_brand_replacements

    item_num = article.item_num
    slug = article.slug_or_name()
    name = article_result.get("name", item_num)
    new_title = f"{item_num}-{slug}-aeo-updated"

    # Get source doc id
    gdoc_url = article_result.get("gdoc_url", "")
    source_doc_id = extract_doc_id(gdoc_url) if gdoc_url else None
    if not source_doc_id:
        logger.error(f"  #{item_num}: no gdoc_url — cannot copy")
        gdoc_progress[item_num] = {"status": "failed", "error": "no gdoc_url"}
        return

    # 1. Copy original doc
    try:
        new_doc_id = copy_doc(drive_service, source_doc_id, new_title, folder_id)
    except Exception as e:
        logger.error(f"  #{item_num}: copy failed: {e}")
        gdoc_progress[item_num] = {"status": "failed", "error": f"copy: {e}"}
        return

    # 2. Build text replacements from brand issues + citation changes
    brand_issues = article_result.get("brand_issues", [])
    replacements = build_brand_replacements(brand_issues)

    # Load enhanced md for citation replacements and structural additions
    enhanced_file = enhanced_dir / f"{item_num}-{slug}-enhanced.md"
    enhanced_md = enhanced_file.read_text(encoding="utf-8") if enhanced_file.exists() else ""
    changes_log = article_result.get("enhanced_changes_log", "")

    if enhanced_md:
        additions = extract_structural_additions(enhanced_md, changes_log)
        replacements.extend(additions["citation_replacements"])
    else:
        additions = {"faq_section": "", "canonical_answer": ""}

    # Apply text replacements
    if replacements:
        try:
            apply_text_replacements(docs_service, new_doc_id, replacements)
        except Exception as e:
            logger.warning(f"  #{item_num}: text replacements partially failed: {e}")

    # 3. Append structural additions
    aeo_additions = "\n\n".join(filter(None, [
        additions.get("faq_section", ""),
        additions.get("canonical_answer", ""),
    ]))
    if aeo_additions:
        try:
            append_aeo_section(docs_service, new_doc_id, aeo_additions)
        except Exception as e:
            logger.warning(f"  #{item_num}: append section failed: {e}")

    # 4. Transfer ownership to share_email
    transferred = transfer_ownership(drive_service, new_doc_id, config.SHARE_EMAIL)

    doc_url = f"https://docs.google.com/document/d/{new_doc_id}/edit"
    article_result["enhanced_gdoc_url"] = doc_url
    save_article_result(article_result, config.ARTICLES_DIR, item_num, slug)

    gdoc_progress[item_num] = {
        "status": "done",
        "doc_url": doc_url,
        "ownership_transferred": transferred,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    status = "ownership transferred" if transferred else "writer access granted"
    logger.info(f"  #{item_num}: {doc_url} ({status})")


GDOC_PROGRESS_FILE = config.OUTPUTS_DIR / "gdoc_progress.json"


def _load_gdoc_progress() -> dict:
    if GDOC_PROGRESS_FILE.exists():
        with open(GDOC_PROGRESS_FILE) as f:
            return json.load(f)
    return {}


def _save_gdoc_progress(progress: dict):
    tmp = GDOC_PROGRESS_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(progress, f, indent=2)
    tmp.replace(GDOC_PROGRESS_FILE)


def cmd_enhance_gdocs(single_item: str | None = None):
    """Copy originals → apply AEO fixes → transfer ownership to chandan@quizizz.com."""
    if not config.GOOGLE_SERVICE_ACCOUNT_JSON:
        logger.error("GOOGLE_SERVICE_ACCOUNT_JSON not set in .env")
        return

    setup_dirs()
    articles = read_articles(config.XLSX_PATH)
    article_map = {a.item_num: a for a in articles}
    all_results = load_all_article_results(config.ARTICLES_DIR, [a.item_num for a in articles])
    result_map = {r["item_num"]: r for r in all_results}

    if single_item:
        if single_item not in result_map:
            logger.error(f"No result found for item #{single_item}")
            return
        to_process = [single_item]
    else:
        to_process = list(result_map.keys())

    gdoc_progress = _load_gdoc_progress()
    pending = [n for n in to_process if gdoc_progress.get(n, {}).get("status") != "done"]

    if not pending:
        folder_id = gdoc_progress.get("__folder_id__", config.GDRIVE_ENHANCED_FOLDER_ID)
        print(f"All articles already processed.")
        if folder_id:
            print(f"Drive folder: https://drive.google.com/drive/folders/{folder_id}")
        return

    logger.info(f"Processing {len(pending)} articles via copy→edit→transfer")

    from scripts.gdocs_writer import get_drive_service, get_docs_service, get_or_create_folder

    drive_service = get_drive_service(config.GOOGLE_SERVICE_ACCOUNT_JSON)
    docs_service = get_docs_service(config.GOOGLE_SERVICE_ACCOUNT_JSON)

    folder_id = config.GDRIVE_ENHANCED_FOLDER_ID
    if not folder_id:
        folder_id = get_or_create_folder(drive_service, config.GDRIVE_ENHANCED_FOLDER_NAME, config.SHARE_EMAIL)
        _update_env_folder_id(folder_id)

    gdoc_progress["__folder_id__"] = folder_id
    _save_gdoc_progress(gdoc_progress)

    enhanced_dir = config.OUTPUTS_DIR / "enhanced"

    done = 0
    failed = 0
    for item_num in pending:
        article = article_map.get(item_num)
        result = result_map.get(item_num)
        if not article or not result:
            logger.warning(f"  #{item_num}: missing record — skipping")
            continue
        _process_gdoc_single(
            article, result, drive_service, docs_service,
            folder_id, enhanced_dir, gdoc_progress,
        )
        _save_gdoc_progress(gdoc_progress)
        if gdoc_progress.get(item_num, {}).get("status") == "done":
            done += 1
        else:
            failed += 1
        time.sleep(0.5)  # gentle rate limiting between docs

    logger.info(f"enhance-gdocs complete: {done} done, {failed} failed")
    print(f"\nDrive folder: https://drive.google.com/drive/folders/{folder_id}")
    if failed:
        print(f"Re-run 'python orchestrator.py enhance-gdocs' to retry {failed} failed articles.")


def cmd_webflow_setup():
    """List Webflow collections to help find collection IDs."""
    from scripts.webflow_stub import WebflowPublisher
    publisher = WebflowPublisher(
        api_token=config.WEBFLOW_API_TOKEN,
        site_id=config.WEBFLOW_SITE_ID,
    )
    if not publisher.enabled:
        print("Webflow credentials not configured. Set WEBFLOW_API_TOKEN and WEBFLOW_SITE_ID in .env")
        return
    collections = asyncio.run(publisher.list_collections())
    print(f"\nWebflow Collections for site {config.WEBFLOW_SITE_ID}:")
    for c in collections:
        print(f"  ID: {c.get('id')}  Name: {c.get('displayName', c.get('name', '?'))}")
    print("\nAdd the relevant collection IDs to your .env file.")
    print("\nRequired .env entries:")
    print("  WEBFLOW_COLLECTION_DIFFERENTIATED_LEARNING=<id>")
    print("  WEBFLOW_COLLECTION_SCAFFOLDING=<id>")
    print("  WEBFLOW_COLLECTION_ENGAGEMENT=<id>")


def cmd_webflow_mcp_export():
    """
    Build Webflow CMS field payloads for all enhanced articles and write to
    outputs/webflow_payloads.json for use with Webflow MCP tools.

    No API token required — Python handles data extraction + MD→HTML conversion;
    Claude Code's Webflow MCP handles authenticated API calls.
    """
    from scripts.webflow_payload_builder import main as run_builder
    run_builder()


def cmd_mcp_publish_single(item_num: str):
    """
    Prepare publish queue file for one article and print MCP publish instructions.
    Actual MCP calls (create FAQ items + article item) are made by Claude Code.
    """
    from scripts.mcp_publisher import cmd_prepare_single
    cmd_prepare_single(item_num)


def cmd_mcp_publish_all():
    """
    Prepare publish queue files for all DL articles.
    Actual MCP calls are made by Claude Code reading outputs/publish_queue/*.json.
    """
    from scripts.mcp_publisher import cmd_prepare_all
    cmd_prepare_all()


# ─── Step 1: Improvement Delta ────────────────────────────────────────────────

def cmd_improvement_delta():
    """Build improvement delta for all enhanced articles and write to Sheets."""
    import json as _json
    from scripts.delta_builder import build_improvement_delta
    from scripts.sheets_writer import get_sheets_client, get_or_create_spreadsheet, write_improvement_delta_tab

    all_results = [
        _json.load(open(f)) for f in sorted(config.ARTICLES_DIR.glob("*.json"))
    ]

    enhanced = [r for r in all_results if r.get("enhanced_changes_log")]
    if not enhanced:
        logger.error("No enhanced articles found. Run 'python orchestrator.py enhance' first.")
        return

    logger.info(f"Building improvement deltas for {len(enhanced)} articles...")
    deltas = [build_improvement_delta(r) for r in enhanced]
    deltas.sort(key=lambda d: d.get("item_num", ""))

    # Print summary
    for d in deltas:
        dims = ", ".join(d.get("dims_improved", [])) or "none"
        print(f"  #{d['item_num']}: {d['changes_count']} changes → dims improved: {dims}")

    # Write to Sheets
    if config.GOOGLE_SERVICE_ACCOUNT_JSON and config.GOOGLE_SHEET_ID:
        try:
            gc = get_sheets_client(config.GOOGLE_SERVICE_ACCOUNT_JSON)
            spreadsheet = get_or_create_spreadsheet(gc, config.GOOGLE_SHEET_NAME, sheet_id=config.GOOGLE_SHEET_ID)
            write_improvement_delta_tab(spreadsheet, deltas)
            print(f"\nSheet: https://docs.google.com/spreadsheets/d/{config.GOOGLE_SHEET_ID}")
        except Exception as e:
            logger.warning(f"Could not write to Sheets: {e}")
    else:
        logger.warning("GOOGLE_SERVICE_ACCOUNT_JSON or GOOGLE_SHEET_ID not set — skipping Sheets write")

    logger.info(f"Improvement delta complete: {len(deltas)} articles processed")


# ─── Step 2: Continuity Check ─────────────────────────────────────────────────

def cmd_continuity_check():
    """Run structural continuity checks on all enhanced articles and write to Sheets."""
    from scripts.continuity_checker import check_continuity
    from scripts.sheets_writer import get_sheets_client, get_or_create_spreadsheet, write_continuity_tab
    import aiohttp

    articles = read_articles(config.XLSX_PATH)
    article_map = {a.item_num: a for a in articles}
    all_results = load_all_article_results(config.ARTICLES_DIR, [a.item_num for a in articles])
    result_map = {r["item_num"]: r for r in all_results}

    enhanced_dir = config.OUTPUTS_DIR / "enhanced"
    enhanced_files = {
        f.stem.split("-enhanced")[0]: f
        for f in enhanced_dir.glob("*-enhanced.md")
    }

    continuity_results = []

    async def _fetch_and_check(item_num: str, result: dict):
        article = article_map.get(item_num)
        if not article:
            return

        # Find enhanced file
        slug = article.slug_or_name()
        key = f"{item_num}-{slug}"
        enh_file = enhanced_files.get(key)
        if not enh_file:
            logger.warning(f"  #{item_num}: no enhanced file found — skipping")
            return
        enhanced_md = enh_file.read_text(encoding="utf-8")

        # Fetch original text
        async with aiohttp.ClientSession() as session:
            original_text, _ = await fetch_doc_text(article.doc_id, session)

        if not original_text:
            logger.warning(f"  #{item_num}: fetch failed — skipping continuity check")
            return

        check = check_continuity(original_text, enhanced_md, article_name=result.get("name", ""))
        check["item_num"] = item_num
        check["name"] = result.get("name", "")
        continuity_results.append(check)
        logger.info(f"  #{item_num}: {check['overall']} — {'; '.join(check['notes'][:2]) or 'OK'}")

    async def _run_all():
        semaphore = asyncio.Semaphore(config.MAX_CONCURRENT_ARTICLES)
        async def _bounded(item_num, result):
            async with semaphore:
                await _fetch_and_check(item_num, result)
        tasks = [_bounded(n, r) for n, r in result_map.items() if r.get("enhanced_local_path")]
        await asyncio.gather(*tasks, return_exceptions=True)

    logger.info("Running continuity checks (fetching originals)...")
    asyncio.run(_run_all())
    continuity_results.sort(key=lambda r: r.get("item_num", ""))

    # Summary
    statuses = [r["overall"] for r in continuity_results]
    print(f"\nContinuity check complete: {len(continuity_results)} articles")
    print(f"  PASS: {statuses.count('PASS')}  WARN: {statuses.count('WARN')}  FAIL: {statuses.count('FAIL')}")

    # Write to Sheets
    if config.GOOGLE_SERVICE_ACCOUNT_JSON and config.GOOGLE_SHEET_ID:
        try:
            gc = get_sheets_client(config.GOOGLE_SERVICE_ACCOUNT_JSON)
            spreadsheet = get_or_create_spreadsheet(gc, config.GOOGLE_SHEET_NAME, sheet_id=config.GOOGLE_SHEET_ID)
            write_continuity_tab(spreadsheet, continuity_results)
            print(f"Sheet: https://docs.google.com/spreadsheets/d/{config.GOOGLE_SHEET_ID}")
        except Exception as e:
            logger.warning(f"Could not write to Sheets: {e}")


# ─── Step 3: Teacher Review ───────────────────────────────────────────────────

TEACHER_REVIEW_DIR = config.OUTPUTS_DIR / "teacher_reviews"


def cmd_teacher_review():
    """Run SME/teacher review on all enhanced articles and write results to Sheets."""
    from scripts.claude_runner import teacher_review_article
    from scripts.sheets_writer import get_sheets_client, get_or_create_spreadsheet, write_teacher_review_tab

    TEACHER_REVIEW_DIR.mkdir(exist_ok=True)

    articles = read_articles(config.XLSX_PATH)
    all_results = load_all_article_results(config.ARTICLES_DIR, [a.item_num for a in articles])
    result_map = {r["item_num"]: r for r in all_results}

    enhanced_dir = config.OUTPUTS_DIR / "enhanced"
    teacher_reviewer = load_agent_definition(config.AGENTS_DIR, "TEACHER_REVIEWER")

    # Find all enhanced files
    to_review = []
    for result in all_results:
        if not result.get("enhanced_local_path"):
            continue
        enh_path = Path(result["enhanced_local_path"])
        if not enh_path.exists():
            continue
        # Skip already reviewed (unless rerun)
        review_file = TEACHER_REVIEW_DIR / f"{result['item_num']}-review.json"
        if review_file.exists():
            logger.info(f"  #{result['item_num']}: already reviewed — skipping (delete file to rerun)")
            continue
        to_review.append(result)

    if not to_review:
        logger.info("All articles already reviewed. Delete outputs/teacher_reviews/*.json to rerun.")
    else:
        logger.info(f"Running teacher review on {len(to_review)} articles...")

    semaphore = asyncio.Semaphore(config.MAX_CONCURRENT_TEACHER_REVIEW)
    teacher_reviews = []

    async def _review_one(result: dict):
        item_num = result["item_num"]
        enh_path = Path(result["enhanced_local_path"])
        enhanced_md = enh_path.read_text(encoding="utf-8")

        # Strip the changes log section (appended after ---)
        if "\n---\n## Enhancement changes log" in enhanced_md:
            enhanced_md = enhanced_md.split("\n---\n## Enhancement changes log")[0]

        try:
            review = await teacher_review_article(
                item_num=item_num,
                article_name=result.get("name", ""),
                enhanced_md=enhanced_md,
                teacher_reviewer_def=teacher_reviewer,
                semaphore=semaphore,
                model=config.TEACHER_REVIEWER_MODEL,
                max_tokens=config.MAX_TOKENS_TEACHER_REVIEW,
            )
        except Exception as e:
            logger.error(f"  #{item_num}: teacher review failed: {e}")
            return

        # Save per-article JSON
        review_file = TEACHER_REVIEW_DIR / f"{item_num}-review.json"
        with open(review_file, "w") as f:
            json.dump(review, f, indent=2)

        verdict = review.get("verdict", "?")
        score = review.get("overall_score", "?")
        logger.info(f"  #{item_num}: {verdict} (score={score})")
        return review

    async def _run_all():
        tasks = [_review_one(r) for r in to_review]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for r in results:
            if isinstance(r, dict):
                teacher_reviews.append(r)

    if to_review:
        asyncio.run(_run_all())

    # Load all saved reviews (including previously done)
    all_reviews = []
    for review_file in sorted(TEACHER_REVIEW_DIR.glob("*-review.json")):
        with open(review_file) as f:
            all_reviews.append(json.load(f))

    # Summary
    verdicts = [r.get("verdict", "?") for r in all_reviews]
    print(f"\nTeacher review complete: {len(all_reviews)} articles")
    print(f"  PASS: {verdicts.count('PASS')}  REVISE: {verdicts.count('REVISE')}")

    # Write to Sheets
    if config.GOOGLE_SERVICE_ACCOUNT_JSON and config.GOOGLE_SHEET_ID:
        try:
            gc = get_sheets_client(config.GOOGLE_SERVICE_ACCOUNT_JSON)
            spreadsheet = get_or_create_spreadsheet(gc, config.GOOGLE_SHEET_NAME, sheet_id=config.GOOGLE_SHEET_ID)
            write_teacher_review_tab(spreadsheet, all_reviews)
            print(f"Sheet: https://docs.google.com/spreadsheets/d/{config.GOOGLE_SHEET_ID}")
        except Exception as e:
            logger.warning(f"Could not write to Sheets: {e}")


# ─── Steps 4–6: Webflow Publish ───────────────────────────────────────────────

def cmd_webflow_publish(mode: str = "draft", single_item: str | None = None):
    """
    Publish enhanced articles to Webflow CMS.

    mode="draft"  → create drafts only (safe to run first)
    mode="live"   → create drafts + publish live
    """
    from scripts.webflow_stub import WebflowPublisher, load_webflow_progress, save_webflow_progress

    publisher = WebflowPublisher(
        api_token=config.WEBFLOW_API_TOKEN,
        site_id=config.WEBFLOW_SITE_ID,
        collections=config.WEBFLOW_COLLECTIONS,
    )
    if not publisher.enabled:
        print("Webflow credentials not configured. Set WEBFLOW_API_TOKEN and WEBFLOW_SITE_ID in .env")
        print("Then run: python orchestrator.py webflow-setup")
        return

    articles = read_articles(config.XLSX_PATH)
    all_results = load_all_article_results(config.ARTICLES_DIR, [a.item_num for a in articles])
    result_map = {r["item_num"]: r for r in all_results}

    # Filter scope
    if single_item:
        if single_item not in result_map:
            logger.error(f"No result for item #{single_item}")
            return
        to_publish = [single_item]
    else:
        to_publish = list(result_map.keys())

    # Load progress — skip already published
    progress = load_webflow_progress()
    pending = [n for n in to_publish if progress.get(n, {}).get("status") not in ("draft", "live")]

    if not pending:
        print("All articles already published to Webflow.")
        return

    logger.info(f"Publishing {len(pending)} articles to Webflow (mode={mode})...")

    async def _publish_all():
        semaphore = asyncio.Semaphore(2)  # gentle rate limit for Webflow API

        async def _bounded(item_num: str):
            result = result_map[item_num]
            enh_path_str = result.get("enhanced_local_path", "")
            enhanced_md = ""
            if enh_path_str:
                enh_path = Path(enh_path_str)
                if enh_path.exists():
                    full = enh_path.read_text(encoding="utf-8")
                    # Strip appended changes log
                    if "\n---\n## Enhancement changes log" in full:
                        full = full.split("\n---\n## Enhancement changes log")[0]
                    enhanced_md = full

            async with semaphore:
                pub_result = await publisher.publish_article(result, enhanced_md, mode=mode)

            progress[item_num] = {**pub_result, "item_num": item_num, "name": result.get("name", "")}
            save_webflow_progress(progress)

            status = pub_result.get("status", "?")
            if status in ("draft", "live"):
                logger.info(f"  #{item_num}: {status} — {pub_result.get('item_url', '')}")
            else:
                logger.error(f"  #{item_num}: {status} — {pub_result.get('error', '')}")

        tasks = [_bounded(n) for n in pending]
        await asyncio.gather(*tasks, return_exceptions=True)

    asyncio.run(_publish_all())

    done = [n for n in pending if progress.get(n, {}).get("status") in ("draft", "live")]
    failed = [n for n in pending if progress.get(n, {}).get("status") == "failed"]

    print(f"\nWebflow publish complete: {len(done)} published, {len(failed)} failed")
    if failed:
        print(f"Failed items: {', '.join(failed)}")
        print("Re-run 'python orchestrator.py webflow-publish' to retry.")
    if done:
        print(f"Webflow CMS: https://webflow.com/design/{config.WEBFLOW_SITE_ID}")


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

    if cmd == "run":
        cmd_run(resume=False)
    elif cmd == "resume":
        cmd_run(resume=True)
    elif cmd == "dry-run":
        cmd_run(dry_run=True)
    elif cmd == "status":
        cmd_status()
    elif cmd == "single":
        if len(sys.argv) < 3:
            print("Usage: python orchestrator.py single <item_num>")
            sys.exit(1)
        cmd_run(single=sys.argv[2])
    elif cmd == "clusters":
        cmd_clusters_only()
    elif cmd == "sheets":
        cmd_sheets_only()
    elif cmd == "webflow-setup":
        cmd_webflow_setup()
    elif cmd == "brand-rerun":
        cmd_brand_rerun()
    elif cmd == "drive-audit":
        cmd_drive_audit()
    elif cmd == "enhance-gdocs":
        cmd_enhance_gdocs()
    elif cmd == "enhance-gdocs-single":
        if len(sys.argv) < 3:
            print("Usage: python orchestrator.py enhance-gdocs-single <item_num>")
            sys.exit(1)
        cmd_enhance_gdocs(single_item=sys.argv[2])
    elif cmd == "enhance":
        cmd_enhance()
    elif cmd == "enhance-single":
        if len(sys.argv) < 3:
            print("Usage: python orchestrator.py enhance-single <item_num>")
            sys.exit(1)
        cmd_enhance(single_item=sys.argv[2])
    elif cmd == "improvement-delta":
        cmd_improvement_delta()
    elif cmd == "continuity-check":
        cmd_continuity_check()
    elif cmd == "teacher-review":
        cmd_teacher_review()
    elif cmd == "webflow-publish":
        mode = "live" if "--live" in sys.argv else "draft"
        cmd_webflow_publish(mode=mode)
    elif cmd == "webflow-publish-single":
        if len(sys.argv) < 3:
            print("Usage: python orchestrator.py webflow-publish-single <item_num> [--live]")
            sys.exit(1)
        mode = "live" if "--live" in sys.argv else "draft"
        cmd_webflow_publish(mode=mode, single_item=sys.argv[2])
    elif cmd == "webflow-mcp-export":
        cmd_webflow_mcp_export()
    elif cmd == "mcp-publish-single":
        if len(sys.argv) < 3:
            print("Usage: python orchestrator.py mcp-publish-single <item_num>")
            sys.exit(1)
        cmd_mcp_publish_single(sys.argv[2])
    elif cmd == "mcp-publish":
        cmd_mcp_publish_all()
    else:
        print(__doc__)
