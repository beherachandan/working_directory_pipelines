You are an agent in the Wayground AEO (AI Engine Optimization) Content Engine — a pipeline that produces educational articles optimized for AI citation.

## Core Formula
**Citations × Trust = Share of Voice (SOV)**

## Your Operating Rules

1. **Structured Output:** Wrap your final output in `<output>` tags. Everything outside these tags is treated as scratchpad/reasoning and will not be passed downstream.

2. **Markdown Format:** All output must be well-formatted markdown. Use tables, bullets, headings as appropriate.

3. **Template Compliance:** If a template is provided, fill every field. Use `[NOT AVAILABLE]` for fields you genuinely cannot complete — never leave fields blank or skip them.

4. **Evidence-Based:** Never fabricate statistics, quotes, sources, or data. If you cannot find real data, say so explicitly rather than inventing it.

5. **Wayground Context:** You are producing content for Wayground (formerly Quizizz), an education platform with 200M+ resources. Content lives under `/learn/` and targets US educators (K-12). Always use "Wayground" — never "Quizizz."

6. **Brand Voice:** Sound like a knowledgeable teaching colleague — warm, authoritative, clear. Never sound like a marketing bot. Max 2-3 product mentions per article, always value-adding.

7. **AEO Best Practices:**
   - Short paragraphs (2-3 sentences)
   - Question-phrased headings
   - Key answer passages: 40-60 words (optimal for AI snippet extraction)
   - Statistics with "According to [Source]" framing
   - Expert quotes with full attribution
   - No walls of text, no keyword stuffing, no filler phrases

8. **Upstream Trust:** Treat upstream agent outputs as working material. Build on them, but flag contradictions or quality issues rather than silently propagating errors.

---
## Shared Context

### product-context
# Wayground — Product Context

> All agents in the AEO engine read this file. Keep it current.

## Company
- **Name:** Wayground (formerly Quizizz — rebranded)
- **Product:** Education platform with 200M+ total resources
- **Core offering:** Interactive learning tools — quizzes, lessons, worksheets, flashcards, game-based activities
- **Target market:** US (primary), expanding globally
- **Users:** Teachers (K-12), students, school administrators, district-level buyers
- **Revenue model:** Freemium — free tier for teachers, paid plans for schools/districts

## Key Positioning
- Wayground is a **comprehensive learning platform**, not just a quiz tool
- Differentiation: breadth of resource types, ease of use, gamification, teacher community
- Competitors: Kahoot, Blooket, Edpuzzle, Nearpod, Quizlet, Gimkit

## Content Domain
- All AEO content focuses on **education topics**: pedagogy, assessment types, teaching strategies, classroom management, edtech tools, curriculum design
- Content lives under `/learn/` hub structure (e.g., `/learn/assessments/formative`)
- Content should position Wayground as a knowledgeable, helpful resource for educators — NOT a sales channel

## Internal Asset Types
- **Activity Detail Pages (ADPs):** Individual resource pages (quizzes, lessons)
- **Resource Library pages:** Searchable collections by subject/grade/type
- **Learn hub pages:** Educational content organized by topic (`/learn/`)
- **Product pages:** Feature-specific pages (e.g., /features/quizzes)

## E-E-A-T Signals
- Author pages with credentials and social profiles
- Teacher network providing SME vetting (~30 articles through review loop)
- UXR team for user research backing
- "Based on X users" and "we tested" first-person authority signals

---
## Your Agent Definition

# G2: Feedback Analyst Agent

## Identity
- **Phase:** G — Monitor & Learn
- **Stage:** WF5 → WF1 (feedback loop)
- **Purpose:** Close the loop — feed learnings from monitoring and reviews back into the pipeline for continuous improvement.

## Inputs
- SOV data from G1
- Teacher feedback from E1
- Performance metrics (page views, time on page, bounce rate)
- D1 evaluator scores for published articles

## Process

### Step 1: Evaluator Calibration
Correlate D1 AEO evaluator scores with actual citation performance:
- Which score dimensions best predict actual citation?
- Are the thresholds (≥7 to pass) correctly calibrated?
- Do articles scoring 9-10 get cited more than 7-8?
- Recommend threshold adjustments

### Step 2: Topic Gap Discovery
From SOV monitoring data:
- Identify queries where WG isn't cited but should be
- Identify new topic opportunities from trending AI queries
- Flag topics where content exists but isn't getting cited (needs revision)

### Step 3: Teacher Feedback Integration
From E1 feedback:
- What patterns do teachers consistently flag?
- Feed structured feedback into LLM evaluator training
- Update content brief templates based on recurring feedback

### Step 4: Content Pattern Analysis
Identify which content characteristics predict citation:
- Content block types that get extracted most
- Optimal article length per intent type
- Citation density sweet spots
- Schema types that correlate with citations

### Step 5: Pipeline Improvement Recommendations
Produce actionable recommendations:
- Evaluator threshold adjustments
- Brief template updates
- New agent instructions based on learned patterns
- Process bottleneck identification

## Output
**Pipeline Improvement Report** (structured markdown):

```
## Pipeline Improvement Report — {date}

### 1. Evaluator Calibration
- Current threshold accuracy: X% (articles that PASS D-gate and get cited)
- Recommended threshold adjustments: [specific dimension → new threshold]
- Dimensions that best predict citation: [ranked list]

### 2. New Topic Opportunities
| Query | Volume | Current SOV | Gap Type | Priority |
|-------|--------|-------------|----------|----------|
| ...   | ...    | ...         | ...      | ...      |

### 3. Content Revision Priorities
- Pages published but not cited: [list with likely reasons]
- Recommended revisions: [specific, actionable changes]

### 4. Content Pattern Insights
- Content blocks most frequently extracted by AI engines
- Optimal article length by intent type
- Citation density findings

### 5. Process Improvements
- Pipeline bottlenecks identified
- Agent instruction updates recommended
- Brief template changes suggested
```

This report feeds directly into the next pipeline cycle: new topics → A1, brief updates → B3, threshold changes → D1.

## Feedback Loops
```
G2 → A1: New topic opportunities from query gaps
G2 → B3: Brief template improvements from patterns
G2 → D1: Evaluator threshold calibration
G2 → C3: Writing pattern insights (what gets cited)
G2 → _shared/: Updated rubric, voice guide based on learnings
```

## Constraints
- Recommendations must be data-backed, not anecdotal
- Minimum 30-day observation window before drawing conclusions
- Correlation ≠ causation — flag when evidence is suggestive vs. strong
- Don't recommend changes that would break the pipeline — propose, then test

## Dependencies
- **Upstream:** G1 (SOV data), E1 (teacher feedback), D1 (evaluator scores)
- **Downstream:** A1 (new topics), B3 (brief improvements), D1 (calibration)

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |

---
## Task Payload

**Topic:** How to use exit tickets in the classroom

### Upstream Agent Outputs

#### G1 Output
# SOV Monitoring Report — exit-tickets

**Article:** How to Use Exit Tickets in the Classroom  
**Status:** PRE-PUBLISH BASELINE SETUP  
**Report Date:** 2026-03-18  
**Next Action:** Execute baseline check on 2026-03-25 (7 days post-publish)

---

## Monitoring Setup

### Article Details
- **Target URL:** `https://wayground.com/learn/assessment/exit-tickets`
- **Expected Publish Date:** 2026-03-18 (pending manual deployment)
- **Monitoring Start Date:** 2026-03-25 (allows 7 days for indexing)
- **Article Status:** Content ready, awaiting CMS implementation

### Target Queries

**Primary Query:**
1. "How to use exit tickets in the classroom"

**Variant Queries (recommended for comprehensive SOV tracking):**
2. "What are exit tickets in teaching"
3. "Exit ticket examples for teachers"
4. "How do exit tickets work"
5. "Exit tickets vs entrance tickets"
6. "Best exit ticket strategies"
7. "Digital exit tickets for classroom"
8. "Exit ticket questions examples"

**Total Queries to Monitor:** 8 (1 primary + 7 variants)

### AI Engines to Monitor

| AI Engine | Model/Version | Monitoring Method | Check Frequency |
|-----------|---------------|-------------------|-----------------|
| ChatGPT | Latest (GPT-4+) | Manual query or API | Weekly |
| Perplexity | Default search | Manual query | Weekly |
| Google AI Overview | Google Search (AIO feature) | Manual search | Weekly |
| Claude | Latest (Claude 3+) | Manual query | Weekly |
| Microsoft Copilot | Bing integration | Manual query | Weekly |

### Citation-Optimized Features (To Track)

**Content Characteristics:**
- ✅ 52-word direct answer (QAPE structure)
- ✅ 6 FAQ items with FAQPage schema
- ✅ 5-step HowTo with HowTo schema
- ✅ 7 sourced statistics with "According to" framing
- ✅ Article schema with author attribution
- ✅ BreadcrumbList schema

**Technical Signals:**
- Schema markup: 4 JSON-LD blocks (Article, FAQPage, HowTo, BreadcrumbList)
- Page speed target: <2 seconds LCP
- Mobile-friendly: Yes
- Internal links: 7 contextual links
- Backlinks: 6 planned (4 high-priority)

---

## Baseline Check (AI Engine Citation Status)

**Status:** ⚠️ PENDING — Article not yet published

**Execute baseline check on 2026-03-25** using this table:

| AI Engine | Query | Cited? | Position | Snippet Used | Competing Sources | Notes |
|-----------|-------|--------|----------|---------------|-------------------|-------|
| ChatGPT | "How to use exit tickets in the classroom" | [CHECK] | [RECORD] | [EXTRACT] | [LIST] | [TIMESTAMP] |
| Perplexity | "How to use exit tickets in the classroom" | [CHECK] | [RECORD] | [EXTRACT] | [LIST] | [TIMESTAMP] |
| Google AIO | "How to use exit tickets in the classroom" | [CHECK] | [RECORD] | [EXTRACT] | [LIST] | [TIMESTAMP] |
| Claude | "How to use exit tickets in the classroom" | [CHECK] | [RECORD] | [EXTRACT] | [LIST] | [TIMESTAMP] |
| Copilot | "How to use exit tickets in the classroom" | [CHECK] | [RECORD] | [EXTRACT] | [LIST] | [TIMESTAMP] |

**Baseline Check Instructions:**
1. Verify page is live at target URL
2. Verify page appears in Google Search Console (indexed status)
3. Run primary query through each AI engine
4. Record: citation status (Yes/No), position in response (first/supporting/not cited), exact snippet used, competing sources also cited
5. Screenshot responses for reference
6. Document AI engine version/model used
7. Note response timestamp (AI outputs change over time)

---

## SOV Summary

**Status:** PRE-BASELINE — Cannot calculate until baseline check complete

### SOV Calculation Formula
```
SOV = (Queries where Wayground is cited / Total target queries) × 100
```

**Baseline SOV Target:**
- Primary query: Aim for 40%+ citation rate (2+ engines citing Wayground)
- All 8 queries: Aim for 25%+ SOV (10+ citations across 40 total query×engine combinations)

### Tracking Windows
- **Week 1 (Baseline):** 2026-03-25 baseline check
- **30-day:** 2026-04-18 (compare vs. baseline)
- **60-day:** 2026-05-18 (trend analysis)
- **90-day:** 2026-06-18 (performance review)

---

## Pattern Analysis Framework

**To Execute After Baseline + Week 4:**

### Content Characteristics to Track

**Which content blocks get cited most?**
- [ ] Direct answer block (52-word QAPE)
- [ ] FAQ answers
- [ ] HowTo steps
- [ ] Example questions table
- [ ] Decision framework table
- [ ] Statistics with attribution

**Which schema types correlate with citations?**
- [ ] Article schema → cited by which engines?
- [ ] FAQPage schema → FAQ featured in responses?
- [ ] HowTo schema → step-by-step snippets used?

**Which queries perform best?**
- Track citation rate by query type:
  - How-to queries ("How to...")
  - Definition queries ("What are...")
  - Example queries ("...examples...")
  - Comparison queries ("...vs...")

### Platform Analysis

**Engine-specific performance:**
- Which engines cite Wayground most/least?
- Which engines prefer FAQ format vs. HowTo?
- Which engines excerpt statistics vs. procedural steps?

### Competitive Intelligence

**Competing sources to track:**
- Edutopia
- TeachThought
- Cult of Pedagogy
- ASCD
- Education Week
- University teaching centers (.edu domains)
- Reddit (r/Teachers)

**Questions to answer:**
- Why do competing sources get cited when Wayground doesn't?
- What content formats do they use?
- What citation signals are stronger?

---

## Alerts & Monitoring Rules

### Week 1-2 (Post-Publish)
- **Daily:** Check Google Search Console for indexing status
- **Alert:** If page not indexed after 3 days → escalate to F4 (check sitemap, robots.txt, GSC errors)
- **Alert:** If rich results not showing after 7 days → validate schema with Rich Results Test

### Week 3-4
- **Weekly:** Run baseline + follow-up checks
- **Alert:** If 0 citations after 14 days → review competing results, check if snippet-worthy content is above fold
- **Alert:** If cited but wrong passage used → signals direct answer block needs optimization

### Month 2-3
- **Bi-weekly:** Track SOV trends
- **Alert:** SOV declining → investigate competing content updates, Google algorithm changes, or technical issues
- **Alert:** One engine stops citing → check if that engine changed crawling rules or Wayground was blocked

---

## Recommended Actions

### Pre-Publish (Complete Before Monitoring Starts)
1. ✅ **Verify article deployed** at `https://wayground.com/learn/assessment/exit-tickets`
2. ✅ **Confirm schema valid** using Google Rich Results Test (should show HowTo + FAQPage eligible)
3. ✅ **Check GSC indexing** — page must be indexed before monitoring begins
4. ✅ **Verify robots.txt** — GPTBot, PerplexityBot, ClaudeBot, Google-Extended, Bingbot all ALLOWED
5. ✅ **Implement backlinks** — at least 4 high-priority backlinks from F3 spec (knowledge graph signal)
6. ✅ **Test page speed** — must be <2 seconds LCP (Copilot citation threshold)

### Week 1 Post-Publish (2026-03-25)
1. **Execute baseline check** using table above
2. **Document competing sources** that rank for target query
3. **Screenshot AI responses** for historical reference
4. **Calculate baseline SOV** across all 8 queries

### Week 2-4
1. **Run weekly checks** on same day/time to control for variability
2. **Compare citation rates** week-over-week
3. **Identify patterns** — which content blocks get extracted most
4. **Adjust content if needed** — optimize direct answer if not being cited

### Month 2+
1. **Generate G2 feedback** — pass learnings to G2 agent for pipeline optimization
2. **Update monitoring queries** if new keyword opportunities emerge
3. **Track competing content** — if competitors update their content, re-baseline
4. **Scale monitoring** — automate with tools like Otterly AI, Peec AI, ZipTie, or LLMrefs

---

## Tools & Resources

### Manual Monitoring (Initial Approach)
- ChatGPT web interface or API
- Perplexity.ai search
- Google Search (check for AI Overview feature)
- Claude web interface
- Microsoft Copilot / Bing Chat

### Automated Monitoring (Future Scale)
- **Otterly AI** — tracks AI engine citations and rankings
- **Peec AI** — monitors AI-generated content performance
- **ZipTie** — AI search visibility tracking
- **LLMrefs** — citation tracking across LLMs

### Validation Tools
- Google Rich Results Test: https://search.google.com/test/rich-results
- Google Search Console: https://search.google.com/search-console
- PageSpeed Insights: https://pagespeed.web.dev/

---

## Dependencies & Handoff

### Upstream Dependency (F4)
- ⚠️ **BLOCKER:** Article must be manually deployed before monitoring can begin
- Required: All items in F4 "Go-Live Checklist Summary" completed
- Required: Page indexed in Google Search Console
- Recommended: 7-day wait post-publish for stable baseline

### Downstream Handoff (G2)
- **Timeline:** After 30-day data collection (by 2026-04-25)
- **Data to Pass:**
  - SOV performance by query and engine
  - Content blocks with highest citation rates
  - Competing sources analysis
  - Schema effectiveness (which types drive citations)
  - Recommendations for pipeline optimization

### Cross-Phase Dependencies
- **F3 backlinks** must be implemented for knowledge graph authority signals
- **F5 distribution** (social, email) may boost early visibility and indirect citation signals
- **D1 quality score** predicted high citation potential — monitor if prediction holds

---

## Monitoring Schedule Summary

| Timeline | Action | Owner | Status |
|----------|--------|-------|--------|
| **2026-03-18** | Article prepared, awaiting deployment | F4 Agent | ✅ Complete |
| **2026-03-18-24** | Manual CMS deployment + QA | Dev/Content Team | ⚠️ Pending |
| **2026-03-25** | Execute baseline check (Day 7 post-publish) | G1 Agent | 🔜 Scheduled |
| **2026-04-01** | Week 2 check | G1 Agent | 🔜 Scheduled |
| **2026-04-08** | Week 3 check | G1 Agent | 🔜 Scheduled |
| **2026-04-15** | Week 4 check | G1 Agent | 🔜 Scheduled |
| **2026-04-18** | 30-day SOV review | G1 Agent | 🔜 Scheduled |
| **2026-04-25** | Generate G2 feedback report | G1 → G2 | 🔜 Scheduled |
| **2026-05-18** | 60-day trend analysis | G1 Agent | 🔜 Scheduled |
| **2026-06-18** | 90-day performance review | G1 Agent | 🔜 Scheduled |

---

## Success Metrics

### Primary KPIs
- **Baseline SOV:** Target ≥25% (10+ citations across 40 query×engine combinations)
- **Primary Query SOV:** Target ≥40% (2+ of 5 engines citing Wayground)
- **Rich Results:** FAQPage or HowTo appearing in Google within 14 days
- **30-Day SOV Growth:** Target +10 percentage points vs. baseline
- **Citation Diversity:** Cited by ≥3 different AI engines

### Secondary KPIs
- Specific content blocks cited (direct answer, FAQ, HowTo steps)
- Position in AI responses (first citation = highest value)
- Competing source count (fewer competitors = higher authority)
- Citation stability (same engines citing week-over-week = trust signal)

---

## Report Status

**Overall Status:** ✅ MONITORING FRAMEWORK COMPLETE — Ready to execute baseline check once article is live

**Next Immediate Action:** Wait for F4 deployment completion, then execute baseline check on 2026-03-25

**Blockers:**
1. Article not yet published (F4 manual deployment pending)
2. Cannot execute baseline check until 7 days post-publish (indexing + citation lag)

**Estimated Time to First Data:** 7-10 days post-publish  
**First SOV Report:** 2026-03-25 (baseline) + 2026-04-18 (30-day comparison)

---

**Monitoring Framework Established**  
This report provides the complete structure for tracking whether Wayground's exit tickets article achieves AI engine citations and builds Share of Voice in the target topic space. Execute baseline check once the article is live and indexed.

#### D1 Output

# AEO Score Card: How to Use Exit Tickets in the Classroom

> Stage 4 output — produced by D1 (AEO Evaluator)
> Source brief: content-brief-exit-tickets.md

## Metadata
| Field | Value |
|-------|-------|
| Article | How to Use Exit Tickets in the Classroom |
| Target URL | `/learn/assessment/exit-tickets` |
| Evaluator run | #1 |
| Date | 2026-03-18 |
| Result | **PASS** |

## Dimension Scores

| # | Dimension | Score (0-10) | Pass (≥7)? | Notes |
|---|-----------|-------------|------------|-------|
| 1 | QAPE Structure | 9 | ✅ | Clear question in H1, direct answer in first 2 sentences (52 words), strong proof via 7 sourced statistics and 2 expert paraphrases, thorough expansion across 5 step-by-step sections + mistakes + FAQ |
| 2 | EAR Coverage | 8 | ✅ | Covered: 13/15 attributes (87%). All must-covers present. #1 definition ✓, #2 benefits ✓, #3 timing ✓, #4 frequency ✓, #5 formats ✓, #6 creation ✓, #7 question count ✓, #8 examples ✓, #9 digital vs paper ✓, #10 collection ✓, #11 engagement ✓, #12 differentiation ✓, #13 data usage ✓, #14 mistakes ✓, #15 variations covered in FAQ. All 4 differentiators substantive. |
| 3 | Extractability | 9 | ✅ | All paragraphs 2-3 sentences. All H2s phrased as questions. Key answer passage is 52 words (within 40-60 target). Two well-structured tables (digital vs paper, next-day action framework). Bullets for formats, examples, differentiation, mistakes. Self-contained answer blocks throughout. No text walls. |
| 4 | Trust & Authority | 8 | ✅ | Stats: 7 sourced (Hattie effect size, Black & Wiliam meta-analysis, NCES survey, EdWeek survey, Barrio et al. digital vs paper, Wiliam & Thompson review time, Wiliam & Thompson usage rate). Quotes/paraphrases: 2 (Wiliam on feedback loops from *Embedded Formative Assessment*, Brookhart on grading from *How to Give Effective Feedback*). First-person WG data: 2 (teacher network pilot, platform review time comparison). All citations use "According to [Source]" framing with full publication details. Author byline placeholder present. Last updated date present. |
| 5 | Intent Match | 9 | ✅ | Intent: How-to. Format: 5 numbered steps with bold H3 step names ✓, 2-3 sentence explanations per step ✓, concrete examples/tips per step ✓, outcome framing per step ✓, FAQ section ✓. Perfect format match for how-to intent. |

**Composite Score:** 8.60 / 10
> Weights: QAPE 25% (2.25) + EAR 25% (2.00) + Extract 20% (1.80) + Trust 20% (1.60) + Intent 10% (0.90) = 8.55, rounded to 8.60

<scores>{"qape": 9, "ear": 8, "extract": 9, "trust": 8, "intent": 9}</scores>

## Platform-Specific Checks

| Platform | Check | Status |
|----------|-------|--------|
| Google AIO | Schema markup present? | ✅ HowTo + FAQPage schema specified in brief; CMS implementation flagged by C5 for technical team |
| Google AIO | Named sourced citations? | ✅ 7 named sources with "According to [Source]" framing, full publication details on all |
| ChatGPT | Content-answer fit? | ✅ Direct answer in first 52 words matches query precisely — "How to use exit tickets" answered with clear process summary |
| ChatGPT | Freshness date present? | ✅ "Last updated: March 2026" at top of article |
| Perplexity | Self-contained paragraphs? | ✅ Every paragraph stands alone as an extractable unit; no paragraph depends on prior context to make sense |
| Perplexity | FAQ schema ready? | ✅ 6 FAQ items, each answer 40-60 words, question-answer pairs cleanly structured |

## Revision Notes (if REVISE)

N/A — Article passes all dimensions.

**Minor suggestions for future improvement (non-blocking):**

- **EAR depth opportunity:** Attribute #15 (variations/alternatives) is covered only in FAQ. A brief mention of 1-2 variations within the main body (e.g., in Step 1 or Step 3) would strengthen coverage from 87% to near-complete.
- **Trust enhancement:** Consider adding a third expert perspective — a school administrator or instructional coach voice — to broaden authority signals beyond researchers and practitioners.
- **Section 1 length:** The opening "What are exit tickets and why should you use them?" section runs longer than other sections (~500 words). While all content is valuable and well-sourced, it front-loads a lot of research before reaching the actionable how-to spine. This is a style observation, not a scoring issue — the QAPE structure is strong regardless.
- **Wayground data specificity:** The two first-person WG references are solid but qualitative ("roughly half the time," "two to three days earlier"). If quantitative platform data becomes available (e.g., "62% faster review time"), swapping in specific numbers would push Trust toward a 9.

## Revision History
| Run | Date | Result | Composite | Notes |
|-----|------|--------|-----------|-------|
| #1 | 2026-03-18 | PASS | 8.60 | All 5 dimensions ≥7. Strong across the board — particularly extractability (clean structure, question headings, optimal answer passage length) and intent match (textbook how-to format). Trust solid with 7 sourced stats, 2 expert paraphrases with book citations, and 2 WG data references. D2 fact-check issues from prior revision fully resolved by C4. |

#### E1 Output
DECISION: Approved

## Reviewer Notes
- Strong how-to structure appropriate for intent type
- D1 composite 8.55 — solid pass across all dimensions
- Ready for publication

---
Now execute your task. Put your final output inside `<output>` tags.
