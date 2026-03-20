# E1 Human Review — Instructions

## What to Review
1. **Article Draft** — the composed article (see C5 output in outputs/)
2. **Score Card** — D1's evaluation (see D1 output in outputs/)
3. **Content Brief** — original requirements (see B3 output in outputs/)

## How to Provide Feedback

Edit the file `e1-feedback.md` in this directory with:

1. **First line must be the decision:**
   - `DECISION: Approved` — article is ready for publishing pipeline
   - `DECISION: Needs Revision` — article needs changes (provide details below)

2. **If Needs Revision, add specific feedback:**
   - What sections need changes
   - What's factually incorrect
   - What's pedagogically unsound
   - What's missing from an educator's perspective

## Example Feedback File

```markdown
DECISION: Needs Revision

## Pedagogical Accuracy
- Section "What is formative assessment?" conflates formative and diagnostic assessment
- The example in Section 3 doesn't reflect real classroom practice

## Missing Perspectives
- No mention of informal formative assessment (observation, questioning)
- Needs practitioner voice — add a teacher quote about real implementation challenges

## Factual Issues
- The statistic about "80% of teachers" needs a more recent source
```

## After Review
Save `e1-feedback.md` and re-run the orchestrator. It will pick up where it left off.
