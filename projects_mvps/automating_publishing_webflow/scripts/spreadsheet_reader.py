"""Parse Next_50_batch_fomo.xlsx → list of ArticleRecord dicts."""
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import openpyxl


@dataclass
class ArticleRecord:
    item_num: str
    name: str
    cluster: str
    sub_cluster: str
    gdoc_url: str
    doc_id: str
    creation_notes: str
    url_slug: str
    keyword_variants: str
    content_type: str = ""
    volume: str = ""

    def slug_or_name(self) -> str:
        """Return url_slug if set, otherwise a kebab-case version of name."""
        if self.url_slug and self.url_slug.strip():
            return self.url_slug.strip()
        return re.sub(r"[^a-z0-9]+", "-", self.name.lower()).strip("-")


def extract_doc_id(url: str) -> str:
    """Extract Google Doc ID from any Google Docs URL format."""
    if not url:
        return ""
    m = re.search(r"/document/d/([a-zA-Z0-9_-]+)", url)
    return m.group(1) if m else ""


def read_articles(xlsx_path: Path) -> list[ArticleRecord]:
    """
    Read all article rows from the spreadsheet.

    The workbook has:
      Row 1: Title row ("Wayground Content Dashboard")
      Row 2: "Client Review" header artefact
      Row 3: Actual column headers
      Row 4+: Data rows
    """
    wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
    ws = wb.active

    rows = list(ws.iter_rows(values_only=True))

    # Find the header row by scanning for the row that contains "Name"
    header_row_idx = None
    for i, row in enumerate(rows):
        if row[0] == "Name":
            header_row_idx = i
            break

    if header_row_idx is None:
        raise ValueError("Could not find header row with 'Name' in column A")

    headers = rows[header_row_idx]
    col = {str(h).strip(): i for i, h in enumerate(headers) if h is not None}

    articles: list[ArticleRecord] = []
    seen_doc_ids: set[str] = set()

    for row in rows[header_row_idx + 1:]:
        name = row[col["Name"]] if col.get("Name") is not None else None
        if not name:
            continue

        item_num = str(row[col.get("Item #", 2)] or "").strip()
        cluster = str(row[col.get("Cluster", 15)] or "").strip()
        sub_cluster = str(row[col.get("Sub-Cluster", 17)] or "").strip()
        draft_url = str(row[col.get("Draft", 10)] or "").strip()
        creation_notes = str(row[col.get("Creation Notes", 18)] or "").strip()
        url_slug = str(row[col.get("URL Slug", 19)] or "").strip()
        keyword_variants = str(row[col.get("Keyword Variants", 23)] or "").strip()
        content_type = str(row[col.get("Content Type", 6)] or "").strip()
        volume_raw = row[col.get("Volume", 7)]
        volume = str(int(volume_raw)) if isinstance(volume_raw, (int, float)) else ""

        doc_id = extract_doc_id(draft_url)

        if doc_id in seen_doc_ids:
            print(f"  WARNING: item #{item_num} ({name!r}) shares doc_id with a previous article — {draft_url}")
        if doc_id:
            seen_doc_ids.add(doc_id)

        articles.append(ArticleRecord(
            item_num=item_num,
            name=str(name).strip(),
            cluster=cluster,
            sub_cluster=sub_cluster,
            gdoc_url=draft_url,
            doc_id=doc_id,
            creation_notes=creation_notes,
            url_slug=url_slug,
            keyword_variants=keyword_variants,
            content_type=content_type,
            volume=volume,
        ))

    wb.close()
    return articles


if __name__ == "__main__":
    from config import XLSX_PATH
    articles = read_articles(XLSX_PATH)
    print(f"Loaded {len(articles)} articles")
    for a in articles:
        status = "OK" if a.doc_id else "NO_DOC_ID"
        print(f"  #{a.item_num} [{status}] {a.name!r} — {a.cluster} / {a.sub_cluster}")
