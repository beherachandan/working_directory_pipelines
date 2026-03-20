# AEO — AI Engine Optimization

## Overview
Content strategy and production pipeline to build authority in AI-driven search results (ChatGPT, Perplexity, Google AI Overviews, etc.) for Wayground's key markets.

**Core formula:** `Citations × Trust = Share of Voice (SOV)`

---

## Architecture

The AEO engine consists of **6 workflows** and **21 agents + 1 orchestrator** organized in 7 phases.

### 6 Workflows

```
┌─────────────────────────────────────────────────────────────────┐
│                    AEO ENGINE (End-State)                        │
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐    │
│  │ WF1      │  │ WF2      │  │ WF3      │  │ WF4          │    │
│  │ Demand   │→ │ Content  │→ │ Content  │→ │ Publish &    │    │
│  │ Intel    │  │ Planning │  │ Ops &    │  │ Distribution │    │
│  │          │  │          │  │ Gen      │  │              │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘    │
│       ↑                                          │              │
│  ┌──────────┐                              ┌──────────────┐    │
│  │ WF5      │←─────────────────────────────│ WF6          │    │
│  │ Observe  │                              │ SEO → AEO    │    │
│  │ & Track  │                              │ Bridge       │    │
│  └──────────┘                              └──────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

### 7 Agent Phases

| Phase | Name | Agents | Purpose |
|-------|------|--------|---------|
| A | Demand Intelligence | A1, A2 | Discover what to write about |
| B | Content Planning | B1, B2, B3 | Define how to structure content |
| C | Content Generation | C1-C5 | Research, outline, draft, enrich, compose |
| D | Quality & Optimization | D1-D4 | Score, fact-check, SEO, extractability |
| E | Expert Review | E1, E2 | SME vetting + brand voice review |
| F | Publish & Distribute | F1-F6 | Schema, design, link, deploy, distribute |
| G | Monitor & Learn | G1, G2 | Track SOV, feed back into pipeline |

→ Full agent registry and DAG: [`agents/README.md`](./agents/README.md)

---

## Pipeline Stages (Updated)

```
STAGE 1          STAGE 2          STAGE 3           STAGE 4          STAGE 5           STAGE 6
KW & Topic  →    Content     →    Draft         →   AEO Quality →   SME / Teacher →   Publish
Understanding     Brief            Generation        Gate             Vetting           & Go-Live
(A1,A2,B1,B2)    (B3)             (C1-C5)           (D1-D4)          (E1,E2)           (F1-F6)
```

| Stage | Agents | Output | Gate |
|-------|--------|--------|------|
| 1. KW & Topic Understanding | A1, A2, B1, B2 | Topic Dossier | — |
| 2. Content Brief | B3 | Content Brief | — |
| 3. Draft Generation | C1, C2, C3, C4, C5 | Composed Draft | — |
| 4. AEO Quality Gate | D1, D2, D3, D4 | Score Card | All 5 scores ≥ 7 to pass |
| 5. SME / Teacher Vetting | E1, E2 | Approved Article | Human approval required |
| 6. Publish & Go-Live | F1, F2, F3, F4 | Live Page | Go-live checklist |
| — Distribution | F5, F6 | Multi-channel presence | — |
| — Monitoring | G1, G2 | SOV data + feedback | Feeds back to Stage 1 |

---

## Directory Structure

```
aeo/
├── README.md                              ← You are here
├── aeo-research-findings.md               # Consolidated AEO research (GEO paper, etc.)
├── workflow-architecture.md               # 6-workflow architecture reference
├── agents/                                # 21 agents + orchestrator
│   ├── README.md                          # Master registry, DAG, phase map
│   ├── _shared/                           # Shared context (all agents read)
│   │   ├── product-context.md
│   │   ├── brand-voice-guide.md
│   │   └── aeo-scoring-rubric.md
│   ├── templates/                         # Output templates
│   │   ├── topic-dossier.md
│   │   ├── content-brief.md
│   │   ├── score-card.md
│   │   └── distribution-plan.md
│   ├── O1-orchestrator/
│   ├── A1-query-intelligence/
│   ├── A2-competitive-intelligence/
│   ├── B1-intent-classifier/
│   ├── B2-ear-decomposer/
│   ├── B3-content-brief-generator/
│   ├── C1-research/
│   ├── C2-outline/
│   ├── C3-draft/
│   ├── C4-citation-enricher/
│   ├── C5-composer/
│   ├── D1-aeo-evaluator/
│   ├── D2-fact-check/
│   ├── D3-seo/
│   ├── D4-extractability-optimizer/
│   ├── E1-sme-teacher/
│   ├── E2-brand-voice-reviewer/
│   ├── F1-schema-markup/
│   ├── F2-page-designer/
│   ├── F3-internal-linking/
│   ├── F4-publisher/
│   ├── F5-distribution-strategist/
│   ├── F6-channel-adaptor/
│   ├── G1-sov-tracker/
│   └── G2-feedback-analyst/
└── (legacy folders: keywords/, strategy/, content/, vetting/, production/)
```

---

## Build Priority

1. **B3** Content Brief Generator — linchpin, all downstream depends on brief quality
2. **D1** AEO Evaluator — quality gate, calibrate with existing ~30 articles
3. **C4** Citation Enricher — highest single AEO impact lever (+41% visibility)
4. Remaining agents progressively

## Key AEO Data Points

| Factor | Impact | Source |
|--------|--------|--------|
| Quotations/citations | +41% visibility | GEO paper |
| Statistics | +33% visibility | GEO paper |
| Source citations | +28% visibility | GEO paper |
| Fluency optimization | +29% | GEO paper |
| Schema markup | 30-40% boost | Google AIO data |
| Keyword stuffing | -8% visibility | GEO paper (anti-pattern) |

## References
- [GEO Paper (arXiv:2311.09735)](https://arxiv.org/abs/2311.09735)
- `AEO_related_research_and_understanding.pdf` (internal)
- [AEO Coach Gist](https://gist.github.com/BayramAnnakov/5c04f7326b6e732a2481c2e0f93bab83)
