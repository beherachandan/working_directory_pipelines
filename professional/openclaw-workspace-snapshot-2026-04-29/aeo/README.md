# AEO Content Engine — MVP

> Slack-triggered pipeline: topic pillar → ranked theme discovery → user selection → N parallel article drafts → AEO quality gate → human review.

## MVP Scope

6 agents + 1 orchestrator covering the critical path:

```
/aeo "<topic pillar>" [n=<number>]
         ↓
    O1  Orchestrator       — state, routing, Slack I/O
         ↓
    A1  Query Intel        — discover all themes, score by AEO opportunity
         ↓
    [User selects N themes from ranked list, max 10]
         ↓
    [N parallel pipelines]
    B2  EAR Decomposer     — what each article must cover
    B3  Content Brief      — full structured brief per article
    C3  Draft Generator    — research + outline + write
    C4  Citation Enricher  — inject stats, quotes, sources (+41% AEO)
    D1  AEO Evaluator      — 5-dimension score gate (all ≥7 to pass)
         ↓
    [PASS → human review in Slack]
    [FAIL → back to C3, max 2 loops, then escalate]
```

## Folder Structure

```
aeo/
├── README.md                        ← You are here
├── skills/
│   ├── _shared/
│   │   ├── product-context.md       ← Wayground context (all skills read)
│   │   ├── brand-voice-guide.md     ← Tone & voice (⚠️ needs real WG brand doc)
│   │   └── aeo-scoring-rubric.md    ← 5-dimension scoring criteria
│   ├── O1-orchestrator/
│   │   └── SKILL.md
│   ├── A1-query-intelligence/
│   │   └── SKILL.md
│   ├── B2-ear-decomposer/
│   │   └── SKILL.md
│   ├── B3-content-brief-generator/
│   │   └── SKILL.md
│   ├── C3-draft/
│   │   └── SKILL.md
│   ├── C4-citation-enricher/
│   │   └── SKILL.md
│   └── D1-aeo-evaluator/
│       └── SKILL.md
```

## Slack Usage

```
/aeo "formative assessment"          → runs with default n=3
/aeo "classroom management" n=5      → generates 5 articles
/aeo "blended learning" n=10         → maximum batch size
```

After A1 runs, bot posts ranked theme list. User replies with numbers (e.g. `1,3,5`).

## Quality Gate

All 5 dimensions must score ≥ 7:

| Dimension | Weight | What it checks |
|-----------|--------|----------------|
| QAPE | 25% | Question → Answer → Proof → Expansion structure |
| EAR | 25% | Entity-Attribute-Relationship coverage completeness |
| Extractability | 20% | AI can chunk and extract clean answers |
| Trust & Authority | 20% | Stats, quotes, citations, first-person signals |
| Intent Match | 10% | Format matches query intent type |

Fail → back to C3 (max 2 loops) → human escalation.

## Deferred (Post-MVP)

| Item | Phase |
|------|-------|
| A2 Competitive Intelligence | v2 |
| B1 Intent Classifier (standalone) | v2 |
| C1 Research, C2 Outline (separate) | v2 |
| D2 Fact Check, D3 SEO, D4 Extractability (separate) | v2 |
| E1 SME Vetting, E2 Brand Voice (automated) | v2 |
| F1-F6 Publish & Distribution | v3 |
| G1-G2 SOV Tracking & Feedback | v3 |
| Cron triggers | post-MVP |
| CMS / Webflow publish | post-MVP |

## Action Items Before First Run

- [ ] Replace `_shared/brand-voice-guide.md` placeholder with real Wayground brand doc
- [ ] Confirm DataForSEO / SEMrush API keys available (A1 falls back to web_search if not)
- [ ] Set up `/aeo` Slack slash command pointing to O1
- [ ] Test with one topic pillar end-to-end
