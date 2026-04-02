#!/usr/bin/env python3
"""Post YouTube comments with Wayground resource links from a Google Sheet."""

import json
import os
import re
import sys
import time
import requests

from google.oauth2.service_account import Credentials as SACredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
_HttpError = HttpError

# ── Standalone config (used when run directly) ────────────────────────────────
SHEET_ID = "1tTpbj9MuKsS_5cM5AS1qodCnjKy9N23szTgfUSqee28"
SHEET_GID = 755464040
SHEET_RANGE = "'iteachalgebra top 120 videos'!A:V"
CREATOR_NAME = "iteachalgebra"
UTM_SHEET_URL = "https://docs.google.com/spreadsheets/d/1tTpbj9MuKsS_5cM5AS1qodCnjKy9N23szTgfUSqee28"

DRY_RUN = True
LIMIT = 0
DELAY_SECONDS = 2

CREDENTIALS_DIR = os.environ.get(
    "SHARED_CREDS_DIR",
    os.path.join(os.path.dirname(__file__), "credentials"),
)
SA_KEY_FILE = os.path.join(CREDENTIALS_DIR, "service-account.json")
OAUTH_CLIENT_FILE = os.path.join(CREDENTIALS_DIR, "oauth-client.json")
TOKEN_FILE = os.path.join(CREDENTIALS_DIR, "token.json")
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")

SHEETS_SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
YOUTUBE_SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Tab names that are never data tabs
TAB_BLOCKLIST = {"content", "overview", "notes", "about", "template", "index", "summary", "info", "readme", "more amazing collections"}

COMMENT_TEMPLATE_HEADER = "Teaching this topic? Wayground has FREE resources that will make your lesson practically plan itself.\n"
COMMENT_TEMPLATE_FOOTER = "\nUse them to check understanding or give your students the extra practice that actually lands. ❤️\nHere is a curated sheet with these resources from {creator_name} and many more!"


# ── Auth ──────────────────────────────────────────────────────────────────────
def auth_sheets(sa_key_file=None):
    key = sa_key_file or SA_KEY_FILE
    creds = SACredentials.from_service_account_file(key, scopes=SHEETS_SCOPES)
    return build("sheets", "v4", credentials=creds)


def auth_youtube(oauth_client_file=None, token_file=None):
    client_file = oauth_client_file or OAUTH_CLIENT_FILE
    tok_file = token_file or TOKEN_FILE
    creds = None
    if os.path.exists(tok_file):
        creds = Credentials.from_authorized_user_file(tok_file, YOUTUBE_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_file, YOUTUBE_SCOPES)
            creds = flow.run_local_server(port=0)
        with open(tok_file, "w") as f:
            f.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)


# ── Rate-limit-aware API helper ───────────────────────────────────────────────
def _api_call_with_backoff(fn, max_retries=5):
    """Execute fn() retrying on HTTP 429 with exponential backoff."""
    delay = 5
    for attempt in range(max_retries):
        try:
            return fn()
        except _HttpError as e:
            if e.resp.status == 429 and attempt < max_retries - 1:
                print(f"  ⏳ Rate limited, waiting {delay}s...")
                time.sleep(delay)
                delay = min(delay * 2, 60)
            else:
                raise


# ── Tab discovery ─────────────────────────────────────────────────────────────
def get_sheet_tabs(sheets_service, sheet_id):
    """
    Return list of dicts: {name, gid} for each tab in the sheet.
    Excludes tabs whose names match the blocklist.
    """
    meta = _api_call_with_backoff(
        lambda: sheets_service.spreadsheets().get(spreadsheetId=sheet_id).execute()
    )
    tabs = []
    for s in meta["sheets"]:
        props = s["properties"]
        name = props["title"]
        gid = props["sheetId"]
        if name.strip().lower() in TAB_BLOCKLIST:
            continue
        tabs.append({"name": name, "gid": gid})
    return tabs


def is_data_tab(sheets_service, sheet_id, tab_name):
    """
    Return True if the tab looks like a data tab.
    Checks columns J and K (rows 2–12) for an 11-char YouTube video ID.
    Covers both column schemas:
      - Old schema: video_id in Col J (index 9)
      - New schema: video_id in Col K (index 10)
    """
    try:
        range_str = f"'{tab_name}'!J2:K12"
        result = _api_call_with_backoff(
            lambda: sheets_service.spreadsheets().values().get(
                spreadsheetId=sheet_id, range=range_str
            ).execute()
        )
        rows = result.get("values", [])
        for row in rows:
            for cell_val in row:
                if cell_val and re.match(r'^[a-zA-Z0-9_-]{11}$', cell_val.strip()):
                    return True
    except _HttpError as e:
        if e.resp.status == 403:
            print(f"    ⚠ Access denied (403) reading sheet {sheet_id} tab '{tab_name}' — folder share may not have propagated")
        elif e.resp.status != 404:
            print(f"    ⚠ HTTP {e.resp.status} reading sheet {sheet_id} tab '{tab_name}'")
    except Exception:
        pass
    return False


# ── Creator name extraction ────────────────────────────────────────────────────
def creator_name_from_tab(tab_name):
    """
    Extract creator name from tab name.
    e.g. "MathWithMrJ top 50 videos" → "MathWithMrJ"
         "iteachalgebra top 120 videos" → "iteachalgebra"
         "TeacherTech - Algebra" → "TeacherTech - Algebra" (no match, kept as-is)
    """
    name = re.sub(r'\s+top\s+\d+\s+videos?\s*$', '', tab_name, flags=re.IGNORECASE).strip()
    name = re.sub(r'\s+top\s+\d+\s*$', '', name, flags=re.IGNORECASE).strip()
    return name or tab_name


# ── Schema detection ─────────────────────────────────────────────────────────
def _detect_schema(header_row):
    """
    Detect column layout from the first header row.

    New schema (sheets with explicit "YouTube Video ID" column header):
      video_id=K(10), yt_url=L(11), assessment=N(13), iv=Q(16), worksheet=V(21), skip_rows=2

    Old schema (original 7-sheet layout):
      video_id=J(9), yt_url=M(12), assessment=U(20), iv=T(19), worksheet=V(21), skip_rows=3
    """
    headers = [h.lower().strip() if h else "" for h in header_row]

    if any("youtube video id" in h for h in headers):
        vid  = next((i for i, h in enumerate(headers) if "youtube video id" in h), 10)
        url  = next((i for i, h in enumerate(headers) if "youtube video link" in h), 11)
        assess = next((i for i, h in enumerate(headers) if "wayground assessment link" in h), 13)
        iv   = next((i for i, h in enumerate(headers) if "wayground iv link" in h), 16)
        # worksheet URL lives in an unlabeled column (V=21) — same position in both schemas
        return {"video_id": vid, "yt_url": url, "assessment": assess,
                "iv": iv, "worksheet": 21, "skip_rows": 2}

    # Old schema defaults
    return {"video_id": 9, "yt_url": 12, "assessment": 20,
            "iv": 19, "worksheet": 21, "skip_rows": 3}


# ── Sheet reading ─────────────────────────────────────────────────────────────
def extract_video_id(url):
    if not url:
        return None
    patterns = [
        r"(?:v=|/v/)([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"shorts/([a-zA-Z0-9_-]{11})",
    ]
    for pat in patterns:
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return None


def read_sheet(sheets_service, sheet_id, sheet_range):
    """Read the given range and return list of row dicts.

    Auto-detects column schema from the header row:
    - Old schema: video_id=J(9), yt_url=M(12), assessment=U(20), iv=T(19), worksheet=V(21)
    - New schema: video_id=K(10), yt_url=L(11), assessment=N(13), iv=Q(16), worksheet=V(21)
    """
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=sheet_id, range=sheet_range
    ).execute()
    rows = result.get("values", [])
    if not rows:
        print("Sheet/tab is empty.")
        return []

    schema = _detect_schema(rows[0])
    skip_rows = schema["skip_rows"]
    print(f"  Schema: video_id=col{schema['video_id']} assess=col{schema['assessment']} iv=col{schema['iv']} skip={skip_rows} rows")

    def cell(row, idx):
        val = row[idx].strip() if idx < len(row) and row[idx] else ""
        val = re.sub(r'\s+&utm_\w+=[^\s]*', '', val)
        return val

    data = []
    for i, row in enumerate(rows):
        if i < skip_rows:
            continue
        video_id = cell(row, schema["video_id"])
        yt_url   = cell(row, schema["yt_url"])
        if not re.match(r'^[a-zA-Z0-9_-]{11}$', video_id):
            video_id = extract_video_id(yt_url) or ""
        if not video_id:
            continue
        if not yt_url:
            yt_url = f"https://www.youtube.com/watch?v={video_id}"
        data.append({
            "row_num": i + 1,
            "yt_url": yt_url,
            "video_id": video_id,
            "assessment": cell(row, schema["assessment"]),
            "iv":         cell(row, schema["iv"]),
            "worksheet":  cell(row, schema["worksheet"]),
        })
    return data


# ── URL shortening ────────────────────────────────────────────────────────────
_short_cache = {}

def shorten_url(url):
    if not url:
        return url
    if url in _short_cache:
        return _short_cache[url]
    try:
        resp = requests.get(f"https://tinyurl.com/api-create.php?url={url}", timeout=10)
        resp.raise_for_status()
        short = resp.text.strip()
        _short_cache[url] = short
        return short
    except Exception as e:
        print(f"  ⚠ URL shortening failed for {url[:60]}…: {e}")
        return url


# ── Comment building ──────────────────────────────────────────────────────────
def build_comment(row, creator_name, sheet_url):
    """Build comment text for a single row, only including non-empty resource links."""
    lines = [COMMENT_TEMPLATE_HEADER]
    if row["assessment"]:
        lines.append(f"📝 Formative Assessment: {row['assessment']}")
    if row["iv"]:
        lines.append(f"🎬 Interactive Video: {row['iv']}")
    if row["worksheet"]:
        lines.append(f"🖨️ Printable Worksheet: {row['worksheet']}")
    lines.append(COMMENT_TEMPLATE_FOOTER.format(creator_name=creator_name))
    lines.append(sheet_url)
    return "\n".join(lines)


# ── YouTube posting ───────────────────────────────────────────────────────────
def post_comment(youtube, video_id, text):
    body = {
        "snippet": {
            "videoId": video_id,
            "topLevelComment": {
                "snippet": {"textOriginal": text}
            }
        }
    }
    resp = youtube.commentThreads().insert(part="snippet", body=body).execute()
    return resp["id"]


# ── Progress tracking ─────────────────────────────────────────────────────────
def load_progress(progress_file):
    if os.path.exists(progress_file):
        with open(progress_file) as f:
            data = json.load(f)
        # Migrate old list format → dict format {video_id: comment_id_or_null}
        if isinstance(data.get("done"), list):
            data["done"] = {vid: None for vid in data["done"]}
        return data
    return {"done": {}}


def save_progress(progress, progress_file):
    with open(progress_file, "w") as f:
        json.dump(progress, f, indent=2)


# ── Comment verification ──────────────────────────────────────────────────────
def check_comment_status(youtube, comment_id):
    """Return moderation status string for a posted comment ID."""
    try:
        resp = youtube.comments().list(part="snippet", id=comment_id).execute()
        items = resp.get("items", [])
        if items:
            return items[0]["snippet"].get("moderationStatus", "unknown")
        return "not_found"
    except Exception as e:
        return f"error: {e}"


def has_wayground_comment(youtube, video_id, marker="Wayground"):
    """Return True if a public Wayground comment exists on this video."""
    try:
        resp = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            searchTerms=marker,
            maxResults=5,
        ).execute()
        return len(resp.get("items", [])) > 0
    except Exception:
        return True  # assume present on error — avoid double-posting


# ── Public API ────────────────────────────────────────────────────────────────
def run(
    sheet_id,
    sheet_range,
    creator_name,
    tab_gid,
    utm_sheet_id=None,
    progress_file=None,
    dry_run=True,
    limit=0,
    delay_seconds=2,
    sa_key_file=None,
    oauth_client_file=None,
    token_file=None,
):
    """
    Post comments for all videos in a single sheet tab.

    Args:
        sheet_id: Google Sheet ID to read from
        sheet_range: e.g. "'Tab Name'!A:V"
        creator_name: Creator channel name (used in comment text)
        tab_gid: Numeric GID of the tab (for #gid= URL anchor)
        utm_sheet_id: Sheet ID for the "overall sheet" link (defaults to sheet_id)
        progress_file: Path to per-creator progress JSON
        dry_run: If True, print comments but don't post
        limit: Max videos to process (0 = all)
        delay_seconds: Pause between posts
        sa_key_file: Service account key path
        oauth_client_file: OAuth client secret path
        token_file: OAuth token cache path
    """
    utm_sheet_id = utm_sheet_id or sheet_id
    sheet_url = f"https://docs.google.com/spreadsheets/d/{utm_sheet_id}/edit#gid={tab_gid}"

    if progress_file is None:
        slug = re.sub(r'[^a-z0-9]+', '_', creator_name.lower()).strip('_')
        progress_file = os.path.join(os.path.dirname(__file__), f"progress_{slug}.json")

    print(f"=== YT Commenter: {creator_name} ===")
    print(f"  Sheet: {sheet_id}  Range: {sheet_range}")
    print(f"  Tab URL: {sheet_url}")
    print(f"  DRY_RUN={dry_run}  LIMIT={limit}  DELAY={delay_seconds}s")
    print()

    print("Authenticating with Sheets API...")
    sheets = auth_sheets(sa_key_file)
    print("  ✓ Sheets OK")

    if not dry_run:
        print("Authenticating with YouTube API (OAuth2)...")
        youtube = auth_youtube(oauth_client_file, token_file)
        print("  ✓ YouTube OK")
    else:
        youtube = None
        print("  (YouTube auth skipped in dry-run mode)")
    print()

    print(f"Reading {sheet_range}...")
    rows = read_sheet(sheets, sheet_id, sheet_range)
    print(f"  Found {len(rows)} rows with valid YouTube URLs")
    print()

    progress = load_progress(progress_file)
    done_set = set(progress["done"].keys())

    pending = [r for r in rows if r["video_id"] not in done_set
               and (r["assessment"] or r["iv"] or r["worksheet"])]
    if limit > 0:
        pending = pending[:limit]
    print(f"  {len(done_set)} already done, {len(pending)} to process this run")
    print()

    posted = 0
    skipped = 0
    for row in pending:
        vid = row["video_id"]
        comment = build_comment(row, creator_name, sheet_url)

        if dry_run:
            print(f"[DRY-RUN] Row {row['row_num']} — {vid}")
            print(f"  URL: {row['yt_url']}")
            print(f"  Comment preview:\n{comment}\n")
            posted += 1
            continue

        try:
            cid = post_comment(youtube, vid, comment)
            print(f"[POSTED] Row {row['row_num']} — {vid} → comment {cid}")
            progress["done"][vid] = cid
            save_progress(progress, progress_file)
            posted += 1
        except HttpError as e:
            status = e.resp.status
            reason = e.error_details[0].get("reason", "") if e.error_details else ""

            if status == 403 and reason == "commentsDisabled":
                print(f"[SKIP] Row {row['row_num']} — {vid}: comments disabled")
                skipped += 1
            elif status == 404:
                print(f"[SKIP] Row {row['row_num']} — {vid}: video not found")
                skipped += 1
            elif status == 403 and "quotaExceeded" in str(e):
                print(f"\n⚠️  Quota exceeded after {posted} comments.")
                print("  Re-run this script later — it will resume from where it stopped.")
                save_progress(progress, progress_file)
                sys.exit(1)
            else:
                print(f"[ERROR] Row {row['row_num']} — {vid}: {e}")
                skipped += 1
        except Exception as e:
            print(f"[ERROR] Row {row['row_num']} — {vid}: {e}")
            skipped += 1

        time.sleep(delay_seconds)

    print()
    print(f"Done. Posted: {posted}, Skipped: {skipped}, Total done: {len(progress['done'])}")
    return posted, skipped


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    run(
        sheet_id=SHEET_ID,
        sheet_range=SHEET_RANGE,
        creator_name=CREATOR_NAME,
        tab_gid=SHEET_GID,
        utm_sheet_id=SHEET_ID,
        progress_file=PROGRESS_FILE,
        dry_run=DRY_RUN,
        limit=LIMIT,
        delay_seconds=DELAY_SECONDS,
    )


if __name__ == "__main__":
    main()
