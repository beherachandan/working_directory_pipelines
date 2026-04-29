# Ground Truth Check Cron
_Frequency: Monthly (1st Monday)_
_Purpose: Detect signal drift — check if D2 scores still predict AI citation_

## What It Does

1. Pull top 10 Wayground URLs by D2 score from `memory/research/scoring-runs/`
2. For each URL, run its target query via `geo-query.js` on Perplexity + ChatGPT
3. Record: URL | D2 score | cited Y/N | platform | position
4. Calculate score-to-citation correlation
5. Compare vs prior month delta
6. Post report to Slack #way-mark

## Trigger for Rubric Review

Any of:
- Citation rate drops >15% month-over-month for URLs scoring ≥75 (D2)
- Any URL scoring ≥80 not cited across 2+ platforms
- Any URL scoring <60 cited consistently (false negative)

## Run Command

```bash
export PORTKEY_API_KEY="..."
node ~/.openclaw/workspace/skills/geo-query/scripts/geo-query.js \
  --batch ~/.openclaw/workspace/memory/research/ground-truth-checks/queries-$(date +%Y-%m).json \
  --platforms chatgpt,perplexity \
  --output ~/.openclaw/workspace/memory/research/ground-truth-checks/$(date +%Y-%m)-check.json
```

## Output

Stored in `memory/research/ground-truth-checks/YYYY-MM-check.json`
Summary posted to Slack #way-mark.
