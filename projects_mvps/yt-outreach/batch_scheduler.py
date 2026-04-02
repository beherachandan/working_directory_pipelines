#!/usr/bin/env python3
"""
Anti-spam batch scheduler for YouTube comment posting.

Spreads comments across a configurable time window with random delays between
batches and within batches to mimic organic behavior.

Usage:
  python batch_scheduler.py --dry-run                          # print schedule without posting
  python batch_scheduler.py --recheck                          # verify "done" videos, re-queue spam-filtered ones
  python batch_scheduler.py --mode fast --shard 0 --shards 2  # fast run, shard 0 of 2
  python batch_scheduler.py --mode moderate --shard 1 --shards 2
  python batch_scheduler.py                                    # live run (safe mode, all videos)
"""

import argparse
import datetime
import hashlib
import json
import os
import random
import sys
import time

import yt_commenter

# ── Config ────────────────────────────────────────────────────────────────────
CREDENTIALS_DIR = os.environ.get(
    "SHARED_CREDS_DIR",
    os.path.join(os.path.dirname(__file__), "credentials"),
)
OAUTH_CLIENT_FILE = os.path.join(CREDENTIALS_DIR, "oauth-client.json")
TOKEN_FILE = os.path.join(CREDENTIALS_DIR, "token.json")
SA_KEY_FILE = os.path.join(CREDENTIALS_DIR, "service-account.json")

STATE_FILE = os.path.join(os.path.dirname(__file__), "pipeline_state.json")

# ── Posting modes ─────────────────────────────────────────────────────────────
POSTING_MODES = {
    "safe": {               # conservative default — ~79 comments over 20h
        "batch_min": 3,
        "batch_max": 8,
        "intra_min": 30,    # seconds between posts within a batch
        "intra_max": 90,
        "inter_min": 45,    # minutes between batches
        "inter_max": 120,
        "window_hours": 20,
        "daily_limit": 150,
    },
    "moderate": {           # ~100–130 comments over 15h
        "batch_min": 5,
        "batch_max": 10,
        "intra_min": 30,
        "intra_max": 60,
        "inter_min": 20,
        "inter_max": 45,
        "window_hours": 15,
        "daily_limit": 150,
    },
    "fast": {               # ~250–350 comments over 6h
        "batch_min": 8,
        "batch_max": 15,
        "intra_min": 15,
        "intra_max": 45,
        "inter_min": 10,
        "inter_max": 25,
        "window_hours": 6,
        "daily_limit": 500,
    },
}


# ── State loading ─────────────────────────────────────────────────────────────
def load_pipeline_state():
    if not os.path.exists(STATE_FILE):
        print(f"No pipeline_state.json found at {STATE_FILE}")
        sys.exit(1)
    with open(STATE_FILE) as f:
        return json.load(f)


def find_progress_files():
    """Return all progress_*.json files in the script directory."""
    base = os.path.dirname(__file__)
    return [
        os.path.join(base, f)
        for f in os.listdir(base)
        if f.startswith("progress_") and f.endswith(".json") and f != "progress.json"
    ]


# ── Work queue building ───────────────────────────────────────────────────────
def load_all_pending_work(sheets_service=None):
    """
    Read pipeline_state.json to find all UTM sheet IDs and their tab info.
    For each tab, read the sheet and collect rows not yet in the progress file.
    Returns list of work items:
      {sheet_id, tab_name, tab_gid, creator_name, sheet_url, progress_file, row}
    """
    state = load_pipeline_state()
    work_items = []

    if sheets_service is None:
        sheets_service = yt_commenter.auth_sheets(SA_KEY_FILE)

    for source_id, sheet_state in state.items():
        utm_sheet_id = sheet_state.get("utm_sheet_id")
        if not utm_sheet_id:
            continue

        sheet_title = sheet_state.get("title", source_id)

        # Derive tabs from progress files — look for matching progress files
        # Progress files are named: progress_{sheet_slug}_{tab_slug}.json
        import re
        sheet_slug = re.sub(r'[^a-z0-9]+', '_', sheet_title.lower()).strip('_')

        base = os.path.dirname(__file__)
        sheet_progress_files = [
            f for f in os.listdir(base)
            if f.startswith(f"progress_{sheet_slug}_") and f.endswith(".json")
        ]

        for pf_name in sheet_progress_files:
            pf_path = os.path.join(base, pf_name)
            # Extract tab slug from filename: progress_{sheet_slug}_{tab_slug}.json
            tab_slug = pf_name[len(f"progress_{sheet_slug}_"):-len(".json")]

            progress = yt_commenter.load_progress(pf_path)
            done_set = set(progress["done"].keys())

            # Find tab in state — we need gid and creator_name
            # These aren't stored in pipeline_state.json currently,
            # so we read the sheet metadata to find the tab
            tab_name = tab_slug.replace("_", " ")  # approximate — will be corrected below

            # Build sheet_url from utm_sheet_id; gid not stored — use 0 as placeholder
            sheet_url = f"https://docs.google.com/spreadsheets/d/{utm_sheet_id}"

            # Derive creator name from sheet title
            creator_name = _creator_from_title(sheet_title)

            # Try to read the sheet to get pending rows
            # Tab name from slug is approximate; try the slug and common variants
            rows = _try_read_tab(sheets_service, utm_sheet_id, tab_slug, tab_name)
            if rows is None:
                continue

            pending = [
                r for r in rows
                if r["video_id"] not in done_set
                and (r["assessment"] or r["iv"] or r["worksheet"])
            ]

            for row in pending:
                work_items.append({
                    "sheet_id": utm_sheet_id,
                    "tab_name": tab_name,
                    "creator_name": creator_name,
                    "sheet_url": sheet_url,
                    "progress_file": pf_path,
                    "row": row,
                })

    return work_items


def _creator_from_title(sheet_title):
    """Extract a clean creator name from a sheet title."""
    import re
    # Strip "Copy of"
    name = re.sub(r'(?i)^copy\s+of\s+', '', sheet_title).strip()
    name = re.sub(r'(?i)\s*[-–]\s*copy\s*$', '', name).strip()
    # Strip boilerplate suffixes
    name = re.sub(
        r'(?i)\s*(most popular youtube videos.*|youtube channel.*|youtube videos.*'
        r'|videos?\s*[-–].*|w[/\s]+activities?.*|top\s+\d+\s+videos?\s*)$',
        '', name
    ).strip()
    return name or sheet_title


def _try_read_tab(sheets_service, sheet_id, tab_slug, tab_name_approx):
    """Try reading a sheet tab, handling title→slug mismatch gracefully."""
    # First try: get actual tab names from sheet metadata
    try:
        meta = yt_commenter._api_call_with_backoff(
            lambda: sheets_service.spreadsheets().get(spreadsheetId=sheet_id).execute()
        )
        import re
        for s in meta["sheets"]:
            actual_name = s["properties"]["title"]
            actual_slug = re.sub(r'[^a-z0-9]+', '_', actual_name.lower()).strip('_')
            if actual_slug == tab_slug:
                sheet_range = f"'{actual_name}'!A:V"
                return yt_commenter.read_sheet(sheets_service, sheet_id, sheet_range)
    except Exception as e:
        print(f"  ⚠ Could not read tab for slug '{tab_slug}': {e}")
    return None


# ── Sharding ──────────────────────────────────────────────────────────────────
def shard_work_items(items, shard, num_shards):
    """
    Deterministically partition items by video_id hash.
    Same video always maps to the same shard across re-runs.
    """
    return [
        item for item in items
        if int(hashlib.md5(item["row"]["video_id"].encode()).hexdigest(), 16) % num_shards == shard
    ]


# ── Scheduling ────────────────────────────────────────────────────────────────
def plan_schedule(work_items, mode_cfg):
    """
    Assign random posting times to work_items within the mode's window.
    Returns sorted list of (post_datetime, work_item).
    """
    items = list(work_items)
    random.shuffle(items)
    items = items[:mode_cfg["daily_limit"]]

    now = datetime.datetime.now()
    cursor = now + datetime.timedelta(seconds=random.randint(30, 300))
    window_end = now + datetime.timedelta(hours=mode_cfg["window_hours"])

    schedule = []
    while items:
        batch_size = random.randint(mode_cfg["batch_min"], mode_cfg["batch_max"])
        batch = items[:batch_size]
        items = items[batch_size:]

        for item in batch:
            if cursor > window_end:
                break
            schedule.append((cursor, item))
            cursor += datetime.timedelta(
                seconds=random.randint(mode_cfg["intra_min"], mode_cfg["intra_max"])
            )

        if cursor > window_end:
            break

        # Long gap before next batch
        cursor += datetime.timedelta(
            minutes=random.randint(mode_cfg["inter_min"], mode_cfg["inter_max"])
        )

    return schedule


def print_schedule(schedule):
    """Print the planned schedule without executing."""
    if not schedule:
        print("No pending work found.")
        return
    first = schedule[0][0]
    last = schedule[-1][0]
    duration = last - first
    print(f"\nSchedule: {len(schedule)} comments over {duration}")
    print(f"  Start: {first.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  End:   {last.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    for i, (post_time, item) in enumerate(schedule, 1):
        vid = item["row"]["video_id"]
        creator = item["creator_name"]
        print(f"  {i:>4}. {post_time.strftime('%H:%M:%S')}  {vid}  ({creator})")


# ── Execution ─────────────────────────────────────────────────────────────────
def execute_schedule(schedule, youtube, dry_run=False):
    """
    Execute the schedule, sleeping until each post_time, then posting.
    Returns (posted_items, skipped, errors) where posted_items is a list of dicts.
    """
    posted_items = []
    skipped = 0
    errors = 0

    for i, (post_time, item) in enumerate(schedule, 1):
        row = item["row"]
        vid = row["video_id"]
        creator = item["creator_name"]
        sheet_url = item["sheet_url"]
        progress_file = item["progress_file"]

        wait = (post_time - datetime.datetime.now()).total_seconds()
        if wait > 60:
            mins = wait / 60
            print(f"\n  [{i}/{len(schedule)}] ⏰  Next post at {post_time.strftime('%H:%M:%S')} "
                  f"(~{mins:.0f} min away) — {vid}")
            time.sleep(wait)
        elif wait > 0:
            time.sleep(wait)

        comment = yt_commenter.build_comment(row, creator, sheet_url)

        if dry_run:
            print(f"  [{i}/{len(schedule)}] [DRY-RUN] {vid}  ({creator})")
            posted_items.append({
                "video_id": vid,
                "comment_id": None,
                "creator": creator,
                "posted_at": datetime.datetime.now().isoformat(),
            })
            continue

        try:
            cid = yt_commenter.post_comment(youtube, vid, comment)
            print(f"  [{i}/{len(schedule)}] [POSTED] {vid} → {cid}  ({creator})")
            # Update progress file
            progress = yt_commenter.load_progress(progress_file)
            progress["done"][vid] = cid
            yt_commenter.save_progress(progress, progress_file)
            posted_items.append({
                "video_id": vid,
                "comment_id": cid,
                "creator": creator,
                "posted_at": datetime.datetime.now().isoformat(),
            })
        except Exception as e:
            from googleapiclient.errors import HttpError
            if isinstance(e, HttpError):
                status = e.resp.status
                reason = e.error_details[0].get("reason", "") if e.error_details else ""
                if status == 403 and "quotaExceeded" in str(e):
                    print(f"\n  ⚠️  Quota exceeded after {len(posted_items)} comments. Re-run tomorrow.")
                    break
                elif status in (403, 404):
                    print(f"  [{i}/{len(schedule)}] [SKIP] {vid}: {reason or status}")
                    skipped += 1
                    continue
            print(f"  [{i}/{len(schedule)}] [ERROR] {vid}: {e}")
            errors += 1

    print(f"\nDone. Posted: {len(posted_items)}, Skipped: {skipped}, Errors: {errors}")
    return posted_items, skipped, errors


# ── Result logging ────────────────────────────────────────────────────────────
def write_result_log(mode_name, shard, num_shards, started_at, posted_items, skipped, errors):
    """Write batch_results_{mode}_{timestamp}.json for later comparison."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(
        os.path.dirname(__file__),
        f"batch_results_{mode_name}_{timestamp}.json"
    )
    result = {
        "mode": mode_name,
        "shard": shard,
        "num_shards": num_shards,
        "started_at": started_at,
        "finished_at": datetime.datetime.now().isoformat(),
        "posted": posted_items,
        "summary": {
            "posted": len(posted_items),
            "skipped": skipped,
            "errors": errors,
        },
    }
    with open(filename, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nResult log written: {filename}")
    return filename


# ── Re-check mode ─────────────────────────────────────────────────────────────
def recheck_done(youtube, progress_files=None):
    """
    For each video in all progress "done" dicts, check if a Wayground comment
    is still publicly visible. Remove those that have been spam-filtered.
    Returns count of videos cleared back to pending.
    """
    if progress_files is None:
        progress_files = find_progress_files()

    if not progress_files:
        print("No progress files found.")
        return 0

    print(f"Re-checking {len(progress_files)} progress file(s)...")
    cleared = 0
    total_checked = 0

    for pf_path in sorted(progress_files):
        data = yt_commenter.load_progress(pf_path)
        done = data["done"]  # dict {video_id: comment_id_or_null}
        still_done = {}
        file_cleared = 0

        for vid, cid in done.items():
            total_checked += 1
            if cid:
                # We have a comment ID — check its status directly
                status = yt_commenter.check_comment_status(youtube, cid)
                is_live = (status == "published")
            else:
                # Old progress without comment ID — search for Wayground comment
                is_live = yt_commenter.has_wayground_comment(youtube, vid)

            if is_live:
                still_done[vid] = cid
            else:
                file_cleared += 1
                cleared += 1
                print(f"  [REQUEUE] {vid} — comment not visible (status: {cid or 'searched'})")

        if file_cleared:
            data["done"] = still_done
            yt_commenter.save_progress(data, pf_path)
            print(f"  {os.path.basename(pf_path)}: {file_cleared} cleared")
        else:
            print(f"  {os.path.basename(pf_path)}: all {len(done)} OK")

        # Small delay to avoid hammering the API
        time.sleep(0.5)

    print(f"\nChecked {total_checked} videos. Cleared {cleared} back to pending.")
    return cleared


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Anti-spam batch comment scheduler")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print schedule without posting")
    parser.add_argument("--recheck", action="store_true",
                        help="Check all done videos for live comments, re-queue spam-filtered ones")
    parser.add_argument("--mode", choices=list(POSTING_MODES.keys()), default="safe",
                        help="Posting speed preset (default: safe)")
    parser.add_argument("--shard", type=int, default=None,
                        help="Only process shard N of --shards total (0-indexed)")
    parser.add_argument("--shards", type=int, default=None,
                        help="Total number of shards (use with --shard)")
    args = parser.parse_args()

    # Validate shard args
    if (args.shard is None) != (args.shards is None):
        parser.error("--shard and --shards must be used together")
    if args.shard is not None and args.shard >= args.shards:
        parser.error(f"--shard must be < --shards (got {args.shard} >= {args.shards})")

    mode_cfg = POSTING_MODES[args.mode]

    # Auth YouTube (always needed for recheck or posting)
    print("Authenticating with YouTube API...")
    youtube = yt_commenter.auth_youtube(OAUTH_CLIENT_FILE, TOKEN_FILE)
    print("  ✓ YouTube OK\n")

    if args.recheck:
        progress_files = find_progress_files()
        recheck_done(youtube, progress_files)
        sys.exit(0)

    # Build work queue
    print("Loading pending work from pipeline_state.json...")
    sheets_service = yt_commenter.auth_sheets(SA_KEY_FILE)
    work_items = load_all_pending_work(sheets_service)
    print(f"  Found {len(work_items)} pending comment(s)")

    # Apply sharding if requested
    shard = args.shard
    num_shards = args.shards
    if shard is not None:
        work_items = shard_work_items(work_items, shard, num_shards)
        print(f"  Shard {shard}/{num_shards}: {len(work_items)} item(s) in this shard\n")
    else:
        shard = None
        num_shards = None
        print()

    if not work_items:
        print("Nothing to do.")
        sys.exit(0)

    # Plan schedule
    schedule = plan_schedule(work_items, mode_cfg)
    print(f"Mode: {args.mode}  |  Window: {mode_cfg['window_hours']}h  "
          f"|  Limit: {mode_cfg['daily_limit']}  |  Planned: {len(schedule)} comment(s)\n")

    if args.dry_run:
        print_schedule(schedule)
        sys.exit(0)

    print_schedule(schedule)
    print("\nStarting execution...")
    started_at = datetime.datetime.now().isoformat()
    posted_items, skipped, errors = execute_schedule(schedule, youtube, dry_run=False)

    # Write result log for A/B comparison
    write_result_log(args.mode, shard, num_shards, started_at, posted_items, skipped, errors)


if __name__ == "__main__":
    main()
