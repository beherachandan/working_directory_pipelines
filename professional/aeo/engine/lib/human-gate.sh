#!/usr/bin/env bash
# human-gate.sh — Pause/resume pattern for E1 human review
# Usage: source this file, then call wait_for_human_review

set -euo pipefail

ENGINE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS_DIR="${ENGINE_DIR}/runs"

source "${ENGINE_DIR}/lib/state-manager.sh"

# ── Prepare for human review ──
# Creates the review package and instructions file
# Usage: prepare_human_review "formative-assessment"
prepare_human_review() {
    local slug="$1"
    local run_dir="${RUNS_DIR}/${slug}"

    # Get the composed draft (C5 output)
    local c5_output
    c5_output=$(state_get "$slug" '.dag_progress["C5"].output_file')

    # Get the score card (D1 output)
    local d1_output
    d1_output=$(state_get "$slug" '.dag_progress["D1"].output_file')

    # Get the content brief (B3 output)
    local b3_output
    b3_output=$(state_get "$slug" '.dag_progress["B3"].output_file')

    # Create review instructions
    cat > "${run_dir}/revisions/REVIEW-INSTRUCTIONS.md" << 'INSTRUCTIONS'
# E1 Human Review — Instructions

## What to Review
1. **Article Draft** — the composed article (see C5 output in outputs/)
2. **Score Card** — D1's evaluation (see D1 output in outputs/)
3. **Content Brief** — original requirements (see B3 output in outputs/)

## How to Provide Feedback

Edit the file `e1-feedback.md` in this directory with:

1. **First line must be the decision:**
   - `DECISION: Approved` — article is ready for publishing pipeline
   - `DECISION: Needs Revision` — article needs changes (provide details below)

2. **If Needs Revision, add specific feedback:**
   - What sections need changes
   - What's factually incorrect
   - What's pedagogically unsound
   - What's missing from an educator's perspective

## Example Feedback File

```markdown
DECISION: Needs Revision

## Pedagogical Accuracy
- Section "What is formative assessment?" conflates formative and diagnostic assessment
- The example in Section 3 doesn't reflect real classroom practice

## Missing Perspectives
- No mention of informal formative assessment (observation, questioning)
- Needs practitioner voice — add a teacher quote about real implementation challenges

## Factual Issues
- The statistic about "80% of teachers" needs a more recent source
```

## After Review
Save `e1-feedback.md` and re-run the orchestrator. It will pick up where it left off.
INSTRUCTIONS

    # Create blank feedback template
    if [[ ! -f "${run_dir}/revisions/e1-feedback.md" ]]; then
        cat > "${run_dir}/revisions/e1-feedback.md" << 'TEMPLATE'
DECISION: [Approved / Needs Revision]

## Feedback
[Your feedback here]
TEMPLATE
    fi

    state_update "$slug" '.status = "waiting_human_review"'

    echo ""
    echo "================================================================"
    echo "  PIPELINE PAUSED — Human Review Required (E1)"
    echo "================================================================"
    echo ""
    echo "  Article: ${slug}"
    echo "  Review directory: ${run_dir}/revisions/"
    echo ""
    echo "  Files to review:"
    [[ -n "$c5_output" && "$c5_output" != "null" ]] && echo "    Draft:   ${run_dir}/${c5_output}"
    [[ -n "$d1_output" && "$d1_output" != "null" ]] && echo "    Scores:  ${run_dir}/${d1_output}"
    [[ -n "$b3_output" && "$b3_output" != "null" ]] && echo "    Brief:   ${run_dir}/${b3_output}"
    echo ""
    echo "  Instructions: ${run_dir}/revisions/REVIEW-INSTRUCTIONS.md"
    echo "  Feedback file: ${run_dir}/revisions/e1-feedback.md"
    echo ""
    echo "  To resume: edit e1-feedback.md, then re-run the orchestrator."
    echo "================================================================"
    echo ""
}

# ── Check if human review is complete ──
# Usage: if is_human_review_done "formative-assessment"; then ...
is_human_review_done() {
    local slug="$1"
    local run_dir="${RUNS_DIR}/${slug}"
    local feedback_file="${run_dir}/revisions/e1-feedback.md"

    if [[ ! -f "$feedback_file" ]]; then
        return 1
    fi

    # Check if the template has been filled in (not still the default)
    local decision_line
    decision_line=$(grep -i "^DECISION:" "$feedback_file" | head -1 || echo "")

    if echo "$decision_line" | grep -qi "approved\|revision"; then
        return 0
    fi

    return 1
}
