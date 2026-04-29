# D2 URL Evaluator — KNOWLEDGE.md
_What's empirically true about URL citability. Updated by ground_truth_check.py (1st Monday) and P-004 research scrape._
_Last updated: 2026-04-27_

---

## Citability Thresholds (empirical)

From calibration corpus (30 URLs, 5 topics, ChatGPT):
- **Composite ≥7.0** = high citability (Stanford CTL: 7.02, cited 50%; learningscientists: 6.97, cited 50%)
- **Composite 5.5–6.9** = moderate — cited mainly on domain authority (Edutopia hub: 3.37, cited 42% — pure brand)
- **Composite <5.5** = low citability — structural or content gaps dominate

**Important caveat:** Domain authority can override composite score. A low-scoring URL from an authoritative domain (.edu, established brand) may still be cited. Flag this explicitly in D2 output.

---

## GEO_GOLD URL Patterns (what actually gets cited)

### Pattern 1: Foundational research papers
- Black & Wiliam 1998 (assess.ucr.edu PDF) — cited 67%, composite 5.98
- Dunlosky 2013 (wku.edu PDF) — cited 50%, composite 6.37
- ASCD Tomlinson PDF — cited 83%, composite ~6.1 (heuristic)
- **Why:** Trust(9) + Uniqueness(10) dominate. AI treats foundational papers as authoritative regardless of structure.
- **Signal to flag in D2:** Any .edu or .gov PDF with named authors = high citation probability even with low structure scores

### Pattern 2: Research-backed practitioner hubs
- learningscientists.org — cited 50%, composite 6.97
- Stanford CTL (ctl.stanford.edu) — cited 50%, composite 7.02
- **Why:** Academic institution + practitioner format + some stats. Best of both worlds.
- **Signal to flag:** .edu domain + practitioner-readable format = strong citation candidate

### Pattern 3: High-domain-authority brand pages (cited despite low content quality)
- Edutopia topic hub — cited 42–83%, composite 3.37–5.96
- **Why:** AI knows the brand, cites it as a reference even when content is thin
- **Signal to flag:** Edutopia, ASCD, NWEA, Learning Scientists = will be cited regardless of D2 score

### Pattern 4: Definition-first + clean structure (what we should build)
- renaissance.com EdWords — composite 6.87, QAPE 8, Intent 9
- Third Space Learning — composite 6.88, QAPE 8
- **Why:** Perfect informational intent execution. ChatGPT prefers definition-first.
- **These are the format templates for Wayground articles**

---

## Competitor Field Benchmarks by Topic

### Differentiated Instruction
- Field best: Vanderbilt IRIS 6.81 | Field avg: 5.73
- Universal weakness: Stats (field avg 3.4/10)
- Win condition: Stats 9 + Uniqueness 9 → composite 7.5+

### Student Engagement
- Field best: Xello 6.42 | Field avg: 5.67
- Universal weakness: Stats (field avg 2.6/10) — worst in any topic scored
- Win condition: Stats 9 + Uniqueness 9 → composite 7.5+ (would be field outlier by wide margin)

### Formative Assessment
- Field best: Black & Wiliam PDF (trust/uniqueness) | practitioner best: Renaissance 6.87
- Universal weakness: Stats on practitioner pages (avg 2–4/10)

### Retrieval Practice
- Field best: learningscientists.org why-it-works 7.07 | cultofpedagogy 7.00
- More competitive field — need Stats 9 to differentiate

---

## Platform Citation Preferences (use when scoring Platform Specificity dim)

| Platform | Primary signal | Secondary |
|---|---|---|
| ChatGPT (GPT-5.3) | Definition-first, authority check, ~16 domains/response | Named sources, recent dates |
| Gemini | Entity coverage, structured data, freshness | .edu/.gov domains |
| Perplexity | Stat density, first-party data, recency | FAQ schema |
| Google AIO | 40–60 word answer blocks, structured data | Core SEO eligibility |
| Claude | Comprehensive, self-contained, accurate | Nuance over brevity |

---

## Domain Authority Modifier (not in rubric — use as commentary)

When scoring Trust & Authority, note if domain is in this list — AI will likely cite regardless of content quality:
`edutopia.org, ascd.org, edweek.org, apa.org, ncbi.nlm.nih.gov, any .edu, any .gov, learningscientists.org, nwea.org, vanderbilt.edu`

Flag in D2 output: *"Domain authority likely compensates for content gaps — cited despite low composite."*
