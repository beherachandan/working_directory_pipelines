#!/usr/bin/env bash
# prompt-builder.sh — 4-part prompt assembly for agent invocation
# Assembles: system preamble + shared context + agent definition + task payload
# Usage: source this file, then call build_prompt
# Compatible with bash 3.2+ (no associative arrays)

set -euo pipefail

ENGINE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENTS_DIR="${ENGINE_DIR}/../agents"
PROMPTS_DIR="${ENGINE_DIR}/prompts"
RUNS_DIR="${ENGINE_DIR}/runs"

# ── Agent → Directory mapping ──
get_agent_dir() {
    case "$1" in
        A1) echo "A1-query-intelligence" ;;
        A2) echo "A2-competitive-intelligence" ;;
        B1) echo "B1-intent-classifier" ;;
        B2) echo "B2-ear-decomposer" ;;
        B3) echo "B3-content-brief-generator" ;;
        C1) echo "C1-research" ;;
        C2) echo "C2-outline" ;;
        C3) echo "C3-draft" ;;
        C4) echo "C4-citation-enricher" ;;
        C5) echo "C5-composer" ;;
        D1) echo "D1-aeo-evaluator" ;;
        D2) echo "D2-fact-check" ;;
        D3) echo "D3-seo" ;;
        D4) echo "D4-extractability-optimizer" ;;
        E1) echo "E1-sme-teacher" ;;
        E2) echo "E2-brand-voice-reviewer" ;;
        F1) echo "F1-schema-markup" ;;
        F2) echo "F2-page-designer" ;;
        F3) echo "F3-internal-linking" ;;
        F4) echo "F4-publisher" ;;
        F5) echo "F5-distribution-strategist" ;;
        F6) echo "F6-channel-adaptor" ;;
        G1) echo "G1-sov-tracker" ;;
        G2) echo "G2-feedback-analyst" ;;
        *) echo "" ;;
    esac
}

# ── Agent → Required upstream outputs ──
get_agent_deps() {
    case "$1" in
        A1) echo "" ;;
        A2) echo "A1" ;;
        B1) echo "A1 A2" ;;
        B2) echo "A1 A2 B1" ;;
        B3) echo "A1 A2 B1 B2" ;;
        C1) echo "B3" ;;
        C2) echo "B3 C1" ;;
        C3) echo "B3 C1 C2" ;;
        C4) echo "B3 C1 C3" ;;
        C5) echo "B3 C4" ;;
        D1) echo "B3 C5" ;;
        D2) echo "C5" ;;
        D3) echo "B3 C5" ;;
        D4) echo "C5" ;;
        E1) echo "B3 C5 D1 D2 D3 D4" ;;
        E2) echo "B3 C5" ;;
        F1) echo "B3 C5" ;;
        F2) echo "B3 C5" ;;
        F3) echo "B3 C5 F1" ;;
        F4) echo "C5 F1 F2 F3" ;;
        F5) echo "B3 C5 F4" ;;
        F6) echo "C5 F4 F5" ;;
        G1) echo "F4" ;;
        G2) echo "G1 D1 E1" ;;
        *) echo "" ;;
    esac
}

# ── Agent → Shared context files ──
get_agent_shared_context() {
    case "$1" in
        B3|C2|C3|C5|F2|F6) echo "product-context brand-voice-guide" ;;
        D1|D3)              echo "product-context aeo-scoring-rubric" ;;
        D4)                 echo "product-context aeo-scoring-rubric" ;;
        E1)                 echo "product-context brand-voice-guide aeo-scoring-rubric" ;;
        E2)                 echo "product-context brand-voice-guide" ;;
        *)                  echo "product-context" ;;
    esac
}

# ── Agent → Output template (empty if none) ──
get_agent_template() {
    case "$1" in
        A1|A2|B1|B2) echo "topic-dossier" ;;
        B3)          echo "content-brief" ;;
        D1)          echo "score-card" ;;
        F5)          echo "distribution-plan" ;;
        *)           echo "" ;;
    esac
}

# ── Agent → Model selection ──
get_agent_model() {
    case "$1" in
        C3|C5|D1) echo "opus" ;;
        *)        echo "sonnet" ;;
    esac
}

# ── Output filename for an agent ──
get_output_filename() {
    local agent="$1"
    local dir_name
    dir_name=$(get_agent_dir "$agent")
    echo "outputs/${agent}-${dir_name#*-}.md"
}

# ── Main prompt builder ──
# Usage: build_prompt "formative-assessment" "A1" ["extra context"]
build_prompt() {
    local slug="$1"
    local agent="$2"
    local extra_context="${3:-}"
    local run_dir="${RUNS_DIR}/${slug}"
    local prompt=""

    # ── Part 1: System Preamble ──
    prompt+="$(cat "${PROMPTS_DIR}/system-preamble.md")"
    prompt+=$'\n\n'

    # ── Part 2: Shared Context ──
    prompt+="---"$'\n'
    prompt+="## Shared Context"$'\n\n'

    local shared_files
    shared_files=$(get_agent_shared_context "$agent")
    for ctx_file in $shared_files; do
        local ctx_path="${AGENTS_DIR}/_shared/${ctx_file}.md"
        if [[ -f "$ctx_path" ]]; then
            prompt+="### ${ctx_file}"$'\n'
            prompt+="$(cat "$ctx_path")"
            prompt+=$'\n\n'
        fi
    done

    # ── Part 3: Agent Definition ──
    prompt+="---"$'\n'
    prompt+="## Your Agent Definition"$'\n\n'

    local agent_dir_name
    agent_dir_name=$(get_agent_dir "$agent")
    local agent_dir="${AGENTS_DIR}/${agent_dir_name}"
    if [[ -f "${agent_dir}/AGENT.md" ]]; then
        prompt+="$(cat "${agent_dir}/AGENT.md")"
        prompt+=$'\n\n'
    else
        echo "ERROR: Agent definition not found: ${agent_dir}/AGENT.md" >&2
        return 1
    fi

    # Include examples if they exist
    if [[ -d "${agent_dir}/examples" ]]; then
        for example in "${agent_dir}/examples"/*.md; do
            [[ -f "$example" ]] || continue
            prompt+="### Example: $(basename "$example" .md)"$'\n'
            prompt+="$(cat "$example")"
            prompt+=$'\n\n'
        done
    fi

    # ── Part 4: Task Payload ──
    prompt+="---"$'\n'
    prompt+="## Task Payload"$'\n\n'

    # Topic
    local topic
    topic=$(jq -r '.topic' "${run_dir}/state.json" 2>/dev/null || echo "$extra_context")
    prompt+="**Topic:** ${topic}"$'\n\n'

    # Upstream outputs
    local deps
    deps=$(get_agent_deps "$agent")
    if [[ -n "$deps" ]]; then
        prompt+="### Upstream Agent Outputs"$'\n\n'
        for dep_agent in $deps; do
            local dep_output
            dep_output=$(jq -r ".dag_progress[\"${dep_agent}\"].output_file // empty" "${run_dir}/state.json" 2>/dev/null)
            if [[ -n "$dep_output" && -f "${run_dir}/${dep_output}" ]]; then
                prompt+="#### ${dep_agent} Output"$'\n'
                prompt+="$(cat "${run_dir}/${dep_output}")"
                prompt+=$'\n\n'
            fi
        done
    fi

    # Output template (if applicable)
    local template_name
    template_name=$(get_agent_template "$agent")
    if [[ -n "$template_name" ]]; then
        local template_path="${AGENTS_DIR}/templates/${template_name}.md"
        if [[ -f "$template_path" ]]; then
            prompt+="### Output Template"$'\n'
            prompt+="Use this template for your output:"$'\n\n'
            prompt+="$(cat "$template_path")"
            prompt+=$'\n\n'
        fi
    fi

    # Extra context
    if [[ -n "$extra_context" ]]; then
        prompt+="### Additional Context"$'\n'
        prompt+="${extra_context}"$'\n\n'
    fi

    # Revision feedback (if in revision loop)
    local rev_count
    rev_count=$(jq -r '.revisions.count' "${run_dir}/state.json" 2>/dev/null || echo "0")
    if [[ "$rev_count" -gt 0 ]] && [[ "$agent" == "C3" || "$agent" == "C4" || "$agent" == "C5" ]]; then
        local latest_revision_file="${run_dir}/revisions/revision-${rev_count}.md"
        if [[ -f "$latest_revision_file" ]]; then
            local revision_addendum
            revision_addendum=$(cat "${PROMPTS_DIR}/revision-addendum.md")

            local prev_scores
            prev_scores=$(jq -r '.gates.D_gate.d1_scores // "No previous scores"' "${run_dir}/state.json")

            revision_addendum="${revision_addendum//\{\{REVISION_NUMBER\}\}/${rev_count}}"
            revision_addendum="${revision_addendum//\{\{GATE_SOURCE\}\}/D1}"
            revision_addendum="${revision_addendum//\{\{REVISION_FEEDBACK\}\}/$(cat "$latest_revision_file")}"
            revision_addendum="${revision_addendum//\{\{PREVIOUS_SCORES\}\}/${prev_scores}}"

            prompt+="---"$'\n'
            prompt+="${revision_addendum}"$'\n\n'
        fi
    fi

    # Agent-specific instructions
    if [[ "$agent" == "D1" ]]; then
        prompt+="### Machine-Readable Scores"$'\n'
        prompt+="IMPORTANT: In addition to the score card template, include a \`<scores>\` block with JSON:"$'\n'
        prompt+='```'$'\n'
        prompt+='<scores>{"qape": 8, "ear": 7, "extract": 9, "trust": 7, "intent": 8}</scores>'$'\n'
        prompt+='```'$'\n'
        prompt+="This enables automated gate checking. Use the actual scores you assigned."$'\n\n'
    fi

    # Final instruction
    prompt+="---"$'\n'
    prompt+="Now execute your task. **IMPORTANT: Wrap your entire output in \`<output>\` and \`</output>\` tags.** Your output begins with \`<output>\` on its own line and ends with \`</output>\` on its own line. Everything between those tags is your deliverable."$'\n'

    echo "$prompt"
}
