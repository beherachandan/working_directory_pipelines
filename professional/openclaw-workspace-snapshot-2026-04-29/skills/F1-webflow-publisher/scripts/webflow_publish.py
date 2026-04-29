"""
webflow_publish.py — Waymark F1 Publisher

Single entry point for publishing one article to Webflow CMS.
Handles: MD → HTML conversion, FAQ extraction, guardrail checks,
FAQ item creation, article item creation, optional live publish.

Usage:
  python3 webflow_publish.py \
    --article aeo/outputs/articles/teaching-strategies/draft-final.md \
    --collection education-assessment \
    --mode draft \
    [--live]

  python3 webflow_publish.py --setup   # lists all collections (verify token)

Output:
  Prints JSON result: {status, item_id, item_url, faq_ids, report_path}
  Writes report to: aeo/outputs/publish/{slug}-report.md

Dependencies:
  pip install aiohttp markdown
"""
import argparse
import asyncio
import json
import logging
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

# ── Config ────────────────────────────────────────────────────────────────────

WEBFLOW_API_TOKEN = "de4f365546bd477f108d9e2434dc1c2e2fd1b958aea9d3af34ecbf72d0a0daf1"
WEBFLOW_API_BASE = "https://api.webflow.com/v2"
SITE_ID = "68355113496452bf05789e95"
FAQS_COLLECTION_ID = "6850473a6fb75a92cada401b"
CONTENT_SIZE_THRESHOLD = 35_000  # bytes

WORKSPACE = Path(__file__).parent.parent.parent.parent  # workspace root

COLLECTION_IDS = {
    "education-assessment":    "69722f178db818ab468d8701",
    "generators":              "69722f2d64a2cc8327352307",
    "question-types":          "69722f7dd5ea1f81a678f394",
    "lesson-plan":             "696e0ecfd20021b0ba12ef08",
    "differentiated-learning": "69ca46c801a5a26e0c8d8f22",
    "scaffolding":             "69e1d89aa44857542a0259b7",
    "engagement":              "69e1d89aa44857542a025a00",
}

CATEGORY_IDS = {
    "education-assessment":    "696e1289e2d4ca298c449e01",
    "generators":              "696e129824e0900a5791fa9e",
    "question-types":          "696e12aa113deb07546ef3c5",
    "lesson-plan":             "696e12750a49c05e9176e4f0",
    "differentiated-learning": "69c66951544f10544a5db6fe",
    "scaffolding":             "69c8b99081dce4d5e48f103a",
    "engagement":              "69c8b995ba86b2f1fada2e3b",
}

QUESTION_WORDS = ("how", "what", "when", "why", "can", "is", "are", "do",
                  "does", "should", "will", "which", "who", "where")

# ── Helpers ───────────────────────────────────────────────────────────────────

def _headers():
    return {
        "Authorization": f"Bearer {WEBFLOW_API_TOKEN}",
        "Content-Type": "application/json",
        "accept": "application/json",
    }


def _slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:80]


def _md_to_html(md_text: str) -> str:
    """Convert markdown to Webflow-compatible HTML via dedicated script."""
    script = Path(__file__).parent / "markdown-to-webflow-html.py"
    try:
        proc = subprocess.run(
            ["python3", str(script)],
            input=md_text, capture_output=True, text=True,
        )
        if proc.returncode == 0:
            return proc.stdout
        logger.warning(f"markdown-to-webflow-html.py failed: {proc.stderr[:200]}")
    except Exception as e:
        logger.warning(f"Could not run markdown-to-webflow-html.py: {e}")
    # Fallback
    import markdown
    return markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])


def _extract_faqs(md_text: str) -> tuple[str, list[dict]]:
    """Extract FAQ section from markdown. Returns (cleaned_md, faqs)."""
    lines = md_text.split("\n")
    sections = []
    for i, line in enumerate(lines):
        if line.startswith("## "):
            heading = line[3:].strip()
            if sections:
                sections[-1] = (sections[-1][0], i - 1, sections[-1][2])
            sections.append((i, len(lines) - 1, heading))

    faq_range = None
    for start, end, heading in sections:
        lower = heading.lower()
        is_faq = "frequently asked" in lower or " faq" in lower or lower.startswith("faq")
        if not is_faq:
            section_lines = lines[start:end + 1]
            h3s = [l.lstrip("#").strip() for l in section_lines if l.startswith("### ")]
            is_faq = bool(h3s) and all(h3.lower().split()[0] in QUESTION_WORDS for h3 in h3s)
        if is_faq:
            faq_range = (start, end)
            break

    if faq_range is None:
        return md_text, []

    faq_start, faq_end = faq_range
    faq_lines = lines[faq_start:faq_end + 1]
    faqs = []
    current_q = None
    current_ans = []

    def _flush():
        if current_q and current_ans:
            faqs.append({"question": current_q, "answer_md": "\n".join(current_ans).strip()})

    for line in faq_lines[1:]:
        if line.startswith("### "):
            _flush()
            current_q = line[4:].strip()
            current_ans = []
        elif current_q is not None:
            current_ans.append(line)
    _flush()

    cleaned = "\n".join(lines[:faq_start] + lines[faq_end + 1:]).rstrip()
    return cleaned, faqs


def _clean_md(md_text: str) -> str:
    """Strip H1, References section, horizontal rules, image prompts."""
    lines = md_text.split("\n")
    # Remove first H1
    h1_gone = False
    out = []
    for line in lines:
        if not h1_gone and line.startswith("# "):
            h1_gone = True
            continue
        out.append(line)
    # Remove ## References
    result = []
    in_refs = False
    for line in out:
        if line.startswith("## ") and "references" in line.lower():
            in_refs = True
            continue
        if in_refs and line.startswith("## "):
            in_refs = False
        if not in_refs:
            result.append(line)
    # Remove standalone ---
    result = [l for l in result if l.strip() != "---"]
    # Strip image prompts before first H2
    h2_seen = False
    final = []
    for line in result:
        if line.startswith("## "):
            h2_seen = True
        if (not h2_seen and line.strip()
                and not re.match(r"^[#*>_\-\[0-9]", line.strip())
                and not any(c in line for c in ["**", "__", "`", "[", "("])):
            continue
        final.append(line)
    return "\n".join(final).strip()


def _validate_html(html: str) -> list[str]:
    """Run structural guardrails. Returns list of FAIL/WARN messages."""
    failures = []
    if re.search(r"<p>\s*<[uo]l>", html):
        failures.append("FAIL: <ul>/<ol> wrapped inside <p>")
    ul_open = len(re.findall(r"<ul[> ]", html))
    ul_close = len(re.findall(r"</ul>", html))
    if ul_open != ul_close:
        failures.append(f"FAIL: unbalanced <ul> (open={ul_open}, close={ul_close})")
    ol_open = len(re.findall(r"<ol[> ]", html))
    ol_close = len(re.findall(r"</ol>", html))
    if ol_open != ol_close:
        failures.append(f"FAIL: unbalanced <ol> (open={ol_open}, close={ol_close})")
    if re.search(r"<p>\s*</p>", html):
        failures.append("FAIL: empty <p></p> present")
    if re.search(r"<h1[> ]", html, re.IGNORECASE):
        failures.append("FAIL: <h1> found in body (should be stripped)")
    if "<table" in html and "data-rt-embed-type" not in html:
        failures.append("FAIL: <table> not wrapped in data-rt-embed-type div")
    if re.search(r'href=["\']["\']', html):
        failures.append("WARN: empty href attribute found")
    return failures


def _extract_metadata(md_text: str) -> dict:
    """Extract title, slug, meta from article markdown."""
    title = ""
    meta_title = ""
    meta_desc = ""

    for line in md_text.split("\n"):
        if line.startswith("# ") and not title:
            title = re.sub(r"\s*\(?\d{4}\)?$", "", line[2:].strip())
        if line.startswith("**Meta Title:**") or line.startswith("**Recommended title tag:**"):
            meta_title = line.split(":", 1)[-1].strip().strip("*")
        if line.startswith("**Meta Description:**") or line.startswith("**Recommended meta description:**"):
            meta_desc = line.split(":", 1)[-1].strip().strip("*")

    if not meta_title:
        meta_title = title[:60] if title else ""
    if not meta_desc:
        # Take first non-heading paragraph
        for line in md_text.split("\n"):
            if line.strip() and not line.startswith("#") and not line.startswith("**"):
                meta_desc = line.strip()[:160]
                break

    slug = _slugify(title) if title else "article"
    return {"title": title, "slug": slug, "meta_title": meta_title, "meta_desc": meta_desc}


# ── API calls ─────────────────────────────────────────────────────────────────

async def _api_get(session, path: str) -> dict:
    import aiohttp
    url = f"{WEBFLOW_API_BASE}{path}"
    async with session.get(url, headers=_headers()) as resp:
        resp.raise_for_status()
        return await resp.json()


async def _create_item(session, collection_id: str, field_data: dict) -> str:
    import aiohttp
    url = f"{WEBFLOW_API_BASE}/collections/{collection_id}/items"
    async with session.post(url, headers=_headers(), json={"fieldData": field_data}) as resp:
        if resp.status not in (200, 201, 202):
            body = await resp.text()
            raise RuntimeError(f"Create item failed ({resp.status}): {body[:400]}")
        data = await resp.json()
        return data.get("id") or data.get("_id") or (data.get("items") or [{}])[0].get("id") or ""


async def _publish_items(session, collection_id: str, item_ids: list[str]):
    import aiohttp
    url = f"{WEBFLOW_API_BASE}/collections/{collection_id}/items/publish"
    async with session.post(url, headers=_headers(), json={"itemIds": item_ids}) as resp:
        if resp.status not in (200, 202):
            body = await resp.text()
            raise RuntimeError(f"Publish items failed ({resp.status}): {body[:400]}")


# ── Setup command ─────────────────────────────────────────────────────────────

async def cmd_setup():
    """List all collections to verify token + site access."""
    import aiohttp
    async with aiohttp.ClientSession() as session:
        data = await _api_get(session, f"/sites/{SITE_ID}/collections")
        cols = data.get("collections", [])
        print(f"\n✅ Token valid. Found {len(cols)} collections:\n")
        for c in cols:
            print(f"  {c.get('displayName','?'):<45} {c.get('id')}  /{c.get('slug')}")


# ── Main publish ──────────────────────────────────────────────────────────────

async def publish(article_path: str, collection_slug: str, mode: str = "draft") -> dict:
    """
    Full publish flow for one article.
    mode: "draft" = create as draft only | "live" = create + publish live
    Returns result dict.
    """
    import aiohttp

    # ── Validate inputs ────────────────────────────────────────────────────
    if collection_slug not in COLLECTION_IDS:
        return {"status": "failed", "error": f"Unknown collection: {collection_slug}. Valid: {list(COLLECTION_IDS.keys())}"}

    article_file = WORKSPACE / article_path
    if not article_file.exists():
        return {"status": "failed", "error": f"Article not found: {article_file}"}

    collection_id = COLLECTION_IDS[collection_slug]
    category_id = CATEGORY_IDS[collection_slug]
    md_text = article_file.read_text(encoding="utf-8")

    # Strip pipeline-internal sections (never published to Webflow)
    # Enhancement logs, editor notes: appended by C5 after the article body
    # Sources/References: bibliography block — inline citations stay, this list is internal
    for sentinel in [
        "\n---\n## Enhancement log",
        "\n---\n## Editor notes",
        "\n## Enhancement log",
        "\n## Editor notes",
        "\n## Sources",
        "\n## References",
    ]:
        if sentinel in md_text:
            md_text = md_text.split(sentinel)[0]

    logger.info(f"Publishing: {article_file.name} → /{collection_slug} ({mode})")

    # ── Extract metadata ───────────────────────────────────────────────────
    meta = _extract_metadata(md_text)
    logger.info(f"  Title: {meta['title']}")
    logger.info(f"  Slug:  {meta['slug']}")

    # ── Extract FAQs ───────────────────────────────────────────────────────
    cleaned_md, faqs = _extract_faqs(md_text)
    logger.info(f"  FAQs: {len(faqs)}")

    # ── Prepare content HTML ───────────────────────────────────────────────
    content_md = _clean_md(cleaned_md)
    content_html = _md_to_html(content_md)

    # ── HTML guardrails ────────────────────────────────────────────────────
    guardrail_issues = _validate_html(content_html)
    critical = [f for f in guardrail_issues if f.startswith("FAIL")]
    if critical:
        for msg in critical:
            logger.error(f"  {msg}")
        return {"status": "failed", "error": f"HTML guardrail failures: {critical}"}
    for w in guardrail_issues:
        logger.warning(f"  {w}")

    # ── Content size check ─────────────────────────────────────────────────
    content_bytes = len(content_html.encode("utf-8"))
    is_large = content_bytes >= CONTENT_SIZE_THRESHOLD
    if is_large:
        large_dir = WORKSPACE / "aeo/outputs/publish/large_content"
        large_dir.mkdir(parents=True, exist_ok=True)
        large_path = large_dir / f"{meta['slug']}.html"
        large_path.write_text(content_html, encoding="utf-8")
        logger.warning(f"  Content {content_bytes:,} bytes ≥ 35KB — saved to {large_path}")
        content_html = ""  # omit from inline payload

    # ── Build field data ───────────────────────────────────────────────────
    field_data = {
        "name": meta["title"],
        "slug": meta["slug"],
        "content": content_html,
        "meta-title-seo": meta["meta_title"],
        "meta-description-seo": meta["meta_desc"],
        "category": category_id,
        "publishing-date": datetime.now(timezone.utc).strftime("%Y-%m-%dT00:00:00.000Z"),
        "main-image-visible": False,
    }
    # Strip empty strings
    field_data = {k: v for k, v in field_data.items() if v != "" and v is not None}

    # ── Publish to Webflow ─────────────────────────────────────────────────
    async with aiohttp.ClientSession() as session:

        # Step 1: Create FAQ items
        # Use a short timestamp suffix on slug to avoid conflicts on re-runs
        import time as _time
        _slug_suffix = str(int(_time.time()))[-5:]
        faq_ids = []
        for faq in faqs:
            faq_html = _md_to_html(faq["answer_md"])
            faq_fields = {
                "name": faq["question"],
                "slug": _slugify(faq["question"])[:60] + "-" + _slug_suffix,
                "answer": faq_html,
            }
            faq_id = await _create_item(session, FAQS_COLLECTION_ID, faq_fields)
            faq_ids.append(faq_id)
            logger.info(f"  FAQ created: {faq_id} — {faq['question'][:50]}")

        # Attach FAQ IDs to article
        if faq_ids:
            field_data["faqs"] = faq_ids
            field_data["faq-title"] = "FAQs"

        # Step 2: Create article item
        item_id = await _create_item(session, collection_id, field_data)
        logger.info(f"  Article created (draft): {item_id}")

        # Step 3: Publish live if requested
        if mode == "live":
            if faq_ids:
                await _publish_items(session, FAQS_COLLECTION_ID, faq_ids)
                logger.info(f"  FAQs published live: {len(faq_ids)}")
            await _publish_items(session, collection_id, [item_id])
            logger.info(f"  Article published live: {item_id}")

    # ── Write report ───────────────────────────────────────────────────────
    report_dir = WORKSPACE / "aeo/outputs/publish"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{meta['slug']}-report.md"
    status = "live" if mode == "live" else "draft"
    item_url = f"https://webflow.com/design/{SITE_ID}/cms/{collection_id}/{item_id}"
    preview_url = f"https://wayground-main-staging.webflow.io/learn/{collection_slug}/{meta['slug']}"

    report = f"""# Webflow Publication Report
**Article:** {meta['title']}
**Published:** {datetime.now(timezone.utc).isoformat()}
**Status:** {'✅ Live' if status == 'live' else '📝 Draft'}

## Item Details
- Collection: {collection_slug} (`{collection_id}`)
- Item ID: `{item_id}`
- Slug: `{meta['slug']}`
- Preview: {preview_url}
- Webflow Editor: {item_url}

## Metadata
- Title tag: {meta['meta_title']}
- Meta description: {meta['meta_desc'][:80]}...
- Content size: {content_bytes:,} bytes{' ⚠️ LARGE — manual upload required' if is_large else ''}

## FAQs
- Created: {len(faq_ids)}
- IDs: {', '.join(faq_ids) if faq_ids else 'none'}

## Next Steps
- [ ] Review draft in Webflow Designer
- [ ] Add featured image if needed
- [ ] Verify FAQs render correctly
{'- [ ] Upload content manually from: aeo/outputs/publish/large_content/' + meta['slug'] + '.html' if is_large else ''}
- [ ] {'Publish when ready' if status == 'draft' else 'Verify live page renders correctly'}
"""
    report_path.write_text(report, encoding="utf-8")
    logger.info(f"  Report written: {report_path}")

    result = {
        "status": status,
        "item_id": item_id,
        "item_url": item_url,
        "preview_url": preview_url,
        "faq_ids": faq_ids,
        "report_path": str(report_path),
        "is_large_content": is_large,
    }
    print(json.dumps(result, indent=2))
    return result


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Publish article to Webflow CMS")
    parser.add_argument("--article", help="Path to article .md file (relative to workspace)")
    parser.add_argument("--collection", help="Collection slug (e.g. education-assessment)")
    parser.add_argument("--mode", default="draft", choices=["draft", "live"])
    parser.add_argument("--setup", action="store_true", help="List collections and verify token")
    args = parser.parse_args()

    if args.setup:
        asyncio.run(cmd_setup())
        return

    if not args.article or not args.collection:
        parser.error("--article and --collection are required")

    asyncio.run(publish(args.article, args.collection, args.mode))


if __name__ == "__main__":
    main()
