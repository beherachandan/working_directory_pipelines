#!/usr/bin/env bash
# parallel-runner.sh — Run N agents concurrently via background processes
# Usage: source this file, then call run_parallel

set -euo pipefail

ENGINE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

source "${ENGINE_DIR}/lib/agent-runner.sh"

# ── Run multiple agents in parallel ──
# Usage: run_parallel "formative-assessment" "D1 D2 D3 D4"
# Returns 0 if all succeed, 1 if any fail
#
# Each agent runs as a separate bash subprocess that sources all libraries
# to avoid environment sharing issues. State file locking prevents corruption.
run_parallel() {
    local slug="$1"
    local agents="$2"
    local pids=()
    local agent_names=()
    local all_passed=true

    echo "[PARALLEL] Starting agents: ${agents}"

    for agent in $agents; do
        # Skip already-completed agents
        if state_agent_is_done "$slug" "$agent"; then
            echo "[PARALLEL] ${agent} already completed, skipping."
            continue
        fi

        # Run each agent in a separate bash process that sources all libs
        bash -c "
            source '${ENGINE_DIR}/lib/state-manager.sh'
            source '${ENGINE_DIR}/lib/prompt-builder.sh'
            source '${ENGINE_DIR}/lib/agent-runner.sh'
            run_agent '$slug' '$agent'
        " &
        pids+=($!)
        agent_names+=("$agent")
    done

    # Wait for all background processes
    if [[ ${#pids[@]} -eq 0 ]]; then
        echo "[PARALLEL] All agents already completed."
        return 0
    fi

    local i=0
    for pid in "${pids[@]}"; do
        local agent="${agent_names[$i]}"
        if wait "$pid"; then
            echo "[PARALLEL] ${agent} completed successfully (pid: ${pid})"
        else
            echo "[PARALLEL] ${agent} FAILED (pid: ${pid})"
            all_passed=false
        fi
        i=$((i + 1))
    done

    if [[ "$all_passed" == "true" ]]; then
        echo "[PARALLEL] All agents completed successfully."
        return 0
    else
        echo "[PARALLEL] Some agents failed."
        return 1
    fi
}
