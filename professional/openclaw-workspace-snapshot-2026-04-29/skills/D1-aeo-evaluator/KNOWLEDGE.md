# D1 AEO Evaluator — KNOWLEDGE.md
_What's empirically true about AEO scoring. Updated by ground_truth_check.py (1st Monday) and P-004 research scrape._
_Last updated: 2026-04-27_

---

## Rubric Weight Calibration History

### v1.1 — 2026-04-27 (current)
Based on delta analysis: 10 GEO_GOLD URLs vs 20 non-cited, 5 topics, ChatGPT platform.

| Dimension | Delta (gold vs rest) | Predictive rank | Weight |
|---|---|---|---|
| Statistical Density | +1.55 | #1 | 15% |
| Uniqueness & Original Data | +1.45 | #2 | 14% |
| Trust & Authority | +1.25 | #3 | 12% |
| Passage Self-Containment | +1.15 | #4 | 12% |
| Intent Match | +0.95 | #5 | 4% |
| QAPE / Answer Structure | +0.70 | #6 | 17% |
| Structural Readability | +0.60 | #7 | 8% |

**Implication for D1 scoring:** When an article narrowly fails, Stats and Uniqueness are the highest-leverage fixes. Structural Readability is a prerequisite (must pass) but doesn't differentiate cited from non-cited content once the threshold is met.

---

## What Gets Articles Cited by AI (empirical)

### Finding 1: Stats density is the single most discriminating signal
- Gold URLs avg 5.1/10 on stats; non-cited avg 3.55/10 — Δ+1.55
- A Wayground article with 5+ named statistics per 500 words is a category outlier in education content
- Source: `memory/research/scoring-runs/rubric-weight-proposal.md` (2026-04-27)

### Finding 2: Original data creates citation dependency
- If Wayground has data no one else has (platform usage metrics, survey results), AI must cite us
- Even one first-party stat ("X% of teachers using Wayground report Y") is enough to anchor a citation
- Source: calibration corpus delta analysis

### Finding 3: Domain authority overrides content quality at the extremes
- Edutopia hub page scored 3.4/10 D2 but cited 42% — pure brand trust effect
- Black & Wiliam 1998 PDF scored 5.98/10 but cited 67% — Trust(9) + Uniqueness(10) dominated
- Implication: don't penalise high-trust sources in D1 scoring; flag the trust signal explicitly

### Finding 4: SERP rank ≠ citation rate
- formative.com ranks #1 for "what is formative assessment" but cited only 17%
- Content quality (stats, uniqueness, trust) predicts citation better than rank
- Source: `memory/research/geo-runs/2026-04-24-calibration-formative-assessment.md`

### Finding 5: Academic PDFs get cited despite poor structure
- Black & Wiliam 1998, Dunlosky 2013, ASCD Tomlinson PDF all cited 50–83%
- Pattern: foundational research papers win on Trust+Uniqueness regardless of QAPE score
- Implication for D1: when scoring Wayground content, Trust + Stats gaps are most worth flagging

---

## Platform-Specific Scoring Signals (from knowledge/aeo-geo/platform-signals.md)

- **ChatGPT (GPT-5.3):** ~15.9 unique domains cited per response (down from 19.8). Authority check via `site:` operators. Definition-first structure critical.
- **Gemini:** +388% referral traffic YoY. Structured data boosts inclusion. Entity coverage matters.
- **Perplexity:** First-party data + third-party citations on same page. Recency-weighted. FAQ schema critical.
- **Google AI Overviews:** Structured data + core SEO eligibility. Concise 40–60 word answer blocks.

---

## Research Basis (from rubric)

| Finding | Source |
|---|---|
| Quotations +41% AI visibility | arXiv:2311.09735 (Princeton/Georgia Tech/IIT Delhi 2024) |
| Statistics +33% AI visibility | arXiv:2311.09735 |
| Source citations +28% AI visibility | arXiv:2311.09735 |
| Definition patterns increase citation 2.1x | Georgia Tech 2024 |
| Optimal citation passage: 134–167 words | Bortolato 2025 |

---

## Scoring Calibration Notes

- **Composite ≥7.5** = likely to be cited if domain trust is adequate
- **Composite 6.5–7.4** = may be cited on domain authority alone; content not strong enough to win cold
- **Composite <6.5** = unlikely to be cited without exceptional domain trust
- **EAR Coverage** is the most Wayground-specific dimension — a well-briefed article covering all B2 attributes is a structural advantage competitors can't easily replicate
