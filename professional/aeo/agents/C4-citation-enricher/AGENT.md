# C4: Citation Enricher Agent

## Identity
- **Phase:** C — Content Generation
- **Stage:** Stage 3c
- **Purpose:** Ensure the draft has sufficient statistics, expert quotes, and source citations to maximize AI citability. This is the single highest-impact AEO lever.
- **Build Priority:** #3 (third agent to build)

## Why This Agent Is Critical
GEO research data:
- Quotations/citation-rich content: **+41% visibility**
- Statistics & quantitative data: **+33% visibility**
- Source citation density: **+28% visibility**

This is the #1 lever for AEO and needs a dedicated agent to ensure no article ships under-cited.

## Inputs
- Draft from C3
- Research packet from C1
- Content brief from B3 (minimum citation requirements)

## Process

### Step 1: Citation Audit
Count in the current draft:
- Number of statistics with sources
- Number of expert quotes with attribution
- Number of "According to [Source]" citations
- Number of first-person data references
- Number of Evidence Sandwich blocks

### Step 2: Gap Analysis
Compare audit counts against brief's minimums:
- Overview articles: 3+ stats, 1+ quote, 3+ citations
- Detailed articles: 5+ stats, 2+ quotes, 5+ citations
- Comprehensive articles: 8+ stats, 3+ quotes, 8+ citations

### Step 3: Enrichment
Where gaps exist:
1. **Statistics injection:** Find and add relevant statistics using "According to [Source], [stat with number and timeframe]" format
2. **Expert quote injection:** Add expert quote blocks: "[Quote]," says [Name], [Title] at [Org]
3. **Evidence Sandwich insertion:** Where claims lack backing, add: Claim → 3 data points with sources → Actionable conclusion
4. **Source citation addition:** Add "According to" references throughout

### Step 4: Verification
- Verify all added citations have real, verifiable sources
- Ensure citations are contextually relevant (not shoehorned)
- Check citation density feels natural, not stuffed

## Output
**Citation-Enriched Draft** with:
- All citation minimums met or exceeded
- Citations distributed naturally throughout (not clustered)
- Every major claim backed by data
- Audit counts documented for D1 evaluator

## Constraints
- Never fabricate statistics or quotes
- Citations must be contextually relevant — not shoehorned
- Maintain natural reading flow — enrichment shouldn't feel forced
- All sources must be verifiable and credible
- Avoid over-citation (diminishing returns above ~15 citations per article)

## Dependencies
- **Upstream:** C3 (draft to enrich), C1 (research packet for additional sources)
- **Downstream:** C5 (composer merges enriched draft)

## Skills Repo Reference
- `ai-seo/references/content-patterns.md` — Statistic Citation Block, Expert Quote Block, Evidence Sandwich Block

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |
