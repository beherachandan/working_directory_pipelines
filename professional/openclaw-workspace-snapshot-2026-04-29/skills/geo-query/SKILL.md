---
name: geo-query
description: GEO query intelligence for Wayground. Use when querying AI platforms (ChatGPT via Azure OpenAI, Perplexity, Gemini) with a prompt and capturing the answer, cited sources, and whether Wayground appears. Core capability for AEO/GEO calibration, ground truth citation checks, signal drift detection, and competitive intelligence. Triggers on phrases like "check what AI cites", "run geo query", "what does perplexity cite", "check citation", "ground truth check", "which URLs get cited", "run calibration queries".
---

# geo-query — GEO Query Intelligence

> Query AI platforms with a prompt. Capture answer, cited sources, Wayground citation status.
> Powers: calibration corpus verification, monthly ground truth cron, signal drift detection.

## Role
Answer: **"Which URLs does each AI platform cite for this query — and is Wayground one of them?"**

## Inputs
- `query` — the search query/prompt to run (string)
- `platforms` — which platforms to query: `chatgpt`, `perplexity`, `gemini` (default: all configured)
- `variations` — number of query phrasings to run (default: 1, max: 5)
- `wayground_domain` — domain to check for in citations (default: `wayground.com`)

## Output
Per platform:
- `answer_snippet` — first 300 chars of AI answer
- `sources` — array of `{url, title, position}` cited
- `wayground_cited` — boolean
- `wayground_position` — position if cited, null if not
- `top_cited_domains` — domain frequency count across sources

## Platform Configuration

### ChatGPT (Azure OpenAI via Portkey) ✅ ACTIVE
- Provider: `@azure-openai-bbfaac`
- Model: `gpt-5` (or `gpt-5-mini` for faster runs)
- Web search: `web_search_preview` tool via Responses API
- Config: see `references/portkey-config.md`

### Perplexity ⚠️ NEEDS VIRTUAL KEY
- Provider: `@perplexity-ai/sonar`
- Citations: requires `strict-openai-compliance: false` header
- Config: needs Perplexity API key added to Portkey virtual keys
- Contact: add `PERPLEXITY_API_KEY` to Portkey dashboard → Virtual Keys

### Gemini ⚠️ NEEDS @ai-oncall
- Provider: `@google/gemini-2.0-flash-001`
- Grounding: `google_search` tool
- Config: needs @ai-oncall to provision access

## Execution — ChatGPT (Active)

Run `scripts/geo-query.js` with Node.js:

```bash
node scripts/geo-query.js \
  --query "what is retrieval practice" \
  --platforms chatgpt \
  --variations 1
```

Or for batch calibration corpus run:
```bash
node scripts/geo-query.js \
  --batch references/calibration-queries.json \
  --platforms chatgpt,perplexity \
  --output memory/research/geo-runs/YYYY-MM-DD-run.json
```

## Output Format

```json
{
  "query": "what is retrieval practice",
  "timestamp": "2026-04-22T14:30:00Z",
  "results": {
    "chatgpt": {
      "answer_snippet": "Retrieval practice is a learning strategy...",
      "sources": [
        {"url": "https://retrievalpractice.org/...", "title": "...", "position": 1},
        {"url": "https://cultofpedagogy.com/...", "title": "...", "position": 2}
      ],
      "wayground_cited": false,
      "wayground_position": null,
      "top_cited_domains": {
        "retrievalpractice.org": 2,
        "cultofpedagogy.com": 1
      }
    },
    "perplexity": { ... },
    "gemini": { ... }
  }
}
```

## Use Cases

### 1. Calibration Corpus Verification
Run all 10 target queries → verify which Tier 1 URLs are actually cited → pin empirical threshold.
```bash
node scripts/geo-query.js --batch references/calibration-queries.json --platforms chatgpt
```

### 2. Monthly Ground Truth Cron
Run top 10 Wayground URLs' target queries → check if Wayground cited → post delta to Slack.
Cron spec: `crons/ground-truth-check.md`

### 3. Competitive Intelligence
Run a query → see which competitors get cited → compare their D2 scores → identify gaps.

### 4. Signal Drift Detection
Run same query set monthly → track citation shift over time → flag rubric review if pattern changes.

## Dependencies
- Node.js (v22+) — already available
- `portkey-ai` npm package — install: `npm install portkey-ai`
- Portkey API key — see `references/portkey-config.md`
- Output stored in: `memory/research/geo-runs/`

## Related Files
- `scripts/geo-query.js` — executable script
- `references/portkey-config.md` — API config (keys stored as env vars)
- `references/calibration-queries.json` — the 10 target queries for corpus runs
- `crons/ground-truth-check.md` — monthly cron spec
- `memory/research/geo-runs/` — run outputs
