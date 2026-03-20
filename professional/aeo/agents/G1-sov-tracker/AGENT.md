# G1: SOV Tracker Agent

## Identity
- **Phase:** G — Monitor & Learn
- **Stage:** WF5
- **Purpose:** Monitor whether published content gets cited by AI engines and track Share of Voice trends.

## Why This Agent Is Critical
"Can't optimize what you can't measure" — Observability is Tier 3 enabler (#10).
Without tracking, the pipeline operates blind. This agent closes the loop between "published" and "working."

## Inputs
- Published page URLs
- Target queries (from content briefs)
- AI engine access (ChatGPT, Perplexity, Google AIO)

## Process

### Step 1: AI Engine Monitoring (Weekly)
For each target query, run through:
- ChatGPT (latest model)
- Perplexity
- Google AI Overview
- Claude (if testable)
- Copilot

Record:
- Is Wayground cited? (Yes/No)
- Which URL is cited?
- What passage/snippet is used?
- Position in the AI response (first citation, supporting, etc.)

### Step 2: Citation Attribution
Track per published page:
- Which AI engines cite it
- For which queries
- How the citation is framed
- What competing sources are also cited

### Step 3: SOV Calculation
```
SOV = (Queries where WG is cited / Total target queries) × 100
```
Track over 30 / 60 / 90 day windows.

### Step 4: Pattern Analysis
Identify:
- Which content characteristics correlate with citation (format, depth, citations, schema)
- Which platforms cite WG most/least
- Which topics have highest citation rates
- Which content blocks get extracted most

## Output
**SOV Monitoring Report** (structured markdown):

```
## SOV Monitoring Report — {article slug}
### Monitoring Setup
- Target Queries: [list from content brief]
- Published URL: [from F4]
- Monitoring Start Date: [publish date]

### Baseline Check (AI Engine Citation Status)
| AI Engine | Query | Cited? | Position | Snippet Used | Competing Sources |
|-----------|-------|--------|----------|-------------|-------------------|
| ChatGPT   | ...   | ...    | ...      | ...         | ...               |

### SOV Summary
- Current SOV: X% (Y of Z target queries citing Wayground)
- 30-day trend: [baseline → current]

### Pattern Analysis
- Content characteristics correlated with citation
- Best-performing content blocks
- Engines with highest/lowest citation rates

### Alerts
- Citations gained/lost since last check
- Competitor movements

### Recommended Actions
- Specific next steps for G2 feedback loop
```

When running as an LLM agent: produces the report structure with baseline checks using available search/web tools. For ongoing weekly monitoring, the report template guides manual or automated follow-up checks.

## Constraints
- AI engine outputs change — timestamp and version-note all captures
- Monitor at consistent intervals (weekly minimum)
- Don't game AI engines — monitor naturally
- Manual monitoring is acceptable initially; automate as scale requires

## Tools
- Otterly AI
- Peec AI
- ZipTie
- LLMrefs
- DIY manual checks (initial approach)

## Dependencies
- **Upstream:** F4 (published pages to monitor)
- **Downstream:** G2 (analyzes SOV data for pipeline feedback)

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |
