#!/usr/bin/env python3
"""
Multi-creator YT outreach pipeline orchestrator.

Usage:
  python run_pipeline.py --list-only          # Discover sheets + tabs, print list, exit
  python run_pipeline.py --dry-run            # Full dry-run: show comment previews, no posts
  python run_pipeline.py --creator "Name"     # Process a single creator by sheet title substring
  python run_pipeline.py                      # Real run for all creators

The pipeline state is saved to pipeline_state.json and supports resume on re-run.
"""

import argparse
import json
import os
import re
import sys
import time

from google.oauth2.service_account import Credentials as SACredentials
from googleapiclient.discovery import build

import utm_duplicator
import yt_commenter

# ── Config ────────────────────────────────────────────────────────────────────
DRIVE_FOLDER_ID = "1IWUD511GSWEGyPq81YAz6G_jMhzoOrIz"
SKIP_SHEETS_CONTAINING = [
    "iteachalgebra",
    "Most Popular Teacher YouTube Channels",  # mega-sheet — duplicates individual sheets
]

# Map sheet-name substrings → YT channel handle used in comment text
CREATOR_NAME_MAP = [
    ("Crash Course",    "CrashCourse"),
    ("Bozeman",         "BozemanScience"),
    ("Amoeba Sisters",  "AmoebaSisters"),
    ("Math Antics",     "MathAntics"),
    ("Flipping Physics","FlippingPhysics"),
]

CREDENTIALS_DIR = os.environ.get(
    "SHARED_CREDS_DIR",
    os.path.join(os.path.dirname(__file__), "credentials"),
)
SA_KEY_FILE = os.path.join(CREDENTIALS_DIR, "service-account.json")
OAUTH_CLIENT_FILE = os.path.join(CREDENTIALS_DIR, "oauth-client.json")
TOKEN_FILE = os.path.join(CREDENTIALS_DIR, "token.json")

STATE_FILE = os.path.join(os.path.dirname(__file__), "pipeline_state.json")

DRIVE_SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
]


# ── Auth ──────────────────────────────────────────────────────────────────────
def auth_drive_and_sheets():
    creds = SACredentials.from_service_account_file(
        SA_KEY_FILE,
        scopes=[
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/spreadsheets.readonly",
        ]
    )
    drive = build("drive", "v3", credentials=creds)
    sheets = build("sheets", "v4", credentials=creds)
    return drive, sheets


# ── Drive discovery ───────────────────────────────────────────────────────────
def list_sheets_in_folder(drive, folder_id):
    """Return list of {id, name} for all Google Sheets in the folder."""
    query = (
        f"'{folder_id}' in parents "
        f"and mimeType='application/vnd.google-apps.spreadsheet' "
        f"and trashed=false"
    )
    results = []
    page_token = None
    while True:
        resp = drive.files().list(
            q=query,
            fields="nextPageToken, files(id, name)",
            pageSize=1000,
            pageToken=page_token,
        ).execute()
        results.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return results


def should_skip(sheet_name):
    name_lower = sheet_name.lower()
    return any(skip.lower() in name_lower for skip in SKIP_SHEETS_CONTAINING)


# ── Title / slug helpers ──────────────────────────────────────────────────────
def to_slug(name):
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')


def creator_name_from_sheet(sheet_name):
    """
    Derive the YT channel name from the source sheet title.
    Checks CREATOR_NAME_MAP first, then falls back to a cleaned sheet name.
    """
    for substring, handle in CREATOR_NAME_MAP:
        if substring.lower() in sheet_name.lower():
            return handle
    # Fallback: strip "Copy of", then strip from any boilerplate trigger word to end
    name = utm_duplicator.clean_title(sheet_name)
    name = re.sub(
        r"(?i)\s*(?:most popular\b|top\s+\d+\b|\byoutube\b|with\s+quizzes|wayground"
        r"|\bmaster\s+sheet\b|\bquizzes\b).*$",
        '', name
    ).strip()
    # Strip trailing possessive apostrophe-s (ASCII ' or smart apostrophe \u2019)
    name = re.sub(r"['\u2019]s\s*$", '', name).strip()
    return name or sheet_name


# ── State management ──────────────────────────────────────────────────────────
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# ── Pre-run status summary ────────────────────────────────────────────────────
def print_status(all_sheets, state):
    """Print a table of all discovered sheets: done/pending, and flag SA-owned UTM copies."""
    utm_ids = {v["utm_sheet_id"] for v in state.values() if "utm_sheet_id" in v}
    source_ids_done = set(state.keys())

    print(f"\n{'='*72}")
    print(f"  {'SHEET NAME':<48} {'STATUS':<12} NOTE")
    print(f"{'='*72}")

    for sheet in sorted(all_sheets, key=lambda s: s["name"]):
        sid = sheet["id"]
        name = sheet["name"]
        display = name[:46] + ".." if len(name) > 48 else name
        if sid in utm_ids:
            print(f"  {display:<48} {'[SA COPY]':<12} UTM-tagged duplicate (skip)")
        elif sid in source_ids_done:
            tabs = state[sid].get("tabs_done", [])
            print(f"  {display:<48} {'DONE':<12} tabs: {tabs}")
        else:
            print(f"  {display:<48} {'PENDING':<12}")

    total = len(all_sheets)
    sa_copies = sum(1 for s in all_sheets if s["id"] in utm_ids)
    done = sum(1 for s in all_sheets if s["id"] in source_ids_done and s["id"] not in utm_ids)
    pending = total - sa_copies - done
    print(f"{'='*72}")
    print(f"  Total: {total}  |  Done: {done}  |  Pending: {pending}  |  SA copies (skip): {sa_copies}\n")


# ── Discovery ─────────────────────────────────────────────────────────────────
def discover(drive, sheets_service, filter_creator=None):
    """
    Discover all eligible sheets and their valid data tabs.
    Returns list of dicts:
      {sheet_id, sheet_name, tabs: [{name, gid, creator_name}]}
    """
    all_sheets = list_sheets_in_folder(drive, DRIVE_FOLDER_ID)

    # Skip sheets we already created as UTM copies (SA owns them — don't re-process)
    state = load_state()
    utm_ids = {v["utm_sheet_id"] for v in state.values() if "utm_sheet_id" in v}
    source_ids_done = set(state.keys())

    eligible = []

    for sheet in all_sheets:
        name = sheet["name"]
        sid = sheet["id"]

        if should_skip(name):
            continue
        if sid in utm_ids:
            continue  # SA-owned UTM copy — skip to avoid double-processing
        if sid in source_ids_done:
            continue  # Already fully processed source sheet — skip
        if filter_creator and filter_creator.lower() not in name.lower():
            continue

        # Discover valid tabs (small sleep to stay under 60 reads/min quota)
        time.sleep(1.5)
        try:
            all_tabs = yt_commenter.get_sheet_tabs(sheets_service, sid)
        except Exception as e:
            print(f"  ⚠ Could not read tabs for '{name}': {e}")
            continue

        sheet_creator = creator_name_from_sheet(name)
        valid_tabs = []
        for tab in all_tabs:
            if yt_commenter.is_data_tab(sheets_service, sid, tab["name"]):
                valid_tabs.append({
                    "name": tab["name"],
                    "gid": tab["gid"],
                    "creator_name": sheet_creator,
                })

        if valid_tabs:
            eligible.append({
                "sheet_id": sid,
                "sheet_name": name,
                "tabs": valid_tabs,
            })

    return eligible


# ── Pipeline runner ───────────────────────────────────────────────────────────
def run_pipeline(eligible_sheets, dry_run=False, utm_only=False):
    state = load_state()

    for sheet in eligible_sheets:
        sid = sheet["sheet_id"]
        sheet_name = sheet["sheet_name"]
        tabs = sheet["tabs"]
        slug = to_slug(sheet_name)
        clean_name = utm_duplicator.clean_title(sheet_name)
        utm_campaign = f"{to_slug(clean_name)}_comments"

        print(f"\n{'='*60}")
        print(f"Sheet: {sheet_name}  ({sid})")
        print(f"  Tabs: {[t['name'] for t in tabs]}")
        print(f"{'='*60}")

        # ── Step 1: UTM Duplicate ──
        sheet_state = state.get(sid, {})
        utm_sheet_id = sheet_state.get("utm_sheet_id")

        if not utm_sheet_id:
            clean_name = utm_duplicator.clean_title(sheet_name)
            new_title = f"{clean_name} (UTM Tagged)"
            utm_sheet_id = utm_duplicator.run(
                source_sheet_id=sid,
                new_sheet_title=new_title,
                utm_campaign=utm_campaign,
                dry_run=dry_run,
                sa_key_file=SA_KEY_FILE,
            )
            sheet_state["utm_sheet_id"] = utm_sheet_id
            sheet_state["title"] = sheet_name
            sheet_state.setdefault("tabs_done", [])
            state[sid] = sheet_state
            if not dry_run:
                save_state(state)
        else:
            print(f"\n[RESUME] UTM sheet already exists: {utm_sheet_id}")

        # ── Step 2: Comment per tab (skipped when utm_only=True) ──
        if utm_only:
            print(f"  [UTM-ONLY] Skipping comment posting for {sheet_name}")
            continue

        for tab in tabs:
            tab_name = tab["name"]
            tab_gid = tab["gid"]
            creator_name = tab["creator_name"]
            tab_slug = to_slug(tab_name)

            tabs_done = sheet_state.get("tabs_done", [])
            if tab_name in tabs_done:
                print(f"\n[SKIP] Tab '{tab_name}' already done.")
                continue

            print(f"\n── Tab: {tab_name}  (creator: {creator_name}) ──")

            sheet_range = f"'{tab_name}'!A:V"
            progress_file = os.path.join(
                os.path.dirname(__file__),
                f"progress_{slug}_{tab_slug}.json"
            )

            yt_commenter.run(
                sheet_id=utm_sheet_id,
                sheet_range=sheet_range,
                creator_name=creator_name,
                tab_gid=tab_gid,
                utm_sheet_id=utm_sheet_id,
                progress_file=progress_file,
                dry_run=dry_run,
                sa_key_file=SA_KEY_FILE,
                oauth_client_file=OAUTH_CLIENT_FILE,
                token_file=TOKEN_FILE,
            )

            if not dry_run:
                sheet_state.setdefault("tabs_done", []).append(tab_name)
                save_state(state)

    print("\n\nPipeline complete.")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Multi-creator YT outreach pipeline")
    parser.add_argument("--list-only", action="store_true",
                        help="Discover and print sheets/tabs, then exit (no writes)")
    parser.add_argument("--status", action="store_true",
                        help="Show all sheets with done/pending status then exit")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print comment previews but do not post or write")
    parser.add_argument("--creator", type=str, default=None,
                        help="Process only sheets whose title contains this string")
    parser.add_argument("--utm-only", action="store_true",
                        help="Only create UTM copies; skip comment posting (use batch_scheduler.py to post)")
    args = parser.parse_args()

    print("Authenticating...")
    drive, sheets_service = auth_drive_and_sheets()
    print("  ✓ Auth OK\n")

    # --status: show all files in folder (regardless of data-tab check) then exit
    if args.status:
        print(f"Listing all sheets in folder {DRIVE_FOLDER_ID}...")
        all_sheets = list_sheets_in_folder(drive, DRIVE_FOLDER_ID)
        state = load_state()
        print_status(all_sheets, state)
        sys.exit(0)

    print(f"Discovering sheets in folder {DRIVE_FOLDER_ID}...")
    eligible = discover(drive, sheets_service, filter_creator=args.creator)

    if not eligible:
        print("No eligible sheets found.")
        sys.exit(0)

    print(f"\nDiscovered {len(eligible)} sheet(s) (excluding: {SKIP_SHEETS_CONTAINING}):\n")
    for i, sheet in enumerate(eligible, 1):
        print(f"  {i}. {sheet['sheet_name']}")
        for tab in sheet["tabs"]:
            print(f"       Tab: \"{tab['name']}\"  →  creator: \"{tab['creator_name']}\"  (gid={tab['gid']})")
    print()

    if args.list_only:
        print("[--list-only] Exiting without processing.")
        sys.exit(0)

    if args.dry_run:
        print("[--dry-run] Will show comment previews, no posts or writes.\n")
    else:
        # Print status table before a real run so user can verify before committing
        all_sheets = list_sheets_in_folder(drive, DRIVE_FOLDER_ID)
        print_status(all_sheets, load_state())

    run_pipeline(eligible, dry_run=args.dry_run, utm_only=args.utm_only)


if __name__ == "__main__":
    main()
