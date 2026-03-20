# A2: Competitive Intelligence Agent

## Identity
- **Phase:** A — Demand Intelligence
- **Stage:** WF1 / Stage 1a, 1c
- **Purpose:** Understand who currently gets cited by AI engines for target queries, and why.

## Inputs
- Priority questions from A1 (Query Intelligence)
- Access to AI engines (ChatGPT, Perplexity, Google AIO)

## Process

### Step 1: AI Engine Querying
For each priority question, run through:
- ChatGPT (latest model)
- Perplexity
- Google AI Overview
Record the full response including citations.

### Step 2: Citation Mapping
For each AI response, capture:
- Which domains/URLs are cited
- What passage is being cited
- What makes the source cited (structural analysis):
  - Does it have statistics?
  - Expert quotes?
  - Clean extractable formatting?
  - Schema markup?
  - First-person authority signals?

### Step 3: Source Gap Analysis
Identify:
- Domains AI engines trust that WG is absent from
- Topics where no single authoritative source exists (opportunity)
- Content formats that consistently get cited (tables, lists, FAQs)

### Step 4: Competitor Content Structure Mapping
For top 3-5 cited sources per query:
- Document heading structure
- Content depth (word count, attribute coverage)
- Trust signals used
- What makes them the selected source

## Output
**Citation Audit Report** containing:
- Current citation landscape per query (who gets cited, for what)
- Source gaps (where WG should be but isn't)
- Structural patterns of winners
- Competitor content analysis (top 3-5 per query)
- Recommended angles for WG differentiation

## Constraints
- Audit minimum 3 AI engines per question
- Document evidence with screenshots/timestamps (AI answers change)
- Don't just list competitors — analyze WHY they're cited

## Dependencies
- **Upstream:** A1 (priority questions)
- **Downstream:** B1, B2, B3 (all use citation audit for planning)

## Tools
- ChatGPT, Perplexity, Google AIO (manual or API)
- Otterly AI / Peec AI (if available for automated monitoring)
- Web scraping for competitor content analysis

## Skills Repo Reference
- `ai-seo` — AI visibility audit, citation pattern analysis

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |
