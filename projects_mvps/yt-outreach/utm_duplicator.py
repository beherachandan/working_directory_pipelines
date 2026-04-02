#!/usr/bin/env python3
"""Duplicate a Google Sheet and add UTM parameters to all URLs."""

import re
import os
from urllib.parse import urlparse, urlencode, urlunparse, parse_qs

from google.oauth2.service_account import Credentials as SACredentials
from googleapiclient.discovery import build

# ── Standalone config (used when run directly) ────────────────────────────────
SOURCE_SHEET_ID = "1g1IOK-ReOplL_iLO0I8nktxVjC4L_BtOy0hnfG974VU"
NEW_SHEET_TITLE = "Wayground Resources (UTM Tagged)"

UTM_PARAMS = {
    "utm_source": "yt_creator",
    "utm_medium": "partnership",
    "utm_campaign": "iteachalgebra_comments",
}

DRY_RUN = False

CREDENTIALS_DIR = os.environ.get(
    "SHARED_CREDS_DIR",
    os.path.join(os.path.dirname(__file__), "credentials"),
)
SA_KEY_FILE = os.path.join(CREDENTIALS_DIR, "service-account.json")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Regex to find URLs in cell text
URL_PATTERN = re.compile(r'https?://[^\s<>"\']+')

# Columns that contain Wayground URLs (0-indexed)
# Old schema: K(10)=video_id, M(12)=yt_url, T(19)=iv, U(20)=assessment, V(21)=worksheet
# New schema: K(10)=video_id, L(11)=yt_url, N(13)=assessment, Q(16)=iv, V(21)=worksheet
TARGET_COLS = {10, 11, 12, 13, 16, 19, 20, 21}


# ── Auth ──────────────────────────────────────────────────────────────────────
def auth(sa_key_file=None):
    """Authenticate with Sheets + Drive APIs via service account."""
    key = sa_key_file or SA_KEY_FILE
    creds = SACredentials.from_service_account_file(key, scopes=SCOPES)
    sheets = build("sheets", "v4", credentials=creds)
    drive = build("drive", "v3", credentials=creds)
    return sheets, drive


# ── Title cleaning ─────────────────────────────────────────────────────────────
def clean_title(title):
    """Strip 'Copy of', '- Copy', '(Copy)' variants (case-insensitive) from a sheet title."""
    # Strip leading "Copy of " (Google Drive auto-prefix)
    cleaned = re.sub(r'(?i)^copy\s+of\s+', '', title).strip()
    # Strip trailing " - Copy" or " (Copy)"
    cleaned = re.sub(r'(?i)\s*[-–]\s*copy\s*$', '', cleaned).strip()
    cleaned = re.sub(r'(?i)\s*\(copy\)\s*$', '', cleaned).strip()
    return cleaned


# ── Sheet duplication ─────────────────────────────────────────────────────────
def duplicate_sheet(drive, source_id, title):
    """Copy a sheet via Drive API and rename it cleanly. Returns new sheet ID."""
    body = {"name": title}
    resp = drive.files().copy(fileId=source_id, body=body).execute()
    new_id = resp["id"]

    # Drive may still have prepended "Copy of" — force the clean name
    drive.files().update(fileId=new_id, body={"name": title}).execute()

    print(f"  Duplicated → {new_id}")
    print(f"  URL: https://docs.google.com/spreadsheets/d/{new_id}")

    # Make publicly viewable + share with owner
    drive.permissions().create(
        fileId=new_id,
        body={"type": "anyone", "role": "reader"},
    ).execute()
    print(f"  ✓ Public view access set")

    drive.permissions().create(
        fileId=new_id,
        body={"type": "user", "role": "writer", "emailAddress": "chandan@quizizz.com"},
        sendNotificationEmail=False,
    ).execute()
    print(f"  ✓ Edit access granted to chandan@quizizz.com")

    return new_id


# ── UTM tagging ───────────────────────────────────────────────────────────────
def add_utms_to_url(url, utm_params):
    """Replace all utm_* params in a URL with the given utm_params dict."""
    parsed = urlparse(url)
    existing = parse_qs(parsed.query)
    cleaned = {k: v for k, v in existing.items() if not k.startswith("utm_")}
    for key, val in utm_params.items():
        cleaned[key] = [val]
    flat = {k: v[0] if len(v) == 1 else v for k, v in cleaned.items()}
    new_query = urlencode(flat, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


def find_and_tag_urls(sheets, sheet_id, utm_params, dry_run=False):
    """Read all cells, find URLs in TARGET_COLS, add UTMs, batch-update changed cells."""
    meta = sheets.spreadsheets().get(spreadsheetId=sheet_id).execute()
    sheet_names = [s["properties"]["title"] for s in meta["sheets"]]

    total_urls = 0
    for sheet_name in sheet_names:
        range_str = f"'{sheet_name}'"
        result = sheets.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=range_str
        ).execute()
        rows = result.get("values", [])
        if not rows:
            continue

        updates = []
        for r_idx, row in enumerate(rows):
            for c_idx, cell in enumerate(row):
                if c_idx not in TARGET_COLS:
                    continue
                if not isinstance(cell, str):
                    continue
                urls_found = URL_PATTERN.findall(cell)
                if not urls_found:
                    continue
                new_cell = cell
                for url in urls_found:
                    tagged = add_utms_to_url(url, utm_params)
                    if tagged != url:
                        new_cell = new_cell.replace(url, tagged)
                if new_cell != cell:
                    col_letter = chr(ord("A") + c_idx) if c_idx < 26 else f"A{chr(ord('A') + c_idx - 26)}"
                    cell_ref = f"'{sheet_name}'!{col_letter}{r_idx + 1}"
                    updates.append({"range": cell_ref, "values": [[new_cell]]})
                    total_urls += len(urls_found)

        if updates:
            print(f"  Sheet '{sheet_name}': {len(updates)} cells to update ({total_urls} URLs)")
            if not dry_run:
                sheets.spreadsheets().values().batchUpdate(
                    spreadsheetId=sheet_id,
                    body={
                        "valueInputOption": "RAW",
                        "data": updates,
                    },
                ).execute()
                print(f"  ✓ Updated")
            else:
                print(f"  (dry-run — no changes written)")
                for u in updates[:5]:
                    print(f"    {u['range']}: {u['values'][0][0][:100]}...")

    return total_urls


# ── Public API ────────────────────────────────────────────────────────────────
def run(source_sheet_id, new_sheet_title, utm_campaign, dry_run=False, sa_key_file=None):
    """
    Duplicate source_sheet_id, tag all URLs with UTMs, return new sheet ID.

    Args:
        source_sheet_id: ID of the source Google Sheet to copy
        new_sheet_title: Clean title for the new sheet (no 'Copy of' needed)
        utm_campaign: Value for utm_campaign parameter
        dry_run: If True, skip duplication and URL writes
        sa_key_file: Path to service account JSON (defaults to module-level SA_KEY_FILE)

    Returns:
        New sheet ID (or source_sheet_id in dry_run mode)
    """
    utm_params = {
        "utm_source": "yt_creator",
        "utm_medium": "partnership",
        "utm_campaign": utm_campaign,
    }

    print(f"=== UTM Duplicator: {new_sheet_title} ===")
    print(f"  DRY_RUN={dry_run}")
    print(f"  SOURCE: {source_sheet_id}")
    print(f"  UTMs: {utm_params}")
    print()

    sheets, drive = auth(sa_key_file)
    print("  ✓ Auth OK")
    print()

    print("Duplicating sheet...")
    if dry_run:
        print("  (dry-run — skipping duplication, will read source directly)")
        target_id = source_sheet_id
    else:
        target_id = duplicate_sheet(drive, source_sheet_id, new_sheet_title)
    print()

    print("Scanning for URLs and adding UTMs...")
    total = find_and_tag_urls(sheets, target_id, utm_params, dry_run=dry_run)
    print()

    if not dry_run:
        print(f"Done! {total} URLs tagged.")
        print(f"New sheet: https://docs.google.com/spreadsheets/d/{target_id}")
    else:
        print(f"Dry run complete. {total} URLs would be tagged.")

    return target_id


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    run(
        source_sheet_id=SOURCE_SHEET_ID,
        new_sheet_title=NEW_SHEET_TITLE,
        utm_campaign=UTM_PARAMS["utm_campaign"],
        dry_run=DRY_RUN,
    )


if __name__ == "__main__":
    main()
