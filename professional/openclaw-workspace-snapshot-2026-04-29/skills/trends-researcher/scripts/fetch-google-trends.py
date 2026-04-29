#!/usr/bin/env python3
"""
Fetch rising/top queries from Google Trends via DataForSEO REST API.

Usage:
  python3 scripts/fetch-google-trends.py --seeds "teachers" "lesson plans" --time-range past_90_days
  python3 scripts/fetch-google-trends.py --seeds-file scripts/trend-seeds.json --time-range past_90_days --output outputs/trends/raw-90d.json
  python3 scripts/fetch-google-trends.py --seeds-file scripts/trend-seeds.json --time-range past_30_days --item-types queries_list topics_list
"""

import argparse
import json
import sys
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


def load_credentials():
    """
    Load DataForSEO credentials from ~/.openclaw/openclaw.json.
    Falls back to .mcp.json in the workspace root if present.
    """
    # Primary: openclaw.json
    openclaw_cfg = Path.home() / ".openclaw" / "openclaw.json"
    if openclaw_cfg.exists():
        with open(openclaw_cfg) as f:
            cfg = json.load(f)
        try:
            env = cfg["mcp"]["servers"]["dataforseo"]["env"]
            login = env.get("DATAFORSEO_LOGIN") or env.get("DATAFORSEO_USERNAME")
            password = env["DATAFORSEO_PASSWORD"]
            return login, password
        except (KeyError, TypeError):
            pass

    # Fallback: .mcp.json in workspace root (legacy)
    mcp_path = Path(__file__).parent.parent / ".mcp.json"
    if mcp_path.exists():
        with open(mcp_path) as f:
            cfg = json.load(f)
        dfs = cfg["mcpServers"]["dataforseo"]["env"]
        login = dfs.get("DATAFORSEO_LOGIN") or dfs.get("DATAFORSEO_USERNAME")
        return login, dfs["DATAFORSEO_PASSWORD"]

    raise FileNotFoundError(
        "DataForSEO credentials not found. "
        "Expected at ~/.openclaw/openclaw.json (mcp.servers.dataforseo.env) "
        "or <workspace>/.mcp.json (mcpServers.dataforseo.env)"
    )


BASE_URL = "https://api.dataforseo.com/v3/keywords_data/google_trends/explore/live"

ITEM_TYPE_MAP = {
    "queries_list": "google_trends_queries_list",
    "topics_list":  "google_trends_topics_list",
    "graph":        "google_trends_graph",
}


def _fetch_single_task(task, login, password):
    """Fetch one task. The /live endpoint only accepts one task per request."""
    resp = requests.post(
        BASE_URL,
        auth=(login, password),
        json=[task],
        headers={"Content-Type": "application/json"},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()


def fetch_trends(seeds, time_range, item_types, location="United States", search_type="web", workers=5):
    login, password = load_credentials()

    # Build one task per seed per item_type
    tasks = []
    for seed in seeds:
        for itype in item_types:
            full_type = ITEM_TYPE_MAP.get(itype, itype)
            tasks.append({
                "keywords": [seed],
                "location_name": location,
                "time_range": time_range,
                "type": search_type,
                "item_types": [full_type],
            })

    total = len(tasks)
    print(
        f"  {total} requests to send ({len(seeds)} seeds × {len(item_types)} item types)"
        f" — {workers} parallel workers",
        file=sys.stderr
    )

    all_results = []
    total_cost = 0.0
    completed = 0

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_fetch_single_task, t, login, password): t for t in tasks}
        for future in as_completed(futures):
            task_def = futures[future]
            completed += 1
            try:
                data = future.result()
            except Exception as e:
                print(f"  [{completed}/{total}] Error for {task_def['keywords']}: {e}", file=sys.stderr)
                continue

            total_cost += data.get("cost", 0)

            for task in data.get("tasks", []):
                if task.get("status_code") != 20000:
                    print(
                        f"  [{completed}/{total}] Task error: {task.get('status_message')}"
                        f" for {task.get('data', {}).get('keywords')}",
                        file=sys.stderr
                    )
                    continue

                result_list = task.get("result") or []
                if not result_list:
                    continue

                seed_kw      = task["data"]["keywords"][0]
                item_type_used = task["data"]["item_types"][0]
                time_r       = task["data"]["time_range"]

                items = result_list[0].get("items", [])
                if not items:
                    continue

                data_block = items[0].get("data", {})
                rising = data_block.get("rising", [])
                all_results.append({
                    "seed":      seed_kw,
                    "item_type": item_type_used,
                    "time_range": time_r,
                    "rising":    rising,
                    "top":       data_block.get("top", []),
                })
                print(
                    f"  [{completed}/{total}] {seed_kw} ({time_r}): {len(rising)} rising signals",
                    file=sys.stderr
                )

    return all_results, total_cost


def main():
    parser = argparse.ArgumentParser(description="Fetch Google Trends data via DataForSEO")
    parser.add_argument("--seeds", nargs="+", help="Seed keywords (space-separated)")
    parser.add_argument("--seeds-file", help="JSON file containing array of seed strings")
    parser.add_argument(
        "--time-range", default="past_90_days",
        choices=["past_7_days", "past_30_days", "past_90_days", "past_12_months", "past_5_years"]
    )
    parser.add_argument(
        "--item-types", nargs="+", default=["queries_list"],
        choices=["queries_list", "topics_list", "graph"]
    )
    parser.add_argument(
        "--search-type", default="web",
        choices=["web", "news", "youtube", "images", "froogle"]
    )
    parser.add_argument("--output", help="Output JSON file path (stdout if omitted)")
    args = parser.parse_args()

    if args.seeds_file:
        with open(args.seeds_file) as f:
            seeds = json.load(f)
    elif args.seeds:
        seeds = args.seeds
    else:
        parser.error("Provide --seeds or --seeds-file")

    print(
        f"Fetching Google Trends for {len(seeds)} seeds"
        f" | time_range={args.time_range}"
        f" | item_types={args.item_types}",
        file=sys.stderr
    )

    results, cost = fetch_trends(
        seeds=seeds,
        time_range=args.time_range,
        item_types=args.item_types,
        search_type=args.search_type,
    )

    output = {
        "fetched_at":    datetime.now(timezone.utc).isoformat(),
        "time_range":    args.time_range,
        "item_types":    args.item_types,
        "search_type":   args.search_type,
        "seeds_count":   len(seeds),
        "results_count": len(results),
        "api_cost_usd":  round(cost, 4),
        "results":       results,
    }

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        print(f"Saved {len(results)} results → {args.output}", file=sys.stderr)
    else:
        print(json.dumps(output, indent=2))

    print(f"Total API cost: ${cost:.4f}", file=sys.stderr)


if __name__ == "__main__":
    main()
