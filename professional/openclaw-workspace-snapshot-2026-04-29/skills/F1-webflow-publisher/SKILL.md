---
name: F1-webflow-publisher
description: Publishes approved Wayground articles to Webflow CMS. Use after E2 ICP review PASS. Handles MD→HTML conversion, FAQ extraction, HTML guardrails, draft/live creation via REST API. Triggers on phrases like "publish this article", "push to Webflow", "run F1", "publish draft", "go live".
model: claude-sonnet-4-6
---

# F1 — Webflow Publisher

> Takes an E2-approved article markdown file and publishes it to Webflow CMS as a draft or live item.

## Role
Answer: **"Is this article now live (or staged as draft) in Webflow — with FAQs, metadata, and content all correctly created?"**

## Inputs
- `article_path` — path to article .md file relative to workspace (required)
- `collection` — Webflow collection slug (required — see reference below)
- `mode` — `"draft"` (default) or `"live"` (required explicit confirmation for live)
- `e2_verdict` — E2 ICP review verdict (required — must be ICP PASS before F1 runs)

## Pre-Flight Check (mandatory)

Before publishing:
- [ ] E2 verdict is **ICP PASS** — if not, stop and route back to E2/C5
- [ ] Article file exists at the given path
- [ ] Collection slug is valid (see reference/webflow-ids.md)
- [ ] Mode `"live"` requires **explicit human confirmation** — never go live silently

If mode is `"live"`:
> "This will publish the article live to wayground.com. Confirm?"
Wait for explicit yes before proceeding.

---

## Publishing Flow

### Step 1 — Continuity check (deterministic)
Run `continuity_checker.py` to verify the enhanced article hasn't lost content:

```bash
python3 skills/F1-webflow-publisher/scripts/continuity_checker.py \
  <original_draft_path> <enhanced_article_path>
```

- PASS → proceed
- WARN → note in report, proceed
- FAIL → stop, report to human

### Step 2 — Delta summary (deterministic)
If article went through C5 enhancement, run `delta_builder.py` to summarise what changed.
Output is included in the publication report.

### Step 3 — Publish (deterministic + API)
Run `webflow_publish.py`:

```bash
python3 skills/F1-webflow-publisher/scripts/webflow_publish.py \
  --article <article_path> \
  --collection <collection_slug> \
  --mode <draft|live>
```

The script handles:
- MD → HTML conversion via `markdown-to-webflow-html.py`
- FAQ extraction and FAQ item creation (FAQs collection first, then article)
- HTML guardrail checks (7 structural checks — blocks on FAIL)
- Content size check (>35KB → save to large_content/, create item without inline content)
- Article field data assembly
- REST API calls: POST items, PUT publish (if live)
- Publication report written to `aeo/outputs/publish/{slug}-report.md`

### Step 4 — Report to human
After script completes, post to Slack:

```
✅ Published: [Article Title]
Status: Draft 📝 / Live 🌐
Preview: [preview_url]
FAQs: [N] created
[⚠️ Large content — manual upload required] (if applicable)
Report: aeo/outputs/publish/{slug}-report.md
```

---

## Collection Reference

| Collection | Slug to use |
|---|---|
| Education Assessments | `education-assessment` |
| Generators | `generators` |
| Question Types | `question-types` |
| Lesson Plans | `lesson-plan` |
| Differentiated Learning | `differentiated-learning` |
| Scaffolding | `scaffolding` |
| Engagement | `engagement` |

Full IDs and category IDs: `skills/F1-webflow-publisher/references/webflow-ids.md`

---

## Error Handling

**HTML guardrail FAIL** → Stop. Report specific failure. Do not publish.
**Content > 35KB** → Create item without inline content. Save HTML to `aeo/outputs/publish/large_content/`. Note manual upload required in report.
**Slug conflict** → Do NOT append `-v2` or `-v3`. Read article angle, append most descriptive keyword (e.g. `diagnostic-assessment` → `diagnostic-assessment-tools`). Report the conflict and chosen slug.
**FAQ creation fails** → Log error + continue with remaining FAQs. Create article with partial FAQ list. Note in report.
**Collection not found** → Stop. Ask human which collection this article belongs to.

---

## Setup / Verification

To verify token and list all collections:
```bash
python3 skills/F1-webflow-publisher/scripts/webflow_publish.py --setup
```

---

## Files
- Script: `skills/F1-webflow-publisher/scripts/webflow_publish.py`
- Supporting: `markdown-to-webflow-html.py`, `continuity_checker.py`, `delta_builder.py`
- Reference: `skills/F1-webflow-publisher/references/webflow-ids.md`
- Reads: `aeo/context/product-context.md` (for Wayground data signals in report)
- Output: `aeo/outputs/publish/{slug}-report.md`
- Input from: E2 PASS output + article .md path
