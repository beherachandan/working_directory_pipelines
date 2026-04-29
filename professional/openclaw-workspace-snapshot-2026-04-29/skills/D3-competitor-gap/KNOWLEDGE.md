# D3 Competitor Gap — KNOWLEDGE.md
_Competitor field patterns by topic. Updated by D3 runs and ground_truth_check.py._
_Last updated: 2026-04-27_

---

## Universal Field Weakness: Statistical Density

Across every topic scored, **statistical density is the weakest dimension in the entire K-12 education content field.**

| Topic | Stats field avg | Best competitor | Wayground target |
|---|---|---|---|
| Student engagement | 2.6/10 | Xello: 4/10 | 9/10 |
| Differentiated instruction | 3.4/10 | NCBI paper: 7/10 | 9/10 |
| Formative assessment | ~3/10 | Black & Wiliam PDF: 9/10 | 9/10 |
| Exit tickets | ~3/10 | Academic PDFs: 7–9/10 | 9/10 |

**Strategic implication:** Stats density is Wayground's single highest-leverage differentiator across ALL topics. Any article with 5+ named statistics per 500 words is a field outlier.

---

## Competitor Field Benchmarks by Topic

### Student Engagement / Learning Strategies
- Full report: `memory/research/scoring-runs/2026-04-27-d3-student-engagement.md`
- Field best: Xello (6.42) — 3-dimension framework (behavioral/cognitive/emotional) is the gold standard structure
- Field weakness: Stats avg 2.6, Uniqueness avg 4.4 — no competitor has original data
- Win condition: Stats 9 + Uniqueness 9 + Xello-style framework → composite 7.5+ (field outlier)
- Key stat to acquire: Gallup 2023 (49% of K-12 students engaged), Freeman et al. 2014 (active learning reduces failure 55%)

### Differentiated Instruction
- Full report: `memory/research/scoring-runs/2026-04-27-d3-differentiated-instruction.md`
- Field best: Vanderbilt IRIS (6.81) — Traditional vs DI comparison table is the format template
- Field weakness: Stats avg 3.4 on practitioner pages (NCBI paper has stats but poor practitioner format)
- Win condition: Vanderbilt format + NCBI-level stats + Wayground implementation data → composite 7.5+
- Key stat to acquire: Tomlinson 2003 research outcomes, flexible grouping effectiveness data

### Formative Assessment
- Calibration run: `memory/research/geo-runs/2026-04-24-calibration-formative-assessment.md`
- GEO gold: Black & Wiliam PDF (67%) — trust+uniqueness play; Renaissance EdWords (6.87) — format template
- Key competitor gap: practitioner pages universally lack stats; academic papers lack practitioner format

### Retrieval Practice
- Calibration run: `memory/research/geo-runs/2026-04-24-calibration-retrieval-practice.md`
- More competitive field: learningscientists.org (6.97), cultofpedagogy (7.00) both near threshold
- Win condition requires: strong stats + Wayground platform data on retrieval/quiz performance

### Exit Tickets
- Calibration run: `memory/research/geo-runs/2026-04-24-calibration-exit-tickets-in-the-classroom.md`
- Richest citation landscape: 6 gold URLs (50–83%). Edutopia dominates on brand.
- Win condition: beat Edutopia on stats + uniqueness while matching their structure

---

## Competitor Domain Authority Tiers

**Tier 1 — Will be cited regardless of content quality (domain authority effect):**
`edutopia.org, ascd.org, edweek.org, apa.org, vanderbilt.edu, stanford.edu, berkeley.edu`

**Tier 2 — Cited when content quality is also present:**
`learningscientists.org, cultofpedagogy.com, thirdspacelearning.com, renaissance.com, understood.org`

**Tier 3 — Cited only when content quality is high:**
`tophat.com, teachtci.com, 3plearning.com, hmhco.com, weareteachers.com`

**Implication for D3:** Wayground is currently Tier 3 (new domain, no brand recognition). Must win on content quality alone — Stats + Uniqueness are the only levers available until domain authority builds.

---

## Format Templates Worth Studying

| Format | Best example | Why it works |
|---|---|---|
| Traditional vs DI comparison table | Vanderbilt IRIS | Extractable, self-contained, answers implicit comparison query |
| 3-dimension framework | Xello (behavioral/cognitive/emotional) | Provides structure AI can reference and attribute |
| Q&A / EdWords glossary | Renaissance EdWords | Perfect ChatGPT extraction format |
| Numbered steps + expert quote per step | TCI (teachtci.com) | Expert attribution + practitioner credibility |
| Definition + Why + How + FAQ | learningscientists.org | Full informational intent coverage |
