# Rubric Changelog

_Every change to aeo-scoring-rubric.md is logged here._
_Format: version | date | what changed | why | validation run_

---

## v1.0 — 2026-04-21

**What changed:** Initial release. Merged two prior rubrics:
- D1 AEO Evaluator (5 dimensions: QAPE, EAR, Extractability, Trust, Intent)
- geo-citability from `geo-seo-claude` reference repo (5 dimensions: Answer Block Quality, Passage Self-Containment, Structural Readability, Statistical Density, Uniqueness)

**Resulting architecture:**
- 9 dimensions total
- D1 uses all 9 (EAR included — pipeline has brief)
- D2/D3 use 8 (EAR excluded — no brief available for ad-hoc URL evaluation)
- Separate weight tables for D1 vs D2/D3

**Key additions vs prior D1:**
- Dimension 3 (Passage Self-Containment) — new, from geo-citability. Per-passage 5-point checklist.
- Dimension 5 (Statistical Density) — split out from Trust & Authority. Threshold: 5+/500 words.
- Dimension 6 (Uniqueness & Original Data) — new, from geo-citability. Highest-leverage gap identified in first calibration run.
- Dimension 9 (Platform Specificity) — new. Per-platform citation preferences (Perplexity, ChatGPT, Google AIO, Claude, Copilot).
- Research basis table added with 10 source citations.
- Anti-patterns table added.

**Why:** First calibration run on `wayground.com/learn/education-assessment/retrieval-practice` showed D1 passed (7.1/10) while geo-citability scored 62/100. Primary gap: Uniqueness dimension not measured in old D1. Rubric restructured to surface this.

**Validation run:** Single URL (retrieval practice article). Calibration corpus not yet built — empirical threshold not yet established. Threshold of ≥7 for D1 gate is rubric-logic-based, not empirically validated. See `memory/research/calibration-corpus.md` (to be created in Step 2).

---

_Next review trigger: Gemini calibration runs + 90-day ground truth cron result._

---

## v1.2 — 2026-04-27

**What changed:** QAPE / Dimension 1 redesigned from mechanical checklist to context-aware path system.

**Root cause:** Scoring formative-assessments article revealed that the prior Dim 1 definition required "explicit question heading" for all H3s, regardless of article structure type. This caused incorrect fix instructions on attribute-driven articles (where H3s are named properties of a concept, not discrete answerable questions). Converting attribute H3s to questions produced editorially wrong output.

**Changes made:**
1. **Added Step 0: Structural Classification** — mandatory pre-scoring step. Agent reads full article, classifies H3 pattern (Query-driven / Attribute-driven / Process-driven / Mixed), selects QAPE path. Output included verbatim in scorecard before any dimension scores — auditable by human reviewer.
2. **Dim 1 redesigned around 3 QAPE paths:**
   - Path A (Query-driven): question heading + answer-first + proof
   - Path B (Attribute-driven): attribute label OK, opening sentence must name attribute + make direct claim + include proof
   - Path C (Process-driven): step named/numbered, outcome stated, example/data point present
3. **Extractability test added as score determinant** — overrides path ambiguity. Score = % of passages passing: (1) named subject, (2) direct claim, (3) specific fact/stat/entity. Classification mistake degrades fix quality but cannot corrupt the score.
4. **Worked examples added for all 3 paths** — high and low citability example per path for consistent agent application.

**Surface area updated:** aeo-scoring-rubric.md, D1 SKILL.md, D2 SKILL.md, D3 SKILL.md. All version strings bumped to v1.2.

**Validation:** No calibration rerun yet. Change is structural (scoring logic), not weight-based — composite scores on prior corpus may shift slightly on articles with attribute-driven structure. Flag for rerun on next calibration cycle.

**Why no calibration rerun gating this:** The extractability test is a refinement of the same underlying signal (can AI extract a clean answer?), not a new dimension. Risk of score corruption is low. Human flagged and approved before applying.

---

## v1.1 — 2026-04-27

**What changed:** Rubric weight rebalancing based on empirical GEO calibration delta analysis.

**Calibration basis:**
- 5 topics calibrated on ChatGPT (formative assessment, retrieval practice, exit tickets, growth mindset, differentiated instruction)
- 12 runs each (4 variations × 3 runs)
- 30 URLs in corpus: 10 GEO_GOLD (cited ≥43% of runs) + 20 non-cited
- Delta = gold avg score − non-gold avg score per dimension

**Delta results (most → least predictive):**
| Dimension | Gold avg | Rest avg | Δ |
|---|---|---|---|
| Statistical Density | 5.10 | 3.55 | +1.55 |
| Uniqueness & Original Data | 6.20 | 4.75 | +1.45 |
| Trust & Authority | 7.30 | 6.05 | +1.25 |
| Passage Self-Containment | 6.60 | 5.45 | +1.15 |
| Intent Match | 6.90 | 5.95 | +0.95 |
| QAPE / Answer Structure | 6.30 | 5.60 | +0.70 |
| Structural Readability | 7.00 | 6.40 | +0.60 |
| Platform Specificity | 5.30 | 4.70 | +0.60 |

**Weight changes (D2/D3):**
| Dimension | v1.0 | v1.1 |
|---|---|---|
| QAPE / Answer Structure | 22% | 18% |
| Passage Self-Containment | 18% | 14% |
| Structural Readability | 12% | 9% |
| Statistical Density | 12% | 17% |
| Uniqueness & Original Data | 12% | 16% |
| Trust & Authority | 12% | 14% |
| Intent Match | 7% | 7% |
| Platform Specificity | 5% | 5% |

**Rationale:** Stats density (+1.55) and uniqueness (+1.45) are the most predictive dimensions — AI systems consistently cite sources with original data and specific facts over well-structured-but-generic content. Structural readability has the smallest delta (+0.60) — it’s a prerequisite (must be readable) but doesn’t differentiate cited from non-cited URLs once that threshold is met. QAPE weight reduced because hub pages with low QAPE (3.4) still get cited 42%+ purely on domain authority.

**Caveats:**
- ChatGPT only (Gemini runs still pending — quota limited)
- 10 GEO_GOLD URLs is a reasonable but not large corpus
- Structural Readability floor set at 9% (algorithm suggested 6%) — judgment call: extraction requires structure as prerequisite

**Validation:** Calibration corpus rerun needed — run D2 on same 18 URLs with v1.1 weights to confirm score delta is not disruptive (target: <1.0 composite shift on any URL).

**Next review trigger:** Gemini calibration runs + 90-day ground truth cron result.
