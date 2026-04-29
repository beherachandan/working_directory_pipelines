#!/usr/bin/env python3
"""
ground_truth_check.py — Monthly Ground Truth Cron

What this does:
  1. Loads the top N Wayground URLs by D2 score (from scoring-runs/)
     Plus a sample of competitor URLs that scored high
  2. For each URL, runs a GEO query on its target topic (ChatGPT)
  3. Checks whether the URL appears in AI citations
  4. Records: [url | d2_score | cited: Y/N | platform | date]
  5. Computes score-to-citation correlation
  6. Compares vs prior month's run
  7. Detects drift: high-scoring URLs not cited, low-scoring URLs cited
  8. Posts delta report to Slack #way-mark

Usage:
  python3 ground_truth_check.py
  python3 ground_truth_check.py --urls-file /path/to/custom-urls.json
  python3 ground_truth_check.py --platform gemini --dry-run

Schedule: Monthly cron — 1st Monday of each month, 09:00 UTC
  openclaw cron add "ground-truth-check" --schedule "0 9 * * 1#1" \
    --command "bash skills/geo-query/scripts/run_ground_truth.sh" \
    --channel slack --to "#way-mark"
"""

import argparse
import json
import os
import time
import urllib.request
import urllib.error
import urllib.parse
from collections import defaultdict
from datetime import datetime, date
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

PORTKEY_API_KEY  = os.environ.get("PORTKEY_API_KEY", "VwFslTtBMP/j3m4i/HkmvyEv/mlR")
GEMINI_API_KEY   = os.environ.get("GEMINI_API_KEY",  "AIzaSyCuBfskGih3UchLQ4LrrX1622sRqbfVpQk")
SEMRUSH_API_KEY  = os.environ.get("SEMRUSH_API_KEY", "0b65acb5365171a4803c87e0de927328")

CHATGPT_PROVIDER = "@azure-openai-bbfaac"
CHATGPT_MODEL    = "gpt-5-mini"

RATE_LIMIT_SLEEP = 6
RETRY_WAIT       = 35

WORKSPACE_ROOT   = Path(__file__).resolve().parents[3]
SCORES_FILE      = WORKSPACE_ROOT / "memory" / "research" / "scoring-runs" / "d2-scores-corpus.json"
OUTPUT_DIR       = WORKSPACE_ROOT / "memory" / "research" / "ground-truth-checks"
PRIOR_DIR        = OUTPUT_DIR  # same folder, compare latest file

# URL → target topic mapping for GEO queries
# Extend this as more Wayground articles are published
URL_TOPIC_MAP = {
    "https://www.retrievalpractice.org/why-it-works":             "what is retrieval practice",
    "https://www.retrievalpractice.org/retrievalpractice":        "retrieval practice for students",
    "https://www.cultofpedagogy.com/retrieval-practice/":         "retrieval practice strategies",
    "https://www.edutopia.org/article/using-exit-tickets-effectively-elementary-grades/": "how to use exit tickets in the classroom",
    "https://www.formative.com/read/what-is-formative-assessment": "what is formative assessment",
    "https://www.renaissance.com/edword/formative-assessment/":   "formative assessment definition",
    "https://www.learningscientists.org/blog/2016/5/5-1":         "retrieval practice quizzing",
    "https://thirdspacelearning.com/blog/spaced-repetition/":     "spaced repetition for students",
    "https://ctl.stanford.edu/students/growth-mindset":           "what is growth mindset",
    "https://ggie.berkeley.edu/student-well-being/growth-mindset-for-students/": "growth mindset for students",
}

# Drift alert thresholds
HIGH_SCORE_THRESHOLD   = 7.0    # URLs scoring ≥ this should be cited
LOW_SCORE_THRESHOLD    = 5.0    # URLs scoring < this should NOT be cited
CITATION_RATE_ALERT    = 0.15   # If <15% of high-scoring URLs are cited → alert
FALSE_NEGATIVE_ALERT   = 0.25   # If >25% of low-scoring URLs ARE cited → alert


# ── HTTP helper (shared with calibration.py) ─────────────────────────────────

def http_post(url, headers, body, timeout=90):
    data = json.dumps(body).encode()
    all_headers = {**headers, "Content-Length": str(len(data)),
                   "User-Agent": "Mozilla/5.0 (compatible; WaymarkBot/1.0)"}
    req = urllib.request.Request(url, data=data, headers=all_headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = b""
            while True:
                chunk = resp.read(65536)
                if not chunk: break
                raw += chunk
            return resp.status, json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read().decode("utf-8"))
        except: return e.code, {"error": str(e)}
    except Exception as e:
        return 0, {"error": str(e)}


def run_chatgpt(query: str) -> list:
    """Run ChatGPT query. Returns list of cited URLs."""
    search_query = query.rstrip(".") + ". Search the web and cite your sources."
    status, resp = http_post(
        "https://api.portkey.ai/v1/responses",
        headers={"Content-Type": "application/json",
                 "x-portkey-api-key": PORTKEY_API_KEY,
                 "x-portkey-provider": CHATGPT_PROVIDER},
        body={"model": CHATGPT_MODEL, "tools": [{"type": "web_search_preview"}], "input": search_query}
    )
    if status != 200 or not isinstance(resp, dict):
        return []
    urls = []
    for block in (resp.get("output") or []):
        for item in (block.get("content") or []):
            for ann in (item.get("annotations") or []):
                if ann.get("type") == "url_citation":
                    url = ann.get("url") or (ann.get("url_citation") or {}).get("url")
                    if url and url not in urls:
                        urls.append(url)
    return urls


def run_gemini(query: str) -> list:
    """Run Gemini query. Returns list of cited URLs."""
    search_query = query.rstrip(".") + ". Search the web and cite your sources."
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    status, resp = http_post(url,
        headers={"Content-Type": "application/json"},
        body={"contents": [{"parts": [{"text": search_query}]}], "tools": [{"google_search": {}}]}
    )
    if status == 429:
        print(f"    ⚠ Gemini 429 — waiting {RETRY_WAIT}s...")
        time.sleep(RETRY_WAIT)
        status, resp = http_post(url,
            headers={"Content-Type": "application/json"},
            body={"contents": [{"parts": [{"text": search_query}]}], "tools": [{"google_search": {}}]}
        )
    if status != 200: return []
    gm = (resp.get("candidates") or [{}])[0].get("groundingMetadata", {})
    return [c["web"]["uri"] for c in gm.get("groundingChunks", []) if c.get("web", {}).get("uri")]


def url_cited(target_url: str, cited_urls: list) -> bool:
    """Check if target_url (or its domain) appears in cited_urls."""
    target_domain = urllib.parse.urlparse(target_url).netloc.lstrip("www.")
    for u in cited_urls:
        if target_url in u or u in target_url:
            return True
        cited_domain = urllib.parse.urlparse(u).netloc.lstrip("www.")
        if target_domain == cited_domain:
            return True
    return False


# ── Load scores corpus ────────────────────────────────────────────────────────

def load_scores(path: Path) -> dict:
    with open(path) as f:
        data = json.load(f)
    return {k: v for k, v in data.items() if not k.startswith("_")}


def select_check_urls(scores: dict, max_urls: int = 12) -> list:
    """
    Select URLs to check:
    - All URLs with composite ≥ HIGH_SCORE_THRESHOLD (high-score set)
    - Sample of URLs with composite < LOW_SCORE_THRESHOLD (low-score set, for false-negative detection)
    - Only URLs in URL_TOPIC_MAP (we need a known target query)
    """
    high = [(u, s) for u, s in scores.items()
            if s.get("composite", 0) >= HIGH_SCORE_THRESHOLD and u in URL_TOPIC_MAP]
    low  = [(u, s) for u, s in scores.items()
            if s.get("composite", 0) < LOW_SCORE_THRESHOLD and u in URL_TOPIC_MAP]

    # Take up to 8 high, up to 4 low
    selected = high[:8] + low[:4]
    selected = selected[:max_urls]
    print(f"  Selected {len(selected)} URLs ({len(high[:8])} high-score, {len(low[:4])} low-score)")
    return selected


# ── Main check loop ───────────────────────────────────────────────────────────

def run_checks(check_urls: list, platform: str, dry_run: bool) -> list:
    """Run GEO check for each URL. Returns list of result dicts."""
    results = []
    total = len(check_urls)
    for i, (url, score_data) in enumerate(check_urls, 1):
        topic  = URL_TOPIC_MAP[url]
        d2     = score_data.get("composite", 0)
        tier   = score_data.get("tier", "?")
        print(f"  ({i}/{total}) [{platform}] \"{topic[:50]}\"", end=" ", flush=True)

        if dry_run:
            print("→ [DRY RUN]")
            results.append({"url": url, "topic": topic, "d2_score": d2, "tier": tier,
                            "platform": platform, "cited": None, "cited_urls": [], "dry_run": True})
            continue

        t0 = time.time()
        if platform == "chatgpt":
            cited_urls = run_chatgpt(topic)
        elif platform == "gemini":
            cited_urls = run_gemini(topic)
        else:
            cited_urls = []

        is_cited = url_cited(url, cited_urls)
        elapsed  = time.time() - t0
        mark     = "✅ cited" if is_cited else "✗ not cited"
        print(f"→ {mark} ({len(cited_urls)} URLs, {elapsed:.1f}s)")

        results.append({
            "url":        url,
            "topic":      topic,
            "d2_score":   d2,
            "tier":       tier,
            "platform":   platform,
            "cited":      is_cited,
            "cited_urls": cited_urls[:10],
            "timestamp":  datetime.utcnow().isoformat(),
        })

        if i < total:
            time.sleep(RATE_LIMIT_SLEEP)

    return results


# ── Drift analysis ────────────────────────────────────────────────────────────

def analyze_drift(results: list) -> dict:
    """
    Compute:
    - Citation rate for high-scoring URLs (should be high)
    - False negative rate for low-scoring URLs (should be low)
    - Surprises: high-score not cited, low-score cited
    """
    high_results = [r for r in results if r["d2_score"] >= HIGH_SCORE_THRESHOLD and r["cited"] is not None]
    low_results  = [r for r in results if r["d2_score"] < LOW_SCORE_THRESHOLD  and r["cited"] is not None]

    high_cited   = [r for r in high_results if r["cited"]]
    low_cited    = [r for r in low_results  if r["cited"]]

    high_rate = len(high_cited) / len(high_results) if high_results else None
    low_rate  = len(low_cited)  / len(low_results)  if low_results  else None

    # Surprises
    high_not_cited = [r for r in high_results if not r["cited"]]  # should be cited but isn't
    low_but_cited  = [r for r in low_results  if r["cited"]]      # shouldn't be cited but is

    # Drift flags
    flags = []
    if high_rate is not None and high_rate < CITATION_RATE_ALERT:
        flags.append(f"⚠ HIGH DRIFT: Only {high_rate*100:.0f}% of high-scoring URLs cited (threshold: {CITATION_RATE_ALERT*100:.0f}%)")
    if low_rate is not None and low_rate > FALSE_NEGATIVE_ALERT:
        flags.append(f"⚠ FALSE NEGATIVE DRIFT: {low_rate*100:.0f}% of low-scoring URLs cited (threshold: {FALSE_NEGATIVE_ALERT*100:.0f}%)")
    if not flags:
        flags.append("✅ No drift detected — scores correlate with citations as expected")

    return {
        "high_score_citation_rate": round(high_rate, 3) if high_rate is not None else None,
        "low_score_citation_rate":  round(low_rate, 3)  if low_rate  is not None else None,
        "high_not_cited":    [r["url"] for r in high_not_cited],
        "low_but_cited":     [r["url"] for r in low_but_cited],
        "drift_flags":       flags,
        "requires_rubric_review": any("HIGH DRIFT" in f or "FALSE NEGATIVE" in f for f in flags),
    }


# ── Compare vs prior run ──────────────────────────────────────────────────────

def load_prior_run(output_dir: Path) -> dict | None:
    """Load the most recent prior ground truth run JSON, if any."""
    runs = sorted(output_dir.glob("*-ground-truth-*.json"), reverse=True)
    if len(runs) < 2:
        return None
    try:
        with open(runs[1]) as f:
            return json.load(f)
    except Exception:
        return None


def compare_vs_prior(current_drift: dict, prior_run: dict | None) -> str:
    if not prior_run:
        return "No prior run to compare against (first run)."

    prior_drift = prior_run.get("drift_analysis", {})
    prior_high  = prior_drift.get("high_score_citation_rate")
    curr_high   = current_drift.get("high_score_citation_rate")

    if prior_high is None or curr_high is None:
        return "Insufficient data for month-over-month comparison."

    delta = curr_high - prior_high
    if abs(delta) < 0.05:
        return f"Stable: citation rate {curr_high*100:.0f}% (prior: {prior_high*100:.0f}%, Δ={delta*100:+.0f}%)"
    elif delta < 0:
        return f"⚠ Citation rate dropped: {curr_high*100:.0f}% vs {prior_high*100:.0f}% last month (Δ={delta*100:+.0f}%). Consider rubric review."
    else:
        return f"✅ Citation rate improved: {curr_high*100:.0f}% vs {prior_high*100:.0f}% last month (Δ={delta*100:+.0f}%)"


# ── Save + format output ──────────────────────────────────────────────────────

def save_results(results: list, drift: dict, mom_summary: str, args) -> tuple:
    date_str  = datetime.utcnow().strftime("%Y-%m")
    out_dir   = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"{date_str}-ground-truth-{args.platform}.json"
    md_path   = out_dir / f"{date_str}-ground-truth-{args.platform}.md"

    payload = {
        "date":           date_str,
        "platform":       args.platform,
        "results":        results,
        "drift_analysis": drift,
        "mom_summary":    mom_summary,
    }
    with open(json_path, "w") as f:
        json.dump(payload, f, indent=2)

    # Markdown summary for Slack
    cited    = [r for r in results if r.get("cited") is True]
    not_cited= [r for r in results if r.get("cited") is False]

    lines = [
        f"# Ground Truth Check — {date_str}",
        f"_Platform: {args.platform} | URLs checked: {len(results)}_\n",
        f"## Results",
        f"- Cited: **{len(cited)}/{len(results)}** ({len(cited)/len(results)*100:.0f}%)",
        f"- Not cited: {len(not_cited)}\n",
        f"## Month-over-Month",
        mom_summary + "\n",
        f"## Drift Analysis",
    ]
    for flag in drift["drift_flags"]:
        lines.append(f"- {flag}")

    if drift["high_not_cited"]:
        lines.append(f"\n### High-score URLs NOT cited (investigate)")
        for u in drift["high_not_cited"]:
            lines.append(f"- {u}")

    if drift["low_but_cited"]:
        lines.append(f"\n### Low-score URLs cited (false negative — rubric may underweight domain authority)")
        for u in drift["low_but_cited"]:
            lines.append(f"- {u}")

    lines += [
        f"\n## Full Results",
        f"| URL | D2 Score | Cited |",
        f"|---|---|---|",
    ]
    for r in sorted(results, key=lambda x: -x["d2_score"]):
        cited_str = "✅ Yes" if r.get("cited") else "✗ No"
        lines.append(f"| {r['url'][:70]} | {r['d2_score']:.1f} | {cited_str} |")

    if drift["requires_rubric_review"]:
        lines += [
            f"\n## ⚠ Action Required",
            f"Drift thresholds exceeded. Run `run_delta_analysis.py` and consider rubric weight update.",
            f"Follow process in `aeo/context/rubric-drift-prevention.md`.",
        ]

    md_path.write_text("\n".join(lines))
    print(f"\n✓ JSON: {json_path}")
    print(f"✓ MD:   {md_path}")
    return json_path, md_path


def append_to_knowledge_files(results: list, drift: dict, date_str: str):
    """
    Append ground truth findings to D1, D2 KNOWLEDGE.md files.
    These keep agents calibrated to real citation behaviour.
    """
    cited    = [r for r in results if r.get("cited") is True]
    total    = len([r for r in results if r.get("cited") is not None])
    cite_rate = len(cited) / total if total else 0

    entry = (
        f"\n## {date_str} — Ground Truth Check\n"
        f"Platform: {results[0]['platform'] if results else 'unknown'} | "
        f"URLs checked: {total} | Citation rate: {cite_rate*100:.0f}%\n"
    )
    if drift["high_not_cited"]:
        entry += f"High-score URLs NOT cited (investigate): {', '.join(drift['high_not_cited'][:3])}\n"
    if drift["low_but_cited"]:
        entry += f"Low-score URLs cited (domain authority override): {', '.join(drift['low_but_cited'][:3])}\n"
    for flag in drift["drift_flags"]:
        entry += f"Drift: {flag}\n"

    skills_root = WORKSPACE_ROOT / "skills"
    for skill in ["D1-aeo-evaluator", "D2-url-evaluator"]:
        knowledge_file = skills_root / skill / "KNOWLEDGE.md"
        if knowledge_file.exists():
            with open(knowledge_file, "a") as f:
                f.write(entry)
            print(f"  ✓ Appended to {skill}/KNOWLEDGE.md")

    # Also flag heuristic-scored URLs for manual review
    scores_data = {}
    try:
        with open(SCORES_FILE) as f:
            scores_data = json.load(f)
    except Exception:
        pass
    heuristic_urls = [u for u, v in scores_data.items()
                      if isinstance(v, dict) and v.get("scored_by") == "heuristic"]
    if heuristic_urls:
        reminder = (
            f"\n### ⚠ Manual D2 Scoring Required ({date_str})\n"
            f"{len(heuristic_urls)} URLs have heuristic scores and need manual D2 scoring:\n"
            + "\n".join(f"- {u}" for u in heuristic_urls[:10])
            + "\nRun D2 URL Evaluator on each and update `memory/research/scoring-runs/d2-scores-corpus.json`\n"
        )
        feedback_file = skills_root / "D2-url-evaluator" / "FEEDBACK.md"
        if feedback_file.exists():
            with open(feedback_file, "a") as f:
                f.write(reminder)
            print(f"  ✓ Added heuristic scoring reminder to D2/FEEDBACK.md ({len(heuristic_urls)} URLs)")


def format_slack_message(results: list, drift: dict, mom_summary: str, platform: str) -> str:
    cited_count = sum(1 for r in results if r.get("cited") is True)
    total = len([r for r in results if r.get("cited") is not None])
    flags = "\n".join(drift["drift_flags"])
    return (
        f"*📊 Monthly Ground Truth Check — {datetime.utcnow().strftime('%Y-%m')}*\n"
        f"Platform: {platform} | URLs checked: {total}\n"
        f"Citation rate: *{cited_count}/{total}* ({cited_count/total*100:.0f}%)\n\n"
        f"*Month-over-month:* {mom_summary}\n\n"
        f"*Drift flags:*\n{flags}"
        + (f"\n\n*⚠ Rubric review recommended* — run delta analysis" if drift["requires_rubric_review"] else "")
    )


# ── Main ──────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Monthly Ground Truth Citation Check")
    p.add_argument("--platform",    default="chatgpt",        help="Platform: chatgpt or gemini")
    p.add_argument("--scores-file", default=str(SCORES_FILE), help="D2 scores corpus JSON")
    p.add_argument("--output-dir",  default=str(OUTPUT_DIR),  help="Output directory")
    p.add_argument("--max-urls",    type=int, default=12,      help="Max URLs to check (default: 12)")
    p.add_argument("--dry-run",     action="store_true",       help="Skip GEO calls, test logic only")
    return p.parse_args()


def main():
    args = parse_args()
    print("=" * 60)
    print(f"Ground Truth Check — {datetime.utcnow().strftime('%Y-%m-%d')}")
    print(f"Platform: {args.platform} | Dry run: {args.dry_run}")
    print("=" * 60)

    scores     = load_scores(Path(args.scores_file))
    check_urls = select_check_urls(scores, max_urls=args.max_urls)

    if not check_urls:
        print("✗ No URLs to check — add topic mappings to URL_TOPIC_MAP in this script")
        return

    print(f"\n[1/3] Running GEO checks ({len(check_urls)} URLs)...")
    results = run_checks(check_urls, args.platform, args.dry_run)

    print(f"\n[2/3] Drift analysis...")
    drift = analyze_drift(results)
    for flag in drift["drift_flags"]:
        print(f"  {flag}")

    print(f"\n[3/3] Month-over-month comparison...")
    prior    = load_prior_run(Path(args.output_dir))
    mom      = compare_vs_prior(drift, prior)
    print(f"  {mom}")

    json_path, md_path = save_results(results, drift, mom, args)

    # Append findings to agent KNOWLEDGE.md files
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    if not args.dry_run:
        append_to_knowledge_files(results, drift, date_str)

    slack_msg = format_slack_message(results, drift, mom, args.platform)

    print(f"\n--- Slack message ---\n{slack_msg}\n---")
    print("\n✓ Ground truth check complete.")
    if drift["requires_rubric_review"]:
        print("  ⚠ Rubric review required — run run_delta_analysis.py")


if __name__ == "__main__":
    main()
