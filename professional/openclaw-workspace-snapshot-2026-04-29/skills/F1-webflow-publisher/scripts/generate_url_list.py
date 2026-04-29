"""
generate_url_list.py — Generate my-urls.txt from webflow-collections-index JSON

Reads the crawl JSON and outputs a flat list of live URLs for:
  - /blog/          → blog posts
  - /learn/         → all /learn/ article collections
  - /solutions/     → B2B solutions pages
  - /cte-*/         → all CTE collections

Usage:
  python3 generate_url_list.py webflow-collections-index-20260429-0642.json
  python3 generate_url_list.py webflow-collections-index-20260429-0642.json --include-drafts

Output:
  my-urls.txt  (one URL per line, grouped by collection, with comments)
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = "https://wayground.com"

# Map collection slug → URL path prefix
# Collections NOT in this map are skipped (testimonials, authors, subjects-card, etc.)
COLLECTION_URL_MAP = {
    # Blog
    "blog":                    "/blog",
    # /learn/ collections
    "lesson-plan":             "/learn/lesson-plan",
    "education-assessment":    "/learn/education-assessment",
    "generators":              "/learn/generators",
    "question-types":          "/learn/question-types",
    "differentiated-learning": "/learn/differentiated-learning",
    "scaffolding":             "/learn/scaffolding",
    "engagement":              "/learn/engagement",
    # Solutions (B2B)
    "solutions":               "/solutions",
    # CTE — NOTE: URL paths below are inferred from collection slugs.
    # Verify against live site if redirects appear in the checker output.
    "cte-blogs":               "/cte-blogs",
    "cte-certification-prep":  "/cte-certification-prep",
    "cte-compare":             "/cte-compare",
    "cte-perkins-v":           "/cte-perkins-v",
    "cte-state-standards":     "/cte-state-standards",
}

def main():
    parser = argparse.ArgumentParser(description="Generate URL list from Webflow collections index")
    parser.add_argument("json_file", help="Path to webflow-collections-index JSON file")
    parser.add_argument("--include-drafts", action="store_true", dest="include_drafts", help="Include draft (unpublished) items")
    parser.add_argument("--output", default="my-urls.txt", help="Output file name (default: my-urls.txt)")
    args = parser.parse_args()

    json_path = Path(args.json_file)
    if not json_path.exists():
        print(f"ERROR: File not found: {args.json_file}")
        sys.exit(1)

    with open(json_path) as f:
        data = json.load(f)

    collections = data.get("collections", {})
    lines = []
    lines.append(f"# Wayground URL check list")
    lines.append(f"# Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append(f"# Source: {args.json_file}")
    lines.append(f"# Drafts included: {args.include_drafts}")

    lines.append("")

    total = 0
    skipped_draft = 0

    for collection_slug, url_prefix in COLLECTION_URL_MAP.items():
        col_data = collections.get(collection_slug)
        if not col_data:
            lines.append(f"# WARNING: collection '{collection_slug}' not found in JSON")
            lines.append("")
            continue

        items = col_data.get("items", [])
        included = []
        drafts = []

        for item in items:
            if item.get("archived"):
                continue
            if item.get("draft") and not args.include_drafts:
                drafts.append(item)
                skipped_draft += 1
                continue
            slug = item.get("slug", "")
            if not slug:
                continue
            url = f"{BASE_URL}{url_prefix}/{slug}"
            included.append((url, item.get("name", ""), item.get("draft", False)))

        lines.append(f"# ── {collection_slug} ({len(included)} live{', ' + str(len(drafts)) + ' drafts skipped' if drafts else ''}) ──")
        for url, name, is_draft in included:
            draft_tag = " [DRAFT]" if is_draft else ""
            lines.append(f"{url}  # {name}{draft_tag}")
            total += 1
        lines.append("")

    lines.append(f"# Total URLs: {total}")
    if skipped_draft:
        lines.append(f"# Skipped drafts: {skipped_draft} (run with --include-drafts to include)")

    out_path = Path(args.output)
    out_path.write_text("\n".join(lines))
    print(f"\n✅ Written {total} URLs to: {out_path}")
    if skipped_draft:
        print(f"   (skipped {skipped_draft} draft items — use --include-drafts to include them)")
    print(f"\nNow run:")
    print(f"   pip install requests beautifulsoup4 lxml  # if not already installed")
    print(f"   python3 url_checker.py --file {out_path}\n")

if __name__ == "__main__":
    main()
