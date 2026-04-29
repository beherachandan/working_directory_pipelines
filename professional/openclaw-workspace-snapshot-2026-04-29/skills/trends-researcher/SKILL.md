---
name: trends-researcher
description: Emerging education topic detector for Wayground. Runs three parallel signal tracks to surface rising K-12 topics before competitors: (1) seed-based trend analysis — stable education category seeds → DataForSEO adjacent topic expansion → MoM growth filtering, (2) upstream signals — policy filings, academic research, conference agendas, grant patterns via Tavily, (3) Reddit grassroots discourse — what teachers are actually discussing now. Merges all three tracks, validates with DataForSEO volume data, cross-references content index, and outputs prioritized first-mover opportunities. Triggers on phrases like "find emerging topics", "what's trending in education", "surface rising topics", "trends research", "emerging content opportunities", "what should we get ahead of", "first-mover content", "capture demand early".
---

# Trends Researcher — Emerging Education Topics

You are an emerging topic analyst for Wayground. Your job is to surface **K-12 education themes rising in real demand but not yet saturated** — giving Wayground a first-mover publishing window before competitors establish authority.

## Three Parallel Signal Tracks

| Track | Signal type | Primary tool | What it catches |
|---|---|---|---|
| **Track 1** | Seed-based trend expansion | DataForSEO | Child topics within stable categories showing MoM search growth |
| **Track 2** | Upstream institutional signals | Tavily | Policy, research, conferences, grants — topics forming before search volume exists |
| **Track 3** | Reddit grassroots discourse | Tavily | What teachers are actually adopting and discussing right now |

Run all three tracks independently. Merge outputs. Validate with DataForSEO volume data. Topics appearing across multiple tracks = highest confidence.

---

## What "Emerging" Means Here

- Volume: 50–3,000/mo (pre-saturation; keyword-researcher handles >3,000)
- Difficulty: < 45 (not yet entrenched)
- MoM growth: > 10% over last 3 months OR upstream signal present before volume forms
- Wayground coverage: none or weak

---

## Prerequisites

- `aeo/outputs/wayground-content-index.json` must exist — run KW-content-auditor if missing
- DataForSEO REST API: live ✅ (credentials in `~/.openclaw/openclaw.json` → `mcp.servers.dataforseo.env`)
- Tavily: live ✅

> **DataForSEO:** Use the `dataforseo__*` MCP tools directly in agent turns. The `fetch-google-trends.py` script uses direct REST (acceptable for `exec`-based runs); for any inline agent step, prefer MCP tools.

```bash
date +%Y-%m-%d  # set for output filenames
```

---

## Track 1: Seed-Based Trend Expansion

### Why category seeds, not topic seeds

Seeds must be **stable structural categories** of K-12 education — not specific topics. A topic seed like "phonemic awareness" only finds sub-themes of something already known. A category seed like "reading instruction" lets DataForSEO surface whatever is currently rising within that space — including topics you haven't thought of.

Categories don't change year to year. The topics within them do. That's the signal.

### Step 1a: Fetch Google Trends rising + top queries per seed

Load the 13 validated seeds from `references/signal-sources.md` → "Category Seeds".

Run the bundled script for both time windows:

```bash
# 90-day window (sustained growth signal)
python3 skills/trends-researcher/scripts/fetch-google-trends.py \
  --seeds-file skills/trends-researcher/scripts/trend-seeds.json \
  --time-range past_90_days \
  --output aeo/outputs/trends/raw-90d-YYYY-MM-DD.json

# 30-day window (breakout / recent spike detection)
python3 skills/trends-researcher/scripts/fetch-google-trends.py \
  --seeds-file skills/trends-researcher/scripts/trend-seeds.json \
  --time-range past_30_days \
  --output aeo/outputs/trends/raw-30d-YYYY-MM-DD.json
```

Expected cost: ~$0.12 per window (13 seeds × $0.009 each). Total Track 1: ~$0.24.

Each result object contains:
- **`rising`** — breakout queries gaining momentum (`value` = % increase; >5000% means near-zero base, treat cautiously)
- **`top`** — consistently high interest queries under that seed (relative index, ordered by volume)

### Step 1b: Noise filter

Drop queries where:
- Length > 80 chars (exam questions copied verbatim — confirmed noise pattern)
- Competitor brand or platform login
- News/political spike with no classroom content angle (e.g. "SEL controversy", "deepseek", "ai detector")
- Careers/jobs terms ("edtech jobs", "math solver")
- State-specific test names
- Clearly off-topic (e.g. "lidl near me" appearing under formative assessment)

See `references/signal-sources.md` → "Noise Filter".

Tag survivors with `source_seed` and `signal_type` (`top` or `rising`).

### Step 1c: Validate with DataForSEO Labs volume data

For the top 20–30 surviving queries from Step 1b, fetch actual search volume and MoM trend using the MCP tool:

```
dataforseo__dataforseo_labs_google_historical_keyword_data
  keywords: ["query1", "query2", ...]
  location_name: "United States"
  language_code: "en"
```

This returns `monthly_searches` (12-month array) for each keyword — use this to calculate MoM growth and confirm the Trends signal has real volumetric backing.

> **Batching:** Pass all 20–30 queries in a single tool call (max 700 keywords supported). Do not loop one keyword at a time.

### Step 1d: Calculate MoM growth

For every keyword with `monthly_searches` data:

```python
def calc_mom(monthly_searches: list) -> dict:
    # monthly_searches: [{"year": int, "month": int, "search_volume": int}, ...]
    vols = [m["search_volume"] for m in
            sorted(monthly_searches, key=lambda x: (x["year"], x["month"]))]

    if len(vols) < 4:
        return {"direction": "INSUFFICIENT_DATA", "mom_3m": None, "consecutive_growth": 0}

    recent = sum(vols[-3:]) / 3   # avg last 3 months
    prior  = sum(vols[-6:-3]) / 3  # avg prior 3 months

    if prior == 0:
        return {"direction": "INSUFFICIENT_DATA", "mom_3m": None, "consecutive_growth": 0}

    mom_3m = round((recent - prior) / prior * 100, 1)
    consecutive = sum(1 for i in range(len(vols)-3, len(vols)-1) if vols[i+1] > vols[i])

    if mom_3m > 20 and consecutive >= 2:   direction = "GROWING"
    elif mom_3m > 10:                       direction = "RISING"
    elif mom_3m < -15:                      direction = "DECLINING"
    else:                                   direction = "FLAT"

    return {"direction": direction, "mom_3m": mom_3m,
            "consecutive_growth": consecutive, "current_volume": vols[-1]}
```

**Keep:** `GROWING` or `RISING` only. Discard `FLAT` and `DECLINING`.

### Step 1d: Noise filter

See `references/signal-sources.md` → "Noise Filter". Remove: named individuals, state tests, competitor brands, jobs/careers, higher ed, corporate learning, calendar-driven seasonal queries.

**Track 1 output:** list of keywords with `mom_summary`, tagged `"track": "1_seed_expansion"`.

---

## Track 2: Upstream Institutional Signals

These sources are upstream of the entire content ecosystem — before competitors know, before search volume forms. Use Tavily with `time_range: "month"` throughout.

### Step 2a: Policy and regulatory signals

```
Search targets:
  - US Department of Education announcements site:ed.gov
  - State education agency policy updates "new requirement" OR "new framework" K-12
  - "ESSA" OR "IDEA" OR "Title I" new guidance 2025
  - Education legislation passed 2025 teachers classroom
```

Extract: named initiatives, frameworks, mandates, or requirements that teachers will need to understand and implement.

### Step 2b: Academic research publication

```
Search targets (include_domains: eric.ed.gov, rand.org, brookings.edu, learningpolicyinstitute.org):
  - new study OR research "classroom" OR "teachers" OR "K-12" 2025
  - "evidence-based" new approach teaching 2025
  - education research findings implications teachers
```

Extract: named methodologies, interventions, or practices from recent research that have practical classroom application.

### Step 2c: Conference agendas

```
Search targets:
  - ISTE 2025 conference sessions emerging topics
  - ASCD 2025 conference agenda new
  - NAESP OR NASSP 2025 sessions topics
  - SXSWedu 2025 topics sessions
```

Extract: session topic clusters — if 5+ sessions at a major conference cover a theme, that's a strong institutional signal.

### Step 2d: Grant funding patterns

```
Search targets:
  - "Department of Education" grant awarded 2025 teachers classroom
  - Gates Foundation education grant 2025
  - "Chan Zuckerberg" education initiative 2025
  - EdTech grant funded 2025 K-12
```

Extract: named initiatives or approaches receiving significant funding. Funded programs → curriculum → teacher training → search volume (6–18 month lag).

### Step 2e: Consolidate and normalize

From all Track 2 results, extract candidate topic names. Normalize each to a clean head term a teacher might search. Group overlapping signals (e.g. "structured literacy" appearing in both a policy mandate and a conference session cluster = strong signal).

For each candidate:
- Source types that mentioned it (policy / research / conference / grants)
- Recency (within 30 days vs 60 days)
- Whether it has a practical classroom angle (a teacher could write or search about this)

**Track 2 output:** list of candidate topics tagged `"track": "2_upstream"`, with source evidence.

---

## Track 3: Reddit Grassroots Discourse

Reddit surfaces bottom-up adoption — teachers talking about what they're *actually starting to use* in their classrooms right now, completely unseeded by any editorial agenda.

Use Tavily `tavily_search` with `time_range: "month"`.

### Step 3a: Adoption signals

```
site:reddit.com/r/Teachers "anyone else using"
site:reddit.com/r/Teachers "just started using" OR "recently started"
site:reddit.com/r/Teachers "changed how I teach" OR "game changer"
site:reddit.com/r/Teachers "has anyone tried"
site:reddit.com/r/TeacherTech new tool OR "started using"
```

### Step 3b: Problem signals (emerging needs without solutions yet)

```
site:reddit.com/r/Teachers "struggling with" OR "how do you handle"
site:reddit.com/r/Teachers "looking for a way to"
site:reddit.com/r/education "anyone have resources for"
```

Problem signals without good search results = content gap Wayground can own.

### Step 3c: Extract and normalize

From Reddit results, extract:
- Named tools, methods, or practices being discussed
- Problems being raised with no clear solution surfacing in the thread
- Normalize to clean head terms
- Note thread recency and engagement level (many replies = strong signal)

**Track 3 output:** list of candidate topics tagged `"track": "3_reddit"`, with source URLs and brief quote/context.

---

## Merge, Validate, and Cluster

### Merge all three tracks

Combine Track 1 keywords, Track 2 topics, Track 3 topics into a single candidate pool.

### Validate Track 2 and 3 topics with DataForSEO

For any topic from Track 2 or 3 that doesn't already have DataForSEO volume data (they won't — they weren't in the keyword ideas results), run a quick volume check:

Use the MCP tool to check volume:
```
dataforseo__dataforseo_labs_google_historical_keyword_data
  keywords: [<all Track 2 + Track 3 head terms>]
  location_name: "United States"
  language_code: "en"
```
Batch all Track 2+3 terms in one call. Check:
- Does any search volume exist at all?
- If yes, is `monthly_searches` trending up?
- If no volume exists yet → keep as `"stage": "pre_search"` (upstream signal, not yet searchable)

Pre-search topics are genuinely first-mover: publish now, own the SERP before volume forms.

### Cluster into themes

Group related candidates into coherent themes. One theme = one content opportunity.

**Signal confidence by track coverage:**

| Tracks present | Confidence |
|---|---|
| All three (1+2+3) | Very high — structural demand + institutional + grassroots |
| Track 1 + either 2 or 3 | High — volume-confirmed + upstream or grassroots |
| Track 2 + Track 3 | High — pre-search but both institutional and grassroots signal |
| Track 1 only | Medium — volume data but no discourse signal |
| Track 2 or 3 only | Monitor — single weak signal |

For each theme:
- `head_term` — canonical searchable phrase (A1 handoff key)
- `contributing_tracks` — which tracks surfaced it
- `dataforseo_summary` — volume, KD, MoM if available
- `stage` — `"forming"` (volume growing), `"pre_search"` (no volume yet), `"early"` (some volume, unclear trajectory)

---

## Cross-Reference Content Index

```python
import json
with open("aeo/outputs/wayground-content-index.json") as f:
    index = json.load(f)
topic_coverage = index.get("topic_coverage", {})
page_titles = [p.get("title", "").lower() for p in index.get("pages", [])]
```

For each theme, assess coverage: `none` / `weak` / `moderate` / `strong`.
Skip themes with `strong` coverage — keyword-researcher handles those.

---

## Score and Tier

| Tier | Criteria |
|---|---|
| `HIGH` | 2+ tracks + coverage none/weak + (MoM > 20% OR pre-search with strong upstream signal) |
| `MEDIUM` | 2 tracks OR 1 strong track + coverage none/weak + MoM > 10% |
| `MONITOR` | 1 weak track, volume unclear, or coverage moderate |

Trajectory:
- `ACCELERATING` — MoM > 30%, 3 consecutive growth months (Track 1 data)
- `GROWING` — MoM 15–30% (Track 1 data)
- `PRE_SEARCH` — upstream/Reddit signal only, no volume yet (publish now, own SERP early)
- `EMERGING` — Track 1 RISING + either Track 2 or 3 confirming

For each HIGH and MEDIUM theme, write a `suggested_angle`:
- What Wayground-specific angle does the product enable?
- What format wins (how-to, definition + examples, comparison, implementation guide)?
- What does the weak/absent existing coverage miss?

---

## Save Output

```python
import json, os
from datetime import datetime, timezone

os.makedirs("aeo/outputs/trends", exist_ok=True)
date_str = datetime.now().strftime("%Y-%m-%d")

report = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "tracks_run": ["seed_expansion", "upstream_signals", "reddit_discourse"],
    "category_seeds_used": 13,
    "total_raw_candidates": 0,   # fill in
    "after_noise_filter": 0,     # fill in
    "themes_identified": 0,      # fill in
    "emerging_themes": [
        # {
        #   "theme": "Structured Literacy for Upper Elementary",
        #   "head_term": "structured literacy activities",
        #   "urgency": "HIGH",
        #   "trajectory": "GROWING",
        #   "stage": "forming",
        #   "contributing_tracks": ["1_seed_expansion", "2_upstream"],
        #   "signal_confidence": "high",
        #   "dataforseo": {"current_volume": 320, "mom_3m_pct": 28.0, "keyword_difficulty": 31},
        #   "upstream_evidence": "ASCD 2025 conference — 6 sessions on structured literacy implementation",
        #   "reddit_evidence": null,
        #   "wayground_coverage": "none",
        #   "suggested_angle": "Structured literacy activity templates for grades 3–5"
        # }
    ]
}

with open(f"aeo/outputs/trends/emerging-topics-{date_str}.json", "w") as f:
    json.dump(report, f, indent=2)
```

---

## Post to Slack

Post to `C0AQGTWEKCJ` via `message` tool:

```
🔭 *Emerging Education Topics — [DATE]*
_Tracks: DataForSEO expansion + upstream signals + Reddit discourse_

🔴 *HIGH — First-mover window open:*
1. *[Theme]*
   `[head_term]` | Vol: ~[N]/mo (+[X]% MoM) | KD: [N] | Stage: [forming/pre-search]
   Tracks: [1+2 / 1+3 / all three] | Coverage: none
   Angle: "[suggested_angle]"

🟡 *MEDIUM — Publish within 30 days:*
...

⚪ *MONITOR:*
...

📊 [N] candidates → [N] themes | [N] HIGH / [N] MEDIUM / [N] MONITOR
💬 _Reply with numbers to run A1 on any theme._
```

---

## Handoff to A1

User selects theme → pass `head_term` as `topic_pillar` to A1 → A1 mines sub-themes, scores AEO opportunity, returns ranked article list.

---

## Error Handling

| Error | Action |
|---|---|
| DataForSEO unavailable | Run Tracks 2+3 only; skip Track 1; note reduced confidence |
| No `monthly_searches` returned | Use current volume only; mark trajectory `UNKNOWN` |
| Tavily returns no education results | Try alternate queries from `references/signal-sources.md` |
| Content index missing | STOP — run KW-content-auditor first |
| < 5 themes after all filters | Lower KD ceiling to 55, lower volume floor to 30 |

---

## Run Cadence

- **Monthly** — default
- **Weekly** — back-to-school (Aug–Sep), major policy announcement periods
- **On-demand** — when user asks "what should we get ahead of"
