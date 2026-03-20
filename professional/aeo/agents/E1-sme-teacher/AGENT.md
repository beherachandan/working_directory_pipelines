# E1: SME / Teacher Agent

## Identity
- **Phase:** E — Expert Review
- **Stage:** Stage 5
- **Purpose:** Validate pedagogical accuracy and educational expertise. This is the primary human gate in the pipeline.

## Inputs
- Quality-passed draft (all D-phase scores ≥ 7)
- Original content brief from B3
- Fact-check report from D2

## Process

### Step 5a: Accuracy Review
SME checks:
- Factual correctness of educational claims
- Pedagogical accuracy (are teaching methods described correctly?)
- Alignment with current curriculum standards where applicable
- Accuracy of tool/technology descriptions

### Step 5b: Voice/Tone Check
- Does it sound like a knowledgeable educator?
- Not a marketing bot? Not a textbook?
- Would a teacher share this with a colleague?
- Is the language accessible but not condescending?

### Step 5c: WG Product Alignment
- Are Wayground product mentions natural and value-adding?
- Do product references help the reader?
- No forced promotional language?

### Step 5d: Feedback Capture
Structured feedback form:
- Overall: Approved / Needs Revision
- Accuracy issues (specific, with corrections)
- Tone issues (specific passages)
- Missing context or nuance
- Suggestions for improvement

## Output
- **Approved** → proceed to Stage 6 (Publish)
- **Needs Revision** → return to C3 with structured feedback

## Human-in-the-Loop
This is NOT an automated agent — it coordinates human review:
- UXR team members
- Teacher network (~30 articles already through this loop)
- Subject matter experts for specialized topics

## Feedback Loop
Teacher feedback data feeds into:
- D1 evaluator calibration (what do teachers catch that the evaluator misses?)
- Brand voice guide updates
- Content brief template improvements

## Constraints
- Human review is mandatory — cannot be bypassed
- Feedback must be structured (not free-text only) for learning loop
- Reviewer must have relevant domain expertise

## Dependencies
- **Upstream:** D1 (must pass quality gate first)
- **Downstream:** C3 (if revision needed), F1-F4 (if approved)
- **Parallel:** E2 runs simultaneously

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |
