"""Async Claude API calls with retry/backoff."""
import asyncio
import logging

import anthropic

logger = logging.getLogger(__name__)


async def call_claude(
    system: str,
    user_message: str,
    model: str,
    max_tokens: int = 8192,
    semaphore: asyncio.Semaphore | None = None,
    retries: int = 3,
    base_delay: float = 2.0,
) -> str:
    """
    Call Claude API. Returns the text content of the response.
    Retries on rate limit errors with exponential backoff.
    """
    client = anthropic.AsyncAnthropic()

    async def _call() -> str:
        for attempt in range(retries):
            try:
                response = await client.messages.create(
                    model=model,
                    max_tokens=max_tokens,
                    system=system,
                    messages=[{"role": "user", "content": user_message}],
                )
                return response.content[0].text
            except anthropic.RateLimitError as e:
                if attempt < retries - 1:
                    delay = base_delay * (2 ** attempt)
                    logger.warning(f"Rate limit hit; retrying in {delay:.0f}s (attempt {attempt+1}/{retries})")
                    await asyncio.sleep(delay)
                else:
                    raise
            except anthropic.APIStatusError as e:
                if e.status_code >= 500 and attempt < retries - 1:
                    delay = base_delay * (2 ** attempt)
                    logger.warning(f"API error {e.status_code}; retrying in {delay:.0f}s")
                    await asyncio.sleep(delay)
                else:
                    raise
        raise RuntimeError(f"Failed after {retries} retries")

    if semaphore:
        async with semaphore:
            return await _call()
    return await _call()


async def evaluate_article(
    article,
    text: str,
    fetch_warning: str,
    shared_context: str,
    geo_agent_def: str,
    brand_agent_def: str,
    semaphore: asyncio.Semaphore,
    geo_model: str,
    brand_model: str,
    geo_max_tokens: int,
    brand_max_tokens: int,
    geo_weights: dict,
) -> dict:
    """
    Run GEO and brand evaluation concurrently for a single article.
    Returns the merged ArticleResult dict.
    """
    from scripts.prompt_builder import build_geo_eval_prompt, build_brand_eval_prompt
    from scripts.response_parser import (
        extract_scores_block, extract_output_block,
        merge_geo_and_brand, validate_article_result, build_article_output
    )

    geo_system, geo_user = build_geo_eval_prompt(shared_context, geo_agent_def, article, text)
    brand_system, brand_user = build_brand_eval_prompt(shared_context, brand_agent_def, article, text)

    # Run both calls concurrently (within the same semaphore slot for this article)
    try:
        geo_raw, brand_raw = await asyncio.gather(
            call_claude(geo_system, geo_user, geo_model, geo_max_tokens),
            call_claude(brand_system, brand_user, brand_model, brand_max_tokens),
        )
    except Exception as e:
        raise RuntimeError(f"Claude call failed for article #{article.item_num}: {e}") from e

    # Parse GEO scores
    try:
        geo_scores = extract_scores_block(geo_raw)
    except Exception as e:
        raise RuntimeError(f"GEO scores parse failed for #{article.item_num}: {e}") from e

    geo_narrative = extract_output_block(geo_raw)

    # Parse brand scores (soft dependency — failures don't abort pipeline)
    brand_scores = {}
    brand_narrative = ""
    try:
        brand_scores = extract_scores_block(brand_raw)
        brand_narrative = extract_output_block(brand_raw)
    except Exception as e:
        logger.warning(f"Brand scores parse failed for #{article.item_num}: {e} — continuing with brand_eval_failed=True")
        brand_narrative = brand_raw  # store raw for debugging

    # Merge
    merged = merge_geo_and_brand(geo_scores, brand_scores, geo_weights)

    # Validate
    warnings = validate_article_result(merged)
    if warnings:
        logger.warning(f"Validation warnings for #{article.item_num}: {warnings}")
    merged["validation_warnings"] = warnings

    # Build final output
    result = build_article_output(article, merged, geo_narrative, brand_narrative, fetch_warning)

    return result


async def enhance_article(
    article_result: dict,
    article_text: str,
    enhancer_agent_def: str,
    semaphore: asyncio.Semaphore,
    model: str,
    max_tokens: int,
) -> tuple[str, str]:
    """
    Apply AEO fixes to an article using the CONTENT_ENHANCER agent.
    Returns (enhanced_markdown, changes_log).
    """
    import re

    # Build the payload with recommendations + brand issues + checklist
    recs = article_result.get("recommendations", [])
    brand_issues = article_result.get("brand_issues", [])
    checklist = article_result.get("pre_publish_checklist", {})
    geo_composite = article_result.get("geo_composite", "N/A")

    recs_text = "\n".join(
        f"  #{r.get('rank',i+1)} [{r.get('dimension','').upper()}] {r.get('issue','')}\n"
        f"     FIX: {r.get('fix','')}"
        for i, r in enumerate(recs)
    )

    brand_text = "\n".join(
        f"  [{i.get('severity','FAIL')}] {i.get('rule','')}\n"
        f"     Instances: {'; '.join(str(x) for x in i.get('instances', []))}\n"
        f"     FIX: {i.get('fix','')}"
        for i in brand_issues
    ) or "  (none)"

    schema_list = checklist.get("schema_to_add", [])
    checklist_text = (
        f"  schema_to_add: {', '.join(schema_list) if isinstance(schema_list, list) else schema_list}\n"
        f"  title_tag: {checklist.get('title_tag', '')}\n"
        f"  meta_description: {checklist.get('meta_description', '')}\n"
        f"  slug_recommendation: {checklist.get('slug_recommendation', '')}\n"
        f"  geo_composite: {geo_composite}"
    )

    user_message = (
        f"ORIGINAL ARTICLE:\n{article_text}\n\n"
        f"RECOMMENDATIONS (apply in order of rank):\n{recs_text}\n\n"
        f"BRAND ISSUES (fix all):\n{brand_text}\n\n"
        f"PRE-PUBLISH CHECKLIST (append as Editor Notes at bottom):\n{checklist_text}"
    )

    raw = await call_claude(
        system=enhancer_agent_def,
        user_message=user_message,
        model=model,
        max_tokens=max_tokens,
        semaphore=semaphore,
    )

    # Extract <enhanced_article> and <changes_log>
    def extract_tag(tag: str, text: str) -> str:
        m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
        return m.group(1).strip() if m else ""

    enhanced = extract_tag("enhanced_article", raw)
    changes = extract_tag("changes_log", raw)

    if not enhanced:
        raise RuntimeError(f"No <enhanced_article> block found in response for article #{article_result.get('item_num')}")

    return enhanced, changes


async def teacher_review_article(
    item_num: str,
    article_name: str,
    enhanced_md: str,
    teacher_reviewer_def: str,
    semaphore: asyncio.Semaphore,
    model: str,
    max_tokens: int,
) -> dict:
    """
    Run teacher/SME review on one enhanced article.
    Returns parsed review dict with scores, verdict, top_issues, positive_signals, narrative.
    """
    import re

    user_message = (
        f"ARTICLE TITLE: {article_name}\n\n"
        f"ARTICLE CONTENT:\n{enhanced_md}"
    )

    raw = await call_claude(
        system=teacher_reviewer_def,
        user_message=user_message,
        model=model,
        max_tokens=max_tokens,
        semaphore=semaphore,
    )

    # Extract <teacher_review> JSON block
    def extract_tag(tag: str, text: str) -> str:
        m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
        return m.group(1).strip() if m else ""

    review_json_str = extract_tag("teacher_review", raw)
    narrative = extract_tag("output", raw)

    if not review_json_str:
        raise RuntimeError(f"No <teacher_review> block found for #{item_num}")

    import json
    try:
        review_data = json.loads(review_json_str)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse teacher_review JSON for #{item_num}: {e}") from e

    scores = review_data.get("scores", {})
    overall_score = review_data.get("overall_score")
    if overall_score is None and scores:
        vals = [v for v in scores.values() if isinstance(v, (int, float))]
        overall_score = round(sum(vals) / len(vals), 1) if vals else 0.0

    verdict = review_data.get("verdict", "PASS")
    if not verdict:
        verdict = "PASS" if (overall_score or 0) >= 3.5 and all(v >= 3 for v in scores.values() if isinstance(v, (int, float))) else "REVISE"

    return {
        "item_num": item_num,
        "name": article_name,
        "scores": scores,
        "overall_score": overall_score,
        "verdict": verdict,
        "top_issues": review_data.get("top_issues", []),
        "positive_signals": review_data.get("positive_signals", []),
        "narrative": narrative,
    }


async def synthesize_cluster(
    cluster_name: str,
    sub_cluster_name: str | None,
    article_summaries: list[dict],
    shared_context: str,
    cluster_agent_def: str,
    semaphore: asyncio.Semaphore,
    model: str,
    max_tokens: int,
) -> dict:
    """Run cluster synthesis for one cluster or sub-cluster."""
    from scripts.prompt_builder import build_cluster_synthesis_prompt
    from scripts.response_parser import extract_scores_block, extract_output_block

    system, user = build_cluster_synthesis_prompt(
        shared_context, cluster_agent_def, cluster_name, sub_cluster_name, article_summaries
    )

    raw = await call_claude(system, user, model, max_tokens, semaphore)

    try:
        scores = extract_scores_block(raw)
    except Exception as e:
        raise RuntimeError(f"Cluster synthesis parse failed for {cluster_name}/{sub_cluster_name}: {e}") from e

    narrative = extract_output_block(raw)
    return {**scores, "narrative": narrative}
