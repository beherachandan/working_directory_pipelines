# D2 URL Evaluator — FEEDBACK.md
_How D2 scores correlate with actual AI citation outcomes. Updated by ground_truth_check.py (1st Monday)._
_Last updated: 2026-04-27_

---

## Score-to-Citation Correlation Log

_Format: URL | D2 score | Citation rate (ChatGPT) | Citation rate (Gemini) | Notes_

| URL | D2 | ChatGPT cite% | Gemini cite% | Notes |
|---|---|---|---|---|
| assess.ucr.edu — Black & Wiliam PDF | 5.98 | 67% | pending | Trust+Uniqueness override low structure |
| learningscientists.org/retrieval-practice | 6.97 | 50% | pending | Research-backed practitioner hub |
| wku.edu — Dunlosky 2013 PDF | 6.37 | 50% | pending | Academic PDF pattern |
| edutopia.org — exit tickets article | 5.96 | 83% | pending | Brand authority dominates |
| thirdspacelearning.com — exit ticket | 6.88 | 75% | pending | Strong QAPE + structure |
| cpet.tc.columbia.edu — exit tickets | 6.61 | 67% | pending | Columbia trust signal |
| formative.com — exit ticket | 6.35 | 58% | pending | Good QAPE, low uniqueness |
| ascd.org — exit slips | 5.73 | 58% | pending | ASCD brand carries it |
| weareteachers.com — exit tickets | 5.34 | 50% | pending | Low stats, brand helps |
| ctl.stanford.edu — growth mindset | 7.02 | 50% | pending | .edu + practitioner format |

**Observed pattern (ChatGPT, 5 topics):**
- D2 ≥6.5 + established brand → cited 50%+ consistently
- D2 <5.5 + no brand → rarely cited
- D2 <5.5 + strong brand (Edutopia, ASCD) → still cited 42–83% (brand override)
- D2 ≥7.0 + .edu domain → cited 50%+ even with no brand recognition

---

## False Positives (high score, not cited)

_URLs that scored well but weren't cited — investigate why_

| URL | D2 | Citation rate | Likely reason |
|---|---|---|---|
| _(none identified yet — Gemini runs pending)_ | — | — | — |

---

## False Negatives (low score, cited anyway)

| URL | D2 | Citation rate | Likely reason |
|---|---|---|---|
| edutopia.org topic hub | 3.37 | 42% | Brand authority (edutopia.org domain) |
| Black & Wiliam PDF | 5.98 | 67% | Foundational research paper — Trust+Uniqueness=9,10 |

---

## Monthly Ground Truth Check Results

| Month | Platform | High-score cite rate | Low-score cite rate | Drift flags |
|---|---|---|---|---|
| _(cron starts May 2026)_ | — | — | — | — |

---

## Pending
- [ ] Run Gemini calibration (quota reset needed) → populate Gemini cite% column
- [ ] First monthly ground truth check (May 2026) → populate monthly log
- [ ] After 3 months of ground truth data: recalibrate composite threshold (currently 7.0)
