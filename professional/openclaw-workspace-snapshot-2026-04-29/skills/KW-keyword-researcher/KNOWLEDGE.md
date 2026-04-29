# KW Keyword Researcher — KNOWLEDGE.md
_Keyword opportunity patterns and field-level insights. Updated by research runs._
_Last updated: 2026-04-27_

---

## Current Opportunity Queue

22 keywords identified and queued (from 2026-04-17 run).
Full list: `aeo/outputs/discovery/opportunities.json`

**Highest AEO priority** (from D3 competitor analysis):
1. **Student engagement strategies** — field avg D2 5.67, stats field avg 2.6 (biggest gap)
2. **Differentiated instruction** — field avg D2 5.73, stats field avg 3.4

---

## Keyword → AEO Opportunity Scoring Logic

When selecting keywords for content generation, prioritise:
1. **Low field D2 avg** (<6.0) — competitors are weak, easier to dominate
2. **Low stats field avg** (<3.5) — biggest content gap, Wayground can win with stats alone
3. **GEO gold URL exists** — confirms AI is already citing on this topic (demand validated)
4. **No Wayground article exists** — true gap, not cannibalisation

Avoid:
- Topics where field best > 7.5 — very hard to beat without exceptional domain authority
- Topics where only academic PDFs are cited — Wayground can't replicate foundational research authority short-term

---

## SEMrush API Notes
- Key: `0b65acb5365171a4803c87e0de927328` (same as openclaw internal)
- `phrase_related` — semantically related terms (static, not trending)
- `url_organic` — rank + volume for a specific URL on topic keywords
- Use DataForSEO REST API for Google Trends (rising/trending queries)
