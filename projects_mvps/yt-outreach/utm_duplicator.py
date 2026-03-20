#!/usr/bin/env python3
"""Duplicate a Google Sheet and add UTM parameters to all URLs."""

import re
import os
from urllib.parse import urlparse, urlencode, urlunparse, parse_qs

from google.oauth2.service_account import Credentials as SACredentials
from googleapiclient.discovery import build

# ── Config ────────────────────────────────────────────────────────────────────
SOURCE_SHEET_ID = "1g1IOK-ReOplL_iLO0I8nktxVjC4L_BtOy0hnfG974VU"
NEW_SHEET_TITLE = "Wayground Resources (UTM Tagged)"

UTM_PARAMS = {
    "utm_source": "yt_creator",
    "utm_medium": "partnership",
    "utm_campaign": "iteachalgebra_comments",
}

DRY_RUN = False

CREDENTIALS_DIR = os.path.join(os.path.dirname(__file__), "credentials")
SA_KEY_FILE = os.path.join(CREDENTIALS_DIR, "service-account.json")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Regex to find URLs in cell text
URL_PATTERN = re.compile(r'https?://[^\s<>"\']+')

# Columns that back the B-F HYPERLINK formulas (0-indexed)
# B→M(12), C→U(20), D→T(19), E→V(21), F→K(10)
TARGET_COLS = {10, 12, 19, 20, 21}


# ── Auth ──────────────────────────────────────────────────────────────────────
def auth():
    """Authenticate with Sheets + Drive APIs via service account."""
    creds = SACredentials.from_service_account_file(SA_KEY_FILE, scopes=SCOPES)
    sheets = build("sheets", "v4", credentials=creds)
    drive = build("drive", "v3", credentials=creds)
    return sheets, drive


# ── Sheet duplication ─────────────────────────────────────────────────────────
def duplicate_sheet(drive, source_id, title):
    """Copy a sheet via Drive API. Returns new sheet ID."""
    body = {"name": title}
    resp = drive.files().copy(fileId=source_id, body=body).execute()
    new_id = resp["id"]
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
def add_utms_to_url(url):
    """Replace all utm_* params in a URL with the configured UTM_PARAMS."""
    parsed = urlparse(url)
    existing = parse_qs(parsed.query)
    # Strip all existing utm_* params
    cleaned = {k: v for k, v in existing.items() if not k.startswith("utm_")}
    # Add our UTM params
    for key, val in UTM_PARAMS.items():
        cleaned[key] = [val]
    # Flatten single-value lists for clean encoding
    flat = {k: v[0] if len(v) == 1 else v for k, v in cleaned.items()}
    new_query = urlencode(flat, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


def find_and_tag_urls(sheets, sheet_id):
    """Read all cells, find URLs, add UTMs, batch-update changed cells."""
    # Get all sheet names
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

        updates = []  # list of {"range": "Sheet1!B2", "values": [[new_val]]}
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
                    tagged = add_utms_to_url(url)
                    if tagged != url:
                        new_cell = new_cell.replace(url, tagged)
                if new_cell != cell:
                    col_letter = chr(ord("A") + c_idx) if c_idx < 26 else f"A{chr(ord('A') + c_idx - 26)}"
                    cell_ref = f"'{sheet_name}'!{col_letter}{r_idx + 1}"
                    updates.append({"range": cell_ref, "values": [[new_cell]]})
                    total_urls += len(urls_found)

        if updates:
            print(f"  Sheet '{sheet_name}': {len(updates)} cells to update ({total_urls} URLs)")
            if not DRY_RUN:
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


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("=== Wayground UTM Duplicator ===")
    print(f"  DRY_RUN={DRY_RUN}")
    print(f"  SOURCE: {SOURCE_SHEET_ID}")
    print(f"  UTMs: {UTM_PARAMS}")
    print()

    sheets, drive = auth()
    print("  ✓ Auth OK")
    print()

    # Step 1: Duplicate
    print("Duplicating sheet...")
    if DRY_RUN:
        print("  (dry-run — skipping duplication, will read source directly)")
        target_id = SOURCE_SHEET_ID
    else:
        target_id = duplicate_sheet(drive, SOURCE_SHEET_ID, NEW_SHEET_TITLE)
    print()

    # Step 2: Find and tag URLs
    print("Scanning for URLs and adding UTMs...")
    total = find_and_tag_urls(sheets, target_id)
    print()

    if not DRY_RUN:
        print(f"Done! {total} URLs tagged.")
        print(f"New sheet: https://docs.google.com/spreadsheets/d/{target_id}")
        print(f"\nCopy this URL into yt_commenter.py as UTM_SHEET_URL.")
    else:
        print(f"Dry run complete. {total} URLs would be tagged.")


if __name__ == "__main__":
    main()
