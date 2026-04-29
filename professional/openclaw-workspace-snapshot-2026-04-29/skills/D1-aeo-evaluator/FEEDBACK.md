# D1 AEO Evaluator — FEEDBACK.md
_How D1 scores correlate with real outcomes. Updated by rubric_self_update.py (2nd Monday) and P-005 performance cron._
_Last updated: 2026-04-27_

---

## Score-to-Outcome Log

_Format: Article slug | D1 score | Published date | Cited by AI (Y/N/pending) | Notes_

| Article | D1 Score | Published | Cited | Notes |
|---|---|---|---|---|
| _(no articles published yet)_ | — | — | — | Pipeline not yet started |

---

## Revision Loop Performance

_Track: how many revision loops articles needed before PASS_

| Article | Loops needed | Dims that failed | Fix that worked |
|---|---|---|---|
| _(no data yet)_ | — | — | — |

---

## Calibration Corpus Validation

### v1.0 → v1.1 weight change (2026-04-27)
- 5 topics calibrated before applying weights
- Delta: Stats +1.55, Uniqueness +1.45, Trust +1.25 — consistent across topics
- Weight changes applied: Stats 12%→15%, Uniqueness 12%→14%, QAPE 20%→17%
- Validation run pending: need to rescore ≥5 corpus URLs with v1.1 weights to confirm <1.0 composite shift

---

## Pending Actions
- [ ] Rescore calibration corpus (≥5 URLs) with v1.1 weights — confirm delta <1.0
- [ ] Once first articles published: log D1 score + citation outcome here
- [ ] After 5+ articles published: look for patterns in which dims most often caused REVISE

---

## Notes for Future Self
- D1 gate is currently set at ≥7/10 per dimension — this is rubric-logic-based, not yet empirically validated
- Once 10+ articles published and citation-checked: revisit whether ≥7 is the right threshold
- Stats and Uniqueness are the dims most worth pushing past 7 — they have the highest citation impact
