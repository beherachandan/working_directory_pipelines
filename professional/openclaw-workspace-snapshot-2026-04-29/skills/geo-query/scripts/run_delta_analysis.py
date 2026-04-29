#!/usr/bin/env python3
"""
run_delta_analysis.py — Cross-topic Delta Analysis

Loads d2-scores-corpus.json and computes:
  - Per-dimension average: GEO_GOLD tier vs all other tiers (non-cited)
  - Delta sorted descending (most predictive dimensions first)
  - Rubric weight recommendations based on delta magnitude

Usage:
  python3 run_delta_analysis.py
  python3 run_delta_analysis.py --scores-file /path/to/d2-scores-corpus.json
  python3 run_delta_analysis.py --output rubric-weight-proposal.md
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict

WORKSPACE_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SCORES = WORKSPACE_ROOT / "memory" / "research" / "scoring-runs" / "d2-scores-corpus.json"
OUTPUT_DIR     = WORKSPACE_ROOT / "memory" / "research" / "scoring-runs"

DIMENSIONS = [
    "qape",
    "self_containment",
    "structural_readability",
    "statistical_density",
    "uniqueness",
    "trust_authority",
    "intent_match",
    "platform_specificity",
]

DIM_LABELS = {
    "qape":                   "QAPE / Answer Structure",
    "self_containment":       "Passage Self-Containment",
    "structural_readability": "Structural Readability",
    "statistical_density":    "Statistical Density",
    "uniqueness":             "Uniqueness & Original Data",
    "trust_authority":        "Trust & Authority",
    "intent_match":           "Intent Match",
    "platform_specificity":   "Platform Specificity",
}

# Current D2 weights
CURRENT_WEIGHTS = {
    "qape":                   0.22,
    "self_containment":       0.18,
    "structural_readability": 0.12,
    "statistical_density":    0.12,
    "uniqueness":             0.12,
    "trust_authority":        0.12,
    "intent_match":           0.07,
    "platform_specificity":   0.05,
}


def load_scores(path: Path) -> dict:
    with open(path) as f:
        data = json.load(f)
    # Strip metadata keys
    return {k: v for k, v in data.items() if not k.startswith("_")}


def compute_delta(scores: dict) -> dict:
    gold_scores = {u: s for u, s in scores.items() if s.get("tier") == "GEO_GOLD"}
    rest_scores = {u: s for u, s in scores.items() if s.get("tier") != "GEO_GOLD"}

    print(f"\nCorpus: {len(scores)} URLs total")
    print(f"  GEO_GOLD (cited by AI):  {len(gold_scores)}")
    print(f"  Non-gold (not cited):    {len(rest_scores)}")

    delta = {}
    for dim in DIMENSIONS:
        gold_vals = [s[dim] for s in gold_scores.values() if dim in s]
        rest_vals = [s[dim] for s in rest_scores.values() if dim in s]
        if not gold_vals or not rest_vals:
            continue
        gold_avg = sum(gold_vals) / len(gold_vals)
        rest_avg = sum(rest_vals) / len(rest_vals)
        delta[dim] = {
            "label":     DIM_LABELS[dim],
            "gold_avg":  round(gold_avg, 2),
            "rest_avg":  round(rest_avg, 2),
            "delta":     round(gold_avg - rest_avg, 2),
            "gold_n":    len(gold_vals),
            "rest_n":    len(rest_vals),
            "current_weight": CURRENT_WEIGHTS.get(dim, 0),
        }

    # Sort by delta descending
    delta = dict(sorted(delta.items(), key=lambda x: -x[1]["delta"]))
    return delta, gold_scores, rest_scores


def propose_weights(delta: dict) -> dict:
    """
    Propose new weights proportional to delta magnitude.
    Scale: delta contributes to weight, capped so total = 1.0 across 8 dims.
    Anchor: QAPE stays ≥ 18% (structural importance regardless of delta).
    """
    # Raw delta values (floor at 0 so no dimension gets negative weight)
    raw = {dim: max(d["delta"], 0.5) for dim, d in delta.items()}
    total_raw = sum(raw.values())

    # Normalise to sum to 1.0
    proposed = {dim: round(v / total_raw, 3) for dim, v in raw.items()}

    # Anchor QAPE floor (structural, always important)
    if proposed.get("qape", 0) < 0.18:
        deficit = 0.18 - proposed["qape"]
        proposed["qape"] = 0.18
        # Distribute deficit reduction proportionally from others
        others = [d for d in proposed if d != "qape"]
        reduction_each = deficit / len(others)
        for d in others:
            proposed[d] = round(max(0.02, proposed[d] - reduction_each), 3)

    # Re-normalise to exactly 1.0 (floating point cleanup)
    total = sum(proposed.values())
    proposed = {k: round(v / total, 3) for k, v in proposed.items()}

    return proposed


def print_delta_table(delta: dict):
    print("\n" + "=" * 75)
    print("DIMENSION DELTA ANALYSIS — GEO_GOLD vs Non-Cited URLs")
    print("=" * 75)
    print(f"{'Dimension':<35} {'Gold':>6} {'Rest':>6} {'Δ':>6}  {'Current':>8}  {'Bar'}")
    print("-" * 75)
    for dim, d in delta.items():
        bar = "█" * max(1, int(d["delta"] * 3))
        current_pct = f"{d['current_weight']*100:.0f}%"
        print(f"{d['label']:<35} {d['gold_avg']:>6.2f} {d['rest_avg']:>6.2f} {d['delta']:>+6.2f}  {current_pct:>8}  {bar}")


def print_weight_proposal(delta: dict, proposed: dict):
    print("\n" + "=" * 60)
    print("PROPOSED RUBRIC WEIGHTS (v1.1 candidate)")
    print("=" * 60)
    print(f"{'Dimension':<35} {'Current':>8} {'Proposed':>9} {'Change':>8}")
    print("-" * 60)
    for dim in DIMENSIONS:
        if dim not in delta:
            continue
        cur  = CURRENT_WEIGHTS.get(dim, 0)
        prop = proposed.get(dim, 0)
        diff = prop - cur
        flag = " ↑" if diff > 0.01 else (" ↓" if diff < -0.01 else "  ~")
        print(f"{DIM_LABELS[dim]:<35} {cur*100:>7.0f}% {prop*100:>8.0f}% {diff*100:>+7.1f}%{flag}")
    print("-" * 60)
    print(f"{'TOTAL':<35} {sum(CURRENT_WEIGHTS.values())*100:>7.0f}% {sum(proposed.values())*100:>8.0f}%")


def save_proposal(delta: dict, proposed: dict, gold_scores: dict, rest_scores: dict, output_path: Path):
    lines = [
        "# Rubric Weight Proposal — v1.1 Candidate",
        f"_Generated: auto from delta analysis_",
        f"_Corpus: {len(gold_scores)} GEO_GOLD URLs + {len(rest_scores)} non-cited URLs_\n",
        "## Delta Analysis (most predictive → least)",
        "| Dimension | Gold avg | Rest avg | Δ | Current weight |",
        "|---|---|---|---|---|",
    ]
    for dim, d in delta.items():
        lines.append(f"| {d['label']} | {d['gold_avg']} | {d['rest_avg']} | {d['delta']:+.2f} | {d['current_weight']*100:.0f}% |")

    lines += [
        "\n## Proposed Weights (v1.1)",
        "| Dimension | Current | Proposed | Change |",
        "|---|---|---|---|",
    ]
    for dim in DIMENSIONS:
        if dim not in delta:
            continue
        cur  = CURRENT_WEIGHTS.get(dim, 0)
        prop = proposed.get(dim, 0)
        diff = prop - cur
        flag = "↑" if diff > 0.01 else ("↓" if diff < -0.01 else "~")
        lines.append(f"| {DIM_LABELS[dim]} | {cur*100:.0f}% | {prop*100:.0f}% | {diff*100:+.1f}% {flag} |")

    top_dim = next(iter(delta))
    lines += [
        f"\n## Key Insight",
        f"Most predictive dimension: **{DIM_LABELS[top_dim]}** (Δ = {delta[top_dim]['delta']:+.2f})",
        f"Least predictive: **{DIM_LABELS[list(delta.keys())[-1]]}** (Δ = {delta[list(delta.keys())[-1]]['delta']:+.2f})",
        "",
        "## Gate to Apply",
        "- [ ] Gemini calibration run on ≥2 topics (compare gold URL overlap with ChatGPT)",
        "- [ ] Human review of proposals above",
        "- [ ] Edit `aeo/context/aeo-scoring-rubric.md` with new weights",
        "- [ ] Bump version to v1.1, log in `rubric-changelog.md`",
        "- [ ] Rerun calibration corpus on ≥5 URLs, capture score delta",
        "- [ ] Post to Slack #way-mark before deploying",
    ]

    output_path.write_text("\n".join(lines))
    print(f"\n✓ Proposal saved: {output_path}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scores-file", default=str(DEFAULT_SCORES))
    p.add_argument("--output", default=None)
    args = p.parse_args()

    scores_path = Path(args.scores_file)
    if not scores_path.exists():
        print(f"✗ Scores file not found: {scores_path}")
        return

    scores = load_scores(scores_path)
    delta, gold_scores, rest_scores = compute_delta(scores)

    if not delta:
        print("✗ Not enough data for delta analysis.")
        return

    print_delta_table(delta)
    proposed = propose_weights(delta)
    print_weight_proposal(delta, proposed)

    output_path = Path(args.output) if args.output else (OUTPUT_DIR / "rubric-weight-proposal.md")
    save_proposal(delta, proposed, gold_scores, rest_scores, output_path)

    print("\n✓ Delta analysis complete.")
    print("  Review proposal before applying to aeo/context/aeo-scoring-rubric.md")


if __name__ == "__main__":
    main()
