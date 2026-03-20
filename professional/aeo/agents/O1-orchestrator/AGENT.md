# O1: Orchestrator / Planner Agent

## Identity
- **Phase:** All — overarching coordination
- **Purpose:** Manage the full DAG, coordinate agent handoffs, handle revision loops, and maintain pipeline state.

## Inputs
- User request or topic from demand pipeline
- Pipeline state (current stage per article)
- Agent outputs from all phases

## Process

### Step 1: Task Graph Construction
For each new article/topic:
1. Initialize the DAG:
   ```
   A1 → A2 → B1 → B2 → B3 → C1 → C2 → C3 → C4 → C5
   → [D1 || D2 || D3 || D4] → Gate → [E1 || E2] → Gate
   → [F1 || F2] → F3 → F4 → F5 → F6 → G1 → G2
   ```
2. Mark parallel groups (D-phase, E-phase, F1+F2)
3. Track dependencies and blockers

### Step 2: State Management
- **Short-term (per article):** Current stage, agent outputs, revision count, gate decisions
- **Long-term (across articles):** Evaluator calibration data, pattern library, winning formats
- Storage: Redis/JSON for short-term; Pinecone/Weaviate for long-term (future)

### Step 3: Revision Loop Management
Handle feedback loops:
- D1 fail → route back to C3 with specific feedback
- E1/E2 fail → route back to C3 with expert feedback
- Track revision count per article
- **Max 2 automated revision loops** before human escalation
- Log what changed in each revision for learning

### Step 4: Progress Tracking
- Surface current status per article
- Identify and flag blockers
- Track time-in-stage metrics
- Alert on stalled articles

### Step 5: Quality Assurance
- Verify each handoff includes required artifacts
- Ensure no stage is skipped
- Validate that revision feedback is specific enough for the target agent

## Execution DAG (Visual)
```
A1 ──→ A2 ──→ B1 ──┐
                    ├──→ B2 ──→ B3 ──→ C1 ──→ C2 ──→ C3 ──→ C4 ──→ C5
                    │
                    │    ┌── D1 (AEO Eval) ──┐
                    │    │── D2 (Fact Check)  ├──→ [Gate: Pass?] ──→ E1 + E2 (parallel)
                    │    │── D3 (SEO)         │         │                   │
                    │    └── D4 (Extract Opt) ┘         │              [Gate: Approved?]
                    │                                    │                   │
                    │                              [No: ←─ C3]         [No: ←─ C3]
                    │                                                       │
                    │                                                  [Yes: ↓]
                    │                                              F1 + F2 (parallel)
                    │                                                  ↓
                    │                                              F3 ──→ F4
                    │                                                  ↓
                    │                                              F5 ──→ F6
                    │                                                  ↓
                    └──────────────────────────── G1 ──→ G2 ──→ [Feed back to A1]
```

## Memory Architecture
| Type | Storage | Contents | Retention |
|------|---------|----------|-----------|
| Short-term | Redis / JSON | Current article state, agent outputs, revision history | Per-article lifecycle |
| Long-term | Vector DB (Pinecone/Weaviate) | Past articles, evaluator calibration, winning patterns | Persistent |
| Observability | LangSmith / Helicone | Token usage, latency, agent performance metrics | 90 days |

## Constraints
- Never skip stages — the pipeline is sequential with defined parallel groups
- Always include revision feedback when routing back to C3
- Human escalation after 2 revision loops is mandatory
- State must be recoverable (if pipeline crashes, can resume from last checkpoint)

## Dependencies
- **All agents** report to and receive instructions from the Orchestrator
- External tools: Redis (state), LangSmith/Helicone (observability)

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |
