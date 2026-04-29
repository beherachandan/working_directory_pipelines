"""
url_checker.py — SEO + structured data verification for Wayground /learn/ URLs

Usage:
  python3 url_checker.py <url1> [url2 url3 ...]
  python3 url_checker.py --file urls.txt
  python3 url_checker.py https://wayground.com/learn/education-assessment/what-are-formative-assessments-a-teachers-guide

Output:
  Prints a summary table to stdout
  Writes full report to: url-check-YYYYMMDD-HHMM.json  (machine-readable)
  Writes summary to:     url-check-YYYYMMDD-HHMM.md    (human-readable)

Checks performed per URL:
  ── HTTP / Accessibility ──
  • HTTP status code (200, 301, 404, etc.)
  • Final URL after redirects
  • Response time (ms)

  ── SEO Basics ──
  • <title> tag — present, length (50–60 chars ideal)
  • <meta name="description"> — present, length (120–160 chars ideal)
  • <link rel="canonical"> — present, matches URL
  • <meta name="robots"> — noindex/nofollow flags
  • H1 tag — present, count (should be exactly 1)
  • OG tags — og:title, og:description, og:image present

  ── Structured Data ──
  • FAQ schema (application/ld+json with @type: FAQPage) — present, question count
  • Article/BlogPosting schema — present
  • BreadcrumbList schema — present
  • Reviewer / Person reference in schema or in page body

  ── Content signals ──
  • Word count (rough estimate from visible text)
  • Internal links count
  • Images without alt text

Dependencies:
  pip install requests beautifulsoup4 lxml
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Missing dependencies. Run: pip install requests beautifulsoup4 lxml")
    sys.exit(1)


# ── Config ─────────────────────────────────────────────────────────────────────

USER_AGENT = "Waymark-URLChecker/1.0 (internal SEO audit; contact=engineering@wayground.com)"
REQUEST_TIMEOUT = 15  # seconds
TITLE_MIN, TITLE_MAX = 30, 65
DESC_MIN, DESC_MAX   = 100, 165


# ── Core checker ───────────────────────────────────────────────────────────────

def check_url(url: str) -> dict:
    result = {
        "input_url": url,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        # HTTP
        "status_code": None,
        "final_url": None,
        "redirect_chain": [],
        "response_ms": None,
        "error": None,
        # SEO basics
        "title": None,
        "title_length": None,
        "title_ok": None,
        "meta_desc": None,
        "meta_desc_length": None,
        "meta_desc_ok": None,
        "canonical": None,
        "canonical_matches": None,
        "robots_noindex": False,
        "robots_nofollow": False,
        "h1_count": 0,
        "h1_text": None,
        "h1_ok": None,
        "og_title": None,
        "og_description": None,
        "og_image": None,
        "og_ok": None,
        # Structured data
        "faq_schema_present": False,
        "faq_question_count": 0,
        "faq_questions": [],
        "article_schema_present": False,
        "breadcrumb_schema_present": False,
        "reviewer_in_schema": False,
        "reviewer_in_body": False,
        "reviewer_names": [],
        # Content signals
        "word_count": 0,
        "internal_links": 0,
        "images_missing_alt": 0,
        # Summary verdict
        "issues": [],
        "warnings": [],
        "passed": [],
    }

    # ── Fetch ──────────────────────────────────────────────────────────────────
    try:
        start = time.time()
        resp = requests.get(
            url,
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT,
            allow_redirects=True,
        )
        elapsed_ms = int((time.time() - start) * 1000)
        result["status_code"] = resp.status_code
        result["final_url"] = resp.url
        result["response_ms"] = elapsed_ms
        result["redirect_chain"] = [r.url for r in resp.history]

        if resp.status_code != 200:
            result["issues"].append(f"HTTP {resp.status_code} — page not accessible")
            return result

    except requests.exceptions.Timeout:
        result["error"] = "Timeout"
        result["issues"].append("Request timed out after 15s")
        return result
    except requests.exceptions.ConnectionError as e:
        result["error"] = str(e)[:200]
        result["issues"].append("Connection error — URL unreachable")
        return result
    except Exception as e:
        result["error"] = str(e)[:200]
        result["issues"].append(f"Fetch error: {e}")
        return result

    # ── Parse ──────────────────────────────────────────────────────────────────
    soup = BeautifulSoup(resp.text, "lxml")

    # ── Title ──────────────────────────────────────────────────────────────────
    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        result["title"] = title
        result["title_length"] = len(title)
        if TITLE_MIN <= len(title) <= TITLE_MAX:
            result["title_ok"] = True
            result["passed"].append(f"Title OK ({len(title)} chars): {title[:60]}")
        else:
            result["title_ok"] = False
            result["warnings"].append(
                f"Title length {len(title)} chars (ideal {TITLE_MIN}–{TITLE_MAX}): {title[:60]}"
            )
    else:
        result["title_ok"] = False
        result["issues"].append("Missing <title> tag")

    # ── Meta description ───────────────────────────────────────────────────────
    meta_desc_tag = soup.find("meta", attrs={"name": "description"})
    if meta_desc_tag and meta_desc_tag.get("content"):
        desc = meta_desc_tag["content"].strip()
        result["meta_desc"] = desc
        result["meta_desc_length"] = len(desc)
        if DESC_MIN <= len(desc) <= DESC_MAX:
            result["meta_desc_ok"] = True
            result["passed"].append(f"Meta description OK ({len(desc)} chars)")
        else:
            result["meta_desc_ok"] = False
            result["warnings"].append(
                f"Meta description length {len(desc)} chars (ideal {DESC_MIN}–{DESC_MAX})"
            )
    else:
        result["meta_desc_ok"] = False
        result["issues"].append("Missing <meta name='description'>")

    # ── Canonical ──────────────────────────────────────────────────────────────
    canonical_tag = soup.find("link", rel="canonical")
    if canonical_tag and canonical_tag.get("href"):
        canonical = canonical_tag["href"].strip()
        result["canonical"] = canonical
        # Normalize for comparison (strip trailing slash)
        final_norm    = resp.url.rstrip("/")
        canonical_norm = canonical.rstrip("/")
        if canonical_norm == final_norm:
            result["canonical_matches"] = True
            result["passed"].append(f"Canonical matches final URL")
        else:
            result["canonical_matches"] = False
            result["warnings"].append(f"Canonical mismatch: canonical={canonical} vs final={resp.url}")
    else:
        result["issues"].append("Missing <link rel='canonical'>")

    # ── Robots meta ────────────────────────────────────────────────────────────
    robots_tag = soup.find("meta", attrs={"name": re.compile(r"robots", re.I)})
    if robots_tag and robots_tag.get("content"):
        content = robots_tag["content"].lower()
        if "noindex" in content:
            result["robots_noindex"] = True
            result["issues"].append("robots meta: NOINDEX — page will not be indexed by search engines")
        if "nofollow" in content:
            result["robots_nofollow"] = True
            result["warnings"].append("robots meta: NOFOLLOW — links not followed")
        if "noindex" not in content and "nofollow" not in content:
            result["passed"].append("Robots meta: index, follow")
    else:
        result["passed"].append("No robots noindex/nofollow meta tag (indexable by default)")

    # ── H1 ─────────────────────────────────────────────────────────────────────
    h1_tags = soup.find_all("h1")
    result["h1_count"] = len(h1_tags)
    if h1_tags:
        result["h1_text"] = h1_tags[0].get_text(strip=True)
    if len(h1_tags) == 1:
        result["h1_ok"] = True
        result["passed"].append(f"H1 present (1): {result['h1_text'][:60]}")
    elif len(h1_tags) == 0:
        result["h1_ok"] = False
        result["issues"].append("No H1 tag found")
    else:
        result["h1_ok"] = False
        result["warnings"].append(f"Multiple H1 tags found ({len(h1_tags)})")

    # ── OG tags ────────────────────────────────────────────────────────────────
    og_title = soup.find("meta", property="og:title")
    og_desc  = soup.find("meta", property="og:description")
    og_image = soup.find("meta", property="og:image")
    result["og_title"]       = og_title["content"].strip() if og_title and og_title.get("content") else None
    result["og_description"] = og_desc["content"].strip()  if og_desc  and og_desc.get("content")  else None
    result["og_image"]       = og_image["content"].strip() if og_image and og_image.get("content") else None
    if result["og_title"] and result["og_description"] and result["og_image"]:
        result["og_ok"] = True
        result["passed"].append("OG tags present (title, description, image)")
    else:
        result["og_ok"] = False
        missing_og = [k for k, v in {"og:title": result["og_title"], "og:description": result["og_description"], "og:image": result["og_image"]}.items() if not v]
        result["warnings"].append(f"Missing OG tags: {', '.join(missing_og)}")

    # ── Structured data (JSON-LD) ───────────────────────────────────────────────
    schema_blocks = soup.find_all("script", type="application/ld+json")
    all_schemas = []
    for block in schema_blocks:
        try:
            data = json.loads(block.string or "")
            # Handle @graph arrays
            if isinstance(data, dict) and "@graph" in data:
                all_schemas.extend(data["@graph"])
            elif isinstance(data, list):
                all_schemas.extend(data)
            else:
                all_schemas.append(data)
        except (json.JSONDecodeError, TypeError):
            pass

    for schema in all_schemas:
        schema_type = schema.get("@type", "")
        if isinstance(schema_type, list):
            schema_type_list = schema_type
        else:
            schema_type_list = [schema_type]

        # FAQ schema
        if "FAQPage" in schema_type_list:
            result["faq_schema_present"] = True
            questions = schema.get("mainEntity", [])
            result["faq_question_count"] = len(questions)
            result["faq_questions"] = [
                q.get("name", "") for q in questions if isinstance(q, dict)
            ]
            result["passed"].append(f"FAQ schema present ({len(questions)} questions)")

        # Article/BlogPosting
        if any(t in schema_type_list for t in ("Article", "BlogPosting", "TechArticle", "ScholarlyArticle")):
            result["article_schema_present"] = True
            result["passed"].append(f"Article schema present (@type: {schema_type})")

            # Reviewer in schema
            reviewer = schema.get("reviewedBy") or schema.get("editor") or schema.get("author")
            if reviewer:
                if isinstance(reviewer, dict):
                    name = reviewer.get("name", "")
                    if name:
                        result["reviewer_in_schema"] = True
                        result["reviewer_names"].append(name)
                elif isinstance(reviewer, list):
                    for r in reviewer:
                        name = r.get("name", "") if isinstance(r, dict) else ""
                        if name:
                            result["reviewer_in_schema"] = True
                            result["reviewer_names"].append(name)

        # Breadcrumb
        if "BreadcrumbList" in schema_type_list:
            result["breadcrumb_schema_present"] = True
            result["passed"].append("BreadcrumbList schema present")

    # Schema summary
    if not result["faq_schema_present"]:
        result["warnings"].append("No FAQPage schema found (structured data missing for FAQ rich results)")
    if not result["article_schema_present"]:
        result["warnings"].append("No Article/BlogPosting schema found")
    if not result["breadcrumb_schema_present"]:
        result["warnings"].append("No BreadcrumbList schema found")

    # ── Reviewer in body ───────────────────────────────────────────────────────
    body_text = soup.get_text(" ", strip=True)
    reviewer_patterns = [
        r"reviewed by\s+([A-Z][a-z]+ [A-Z][a-z]+)",
        r"fact.checked by\s+([A-Z][a-z]+ [A-Z][a-z]+)",
        r"written by\s+([A-Z][a-z]+ [A-Z][a-z]+)",
        r"expert reviewer[:\s]+([A-Z][a-z]+ [A-Z][a-z]+)",
    ]
    for pattern in reviewer_patterns:
        matches = re.findall(pattern, body_text, re.IGNORECASE)
        if matches:
            result["reviewer_in_body"] = True
            result["reviewer_names"].extend(matches)

    result["reviewer_names"] = list(set(result["reviewer_names"]))  # dedupe

    if result["reviewer_in_schema"] or result["reviewer_in_body"]:
        result["passed"].append(f"Reviewer/author signal present: {', '.join(result['reviewer_names'])}")
    else:
        result["warnings"].append("No reviewer/author attribution found in schema or body (E-E-A-T signal missing)")

    # ── Content signals ─────────────────────────────────────────────────────────
    # Word count from visible text
    visible_text = soup.get_text(" ")
    words = [w for w in visible_text.split() if len(w) > 1]
    result["word_count"] = len(words)
    if result["word_count"] < 800:
        result["warnings"].append(f"Low word count: {result['word_count']} words (AEO articles typically 1500+)")
    else:
        result["passed"].append(f"Word count: {result['word_count']}")

    # Internal links
    parsed_base = urlparse(resp.url)
    base_domain = f"{parsed_base.scheme}://{parsed_base.netloc}"
    all_links = soup.find_all("a", href=True)
    internal = [a for a in all_links if a["href"].startswith("/") or a["href"].startswith(base_domain)]
    result["internal_links"] = len(internal)

    # Images without alt
    images = soup.find_all("img")
    missing_alt = [img for img in images if not img.get("alt")]
    result["images_missing_alt"] = len(missing_alt)
    if missing_alt:
        result["warnings"].append(f"{len(missing_alt)} image(s) missing alt text")

    return result


# ── Output formatting ─────────────────────────────────────────────────────────

def verdict(r: dict) -> str:
    if r.get("error") or r.get("status_code") not in (200, None) and r.get("status_code") != 200:
        return "❌ FAIL"
    if r["issues"]:
        return "❌ ISSUES"
    if r["warnings"]:
        return "⚠️  WARN"
    return "✅ PASS"


def print_summary(results: list):
    print("\n" + "=" * 110)
    print(f"{'URL':<60} {'STATUS':>6}  {'TITLE':>5}  {'DESC':>4}  {'H1':>2}  {'FAQ':>3}  {'ART':>3}  VERDICT")
    print("=" * 110)
    for r in results:
        url_short = r["input_url"][-58:] if len(r["input_url"]) > 58 else r["input_url"]
        status    = str(r["status_code"] or r.get("error", "ERR"))
        title_ok  = "✅" if r["title_ok"]     else "❌"
        desc_ok   = "✅" if r["meta_desc_ok"] else "❌"
        h1_ok     = "✅" if r["h1_ok"]        else "❌"
        faq_ok    = "✅" if r["faq_schema_present"] else "—"
        art_ok    = "✅" if r["article_schema_present"] else "—"
        v         = verdict(r)
        print(f"{url_short:<60} {status:>6}  {title_ok:>5}  {desc_ok:>4}  {h1_ok:>2}  {faq_ok:>3}  {art_ok:>3}  {v}")
    print("=" * 110)
    passes  = sum(1 for r in results if verdict(r) == "✅ PASS")
    warns   = sum(1 for r in results if verdict(r) == "⚠️  WARN")
    issues  = sum(1 for r in results if "ISSUES" in verdict(r) or "FAIL" in verdict(r))
    print(f"\nSummary: {passes} PASS  |  {warns} WARN  |  {issues} ISSUES  ({len(results)} URLs checked)\n")


def write_report(results: list, urls_input: list):
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    base_name = f"url-check-{ts}"

    # JSON
    json_path = f"{base_name}.json"
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_urls": urls_input,
        "total_checked": len(results),
        "summary": {
            "pass":   sum(1 for r in results if verdict(r) == "✅ PASS"),
            "warn":   sum(1 for r in results if verdict(r) == "⚠️  WARN"),
            "issues": sum(1 for r in results if "ISSUES" in verdict(r) or "FAIL" in verdict(r)),
        },
        "results": results,
    }
    with open(json_path, "w") as f:
        json.dump(payload, f, indent=2)

    # Markdown
    md_path = f"{base_name}.md"
    lines = [
        f"# URL Check Report",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**URLs checked:** {len(results)}  ",
        f"**Pass:** {payload['summary']['pass']}  |  **Warn:** {payload['summary']['warn']}  |  **Issues:** {payload['summary']['issues']}",
        "",
        "---",
        "",
    ]
    for r in results:
        v = verdict(r)
        lines.append(f"## {v} `{r['input_url']}`")
        lines.append("")
        lines.append(f"| Field | Value |")
        lines.append(f"|---|---|")
        lines.append(f"| HTTP Status | {r['status_code']} |")
        lines.append(f"| Final URL | {r['final_url'] or '—'} |")
        lines.append(f"| Response time | {r['response_ms']}ms |")
        lines.append(f"| Title | {(r['title'] or '❌ MISSING')[:80]} ({r['title_length'] or 0} chars) |")
        lines.append(f"| Meta Description | {(r['meta_desc'] or '❌ MISSING')[:100]} ({r['meta_desc_length'] or 0} chars) |")
        lines.append(f"| Canonical | {r['canonical'] or '❌ MISSING'} {'✅' if r['canonical_matches'] else '⚠️'} |")
        lines.append(f"| Robots noindex | {'🚫 YES' if r['robots_noindex'] else '✅ No'} |")
        lines.append(f"| H1 count | {r['h1_count']} — {r['h1_text'] or '—'} |")
        lines.append(f"| OG tags | title={'✅' if r['og_title'] else '❌'} desc={'✅' if r['og_description'] else '❌'} image={'✅' if r['og_image'] else '❌'} |")
        lines.append(f"| FAQ schema | {'✅ ' + str(r['faq_question_count']) + ' questions' if r['faq_schema_present'] else '❌ Missing'} |")
        lines.append(f"| Article schema | {'✅' if r['article_schema_present'] else '❌ Missing'} |")
        lines.append(f"| Breadcrumb schema | {'✅' if r['breadcrumb_schema_present'] else '❌ Missing'} |")
        lines.append(f"| Reviewer signal | {'✅ ' + ', '.join(r['reviewer_names']) if (r['reviewer_in_schema'] or r['reviewer_in_body']) else '⚠️ Missing'} |")
        lines.append(f"| Word count | {r['word_count']} |")
        lines.append(f"| Internal links | {r['internal_links']} |")
        lines.append(f"| Images missing alt | {r['images_missing_alt']} |")
        lines.append("")
        if r["issues"]:
            lines.append("**❌ Issues (must fix):**")
            for issue in r["issues"]:
                lines.append(f"- {issue}")
            lines.append("")
        if r["warnings"]:
            lines.append("**⚠️ Warnings (should fix):**")
            for w in r["warnings"]:
                lines.append(f"- {w}")
            lines.append("")
        if r["passed"]:
            lines.append("**✅ Passed:**")
            for p in r["passed"]:
                lines.append(f"- {p}")
            lines.append("")
        if r.get("faq_questions"):
            lines.append("**FAQ questions found in schema:**")
            for q in r["faq_questions"]:
                lines.append(f"- {q}")
            lines.append("")
        lines.append("---")
        lines.append("")

    with open(md_path, "w") as f:
        f.write("\n".join(lines))

    return json_path, md_path


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Check one or more URLs for SEO basics and structured data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 url_checker.py https://wayground.com/learn/education-assessment/what-are-formative-assessments-a-teachers-guide
  python3 url_checker.py https://wayground.com/learn/generators/rubric-generator https://wayground.com/learn/question-types/types-of-test-questions-how-to-choose-the-right-format-for-every-learner
  python3 url_checker.py --file my-urls.txt
        """
    )
    parser.add_argument(
        "urls",
        nargs="*",
        help="One or more URLs to check",
    )
    parser.add_argument(
        "--file", "-f",
        help="Text file with one URL per line",
    )
    args = parser.parse_args()

    urls = list(args.urls)

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"ERROR: File not found: {args.file}")
            sys.exit(1)
        file_urls = [line.strip() for line in file_path.read_text().splitlines() if line.strip() and not line.startswith("#")]
        urls.extend(file_urls)

    if not urls:
        parser.print_help()
        sys.exit(1)

    # Strip inline comments ("# ...") and whitespace from each URL
    def clean_url(u: str) -> str:
        return u.split("#")[0].strip()

    # Dedupe while preserving order
    seen = set()
    unique_urls = []
    for u in urls:
        u = clean_url(u)
        if u and u not in seen:
            seen.add(u)
            unique_urls.append(u)

    print(f"\nChecking {len(unique_urls)} URL(s)...\n")

    results = []
    for url in unique_urls:
        print(f"  → {url}")
        r = check_url(url)
        results.append(r)

    print_summary(results)

    json_path, md_path = write_report(results, unique_urls)
    print(f"JSON report: {json_path}")
    print(f"MD  report:  {md_path}\n")


if __name__ == "__main__":
    main()
