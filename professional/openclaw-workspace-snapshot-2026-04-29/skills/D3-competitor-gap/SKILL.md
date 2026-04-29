---
name: D3-competitor-gap
description: AEO competitor gap analyzer for Wayground. Use when comparing multiple URLs on a topic to find where Wayground can win AI citations. Scores all URLs through D2 rubric, builds a dimension-by-dimension comparison matrix, and outputs a ranked opportunity report. Triggers on phrases like "competitor analysis", "compare these URLs", "where can we beat competitors", "run D3", "gap analysis on topic", "what are competitors doing better".
model: claude-sonnet-4-6
---

# D3 — Competitor Gap Analyzer

> Scores multiple URLs on the same topic. Finds where Wayground can differentiate and win AI citations.

## Role
Answer: **"On this topic, where are competitors weak — and what would a Wayground article need to do to dominate AI citations?"**

## Inputs
- `topic` — the target query/keyword (required)
- `urls` — list of competitor URLs to score (required; 3–8 URLs recommended)
- `wayground_url` — Wayground's existing URL on this topic, if any (optional — included in comparison if provided)

## Before Scoring — Read These Files
1. `aeo/context/aeo-scoring-rubric.md` — **scoring authority**. Always follow this.
2. `skills/D3-competitor-gap/KNOWLEDGE.md` — field benchmarks by topic, competitor authority tiers, format templates
3. `skills/D3-competitor-gap/FEEDBACK.md` — which gap analyses led to winning articles

### How to use KNOWLEDGE.md + FEEDBACK.md
- **Score strictly from the rubric.** KNOWLEDGE.md and FEEDBACK.md do not change scoring.
- **Use KNOWLEDGE.md for contextualisation** — e.g. a score of 6.5 means something different in student engagement (field best 6.42) vs retrieval practice (field best 7.07). State this context in output.
- **Use FEEDBACK.md for pattern suggestions** — if a prior gap analysis led to a winning article, note that as a positive signal for the current topic.
- **Never change win conditions, thresholds, or weights** unless approved by human and applied to rubric.
- **Drastic delta rule:** Only flag a pattern if it's consistent across ≥3 prior topics in FEEDBACK.md.

Current version: **v1.2** (2026-04-27)

## D3 Weight Table (same as D2)
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

## Evaluation Process

### Step 1 — Gather competitor URLs (if not provided)
If `urls` not provided, run Tavily search for the topic to find top-ranking pages:
```
tavily_search(query=topic, max_results=8)
```
Take the top 5–7 URLs excluding Wayground's own domain.

### Step 2 — Score each URL via D2 logic
For each URL:
1. Fetch content: `tavily_extract(urls=[url], extract_depth="advanced", query=topic)`
2. Fetch schema: `web_fetch(url, extractMode="text")` — scan for `application/ld+json` blocks, extract `@type` values (FAQPage, Article, HowTo, etc.). If web_fetch returns empty, note "schema unverifiable" for that URL.
3. Run Step 0 structural classification (see rubric) — classify H3 pattern, select QAPE path
4. Score all 8 dimensions using D2 rubric (same criteria, same weights)
5. For Dim 1 (QAPE): apply path-appropriate criteria + extractability test; score = % of passages passing extractability test
6. For Dim 9 (Platform Specificity): incorporate schema signals from step 2
7. Compute composite

Run all content + schema fetches first, then score. Do not interleave. Include structural classification and schema findings in per-URL notes.

> Schema verification is owned by the SEO Technical Evaluator agent (T1) when built. D3 performs best-effort extraction here; T1 is the authoritative source. Reference: `memory/BACKLOG.md` P-008.

### Step 2b — Platform flags per URL
For each URL, after scoring, evaluate platform flags:
```
aio_ready, chatgpt_ready, perplexity_ready, gemini_ready, bing_ready
```
Include as a summary row in the comparison matrix. This shows which platforms each competitor is optimised for — and which are unclaimed territory for Wayground.

### Step 3 — Build comparison matrix
Create a dimension-by-dimension table across all URLs. Identify:
- **Field ceiling** — best score any competitor achieves per dimension
- **Field floor** — worst score per dimension
- **Field average** — mean per dimension across all competitors
- **Gap to beat** — what score Wayground needs to exceed the field leader on each dimension

### Step 4 — Rank by citability threat
Sort competitors by composite score descending. Top = hardest to beat.

### Step 5 — Identify winning dimensions
For each dimension, ask: *"Can Wayground realistically score higher than the field leader here?"*

**High-opportunity dimensions** (where Wayground can win):
- Statistical Density — almost all competitors score low (avg 3–4). Wayground can use platform data.
- Uniqueness — competitors rarely have original data. Wayground's usage data is exclusive.
- Trust — achievable with named expert quotes + research citations (C4 does this).

**Low-opportunity dimensions** (where established brands win on authority alone):
- Trust (domain authority component) — edutopia.org, ascd.org score 7–9 purely on brand
- Platform Specificity — hard to beat established sites already indexed

### Step 6 — Generate content strategy
Based on the gap analysis, produce:
1. **"Win conditions"** — dimensions where a Wayground article should aim to exceed all competitors
2. **"Table stakes"** — dimensions where Wayground must match the field to not be excluded
3. **"Concede"** — dimensions where incumbents have structural advantages (domain authority, age)

## Output Format

```markdown
# D3 Competitor Gap: [Topic]
_Rubric version: v1.1 | Scored: [date]_
_URLs scored: N_

## Composite Scores (ranked)
| URL | Composite | Citability |
|---|---|---|
| [url 1] | X.X/10 | High/Med/Low |
| [url 2] | X.X/10 | High/Med/Low |
| ... | | |
| **Wayground target** | **need X.X** | **to win** |

---

## Dimension Comparison Matrix
| Dimension | [Competitor A] | [Competitor B] | [Competitor C] | Field avg | Field best | Wayground target |
|---|---|---|---|---|---|---|
| QAPE (18%) | X | X | X | X.X | X | X+ |
| Self-Containment (14%) | X | X | X | X.X | X | X+ |
| Structural Readability (9%) | X | X | X | X.X | X | X+ |
| Statistical Density (17%) | X | X | X | X.X | X | X+ |
| Uniqueness (16%) | X | X | X | X.X | X | X+ |
| Trust & Authority (14%) | X | X | X | X.X | X | X+ |
| Intent Match (7%) | X | X | X | X.X | X | X+ |
| Platform Specificity (5%) | X | X | X | X.X | X | X+ |
| **Composite** | X.X | X.X | X.X | X.X | X.X | **X.X+** |

---

## Win Conditions for Wayground
_Dimensions where a Wayground article can realistically exceed all competitors:_

1. **Statistical Density** — field avg X.X. Competitors cite vague claims. Wayground can hit 9/10 with: [specific stat opportunities — Wayground usage data, named studies]
2. **Uniqueness** — field avg X.X. No competitor has original data. Wayground can hit 8–9/10 with: [specific original data Wayground could use]
3. **[Third dim]** — [same pattern]

## Table Stakes (must match field)
- [Dim]: field scores X–X. Must achieve ≥X or won't be competitive.

## Concede (structural disadvantage)
- Domain authority component of Trust: [edutopia.org, ascd.org] have years of trust signals we can't replicate short-term. Compensate via original data.

---

## Content Brief Inputs
_Direct inputs for B3 brief generator:_

- **Minimum composite to be competitive:** X.X
- **Priority dimensions (build to these first):** Statistical Density, Uniqueness, [third]
- **Format requirement:** [what intent type + specific format elements the field is missing]
- **Stats to acquire:** [specific statistics Wayground should find/generate]
- **Unique data angle:** [what Wayground-exclusive data could anchor this article]
- **Citation targets:** [URLs in this analysis worth citing as supporting sources]
```

## Notes
- D3 has **no gate** — produces analysis, platform flags, and brief inputs, not pass/fail
- Platform flags in matrix reveal unclaimed distribution opportunities — if no competitor is perplexity_ready, that's a fast win
- Always challenge the topic framing before running: does Wayground already have coverage? Is the KD achievable? Is this the right ICP angle? Surface this before scoring.
- Results feed directly into B3 content brief as competitive context
- Run D3 before writing any article on a competitive keyword — tells B3 exactly what to beat
- Save full output to `memory/research/scoring-runs/` for calibration corpus expansion

## Files
- Reads: `aeo/context/aeo-scoring-rubric.md` (always)
- Fetches: competitor URLs via `tavily_extract` (advanced)
- Outputs to: B3 content brief (as competitive context input), `memory/research/scoring-runs/`
