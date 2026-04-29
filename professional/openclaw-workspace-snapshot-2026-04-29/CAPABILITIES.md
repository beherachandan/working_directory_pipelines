# CAPABILITIES.md — What Waymark Can & Cannot Do

_Operational reference. Always loaded. Updated when capabilities genuinely change — not every session._
_Last updated: 2026-04-20_

---

## ✅ Active Capabilities

### Content & AEO Pipeline
- Keyword research & opportunity discovery (SEMrush, DataForSEO)
- Query intelligence — mine sub-themes, score AEO opportunity (A1)
- EAR decomposition — entities, attributes, relationships for a topic (B2)
- Content brief generation (B3)
- Full article drafting (C3/C4)
- Citation enrichment with real stats, quotes, sources (C4)
- AEO quality scoring — 5-dimension evaluator, pass/fail/escalate (D1)
- Content publishing to Webflow
- Sitemap management (UGC-led)

### Research & Intelligence
- Competitor analysis (SEMrush organic/backlink/overview)
- Domain overview, keyword gap analysis
- Site audit (technical SEO)
- Position tracking
- Traffic analytics (SEMrush Trends)
- Web search (Brave/Tavily)
- **URL evaluation from Slack** — scan + optional D1 scoring (see `slack-url-eval` skill)

### Integrations (confirmed live)
- **SEMrush** — keyword research, organic, backlink, overview, audit, tracking, trends
- **Slack** — read/post to #way-mark (channel ID: C0AQGTWEKCJ)
- **File system** — full read/write to workspace

### Memory & Persistence
- Daily session logs (`memory/YYYY-MM-DD.md`)
- Long-term curated memory (`MEMORY.md`)
- Project state (`PROJECTS.md`)
- Per-project memory (`memory/projects/*.md`)
- Per-capability notes (`memory/capabilities/*.md`)
- Semantic search via sqlite vector index (`~/.openclaw/memory/main.sqlite`)

### Scheduling
- Cron jobs (exact timing, isolated sub-agent)
- Heartbeat checks (periodic, main session)

---

## ❌ Not Currently Capable

| Capability | Status | Notes |
|---|---|---|
| DataForSEO direct API | Live ✅ | Available via `bundle-mcp` allowlist group — same as SEMrush |
| GEO APIs | Not configured | On roadmap |
| Webflow API | Not confirmed live | Publishing referenced but untested |
| Per-user task tracking | Not implemented | Single shared PROJECTS.md (L-001) |
| Paid/PPC campaign management | Not started | On roadmap |
| Email / social posting | Not configured | — |
| Thread history injection (Slack) | Not configured | Context lost across days without it |
| URL eval from Slack — `web_fetch` fallback | **Disabled by design** | Always use `tavily_extract` (advanced) for article URLs — `web_fetch` fails on JS-rendered pages |

---

## 🧠 ICPs Served

| ICP | Notes |
|---|---|
| Teachers | Primary — classroom management, lesson planning, assessment |
| Admins | School/district administrators |
| Students | Secondary — learning tools, study aids |

---

## 📋 Constraints & Rules

- All content must pass D1 evaluator before publishing
- n > 10 articles per pipeline run → reject with message
- AEO/GEO is the primary content focus now; SEO/Paid expanding later
- #way-mark is the primary coordination and output channel
- Never send half-baked replies to messaging surfaces
- Private data stays private — no exfiltration

---

## 🔧 Skills Installed

| Skill | Purpose |
|---|---|
| `marketing-director` | Master router — entry point for all content/marketing work |
| `keyword-researcher` (KW) | Autonomous content opportunity discovery |
| `trends-researcher` | Emerging topic detection via competitor velocity + web signals |
| `KW-content-auditor` | Crawl & index existing Wayground content |
| `A1-query-intelligence` | Theme mining & AEO opportunity scoring |
| `B2-ear-decomposer` | Entity/attribute/relationship decomposition |
| `B3-content-brief-generator` | Structured content brief from EAR map |
| `C4-citation-enricher` | Real citations, stats, quotes injection |
| `D1-aeo-evaluator` | AEO quality gate — score, pass/revise/escalate |
| `taskflow` | Durable multi-step background job orchestration |
| `slack` | Slack read/post control |
| `healthcheck` | Security hardening & risk posture |
| `skill-creator` | Create/edit/audit AgentSkills |
| `clawhub` | Install/update skills from clawhub.com |
| `weather` | Weather forecasts |
| `tavily` | Deep web search & content extraction |
| `slack-url-eval` | Slack URL scan + D1 scoring handler |
