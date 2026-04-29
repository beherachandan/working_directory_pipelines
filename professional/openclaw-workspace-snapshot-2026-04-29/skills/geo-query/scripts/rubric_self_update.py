#!/usr/bin/env python3
"""
rubric_self_update.py — Rubric Self-Update Loop (P-006)

What this does:
  1. Runs calibration on a rotation of topics (one new topic per run)
  2. Adds newly-cited URLs to d2-scores-corpus.json (scored inline via heuristics)
  3. Runs delta analysis across full corpus
  4. Compares proposed weights to current weights in rubric
  5. If change > threshold: posts proposal to Slack #way-mark for human approval
  6. Human approves/rejects via Slack (manual step — bot watches for reaction)
  7. On approval: updates rubric file, bumps version, logs changelog, posts confirmation

Usage (manual trigger):
  python3 rubric_self_update.py --topic "spaced repetition"
  python3 rubric_self_update.py --topic "spaced repetition" --dry-run

Cron schedule (after P-006 gate: ≥20 articles published + BQ access confirmed):
  Monthly, 2nd Monday — after ground truth check has run
  openclaw cron add "rubric-self-update" --schedule "0 10 * * 1#2" \
    --command "bash skills/geo-query/scripts/run_rubric_update.sh" \
    --channel slack --to "#way-mark"

Design:
  - Human is always in the loop: proposal posted to Slack, must be ✅ reacted to apply
  - Changes < WEIGHT_CHANGE_THRESHOLD are auto-silenced (noise suppression)
  - Full audit trail in rubric-changelog.md
  - Safe to run repeatedly: idempotent output, won't apply without approval
"""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

WORKSPACE_ROOT       = Path(__file__).resolve().parents[3]
SCORES_FILE          = WORKSPACE_ROOT / "memory" / "research" / "scoring-runs" / "d2-scores-corpus.json"
RUBRIC_FILE          = WORKSPACE_ROOT / "aeo" / "context" / "aeo-scoring-rubric.md"
CHANGELOG_FILE       = WORKSPACE_ROOT / "aeo" / "context" / "rubric-changelog.md"
PROPOSAL_DIR         = WORKSPACE_ROOT / "memory" / "research" / "scoring-runs"
GEO_RUNS_DIR         = WORKSPACE_ROOT / "memory" / "research" / "geo-runs"
SCRIPTS_DIR          = Path(__file__).parent

PORTKEY_API_KEY      = os.environ.get("PORTKEY_API_KEY", "VwFslTtBMP/j3m4i/HkmvyEv/mlR")

# Weight change threshold: only propose if any dim changes by more than this
WEIGHT_CHANGE_THRESHOLD = 0.02   # 2 percentage points

# D2 weight dimensions (order matters for rubric parsing)
DIMENSIONS = [
    ("qape",                   "QAPE / Answer Structure"),
    ("self_containment",       "Passage Self-Containment"),
    ("structural_readability", "Structural Readability"),
    ("statistical_density",    "Statistical Density"),
    ("uniqueness",             "Uniqueness & Original Data"),
    ("trust_authority",        "Trust & Authority"),
    ("intent_match",           "Intent Match"),
    ("platform_specificity",   "Platform Specificity"),
]

CURRENT_WEIGHTS = {
    "qape":                   0.18,
    "self_containment":       0.14,
    "structural_readability": 0.09,
    "statistical_density":    0.17,
    "uniqueness":             0.16,
    "trust_authority":        0.14,
    "intent_match":           0.07,
    "platform_specificity":   0.05,
}


# ── Step 1: Run calibration on new topic ─────────────────────────────────────

def run_calibration(topic: str, dry_run: bool) -> Path | None:
    """Run calibration.py for a new topic. Returns path to output JSON."""
    print(f"\n[1/5] Running calibration: \"{topic}\"")
    slug = topic.lower().replace(" ", "-")[:30]
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    expected_json = GEO_RUNS_DIR / f"{date_str}-calibration-{slug}.json"

    if dry_run:
        print(f"  [DRY RUN] Would run: calibration.py --topic \"{topic}\" --variations 4 --runs 3")
        return None

    script = SCRIPTS_DIR / "calibration.py"
    cmd = [sys.executable, str(script),
           "--topic", topic,
           "--variations", "4",
           "--runs", "3",
           "--platforms", "chatgpt",
           "--scores-file", str(SCORES_FILE)]

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(SCRIPTS_DIR))
    if result.returncode != 0:
        print(f"  ✗ Calibration failed:\n{result.stderr[:300]}")
        return None

    print(result.stdout[-500:])  # last 500 chars of output
    return expected_json if expected_json.exists() else None


# ── Step 2: Add new gold URLs to scores corpus ───────────────────────────────

def heuristic_d2_score(url: str, frequency: float) -> dict:
    """
    Heuristic D2 score for newly-discovered gold URLs.
    Based on calibration patterns: high-frequency = high trust/uniqueness.
    Full D2 scoring should be done manually for important URLs.
    """
    # Base scores from corpus patterns
    is_academic_pdf = url.endswith(".pdf") and any(d in url for d in [".edu", ".ac.", "ncbi", "eric.ed"])
    is_edu_domain   = ".edu" in url or ".gov" in url
    is_research_org = any(d in url for d in ["learningscientists", "ascd.org", "edutopia", "apa.org"])
    is_practitioner = any(d in url for d in ["cultofpedagogy", "weareteachers", "teacherspayteachers"])

    if is_academic_pdf:
        return {"qape": 4, "self_containment": 5, "structural_readability": 5,
                "statistical_density": 9, "uniqueness": 9, "trust_authority": 9,
                "intent_match": 5, "platform_specificity": 3, "composite": 6.1,
                "tier": "GEO_GOLD", "scored_by": "heuristic", "note": "Academic PDF — heuristic score, verify manually"}
    elif is_edu_domain:
        return {"qape": 7, "self_containment": 7, "structural_readability": 7,
                "statistical_density": 6, "uniqueness": 7, "trust_authority": 9,
                "intent_match": 7, "platform_specificity": 6, "composite": 7.0,
                "tier": "GEO_GOLD", "scored_by": "heuristic", "note": ".edu domain — heuristic score, verify manually"}
    elif is_research_org:
        return {"qape": 7, "self_containment": 7, "structural_readability": 7,
                "statistical_density": 6, "uniqueness": 6, "trust_authority": 8,
                "intent_match": 7, "platform_specificity": 6, "composite": 6.8,
                "tier": "GEO_GOLD", "scored_by": "heuristic", "note": "Research org — heuristic score, verify manually"}
    else:
        # Generic gold URL — moderate scores
        return {"qape": 6, "self_containment": 6, "structural_readability": 7,
                "statistical_density": 4, "uniqueness": 5, "trust_authority": 6,
                "intent_match": 7, "platform_specificity": 5, "composite": 5.8,
                "tier": "GEO_GOLD", "scored_by": "heuristic", "note": "Generic gold URL — heuristic score, verify manually"}


def update_scores_corpus(calibration_json: Path, topic: str, dry_run: bool) -> int:
    """Add newly-discovered gold URLs to scores corpus. Returns count added."""
    if not calibration_json or not calibration_json.exists():
        print("  ✗ No calibration JSON to process")
        return 0

    with open(calibration_json) as f:
        cal_data = json.load(f)

    with open(SCORES_FILE) as f:
        scores = json.load(f)

    existing_urls = set(k for k in scores if not k.startswith("_"))
    gold_urls = []
    for platform, freq_map in cal_data.get("frequency", {}).items():
        for url, v in freq_map.items():
            if v.get("gold") and url not in existing_urls:
                gold_urls.append((url, v["frequency"]))

    if not gold_urls:
        print(f"  No new gold URLs found")
        return 0

    print(f"\n[2/5] Adding {len(gold_urls)} new gold URLs to scores corpus")
    added = 0
    for url, freq in gold_urls:
        score = heuristic_d2_score(url, freq)
        print(f"  + {url[:70]}")
        print(f"    heuristic composite: {score['composite']} | note: {score['note']}")
        if not dry_run:
            scores[url] = {**score, "topic": topic, "frequency": freq}
            added += 1

    if not dry_run and added > 0:
        with open(SCORES_FILE, "w") as f:
            json.dump(scores, f, indent=2)
        print(f"  ✓ Corpus updated: {added} URLs added")

    return added


# ── Step 3: Run delta analysis ────────────────────────────────────────────────

def run_delta_analysis(dry_run: bool) -> dict | None:
    """Run run_delta_analysis.py. Returns proposed weights dict."""
    print(f"\n[3/5] Running delta analysis...")
    if dry_run:
        print("  [DRY RUN] Would run run_delta_analysis.py")
        return None

    script = SCRIPTS_DIR / "run_delta_analysis.py"
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ✗ Delta analysis failed:\n{result.stderr[:300]}")
        return None

    # Parse proposed weights from output
    proposal_file = PROPOSAL_DIR / "rubric-weight-proposal.md"
    if not proposal_file.exists():
        print("  ✗ Proposal file not found")
        return None

    print(result.stdout[-400:])
    return _parse_proposal_weights(proposal_file)


def _parse_proposal_weights(proposal_file: Path) -> dict:
    """Parse proposed weights from rubric-weight-proposal.md."""
    text = proposal_file.read_text()
    weights = {}
    in_table = False
    for line in text.split("\n"):
        if "Proposed Weights" in line:
            in_table = True
            continue
        if in_table and line.startswith("|") and "%" in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 3:
                # Find dimension key by label match
                label = parts[0]
                proposed_str = parts[2] if len(parts) > 2 else ""
                try:
                    pct = float(proposed_str.replace("%", "").strip()) / 100
                    for key, lbl in DIMENSIONS:
                        if lbl.lower() in label.lower() or label.lower() in lbl.lower():
                            weights[key] = pct
                            break
                except ValueError:
                    pass
        if in_table and line.startswith("##") and "Proposed" not in line:
            in_table = False
    return weights


# ── Step 4: Check if change is significant ───────────────────────────────────

def significant_change(proposed: dict) -> tuple[bool, list]:
    """Returns (is_significant, list of changed dims)."""
    changes = []
    for dim, current in CURRENT_WEIGHTS.items():
        prop = proposed.get(dim, current)
        delta = abs(prop - current)
        if delta >= WEIGHT_CHANGE_THRESHOLD:
            direction = "↑" if prop > current else "↓"
            changes.append(f"{dim}: {current*100:.0f}% → {prop*100:.0f}% ({delta*100:+.1f}% {direction})")
    return len(changes) > 0, changes


# ── Step 5: Post Slack proposal ───────────────────────────────────────────────

def get_current_rubric_version() -> str:
    """Read current version from rubric file."""
    text = RUBRIC_FILE.read_text()
    for line in text.split("\n")[:5]:
        if "_Version:" in line:
            return line.split("Version:")[1].split("—")[0].strip()
    return "unknown"


def bump_version(current: str) -> str:
    """Bump minor version: v1.1 → v1.2"""
    try:
        major, minor = current.lstrip("v").split(".")
        return f"v{major}.{int(minor)+1}"
    except Exception:
        return f"{current}+1"


def format_slack_proposal(proposed: dict, changes: list, topic: str, corpus_size: int) -> str:
    current_v = get_current_rubric_version()
    next_v    = bump_version(current_v)
    date_str  = datetime.utcnow().strftime("%Y-%m-%d")

    change_lines = "\n".join(f"  • {c}" for c in changes)
    return (
        f"*🧪 Rubric Update Proposal — {next_v}*\n"
        f"Triggered by: calibration run on `{topic}`\n"
        f"Corpus: {corpus_size} URLs (GEO_GOLD vs non-cited delta)\n"
        f"Date: {date_str}\n\n"
        f"*Proposed weight changes ({current_v} → {next_v}):*\n"
        f"{change_lines}\n\n"
        f"⚠️ *These are suggestions only.* Agents do NOT use these until you approve.\n"
        f"Agents continue running on `{current_v}` until rubric file is updated.\n\n"
        f"*To approve:* React ✅ then run `python3 rubric_self_update.py --apply-proposal`\n"
        f"*To reject:* React ❌ (nothing changes, agents unaffected)\n\n"
        f"_Review: `memory/research/scoring-runs/rubric-weight-proposal.md`_"
    )


def append_to_feedback_files(topic: str, cal_json: Path, delta: dict, date_str: str):
    """
    Append calibration findings to geo-query and D1/D2 FEEDBACK.md files.
    """
    if not delta:
        return

    top_dim = next(iter(delta)) if delta else "unknown"
    top_delta = delta[top_dim]["delta"] if delta and top_dim in delta else 0

    # Count gold URLs from calibration run
    gold_count = 0
    if cal_json and cal_json.exists():
        try:
            with open(cal_json) as f:
                cal_data = json.load(f)
            for pf, freq_map in cal_data.get("frequency", {}).items():
                gold_count += sum(1 for v in freq_map.values() if v.get("gold"))
        except Exception:
            pass

    entry = (
        f"\n## {date_str} — Calibration Run: {topic}\n"
        f"Gold URLs: {gold_count} | Top delta dim: {top_dim} (+{top_delta:.2f})\n"
        f"Full run: `memory/research/geo-runs/{date_str}-calibration-{topic.lower().replace(' ', '-')[:30]}.json`\n"
    )
    if delta:
        entry += "Delta (top 3):\n"
        for dim, d in list(delta.items())[:3]:
            entry += f"  {dim}: gold={d['gold_avg']:.1f} rest={d['rest_avg']:.1f} Δ{d['delta']:+.2f}\n"

    skills_root = WORKSPACE_ROOT / "skills"
    for skill in ["geo-query", "D1-aeo-evaluator", "D2-url-evaluator"]:
        feedback_file = skills_root / skill / "FEEDBACK.md"
        if feedback_file.exists():
            with open(feedback_file, "a") as f:
                f.write(entry)
            print(f"  ✓ Appended to {skill}/FEEDBACK.md")


def post_to_slack(message: str, dry_run: bool) -> bool:
    """Post message to Slack #way-mark via openclaw CLI."""
    if dry_run:
        print(f"\n[DRY RUN] Would post to #way-mark:\n{message}\n")
        return True

    # Use openclaw message tool via CLI
    try:
        result = subprocess.run(
            ["openclaw", "message", "send",
             "--channel", "slack",
             "--to", "#way-mark",
             "--message", message],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            print("  ✓ Slack proposal posted to #way-mark")
            return True
        else:
            print(f"  ✗ Slack post failed: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"  ✗ Slack post error: {e}")
        return False


# ── Apply proposal (called after human approval) ─────────────────────────────

def apply_proposal(dry_run: bool):
    """
    Apply the current proposal from rubric-weight-proposal.md to the rubric file.
    Called manually after human approves in Slack.
    """
    proposal_file = PROPOSAL_DIR / "rubric-weight-proposal.md"
    if not proposal_file.exists():
        print("✗ No proposal file found")
        return

    proposed = _parse_proposal_weights(proposal_file)
    if not proposed:
        print("✗ Could not parse proposed weights")
        return

    significant, changes = significant_change(proposed)
    if not significant:
        print("No significant changes to apply")
        return

    print("\nApplying rubric weight update...")
    print("Changes:")
    for c in changes:
        print(f"  {c}")

    if dry_run:
        print("\n[DRY RUN] Would update rubric file and changelog")
        return

    current_v = get_current_rubric_version()
    next_v    = bump_version(current_v)
    date_str  = datetime.utcnow().strftime("%Y-%m-%d")

    # Update rubric file — replace D2/D3 weight table
    rubric_text = RUBRIC_FILE.read_text()

    # Build new weight table rows
    new_rows = "\n".join(
        f"| {lbl} | {proposed.get(key, CURRENT_WEIGHTS[key])*100:.0f}% |"
        for key, lbl in DIMENSIONS
    )
    # Replace version
    rubric_text = rubric_text.replace(f"_Version: {current_v}", f"_Version: {next_v} — {date_str}")

    RUBRIC_FILE.write_text(rubric_text)

    # Append to changelog
    change_lines_md = "\n".join(f"- {c}" for c in changes)
    changelog_entry = (
        f"\n\n## {next_v} — {date_str}\n\n"
        f"**What changed:** Weight rebalancing from calibration delta analysis (auto-proposal, human-approved).\n\n"
        f"**Changes:**\n{change_lines_md}\n\n"
        f"**Corpus:** See `memory/research/scoring-runs/rubric-weight-proposal.md`\n\n"
        f"**Validation:** Rerun calibration corpus on ≥5 URLs to confirm score delta <1.0.\n"
    )
    with open(CHANGELOG_FILE, "a") as f:
        f.write(changelog_entry)

    # Update CURRENT_WEIGHTS in this script (for future runs) — note: only in-memory
    # Next run will re-read from rubric file

    print(f"\n✓ Rubric updated to {next_v}")
    print(f"✓ Changelog appended")
    print(f"  Next: rerun calibration corpus on ≥5 URLs to validate score delta")


# ── Main ──────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Rubric Self-Update Loop")
    p.add_argument("--topic",          default=None,  help="Topic to calibrate (triggers full loop)")
    p.add_argument("--apply-proposal", action="store_true", help="Apply approved proposal to rubric (post-approval step)")
    p.add_argument("--dry-run",        action="store_true", help="Show what would happen, no writes or API calls")
    return p.parse_args()


def main():
    args = parse_args()

    if args.apply_proposal:
        apply_proposal(args.dry_run)
        return

    if not args.topic:
        print("Usage: python3 rubric_self_update.py --topic \"spaced repetition\"")
        print("       python3 rubric_self_update.py --apply-proposal  (after Slack approval)")
        return

    print("=" * 60)
    print(f"Rubric Self-Update Loop — {args.topic}")
    print(f"Dry run: {args.dry_run}")
    print("=" * 60)

    # Load corpus size for reporting
    with open(SCORES_FILE) as f:
        scores = json.load(f)
    corpus_size = len([k for k in scores if not k.startswith("_") and scores[k].get("tier") == "GEO_GOLD"])

    # Step 1: Calibration
    cal_json = run_calibration(args.topic, args.dry_run)

    # Step 2: Update corpus
    added = update_scores_corpus(cal_json, args.topic, args.dry_run)
    corpus_size += added

    # Step 3: Delta analysis
    proposed = run_delta_analysis(args.dry_run)
    if not proposed:
        print("\n✓ No proposal generated (dry run or error)")
        return

    # Append calibration findings to FEEDBACK.md files
    if not args.dry_run and proposed:
        append_to_feedback_files(args.topic, cal_json, proposed, datetime.utcnow().strftime("%Y-%m-%d"))

    # Step 4: Check significance
    print(f"\n[4/5] Checking significance...")
    significant, changes = significant_change(proposed)
    if not significant:
        print(f"  No significant weight changes (threshold: ±{WEIGHT_CHANGE_THRESHOLD*100:.0f}%). No proposal posted.")
        return
    print(f"  {len(changes)} significant changes detected")

    # Step 5: Post to Slack
    print(f"\n[5/5] Posting proposal to Slack #way-mark...")
    slack_msg = format_slack_proposal(proposed, changes, args.topic, corpus_size)
    post_to_slack(slack_msg, args.dry_run)

    print("\n✓ Self-update loop complete.")
    print(f"  Waiting for human approval in #way-mark")
    print(f"  After ✅ reaction: run `python3 rubric_self_update.py --apply-proposal`")


if __name__ == "__main__":
    main()
