# AEO Workflow Architecture

> Reference document — the 6 workflows that compose the AEO engine.

## Overview: 6 Workflows

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

## WF1: Demand Intelligence
- **Purpose:** Identify WHAT to create content about
- **Input:** External demand (AI query volume) + Internal positioning (product offerings)
- **Output:** Prioritized topic list with AEO Opportunity Scores
- **Agents:** A1 (Query Intelligence), A2 (Competitive Intelligence)
- **Tools:** DataForSEO, SEMrush, FOMO, AirOps, manual AI engine querying

## WF2: Content Planning & Strategy
- **Purpose:** Define HOW each topic should be structured
- **Input:** Prioritized topics from WF1
- **Output:** Content briefs with structure, intent mapping, target attributes
- **Agents:** B1 (Intent Classifier), B2 (EAR Decomposer), B3 (Content Brief Generator)

## WF3: Content Ops & Generation
- **Purpose:** Generate, evaluate, and refine AEO-optimized content
- **Input:** Content briefs from WF2
- **Output:** Vetted, AEO-ready content
- **Agents:** C1-C5 (Generation), D1-D4 (Quality), E1-E2 (Review)
- **Status:** Building next

## WF4: Publish & Distribution
- **Purpose:** Get content live and amplify across citation surfaces
- **Input:** AEO-ready content from WF3
- **Output:** Published pages + off-site presence
- **Agents:** F1-F4 (Publish), F5-F6 (Distribute)

## WF5: Observability & SOV Tracking
- **Purpose:** Measure what's working, feed back into WF1
- **Input:** Published content URLs + target queries
- **Output:** Dashboards, alerts, optimization signals
- **Agents:** G1 (SOV Tracker), G2 (Feedback Analyst)

## WF6: SEO → AEO Bridge
- **Purpose:** Leverage existing SEO authority for AEO gains
- **Input:** Pages already ranking in SERP (resource/library pages, ADPs)
- **Output:** AEO-enhanced versions of existing high-authority pages
- **Process:** SEO Audit → AEO Layer Addition → Interlink to /learn/ Hubs

## End-to-End Pipeline (WF3 Detail)

```
STAGE 1          STAGE 2          STAGE 3           STAGE 4          STAGE 5           STAGE 6
KW & Topic  →    Content     →    Draft         →   AEO Quality →   SME / Teacher →   Publish
Understanding     Brief            Generation        Gate             Vetting           & Go-Live
                  Creation                           (LLM Eval)       (Human Eval)
```

### Revision Loops
- Stage 4 fail (score < 7) → back to Stage 3
- Stage 5 fail (SME rejects) → back to Stage 3
- Stage 5 feedback → LLM Evaluator training data
- WF5 post-publish → Stage 1 (new topic dossier if gaps found)
- Max 2 automated revision loops before human escalation
