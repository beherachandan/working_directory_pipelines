# AEO Scoring Rubric
_Version: 1.2 — 2026-04-27_
_Changelog: aeo/context/rubric-changelog.md_

> **Single source of truth for all scoring agents (D1, D2, D3).**
> No scoring dimension logic lives inside agent files. Agents handle routing, input, output formatting only.
> Any change to this file = version bump + changelog entry + calibration rerun on ≥5 URLs.

---

## Philosophy

**Citations × Trust = Share of Voice.**

AI systems cite passages that are:
- Directly answerable (answer-first, not buried)
- Self-contained (extractable without surrounding context)
- Fact-dense (specific numbers, named sources, dates)
- Structurally clean (parseable heading hierarchy, short paragraphs)
- Authoritative (original data, expert attribution, first-party signals)

Traditional SEO optimises for *ranking*. AEO optimises for *citation* — being the source an AI chooses to quote. These overlap but are not the same. A page can rank #1 and never be cited. A page can be cited constantly from position #8.

---

## Scoring Architecture

### Which dimensions apply where

| Dimension | D1 Pipeline Gate | D2 URL Evaluator | D3 Competitor Gap |
|---|---|---|---|
| 1. QAPE / Answer Structure | ✅ | ✅ | ✅ |
| 2. EAR Coverage | ✅ pipeline only | ❌ no brief available | ❌ |
| 3. Passage Self-Containment | ✅ | ✅ | ✅ |
| 4. Structural Readability | ✅ | ✅ | ✅ |
| 5. Statistical Density | ✅ | ✅ | ✅ |
| 6. Uniqueness & Original Data | ✅ | ✅ | ✅ |
| 7. Trust & Authority | ✅ | ✅ | ✅ |
| 8. Intent Match | ✅ | ✅ | ✅ |
| 9. Platform Specificity | ❌ pipeline N/A | ✅ | ✅ |

### Composite weights by agent

**D1 (9 dimensions, EAR included):**
| Dimension | Weight |
|---|---|
| QAPE / Answer Structure | 17% |
| EAR Coverage | 18% |
| Passage Self-Containment | 12% |
| Structural Readability | 8% |
| Statistical Density | 15% |
| Uniqueness & Original Data | 14% |
| Trust & Authority | 12% |
| Intent Match | 4% |
| _(Platform Specificity excluded — pipeline context)_ | — |

**D2 / D3 (8 dimensions, EAR excluded):**
| Dimension | Weight |
|---|---|
| QAPE / Answer Structure | 18% |
| Passage Self-Containment | 14% |
| Structural Readability | 9% |
| Statistical Density | 17% |
| Uniqueness & Original Data | 16% |
| Trust & Authority | 14% |
| Intent Match | 7% |
| Platform Specificity | 5% |

---

## Step 0: Structural Classification (Required Before Scoring Any Dimension)

Before scoring any dimension, read the full article and produce this classification block. Include it verbatim at the top of the scorecard output — before any dimension scores appear.

```
STRUCTURAL CLASSIFICATION
Article type: [Informational / Comparison / How-to / Recommendation]
H3 pattern:   [Query-driven / Attribute-driven / Process-driven / Mixed]
Evidence:     [1-2 sentences explaining what in the article signals this pattern]
QAPE path:    [Path A / Path B / Path C — see Dim 1]
```

**Classification guidance:**
- **Query-driven:** H3s are discrete answerable questions ("What is X?", "How does Y work?") — each stands alone as a query
- **Attribute-driven:** H3s are named properties of a central concept ("It's Ongoing", "It's Low-Stakes") — all sit under a single definition H2, describing sub-features of one thing
- **Process-driven:** H3s are sequential steps toward an outcome ("Step 1: Define the goal", "Step 2: Select a format")
- **Mixed:** article uses more than one pattern in different sections — note which sections use which pattern, apply appropriate path per section

> **Important:** The Step 0 output is auditable — it appears before any scores. A wrong classification degrades fix instruction quality but does NOT change the extractability-test score (see Dim 1). If the classification looks wrong, flag it before reading dimension scores.

---

## Dimension Definitions

---

### Dimension 1: QAPE / Answer Structure
_Goal: every section is independently extractable by an AI system._

QAPE (Question → Answer → Proof → Expansion) describes the ideal extractable pattern, but the path to achieving it depends on the article's H3 structure type. Use the Step 0 classification to select the right path. Then apply the extractability test to determine the score.

---

#### QAPE Paths (select based on Step 0 classification)

**Path A — Query-driven** (H3s are discrete questions)
Each H3 section should have:
- Explicit question heading ("What is X?", "Why does Y matter?", "How does Z work?")
- Direct answer in first 1–2 sentences using definition pattern ("X is…", "X refers to…")
- Concrete proof element in first 3 sentences: stat with source OR named expert quote
- Expansion with depth/context

**Path B — Attribute-driven** (H3s are properties of a defined concept)
Each H3 section should have:
- Attribute label in heading is fine — no question required
- Opening sentence names the attribute AND makes a direct claim about it ("Formative assessment is intentionally low-stakes — meaning…")
- Proof element in first 3 sentences: stat with source OR named expert quote
- Expansion with depth/context

**Path C — Process-driven** (H3s are sequential steps)
Each H3 section should have:
- Step clearly named (and numbered if sequence matters)
- Outcome of the step stated explicitly ("This allows teachers to…", "The result is…")
- At least one specific example or data point
- Transition only if it does not create context dependency on the prior step

**Mixed articles:** Apply the path matching each section's H3 pattern. Note in the scorecard which path was applied per section.

---

#### Extractability Test (determines the score)

After applying path criteria, run this test on each H2/H3 block:

> _"If this passage were shown to an AI system with no surrounding context — does it contain (1) a named subject, (2) a direct claim about that subject, and (3) at least one specific fact, stat, or named entity?"_

- **Yes to all 3 → extractable ✅**
- **No to any → not extractable ❌**

**Score = % of passages passing the extractability test.** Fix instructions reference the specific path criteria the passage failed — but the score is determined by extractability, not path compliance. This means a misclassification at Step 0 degrades fix quality but cannot corrupt the score.

---

#### Score Table

| Score | Criteria |
|---|---|
| 9-10 | 90-100% of passages pass extractability test. All have named subject, direct claim, specific fact. Proof element present in first 3 sentences. |
| 7-8 | 70-89% pass. Proof occasionally missing or anecdotal. Subject named but claim sometimes buried. |
| 5-6 | 50-69% pass. Mixed extractable/non-extractable. Some buried claims. Fact-free sections present. |
| 3-4 | 30-49% pass. Narrative-driven. Claims buried mid-paragraph. Few specific facts across sections. |
| 0-2 | <30% pass. No direct claims. No specific facts. Entirely conversational or preamble-heavy. |

---

#### Worked Examples

**Path A — Query-driven (high citability):**
```
## What is retrieval practice?
Retrieval practice is a learning strategy where students actively recall
information from memory rather than reviewing it passively. Research shows
retrieval-based study produces 50% better retention than review-based study
after one week (Karpicke & Blunt, 2011). Teachers implement it through
low-stakes quizzes, brain dumps, and flashcard review...
```
Named subject ✅ | Direct claim ✅ | Named stat with source ✅ → Extractable ✅

**Path B — Attribute-driven (high citability):**
```
### It's Low-Stakes for Students
Formative assessment is intentionally low-stakes — it is not graded and
carries no performance consequences. Research shows low-stakes conditions
reduce test anxiety by 23% compared to high-stakes formats (Adesope et al.,
2017), producing more honest responses and clearer signals of what students
actually understand...
```
Named subject ✅ | Direct claim ✅ | Named stat with source ✅ → Extractable ✅

**Path B — Attribute-driven (low citability):**
```
### It's Low Pressure for Students
Because formative assessments are not designed to be graded or high-stakes,
they create space for students to take risks. Mistakes become information,
not penalties...
```
Named subject ✅ | Direct claim ✅ | Specific fact ❌ (no stat, no named source) → Not extractable ❌

**Path A — Query-driven (low citability):**
```
## Understanding How Students Learn
There's been a lot of discussion in education circles about how students
actually retain information. The research community has been studying this
for decades...
```
Named subject ❌ | Direct claim ❌ | Specific fact ❌ → Not extractable ❌

---

### Dimension 2: EAR Coverage
_Entity → Attribute → Relationship coverage against brief_
**D1 only. Skip for D2/D3 — no brief available.**

| Score | Formula |
|---|---|
| All scores | `(attributes covered / total target attributes from B2 EAR map) × 10` |
| 9-10 | ≥90% of must-cover attributes present with depth |
| 7-8 | 70-89% coverage; all critical attributes present |
| 5-6 | 50-69%; some critical attributes missing or thin |
| 3-4 | 30-49%; significant topic gaps |
| 0-2 | <30% coverage |

---

### Dimension 3: Passage Self-Containment
_Can each passage be extracted and understood in isolation?_

AI systems pull passages verbatim. A passage that relies on surrounding context for meaning cannot be cleanly cited.

**Per-passage checklist (score each H2/H3 block):**
1. Subject named explicitly (not "it", "this", "they" — full noun)
2. Passage can be understood reading ONLY this passage
3. Contains at least one specific fact, stat, or named entity
4. Length 50-200 words (optimal AI extraction window)
5. Does not open with a conjunction implying prior context ("However,", "But,", "As mentioned,")

| Score | Criteria |
|---|---|
| 9-10 | 80%+ of content blocks pass all 5 checklist items |
| 7-8 | 60-79% pass. Most name their subject. Occasional pronoun dependency. |
| 5-6 | 40-59% pass. Mixed explicit/pronoun subjects. Many passages need surrounding text. |
| 3-4 | 20-39% pass. Heavy pronoun use. Continuous narrative structure. |
| 0-2 | <20% pass. Content only makes sense read end-to-end. |

---

### Dimension 4: Structural Readability
_Can AI systems parse and segment the content reliably?_

| Score | Criteria |
|---|---|
| 9-10 | Clean H1→H2→H3 hierarchy (no skipped levels). Question-based headings for informational content. Paragraphs 2-4 sentences. Tables used for any 3+ item comparison. Ordered lists for processes, unordered for features. Key terms bolded on first use. |
| 7-8 | Good hierarchy, minor skips. Some question headings. Mostly short paragraphs. Some tables/lists. |
| 5-6 | Heading hierarchy present but inconsistent. Few question headings. Mix of short and long paragraphs. |
| 3-4 | Minimal heading structure. Long paragraphs dominate. Rare tables/lists. |
| 0-2 | No heading structure or broken hierarchy. Wall-of-text. No tables or lists. |

**Specific checks:**
- Paragraphs: flag any block >4 sentences
- Tables: present for comparison content? (if applicable)
- FAQ section: present? (strong Perplexity citability signal)
- Key terms bolded on first use: Y/N

---

### Dimension 5: Statistical Density
_Are claims backed by specific, verifiable data points?_

AI systems strongly prefer fact-dense passages. Vague quantifiers ("many", "most", "several") are not statistics.

**Threshold: 5+ named statistics per 500 words = top score.**

| Score | Criteria |
|---|---|
| 9-10 | 5+ specific statistics per 500 words. All claims backed by named source or date. Exact numbers (not ranges unless ranges are the finding). Named studies. |
| 7-8 | 3-4 statistics per 500 words. Most claims sourced. Mostly specific. |
| 5-6 | 1-2 statistics per 500 words. Some sourced. Mix of specific and vague. |
| 3-4 | <1 statistic per 500 words. Few sourced claims. Predominantly vague quantifiers. |
| 0-2 | No statistics. No sourced claims. All quantifiers vague. |

**Counts as a statistic:**
- Specific percentages with source: "73% of teachers report X (Smith, 2024)"
- Dollar/time amounts: "implementation takes 6-8 weeks on average"
- Named study results: "According to the 2025 HubSpot State of Marketing Report..."
- Comparison data: "40% faster than the industry average"
- Specific counts: "used by 340,000+ teachers"

**Does NOT count:**
- "Many companies use..." / "A significant percentage..." / "Studies show..." / "Experts agree..."

---

### Dimension 6: Uniqueness & Original Data
_Does this content provide something AI cannot find elsewhere?_

The single most-neglected dimension. Derivative content — however well-structured — competes with hundreds of similar pages on authority alone. Original data creates a citation dependency: AI *must* cite you because no one else has the data.

| Score | Criteria |
|---|---|
| 9-10 | First-party research or proprietary data. Original surveys, internal usage data, custom datasets. Clear methodology. Something no other page has. |
| 7-8 | Some original insights or unique analysis of existing data. Distinct perspective with original examples or frameworks. |
| 5-6 | Mostly synthesises existing info but adds unique commentary, case studies, or examples with specific outcomes. |
| 3-4 | Largely derivative. Restates common knowledge with minimal original contribution. |
| 0-2 | Entirely derivative. All information available (often verbatim) on higher-authority sources. |

**High-uniqueness signals:**
- "Our analysis of [N] classrooms found..."
- "We surveyed [N] teachers and found..."
- "Based on [N] student sessions on Wayground..."
- Custom charts/visualisations from original data
- Case studies with specific named outcomes and metrics
- Original frameworks or taxonomies (not restatements of existing ones)

**For Wayground specifically:** Product usage data is the highest-leverage uniqueness source. Even one stat from platform data ("X% of teachers using Wayground's quiz tool report Y") is a genuine original data point that competitors cannot replicate.

---

### Dimension 7: Trust & Authority
_First-hand signals, expert attribution, and source credibility_

Separate from statistical density — this is about *who* is speaking and *how* authoritative the signals are.

| Score | Criteria |
|---|---|
| 9-10 | Named author with credentials/byline. 3+ expert quotes with full attribution (name, title, institution). First-person signals ("we tested", "based on our analysis"). External authoritative source citations. No unresolved placeholders. |
| 7-8 | Some author signal. 2 expert quotes. Some first-person or brand signals. Clean citations. |
| 5-6 | Minimal author signal. 1 quote or citations without expert attribution. Some trust signals. |
| 3-4 | No author. Claims without backing. No expert attribution. |
| 0-2 | No trust signals at all. Anonymous, uncited, no authority markers. |

**For D1 pipeline specifically:** Also flag any unresolved `[HUMAN REVIEW NEEDED]` or `[CITATION NEEDED]` placeholders — each counts as -0.5 from raw score, minimum 0.

---

### Dimension 8: Intent Match
_Does content format match what the query is looking for?_

| Intent Type | Required Format Elements |
|---|---|
| **Informational** ("What is X?") | Definition in first paragraph; expansion with depth; FAQ section |
| **Comparison** ("X vs Y") | Comparison table with criteria rows + "Best For" row; bottom-line recommendation |
| **How-to** ("How to X") | Numbered steps; bolded step name; outcome stated per step |
| **Recommendation** ("Best X for Y") | Ranked list; criteria explained; top pick highlighted |
| **Transactional** | CTA placement; pricing/feature clarity; trust signals prominent |

| Score | Criteria |
|---|---|
| 9-10 | All required format elements for intent type present and well-executed |
| 7-8 | Correct format, 1 element missing |
| 5-6 | Partially correct; key element missing (e.g. comparison without table) |
| 3-4 | Wrong format for intent (e.g. prose essay for a comparison query) |
| 0-2 | No format consideration for intent |

---

### Dimension 9: Platform Specificity
_D2 and D3 only. How well is this content optimised for each AI platform's citation preferences?_

Different AI systems have different citation behaviours. A page optimised generically may underperform on specific platforms.

| Platform | Citation Preference | Key Signal |
|---|---|---|
| **Perplexity** | Fact-dense passages; 4-8 sources per response; values recency | Statistical density is highest predictor; FAQ schema critical |
| **ChatGPT (Search)** | Explicit definitions; named sources; recent dates; 2-4 sources per response | Content-answer fit ~55% of citation likelihood |
| **Google AIO** | Concise answer blocks 40-60 words; content already ranking top 10 organic | Schema markup gives 30-40% visibility boost |
| **Claude** | Well-structured, comprehensive; values nuance and accuracy over brevity | Extremely selective; self-containment matters most |
| **Copilot (Bing)** | Similar to Google AIO; high-authority domains; page load <2s | Domain authority and page speed |

**Scoring:**

| Score | Criteria |
|---|---|
| 9-10 | Optimised for ≥3 platforms: answer blocks 40-60 words for AIO, stat-dense for Perplexity, definition-first for ChatGPT, FAQ schema present |
| 7-8 | Naturally serves 2 platforms well without explicit optimisation |
| 5-6 | Serves 1 platform well; others would struggle to extract |
| 3-4 | Generic content; no platform-specific signals |
| 0-2 | Actively mismatched (e.g. wall of text, no definitions, no stats) |

---

## Gate Logic (D1 Pipeline Only)

```
All scored dimensions ≥ 7 → PASS → route to human review
Any dimension < 7      → REVISE → route back to C3 with specific feedback
After 2 revision loops → ESCALATE → human review regardless of score
```

**D2/D3 have no gate** — they produce scores and recommendations, not pass/fail decisions.

---

## Calibration & Validation

> Full drift prevention protocol: `aeo/context/rubric-drift-prevention.md`

### Empirical threshold (to be established)
The pass threshold of ≥7 (D1) and equivalent on D2's 0-100 scale is currently based on rubric logic, not empirical data. Calibration corpus will establish the score range that predicts actual AI citation.

**Calibration corpus:** `memory/research/calibration-corpus.md` (15-20 URLs, 3 tiers + worst 5-10)
**Scoring run results:** `memory/research/scoring-runs/`
**Ground truth checks:** `memory/research/ground-truth-checks/`
**AEO research:** `memory/research/aeo-research/`

### Three drift types and mitigations

| Drift Type | Prevention |
|---|---|
| **Rubric drift** — scoring logic fragments into agent files | Single source of truth here; agents are readers only; skill-creator audits periodically |
| **Signal drift** — scores stop predicting citation | Monthly ground truth cron; major model release triggers full corpus rerun |
| **Knowledge drift** — research basis ages | Quarterly research scan of memory/research/aeo-research/ |

### Rubric update process
Any change follows this exact sequence:
```
1. Edit this file
2. Bump version (minor: v1.x → v1.x+1 | structural: vX → vX+1.0)
3. Log in rubric-changelog.md (what, why, date)
4. Rerun calibration corpus on ≥5 URLs
5. Capture score delta
6. Post validation delta to Slack #way-mark
7. If delta >1.0 composite on any URL → flag for human review before deploying
```

---

## Research Basis

| Finding | Source | Incorporated in |
|---|---|---|
| Quotations +41% AI visibility | arXiv:2311.09735 (Princeton/Georgia Tech/IIT Delhi 2024) | Dim 7: Trust & Authority |
| Statistics +33% AI visibility | arXiv:2311.09735 | Dim 5: Statistical Density |
| Source citations +28% AI visibility | arXiv:2311.09735 | Dim 7: Trust & Authority |
| Fluency optimisation +30% | arXiv:2311.09735 | Dim 4: Structural Readability |
| Optimal AI citation passage: 134-167 words | Bortolato 2025 | Dim 3: Passage Self-Containment |
| Definition patterns increase citation 2.1x | Georgia Tech 2024 | Dim 1: QAPE |
| Statistics in passages increase citation +40% | Princeton GEO study 2024 | Dim 5: Statistical Density |
| Expert quotations increase citation +115% (some categories) | IIT Delhi 2024 | Dim 7: Trust & Authority |
| Brand mentions vs backlinks: 3x stronger correlation for AI | Ahrefs Dec 2025 | Dim 7: Trust & Authority |
| AI-referred sessions growth +527% (Jan-May 2025) | SparkToro | Context |
| AI traffic conversion vs organic: 4.4x higher | Industry data | Context |

---

## Anti-patterns (penalise)

| Pattern | Effect | Dimension |
|---|---|---|
| Keyword stuffing | -8% AI visibility | Dim 1 |
| Pronoun-heavy passages ("it", "they", "this" without referent) | Extraction failure | Dim 3 |
| Vague quantifiers ("many", "most", "several") without data | Zero citability weight | Dim 5 |
| Anonymous content (no author, no brand signal) | Trust collapse | Dim 7 |
| Wall-of-text paragraphs >6 sentences | Parser failure | Dim 4 |
| Derivative synthesis with no original angle | Citation competition with higher-authority pages | Dim 6 |
