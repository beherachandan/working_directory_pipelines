"""
Prepare Webflow MCP publishing queue from webflow_payloads.json.

This script handles all data prep — HTML validation, FAQ HTML conversion,
slug dedup checks, size threshold decisions — and writes per-article
publish_queue files. Claude Code then reads those files and makes the
actual Webflow MCP tool calls (create_collection_items, etc.).

Usage (via orchestrator.py):
  python orchestrator.py mcp-publish-single 52   # queue one article, print summary
  python orchestrator.py mcp-publish             # queue all DL articles

After running, open Claude Code and say:
  "publish article 52" or "publish all queued articles"
Claude Code will read outputs/publish_queue/<N>.json and make MCP calls:
  1. create_collection_items (FAQs collection) — one call per article
  2. publish_collection_items (FAQs collection) — publish all FAQ IDs
  3. create_collection_items (DL collection) — one call with faqs:[ids]
  4. publish_collection_items (DL collection) — publish the article ID

IMPORTANT: create alone leaves items as "Queued to publish". publish_collection_items
must be called after create for both FAQs and the article.

Configuration:
  COLLECTION_IDS / CATEGORY_IDS hardcoded below (verified 2026-03-30)
"""

import json
import logging
import re
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

# ── Paths ─────────────────────────────────────────────────────────────────────
_ROOT = Path(__file__).parent.parent
PAYLOADS_PATH = _ROOT / "outputs" / "webflow_payloads.json"
QUEUE_DIR = _ROOT / "outputs" / "publish_queue"
REPORTS_DIR = _ROOT / "outputs" / "publish_reports"
LARGE_CONTENT_DIR = _ROOT / "outputs" / "large_content"

# ── Webflow IDs (all verified 2026-03-30) ─────────────────────────────────────
SITE_ID = "68355113496452bf05789e95"
FAQS_COLLECTION_ID = "6850473a6fb75a92cada401b"
PUBLISHING_DATE = "2026-03-27T00:00:00.000Z"
CONTENT_SIZE_THRESHOLD = 35_000  # bytes

COLLECTION_IDS: dict[str, str] = {
    "Differentiated Learning": "69ca46c801a5a26e0c8d8f22",
    "Scaffolding": "69e1d89aa44857542a0259b7",
    "Engagement": "69e1d89aa44857542a025a00",
}
CATEGORY_IDS: dict[str, str] = {
    "Differentiated Learning": "69c66951544f10544a5db6fe",
    "Scaffolding": "69c8b99081dce4d5e48f103a",
    "Engagement": "69c8b995ba86b2f1fada2e3b",
}


# ── HTML Guardrails ────────────────────────────────────────────────────────────

def _validate_html(html: str) -> list[str]:
    """
    Run structural guardrails on converted HTML.
    Returns a list of failure messages (empty = all pass).
    """
    failures: list[str] = []

    # No list inside a <p>
    if re.search(r"<p>\s*<[uo]l>", html):
        failures.append("FAIL: <ul> or <ol> wrapped inside <p>")

    # Balanced <ul> tags
    ul_open = len(re.findall(r"<ul[> ]", html))
    ul_close = len(re.findall(r"</ul>", html))
    if ul_open != ul_close:
        failures.append(f"FAIL: unbalanced <ul> tags (open={ul_open}, close={ul_close})")

    # Balanced <ol> tags
    ol_open = len(re.findall(r"<ol[> ]", html))
    ol_close = len(re.findall(r"</ol>", html))
    if ol_open != ol_close:
        failures.append(f"FAIL: unbalanced <ol> tags (open={ol_open}, close={ol_close})")

    # No empty paragraphs
    if re.search(r"<p>\s*</p>", html):
        failures.append("FAIL: empty <p></p> tags present")

    # No <h1> in body
    if re.search(r"<h1[> ]", html, re.IGNORECASE):
        failures.append("FAIL: <h1> found in body content (should have been stripped)")

    # Tables wrapped
    if "<table" in html and "data-rt-embed-type" not in html:
        failures.append("FAIL: <table> not wrapped in <div data-rt-embed-type='true'>")

    # No empty hrefs
    if re.search(r'href=["\']["\']', html):
        failures.append("WARN: empty href attribute found")

    return failures


# ── Title helpers ─────────────────────────────────────────────────────────────

_LOWERCASE_WORDS = {
    "a", "an", "the",                          # articles
    "and", "but", "for", "nor", "or", "so", "yet",  # coordinating conjunctions
    "as", "at", "by", "in", "of", "on", "to", "up", "with", "from",  # short prepositions
}


def _title_case(text: str) -> str:
    """
    Apply title case: capitalize all words except articles, conjunctions,
    and short prepositions — unless the word is first, last, or follows a colon.
    """
    words = text.split()
    result = []
    for i, word in enumerate(words):
        # Always capitalize first and last word; capitalize after ": "
        force_cap = (
            i == 0
            or i == len(words) - 1
            or (i > 0 and words[i - 1].endswith(":"))
        )
        lower = word.lower()
        result.append(word.capitalize() if (force_cap or lower not in _LOWERCASE_WORDS) else lower)
    return " ".join(result)


# ── FAQ helpers ────────────────────────────────────────────────────────────────

def _faq_slug(question: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", question.lower()).strip("-")[:80]


def _faq_answer_to_html(answer_md: str) -> str:
    """Convert FAQ answer markdown to HTML using the canonical converter."""
    from scripts.webflow_payload_builder import _md_to_html
    return _md_to_html(answer_md)


# ── Queue builder ──────────────────────────────────────────────────────────────

def prepare_article(item_num: str) -> dict | None:
    """
    Load payload for item_num, validate, and return a publish-queue dict.
    Returns None if the article isn't found or fails a critical guardrail.
    """
    if not PAYLOADS_PATH.exists():
        logger.error(f"webflow_payloads.json not found at {PAYLOADS_PATH}")
        logger.error("Run: python orchestrator.py webflow-mcp-export")
        return None

    with open(PAYLOADS_PATH, encoding="utf-8") as f:
        data = json.load(f)

    article = next(
        (a for a in data["articles"] if str(a["item_num"]) == str(item_num)),
        None
    )
    if not article:
        logger.error(f"Article #{item_num} not found in webflow_payloads.json")
        return None

    cluster = article["cluster"]
    if cluster not in COLLECTION_IDS:
        logger.error(f"#{item_num}: cluster '{cluster}' not in COLLECTION_IDS — not publishing this session")
        return None

    collection_id = COLLECTION_IDS[cluster]
    category_id = CATEGORY_IDS[cluster]

    field_data = dict(article["fieldData"])  # shallow copy
    raw_faqs = article.get("raw_faqs", [])

    # ── Title case on name ─────────────────────────────────────────────────
    if "name" in field_data:
        field_data["name"] = _title_case(field_data["name"])
    if "meta-title-seo" in field_data:
        field_data["meta-title-seo"] = _title_case(field_data["meta-title-seo"])

    # ── Content size check ─────────────────────────────────────────────────
    content_html = field_data.get("content", "")
    content_bytes = len(content_html.encode("utf-8"))
    is_large = content_bytes >= CONTENT_SIZE_THRESHOLD

    if is_large:
        # Save HTML to large_content dir; omit from inline fieldData
        LARGE_CONTENT_DIR.mkdir(parents=True, exist_ok=True)
        slug = field_data.get("slug", str(item_num))
        large_path = LARGE_CONTENT_DIR / f"{item_num}-{slug}.html"
        large_path.write_text(content_html, encoding="utf-8")
        field_data.pop("content", None)
        logger.warning(
            f"  #{item_num}: content {content_bytes:,} bytes ≥ 35KB — "
            f"saved to {large_path.name}, will be omitted from inline create"
        )

    # ── HTML guardrails ────────────────────────────────────────────────────
    guardrail_failures: list[str] = []
    if content_html:
        guardrail_failures = _validate_html(content_html)
        for msg in guardrail_failures:
            if msg.startswith("FAIL"):
                logger.error(f"  #{item_num}: {msg}")
            else:
                logger.warning(f"  #{item_num}: {msg}")

    critical_failures = [f for f in guardrail_failures if f.startswith("FAIL")]
    if critical_failures:
        logger.error(f"  #{item_num}: blocking due to {len(critical_failures)} critical guardrail failures")
        return None

    # ── Inject category ────────────────────────────────────────────────────
    field_data["category"] = category_id

    # ── Prepare FAQs ───────────────────────────────────────────────────────
    prepared_faqs = []
    for faq in raw_faqs:
        question = faq["question"].strip()
        answer_md = faq["answer_md"].strip()
        if not question or not answer_md:
            logger.warning(f"  #{item_num}: skipping empty FAQ — q={question!r}")
            continue
        answer_html = _faq_answer_to_html(answer_md)
        slug = _faq_slug(question)
        prepared_faqs.append({
            "name": question,      # FAQ collection uses "name" not "question"
            "answer_html": answer_html,
            "slug": slug,
        })

    return {
        "item_num": str(item_num),
        "name": article["name"],
        "cluster": cluster,
        "collection_id": collection_id,
        "field_data": field_data,
        "prepared_faqs": prepared_faqs,
        "content_bytes": content_bytes,
        "is_large_content": is_large,
        "guardrail_warnings": [f for f in guardrail_failures if f.startswith("WARN")],
    }


def write_queue_file(queue_item: dict) -> Path:
    """Write queue item to outputs/publish_queue/<N>.json."""
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    item_num = queue_item["item_num"]
    slug = queue_item["field_data"].get("slug", item_num)
    path = QUEUE_DIR / f"{item_num}.json"
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(queue_item, f, indent=2, ensure_ascii=False)
    tmp.replace(path)
    return path


def load_queue_file(item_num: str) -> dict | None:
    """Load a queue file for the given item_num."""
    path = QUEUE_DIR / f"{item_num}.json"
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ── CLI entry points ───────────────────────────────────────────────────────────

def cmd_prepare_single(item_num: str) -> bool:
    """Prepare queue file for one article. Returns True on success."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )
    logger.info(f"Preparing publish queue for article #{item_num}...")
    queue_item = prepare_article(item_num)
    if not queue_item:
        print(f"\n❌ Article #{item_num}: preparation failed — see errors above")
        return False

    path = write_queue_file(queue_item)
    n_faqs = len(queue_item["prepared_faqs"])
    size_kb = queue_item["content_bytes"] / 1024
    large_note = " [LARGE — content omitted from inline payload]" if queue_item["is_large_content"] else ""
    warn_count = len(queue_item.get("guardrail_warnings", []))

    print(f"\n✅ Article #{item_num}: queue file written → {path}")
    print(f"   Name:      {queue_item['name']}")
    print(f"   Cluster:   {queue_item['cluster']}")
    print(f"   Slug:      {queue_item['field_data'].get('slug')}")
    print(f"   Content:   {size_kb:.1f} KB{large_note}")
    print(f"   FAQs:      {n_faqs}")
    if warn_count:
        print(f"   Warnings:  {warn_count}")
        for w in queue_item["guardrail_warnings"]:
            print(f"     {w}")
    print(f"\nNext: in Claude Code session, run MCP publish for article #{item_num}")
    return True


def cmd_prepare_all() -> None:
    """Prepare queue files for all DL articles."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )
    if not PAYLOADS_PATH.exists():
        print(f"Error: {PAYLOADS_PATH} not found. Run: python orchestrator.py webflow-mcp-export")
        return

    with open(PAYLOADS_PATH, encoding="utf-8") as f:
        data = json.load(f)

    dl_articles = [a for a in data["articles"] if a["cluster"] in COLLECTION_IDS]
    logger.info(f"Preparing {len(dl_articles)} DL articles...")

    ok, failed = 0, 0
    for article in dl_articles:
        item_num = article["item_num"]
        queue_item = prepare_article(item_num)
        if queue_item:
            write_queue_file(queue_item)
            ok += 1
        else:
            failed += 1

    print(f"\nQueue files written: {ok} ready, {failed} failed")
    print(f"Queue directory: {QUEUE_DIR}")
    print(f"\nNext: in Claude Code session, run MCP publish for all queued articles")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mcp_publisher.py <item_num>|all")
        sys.exit(1)
    arg = sys.argv[1]
    if arg == "all":
        cmd_prepare_all()
    else:
        success = cmd_prepare_single(arg)
        sys.exit(0 if success else 1)
