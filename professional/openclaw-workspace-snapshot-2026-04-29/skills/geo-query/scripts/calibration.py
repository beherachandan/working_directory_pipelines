#!/usr/bin/env python3
"""
calibration.py — GEO Calibration Runner

What this does:
  1. Takes a topic prompt (e.g. "formative assessment")
  2. Generates N precise query variations via LLM (same article scope, minor phrasing shifts)
  3. Runs each variation on Gemini + ChatGPT, K times each
  4. Frequency analysis: URLs cited in ≥70% of runs = GOLD (consistently cited)
  5. SERP cross-reference: checks gold URLs against SEMrush organic rankings (rank 1-20)
  6. Splits into HIGH performers (rank 1-10) vs LOW (rank 11-20+) vs NOT-RANKED
  7. D2 rubric scores are loaded from a pre-scored file (run D2 separately per URL)
  8. Delta analysis: which rubric dimensions separate cited vs not-cited URLs most
  9. Outputs: JSON results + markdown summary → memory/research/geo-runs/

Usage:
  python3 calibration.py --topic "formative assessment" --variations 4 --runs 3
  python3 calibration.py --topic "retrieval practice" --variations 5 --runs 5 --platforms gemini,chatgpt

Options:
  --topic       Topic to calibrate on (required)
  --variations  Number of query variations to generate (default: 4)
  --runs        Number of times to run each variation per platform (default: 3)
  --platforms   Comma-separated: gemini,chatgpt (default: chatgpt)
  --scores-file Path to pre-scored D2 JSON (optional — skips delta analysis if absent)
  --output-dir  Where to save results (default: memory/research/geo-runs/)
  --threshold   Citation frequency threshold for GOLD (default: 0.7 = 70%)
  --dry-run     Generate variations and show plan, don't run GEO calls
  --compare     Path to existing calibration JSON to merge and compare (e.g. Gemini results against ChatGPT baseline)

Design notes:
  - Variations must be "same article scope" — one article should cover all of them
  - Variations differ in phrasing only (question form, synonym, teacher vs student angle)
  - NOT topic pivots — those would be different calibration runs
  - Self-learning: delta analysis output feeds back into aeo/context/aeo-scoring-rubric.md
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

PORTKEY_API_KEY   = os.environ.get("PORTKEY_API_KEY", "VwFslTtBMP/j3m4i/HkmvyEv/mlR")
GEMINI_API_KEY    = os.environ.get("GEMINI_API_KEY",  "AIzaSyCuBfskGih3UchLQ4LrrX1622sRqbfVpQk")
SEMRUSH_API_KEY   = os.environ.get("SEMRUSH_API_KEY", "0b65acb5365171a4803c87e0de927328")

GEMINI_MODEL      = "gemini-2.0-flash"
CHATGPT_PROVIDER  = "@azure-openai-bbfaac"
CHATGPT_MODEL     = "gpt-5-mini"

GOLD_THRESHOLD    = 0.70   # URL must appear in ≥70% of runs to be GOLD
                           # Note: auto-adjusted down for small run counts (see adaptive_threshold())
RATE_LIMIT_SLEEP  = 6      # seconds between GEO calls (free tier safety)
RETRY_WAIT        = 35     # seconds to wait on 429 (free tier resets ~30s)

WORKSPACE_ROOT    = Path(__file__).resolve().parents[3]   # geo-query/scripts → workspace root
OUTPUT_DIR        = WORKSPACE_ROOT / "memory" / "research" / "geo-runs"

# ── HTTP helper ───────────────────────────────────────────────────────────────

def http_post(url, headers, body, timeout=90):
    data = json.dumps(body).encode()
    all_headers = {
        **headers,
        "Content-Length": str(len(data)),
        "User-Agent": "Mozilla/5.0 (compatible; WaymarkBot/1.0)",
    }
    req  = urllib.request.Request(url, data=data, headers=all_headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = b""
            while True:
                chunk = resp.read(65536)
                if not chunk:
                    break
                raw += chunk
            return resp.status, json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            raw = e.read()
            return e.code, json.loads(raw.decode("utf-8"))
        except Exception:
            return e.code, {"error": str(e)}
    except Exception as e:
        return 0, {"error": str(e)}


# ── Step 1: Generate query variations via Portkey/Gemini ──────────────────────

def generate_variations(topic: str, n: int) -> list[str]:
    """
    Generate N precise query variations of a topic.
    Rule: all variations must be answerable by a single article — same scope, different phrasing.
    """
    print(f"\n[1/5] Generating {n} query variations for: \"{topic}\"")

    prompt = f"""You are a search query analyst. Generate exactly {n} search query variations for the topic: "{topic}"

Rules:
- All variations must be answerable by ONE article (same scope, same depth)
- Vary phrasing only: question form, synonyms, audience angle (teacher/student), context framing
- Do NOT pivot to subtopics or adjacent topics — that would require a different article
- Keep queries natural, as a real person would type them
- Each must be distinct enough to surface different URL results from search engines

Return ONLY a JSON array of strings, no explanation:
["variation 1", "variation 2", ...]"""

    # Use direct Gemini API for variation generation (Portkey strips too much)
    status, resp = http_post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}",
        headers={"Content-Type": "application/json"},
        body={"contents": [{"parts": [{"text": prompt}]}]}
    )
    # Normalise to OpenAI-style for uniform parsing below
    if status == 200:
        text = (resp.get("candidates") or [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        resp = {"choices": [{"message": {"content": text}}]}

    if status != 200:
        print(f"  ⚠ LLM call failed ({status}), falling back to rule-based variations")
        return _rule_based_variations(topic, n)

    content = resp.get("choices", [{}])[0].get("message", {}).get("content", "")
    try:
        # Strip markdown code fences if present
        content = content.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        variations = json.loads(content)
        if isinstance(variations, list) and len(variations) >= n:
            variations = variations[:n]
            print(f"  ✓ Generated {len(variations)} variations:")
            for i, v in enumerate(variations):
                print(f"    [{i+1}] {v}")
            return variations
    except Exception as e:
        print(f"  ⚠ Failed to parse LLM output ({e}), falling back to rule-based")

    return _rule_based_variations(topic, n)


def _rule_based_variations(topic: str, n: int) -> list[str]:
    """Deterministic fallback if LLM fails."""
    templates = [
        f"what is {topic}",
        f"how does {topic} work",
        f"{topic} definition and examples",
        f"teaching {topic} to students",
        f"benefits of {topic} for teachers",
    ]
    variations = templates[:n]
    print(f"  ✓ Rule-based variations: {variations}")
    return variations


# ── Step 2: GEO Runs ──────────────────────────────────────────────────────────

def run_gemini(query: str) -> list[str]:
    """Run query on Gemini direct API. Returns list of cited URLs."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
    status, resp = http_post(
        url,
        headers={"Content-Type": "application/json"},
        body={
            "contents": [{"parts": [{"text": query}]}],
            "tools":    [{"google_search": {}}],
        }
    )

    if status == 429:
        print(f"    ⚠ Gemini 429 — waiting {RETRY_WAIT}s...")
        time.sleep(RETRY_WAIT)
        status, resp = http_post(
            url,
            headers={"Content-Type": "application/json"},
            body={"contents": [{"parts": [{"text": query}]}], "tools": [{"google_search": {}}]}
        )

    if status != 200:
        print(f"    ✗ Gemini error {status}: {resp.get('error', {}).get('message', '')[:80]}")
        return []

    gm     = (resp.get("candidates") or [{}])[0].get("groundingMetadata", {})
    chunks = gm.get("groundingChunks", [])
    urls   = [c["web"]["uri"] for c in chunks if c.get("web", {}).get("uri")]
    return urls


def run_chatgpt(query: str) -> list:
    """Run query on ChatGPT via Portkey Responses API. Returns list of cited URLs."""
    status, resp = http_post(
        "https://api.portkey.ai/v1/responses",
        headers={
            "Content-Type":       "application/json",
            "x-portkey-api-key":  PORTKEY_API_KEY,
            "x-portkey-provider": CHATGPT_PROVIDER,
        },
        body={
            "model":  CHATGPT_MODEL,
            "tools":  [{"type": "web_search_preview"}],
            "input":  query,
        }
    )

    if not isinstance(resp, dict):
        print(f"    ✗ ChatGPT error {status}: (non-dict) — retrying in 10s...")
        time.sleep(10)
        status, resp = http_post(
            "https://api.portkey.ai/v1/responses",
            headers={
                "Content-Type":       "application/json",
                "x-portkey-api-key":  PORTKEY_API_KEY,
                "x-portkey-provider": CHATGPT_PROVIDER,
            },
            body={"model": CHATGPT_MODEL, "tools": [{"type": "web_search_preview"}], "input": query},
            timeout=90
        )
        if not isinstance(resp, dict):
            print(f"    ✗ ChatGPT retry also failed")
            return []
    if status != 200:
        err = resp.get("error") or {}
        err_msg = err.get("message", str(resp)[:80]) if isinstance(err, dict) else str(err)[:80]
        print(f"    ✗ ChatGPT error {status}: {err_msg}")
        return []

    urls = []
    # Responses API shape: output[].content[].annotations[].url_citation
    for block in (resp.get("output") or []):
        for item in (block.get("content") or []):
            for ann in (item.get("annotations") or []):
                if ann.get("type") == "url_citation":
                    url = ann.get("url") or (ann.get("url_citation") or {}).get("url")
                    if url and url not in urls:
                        urls.append(url)
    return urls


def run_geo(query: str, platform: str) -> dict:
    """Run a single GEO query. Returns {platform, query, urls, timestamp}."""
    print(f"    → [{platform}] \"{query[:60]}\"", end=" ", flush=True)
    t0 = time.time()

    # Append search instruction to force web retrieval + citations
    search_query = query.rstrip(".") + ". Search the web and cite your sources."

    if platform == "gemini":
        urls = run_gemini(search_query)
    elif platform == "chatgpt":
        urls = run_chatgpt(search_query)
    else:
        urls = []

    elapsed = time.time() - t0
    print(f"→ {len(urls)} URLs ({elapsed:.1f}s)")
    return {"platform": platform, "query": query, "urls": urls, "timestamp": datetime.utcnow().isoformat()}


# ── Step 3: Frequency Analysis ────────────────────────────────────────────────

def frequency_analysis(runs: list[dict], threshold: float) -> dict:
    """
    Count URL frequency across all runs per platform.
    Returns {platform: {url: {count, frequency, gold}}}
    """
    print(f"\n[3/5] Frequency analysis (gold threshold: {threshold*100:.0f}%)")

    by_platform = defaultdict(list)
    for run in runs:
        by_platform[run["platform"]].append(run)

    results = {}
    for platform, platform_runs in by_platform.items():
        total = len(platform_runs)
        url_counts = defaultdict(int)
        for run in platform_runs:
            for url in run["urls"]:
                url_counts[url] += 1

        freq_map = {}
        gold_count = 0
        for url, count in sorted(url_counts.items(), key=lambda x: -x[1]):
            freq = count / total
            is_gold = freq >= threshold
            if is_gold:
                gold_count += 1
            freq_map[url] = {"count": count, "total_runs": total, "frequency": round(freq, 3), "gold": is_gold}

        results[platform] = freq_map
        print(f"  {platform}: {total} runs, {len(freq_map)} unique URLs, {gold_count} GOLD (≥{threshold*100:.0f}%)")
        gold_urls = [u for u, v in freq_map.items() if v["gold"]]
        for u in gold_urls:
            print(f"    ⭐ {freq_map[u]['frequency']*100:.0f}%  {u[:90]}")

    return results


# ── Step 4: SERP Cross-reference via SEMrush ─────────────────────────────────

def semrush_url_organic(url: str, topic_keywords: list) -> dict:
    """
    Call SEMrush url_organic API for a single URL.
    Returns best matching keyword row for this topic: {rank, keyword, search_volume, traffic}
    Uses direct HTTP call to SEMrush API (same key OpenClaw uses internally).
    """
    semrush_key = SEMRUSH_API_KEY
    if not semrush_key:
        return {"rank": None, "keyword": None, "traffic": None, "note": "no_semrush_key"}

    # Build keyword filter: include rows where keyword contains any topic word
    # SEMrush filter format: +|Ph|Co|<word>
    # We use the first significant word of the topic
    topic_word = topic_keywords[0] if topic_keywords else ""
    filter_str = f"+|Ph|Co|{topic_word}" if topic_word else ""

    params = [
        ("type",             "url_organic"),
        ("key",              semrush_key),
        ("url",              url),
        ("database",         "us"),
        ("display_limit",    "10"),
        ("display_sort",     "po_asc"),       # best rank first
        ("export_columns",   "Ph,Po,Nq,Tr"),  # keyword, position, volume, traffic
        ("export_decode",    "1"),
    ]
    if filter_str:
        params.append(("display_filter", filter_str))

    query_string = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params)
    api_url = f"https://api.semrush.com/?{query_string}"

    try:
        req = urllib.request.Request(api_url)
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode()
    except Exception as e:
        return {"rank": None, "keyword": None, "traffic": None, "note": str(e)}

    # Parse CSV response: header row + data rows
    lines = [l.strip() for l in raw.strip().split("\n") if l.strip()]
    if len(lines) < 2 or "ERROR" in lines[0]:
        return {"rank": None, "keyword": None, "traffic": None, "note": lines[0] if lines else "empty"}

    headers = [h.strip() for h in lines[0].split(";")]
    best = None
    for line in lines[1:]:
        cols  = [c.strip() for c in line.split(";")]
        row   = dict(zip(headers, cols))
        try:
            rank = int(row.get("Po", 9999))
        except ValueError:
            continue
        if best is None or rank < best["rank"]:
            best = {
                "rank":          rank,
                "keyword":       row.get("Ph", ""),
                "search_volume": int(row.get("Nq", 0) or 0),
                "traffic":       int(row.get("Tr", 0) or 0),
            }

    return best or {"rank": None, "keyword": None, "traffic": None, "note": "no matching keywords"}


def semrush_rank_check(urls: list, topic: str) -> dict:
    """
    Check SEMrush organic rankings for gold URLs on topic keywords.
    Returns {url: {rank, keyword, search_volume, traffic}}
    """
    print(f"\n[4/5] SERP cross-reference via SEMrush (topic: \"{topic}\")")
    print(f"  Checking {len(urls)} gold URLs...")

    # Topic keywords to filter SEMrush results
    topic_keywords = [w for w in topic.lower().split() if len(w) > 3]

    results = {}
    for url in urls:
        data = semrush_url_organic(url, topic_keywords)
        results[url] = data
        rank_str = f"rank {data['rank']} — {data['keyword']}" if data.get('rank') else f"not ranked ({data.get('note', '')})"
        print(f"  {rank_str:<50}  {url[:70]}")
        time.sleep(1)  # gentle on SEMrush API

    return results


def classify_performers(gold_urls: list[str], serp_data: dict) -> dict:
    """
    Split gold URLs into HIGH (rank 1-10), LOW (rank 11-20), NOT_RANKED.
    """
    classified = {"HIGH": [], "LOW": [], "NOT_RANKED": []}
    for url in gold_urls:
        rank = (serp_data.get(url) or {}).get("rank")
        if rank is None:
            classified["NOT_RANKED"].append(url)
        elif rank <= 10:
            classified["HIGH"].append(url)
        else:
            classified["LOW"].append(url)
    return classified


# ── Step 5: Delta Analysis ────────────────────────────────────────────────────

def delta_analysis(gold_urls: list, all_urls: list, scores_file) -> dict:
    """
    Load pre-scored D2 scores. Compute per-dimension delta between gold vs non-gold.
    Most predictive dimensions = largest delta.
    """
    print(f"\n[5/5] Delta analysis")

    if not scores_file or not Path(scores_file).exists():
        print(f"  ⚠ No scores file provided — skipping delta analysis")
        print(f"  To enable: run D2 scorer on gold + non-gold URLs, save as JSON, pass --scores-file")
        return {}

    with open(scores_file) as f:
        scores = json.load(f)   # {url: {dim1: score, dim2: score, ...}}

    gold_set    = set(gold_urls)
    gold_scores = {u: s for u, s in scores.items() if u in gold_set}
    rest_scores = {u: s for u, s in scores.items() if u not in gold_set}

    if not gold_scores or not rest_scores:
        print(f"  ⚠ Not enough scored URLs to compute delta ({len(gold_scores)} gold, {len(rest_scores)} non-gold)")
        return {}

    # Get all dimension names
    dims = list(next(iter(scores.values())).keys())
    delta = {}
    for dim in dims:
        gold_avg = sum(s.get(dim, 0) for s in gold_scores.values()) / len(gold_scores)
        rest_avg = sum(s.get(dim, 0) for s in rest_scores.values()) / len(rest_scores)
        delta[dim] = {"gold_avg": round(gold_avg, 2), "rest_avg": round(rest_avg, 2), "delta": round(gold_avg - rest_avg, 2)}

    # Sort by delta descending (most predictive first)
    delta = dict(sorted(delta.items(), key=lambda x: -x[1]["delta"]))

    print(f"  Dimension deltas (gold vs non-gold, most predictive first):")
    for dim, d in delta.items():
        bar = "█" * int(d["delta"] * 2)
        print(f"    {dim:<35} gold={d['gold_avg']:.1f}  rest={d['rest_avg']:.1f}  Δ={d['delta']:+.2f}  {bar}")

    return delta


# ── Output ────────────────────────────────────────────────────────────────────

def save_results(topic, variations, all_runs, freq, performers, delta, args):
    date_str  = datetime.utcnow().strftime("%Y-%m-%d")
    slug      = topic.lower().replace(" ", "-")[:30]
    out_dir   = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"{date_str}-calibration-{slug}.json"
    md_path   = out_dir / f"{date_str}-calibration-{slug}.md"

    # ── JSON ──────────────────────────────────────────────────────────────────
    result = {
        "topic":      topic,
        "date":       date_str,
        "config":     {"variations": args.variations, "runs": args.runs, "platforms": args.platforms, "threshold": args.threshold},
        "variations": variations,
        "runs":       all_runs,
        "frequency":  freq,
        "performers": performers,
        "delta":      delta,
    }
    with open(json_path, "w") as f:
        json.dump(result, f, indent=2)

    # ── Markdown summary ──────────────────────────────────────────────────────
    md = [f"# Calibration Run — {topic}", f"_Date: {date_str}_\n"]
    md.append(f"## Config\n- Variations: {args.variations}\n- Runs per variation: {args.runs}\n- Platforms: {args.platforms}\n- Gold threshold: {args.threshold*100:.0f}%\n")
    md.append(f"## Query Variations\n" + "\n".join(f"{i+1}. {v}" for i, v in enumerate(variations)) + "\n")

    for platform, freq_map in freq.items():
        gold = [(u, v) for u, v in freq_map.items() if v["gold"]]
        md.append(f"## {platform.title()} — Gold URLs ({len(gold)})")
        if gold:
            for url, v in sorted(gold, key=lambda x: -x[1]["frequency"]):
                md.append(f"- {v['frequency']*100:.0f}% ({v['count']}/{v['total_runs']} runs)  {url}")
        else:
            md.append("_(none above threshold)_")
        md.append("")

    if performers:
        md.append("## Performer Classification (SERP)")
        for tier, urls in performers.items():
            md.append(f"### {tier} ({len(urls)})")
            for u in urls:
                md.append(f"- {u}")
        md.append("")

    if delta:
        md.append("## Dimension Delta (most predictive → least)")
        md.append("| Dimension | Gold avg | Rest avg | Δ |")
        md.append("|---|---|---|---|")
        for dim, d in delta.items():
            md.append(f"| {dim} | {d['gold_avg']} | {d['rest_avg']} | {d['delta']:+.2f} |")
        md.append("")
        top_dim = next(iter(delta))
        md.append(f"**Most predictive dimension:** `{top_dim}` (Δ = {delta[top_dim]['delta']:+.2f})\n")
        md.append("### Rubric Update Recommendation")
        md.append(f"Consider increasing weight of `{top_dim}` in `aeo/context/aeo-scoring-rubric.md`.")
        md.append("Run 4-5 topics before updating rubric — average deltas across topics first.\n")

    with open(md_path, "w") as f:
        f.write("\n".join(md))

    print(f"\n✓ JSON saved: {json_path}")
    print(f"✓ Summary:    {md_path}")
    return json_path, md_path


# ── Compare runs ─────────────────────────────────────────────────────────────

def compare_runs(result_path: Path, other_path: Path):
    """
    Merge two calibration JSON outputs (e.g. chatgpt vs gemini) and compare:
    - URLs that appear in BOTH = high-confidence gold (platform-agnostic)
    - URLs only in one = platform-specific citation pattern
    - Frequency delta = how much platforms agree
    """
    with open(result_path) as f: run_a = json.load(f)
    with open(other_path)  as f: run_b = json.load(f)

    print("\n" + "=" * 60)
    print("CROSS-PLATFORM COMPARISON")
    print(f"  A: {result_path.name}")
    print(f"  B: {other_path.name}")
    print("=" * 60)

    # Collect all cited URLs per run, with frequency
    def gold_urls(run):
        out = {}
        for platform, freq_map in run.get("frequency", {}).items():
            for url, v in freq_map.items():
                if url not in out or v["frequency"] > out[url]["frequency"]:
                    out[url] = {**v, "platform": platform}
        return out

    urls_a = gold_urls(run_a)
    urls_b = gold_urls(run_b)
    all_urls = set(urls_a) | set(urls_b)

    both     = sorted([u for u in all_urls if u in urls_a and u in urls_b],
                      key=lambda u: -(urls_a[u]["frequency"] + urls_b[u]["frequency"]))
    only_a   = sorted([u for u in all_urls if u in urls_a and u not in urls_b],
                      key=lambda u: -urls_a[u]["frequency"])
    only_b   = sorted([u for u in all_urls if u in urls_b and u not in urls_a],
                      key=lambda u: -urls_b[u]["frequency"])

    print(f"\n⭐ BOTH platforms ({len(both)}) — highest confidence:")
    for u in both[:10]:
        fa = urls_a[u]["frequency"]
        fb = urls_b[u]["frequency"]
        print(f"  A={fa*100:.0f}%  B={fb*100:.0f}%  {u[:85]}")

    print(f"\n🟠 Only in A [{run_a.get('config',{}).get('platforms','?')}] ({len(only_a)}):")
    for u in only_a[:8]:
        print(f"  {urls_a[u]['frequency']*100:.0f}%  {u[:90]}")

    print(f"\n🔵 Only in B [{run_b.get('config',{}).get('platforms','?')}] ({len(only_b)}):")
    for u in only_b[:8]:
        print(f"  {urls_b[u]['frequency']*100:.0f}%  {u[:90]}")

    # Agreement score
    agreement = len(both) / max(len(urls_a), len(urls_b), 1)
    print(f"\nPlatform agreement score: {agreement*100:.0f}% ({len(both)} shared / {max(len(urls_a),len(urls_b))} max unique)")
    if agreement > 0.5:
        print("✓ High agreement — gold URLs are platform-agnostic signals")
    elif agreement > 0.25:
        print("⚠ Moderate agreement — some platform-specific citation patterns")
    else:
        print("⚠ Low agreement — platforms cite very different sources, treat separately")

    # Write comparison to file
    compare_path = result_path.parent / f"{result_path.stem}-vs-{other_path.stem}-comparison.md"
    lines = [
        f"# Cross-Platform Comparison",
        f"- A: `{result_path.name}`",
        f"- B: `{other_path.name}`",
        f"- Agreement: {agreement*100:.0f}%\n",
        f"## Shared URLs (both platforms)",
    ] + [f"- A={urls_a[u]['frequency']*100:.0f}%  B={urls_b[u]['frequency']*100:.0f}%  {u}" for u in both[:15]] + [
        f"\n## Only in A",
    ] + [f"- {urls_a[u]['frequency']*100:.0f}%  {u}" for u in only_a[:10]] + [
        f"\n## Only in B",
    ] + [f"- {urls_b[u]['frequency']*100:.0f}%  {u}" for u in only_b[:10]]
    compare_path.write_text("\n".join(lines))
    print(f"\n✓ Comparison saved: {compare_path}")


# ── Main ──────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="GEO Calibration Runner")
    p.add_argument("--topic",       required=True,               help="Topic to calibrate (e.g. 'formative assessment')")
    p.add_argument("--variations",  type=int,   default=4,       help="Number of query variations (default: 4)")
    p.add_argument("--runs",        type=int,   default=3,       help="Runs per variation per platform (default: 3)")
    p.add_argument("--platforms",   default="chatgpt",           help="Comma-separated platforms (default: chatgpt)")
    p.add_argument("--scores-file", default=None,                help="Path to pre-scored D2 JSON for delta analysis")
    p.add_argument("--output-dir",  default=str(OUTPUT_DIR),     help="Output directory")
    p.add_argument("--threshold",   type=float, default=GOLD_THRESHOLD, help="Gold citation threshold (default: 0.7)")
    p.add_argument("--dry-run",     action="store_true",         help="Generate variations and show plan, no GEO calls")
    p.add_argument("--compare",     default=None,                help="Path to existing calibration JSON to merge + compare")
    return p.parse_args()


def main():
    args     = parse_args()
    platforms = [p.strip() for p in args.platforms.split(",")]
    total_calls = args.variations * args.runs * len(platforms)

    print("=" * 60)
    print(f"GEO Calibration — {args.topic}")
    print(f"Variations: {args.variations}  |  Runs each: {args.runs}  |  Platforms: {platforms}")
    print(f"Total GEO calls: {total_calls}  |  Gold threshold: {args.threshold*100:.0f}%")
    print("=" * 60)

    # ── Step 1: Generate variations ───────────────────────────────────────────
    variations = generate_variations(args.topic, args.variations)

    if args.dry_run:
        print("\n[DRY RUN] Plan:")
        for v in variations:
            for platform in platforms:
                for r in range(args.runs):
                    print(f"  run {r+1}: [{platform}] {v}")
        print(f"\nTotal calls: {total_calls}. Run without --dry-run to execute.")
        return

    # ── Step 2: GEO runs ──────────────────────────────────────────────────────
    print(f"\n[2/5] Running {total_calls} GEO queries...")
    all_runs = []
    call_num = 0
    for variation in variations:
        for platform in platforms:
            for run_i in range(args.runs):
                call_num += 1
                print(f"  ({call_num}/{total_calls})", end=" ")
                result = run_geo(variation, platform)
                all_runs.append(result)
                if call_num < total_calls:
                    time.sleep(RATE_LIMIT_SLEEP)  # free tier rate limit

    # ── Step 3: Frequency analysis ────────────────────────────────────────────
    # Auto-adjust threshold for small run counts
    total_runs_per_platform = args.variations * args.runs
    effective_threshold = args.threshold
    if total_runs_per_platform < 20 and args.threshold >= 0.7:
        # Scale threshold to run count: needs ~20 total runs for 70% to be meaningful
        # 12 runs → ~44%, 15 runs → ~55%, 20 runs → ~70%
        effective_threshold = max(0.25, total_runs_per_platform / (total_runs_per_platform + 16))
        print(f"\n[auto] Adjusted gold threshold: {args.threshold*100:.0f}% → {effective_threshold*100:.0f}% (only {total_runs_per_platform} runs per platform)")
    freq = frequency_analysis(all_runs, effective_threshold)

    # Collect all gold URLs across platforms
    all_gold = list({url for pf in freq.values() for url, v in pf.items() if v["gold"]})

    # ── Step 4: SERP cross-reference ──────────────────────────────────────────
    serp_data   = semrush_rank_check(all_gold, args.topic)
    performers  = classify_performers(all_gold, serp_data)

    # ── Step 5: Delta analysis ────────────────────────────────────────────────
    all_cited = list({url for pf in freq.values() for url in pf})
    delta = delta_analysis(all_gold, all_cited, args.scores_file)

    # ── Save ──────────────────────────────────────────────────────────────────
    json_path, md_path = save_results(args.topic, variations, all_runs, freq, performers, delta, args)

    print("\n✓ Calibration complete.")
    if not delta:
        print("  Next step: run D2 scorer on gold URLs, pass --scores-file to enable delta analysis")
    else:
        print("  Next step: review dimension deltas → update aeo/context/aeo-scoring-rubric.md")
    print("  Repeat for 4-5 topics before updating rubric weights.\n")

    # ── Optional: compare against another platform's run ─────────────────────────
    if args.compare and Path(args.compare).exists():
        compare_runs(result_path=json_path, other_path=Path(args.compare))


if __name__ == "__main__":
    main()
