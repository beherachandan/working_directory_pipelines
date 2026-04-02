#!/usr/bin/env bash
# orchestrator.sh — AEO Content Engine main entry point
# Runs the full 22-agent DAG with gates, revision loops, parallel groups, and resume capability
#
# Usage:
#   ./orchestrator.sh run    <slug> <topic>     — Run full pipeline for a topic
#   ./orchestrator.sh resume <slug>             — Resume a paused/failed pipeline
#   ./orchestrator.sh status <slug>             — Show pipeline status
#   ./orchestrator.sh list                      — List all runs
#   ./orchestrator.sh dry-run <slug> <agent>    — Preview prompt for an agent
#   ./orchestrator.sh single <slug> <agent>     — Run a single agent only
#
# Examples:
#   ./orchestrator.sh run formative-assessment "What are formative assessment strategies?"
#   ./orchestrator.sh resume formative-assessment
#   ./orchestrator.sh status formative-assessment

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENGINE_DIR="$SCRIPT_DIR"

# Source all library modules
source "${ENGINE_DIR}/lib/state-manager.sh"
source "${ENGINE_DIR}/lib/prompt-builder.sh"
source "${ENGINE_DIR}/lib/agent-runner.sh"
source "${ENGINE_DIR}/lib/gate-checker.sh"
source "${ENGINE_DIR}/lib/parallel-runner.sh"
source "${ENGINE_DIR}/lib/human-gate.sh"

# ── Pipeline execution ──
run_pipeline() {
    local slug="$1"
    local run_dir="${RUNS_DIR}/${slug}"

    echo ""
    echo "╔══════════════════════════════════════════════════╗"
    echo "║  AEO Content Engine — Pipeline Execution        ║"
    echo "╠══════════════════════════════════════════════════╣"
    echo "║  Article: $(printf '%-39s' "$slug") ║"
    echo "║  Topic:   $(printf '%-39s' "$(state_get "$slug" '.topic' | cut -c1-39)")║"
    echo "╚══════════════════════════════════════════════════╝"
    echo ""

    state_update "$slug" '.status = "running"'

    # ════════════════════════════════════════
    # PHASE A: Demand Intelligence (sequential)
    # ════════════════════════════════════════
    echo "━━━ Phase A: Demand Intelligence ━━━"
    run_agent "$slug" "A1" || { echo "FATAL: A1 failed"; return 1; }
    run_agent "$slug" "A2" || { echo "FATAL: A2 failed"; return 1; }

    # ════════════════════════════════════════
    # PHASE B: Content Planning (sequential)
    # ════════════════════════════════════════
    echo "━━━ Phase B: Content Planning ━━━"
    run_agent "$slug" "B1" || { echo "FATAL: B1 failed"; return 1; }
    run_agent "$slug" "B2" || { echo "FATAL: B2 failed"; return 1; }
    run_agent "$slug" "B3" || { echo "FATAL: B3 failed"; return 1; }

    # ════════════════════════════════════════
    # PHASE C → D LOOP (with revision capability)
    # ════════════════════════════════════════
    local loop_result
    loop_result=$(run_generation_quality_loop "$slug")

    if [[ "$loop_result" == "ESCALATE" ]]; then
        state_update "$slug" '.status = "escalated"'
        echo ""
        echo "⚠ ESCALATED: Article exceeded max revision loops."
        echo "  Human intervention required. Review revision history in: ${run_dir}/revisions/"
        return 1
    fi

    # ════════════════════════════════════════
    # PHASE E: Expert Review (parallel E1 + E2)
    # ════════════════════════════════════════
    echo "━━━ Phase E: Expert Review ━━━"

    # E2 (automated brand voice review) runs alongside E1 (human)
    run_agent "$slug" "E2" || echo "WARNING: E2 failed (non-blocking)"

    # E1 human gate
    if ! state_agent_is_done "$slug" "E1"; then
        # Check if human review is already submitted
        if is_human_review_done "$slug"; then
            # Process the feedback
            local e_decision
            e_decision=$(check_e_gate "$slug")

            case "$e_decision" in
                PASS)
                    echo "[E-Gate] APPROVED — proceeding to publish."
                    state_agent_complete "$slug" "E1" "revisions/e1-feedback.md"
                    ;;
                REVISE)
                    echo "[E-Gate] NEEDS REVISION — looping back to generation."
                    state_reset_for_revision "$slug"
                    loop_result=$(run_generation_quality_loop "$slug")
                    if [[ "$loop_result" == "ESCALATE" ]]; then
                        state_update "$slug" '.status = "escalated"'
                        echo "⚠ ESCALATED after E1 revision."
                        return 1
                    fi
                    # Re-enter E phase
                    run_agent "$slug" "E2" || true
                    prepare_human_review "$slug"
                    return 0
                    ;;
                ESCALATE)
                    state_update "$slug" '.status = "escalated"'
                    echo "⚠ ESCALATED: Max revisions reached after E1 feedback."
                    return 1
                    ;;
            esac
        else
            # Human review not yet submitted — pause
            prepare_human_review "$slug"
            return 0
        fi
    fi

    # ════════════════════════════════════════
    # PHASE F: Publish & Distribute
    # ════════════════════════════════════════
    echo "━━━ Phase F: Publish & Distribute ━━━"

    # F1 + F2 in parallel
    run_parallel "$slug" "F1 F2" || echo "WARNING: F1/F2 partial failure"

    # F3 → F4 sequential
    run_agent "$slug" "F3" || echo "WARNING: F3 failed"
    run_agent "$slug" "F4" || echo "WARNING: F4 failed"

    # F5 → F6 sequential
    run_agent "$slug" "F5" || echo "WARNING: F5 failed"
    run_agent "$slug" "F6" || echo "WARNING: F6 failed"

    # ════════════════════════════════════════
    # PHASE G: Monitor & Learn
    # ════════════════════════════════════════
    echo "━━━ Phase G: Monitor & Learn ━━━"
    run_agent "$slug" "G1" || echo "WARNING: G1 failed"
    run_agent "$slug" "G2" || echo "WARNING: G2 failed"

    # ════════════════════════════════════════
    # DONE
    # ════════════════════════════════════════
    state_complete "$slug"

    echo ""
    echo "╔══════════════════════════════════════════════════╗"
    echo "║  ✓ Pipeline Complete                            ║"
    echo "╠══════════════════════════════════════════════════╣"
    local total_cost
    total_cost=$(state_get "$slug" '.token_usage.cost_estimate_usd')
    local rev_count
    rev_count=$(state_get "$slug" '.revisions.count')
    echo "║  Article:    $(printf '%-36s' "$slug") ║"
    echo "║  Revisions:  $(printf '%-36s' "$rev_count") ║"
    echo "║  Est. cost:  $(printf '%-36s' "\$${total_cost}") ║"
    echo "╚══════════════════════════════════════════════════╝"
    echo ""
}

# ── Demand Gap Audit — runs only A1+A2 as a diagnostic ──
# Usage: run_demand_audit "formative-assessment" "formative assessment strategies"
run_demand_audit() {
    local slug="$1"
    local topic="$2"
    local audit_slug="audit-${slug}"
    local run_dir="${RUNS_DIR}/${audit_slug}"

    echo ""
    echo "╔══════════════════════════════════════════════════╗"
    echo "║  AEO Demand Gap Audit                           ║"
    echo "╠══════════════════════════════════════════════════╣"
    echo "║  Topic: $(printf '%-43s' "$topic") ║"
    echo "╚══════════════════════════════════════════════════╝"
    echo ""

    # ── Build internal coverage snapshot from existing runs ──
    local coverage_lines=""
    local found_runs=0
    if [[ -d "${RUNS_DIR}" ]]; then
        for state_file in "${RUNS_DIR}"/*/state.json; do
            [[ -f "$state_file" ]] || continue
            local run_slug run_status run_topic d1_composite rev_count
            run_slug=$(jq -r '.article_slug // ""' "$state_file" 2>/dev/null)
            # Skip other audit runs
            [[ "$run_slug" == audit-* ]] && continue
            run_status=$(jq -r '.status // "unknown"' "$state_file" 2>/dev/null)
            run_topic=$(jq -r '.topic // ""' "$state_file" 2>/dev/null)
            d1_composite=$(jq -r '.gates.D_gate.composite // "n/a"' "$state_file" 2>/dev/null)
            rev_count=$(jq -r '.revisions.count // 0' "$state_file" 2>/dev/null)
            coverage_lines+="- ${run_slug}: \"${run_topic}\" (status: ${run_status}, D1: ${d1_composite}, revisions: ${rev_count})"$'\n'
            found_runs=$((found_runs + 1))
        done
    fi

    local internal_context
    if [[ $found_runs -gt 0 ]]; then
        internal_context="### Published Articles (Internal Coverage — ${found_runs} articles in pipeline)

Use these to determine Gap Factor in your Opportunity Score calculation.
- Articles with status 'completed' = Wayground has content → check if it covers this topic
- If a topic matches or overlaps → Gap Factor = 1.0 (optimization) or 1.2 (weak)
- If no match → Gap Factor = 1.5 (no coverage)

${coverage_lines}"
    else
        internal_context="### Published Articles (Internal Coverage)

No completed pipeline runs found. Treat all topics as Gap Factor = 1.5 (no Wayground coverage)."
    fi

    # ── Initialize audit run (guard against re-init) ──
    if [[ -f "${run_dir}/state.json" ]]; then
        echo "Resuming existing audit run: ${audit_slug}"
    else
        state_init "$audit_slug" "$topic"
    fi

    # ── Run A1 with internal coverage context ──
    echo "━━━ Phase A1: Query Intelligence ━━━"
    run_agent "$audit_slug" "A1" "$internal_context" || {
        echo "FATAL: A1 failed. Check logs at ${run_dir}/logs/A1.log"
        return 1
    }

    # ── Run A2 (uses A1 output automatically via dep graph) ──
    echo "━━━ Phase A2: Competitive Intelligence ━━━"
    run_agent "$audit_slug" "A2" || {
        echo "WARNING: A2 failed. Gap report will be based on A1 only."
    }

    # ── Print gap report ──
    echo ""
    echo "╔══════════════════════════════════════════════════╗"
    echo "║  Demand Gap Report                              ║"
    echo "╠══════════════════════════════════════════════════╣"

    # Internal coverage section (from injected context)
    echo "║  INTERNAL COVERAGE                              ║"
    echo "╠══════════════════════════════════════════════════╣"
    if [[ $found_runs -gt 0 ]]; then
        printf "║  %-48s ║\n" "${found_runs} articles in pipeline:"
        for state_file in "${RUNS_DIR}"/*/state.json; do
            [[ -f "$state_file" ]] || continue
            local r_slug r_status r_d1
            r_slug=$(jq -r '.article_slug // ""' "$state_file" 2>/dev/null)
            [[ "$r_slug" == audit-* ]] && continue
            r_status=$(jq -r '.status // "unknown"' "$state_file" 2>/dev/null)
            r_d1=$(jq -r '.gates.D_gate.composite // "—"' "$state_file" 2>/dev/null)
            printf "║    %-46s ║\n" "${r_slug} (${r_status}, D1:${r_d1})"
        done
    else
        printf "║  %-48s ║\n" "No existing articles found"
    fi

    # External demand / gaps (from A1 output)
    local a1_output_path
    a1_output_path=$(jq -r '.dag_progress["A1"].output_file // ""' "${run_dir}/state.json" 2>/dev/null)
    echo "╠══════════════════════════════════════════════════╣"
    echo "║  OUTPUTS                                        ║"
    echo "╠══════════════════════════════════════════════════╣"
    if [[ -n "$a1_output_path" && -f "${run_dir}/${a1_output_path}" ]]; then
        printf "║  A1: %-44s ║\n" "${run_dir}/${a1_output_path}"
    fi
    local a2_output_path
    a2_output_path=$(jq -r '.dag_progress["A2"].output_file // ""' "${run_dir}/state.json" 2>/dev/null)
    if [[ -n "$a2_output_path" && -f "${run_dir}/${a2_output_path}" ]]; then
        printf "║  A2: %-44s ║\n" "${run_dir}/${a2_output_path}"
    fi

    echo "╠══════════════════════════════════════════════════╣"
    local total_cost
    total_cost=$(state_get "$audit_slug" '.token_usage.cost_estimate_usd')
    printf "║  Est. cost: %-37s ║\n" "\$${total_cost}"
    echo "╚══════════════════════════════════════════════════╝"
    echo ""
    echo "Review full outputs above. Look for:"
    echo "  • opportunity_score + gap_factor in A1 output"
    echo "  • double_gap: true entries in A2 output"
    echo "  • Domains where Wayground is absent (A2 citation landscape)"
    echo ""
}

# ── Generation + Quality loop (C-phase → D-phase with revision) ──
# Returns: PASS or ESCALATE
run_generation_quality_loop() {
    local slug="$1"

    while true; do
        # ── PHASE C: Content Generation (sequential) ──
        echo "━━━ Phase C: Content Generation ━━━" >&2
        run_agent "$slug" "C1" || { echo "FATAL: C1 failed" >&2; return 1; }
        run_agent "$slug" "C2" || { echo "FATAL: C2 failed" >&2; return 1; }
        run_agent "$slug" "C3" || { echo "FATAL: C3 failed" >&2; return 1; }
        run_agent "$slug" "C4" || { echo "FATAL: C4 failed" >&2; return 1; }
        run_agent "$slug" "C5" || { echo "FATAL: C5 failed" >&2; return 1; }

        # ── PHASE D: Quality Gate (parallel D1-D4) ──
        echo "━━━ Phase D: Quality Gate ━━━" >&2
        run_parallel "$slug" "D1 D2 D3 D4" || echo "WARNING: Some D-phase agents failed" >&2

        # ── D-GATE CHECK ──
        local d_decision
        d_decision=$(check_d_gate "$slug")
        echo "[D-Gate] Decision: ${d_decision}" >&2

        case "$d_decision" in
            PASS)
                echo "[D-Gate] PASSED — all dimensions ≥ 7." >&2
                echo "PASS"
                return 0
                ;;
            REVISE)
                local rev_count
                rev_count=$(state_get "$slug" '.revisions.count')
                echo "[D-Gate] REVISE — revision #${rev_count}. Looping back to C-phase." >&2
                state_reset_for_revision "$slug"
                # Loop continues
                ;;
            ESCALATE)
                echo "[D-Gate] ESCALATE — max revisions reached." >&2
                echo "ESCALATE"
                return 0
                ;;
            *)
                echo "ERROR: Unexpected D-gate decision: ${d_decision}" >&2
                return 1
                ;;
        esac
    done
}

# ── Status display ──
show_status() {
    local slug="$1"
    local run_dir="${RUNS_DIR}/${slug}"

    if [[ ! -f "${run_dir}/state.json" ]]; then
        echo "No run found for: ${slug}"
        return 1
    fi

    echo ""
    echo "Pipeline Status: ${slug}"
    echo "════════════════════════════════"

    local status topic stage rev_count cost
    status=$(state_get "$slug" '.status')
    topic=$(state_get "$slug" '.topic')
    stage=$(state_get "$slug" '.current_stage')
    rev_count=$(state_get "$slug" '.revisions.count')
    cost=$(state_get "$slug" '.token_usage.cost_estimate_usd')

    echo "Topic:     ${topic}"
    echo "Status:    ${status}"
    echo "Stage:     ${stage}"
    echo "Revisions: ${rev_count}"
    echo "Est. cost: \$${cost}"
    echo ""
    echo "Agent Progress:"
    echo "──────────────────────────────"

    for agent in "${ALL_AGENTS[@]}"; do
        local agent_status
        agent_status=$(state_get "$slug" ".dag_progress[\"${agent}\"].status")
        local icon
        case "$agent_status" in
            completed)  icon="✓" ;;
            running)    icon="▶" ;;
            failed)     icon="✗" ;;
            pending)    icon="○" ;;
            *)          icon="?" ;;
        esac
        printf "  %s %-4s %s\n" "$icon" "$agent" "$agent_status"
    done

    echo ""

    # Show gate decisions
    local d_gate e_gate
    d_gate=$(state_get "$slug" '.gates.D_gate.decision')
    e_gate=$(state_get "$slug" '.gates.E_gate.decision')
    echo "Gates:"
    echo "  D-Gate: ${d_gate:-pending}"
    echo "  E-Gate: ${e_gate:-pending}"
    echo ""
}

# ── Main CLI ──
main() {
    local command="${1:-help}"

    case "$command" in
        run)
            local slug="${2:?Usage: orchestrator.sh run <slug> <topic>}"
            local topic="${3:?Usage: orchestrator.sh run <slug> <topic>}"
            state_init "$slug" "$topic"
            run_pipeline "$slug"
            ;;
        resume)
            local slug="${2:?Usage: orchestrator.sh resume <slug>}"
            if [[ ! -f "${RUNS_DIR}/${slug}/state.json" ]]; then
                echo "No run found for: ${slug}"
                exit 1
            fi
            run_pipeline "$slug"
            ;;
        status)
            local slug="${2:?Usage: orchestrator.sh status <slug>}"
            show_status "$slug"
            ;;
        list)
            echo "All runs:"
            echo "══════════════════════════════"
            printf "%-30s %-15s %-8s %s\n" "SLUG" "STATUS" "STAGE" "REVISIONS"
            echo "──────────────────────────────────────────────────────────────"
            state_list_runs | while IFS='|' read -r slug status stage revs; do
                printf "%-30s %-15s %-8s %s\n" "$(echo "$slug" | xargs)" "$(echo "$status" | xargs)" "$(echo "$stage" | xargs)" "$(echo "$revs" | xargs)"
            done
            ;;
        dry-run)
            local slug="${2:?Usage: orchestrator.sh dry-run <slug> <agent>}"
            local agent="${3:?Usage: orchestrator.sh dry-run <slug> <agent>}"
            dry_run_agent "$slug" "$agent"
            ;;
        single)
            local slug="${2:?Usage: orchestrator.sh single <slug> <agent>}"
            local agent="${3:?Usage: orchestrator.sh single <slug> <agent>}"
            run_agent "$slug" "$agent"
            ;;
        audit)
            local slug="${2:?Usage: orchestrator.sh audit <slug> <topic>}"
            local topic="${3:?Usage: orchestrator.sh audit <slug> <topic>}"
            run_demand_audit "$slug" "$topic"
            ;;
        reset)
            local slug="${2:?Usage: orchestrator.sh reset <slug>}"
            echo "This will delete ALL data (outputs + state) for run: ${slug}"
            read -rp "Are you sure? [y/N] " confirm
            if [[ "$confirm" =~ ^[Yy] ]]; then
                state_delete "$slug"
            fi
            ;;
        help|*)
            echo "AEO Content Engine — Orchestrator"
            echo ""
            echo "Usage:"
            echo "  ./orchestrator.sh run    <slug> <topic>   — Run full pipeline"
            echo "  ./orchestrator.sh resume <slug>           — Resume paused/failed run"
            echo "  ./orchestrator.sh status <slug>           — Show pipeline status"
            echo "  ./orchestrator.sh list                    — List all runs"
            echo "  ./orchestrator.sh dry-run <slug> <agent>  — Preview prompt"
            echo "  ./orchestrator.sh single <slug> <agent>   — Run single agent"
            echo "  ./orchestrator.sh reset  <slug>           — Delete a run"
            echo "  ./orchestrator.sh audit  <slug> <topic>   — Demand gap audit (A1+A2 only)"
            echo ""
            echo "Examples:"
            echo "  ./orchestrator.sh run formative-assessment 'What are formative assessment strategies?'"
            echo "  ./orchestrator.sh resume formative-assessment"
            echo "  ./orchestrator.sh dry-run formative-assessment B3"
            echo "  ./orchestrator.sh audit formative-assessment 'formative assessment strategies'"
            ;;
    esac
}

main "$@"
