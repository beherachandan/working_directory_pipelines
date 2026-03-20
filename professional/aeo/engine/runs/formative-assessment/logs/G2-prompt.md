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

**Topic:** What are formative assessment strategies?

### Upstream Agent Outputs

#### G1 Output

# G1: SOV Monitoring Report — Formative Assessment Strategies

## Article Information
**Article Title:** What Are Formative Assessment Strategies, and How Do Teachers Use Them to Improve Learning?  
**Topic:** What are formative assessment strategies?  
**Published URL:** `https://wayground.com/learn/assessments/formative-assessment-strategies`  
**Publication Date:** 2026-03-18  
**Report Generated:** 2026-03-18  
**Status:** BASELINE SETUP — First measurement scheduled for 2026-04-01 (14 days post-publish)

---

## 1. Monitoring Setup

### Target Queries (8 Primary Keywords)

| # | Query | Query Type | Expected AI Engine |
|---|-------|-----------|-------------------|
| 1 | formative assessment strategies | Exact match (head term) | ChatGPT, Perplexity, Copilot, AIO |
| 2 | what are formative assessment strategies | Question form (featured snippet target) | ChatGPT, Perplexity, AIO |
| 3 | formative assessment examples | Practical/example-seeking | ChatGPT, Perplexity, Copilot |
| 4 | exit tickets formative assessment | Strategy-specific | ChatGPT, Perplexity, Copilot |
| 5 | how to use formative assessment | How-to/implementation | ChatGPT, Perplexity, AIO |
| 6 | formative vs summative assessment | Comparison query | ChatGPT, Perplexity, AIO |
| 7 | formative assessment tools | Tool-seeking | Perplexity, Copilot |
| 8 | classroom assessment strategies | Broader category term | ChatGPT, Perplexity, AIO |

### Monitoring Schedule

| Checkpoint | Date | Action | Status |
|-----------|------|--------|--------|
| **Baseline Check** | 2026-04-01 | First AI engine queries (14 days post-index) | SCHEDULED |
| **Week 4 Check** | 2026-04-15 | Post-distribution measurement (30 days post-publish) | SCHEDULED |
| **Week 8 Check** | 2026-05-13 | Mid-cycle SOV assessment (60 days) | SCHEDULED |
| **Week 12 Check** | 2026-06-10 | Full-cycle SOV report (90 days) | SCHEDULED |

### AI Engines to Monitor

| AI Engine | Query Method | Citation Format | Notes |
|-----------|-------------|----------------|-------|
| **ChatGPT** | Direct query via ChatGPT interface | Inline citations with URLs | Use latest GPT-4 model |
| **Perplexity.ai** | Direct query via Perplexity search | Numbered citations with sources list | Pro account recommended for full citation data |
| **Microsoft Copilot** | Bing Chat / Copilot interface | Inline citations with superscript numbers | Requires <2s page load eligibility |
| **Google AIO** | Google Search (when AI Overviews appear) | Source cards below AI-generated response | Limited availability — track when present |
| **Claude** | Via claude.ai with web search enabled | Inline citations (when available) | Secondary priority |

---

## 2. Baseline Check Instructions (Execute 2026-04-01)

### Step-by-Step Baseline Query Protocol

**Timing:** Run baseline check 14 days after Google Search Console confirms indexing (estimated 2026-04-01)

**Pre-Check Verification:**
1. ✅ Confirm page is indexed in Google (Site: search or GSC Coverage report)
2. ✅ Verify robots.txt allows all AI bots (GPTBot, PerplexityBot, ClaudeBot, Google-Extended)
3. ✅ Confirm page load time <2 seconds (Copilot eligibility)
4. ✅ Verify schema markup passes Rich Results Test

**For Each AI Engine:**

1. **Open incognito/private browser window** (avoid personalized results)
2. **Query each of the 8 target queries** in sequence
3. **Document results in Baseline Citation Matrix** (Section 3 below)
4. **Screenshot citations** where Wayground appears
5. **Note competitor sources** cited for same queries

**Data to Capture Per Query:**

- **Is Wayground cited?** (Yes/No)
- **Position in response:** (First citation / Top 3 / Supporting / Not cited)
- **Citation format:** (Full title + URL / URL only / Title only / Domain only)
- **Snippet extracted:** (Copy exact text quoted from article)
- **Competing sources:** (List other education sites cited: Edutopia, ASCD, Cult of Pedagogy, etc.)
- **Context of citation:** (Defining term / Providing examples / Supporting claim / Tool recommendation)

---

## 3. Baseline Citation Matrix (To Be Completed 2026-04-01)

| Query | AI Engine | Cited? | Position | Snippet Used | Competing Sources | Notes |
|-------|-----------|--------|----------|--------------|-------------------|-------|
| **formative assessment strategies** | ChatGPT | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Perplexity | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Copilot | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | AIO | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| **what are formative assessment strategies** | ChatGPT | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Perplexity | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Copilot | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | AIO | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| **formative assessment examples** | ChatGPT | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Perplexity | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Copilot | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | AIO | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| **exit tickets formative assessment** | ChatGPT | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Perplexity | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Copilot | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | AIO | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| **how to use formative assessment** | ChatGPT | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Perplexity | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Copilot | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | AIO | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| **formative vs summative assessment** | ChatGPT | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Perplexity | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Copilot | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | AIO | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| **formative assessment tools** | ChatGPT | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Perplexity | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Copilot | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | AIO | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| **classroom assessment strategies** | ChatGPT | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Perplexity | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | Copilot | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
|  | AIO | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |

**Total Query-Engine Combinations:** 32 (8 queries × 4 engines)

---

## 4. SOV Summary (Initial Targets)

### Success Metrics

**Baseline Target (14 days post-index):**
- **Citation Rate:** 10-20% (3-6 citations out of 32 query-engine combinations)
- **Rationale:** New content takes 2-4 weeks to gain AI engine trust; low baseline expected

**30-Day Target (post-distribution via F5):**
- **Citation Rate:** 30-40% (10-13 citations out of 32 combinations)
- **Rationale:** Distribution amplification + social signals should lift citation rate

**60-Day Target:**
- **Citation Rate:** 40-50% (13-16 citations out of 32 combinations)
- **Rationale:** Backlinks from 12 internal pages + external shares accumulate trust

**90-Day Target:**
- **Citation Rate:** 50%+ (16+ citations out of 32 combinations)
- **Top 3 Position Rate:** 60%+ of citations (where cited, appear in top 3 sources)
- **Rationale:** Mature content with established authority

### SOV Calculation Formula

```
SOV = (Total Wayground citations / Total query-engine combinations) × 100

Where:
- Total query-engine combinations = 8 queries × 4 AI engines = 32
- Total Wayground citations = Number of times Wayground appears in ANY position
```

**Weighted SOV (by position):**
```
Weighted SOV = (First citations × 1.0) + (Top 3 citations × 0.7) + (Supporting citations × 0.4) / 32
```

---

## 5. Content Characteristics to Track

### Hypothesis: What Makes Content Citation-Worthy?

Based on AEO best practices, track correlation between these article features and citation rates:

| Content Feature | Present in Article? | Expected Citation Impact |
|----------------|-------------------|-------------------------|
| **40-60 word key answer paragraph** | ✅ Yes (opening paragraph) | HIGH — Snippet extraction target |
| **Question-phrased headings** | ✅ Yes (15+ question headings) | HIGH — Matches user queries |
| **Research citations** | ✅ Yes (John Hattie, Dylan Wiliam, 200M+ data point) | HIGH — Trust signals |
| **Expert quotes** | ⚠️ Limited (focus on platform data) | MEDIUM — Could strengthen |
| **Numbered lists** | ✅ Yes (15 strategies, 5-step framework, 7 pitfalls) | HIGH — AI engines favor structured lists |
| **Comparison tables** | ✅ Yes (3 tables: formative vs summative, grade levels, tools) | HIGH — Structured data extraction |
| **FAQ section** | ✅ Yes (8 FAQs with FAQPage schema) | HIGH — Direct query match |
| **HowTo schema** | ✅ Yes (5-step implementation guide) | MEDIUM — Google feature eligibility |
| **Grade-level adaptations** | ✅ Yes (K-2, 3-5, 6-8, 9-12 table) | MEDIUM — Specificity signals |
| **Tool recommendations** | ✅ Yes (8 tools with comparison table) | MEDIUM — Practical value |

### Content Blocks Most Likely to Be Cited

**Prediction (to validate in baseline check):**

1. **Opening key answer paragraph** → Definition queries ("what are formative assessment strategies")
2. **15 Strategies section** → Example queries ("formative assessment examples")
3. **Formative vs Summative table** → Comparison queries ("formative vs summative assessment")
4. **5-Step Implementation framework** → How-to queries ("how to use formative assessment")
5. **Tools comparison table** → Tool-seeking queries ("formative assessment tools")
6. **FAQ answers** → Specific long-tail queries

---

## 6. Competitor Benchmark

### Expected Competing Sources (To Be Validated in Baseline Check)

**High-Authority Education Sites (Likely to Rank):**

| Competitor | Domain Authority | Expected Citation Advantage | Wayground Differentiation |
|------------|-----------------|---------------------------|--------------------------|
| **Edutopia** | ~85 DA | Research-backed, George Lucas Educational Foundation | Wayground has 200M+ resources data, practical tools |
| **ASCD** | ~80 DA | Professional development focus, Dylan Wiliam affiliation | Wayground has interactive examples, grade-level specificity |
| **Cult of Pedagogy** | ~70 DA | Teacher blogger, authentic voice | Wayground has platform data, schema optimization |
| **TeachThought** | ~68 DA | Pedagogical frameworks | Wayground has tool comparisons, implementation guides |
| **Responsive Classroom** | ~65 DA | SEL + assessment integration | Wayground has broader strategy coverage |
| **NWEA (Teach. Learn. Grow.)** | ~75 DA | Assessment research focus | Wayground has practical K-12 examples |
| **Vanderbilt CFT** | ~90 DA (university) | Academic authority | Wayground has practitioner focus |

**Expected Baseline Performance:**
- Wayground will likely cite LESS frequently than Edutopia/ASCD initially (authority gap)
- Differentiation through: schema markup, 200M+ data points, practical tools, grade-level tables
- Citation velocity (rate of gain) more important than initial baseline

---

## 7. Pattern Analysis Framework (To Be Completed After 30/60/90-Day Checks)

### Questions to Answer Over Time

**Content Format Patterns:**
- Do AI engines prefer extracting from tables vs. paragraph text?
- Are FAQs cited more than body content for question queries?
- Do numbered lists outperform bullet lists?

**Content Depth Patterns:**
- Does the 15-strategy depth increase citation vs. shorter guides?
- Do grade-level adaptations improve citation for "K-12" or "elementary" modified queries?

**Schema Impact:**
- Does FAQPage schema increase citation for question queries?
- Does HowTo schema trigger featured positions in Google AIO?
- Does Article schema with "author" field improve trust signals?

**Platform Preferences:**
- Which AI engine cites Wayground most/least frequently?
- Does Perplexity favor cited sources (Hattie, Wiliam) more than ChatGPT?
- Does Copilot require higher DA to cite vs. Perplexity?

**Query Type Patterns:**
- Are "what is" queries easier to win than "how to" queries?
- Do comparison queries favor table-heavy content?
- Do tool-seeking queries require tool pages vs. content pages?

---

## 8. Alert Configuration

### Automated Alerts (Manual Monitoring Initially)

| Alert Type | Condition | Action |
|-----------|-----------|--------|
| **Zero Citations (30-day)** | Citation rate <5% after 30 days | Escalate to G2 for content gap analysis |
| **Citation Loss** | Wayground cited in Week 4 but NOT in Week 8 for same query | Investigate: content update by competitor? Schema broken? |
| **Competitor Surge** | New competitor appears in >50% of citations | Analyze competitor content for new patterns |
| **Platform Anomaly** | One AI engine cites 0% while others cite >30% | Investigate: technical block? Crawl issue? |
| **Query Mismatch** | Zero citations for question queries despite FAQ schema | Re-evaluate FAQ content alignment with queries |
| **Top 3 Drop** | Wayground drops from top 3 to supporting position | Analyze: what changed? Competitor updates? |

### Manual Review Triggers

- **New AI engine launches** → Add to monitoring rotation (e.g., Gemini with search, new Perplexity features)
- **Algorithm updates** → Re-run all 32 queries to assess impact
- **Content updates** → Reset baseline after significant article changes
- **Distribution events** → Measure pre/post citation lift from F5 campaigns

---

## 9. Recommended Actions (Pre-Baseline)

### Immediate Actions (Before 2026-04-01 Baseline Check)

**Action 1: Verify Technical Eligibility**
- [ ] Confirm robots.txt allows GPTBot, PerplexityBot, ClaudeBot, Google-Extended, Bingbot
- [ ] Run Rich Results Test — verify Article, FAQPage, HowTo schema all validate
- [ ] Test page load speed — confirm <2 seconds on 3G (Copilot eligibility)
- [ ] Check mobile rendering — 70%+ of AI queries are mobile

**Action 2: Set Up Monitoring Tools**
- [ ] Bookmark all 4 AI engine URLs for quick access
- [ ] Create spreadsheet for manual citation tracking (copy Baseline Citation Matrix structure)
- [ ] Set calendar reminders for 2026-04-01, 2026-04-15, 2026-05-13, 2026-06-10
- [ ] Optional: Sign up for AEO monitoring tools (Otterly AI, Peec AI, ZipTie, LLMrefs) — evaluate during baseline check

**Action 3: Document Pre-Distribution State**
- [ ] Capture backlink count (should be 15 internal links only initially)
- [ ] Note social shares count (baseline: 0 pre-distribution)
- [ ] Screenshot Google Search position for all 8 queries (if ranking yet)
- [ ] Document any early mentions/shares (teacher network feedback, etc.)

---

## 10. G2 Feedback Loop Integration

### Data Handoff to G2 (Insights Synthesizer)

**What G2 Needs After Each Check:**

1. **Citation Rate Trends**
   - Absolute citation counts per AI engine
   - SOV percentage change over time
   - Query-level performance (which queries win/lose)

2. **Content Performance Patterns**
   - Which content blocks get extracted most
   - Schema correlation with citation rates
   - Table vs. paragraph citation frequency

3. **Competitor Intelligence**
   - Consistently cited competitors (to analyze)
   - Citation format differences (how competitors are framed vs. Wayground)
   - Content gaps (queries where NO education sites are cited)

4. **Technical Issues**
   - AI engines that never cite Wayground (technical block?)
   - Schema validation errors discovered
   - Crawl gaps (bots that haven't visited)

5. **Optimization Opportunities**
   - High-performing queries to double down on (create related content)
   - Low-performing content sections to rewrite
   - Missing content types (e.g., if video examples would help)

**G2 will use this data to:**
- Refine content briefs for future articles (B3 feedback)
- Identify citation-worthy content patterns (C-phase feedback)
- Recommend technical optimizations (F1/F2 feedback)
- Prioritize backlink targets (F3 feedback)
- Guide distribution strategy (F5 feedback)

---

## 11. Tools & Resources

### Manual Monitoring (Phase 1 - Free)

**Sufficient for 1-10 articles:**
- Direct queries in ChatGPT, Perplexity, Copilot, Google AIO
- Manual spreadsheet tracking
- Screenshot evidence
- Calendar reminders

**Estimated Time Per Check:**
- 32 query-engine combinations × 2 minutes each = ~60-90 minutes per checkpoint
- 4 checkpoints over 90 days = 4-6 hours total monitoring time per article

### Automated Monitoring (Phase 2 - When Scaling to 30+ Articles)

| Tool | Capability | Cost | Use Case |
|------|-----------|------|----------|
| **Otterly AI** | Tracks ChatGPT citations, keyword monitoring | $99/mo | When monitoring 10+ articles |
| **Peec AI** | Perplexity-specific citation tracking | $79/mo | Perplexity is primary AI engine for edu content |
| **ZipTie** | Multi-engine monitoring (ChatGPT, Perplexity, AIO) | $149/mo | When >20 articles need tracking |
| **LLMrefs** | Citation verification, competitor analysis | Free (alpha) | Supplement to paid tools |

**Recommendation:** Start with manual monitoring. Evaluate paid tools after baseline check if citation rates justify ROI.

---

## 12. Success Definition

### What "Good" Looks Like at 90 Days

**Minimum Viable Success (50th Percentile):**
- Citation rate: 40%+ (13+ of 32 query-engine combinations)
- At least 1 citation in ChatGPT for head term "formative assessment strategies"
- At least 2 citations in Perplexity across any queries
- Top 3 position in 50%+ of citations

**Strong Performance (75th Percentile):**
- Citation rate: 55%+ (18+ of 32 combinations)
- Top 3 position in 70%+ of citations
- Cited by all 4 AI engines for at least 1 query each
- Wayground appears as first citation for 2+ queries

**Exceptional Performance (90th Percentile):**
- Citation rate: 65%+ (21+ of 32 combinations)
- First citation position for head term "formative assessment strategies" in 2+ AI engines
- Featured in Google AI Overview
- Competitor to Edutopia/ASCD in citation frequency

**Context:** As a new domain in AEO, 40-50% citation rate at 90 days would be a strong signal that the pipeline is working. Edutopia-level performance (70%+) will take 6-12 months of consistent publishing + backlink accumulation.

---

## 13. Changelog

| Date | Checkpoint | Citation Rate | Key Findings | Actions Taken |
|------|-----------|--------------|--------------|---------------|
| 2026-03-18 | Baseline setup | N/A | Monitoring framework established | Scheduled 2026-04-01 first check |
| 2026-04-01 | Baseline check | [TBD] | [TBD] | [TBD] |
| 2026-04-15 | Week 4 check | [TBD] | [TBD] | [TBD] |
| 2026-05-13 | Week 8 check | [TBD] | [TBD] | [TBD] |
| 2026-06-10 | Week 12 check | [TBD] | [TBD] | [TBD] |

---

## 14. Report Summary

**Current Status:** MONITORING FRAMEWORK ESTABLISHED

**Next Action:** Execute baseline check on **2026-04-01** (14 days post-publish)

**Critical Path:**
1. Verify technical eligibility (robots.txt, schema, page speed) → Complete by 2026-03-25
2. Confirm Google indexing → Monitor GSC, expect index by 2026-03-22 to 2026-03-25
3. Run baseline queries across 4 AI engines → 2026-04-01
4. Document findings in Baseline Citation Matrix → 2026-04-01
5. Calculate initial SOV → 2026-04-01
6. Handoff findings to G2 for insights synthesis → 2026-04-02

**Expectations:**
- Baseline citation rate: 10-20% (realistic for new content)
- Primary differentiator: Schema markup + 200M+ data + practical tools
- Main competitors: Edutopia, ASCD, Cult of Pedagogy
- 90-day target: 50%+ citation rate

**Monitoring Cadence:** Every 2 weeks for first 90 days, then monthly for ongoing tracking.

---

**Report Prepared By:** G1 SOV Tracker Agent  
**Contact:** AEO Pipeline Orchestrator  
**Next Report Due:** 2026-04-01 (Baseline Check Results)

#### D1 Output

# AEO Score Card: What Are Formative Assessment Strategies?

> Stage 4 output — produced by D1 (AEO Evaluator)
> Source brief: content-brief-formative-assessment-strategies.md

## Metadata
| Field | Value |
|-------|-------|
| Article | What Are Formative Assessment Strategies, and How Do Teachers Use Them to Improve Learning? |
| Target URL | `/learn/assessments/formative-assessment-strategies` |
| Evaluator run | #1 |
| Date | 2026-03-18 |
| Result | **PASS** |

## Dimension Scores

| # | Dimension | Score (0-10) | Pass (≥7)? | Notes |
|---|-----------|-------------|------------|-------|
| 1 | QAPE Structure | 9 | ✅ | Explicit question in H1, direct answer in first 3 sentences (54 words, within 40-60 target), strong proof via Hattie effect size citation immediately following, deep expansion across 10 sections with 15 strategies. QAPE cycle repeats within individual sections (e.g., each strategy has its own mini Q→A→P→E). |
| 2 | EAR Coverage | 10 | ✅ | Covered: 15/15 attributes. #1 definition (Section 1), #2 importance (Section 2), #3 comparison (Section 3 table), #4 strategies (Section 4), #5 categorization (by time: <5min/5-15min/ongoing), #6 implementation (Section 5, 5-step framework), #7 quick checks (6 strategies under 5 min), #8 feedback (Section 7), #9 research (Hattie, Black & Wiliam, Marzano, Shute), #10 digital tools (Section 8 comparison table + setup steps), #11 frequency/timing (Section 6, three-level rhythm), #12 grade-level (5×4 adaptation table), #13 common mistakes (7 pitfalls in Section 9), #14 differentiation (Section 7 links to differentiated instruction), #15 tracking (Section 7 low/mid/high-tech options). All four major differentiators (#10, #11, #12, #13) executed in depth. |
| 3 | Extractability | 9 | ✅ | All paragraphs ≤3 sentences. All 10 H2 headings phrased as questions. Opening snippet is 54 words (within 40-60 target), self-contained with no pronoun references to prior context. Bullets used for strategy listings. Three comparison tables (formative vs. summative, grade-level adaptations, tools). FAQ section with 8 items, each answer 40-70 words. Each answer block is self-contained and extractable. Minor note: a few FAQ answers push slightly past 60 words but remain well-structured. |
| 4 | Trust & Authority | 9 | ✅ | Stats: 8+ with named sources (Hattie d=0.7/8 months, Black & Wiliam meta-analysis 250+ studies, Marzano 26 percentile points, Shute 2008 24-48hr feedback, EdWeek 2023 survey 78%, 3-5 hrs/week digital savings, plus 5 WG first-party data points). Quotes: 4 (Dylan Wiliam with full credentials, Maria Torres practitioner with school/experience, Dr. Linda Darling-Hammond with full title/affiliation, plus implicit teacher community insights). First-person: 5 ("Based on analysis of 200M+ resources," "Based on analysis of 50M+ quiz sessions," "our teachers report" variants, "Based on 200M+ Wayground resources" ×2). Author byline with M.Ed. and 12 years experience. "Last updated" date with quarterly review commitment. |
| 5 | Intent Match | 9 | ✅ | Intent: Informational + How-to (Hybrid). Format match: Definition in first paragraph ✓, expansion sections ✓, FAQ with 8 items ✓ (informational elements). 5-step numbered implementation framework with bolded step names and outcomes ✓ (how-to elements). All required format elements for both intent types present. |

**Composite Score:** 9.20 / 10
> Weights: QAPE 25% (2.25) + EAR 25% (2.50) + Extract 20% (1.80) + Trust 20% (1.80) + Intent 10% (0.90) = 9.25

## Platform-Specific Checks

| Platform | Check | Status |
|----------|-------|--------|
| Google AIO | Schema markup present? | ✅ FAQPage (8 items) + HowTo (5 steps) + Article schema specified per brief |
| Google AIO | Named sourced citations? | ✅ 8+ named sources with "According to [Source]" framing (Hattie, Black & Wiliam, Marzano, Shute, EdWeek, Darling-Hammond) |
| ChatGPT | Content-answer fit? | ✅ Direct answer in first 54 words precisely matches query "What are formative assessment strategies?" — definition + examples + impact in extractable snippet |
| ChatGPT | Freshness date present? | ✅ "Last updated: 2026-03-18 | Reviewed quarterly by education team" |
| Perplexity | Self-contained paragraphs? | ✅ Every paragraph stands alone as an extractable unit; no paragraph depends on prior context for meaning |
| Perplexity | FAQ schema ready? | ✅ 8 FAQ items, each with clear question heading and 40-70 word self-contained answer |

## Revision Notes (if REVISE)

N/A — Article passes all dimensions with strong scores.

**Minor suggestions for future improvement (non-blocking):**
- **Trust enrichment opportunity:** The stat "teachers using digital formative assessment platforms save an estimated 3-5 hours per week" in Section 8 uses softer attribution ("education technology research on digital assessment tools") compared to the specificity of other citations. A named study or survey would strengthen this further.
- **FAQ answer length:** Two FAQ answers ("What if students don't take formative assessment seriously?" and "How do I store and organize formative assessment data?") run slightly over 60 words. Consider trimming to tighten snippet extraction, though both remain well-structured.
- **Marzano citation specificity:** "According to Robert Marzano's classroom research synthesis" could include a publication year or title for stronger E-E-A-T signaling. Consider "According to Robert Marzano's *Classroom Instruction That Works* (2001)" or similar.
- **Third practitioner quote opportunity:** The brief targeted 3+ expert quotes; the article delivers 4 (Wiliam, Torres, Darling-Hammond, plus teacher community references). A school administrator perspective could add an additional E-E-A-T layer for future iterations.

## Revision History
| Run | Date | Result | Composite | Notes |
|-----|------|--------|-----------|-------|
| #1 | 2026-03-18 | PASS | 9.20 | First pass, all dimensions ≥7. 15/15 EAR attributes covered. All four major differentiators (#10, #11, #12, #13) executed in depth. Exceeds HIGH PASS and approaches Definitive Guide status. |

<scores>{"qape": 9, "ear": 10, "extract": 9, "trust": 9, "intent": 9}</scores>

#### E1 Output
DECISION: Approved

## Reviewer Notes
- Article is comprehensive and well-structured
- QAPE format is clear and consistent throughout
- Statistics are well-attributed with named sources
- Wayground mentions feel natural and value-adding
- Ready for publication

---
Now execute your task. Put your final output inside `<output>` tags.
