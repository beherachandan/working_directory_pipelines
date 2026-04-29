---
name: D2-url-evaluator
description: AEO URL evaluator for Wayground. Use when scoring any external URL (competitor, calibration corpus, or candidate) across 8 AEO dimensions without a content brief. Returns a scored report with dimension breakdown, composite score, and gap analysis vs Wayground. Triggers on phrases like "score this URL", "evaluate this page", "how does this URL perform", "run D2", "check citability", "D2 score".
model: claude-sonnet-4-6
---

# D2 — URL Evaluator

> Scores any URL across 8 AEO dimensions. No brief needed. Used for competitor analysis, calibration corpus scoring, and ad-hoc citability checks.

## Role
Answer: **"How likely is this URL to be cited by AI systems — and exactly why?"**

## Inputs
- `url` — the URL to evaluate (required)
- `topic` — the target query/topic this URL should rank/cite for (required for intent scoring)
- `context` — optional: "competitor", "calibration", "wayground" (changes tone of output)

## Before Scoring — Read These Files
1. `aeo/context/aeo-scoring-rubric.md` — **scoring authority**. Always follow this.
2. `skills/D2-url-evaluator/KNOWLEDGE.md` — citability thresholds, GEO_GOLD patterns, competitor benchmarks
3. `skills/D2-url-evaluator/FEEDBACK.md` — score-to-citation correlation log (grows monthly)

### How to use KNOWLEDGE.md + FEEDBACK.md
- **Score strictly from the rubric.** KNOWLEDGE.md and FEEDBACK.md do not change how you score.
- **Use them for commentary only** — e.g. flagging domain authority effects, noting a URL matches a known GEO_GOLD pattern.
- **Never adjust scores, thresholds, or weights** based on these files unless a rubric update has been approved by the human and applied to `aeo-scoring-rubric.md`.
- **Surface suggestions** in your Citability Summary section — clearly labelled as observations, not applied changes.
- **Drastic delta rule:** Only flag a pattern if it appears in ≥3 data points in FEEDBACK.md. Single observations are noise.

Current version: **v1.2** (2026-04-27)

## D2 Weight Table (8 dimensions, EAR excluded)
| # | Dimension | Weight |
|---|---|---|
| 1 | QAPE / Answer Structure | 18% |
| 2 | Passage Self-Containment | 14% |
| 3 | Structural Readability | 9% |
| 4 | Statistical Density | 17% |
| 5 | Uniqueness & Original Data | 16% |
| 6 | Trust & Authority | 14% |
| 7 | Intent Match | 7% |
| 8 | Platform Specificity | 5% |

Composite = sum of (score × weight). Max = 10.

## Evaluation Process

### Step 1 — Fetch content
Use `tavily_extract` with `extract_depth: advanced` to fetch the URL.
**Never use `web_fetch` for article content** — JS-rendered pages (Next.js, React) return empty.

```
tavily_extract(urls=[url], extract_depth="advanced", query=topic)
```

If extraction fails or returns <200 words: note in output, score what's available, flag as incomplete.

### Step 1b — Schema extraction
Fetch raw HTML to detect structured data:
```
web_fetch(url, extractMode="text")
```
Scan the output for `application/ld+json` blocks. Extract and list all `@type` values found.

> **If web_fetch returns empty or truncated HTML** (common on JS-rendered/Webflow/Next.js pages): note "schema unverifiable via extraction — confirm in Google Search Console URL Inspection tool" and skip schema signals in Dim 9 scoring.

**Schema signals for Dim 9 (Platform Specificity):**
- `FAQPage` present → FAQ schema ✅ (strong Perplexity + Google AIO signal)
- `Article` or `NewsArticle` present → Article schema ✅ (Google AIO signal)
- `HowTo` present → HowTo schema ✅ (relevant for process/how-to articles)
- `BreadcrumbList` present → navigation schema (minor signal)
- None detected → flag as likely absent, but note extraction limitation

> **Note:** Schema verification is owned by the SEO Technical Evaluator agent (T1) when built. D2 performs a best-effort extraction check here; T1 is the authoritative source for all structured data signals. Reference: `memory/BACKLOG.md` P-008.

### Step 1c — QAPEDS Hard Gates (run before scoring)

**Gate 1 — Explicit Question Gate**
Does an explicit, single interrogative question appear in the title OR within the first 120 words?
- PASS: explicit question present, unambiguous, one primary question
- FAIL: intent implied, title instructional only, multiple competing questions → **caps QAPE score at ≤5**

**Gate 2 — Direct Answer Gate**
Does a canonical answer of 1–3 sentences appear within the first 150 words, structurally isolatable?
- PASS: standalone paragraph or labeled block within first 150 words
- FAIL: answer distributed, embedded in narrative → **caps QAPE score at ≤5 AND Self-Containment at ≤4**

Output gate results in scorecard:
```
GATE CHECKS
Gate 1 (Explicit Question): PASS/FAIL — [reason]
Gate 2 (Direct Answer):     PASS/FAIL — [reason]
```

### Step 2 — Structural classification (mandatory, before scoring)
Read the full article. Identify the H3 pattern. Produce this block and include it at the top of your output, before any dimension scores:

```
STRUCTURAL CLASSIFICATION
Article type: [Informational / Comparison / How-to / Recommendation]
H3 pattern:   [Query-driven / Attribute-driven / Process-driven / Mixed]
Evidence:     [1-2 sentences explaining what signals this pattern]
QAPE path:    [Path A / Path B / Path C]
```

See rubric Step 0 for classification guidance. This output is auditable.

### Step 3 — Read rubric
Load `aeo/context/aeo-scoring-rubric.md`. Use dimension definitions verbatim.

### Step 4 — Score each dimension

**Dim 1: QAPE / Answer Structure (18%)**
Confirm your Step 2 path (A/B/C). Apply path-appropriate criteria from the rubric Dim 1 section. Then run the extractability test on each H2/H3 block:

> _"Named subject + direct claim + specific fact/stat/entity? Yes to all → extractable. No to any → not extractable."_

Score = % of passages passing the extractability test. Quote the best and weakest section. Fix instructions reference path-appropriate criteria.

**Dim 2: Passage Self-Containment (14%)**
Per-passage 5-item checklist. What % of content blocks pass all 5?
Flag specific failing passages — explain which checklist item they fail.

**Dim 3: Structural Readability (9%)**
Check: heading hierarchy clean? paragraphs ≤4 sentences? tables for comparisons? FAQ present?
Flag specific violations.

**Dim 4: Statistical Density (17%)**
Count named statistics per 500 words. Threshold: 5+/500w = 9–10.
List the actual stats found. Call out sections that are stat-free.

**Dim 5: Uniqueness & Original Data (16%)**
Is there anything here AI can't find elsewhere?
Look for: original surveys, proprietary data, custom frameworks, first-party case studies.
If nothing original exists, score 2–3 (derivative). Be precise about what's missing.

**Dim 6: Trust & Authority (14%)**
Count: named expert quotes with attribution, stats with inline sources, author credentials, institution signals, external citations.
Note domain authority signals (edu, gov, established brand).

**Dim 7: Intent Match (7%)**
What is the query intent? Does the format match? (See rubric intent table.)
Informational → definition + expansion + FAQ. Comparison → table. How-to → numbered steps.

**Dim 8: Platform Specificity (5%)**
How well does this content serve each AI platform's citation preferences?
See rubric platform table: Perplexity (stat-dense), ChatGPT (definition-first), Google AIO (40–60w answer blocks), Claude (comprehensive, self-contained), Copilot (authority + speed).

### Step 4b — Platform Flags

After scoring, evaluate these boolean flags:
```
aio_ready:        ≤60w answer block present + ≥1 named citation + structured headings
chatgpt_ready:    article directly answers its title question with clear factual density
perplexity_ready: FAQ-structured sections present + ≥2 named stats per 500 words
gemini_ready:     clear entity definitions + structured sections + E-E-A-T signals
bing_ready:       structured headings, clear entities, technical basics present
```

### Step 4c — SEO Metadata Assessment

Evaluate and generate recommendations:
- **Title tag:** current title length + keyword placement. Suggest optimised version (50–60 chars).
- **Meta description:** if detectable, assess. Generate suggested version (150–160 chars, value-prop clear).
- **URL slug:** assess current slug (keyword-rich? ≤60 chars? lowercase?). Suggest if poor.
- **Schema detected:** list `@type` values found in Step 1b. Recommend any missing types (Article, FAQPage, HowTo, LearningResource).

### Step 5 — Compute composite
`Composite = (D1×0.18) + (D2×0.14) + (D3×0.09) + (D4×0.17) + (D5×0.16) + (D6×0.14) + (D7×0.07) + (D8×0.05)`

### Step 6 — Gap analysis (if context = "competitor" or "wayground")
For competitor URLs: identify the 2–3 dimensions where Wayground can most easily beat them.
For Wayground URLs: identify the 2–3 dimensions with the largest improvement opportunity.

## Output Format

```markdown
# D2 Score: [Page Title]
_URL: [url]_
_Topic: [topic]_
_Context: [competitor / calibration / wayground]_
_Rubric version: v1.2 | Scored: [date]_

**Composite Score: X.X/10**
**Routing (Wayground URLs only):** [Pass / Minor C5 / High — ask human / Extreme C3 / Escalate]

## Gate Checks
| Gate | Result | Reason |
|---|---|---|
| Gate 1: Explicit Question | PASS/FAIL | [reason] |
| Gate 2: Direct Answer | PASS/FAIL | [reason] |

## Dimension Scores
| Dimension | Weight | Score | Key Finding |
|---|---|---|---|
| QAPE / Answer Structure | 18% | X/10 | [one-line finding] |
| Passage Self-Containment | 14% | X/10 | [one-line finding] |
| Structural Readability | 9% | X/10 | [one-line finding] |
| Statistical Density | 17% | X/10 | [one-line finding] |
| Uniqueness & Original Data | 16% | X/10 | [one-line finding] |
| Trust & Authority | 14% | X/10 | [one-line finding] |
| Intent Match | 7% | X/10 | [one-line finding] |
| Platform Specificity | 5% | X/10 | [one-line finding] |

## Platform Flags
| Platform | Ready | Key gap |
|---|---|---|
| Google AIO | ✅/❌ | |
| ChatGPT | ✅/❌ | |
| Perplexity | ✅/❌ | |
| Gemini | ✅/❌ | |
| Bing Copilot | ✅/❌ | |

## SEO Metadata
- **Current title:** [title] ([N] chars) — [assessment]
- **Suggested title tag:** [50–60 chars]
- **Suggested meta description:** [150–160 chars]
- **Slug assessment:** [current slug] — [good/poor + reason]
- **Schema detected:** [list or “none detected”]
- **Schema to add:** [Article, FAQPage, HowTo, LearningResource as applicable]

---

## Dimension Notes

### Statistical Density (X/10)
Stats found:
- "[stat 1]" (source)
- "[stat 2]" (source)
Stat-free sections: [list]

### Uniqueness & Original Data (X/10)
Original content found: [yes/no — describe]
Derivative content: [what's recycled from common knowledge]

### Trust & Authority (X/10)
- Expert quotes: N ([names])
- Stats with source: N
- Author: [name/credentials if present]
- Domain authority signal: [edu/gov/brand]

---

## Gap Analysis
[2–3 bullet points: where this URL is beatable / where Wayground should focus]

## Citability Summary
[2–3 sentence plain-English verdict: why this URL does or doesn't get cited by AI]
```

## Scoring Notes
- D2 has **no binary gate** — it produces scores, analysis, and routing recommendations
- Composite ≥ 7.0 = high citability candidate (empirical threshold from calibration corpus)
- Composite 5.5–6.9 = moderate — likely cited on domain authority alone if brand is strong
- Composite < 5.5 = low citability — structural or content gaps are the bottleneck

## Enhancement Routing (for Wayground URLs)
```
PASS (all dims ≥ 7)                         → E1 brand → E2 ICP review → F1 publish
Minor gaps (1–2 dims < 7, composite ≥ 6)    → C5 surgical fix → re-score
High gaps (3+ dims < 7, composite 4–6)      → Ask human confirmation → C5 heavy → re-score
Extreme (composite < 4 OR 4+ dims < 5)      → C3 full regeneration (same slug/topic)
Escalate (2x loops no PASS)                 → Human review
```
For competitor/external URLs: output gap analysis + brief inputs for B3 (new article), not C5.

## Files
- Reads: `aeo/context/aeo-scoring-rubric.md` (always, before scoring)
- Fetches: URL content via `tavily_extract` (advanced)
- Saves results to: `memory/research/scoring-runs/` when run as part of calibration
