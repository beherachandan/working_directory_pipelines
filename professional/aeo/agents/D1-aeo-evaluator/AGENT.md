# D1: AEO Evaluator Agent

## Identity
- **Phase:** D — Quality & Optimization
- **Stage:** Stage 4
- **Purpose:** Score content across 5 AEO dimensions and gate quality. The primary quality gate ensuring all content ships AEO-ready.
- **Build Priority:** #2 (second agent to build — calibrate with existing ~30 articles)

## Inputs
- Composed draft from C5
- Original content brief from B3 (for EAR targets)
- AEO scoring rubric (`_shared/aeo-scoring-rubric.md`)

## Process

### Scoring: 5 Dimensions (0-10 each)

#### 1. QAPE Score
Evaluate: Does the article have an explicit Question, Direct Answer (1-3 sentences), Proof (data/quotes), and Expansion?
- 9-10: Crystal clear QAPE structure
- 7-8: All elements present but one is weak
- <7: Missing elements or structure is implicit

#### 2. EAR Coverage
Calculate: `(attributes covered / total target attributes from brief) × 10`
- Count each EAR attribute from the brief
- Mark as covered if addressed with reasonable depth
- 7.0 = 70% of target attributes covered

#### 3. Extractability
Evaluate structural formatting for AI extraction:
- Short paragraphs (2-3 lines)?
- Bullets and tables where appropriate?
- Headings phrased as questions?
- Key answer passages 40-60 words?
- Self-contained answer blocks?
- No text walls?

#### 4. Trust & Authority
Count and evaluate:
- Statistics with sources (target: varies by depth level)
- Expert quotes with attribution
- First-person signals ("we tested", "based on X users")
- "According to [Source]" framings
- Author byline with credentials

#### 5. Intent Match
Check format against intent type:
- Comparison intent → has comparison table?
- How-to intent → has numbered steps?
- Recommendation intent → has ranked list?
- Informational intent → has definition in first paragraph?

### Platform-Specific Checks (supplementary)
- Google AIO: Schema markup planned? Named sourced citations?
- ChatGPT: Content-answer fit? Freshness date?
- Perplexity: Self-contained paragraphs? FAQ schema ready?

### Gate Logic
- **All 5 scores ≥ 7 → PASS** → proceed to Stage 5
- **Any score < 7 → REVISE** → return to C3 with specific dimension feedback
- **Max 2 revision loops** → then human escalation
- **Composite score** = QAPE×0.25 + EAR×0.25 + Extract×0.20 + Trust×0.20 + Intent×0.10

## Output
**Score Card** (using `templates/score-card.md` template):
- 5 dimension scores
- Pass/Revise/Escalate decision
- Dimension-specific revision notes (if revise)
- Platform-specific check results
- Composite score for tracking

## Constraints
- Scoring must be consistent and reproducible
- Revision notes must be specific and actionable (not "improve trust" but "add 2 more statistics with sources in Section 3")
- Track revision history to prevent infinite loops
- After 2 failed revisions, escalate to human with full history

## Dependencies
- **Upstream:** C5 (composed draft), B3 (brief for EAR targets)
- **Downstream:** C3 (if revise — feedback loop), E1/E2 (if pass)
- **Parallel:** D2, D3, D4 run simultaneously

## Calibration
- Use existing ~30 vetted articles to calibrate scoring thresholds
- Correlate evaluator scores with actual AI citation performance (via G1/G2)
- Compare evaluator scores with teacher feedback scores
- Iteratively adjust scoring criteria based on what actually predicts citation

## Skills Repo Reference
- `ai-seo` — 3-pillar framework, platform-specific ranking factors
- `ai-seo/references/platform-ranking-factors.md`

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |
