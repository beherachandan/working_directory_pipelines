# AEO Content Engine — Agent Registry

> Master reference for the 21-agent AEO pipeline + Orchestrator.
> Core formula: **Citations × Trust = Share of Voice (SOV)**

## Architecture Overview

```
PHASE A          PHASE B        PHASE C          PHASE D           PHASE E         PHASE F         PHASE G
Demand      →    Content   →    Content     →    Quality &    →    Expert    →     Publish &  →    Monitor &
Intelligence     Planning       Generation       Optimization      Review          Distribute      Learn

A1 Query Intel   B1 Intent      C1 Research      D1 AEO Eval      E1 SME/         F1 Schema       G1 SOV
A2 Competitive   Classifier     C2 Outline       D2 Fact Check    Teacher         F2 Page         Tracker
   Intel         B2 EAR         C3 Draft         D3 SEO           E2 Brand        Designer        G2 Feedback
                 Decomposer     C4 Citation      D4 Extract-      Voice           F3 Interlink    Analyst
                 B3 Brief       Enricher         ability          Reviewer        F4 Publisher
                 Generator      C5 Composer      Optimizer                        F5 Distribution
                                                                                  Strategist
                                                                                  F6 Channel
                                                                                  Adaptor
```

**O1 Orchestrator** sits above all phases, managing the DAG and coordinating handoffs.

## Agent Registry

| # | Agent | Phase | Folder | Type | Core Responsibility |
|---|-------|-------|--------|------|-------------------|
| O1 | Orchestrator | All | `O1-orchestrator/` | Coordination | DAG management, state, revision loops |
| A1 | Query Intelligence | A: Demand Intel | `A1-query-intelligence/` | Discovery | Question mining, AEO opportunity scoring |
| A2 | Competitive Intelligence | A: Demand Intel | `A2-competitive-intelligence/` | Discovery | Citation audit, source gap analysis |
| B1 | Intent Classifier | B: Planning | `B1-intent-classifier/` | Planning | Query intent → content format mapping |
| B2 | EAR Decomposer | B: Planning | `B2-ear-decomposer/` | Planning | Primary Q → sub-questions/attributes |
| B3 | Content Brief Generator | B: Planning | `B3-content-brief-generator/` | Planning | QAPE skeleton, linking plan, requirements |
| C1 | Research | C: Generation | `C1-research/` | Generation | Facts, stats, quotes, sources |
| C2 | Outline | C: Generation | `C2-outline/` | Generation | Article structure from brief |
| C3 | Draft | C: Generation | `C3-draft/` | Generation | Full article writing |
| C4 | Citation Enricher | C: Generation | `C4-citation-enricher/` | Generation | Stats/quotes/citation injection (+41% impact) |
| C5 | Composer | C: Generation | `C5-composer/` | Generation | Merge outputs into cohesive draft |
| D1 | AEO Evaluator | D: Quality | `D1-aeo-evaluator/` | Evaluation | 5-dimension scoring + quality gate |
| D2 | Fact Check | D: Quality | `D2-fact-check/` | Evaluation | Claim/stat/source verification |
| D3 | SEO | D: Quality | `D3-seo/` | Evaluation | Traditional on-page SEO optimization |
| D4 | Extractability Optimizer | D: Quality | `D4-extractability-optimizer/` | Optimization | AI-extraction-ready formatting |
| E1 | SME / Teacher | E: Review | `E1-sme-teacher/` | Human Review | Pedagogical accuracy (human gate) |
| E2 | Brand Voice Reviewer | E: Review | `E2-brand-voice-reviewer/` | Review | WG brand alignment, educator tone |
| F1 | Schema Markup | F: Publish | `F1-schema-markup/` | Technical | JSON-LD structured data generation |
| F2 | Page Designer | F: Publish | `F2-page-designer/` | Design | Visual layout, /learn/ page template |
| F3 | Internal Linking | F: Publish | `F3-internal-linking/` | Technical | Knowledge graph connections |
| F4 | Publisher | F: Publish | `F4-publisher/` | Technical | CMS deploy, sitemap, indexing, bot access |
| F5 | Distribution Strategist | F: Distribute | `F5-distribution-strategist/` | Strategy | Channel selection & prioritization |
| F6 | Channel Adaptor | F: Distribute | `F6-channel-adaptor/` | Generation | Repurpose for Reddit/YouTube/Medium/etc |
| G1 | SOV Tracker | G: Monitor | `G1-sov-tracker/` | Monitoring | AI engine citation monitoring |
| G2 | Feedback Analyst | G: Monitor | `G2-feedback-analyst/` | Analysis | Learning loop, pipeline improvement |

## Execution DAG

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

### Parallel Execution Groups
- **Phase D:** D1, D2, D3, D4 run in parallel
- **Phase E:** E1, E2 run in parallel
- **Phase F (early):** F1, F2 run in parallel
- All other agents run sequentially

### Revision Loops
- D1 fail (any score < 7) → back to C3 (Draft)
- E1/E2 fail → back to C3 (Draft) with expert feedback
- Max 2 automated revision loops before human escalation
- E1 feedback → feeds into D1 evaluator training (continuous improvement)
- G2 findings → feed back to A1 (new topic opportunities)

## Shared Resources
- `_shared/product-context.md` — WG product context (all agents read)
- `_shared/brand-voice-guide.md` — Tone, terminology, rebrand rules
- `_shared/aeo-scoring-rubric.md` — 5-dimension evaluation criteria

## Templates
- `templates/topic-dossier.md` — Stage 1 output (A1+A2+B1+B2)
- `templates/content-brief.md` — Stage 2 output (B3)
- `templates/score-card.md` — Stage 4 output (D1)
- `templates/distribution-plan.md` — Stage F5 output (F5)

## Pipeline Stages → Agent Mapping

| Stage | Name | Agents | Output |
|-------|------|--------|--------|
| 1 | KW & Topic Understanding | A1, A2, B1, B2 | Topic Dossier |
| 2 | Content Brief Creation | B3 | Content Brief |
| 3 | Draft Generation | C1, C2, C3, C4, C5 | Composed Draft |
| 4 | AEO Quality Gate | D1, D2, D3, D4 | Score Card (pass/revise) |
| 5 | SME / Teacher Vetting | E1, E2 | Approved Article |
| 6 | Publish & Go-Live | F1, F2, F3, F4 | Live Page |
| — | Distribution | F5, F6 | Channel-adapted content |
| — | Monitoring | G1, G2 | SOV data + pipeline feedback |

## Build Priority
1. **B3** Content Brief Generator (linchpin — all downstream depends on briefs)
2. **D1** AEO Evaluator (quality gate — calibrate with existing ~30 articles)
3. **C4** Citation Enricher (highest single AEO impact lever: +41%)
4. Remaining agents progressively

## Key Data Points
- Quotations: +41% visibility (GEO paper)
- Statistics: +33% visibility
- Source citations: +28% visibility
- Fluency optimization: +29%
- Keyword stuffing: -8% visibility
- Schema markup: 30-40% AI visibility boost (Google AIO)
- Content-answer fit: 55% of ChatGPT citation likelihood
- 30-day freshness: 3.2x more ChatGPT citations

## References
- [GEO Paper (arXiv:2311.09735)](https://arxiv.org/abs/2311.09735)
- `_shared/aeo-scoring-rubric.md`
- `../../AEO_related_research_and_understanding.pdf`
