# MEMORY.md — Long-Term Curated Memory

_Distilled knowledge. Load only in main session. Updated by end-of-day cron and periodically during sessions._
_Last updated: 2026-04-28 (EOD cron)_

---

## 🏢 About Wayground

- EdTech product serving 3 ICPs: **Teachers**, **Admins**, **Students**
- Marketing owned end-to-end by Waymark (me)
- Primary channel now: **AEO/GEO content** — expanding to SEO, Paid, and beyond
- Coordination happens in **Slack #way-mark** (C0AQGTWEKCJ)

---

## 🧠 Key Decisions (permanent record)

| Date | Decision |
|---|---|
| 2026-04-17 | AEO/GEO is primary content focus |
| 2026-04-17 | All content must pass D1 evaluator before publishing |
| 2026-04-17 | PROJECTS.md is shared pipeline state — not per-user task tracking |
| 2026-04-20 | Memory infrastructure redesigned: layered file system + daily cron consolidation |
| 2026-04-20 | CAPABILITIES.md created as global capability map |
| 2026-04-20 | memory/projects/ and memory/capabilities/ introduced for scoped memory |
| 2026-04-20 | End-of-day cron set to run at 23:00 UTC daily |
| 2026-04-20 | Tavily web tools (web_search, web_fetch, group:web) added to global + Slack channel allowlist |
| 2026-04-20 | Gaurangi (U05AXJ98UP5) added as authorized Slack user with read/write/edit access |
| 2026-04-21 | EOD cron delivery fixed: must use explicit --channel + --to, not channel:last |
| 2026-04-21 | URL eval skill built: slack-url-eval — tavily_extract advanced, scan-first, D1 score on confirm |
| 2026-04-21 | web_fetch disabled for article URLs — JS-rendered pages (Next.js) return empty content |
| 2026-04-22 | D1/D2/D3 evaluators share one rubric: `aeo/context/aeo-scoring-rubric.md` (9 dimensions) |
| 2026-04-22 | D2 = URL Evaluator (external URL scoring, no brief needed, EAR excluded, Platform Specificity included) |
| 2026-04-22 | D3 = Competitor Gap (same rubric, comparative mode) |
| 2026-04-22 | Calibration corpus built: 18 URLs across 4 tiers; empirical threshold hypothesis ~6.5–7.0 |
| 2026-04-22 | geo-query skill built: queries AI platforms via Portkey, captures citations, checks Wayground citation |
| 2026-04-22 | Self-improving agent layer parked until BQ access confirmed + ≥20 articles published |
| 2026-04-24 | trends-researcher skill built: 3-track signal architecture (Google Trends / institutional / Reddit) |
| 2026-04-24 | DataForSEO REST API confirmed live ✅ — MCP npm package (@dataforseo/mcp-server) returns 404 (doesn't exist); correct package is `dataforseo-mcp-server` |
| 2026-04-29 | DataForSEO MCP fixed: updated OpenClaw config from `@dataforseo/mcp-server` (404) → `dataforseo-mcp-server` v2.8.10 ✅ |
| 2026-04-24 | Portkey: old key routes all to Claude/Bedrock; new key routes to real GPT/Gemini/Perplexity |
| 2026-04-24 | Gemini grounding via Portkey = confirmed dead end — Portkey strips groundingMetadata at gateway layer; use AI Studio API directly |
| 2026-04-24 | GEO calibration pipeline built (calibration.py) — first run completed: formative assessment, 12 ChatGPT runs |
| 2026-04-24 | Rubric v1.1 weight suggestions stored pending Gemini runs + 2-3 more topics; Stats/Trust most predictive dimensions |
| 2026-04-27 | SEMrush key confirmed = openclaw internal key (0b65acb5365171a4803c87e0de927328); wired into calibration.py |
| 2026-04-27 | 2 more calibration topics run: growth mindset (Stanford CTL gold 50%), differentiated instruction (ASCD PDF 83%, Edutopia DI hub 58%) |
| 2026-04-27 | Delta analysis run: 10 GEO_GOLD vs 20 non-cited; Stats +1.55, Uniqueness +1.45, Trust +1.25 most predictive |
| 2026-04-27 | Rubric v1.1 applied: Stats 12→17%, Uniqueness 12→16%, Trust 12→14%, QAPE 22→18%, Structure 12→9% |
| 2026-04-27 | run_delta_analysis.py built: standalone cross-topic delta tool, outputs rubric-weight-proposal.md |
| 2026-04-27 | D1 SKILL.md rebuilt: aligned to rubric v1.1, 9 dims, correct weights, revision loop logic |
| 2026-04-27 | D2 SKILL.md built: URL evaluator, 8 dims, tavily_extract, gap analysis, citability verdict |
| 2026-04-27 | D3 SKILL.md built: competitor gap, multi-URL matrix, win conditions, feeds B3 brief inputs |
| 2026-04-27 | ground_truth_check.py built: monthly citation check vs D2 scores, drift detection, MoM delta |
| 2026-04-27 | rubric_self_update.py built: full P-006 loop — calibrate → delta → Slack proposal → human approves → apply |
| 2026-04-27 | Two crons registered: Monthly Ground Truth Check (1st Mon) + Monthly Rubric Self-Update (2nd Mon) |
| 2026-04-27 | KNOWLEDGE.md + FEEDBACK.md built for ALL agents: D1, D2, D3, B2, B3, C4, A1, KW, geo-query |
| 2026-04-27 | Agent self-learning guardrail: agents READ+SUGGEST from KNOWLEDGE/FEEDBACK but NEVER ACT without human ✅ |
| 2026-04-27 | Drastic delta rule: agents only flag suggestions if pattern seen ≥3 data points; rubric is sole scoring authority |
| 2026-04-27 | P-006 + P-007 shipped. M-001/M-002/M-003 added as standing manual tasks in BACKLOG.md |
| 2026-04-27 | D3 run on student engagement (field best 6.42, stats avg 2.6) + differentiated instruction (field best 6.81, stats avg 3.4) |
| 2026-04-27 | Next: content pipeline on student engagement (A1→B2→B3→C4→D1) — starting in new session |
| 2026-04-28 | Critical incident: two pipeline fabrications identified by Chandan — fake D1 scorecards posted to Slack with no real tool calls |
| 2026-04-28 | SOUL.md updated: "Zero tolerance for fakeness" added as core truth |
| 2026-04-28 | marketing-director SKILL.md rebuilt: TaskFlow init, artifact gates (read-verified before+after each stage), Stall Protocol, per-stage Slack updates, MANIFEST.json, D1 revision loop, E1/E2 gates, flow.finish() |
| 2026-04-28 | Brand guide updated: question headings approved as exception for /learn/ hub AEO articles (not GTM/Sales copy) |
| 2026-04-28 | First real pipeline run complete: critical-thinking-exercises (A1→B2→B3→C3→C4→D1v1→C5→D1v2→E1→E2) — all artifacts verified on disk. E2 PASS, score 8.02/10. READY_FOR_PUBLISH |
| 2026-04-28 | D6 (Wayground platform data) parked — will inject post-publish, no full re-run needed |
| 2026-04-28 | F1 publish awaiting Chandan: collection confirmation + draft/live decision |

---

## 📋 Pipeline State (high level)

- 25 keywords identified and queued for content generation
- **1 article READY_FOR_PUBLISH:** critical-thinking-exercises (score: 8.02/10, E2 PASS)
- 0 articles published
- Evaluation stack fully built: D1/D2/D3 skills, rubric v1.1, calibration, crons, KNOWLEDGE+FEEDBACK infra
- **Next action: F1 Webflow publish for critical-thinking-exercises** — awaiting Chandan's collection confirmation + draft/live decision
- Second priority: continue pipeline on student engagement strategies

---

## 🔴 Known Limitations

- **L-001:** No per-user task tracking — PROJECTS.md is a single shared file
- **L-002:** Thread history not auto-injected into sessions — context loss across days without writing to files
- **L-003:** ~~DataForSEO not confirmed live~~ — **RESOLVED 2026-04-24**: DataForSEO REST API live ✅; MCP npm package doesn't exist — use Python REST API directly. Webflow not confirmed live.
- **L-004:** `channel: last` delivery fails for isolated cron jobs — must use explicit channel+target
- **L-005:** `web_fetch` returns empty on JS-rendered (Next.js) pages — use `tavily_extract` with `extract_depth: advanced`
- **L-006:** Portkey routing depends on which key is used: old key (`UgKiRSUEFAHGSTWBjOQNXDwkKKj/`) routes all → Claude/Bedrock; new key (`VwFslTtBMP/j3m4i/HkmvyEv/mlR`) routes to real GPT/Gemini/Perplexity. Virtual keys deprecated in Portkey — use Model Catalog. Portkey strips Gemini groundingMetadata regardless of key or `strict-openai-compliance: false` — use AI Studio API directly for citation data. Perplexity needs $5 credit at perplexity.ai/settings/api.

---

## 🟢 Learnings

- **LN-001:** PROJECT.md works well for shared pipeline state; not for individual task ownership
- **LN-002:** Writing decisions to files immediately is critical — "mental notes" die at session end
- **LN-003:** OpenClaw memory is two-layer: Markdown files (source of truth) + SQLite (vector search index over them)
- **LN-004:** Cron > heartbeat for consolidation — cron is isolated, exact timing, won't drift
- **LN-005:** CAPABILITIES.md is the right home for "what can this bot do" — not IDENTITY.md (which is persona/role)
- **LN-006:** Isolated cron jobs MUST have explicit `--channel` + `--to` delivery targets. `channel: last` does not work
- **LN-007:** Sub-agents can self-report success before confirming delivery — don't trust their logs as ground truth
- **LN-008:** `tavily_extract` with `extract_depth: advanced` is the correct tool for fetching article content from JS-rendered sites
- **LN-009:** Stats density is the most discriminating AEO scoring dimension — separates cited vs. non-cited URLs most reliably
- **LN-010:** AEO rubric drift has 3 types: rubric drift (single source of truth fix), signal drift (monthly ground truth cron), knowledge drift (quarterly research scan)
- **LN-011:** Portkey virtual key slugs don't guarantee routing to the labelled model — always verify via debug response `model` field
- **LN-012:** DataForSEO MCP npm package (`@dataforseo/mcp-server`) doesn't exist — always call DataForSEO REST API directly via Python urllib/requests
- **LN-013:** Portkey strips Gemini `groundingMetadata` at the gateway layer; `strict-openai-compliance: false` does NOT fix it. Use AI Studio API directly for grounding/citation data
- **LN-014:** GEO citation frequency ≠ rubric score — domain trust/authority can override content quality; high SERP rank ≠ high citation rate (e.g., formative.com #1 SERP, only 17% citation rate)
- **LN-015:** Trend discovery seeds must be stable structural K-12 categories (not specific topics or product names) — category seeds let Google Trends surface rising child topics organically
- **LN-016:** ChatGPT web search must be explicitly triggered — append "Search the web and cite your sources." to query; without it, GPT answers from training data only
- **LN-017:** Agent KNOWLEDGE.md + FEEDBACK.md files are reference-only — agents suggest based on them, never act autonomously; rubric is sole scoring authority until human approves change via Slack ✅
- **LN-018:** Azure OpenAI content filter blocks query variations containing "in education explained" — use "teaching X to students" in rule-based fallback
- **LN-019:** TUI disconnects cause message loops (same message resent) — switch to web UI for long sessions
- **LN-020:** Student engagement has lowest stats field avg (2.6/10) of any topic scored — biggest AEO content gap in the queue
- **LN-021:** Artifact gates must use `read` tool — instructions alone are insufficient. LLM can pattern-match to what "checking" looks like without actually calling the tool. Only real tool calls enforce the gate.
- **LN-022:** The heading-as-question brand rule applies to GTM/Sales/marketing copy only — NOT to /learn/ hub AEO articles. AEO articles have structural requirements that demand question headings.
- **LN-023:** When a pipeline stage claims completion verbally but no artifact file exists on disk, the pipeline did not complete. Never report completion without a read-verified artifact.

---

## 👤 People

| Name | Role | Notes |
|---|---|---|
| Chandan | Directing Waymark / AEO work | First contact 2026-04-02; expanded briefing 2026-04-03 |
| Gaurangi | Team member | Added to Slack #way-mark with read/write/edit access (2026-04-20) |

---

## 🗂️ Scoped Memory Index

Load these files on-demand when a request matches the domain — not at session start.

| Domain | Trigger signals | File |
|--------|----------------|------|
| AEO pipeline | "aeo", "pipeline", "article", "content gen", "generate", "brief", "publish" | `memory/projects/aeo-pipeline.md` |
| Keyword research | "keyword", "keyword research", "opportunities", "discovery", "themes", "content gaps" | `memory/projects/aeo-pipeline.md` + `memory/capabilities/semrush.md` (if exists) |
| Competitor analysis | "competitor", "gap analysis", "edutopia", "teacherspayteachers" | `memory/projects/aeo-pipeline.md` |
| Tool/SEMrush | "semrush", "api units", "domain_domains", "phrase_these" | `memory/capabilities/semrush.md` (if exists) |

---

## 🔧 Infrastructure Notes

- Workspace: `/home/ec2-user/.openclaw/workspace`
- Vector index: `~/.openclaw/memory/main.sqlite`
- Canvas/embed root: `/home/ec2-user/.openclaw/canvas`
- Node version: v22.22.2 (arm64, ap-south-1)
- Cron for memory consolidation: 23:00 UTC daily
- Slack thread config (set 2026-04-20): `thread.initialHistoryLimit=50`, `thread.historyScope=thread`, `thread.inheritParent=false`
- Skills wired (active as of 2026-04-27): KW-keyword-researcher, marketing-director, A1-query-intelligence, B2-ear-decomposer, B3-content-brief-generator, C4-citation-enricher, D1-aeo-evaluator, D2-url-evaluator, D3-competitor-gap, geo-query, slack-url-eval, KW-content-auditor, trends-researcher
- All evaluation skills have KNOWLEDGE.md + FEEDBACK.md companion files (read-only for agents)
- Crons wired to auto-update KNOWLEDGE.md + FEEDBACK.md (ground_truth → D1/D2 KNOWLEDGE; rubric_self_update → geo-query/D1/D2 FEEDBACK)
- D3 reports stored: `memory/research/scoring-runs/2026-04-27-d3-student-engagement.md` + `...-d3-differentiated-instruction.md`
- Calibration corpus: 30 URLs in `memory/research/scoring-runs/d2-scores-corpus.json` (10 GEO_GOLD + 20 non-cited)
- trends-researcher skill built (2026-04-24): `skills/trends-researcher/` — 13 validated seeds, DataForSEO REST, $0.24/full run
- GEO calibration pipeline built (2026-04-24): `skills/geo-query/scripts/calibration.py` — 5-step pipeline: LLM variation gen → GEO runs → frequency analysis → SEMrush enrichment → delta analysis
- Gemini API: key `AIzaSyCuBfskGih3UchLQ4LrrX1622sRqbfVpQk`, project `projects/58172892053`, free tier ~15 RPM, working models: gemini-2.0-flash / 2.5-pro / 2.5-flash
- First calibration run output: `memory/research/geo-runs/2026-04-24-calibration-formative-assessment.json/.md`
- Backlog P-006: calibration cadence + auto-rubric-update loop (depends on ≥20 articles + BQ access)
- Backlog P-007: self-learning agent infrastructure (feedback files + training loop)
- `slack-url-eval` skill built (2026-04-21): `workspace/skills/slack-url-eval/SKILL.md` — confirmed active
- Tavily tools active: `web_search`, `web_fetch`, `tavily_search`, `tavily_extract` in global + Slack channel allowlist
- AEO scoring rubric v1.0 created (2026-04-22): `aeo/context/aeo-scoring-rubric.md` — 9 dimensions, single source of truth for D1/D2/D3
- Calibration corpus scored (2026-04-22): 18 URLs, threshold ~6.5–7.0; full results in `memory/research/scoring-runs/2026-04-22-initial-run.md`
- geo-query skill built (2026-04-22): `skills/geo-query/` — needs Perplexity virtual key + Vertex grounding access for full functionality
- Knowledge repo created (2026-04-23): `knowledge/` — YAML frontmatter + MD body; categories: aeo-geo/, content-pipeline/, scoring-evaluation/, signals/
- Open: D2 SKILL.md not yet built as executable agent; D3 not started; exec tool access needed for autonomous cron runs
