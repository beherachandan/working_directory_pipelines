---
name: slack-url-eval
description: Slack URL evaluation handler for Wayground. Use when a user shares a URL in Slack and asks to evaluate, summarize, review, or analyze it. Runs a structured content scan first, then offers D1 AEO scoring on confirmation. Always uses tavily_extract (advanced) — never web_fetch for article content.
---

# Slack URL Evaluator

> Handles "evaluate [URL]" and similar intents from Slack. Two-phase: scan first, D1 score only on user confirmation.

## Trigger Patterns

Activate this skill when a Slack message contains a URL **and** any of:
- `evaluate`, `review`, `analyse`, `analyze`, `summarize`, `summarise`, `score`, `check`, `how good is`, `what is this`
- Or a bare URL with no other text (default to scan)

## Phase 1 — Content Scan (always run first)

### Step 1: Extract content

Always use `tavily_extract` with `extract_depth: "advanced"`.

```
tool: tavily_extract
urls: [the URL]
extract_depth: "advanced"
query: "main content, key claims, structure, target audience"
chunks_per_source: 3
```

**If extraction returns empty or near-empty content:**
- Try once more with no query param
- If still empty, reply: "I couldn't extract readable content from that URL — it may require authentication or be blocked. Can you paste the article text directly?"
- Do NOT fall back to `web_fetch` and do NOT fabricate content

### Step 2: Build scan summary

From extracted content, produce this structured summary (Slack-formatted):

```
🔍 *Scan: [Page Title or URL]*

*What it is*
[1-2 sentences: content type, topic, format]

*Target audience*
[Who this is written for — be specific, e.g. "K-12 teachers looking for classroom management strategies"]

*Key claims / structure*
• [Main point or section 1]
• [Main point or section 2]
• [Main point or section 3]
• (up to 5 bullets max)

*Obvious gaps*
• [Something clearly missing or thin — no rubric, just common sense]
• [Another gap if present]
• (skip section entirely if nothing obvious)

---
Want me to score this against the AEO rubric? Reply *yes* or *score it*.
```

**Rules for scan output:**
- No scores, no numbers, no pass/fail in Phase 1
- Keep it tight — scan should read in under 30 seconds
- Obvious gaps = genuinely obvious (missing conclusion, no examples, wall of text) — not rubric gaps
- Reply in the **same Slack thread** as the original message

---

## Phase 2 — D1 Scoring (only on explicit user confirmation)

Trigger: user replies "yes", "score it", "go ahead", "score", "run D1", or similar affirmative in the same thread.

### Step 1: Load D1 rubric

Read: `skills/D1-aeo-evaluator/SKILL.md`

### Step 2: Adapt inputs

D1 was designed for pipeline-generated articles (with brief + EAR map). For URL evaluation, adapt as follows:

| D1 Input | Pipeline mode | URL eval mode |
|----------|--------------|---------------|
| `enriched_draft` | C4 output | Extracted content from Phase 1 |
| `content_brief` | B3 output | Infer intent from page title + content |
| `ear_map` | B2 output | Skip EAR Coverage dimension — mark as N/A with explanation |
| `scoring_rubric` | `aeo/context/aeo-scoring-rubric.md` | Same |

**EAR Coverage note:** EAR map requires knowing what the article *was supposed to cover* (from B2). Without that, you can't fairly score coverage gaps. Mark this dimension as `N/A — no brief available` and exclude it from composite score calculation. Be explicit about this in the scorecard.

### Step 3: Score remaining 4 dimensions

Score: QAPE, Extractability, Trust & Authority, Intent Match — exactly per D1 rubric.

### Step 4: Post scorecard

Use D1's scorecard output format. Adapt header:

```
# AEO Scorecard: [Page Title]
*Source:* [URL]
*Mode:* URL evaluation (no brief — EAR Coverage skipped)
*Composite Score:* [X.X]/10 (4 dimensions)
```

Reply in **same Slack thread**.

---

## Constraints

- Never use `web_fetch` for article content — always `tavily_extract` advanced
- Never fabricate content if extraction fails — ask for paste
- Never skip to D1 without user confirmation
- Always reply in the originating Slack thread
- D1 is the only scoring rubric — do not invent other scoring systems
- If the URL is not an article (e.g. a homepage, product page, login wall) — note that in the scan and skip the D1 offer unless it has substantive readable content
