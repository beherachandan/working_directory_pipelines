#!/usr/bin/env bash
# gate-checker.sh — Evaluate D1 scores and E1/E2 decisions
# Usage: source this file, then call check_d_gate or check_e_gate

set -euo pipefail

ENGINE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS_DIR="${ENGINE_DIR}/runs"

source "${ENGINE_DIR}/lib/state-manager.sh"

# ── Parse D1 score card output for JSON scores ──
# D1 output should contain a scores block. We extract scores from the markdown table.
# Returns JSON: {"qape":8,"ear":7,"extract":9,"trust":7,"intent":8}
parse_d1_scores() {
    local d1_output_file="$1"

    if [[ ! -f "$d1_output_file" ]]; then
        echo '{"error": "D1 output file not found"}' >&2
        return 1
    fi

    local content
    content=$(cat "$d1_output_file")

    # Try to find a JSON scores block first (preferred format)
    # D1 is instructed to include <scores>{"qape":8,...}</scores>
    local json_block
    json_block=$(echo "$content" | grep -o '<scores>{[^<]*}</scores>' | sed 's/<scores>//;s/<\/scores>//' 2>/dev/null || echo "")
    if [[ -n "$json_block" ]] && echo "$json_block" | jq . >/dev/null 2>&1; then
        echo "$json_block"
        return 0
    fi

    # Fallback: parse from markdown table
    # Expected format: | 1 | QAPE Structure | 8 | ✅ | ... |
    # We extract the 3rd pipe-delimited field (the score column)
    local qape ear extract trust intent

    # Extract score from dimension row: split by |, take the score field (3rd column = index 3)
    qape=$(echo "$content" | grep -i "QAPE" | awk -F'|' '{gsub(/[[:space:]]/, "", $4); print $4}' | head -1 || echo "0")
    ear=$(echo "$content" | grep -i "EAR" | awk -F'|' '{gsub(/[[:space:]]/, "", $4); print $4}' | head -1 || echo "0")
    extract=$(echo "$content" | grep -i "Extractability" | awk -F'|' '{gsub(/[[:space:]]/, "", $4); print $4}' | head -1 || echo "0")
    trust=$(echo "$content" | grep -i "Trust" | awk -F'|' '{gsub(/[[:space:]]/, "", $4); print $4}' | head -1 || echo "0")
    intent=$(echo "$content" | grep -i "Intent Match" | awk -F'|' '{gsub(/[[:space:]]/, "", $4); print $4}' | head -1 || echo "0")

    # Default 0 for any unparsed scores
    qape="${qape:-0}"
    ear="${ear:-0}"
    extract="${extract:-0}"
    trust="${trust:-0}"
    intent="${intent:-0}"

    jq -n \
        --argjson q "${qape}" \
        --argjson e "${ear}" \
        --argjson x "${extract}" \
        --argjson t "${trust}" \
        --argjson i "${intent}" \
        '{"qape": $q, "ear": $e, "extract": $x, "trust": $t, "intent": $i}'
}

# ── Compute composite score ──
# Weights: QAPE 25%, EAR 25%, Extract 20%, Trust 20%, Intent 10%
compute_composite() {
    local scores_json="$1"
    local q e x t i
    q=$(echo "$scores_json" | jq '.qape')
    e=$(echo "$scores_json" | jq '.ear')
    x=$(echo "$scores_json" | jq '.extract')
    t=$(echo "$scores_json" | jq '.trust')
    i=$(echo "$scores_json" | jq '.intent')

    echo "scale=2; ($q * 0.25) + ($e * 0.25) + ($x * 0.20) + ($t * 0.20) + ($i * 0.10)" | bc
}

# ── Check D-Gate ──
# Returns: PASS, REVISE, or ESCALATE
# Usage: decision=$(check_d_gate "formative-assessment")
check_d_gate() {
    local slug="$1"
    local run_dir="${RUNS_DIR}/${slug}"

    # Find D1 output
    local d1_output
    d1_output=$(state_get "$slug" '.dag_progress["D1"].output_file')
    if [[ -z "$d1_output" || "$d1_output" == "null" ]]; then
        echo "ERROR: D1 has not completed yet" >&2
        return 1
    fi

    # Parse scores
    local scores
    scores=$(parse_d1_scores "${run_dir}/${d1_output}")

    # Calculate composite
    local composite
    composite=$(compute_composite "$scores")

    # Check if all scores >= 7
    local all_pass=true
    local failed_dims=""
    for dim in qape ear extract trust intent; do
        local score
        score=$(echo "$scores" | jq ".${dim}")
        if (( $(echo "$score < 7" | bc -l) )); then
            all_pass=false
            failed_dims+="${dim}(${score}) "
        fi
    done

    local decision
    if [[ "$all_pass" == "true" ]]; then
        decision="PASS"
    elif state_max_revisions_reached "$slug"; then
        decision="ESCALATE"
    else
        decision="REVISE"
    fi

    # Record in state
    state_set_d_gate "$slug" "$decision" "$scores" "$composite"

    # If REVISE, generate revision feedback file
    if [[ "$decision" == "REVISE" ]]; then
        local rev_count
        rev_count=$(state_get "$slug" '.revisions.count')
        local next_rev=$((rev_count + 1))
        local feedback_file="${run_dir}/revisions/revision-${next_rev}.md"

        # Compile feedback from D1-D4 outputs
        {
            echo "# Revision Feedback #${next_rev}"
            echo ""
            echo "## D-Gate Decision: REVISE"
            echo "**Failed dimensions:** ${failed_dims}"
            echo "**Composite score:** ${composite}/10"
            echo ""

            # Include D1 revision notes
            echo "## D1 (AEO Evaluator) Feedback"
            if [[ -f "${run_dir}/${d1_output}" ]]; then
                # Extract revision notes section
                sed -n '/## Revision Notes/,/## [^R]/p' "${run_dir}/${d1_output}" 2>/dev/null || \
                    echo "See full D1 output for details."
            fi
            echo ""

            # Include D2 feedback if available
            local d2_output
            d2_output=$(state_get "$slug" '.dag_progress["D2"].output_file')
            if [[ -n "$d2_output" && "$d2_output" != "null" && -f "${run_dir}/${d2_output}" ]]; then
                echo "## D2 (Fact Check) Feedback"
                cat "${run_dir}/${d2_output}"
                echo ""
            fi

            # Include D3 feedback if available
            local d3_output
            d3_output=$(state_get "$slug" '.dag_progress["D3"].output_file')
            if [[ -n "$d3_output" && "$d3_output" != "null" && -f "${run_dir}/${d3_output}" ]]; then
                echo "## D3 (SEO) Feedback"
                cat "${run_dir}/${d3_output}"
                echo ""
            fi

            # Include D4 feedback if available
            local d4_output
            d4_output=$(state_get "$slug" '.dag_progress["D4"].output_file')
            if [[ -n "$d4_output" && "$d4_output" != "null" && -f "${run_dir}/${d4_output}" ]]; then
                echo "## D4 (Extractability) Feedback"
                cat "${run_dir}/${d4_output}"
                echo ""
            fi
        } > "$feedback_file"

        state_add_revision "$slug" "D1" "Failed dimensions: ${failed_dims}"
    fi

    echo "$decision"
}

# ── Compile E-gate feedback from E1 human review ──
# Reads the E1 feedback file and determines the decision
# Usage: decision=$(check_e_gate "formative-assessment")
check_e_gate() {
    local slug="$1"
    local run_dir="${RUNS_DIR}/${slug}"

    # Look for E1 human feedback file
    local feedback_file="${run_dir}/revisions/e1-feedback.md"
    if [[ ! -f "$feedback_file" ]]; then
        echo "WAITING"
        return 0
    fi

    # Parse decision from feedback file
    # Expected format: first line should contain "DECISION: Approved" or "DECISION: Needs Revision"
    local decision_line
    decision_line=$(grep -i "^DECISION:" "$feedback_file" | head -1 || echo "")

    if echo "$decision_line" | grep -qi "approved"; then
        state_set_e_gate "$slug" "Approved" "$feedback_file"
        echo "PASS"
    elif echo "$decision_line" | grep -qi "revision"; then
        # Create revision feedback
        local rev_count
        rev_count=$(state_get "$slug" '.revisions.count')
        local next_rev=$((rev_count + 1))
        local rev_file="${run_dir}/revisions/revision-${next_rev}.md"

        {
            echo "# Revision Feedback #${next_rev} (from E1 SME Review)"
            echo ""
            cat "$feedback_file"
        } > "$rev_file"

        state_set_e_gate "$slug" "Needs Revision" "$feedback_file"
        state_add_revision "$slug" "E1" "SME/Teacher review requested changes"

        if state_max_revisions_reached "$slug"; then
            echo "ESCALATE"
        else
            echo "REVISE"
        fi
    else
        echo "WAITING"
    fi
}
