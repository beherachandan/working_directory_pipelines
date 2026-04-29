"""
Build Webflow CMS field payloads for all enhanced articles.

No credentials required — this is pure data extraction and MD→HTML conversion.
Output is written to outputs/webflow_payloads.json for use with Webflow MCP tools.

Usage:
  python orchestrator.py webflow-mcp-export

After running, use Claude Code Webflow MCP tools to publish:
  1. data_sites_tool.list_sites           → get site ID
  2. data_cms_tool.get_collection_list    → map cluster names to collection IDs
  3. Read outputs/webflow_payloads.json
  4. For each article: create FAQ items in FAQs collection, then create article
  5. data_cms_tool.publish_collection_items → go live (optional)

Best-practice spec: webflow-publisher.md
"""
import json
import logging
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

ARTICLES_DIR = Path(__file__).parent.parent / "outputs" / "articles"
PAYLOADS_PATH = Path(__file__).parent.parent / "outputs" / "webflow_payloads.json"
MD_TO_HTML_SCRIPT = Path(__file__).parent / "markdown-to-webflow-html.py"

CHANGES_LOG_SENTINEL = "\n---\n## Enhancement changes log"
EDITOR_NOTES_SENTINEL = "\n---\n## Editor notes"

PUBLISHING_DATE = "2026-03-27T00:00:00.000Z"

# Words that indicate an H3 is a question (for auto-detecting FAQ sections)
QUESTION_WORDS = ("how", "what", "when", "why", "can", "is", "are", "do",
                  "does", "should", "will", "which", "who", "where")


def _load_enhanced_md(result: dict) -> str:
    """Read the enhanced .md file and strip appended metadata sections."""
    path_str = result.get("enhanced_local_path", "")
    if not path_str:
        return ""
    path = Path(path_str)
    if not path.exists():
        return ""
    full = path.read_text(encoding="utf-8")
    # Strip editor notes pre-publish checklist (added by CONTENT_ENHANCER agent)
    if EDITOR_NOTES_SENTINEL in full:
        full = full.split(EDITOR_NOTES_SENTINEL)[0]
    # Strip changes log (added by enhancement pipeline)
    if CHANGES_LOG_SENTINEL in full:
        full = full.split(CHANGES_LOG_SENTINEL)[0]
    return full.rstrip()


def _is_faq_heading(heading: str) -> bool:
    """Return True if an H2 heading identifies an FAQ section."""
    lower = heading.lower()
    return "frequently asked" in lower or " faq" in lower or lower.startswith("faq")


def _all_h3s_are_questions(section_lines: list[str]) -> bool:
    """Return True if every H3 in the section starts with a question word."""
    h3s = [l.lstrip("#").strip() for l in section_lines if l.startswith("### ")]
    if not h3s:
        return False
    return all(h3.lower().split()[0] in QUESTION_WORDS for h3 in h3s)


def _extract_faqs(md_text: str) -> tuple[str, list[dict]]:
    """
    Extract FAQ Q&A pairs from the markdown.

    Detects FAQ section via:
    1. H2 heading containing "frequently asked" or "faq" (case-insensitive)
    2. H2 section where ALL H3 children start with a question word

    Returns:
        (cleaned_md, faq_list)
        cleaned_md — markdown with the FAQ section removed
        faq_list   — list of {"question": str, "answer_md": str}
    """
    lines = md_text.split("\n")
    # Split into H2 sections
    sections: list[tuple[int, int, str]] = []  # (start_line, end_line, heading)
    for i, line in enumerate(lines):
        if line.startswith("## "):
            heading = line[3:].strip()
            if sections:
                sections[-1] = (sections[-1][0], i - 1, sections[-1][2])
            sections.append((i, len(lines) - 1, heading))

    faq_section_range: tuple[int, int] | None = None
    for start, end, heading in sections:
        section_lines = lines[start:end + 1]
        if _is_faq_heading(heading) or _all_h3s_are_questions(section_lines):
            faq_section_range = (start, end)
            break

    if faq_section_range is None:
        return md_text, []

    faq_start, faq_end = faq_section_range
    faq_lines = lines[faq_start:faq_end + 1]

    # Extract H3 Q&A pairs within the FAQ section
    faqs: list[dict] = []
    current_q: str | None = None
    current_answer_lines: list[str] = []

    def _flush():
        if current_q and current_answer_lines:
            answer_md = "\n".join(current_answer_lines).strip()
            faqs.append({"question": current_q, "answer_md": answer_md})

    for line in faq_lines[1:]:  # skip the H2 heading itself
        if line.startswith("### "):
            _flush()
            current_q = line[4:].strip()
            current_answer_lines = []
        elif current_q is not None:
            current_answer_lines.append(line)

    _flush()

    # Remove the FAQ section from the markdown
    before = lines[:faq_start]
    after = lines[faq_end + 1:]
    cleaned_lines = before + after
    cleaned_md = "\n".join(cleaned_lines).rstrip()

    return cleaned_md, faqs


def _clean_content_md(md_text: str) -> str:
    """
    Prepare article markdown for HTML conversion:
    - Strip first H1 heading (Webflow `name` field handles the title)
    - Strip ## References section
    - Strip standalone horizontal rules (---)
    - Strip image description paragraphs (editorial photo prompts before first H2)
    """
    lines = md_text.split("\n")

    # Remove first H1
    h1_removed = False
    cleaned: list[str] = []
    for line in lines:
        if not h1_removed and line.startswith("# "):
            h1_removed = True
            continue
        cleaned.append(line)

    # Remove ## References section
    result: list[str] = []
    in_refs = False
    for line in cleaned:
        if line.startswith("## ") and "references" in line.lower():
            in_refs = True
            continue
        if in_refs and line.startswith("## "):
            in_refs = False
        if not in_refs:
            result.append(line)

    # Remove standalone horizontal rules
    final: list[str] = []
    for line in result:
        if line.strip() == "---":
            continue
        final.append(line)

    # Strip image description paragraphs (scene descriptions before first H2).
    # These are editorial photo prompts written as plain text, not real images.
    # Heuristic: non-empty line before any H2 with no markdown formatting chars.
    h2_seen = False
    final2: list[str] = []
    for line in final:
        if line.startswith("## "):
            h2_seen = True
        if (
            not h2_seen
            and line.strip()
            and not re.match(r"^[#*>_\-\[0-9]", line.strip())
            and not any(c in line for c in ["**", "__", "`", "[", "("])
        ):
            continue  # skip image prompt / scene description line
        final2.append(line)

    return "\n".join(final2).strip()


def _md_to_html(md_text: str) -> str:
    """Convert markdown to HTML using the dedicated script (sane_lists)."""
    try:
        proc = subprocess.run(
            ["python3", str(MD_TO_HTML_SCRIPT)],
            input=md_text,
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            return proc.stdout
        logger.warning(f"markdown-to-webflow-html.py failed: {proc.stderr[:200]}")
    except Exception as e:
        logger.warning(f"Could not run markdown-to-webflow-html.py: {e}")

    # Fallback: import directly
    try:
        import markdown as md_lib
        return md_lib.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])
    except ImportError:
        pass

    # Last resort: basic regex (should rarely hit this)
    from scripts.webflow_stub import WebflowPublisher
    return WebflowPublisher._md_to_html(md_text)


def _apply_links(html: str, links_path: Path) -> str:
    """
    Apply stored hyperlinks from Google Docs back into the HTML content.

    For each {anchor, url} pair in the links JSON, substitute the first
    occurrence of the anchor text in the HTML with <a href="url">anchor</a>.
    Only replaces text nodes (outside existing <a> tags) by checking that
    the anchor isn't already wrapped in an anchor tag.
    """
    if not links_path.exists():
        return html
    try:
        links = json.loads(links_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return html
    for item in links:
        anchor = item.get("anchor", "")
        url = item.get("url", "")
        if not anchor or not url:
            continue
        # Skip if anchor text is already inside an <a> tag in the HTML
        already_linked = re.search(
            r'<a\b[^>]*>' + re.escape(anchor) + r'</a>', html, flags=re.IGNORECASE
        )
        if already_linked:
            continue
        replacement = f'<a href="{url}">{anchor}</a>'
        html, count = re.subn(
            re.escape(anchor), replacement, html, count=1, flags=re.IGNORECASE
        )
    return html


def _faq_slug(question: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", question.lower()).strip("-")[:80]


def build_payloads() -> list[dict]:
    """
    Load all article results, build Webflow fieldData for each, and return
    a list of payload dicts: {item_num, name, cluster, fieldData, raw_faqs}.
    """
    from scripts.webflow_stub import WebflowPublisher
    publisher = WebflowPublisher()  # no credentials needed — stateless helpers

    article_files = sorted(ARTICLES_DIR.glob("*.json"), key=lambda f: _sort_key(f.stem))
    if not article_files:
        logger.error(f"No article JSON files found in {ARTICLES_DIR}")
        return []

    payloads = []
    for article_file in article_files:
        with open(article_file, encoding="utf-8") as f:
            result = json.load(f)

        item_num = result.get("item_num", article_file.stem.split("-")[0])
        name = result.get("name", "")
        cluster = result.get("cluster", "")

        # 1. Load raw enhanced markdown
        raw_md = _load_enhanced_md(result)
        if not raw_md:
            logger.warning(f"  #{item_num}: no enhanced MD found — content will be empty")

        # 2. Extract FAQs and get FAQ-cleaned markdown
        cleaned_md, raw_faqs = _extract_faqs(raw_md) if raw_md else ("", [])

        # 3. Clean for HTML conversion (strip H1, refs, hr)
        content_md = _clean_content_md(cleaned_md) if cleaned_md else ""

        # 4. Convert to HTML
        content_html = _md_to_html(content_md) if content_md else ""

        # 4b. Apply hyperlinks from original Google Doc (if fetched)
        links_path = (
            Path(__file__).parent.parent / "outputs" / "article_links"
            / f"{item_num}-{re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')}.json"
        )
        content_html = _apply_links(content_html, links_path)

        # 5. Build base fieldData from result metadata
        checklist = result.get("pre_publish_checklist", {})
        platform_flags = result.get("platform_flags", {})
        schema_list = checklist.get("schema_to_add", [])
        schema_str = ", ".join(schema_list) if isinstance(schema_list, list) else str(schema_list)

        slug = (
            checklist.get("slug_recommendation")
            or result.get("url_slug")
            or re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        )

        field_data: dict = {
            "name": name,
            "slug": slug,
            "content": content_html,
            "meta-title-seo": checklist.get("title_tag", ""),
            "meta-description-seo": checklist.get("meta_description", ""),
            "geo-score": int(float(result.get("geo_composite", 0) or 0)),
            "brand-verdict": result.get("brand_verdict", ""),
            "sub-cluster": result.get("sub_cluster", ""),
            "schema-markup": schema_str,
            "aio-ready": bool(platform_flags.get("aio_ready")),
            "chatgpt-ready": bool(platform_flags.get("chatgpt_ready")),
            "publishing-date": PUBLISHING_DATE,
            "main-image-visible": False,
        }

        # Add faq-title when FAQs exist (filled with IDs at publish time)
        if raw_faqs:
            field_data["faq-title"] = "FAQs"

        # Strip empty strings for optional fields (but keep bools and ints)
        field_data = {
            k: v for k, v in field_data.items()
            if v != "" and v is not None
        }

        payloads.append({
            "item_num": str(item_num),
            "name": name,
            "cluster": cluster,
            "fieldData": field_data,
            "raw_faqs": [
                {"question": faq["question"], "answer_md": faq["answer_md"]}
                for faq in raw_faqs
            ],
        })
        logger.info(
            f"  #{item_num}: built payload ({len(field_data)} fields, {len(raw_faqs)} FAQs)"
        )

    return payloads


def _sort_key(stem: str) -> int:
    """Sort article files numerically by item_num prefix."""
    try:
        return int(stem.split("-")[0])
    except (ValueError, IndexError):
        return 0


def main():
    """Build all payloads and write outputs/webflow_payloads.json."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")

    logger.info("Building Webflow MCP payloads...")
    payloads = build_payloads()

    if not payloads:
        logger.error("No payloads built — check that enhanced articles exist in outputs/articles/")
        return

    # Cluster breakdown
    cluster_counts: dict[str, int] = defaultdict(int)
    faq_counts: dict[str, int] = defaultdict(int)
    for p in payloads:
        cluster_counts[p["cluster"]] += 1
        faq_counts[p["cluster"]] += len(p["raw_faqs"])

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(payloads),
        "clusters": dict(cluster_counts),
        "articles": payloads,
    }

    PAYLOADS_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = PAYLOADS_PATH.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    tmp.replace(PAYLOADS_PATH)

    print(f"\nWebflow MCP payloads written to: {PAYLOADS_PATH}")
    print(f"Total articles: {len(payloads)}")
    print("Cluster breakdown:")
    for cluster, count in sorted(cluster_counts.items()):
        print(f"  {cluster}: {count} articles, {faq_counts[cluster]} FAQs total")
    print("\nNext steps in Claude Code session:")
    print("  For each article:")
    print("    1. Create FAQ items in FAQs collection (6850473a6fb75a92cada401b)")
    print("    2. Create article with faqs:[ids], category, geo-score int")
    print("  data_cms_tool.publish_collection_items per cluster (optional, live)")


if __name__ == "__main__":
    main()
