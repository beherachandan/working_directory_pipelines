"""Fetch article text from publicly shared Google Docs via export API."""
import asyncio
import re

import aiohttp

EXPORT_URL = "https://docs.google.com/document/d/{doc_id}/export?format=txt"
EXPORT_HTML_URL = "https://docs.google.com/document/d/{doc_id}/export?format=html"
MIN_TEXT_LENGTH = 500  # chars; flag as suspiciously short below this


async def fetch_doc_text(
    doc_id: str,
    session: aiohttp.ClientSession,
    retries: int = 3,
    base_delay: float = 1.0,
) -> tuple[str, str]:
    """
    Fetch the plain-text export of a Google Doc.

    Returns (text, warning) where warning is "" on success or a message if
    the text looks suspiciously short and we fell back to HTML stripping.
    """
    url = EXPORT_URL.format(doc_id=doc_id)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; WaygroundEval/1.0)"}

    for attempt in range(retries):
        try:
            async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=30)) as resp:
                if resp.status == 403:
                    return "", f"HTTP 403 — doc may be restricted: {doc_id}"
                if resp.status == 404:
                    return "", f"HTTP 404 — doc not found: {doc_id}"
                resp.raise_for_status()
                raw = await resp.read()
                text = raw.decode("utf-8-sig").strip()

                if len(text) < MIN_TEXT_LENGTH:
                    # Try HTML export as fallback
                    html_text = await _fetch_html_fallback(doc_id, session, headers)
                    if html_text and len(html_text) > len(text):
                        return html_text, f"Short plain text ({len(text)} chars); used HTML fallback ({len(html_text)} chars)"
                    return text, f"Short text ({len(text)} chars) — may contain mostly images/tables"

                return text, ""

        except asyncio.TimeoutError:
            if attempt < retries - 1:
                await asyncio.sleep(base_delay * (2 ** attempt))
                continue
            return "", f"Timeout after {retries} attempts: {doc_id}"
        except aiohttp.ClientError as e:
            if attempt < retries - 1:
                await asyncio.sleep(base_delay * (2 ** attempt))
                continue
            return "", f"Network error: {e}"

    return "", f"Failed after {retries} retries: {doc_id}"


async def _fetch_html_fallback(
    doc_id: str,
    session: aiohttp.ClientSession,
    headers: dict,
) -> str:
    """Fetch HTML export and strip tags to plain text."""
    url = EXPORT_HTML_URL.format(doc_id=doc_id)
    try:
        async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=30)) as resp:
            if resp.status != 200:
                return ""
            html = await resp.text(encoding="utf-8")
            # Strip HTML tags
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"&nbsp;", " ", text)
            text = re.sub(r"&amp;", "&", text)
            text = re.sub(r"&lt;", "<", text)
            text = re.sub(r"&gt;", ">", text)
            text = re.sub(r"\s{2,}", " ", text).strip()
            return text
    except Exception:
        return ""


async def fetch_all_docs(
    articles: list,
    semaphore: asyncio.Semaphore,
) -> dict[str, tuple[str, str]]:
    """
    Fetch all articles concurrently.
    Returns {item_num: (text, warning)}.
    """
    async with aiohttp.ClientSession() as session:
        tasks = {
            article.item_num: fetch_doc_text(article.doc_id, session)
            for article in articles
            if article.doc_id
        }
        results = {}
        for item_num, coro in tasks.items():
            async with semaphore:
                results[item_num] = await coro
        return results


if __name__ == "__main__":
    import sys
    doc_id = sys.argv[1] if len(sys.argv) > 1 else "1GT7Scrxw37OOowWcBVztknvIyYb9INegHTiT9I3h8J4"

    async def _test():
        async with aiohttp.ClientSession() as session:
            text, warning = await fetch_doc_text(doc_id, session)
            if warning:
                print(f"WARNING: {warning}")
            print(f"Text length: {len(text)} chars")
            print(text[:1000])

    asyncio.run(_test())
