#!/usr/bin/env bash
# state-manager.sh — Article pipeline state management (JSON via jq)
# Usage: source this file, then call functions

set -euo pipefail

ENGINE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS_DIR="${ENGINE_DIR}/runs"

# All agents in DAG order (for initialization)
ALL_AGENTS=(A1 A2 B1 B2 B3 C1 C2 C3 C4 C5 D1 D2 D3 D4 E1 E2 F1 F2 F3 F4 F5 F6 G1 G2)

# Initialize a new article run
# Usage: state_init "formative-assessment" "What are formative assessment strategies?"
state_init() {
    local slug="$1"
    local topic="$2"
    local run_dir="${RUNS_DIR}/${slug}"

    if [[ -f "${run_dir}/state.json" ]]; then
        echo "Run already exists: ${slug}. Use state_reset to start over." >&2
        return 1
    fi

    mkdir -p "${run_dir}"/{outputs,revisions,logs}

    # Build dag_progress object with all agents set to pending
    local dag_progress="{}"
    for agent in "${ALL_AGENTS[@]}"; do
        dag_progress=$(echo "$dag_progress" | jq --arg a "$agent" '. + {($a): {"status": "pending", "output_file": null}}')
    done

    jq -n \
        --arg slug "$slug" \
        --arg topic "$topic" \
        --arg date "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        --argjson dag "$dag_progress" \
        '{
            article_slug: $slug,
            topic: $topic,
            created_at: $date,
            updated_at: $date,
            current_stage: null,
            status: "initialized",
            dag_progress: $dag,
            gates: {
                D_gate: { decision: null, d1_scores: null, composite: null },
                E_gate: { decision: null, feedback_file: null }
            },
            revisions: { count: 0, max: 2, history: [] },
            model_overrides: {},
            token_usage: { total_input: 0, total_output: 0, cost_estimate_usd: 0 }
        }' > "${run_dir}/state.json"

    echo "Initialized run: ${slug}"
}

# Read full state JSON
# Usage: state_read "formative-assessment"
state_read() {
    local slug="$1"
    cat "${RUNS_DIR}/${slug}/state.json"
}

# Get a specific field from state
# Usage: state_get "formative-assessment" ".current_stage"
state_get() {
    local slug="$1"
    local query="$2"
    jq -r "$query" "${RUNS_DIR}/${slug}/state.json"
}

# Update state with a jq expression
# Usage: state_update "formative-assessment" '.current_stage = "A1" | .status = "running"'
state_update() {
    local slug="$1"
    local expr="$2"
    local state_file="${RUNS_DIR}/${slug}/state.json"
    local lock_file="${state_file}.lock"
    local tmp_file="${state_file}.tmp.$$"

    # File locking to prevent race conditions during parallel agent runs
    # macOS doesn't have flock, so use mkdir as atomic lock
    local retries=0
    while ! mkdir "$lock_file" 2>/dev/null; do
        retries=$((retries + 1))
        if [[ $retries -gt 50 ]]; then
            echo "ERROR: Could not acquire state lock after 5s" >&2
            return 1
        fi
        sleep 0.1
    done

    # Critical section: read → transform → write
    jq "$expr | .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"" "$state_file" > "$tmp_file"
    mv "$tmp_file" "$state_file"

    # Release lock
    rmdir "$lock_file" 2>/dev/null
}

# Mark an agent as running
# Usage: state_agent_start "formative-assessment" "A1"
state_agent_start() {
    local slug="$1"
    local agent="$2"
    state_update "$slug" \
        ".current_stage = \"${agent}\" | .status = \"running\" | .dag_progress[\"${agent}\"].status = \"running\" | .dag_progress[\"${agent}\"].started_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\""
}

# Mark an agent as completed with output file
# Usage: state_agent_complete "formative-assessment" "A1" "outputs/A1-query-intelligence.md"
state_agent_complete() {
    local slug="$1"
    local agent="$2"
    local output_file="$3"
    state_update "$slug" \
        ".dag_progress[\"${agent}\"].status = \"completed\" | .dag_progress[\"${agent}\"].output_file = \"${output_file}\" | .dag_progress[\"${agent}\"].completed_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\""
}

# Mark an agent as failed
# Usage: state_agent_fail "formative-assessment" "A1" "API error"
state_agent_fail() {
    local slug="$1"
    local agent="$2"
    local error="$3"
    state_update "$slug" \
        ".status = \"failed\" | .dag_progress[\"${agent}\"].status = \"failed\" | .dag_progress[\"${agent}\"].error = \"${error}\""
}

# Check if an agent is already completed (for resume)
# Usage: state_agent_is_done "formative-assessment" "A1" && echo "skip"
state_agent_is_done() {
    local slug="$1"
    local agent="$2"
    local status
    status=$(state_get "$slug" ".dag_progress[\"${agent}\"].status")
    [[ "$status" == "completed" ]]
}

# Record D-gate decision
# Usage: state_set_d_gate "formative-assessment" "PASS" '{"qape":8,"ear":7,"extract":9,"trust":7,"intent":8}' "7.8"
state_set_d_gate() {
    local slug="$1"
    local decision="$2"
    local scores="$3"
    local composite="$4"
    state_update "$slug" \
        ".gates.D_gate.decision = \"${decision}\" | .gates.D_gate.d1_scores = ${scores} | .gates.D_gate.composite = ${composite}"
}

# Record E-gate decision
# Usage: state_set_e_gate "formative-assessment" "Approved" "revisions/e1-feedback.md"
state_set_e_gate() {
    local slug="$1"
    local decision="$2"
    local feedback_file="${3:-null}"
    if [[ "$feedback_file" == "null" ]]; then
        state_update "$slug" ".gates.E_gate.decision = \"${decision}\""
    else
        state_update "$slug" ".gates.E_gate.decision = \"${decision}\" | .gates.E_gate.feedback_file = \"${feedback_file}\""
    fi
}

# Increment revision count and log
# Usage: state_add_revision "formative-assessment" "D1" "QAPE score 5, Trust score 4"
state_add_revision() {
    local slug="$1"
    local source="$2"
    local reason="$3"
    local rev_count
    rev_count=$(state_get "$slug" ".revisions.count")
    local new_count=$((rev_count + 1))

    state_update "$slug" \
        ".revisions.count = ${new_count} | .revisions.history += [{\"revision\": ${new_count}, \"source\": \"${source}\", \"reason\": \"${reason}\", \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}]"
}

# Check if max revisions reached
# Usage: state_max_revisions_reached "formative-assessment" && echo "escalate"
state_max_revisions_reached() {
    local slug="$1"
    local count max
    count=$(state_get "$slug" ".revisions.count")
    max=$(state_get "$slug" ".revisions.max")
    [[ "$count" -ge "$max" ]]
}

# Reset C-phase agents for revision loop (C1-C5 back to pending)
# Usage: state_reset_for_revision "formative-assessment"
state_reset_for_revision() {
    local slug="$1"
    for agent in C1 C2 C3 C4 C5 D1 D2 D3 D4; do
        state_update "$slug" ".dag_progress[\"${agent}\"].status = \"pending\" | .dag_progress[\"${agent}\"].output_file = null"
    done
    state_update "$slug" ".gates.D_gate.decision = null | .gates.D_gate.d1_scores = null | .gates.D_gate.composite = null"
}

# Record token usage for an agent run
# Usage: state_add_tokens "formative-assessment" "A1" 1500 800 0.05
state_add_tokens() {
    local slug="$1"
    local agent="$2"
    local input_tokens="$3"
    local output_tokens="$4"
    local cost="$5"
    state_update "$slug" \
        ".token_usage.total_input += ${input_tokens} | .token_usage.total_output += ${output_tokens} | .token_usage.cost_estimate_usd += ${cost} | .dag_progress[\"${agent}\"].input_tokens = ${input_tokens} | .dag_progress[\"${agent}\"].output_tokens = ${output_tokens}"
}

# Mark pipeline as complete
# Usage: state_complete "formative-assessment"
state_complete() {
    local slug="$1"
    state_update "$slug" '.status = "completed" | .current_stage = "done"'
}

# Reset state only (preserves outputs and logs)
# Usage: state_reset "formative-assessment"
state_reset() {
    local slug="$1"
    local run_dir="${RUNS_DIR}/${slug}"
    if [[ -d "$run_dir" ]]; then
        rm -f "${run_dir}/state.json" "${run_dir}/state.json.tmp".*
        rmdir "${run_dir}/state.json.lock" 2>/dev/null || true
        rm -rf "${run_dir}/revisions"
        mkdir -p "${run_dir}/revisions"
        echo "Reset state for: ${slug} (outputs preserved)"
    fi
}

# Delete entire run (destructive — removes all outputs)
# Usage: state_delete "formative-assessment"
state_delete() {
    local slug="$1"
    local run_dir="${RUNS_DIR}/${slug}"
    if [[ -d "$run_dir" ]]; then
        rm -rf "$run_dir"
        echo "Deleted run: ${slug}"
    fi
}

# Get the run directory path
# Usage: run_dir="$(state_run_dir "formative-assessment")"
state_run_dir() {
    local slug="$1"
    echo "${RUNS_DIR}/${slug}"
}

# List all runs with status
# Usage: state_list_runs
state_list_runs() {
    if [[ ! -d "$RUNS_DIR" ]]; then
        echo "No runs found."
        return
    fi
    for state_file in "${RUNS_DIR}"/*/state.json; do
        [[ -f "$state_file" ]] || continue
        jq -r '[.article_slug, .status, .current_stage // "none", .revisions.count | tostring] | join(" | ")' "$state_file"
    done
}
