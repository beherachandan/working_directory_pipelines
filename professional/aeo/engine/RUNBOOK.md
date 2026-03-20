# AEO Content Engine — Operator Runbook

## Prerequisites

- **Claude CLI** (`claude`) installed and authenticated — [install guide](https://docs.anthropic.com/en/docs/claude-code)
- **jq** installed (`brew install jq` on macOS)
- **bc** installed (standard on macOS)
- **bash 3.2+** (macOS default works)

### MCP Servers (optional, enhance quality)

| MCP | Status | Used By |
|-----|--------|---------|
| DataForSEO | Placeholder credentials in `.mcp.json` | A1, A2, D3 |
| SEMrush | Placeholder credentials in `.mcp.json` | A1, B2, D3 |
| Webflow | OAuth configured | F2, F4 |
| Google Search Console | Not yet configured | F4, G1 |

Without MCP servers, agents still work — they produce output based on LLM knowledge instead of live data.

---

## Quick Start

```bash
cd professional/aeo/engine

# Run a new article
./orchestrator.sh run <slug> "<topic question>"

# Example
./orchestrator.sh run formative-assessment "What are formative assessment strategies?"
```

---

## Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `run` | `./orchestrator.sh run <slug> <topic>` | Start a new pipeline run |
| `resume` | `./orchestrator.sh resume <slug>` | Resume a paused/failed run |
| `status` | `./orchestrator.sh status <slug>` | Show pipeline progress |
| `list` | `./orchestrator.sh list` | List all runs with status |
| `dry-run` | `./orchestrator.sh dry-run <slug> <agent>` | Preview prompt for an agent |
| `single` | `./orchestrator.sh single <slug> <agent>` | Run one agent only |
| `reset` | `./orchestrator.sh reset <slug>` | Delete a run (destructive) |

---

## Pipeline Phases

```
A1 → A2 → B1 → B2 → B3 → C1 → C2 → C3 → C4 → C5
                                                    ↓
                                              D1 D2 D3 D4  (parallel)
                                                    ↓
                                              [D-Gate Check]
                                              PASS → E1 + E2
                                              REVISE → back to C1
                                              ESCALATE → human
                                                    ↓
                                              [E-Gate Check]
                                              APPROVED → F1+F2 → F3 → F4 → F5 → F6
                                                    ↓
                                              G1 → G2
```

### Phase Details

| Phase | Agents | Type | Description |
|-------|--------|------|-------------|
| A — Demand Intel | A1, A2 | Sequential | Question mining, competitor analysis |
| B — Planning | B1, B2, B3 | Sequential | Intent classification, EAR decomposition, content brief |
| C — Generation | C1-C5 | Sequential | Research, outline, draft, citation enrichment, composition |
| D — Quality Gate | D1-D4 | Parallel | AEO evaluation, fact-check, SEO audit, extractability |
| E — Expert Review | E1, E2 | E2 auto, E1 human | Brand voice review, SME/teacher review |
| F — Publish | F1-F6 | Mixed | Schema, page design, linking, publish, distribution, channel adapt |
| G — Monitor | G1, G2 | Sequential | SOV tracking, feedback analysis |

---

## E1 Human Review Workflow

When the pipeline reaches E1, it **pauses** and creates review materials.

### 1. Pipeline Pauses

```
⏸ HUMAN REVIEW REQUIRED
Article: formative-assessment

Review materials are in: runs/formative-assessment/
  - outputs/C5-composer.md      ← Final draft to review
  - outputs/D1-aeo-evaluator.md ← Score card
  - outputs/D2-fact-check.md    ← Fact check report
  - revisions/REVIEW-INSTRUCTIONS.md ← What to do

Fill in: revisions/e1-feedback.md
Then run: ./orchestrator.sh resume formative-assessment
```

### 2. Review the Draft

Read `outputs/C5-composer.md` (the composed article). Check:
- Factual accuracy for your subject area
- Classroom applicability and practical value
- Tone (educator-friendly, not marketing)
- Wayground product mentions feel natural

### 3. Fill in Feedback

Edit `revisions/e1-feedback.md`. The first line must be one of:

```
DECISION: Approved
```
or
```
DECISION: Needs Revision
```

If requesting revision, add specific feedback below the decision line.

### 4. Resume

```bash
./orchestrator.sh resume formative-assessment
```

- **Approved** → pipeline proceeds to F-phase (publish)
- **Needs Revision** → loops back to C-phase with your feedback injected
- After 2 revision loops → ESCALATE (manual intervention required)

---

## Quality Gates

### D-Gate (Automated)

D1 scores the article on 5 dimensions (each 1-10):

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| QAPE Structure | 25% | Question→Answer→Proof→Expansion format |
| EAR Coverage | 25% | Entity-Attribute-Relationship sub-query coverage |
| Extractability | 20% | AI snippet readiness (40-60 word answers, tables, lists) |
| Trust Signals | 20% | Citations, expert quotes, data attribution |
| Intent Match | 10% | Alignment with searcher intent |

**PASS:** All 5 dimensions ≥ 7
**REVISE:** Any dimension < 7 (feedback compiled from D1-D4, sent back to C-phase)
**ESCALATE:** 2 revision loops failed

### E-Gate (Human)

SME/teacher reviews the draft. See E1 workflow above.

---

## Resume & Recovery

The pipeline is **resume-capable**. If it fails or is interrupted:

```bash
# Check where it stopped
./orchestrator.sh status <slug>

# Resume — completed agents are skipped
./orchestrator.sh resume <slug>
```

### Common Failure Scenarios

| Scenario | What Happens | Fix |
|----------|-------------|-----|
| API rate limit | Agent fails, pipeline stops | Wait a few minutes, then `resume` |
| Agent produces bad output | D-gate catches it, auto-revises | Automatic (up to 2 loops) |
| State file locked | Lock timeout after 5s | Delete `runs/<slug>/state.json.lock/` dir, then `resume` |
| Pipeline stuck at E1 | Waiting for human review | Fill in `e1-feedback.md`, then `resume` |
| Escalated | 2 revision loops failed | Review `runs/<slug>/revisions/` history, manually fix or adjust brief |

---

## File Structure

```
engine/
  orchestrator.sh          # Main CLI entry point
  RUNBOOK.md               # This file
  lib/
    state-manager.sh       # JSON state management (jq-based)
    prompt-builder.sh      # 4-part prompt assembly
    agent-runner.sh        # claude CLI invocation
    gate-checker.sh        # D-gate and E-gate logic
    parallel-runner.sh     # Concurrent agent execution
    human-gate.sh          # E1 pause/resume
  prompts/
    system-preamble.md     # Universal system prompt
    revision-addendum.md   # Revision feedback template
  runs/
    {slug}/
      state.json           # Pipeline state
      outputs/             # Agent outputs (one .md per agent)
      revisions/           # Revision feedback + E1 review materials
      logs/                # Execution logs + prompts for debugging
```

---

## Cost Management

### Model Routing

| Model | Agents | Price (input/output per 1M tokens) |
|-------|--------|-----------------------------------|
| Opus | C3, C5, D1 | $15 / $75 |
| Sonnet | All others (21 agents) | $3 / $15 |

### Estimated Cost Per Article

- **No revisions:** ~$8-10
- **1 revision loop:** ~$12-15 (C1-C5 + D1-D4 re-run)
- **2 revision loops:** ~$16-20
- **Escalated:** Same as 2 loops + human time

### Monitoring Cost

After each run:
```bash
./orchestrator.sh status <slug>
# Shows "Est. cost: $X.XX"
```

Or check directly:
```bash
jq '.token_usage' runs/<slug>/state.json
```

---

## Debugging

### View an agent's prompt
```bash
# Before running
./orchestrator.sh dry-run <slug> <agent>

# After running (saved automatically)
cat runs/<slug>/logs/<agent>-prompt.md
```

### View raw claude output
```bash
cat runs/<slug>/logs/<agent>-raw.md
```

### Re-run a single agent
```bash
# Reset the agent's status to pending first
jq '.dag_progress["A1"].status = "pending"' runs/<slug>/state.json > /tmp/state.tmp && mv /tmp/state.tmp runs/<slug>/state.json

# Then run it
./orchestrator.sh single <slug> A1
```

### Check gate decisions
```bash
jq '.gates' runs/<slug>/state.json
```

---

## Choosing Topics

Good AEO topics have:
- **Search volume:** 1,000+ monthly (US)
- **Intent:** Informational or how-to (not navigational)
- **AI Overview presence:** Google shows an AI Overview for the query
- **Wayground relevance:** Topic connects naturally to education/assessment/quizzes
- **Gap:** Current AI citations don't mention Wayground or are incomplete

### Slug Conventions

- Lowercase, hyphenated: `formative-assessment`, `exit-tickets`, `blooket-vs-wayground`
- Match the URL path: slug becomes `/learn/{slug}`
- Keep short but descriptive

---

## Batch Operations

To run multiple articles sequentially:
```bash
topics=(
    "formative-assessment|What are formative assessment strategies?"
    "exit-tickets|How to use exit tickets in the classroom"
    "blooket-vs-wayground|Blooket vs Wayground comparison"
)

for entry in "${topics[@]}"; do
    IFS='|' read -r slug topic <<< "$entry"
    echo "Starting: $slug"
    ./orchestrator.sh run "$slug" "$topic"
done
```

Note: Each article pauses at E1 for human review. Run in batches of 3-5, review all E1s, then resume all.
