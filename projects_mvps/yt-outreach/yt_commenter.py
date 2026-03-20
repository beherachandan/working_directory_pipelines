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

# ── Config ────────────────────────────────────────────────────────────────────
SHEET_ID = "1tTpbj9MuKsS_5cM5AS1qodCnjKy9N23szTgfUSqee28"
SHEET_GID = 755464040
SHEET_RANGE = "'iteachalgebra top 120 videos'!A:V"
# Column map: A=title, J=video_id, M=yt_url, O=assessment, R=iv, V=worksheet
CREATOR_NAME = "iteachalgebra"
UTM_SHEET_URL = "https://docs.google.com/spreadsheets/d/1tTpbj9MuKsS_5cM5AS1qodCnjKy9N23szTgfUSqee28"

DRY_RUN = True                    # Set False for real posting
LIMIT = 0                         # 0 = all rows; start with 3-5 for testing
DELAY_SECONDS = 2                 # Pause between comments

CREDENTIALS_DIR = os.path.join(os.path.dirname(__file__), "credentials")
SA_KEY_FILE = os.path.join(CREDENTIALS_DIR, "service-account.json")
OAUTH_CLIENT_FILE = os.path.join(CREDENTIALS_DIR, "oauth-client.json")
TOKEN_FILE = os.path.join(CREDENTIALS_DIR, "token.json")
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")

SHEETS_SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
YOUTUBE_SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

COMMENT_TEMPLATE = """\
Teaching this topic? Wayground has FREE resources that will make your lesson practically plan itself.

📝 Formative Assessment: {assessment_link}
🎬 Interactive Video: {iv_link}
🖨️ Printable Worksheet: {worksheet_link}

Use them to check understanding or give your students the extra practice that actually lands. ❤️
Here is a curated sheet with these resources from {creator_name} and many more!"""
# Note: "sheet" in the last line should be a hyperlink to UTM_SHEET_URL when
# posting. YouTube comments support plain URLs (auto-linked), not markdown.
# We append the URL on a new line so it's clickable.


# ── Auth ──────────────────────────────────────────────────────────────────────
def auth_sheets():
    """Authenticate with Sheets API via service account."""
    creds = SACredentials.from_service_account_file(SA_KEY_FILE, scopes=SHEETS_SCOPES)
    return build("sheets", "v4", credentials=creds)


def auth_youtube():
    """Authenticate with YouTube API via OAuth2 (desktop flow)."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, YOUTUBE_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(OAUTH_CLIENT_FILE, YOUTUBE_SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)


# ── Sheet reading ─────────────────────────────────────────────────────────────
def extract_video_id(url):
    """Parse YouTube URL variants and return video ID, or None."""
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


def read_sheet(sheets_service):
    """Read the sheet and return list of row dicts."""
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=SHEET_ID, range=SHEET_RANGE
    ).execute()
    rows = result.get("values", [])
    if not rows:
        print("Sheet is empty.")
        return []

    def cell(row, idx):
        """Safely get cell value by index, cleaning up broken URL fragments."""
        val = row[idx].strip() if idx < len(row) and row[idx] else ""
        # Some cells have a space before &utm_term due to sheet formatting errors
        # e.g. "https://...campaign=foo &utm_term=defaultsheet" — strip the trailing junk
        val = re.sub(r'\s+&utm_\w+=[^\s]*', '', val)
        return val

    data = []
    for i, row in enumerate(rows):
        # Skip header rows (first 3 rows: header, info, category)
        if i < 3:
            continue
        # Col J (9) = video ID, Col M (12) = YouTube URL
        video_id = cell(row, 9)
        yt_url = cell(row, 12)
        if not video_id:
            # Likely a category header row — skip silently
            continue
        if not yt_url:
            yt_url = f"https://www.youtube.com/watch?v={video_id}"
        data.append({
            "row_num": i + 1,
            "yt_url": yt_url,
            "video_id": video_id,
            "assessment": cell(row, 20),   # Col U — Wayground Assessment Link (UTM-tagged)
            "iv": cell(row, 19),           # Col T — Wayground IV Link (UTM-tagged)
            "worksheet": cell(row, 21),    # Col V — Printable Worksheet Link (UTM-tagged)
        })
    return data


# ── URL shortening ───────────────────────────────────────────────────────────
_short_cache = {}

def shorten_url(url):
    """Shorten a URL via TinyURL. Caches results to avoid duplicate calls."""
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
def build_comment(row):
    """Build comment text for a single row."""
    text = COMMENT_TEMPLATE.format(
        assessment_link=shorten_url(row["assessment"]),
        iv_link=shorten_url(row["iv"]),
        worksheet_link=shorten_url(row["worksheet"]),
        creator_name=CREATOR_NAME,
    )
    # Append the UTM sheet URL on a new line so YouTube auto-links it
    text += f"\n{shorten_url(UTM_SHEET_URL)}"
    return text


# ── YouTube posting ───────────────────────────────────────────────────────────
def post_comment(youtube, video_id, text):
    """Post a top-level comment on a YouTube video. Returns comment ID."""
    body = {
        "snippet": {
            "videoId": video_id,
            "topLevelComment": {
                "snippet": {
                    "textOriginal": text,
                }
            }
        }
    }
    resp = youtube.commentThreads().insert(part="snippet", body=body).execute()
    return resp["id"]


# ── Progress tracking ─────────────────────────────────────────────────────────
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"done": []}


def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("=== Wayground YT Commenter ===")
    print(f"  DRY_RUN={DRY_RUN}  LIMIT={LIMIT}  DELAY={DELAY_SECONDS}s")
    print()

    # Auth
    print("Authenticating with Sheets API (service account)...")
    sheets = auth_sheets()
    print("  ✓ Sheets OK")

    if not DRY_RUN:
        print("Authenticating with YouTube API (OAuth2)...")
        youtube = auth_youtube()
        print("  ✓ YouTube OK")
    else:
        youtube = None
        print("  (YouTube auth skipped in dry-run mode)")

    print()

    # Read sheet
    print(f"Reading sheet {SHEET_ID}...")
    rows = read_sheet(sheets)
    print(f"  Found {len(rows)} rows with valid YouTube URLs")
    print()

    # Progress
    progress = load_progress()
    done_set = set(progress["done"])

    # Filter
    pending = [r for r in rows if r["video_id"] not in done_set]
    if LIMIT > 0:
        pending = pending[:LIMIT]
    print(f"  {len(done_set)} already done, {len(pending)} to process this run")
    print()

    posted = 0
    skipped = 0
    for row in pending:
        vid = row["video_id"]
        comment = build_comment(row)

        if DRY_RUN:
            print(f"[DRY-RUN] Row {row['row_num']} — {vid}")
            print(f"  URL: {row['yt_url']}")
            print(f"  Comment preview:\n{comment}\n")
            posted += 1
            continue

        try:
            cid = post_comment(youtube, vid, comment)
            print(f"[POSTED] Row {row['row_num']} — {vid} → comment {cid}")
            progress["done"].append(vid)
            save_progress(progress)
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
                save_progress(progress)
                sys.exit(1)
            else:
                print(f"[ERROR] Row {row['row_num']} — {vid}: {e}")
                skipped += 1
        except Exception as e:
            print(f"[ERROR] Row {row['row_num']} — {vid}: {e}")
            skipped += 1

        time.sleep(DELAY_SECONDS)

    print()
    print(f"Done. Posted: {posted}, Skipped: {skipped}, Total done: {len(progress['done'])}")


if __name__ == "__main__":
    main()
