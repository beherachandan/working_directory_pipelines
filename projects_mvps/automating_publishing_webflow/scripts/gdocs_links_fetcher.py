"""
Fetch hyperlinks from all Google Docs and store them for use in HTML content.

Reads outputs/articles/*.json for gdoc_url fields, fetches each doc as HTML,
extracts and decodes all hyperlinks, and saves them to outputs/article_links/.

Usage:
    python scripts/gdocs_links_fetcher.py

Output:
    outputs/article_links/{item_num}-{slug}.json
    Each file is a list of {"anchor": "link text", "url": "https://..."}
"""
import json
import logging
import re
import time
import urllib.parse
from pathlib import Path

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

ARTICLES_DIR = Path(__file__).parent.parent / "outputs" / "articles"
LINKS_DIR = Path(__file__).parent.parent / "outputs" / "article_links"


def _extract_doc_id(gdoc_url: str) -> str | None:
    """Extract the doc ID from a Google Docs URL."""
    m = re.search(r"/d/([a-zA-Z0-9_-]+)", gdoc_url)
    return m.group(1) if m else None


def _decode_href(href: str) -> str:
    """Decode Google redirect wrapper URLs to actual target URLs."""
    # Google wraps links as: https://www.google.com/url?q=ACTUAL_URL&sa=...
    if "google.com/url" in href or href.startswith("https://www.google.com/url"):
        m = re.search(r"[?&]q=([^&]+)", href)
        if m:
            return urllib.parse.unquote(m.group(1))
    return href


def _fetch_links(doc_id: str) -> list[dict]:
    """Fetch a Google Doc as HTML and extract all hyperlinks."""
    html_url = f"https://docs.google.com/document/d/{doc_id}/export?format=html"
    try:
        r = requests.get(html_url, timeout=30)
        r.raise_for_status()
    except requests.RequestException as e:
        logger.warning(f"  Failed to fetch doc {doc_id}: {e}")
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    links = []
    seen_urls = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        anchor = a.get_text(strip=True)

        # Skip empty anchors, bookmark links, data URIs
        if not anchor:
            continue
        if href.startswith("#"):
            continue
        if href.startswith("data:"):
            continue

        # Decode Google redirect wrapper
        decoded_url = _decode_href(href)

        # Skip if still a Google internal URL after decoding
        if "google.com/url" in decoded_url:
            continue

        # Deduplicate by (anchor, url) pair
        key = (anchor.lower(), decoded_url)
        if key in seen_urls:
            continue
        seen_urls.add(key)

        links.append({"anchor": anchor, "url": decoded_url})

    return links


def main():
    LINKS_DIR.mkdir(parents=True, exist_ok=True)

    article_files = sorted(ARTICLES_DIR.glob("*.json"))
    if not article_files:
        logger.error(f"No article JSON files found in {ARTICLES_DIR}")
        return

    total_links = 0
    for article_file in article_files:
        with open(article_file, encoding="utf-8") as f:
            result = json.load(f)

        item_num = result.get("item_num", article_file.stem.split("-")[0])
        slug = re.sub(r"[^a-z0-9]+", "-", result.get("name", "").lower()).strip("-")
        gdoc_url = result.get("gdoc_url", "")

        if not gdoc_url:
            logger.warning(f"  #{item_num}: no gdoc_url — skipping")
            # Write empty file so downstream knows we checked
            out_path = LINKS_DIR / f"{item_num}-{slug}.json"
            out_path.write_text("[]", encoding="utf-8")
            continue

        doc_id = _extract_doc_id(gdoc_url)
        if not doc_id:
            logger.warning(f"  #{item_num}: could not extract doc ID from {gdoc_url}")
            out_path = LINKS_DIR / f"{item_num}-{slug}.json"
            out_path.write_text("[]", encoding="utf-8")
            continue

        logger.info(f"  #{item_num}: fetching links from doc {doc_id}...")
        links = _fetch_links(doc_id)

        out_path = LINKS_DIR / f"{item_num}-{slug}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(links, f, indent=2, ensure_ascii=False)

        logger.info(f"  #{item_num}: {len(links)} links → {out_path.name}")
        total_links += len(links)

        # Polite delay to avoid rate limiting
        time.sleep(0.5)

    print(f"\nDone. {len(article_files)} articles processed, {total_links} total links saved.")
    print(f"Output: {LINKS_DIR}")


if __name__ == "__main__":
    main()
