# PROJECT.md - Active Pipeline State

_Loaded at every session start. Reflects shared Wayground pipeline state — not per-user tasks._

## Active Projects

### 1. AEO Content Pipeline
**Status:** Active

| Stage | Count | Notes |
|-------|-------|-------|
| Keywords identified | 22 | Open opportunities ready for content gen |
| Articles drafted | 0 | |
| Articles scored | 0 | |
| Articles published | 0 | |

**Next action:** Run A1→B2→B3→C4→D1 pipeline on **student engagement strategies** (biggest AEO gap: stats field avg 2.6, field best only 6.42). Then differentiated instruction.

---

### 2. `trends-researcher` Skill
**Status:** Built & validated — ready to run

Built 2026-04-24 from scratch through iterative design with the user. Full skill at `skills/trends-researcher/`.

**Architecture (3 tracks):**
- Track 1: Google Trends via DataForSEO REST API (`/v3/keywords_data/google_trends/explore/live`) — rising/top queries per 13 validated category seeds, dual window (90d + 30d)
- Track 2: Upstream institutional signals — policy, research, conferences, grants via Tavily
- Track 3: Reddit grassroots discourse via Tavily

**Key files:**
- `skills/trends-researcher/SKILL.md` — full workflow
- `skills/trends-researcher/scripts/fetch-google-trends.py` — live, tested, working
- `skills/trends-researcher/scripts/trend-seeds.json` — 13 empirically validated seeds
- `skills/trends-researcher/references/signal-sources.md` — seeds, rejected seeds (with reasons), noise filter, Tavily templates

**Validated seeds** (tested against both SEMrush phrase_related AND Google Trends live API):
`reading instruction`, `writing instruction`, `differentiated instruction`, `formative assessment`, `social emotional learning`, `project based learning`, `inquiry based learning`, `phonics instruction`, `learning disabilities`, `STEM education`, `student engagement`, `educational technology`, `classroom behavior`

**DataForSEO note:** MCP npm package doesn't exist — call REST API directly via Python. Script handles this. Cost: ~$0.009/seed, ~$0.24 for full 13-seed dual-window run.

**Next action:** Run the skill end-to-end for first live emerging topics report → post to #way-mark

---

### 4. Full Pipeline + Publishing Stack
**Status:** Complete as of 2026-04-28 ✅

| Component | Status | Notes |
|---|---|---|
| E1 Brand Reviewer | ✅ Built | 20+ hard rules, vocabulary scan, format check |
| E2 ICP/Teacher Reviewer | ✅ Built | 10 criteria, Teacher/Admin/Student ICPs |
| C5 Content Enhancer | ✅ Built | Minor/high tiers, C4 delegation, all fix types |
| F1 Webflow Publisher | ✅ Built | REST API, FAQ extraction, guardrails, draft/live |
| brand-voice-guide.md | ✅ Real content | Imported from repo, canonical brand rules |
| product-context.md | ✅ Real content | Imported from repo, ICP profiles, product features |
| Webflow token | ✅ Wired | Token live, 30 collections confirmed, IDs mapped |
| D1/D2/D3 extensions | ✅ Done | Hard gates, platform flags, SEO metadata, routing |

**Full pipeline:** A1 → B2 → B3 → C3 → C4 → D1 → C5 → E1 → E2 → F1

**Pipeline runs in progress:** `aeo/runs/20260428-1058-critical-thinking-exercises/` + `aeo/runs/20260428-1058-rti/` (B3+C3+C4 outputs exist)

**Next action:** Run D1 on existing enriched drafts → E1 → E2 → F1 publish

---

### 3. Evaluation Agents (D1/D2/D3) + Calibration System
**Status:** Built & calibrated ✅

| Component | Status | Notes |
|---|---|---|
| AEO Scoring Rubric | ✅ v1.1 live | Empirically calibrated — 5 topics, 60 runs, delta analysis |
| D1 AEO Evaluator | ✅ Rebuilt | Aligned to rubric v1.1, 9 dims, correct weights, revision loop |
| D2 URL Evaluator | ✅ Built | 8 dims, no brief needed, tavily_extract, gap analysis output |
| D3 Competitor Gap | ✅ Built | Multi-URL comparison matrix, win conditions, feeds B3 brief |
| calibration.py | ✅ Live | 5 topics done; SERP step fixed (SEMrush key wired) |
| run_delta_analysis.py | ✅ Built | Standalone cross-topic delta → rubric-weight-proposal.md |
| ground_truth_check.py | ✅ Built | Monthly citation check vs D2 scores; drift detection |
| rubric_self_update.py | ✅ Built | Full loop: calibrate → delta → propose → Slack → human approves → apply |
| Ground truth cron | ✅ Registered | 1st Monday monthly, 09:00 UTC, posts to #way-mark |
| Rubric self-update cron | ✅ Registered | 2nd Monday monthly, 09:00 UTC, posts proposal to #way-mark |

**Calibration state:**
- 5 topics run (ChatGPT): formative assessment, retrieval practice, exit tickets, growth mindset, differentiated instruction
- 30 URLs in corpus: 10 GEO_GOLD + 20 non-cited
- Rubric v1.1 weights: Stats 17%, Uniqueness 16%, Trust 14%, QAPE 18%, Self-contain 14%, Structure 9%
- Gemini runs still pending (free tier quota — run when available)
- Calibration corpus v1.1 rerun: pending (validate <1.0 composite shift)

**P-006 gate (rubric self-update full auto):** Pending ≥20 published articles + BQ access

---

## Known Limitations
- **Multi-user task tracking:** PROJECT.md is a single shared file — doesn't track per-user asks. → See `BACKLOG.md`

## Decisions & Constraints
- AEO/GEO is primary content focus
- 3 ICPs: Teachers, Admins, Students
- All content must pass D1 evaluator before publishing
- Slack (#way-mark) is primary coordination channel

_Last updated: 2026-04-28_
