# Rubric Drift Prevention
_Version: 1.0 — 2026-04-22_
_Owner: Waymark (aeo/context/ is the canonical home for all rubric governance)_

---

## The Three Drift Problems

| Drift Type | What Happens | How We Prevent It |
|---|---|---|
| **Rubric Drift** | Scoring logic fragments across D1/D2/D3 files; agents diverge from each other silently | Single source of truth — rubric lives in one file, agents are readers only |
| **Signal Drift** | Rubric scores stop predicting actual AI citation; threshold ≥7 becomes meaningless | Monthly ground truth cron — check if scores correlate with real citation |
| **Knowledge Drift** | AEO/GEO research landscape evolves; rubric weights become stale | Quarterly research scan — update memory/research/, review dimension weights |

---

## 1. Rubric Drift → Single Source of Truth

### The Rule
One file. One version. All agents read it, none own it.

```
aeo/context/aeo-scoring-rubric.md   ← THE rubric (versioned)
aeo/context/rubric-changelog.md     ← version history + reasons + validation runs
```

**No scoring dimension logic lives inside D1, D2, or D3.**
Those agents contain: routing logic, input handling, output formatting only.
If you find scoring criteria, score thresholds, or dimension definitions inside an agent file — it's wrong. Move it to the rubric.

### Enforcement
The `skill-creator` skill can audit skill files for embedded scoring logic.
Periodically run it against D1, D2, D3 with the prompt:
> "Audit this skill for any scoring dimension definitions, score thresholds, or rubric criteria that should live in aeo-scoring-rubric.md instead."

Run this audit:
- After any rubric update
- After any agent skill edit
- Quarterly as part of the knowledge drift review

### Change Process
Any rubric change follows this exact sequence:
```
1. Edit aeo-scoring-rubric.md
2. Bump version (v1.x → v1.x+1 for minor, v1.x → v2.0 for structural)
3. Add entry to rubric-changelog.md (what changed, why, date)
4. Rerun calibration corpus on ≥5 URLs from memory/research/calibration-corpus.md
5. Compare new scores vs previous scores — capture delta
6. Post validation delta to Slack #way-mark
7. If delta is large (>1.0 composite on any URL) → flag for human review before deploying
```

---

## 2. Signal Drift → Ground Truth Cron

### The Problem
The ≥7 pass threshold (D1) and equivalent D2 scores were set from rubric logic, not empirical data.
Over time, AI citation behavior evolves. A rubric score that predicted citation in April 2026 may not predict it in October 2026.

### Monthly Ground Truth Check
**Cron:** Monthly (first Monday of each month)
**Agent:** D2 URL Evaluator

```
Process:
1. Pull top 10 Wayground URLs by D2 score (from memory/research/scoring-runs/)
2. For each URL, run Tavily search on its target query
3. Check whether the URL (or its content) appears in AI citations
   - Test on: ChatGPT, Perplexity, Gemini (pick 2 of 3 each month, rotate)
4. Record: [URL | D2 score | cited: Y/N | platform | date]
5. Calculate score-to-citation correlation for the month
6. Compare vs prior month
7. Post delta report to Slack #way-mark
```

**Trigger for rubric review:**
- Citation rate drops >15% month-over-month for high-scoring URLs (≥75)
- Any URL scoring ≥80 fails to get cited across 2+ platforms
- Any URL scoring <60 gets cited consistently (false negative pattern)

### Major Model Release Protocol
On any major AI model release (GPT-5, Gemini 3, Claude 4+, Perplexity major version):
1. **Manually rerun full calibration corpus** (all 15-20 URLs in memory/research/calibration-corpus.md)
2. Compare scores vs previous run
3. Check citation status on new model
4. If citation patterns shift → rubric weight review

**Backlog item (recurring):** "On major model release: rerun calibration corpus."
_This item should live in BACKLOG.md as a standing trigger, not a one-time task._

---

## 3. Knowledge Drift → Periodic Research Scan

### The Problem
AEO/GEO is a fast-moving field. The research basis in the rubric (Princeton/Georgia Tech/IIT Delhi studies etc.) will age. New findings may shift which dimensions matter most.

### Quarterly Research Scan
**Trigger:** Quarterly (or manually when significant new research surfaces)

```
Process:
1. Read memory/research/ — flag any entries >6 months old
2. Search for new GEO/AEO papers:
   - arXiv: "generative engine optimization", "AI citation", "LLM citation behavior"
   - Practitioner: SparkToro, Ahrefs, Search Engine Land, Kevin Indig
3. Check if any reference repo (geo-seo-claude or equivalent) has been updated
4. For each new finding:
   - Does it validate an existing dimension? → Update research basis table in rubric
   - Does it challenge a weight? → Flag for weight review
   - Does it surface a missing dimension? → Propose new dimension via rubric-changelog.md
5. Update memory/research/ with new entries (dated, sourced)
6. If weight adjustment warranted → follow rubric change process (section 1 above)
```

### memory/research/ Structure
```
memory/research/
├── calibration-corpus.md        ← 15-20 URL corpus for threshold validation
├── scoring-runs/                ← timestamped scoring run outputs
│   └── YYYY-MM-DD-run.md
├── ground-truth-checks/         ← monthly citation check results
│   └── YYYY-MM-check.md
└── aeo-research/                ← GEO/AEO research papers and findings
    └── YYYY-MM-DD-source.md
```

This folder is only useful if it gets updated. The quarterly scan is its maintenance trigger.

---

## Combined Cron/Trigger Summary

| Frequency | Trigger | Action | Owner |
|---|---|---|---|
| On every rubric edit | Manual | Version bump → changelog → rerun ≥5 URLs → Slack delta | Waymark |
| Monthly | Cron (1st Monday) | Ground truth check: D2 score vs actual AI citation | Waymark |
| On major model release | Standing backlog item | Full calibration corpus rerun | Waymark |
| Quarterly | Cron or manual | Research scan, stale entry review, weight check | Waymark |
| After any agent skill edit | Manual | skill-creator audit for embedded scoring logic | Waymark |

---

## The Self-Improving Layer (Future — Parked)

A deeper feedback loop is designed but not yet built:
- **TRAINING.md** per agent: seeded knowledge, updated by knowledge-refresh cron (Axis 1 — what's new in AEO)
- **FEEDBACK.md** per agent: performance correlation log, rubric drift notes, updated by experience-refresh cron (Axis 2 — what actual published articles taught us)
- **Contrastive corpus:** top 15-20 + worst 5-10 performing articles; delta grounds dimension weights
- **Performance data sources:** BigQuery (GA4 + GSC), SEMrush — join in BQ for richest signal
- **Approval UX:** cron posts proposals to #way-mark on spike; human approves/rejects inline

_Revisit when: BQ access confirmed from OpenClaw, ≥20 articles published (enough performance data to be meaningful)._

---

_Related files:_
- `aeo/context/aeo-scoring-rubric.md` — the rubric itself
- `aeo/context/rubric-changelog.md` — version history
- `memory/research/calibration-corpus.md` — calibration URL set (to be built)
- `memory/research/scoring-runs/` — historical scoring run outputs
