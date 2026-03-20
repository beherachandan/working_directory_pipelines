#!/usr/bin/env bash
# agent-runner.sh — Single agent invocation: build prompt → call claude → save output
# Usage: source this file, then call run_agent

set -euo pipefail

ENGINE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS_DIR="${ENGINE_DIR}/runs"

# Source dependencies
source "${ENGINE_DIR}/lib/state-manager.sh"
source "${ENGINE_DIR}/lib/prompt-builder.sh"

# ── Run a single agent ──
# Usage: run_agent "formative-assessment" "A1" ["extra context"]
# Returns 0 on success, 1 on failure
run_agent() {
    local slug="$1"
    local agent="$2"
    local extra_context="${3:-}"
    local run_dir="${RUNS_DIR}/${slug}"
    local log_file="${run_dir}/logs/${agent}.log"
    local output_filename
    output_filename=$(get_output_filename "$agent")
    local output_path="${run_dir}/${output_filename}"

    # Resume check — skip if already completed
    if state_agent_is_done "$slug" "$agent"; then
        echo "[${agent}] Already completed, skipping." | tee -a "$log_file"
        return 0
    fi

    echo "[${agent}] Starting..." | tee -a "$log_file"
    state_agent_start "$slug" "$agent"

    # Build the prompt
    local prompt
    prompt=$(build_prompt "$slug" "$agent" "$extra_context")
    if [[ $? -ne 0 ]]; then
        state_agent_fail "$slug" "$agent" "Prompt build failed"
        echo "[${agent}] FAILED: Could not build prompt" | tee -a "$log_file"
        return 1
    fi

    # Save prompt for debugging
    echo "$prompt" > "${run_dir}/logs/${agent}-prompt.md"

    # Determine model
    local model
    model=$(get_agent_model "$agent")

    # Call claude
    echo "[${agent}] Calling claude (model: ${model})..." | tee -a "$log_file"
    local start_time
    start_time=$(date +%s)

    local raw_output
    if ! raw_output=$(echo "$prompt" | claude -p --model "$model" 2>>"$log_file"); then
        state_agent_fail "$slug" "$agent" "Claude API call failed"
        echo "[${agent}] FAILED: Claude API call failed" | tee -a "$log_file"
        return 1
    fi

    local end_time
    end_time=$(date +%s)
    local duration=$((end_time - start_time))
    echo "[${agent}] Claude responded in ${duration}s" | tee -a "$log_file"

    # Extract content between <output> tags (or use full output if no tags)
    local extracted_output
    if echo "$raw_output" | grep -q '<output>'; then
        extracted_output=$(echo "$raw_output" | sed -n '/<output>/,/<\/output>/p' | sed '1d;$d')
    else
        # No <output> tags — use the full response
        extracted_output="$raw_output"
        echo "[${agent}] WARNING: No <output> tags found, using full response" | tee -a "$log_file"
    fi

    # Save output
    echo "$extracted_output" > "$output_path"

    # Save raw output for debugging
    echo "$raw_output" > "${run_dir}/logs/${agent}-raw.md"

    # Update state
    state_agent_complete "$slug" "$agent" "$output_filename"

    # Estimate token usage (rough: 4 chars per token)
    local prompt_len=${#prompt}
    local output_len=${#raw_output}
    local est_input_tokens=$((prompt_len / 4))
    local est_output_tokens=$((output_len / 4))

    # Cost estimation (approximate rates for sonnet/opus)
    local cost
    if [[ "$model" == "opus" ]]; then
        # Opus: ~$15/M input, ~$75/M output
        cost=$(echo "scale=4; ($est_input_tokens * 0.000015) + ($est_output_tokens * 0.000075)" | bc 2>/dev/null || echo "0")
    else
        # Sonnet: ~$3/M input, ~$15/M output
        cost=$(echo "scale=4; ($est_input_tokens * 0.000003) + ($est_output_tokens * 0.000015)" | bc 2>/dev/null || echo "0")
    fi
    state_add_tokens "$slug" "$agent" "$est_input_tokens" "$est_output_tokens" "${cost:-0}"

    echo "[${agent}] Completed. Output: ${output_filename} (${duration}s, ~${est_input_tokens}+${est_output_tokens} tokens)" | tee -a "$log_file"
    return 0
}

# ── Dry run — build prompt but don't call claude ──
# Usage: dry_run_agent "formative-assessment" "A1"
dry_run_agent() {
    local slug="$1"
    local agent="$2"
    local extra_context="${3:-}"

    echo "=== DRY RUN: ${agent} ==="
    echo "Model: $(get_agent_model "$agent")"
    echo "Dependencies: $(get_agent_deps "$agent")"
    echo ""

    local prompt
    prompt=$(build_prompt "$slug" "$agent" "$extra_context")
    local prompt_len=${#prompt}
    local est_tokens=$((prompt_len / 4))

    echo "Prompt length: ${prompt_len} chars (~${est_tokens} tokens)"
    echo ""
    echo "--- Prompt Preview (first 500 chars) ---"
    echo "${prompt:0:500}"
    echo "..."
    echo "--- End Preview ---"
}
