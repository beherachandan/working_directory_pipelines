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

**Topic:** Blooket vs Wayground comparison for classroom learning

### Upstream Agent Outputs

#### G1 Output

# G1 SOV Monitoring Report — Blooket vs Wayground

## Status: PRE-PUBLICATION MONITORING FRAMEWORK

**Article Slug:** `blooket-vs-wayground`  
**Target URL:** `https://wayground.com/learn/edtech-tools/blooket-vs-wayground`  
**Current Status:** 🚫 NOT YET PUBLISHED (HOLD)  
**Blocking Items:** 6 teacher quotes, named author assignment, author photo  
**Framework Prepared:** March 20, 2026  
**Monitoring Start Date:** [PENDING PUBLICATION]

---

## 1. Monitoring Setup

### Target Queries (From Content Brief)

**Primary Query:**
- "Blooket vs Wayground"

**Secondary Queries:**
- "Blooket vs Quizizz"
- "Wayground vs Blooket"
- "Wayground comparison"
- "classroom game platforms"
- "Blooket or Wayground for assessment"
- "best game platform for teachers"

**Question-Based Queries (From FAQ Schema):**
- "Is Blooket or Wayground better for formative assessment?"
- "Which platform is easier to learn and set up?"
- "Can I use both Blooket and Wayground together?"
- "Does Wayground have the same game modes as Blooket?"
- "Which platform has better reporting and analytics?"
- "Are Blooket and Wayground FERPA and COPPA compliant?"
- "Do Blooket and Wayground have mobile apps?"

**Total Target Queries:** 14

### Article Metadata

| Field | Value |
|-------|-------|
| **Content Type** | Comparison article (competitor focus) |
| **Target Audience** | K-12 teachers (elementary through high school) |
| **Word Count** | ~3,400 words |
| **Read Time** | 12 minutes |
| **FAQ Count** | 7 structured FAQs (FAQPage schema) |
| **Internal Links** | 7 (to hub, resource, and feature pages) |
| **External Links** | To Blooket.com (with nofollow) |
| **Category** | EdTech Tools |
| **Hub** | `/learn/edtech-tools/` |

### Citation-Optimized Content Elements

**Factors supporting AI citation eligibility:**
- ✓ 7 FAQ items with 40-60 word answer passages (optimal snippet length)
- ✓ Question-phrased headings throughout article
- ✓ FAQPage schema markup (targets Google AI Overviews and Perplexity)
- ✓ Comparison table (structured data for AI extraction)
- ✓ "According to [Source]" citation framing for statistics
- ✓ Expert quote placeholders (pending real teacher sourcing)
- ✓ Short paragraphs (2-3 sentences — AI-friendly format)
- ✓ Clear section hierarchy with descriptive headings

**Trust signals embedded:**
- Author attribution (pending named educator)
- Real-world use cases and grade-level recommendations
- Evidence-based comparisons (not promotional)
- Competitor neutrality (acknowledges Blooket strengths)

---

## 2. Baseline Monitoring Plan (Post-Publication)

### Week 1 Monitoring Protocol

**Timing:** Begin monitoring 7 days after publication (allows for indexing)

**AI Engines to Monitor:**

| AI Engine | Query Method | Monitoring Frequency | Priority |
|-----------|--------------|----------------------|----------|
| **ChatGPT (GPT-4/4o)** | Direct conversational queries | Weekly | HIGH |
| **Perplexity AI** | Direct search queries | Weekly | HIGH |
| **Google AI Overviews** | Google Search (signed out, incognito) | Weekly | HIGH |
| **Microsoft Copilot** | Bing Chat / Edge Copilot | Bi-weekly | MEDIUM |
| **Claude (Anthropic)** | Direct queries (if web search enabled) | Bi-weekly | MEDIUM |

**Monitoring Tools:**
- Otterly AI (automated AEO tracking)
- Peec AI (AI citation monitoring)
- ZipTie (SOV measurement)
- LLMrefs (citation database)
- Manual DIY checks (initial baseline)

### Baseline Check Template (First Monitoring Cycle)

**To be completed 7-10 days post-publication:**

| AI Engine | Query | Cited? | Position | Snippet Used | Competing Sources | Notes |
|-----------|-------|--------|----------|-------------|-------------------|-------|
| ChatGPT | "Blooket vs Wayground" | [CHECK] | [1st/2nd/Supporting/None] | [Exact text extracted] | [List competitor URLs cited] | [Model version, date] |
| ChatGPT | "Is Blooket or Wayground better for assessment?" | [CHECK] | [Position] | [Snippet] | [Competitors] | [Context] |
| Perplexity | "Blooket vs Wayground" | [CHECK] | [Position] | [Snippet] | [Competitors] | [Date checked] |
| Perplexity | "best game platform for teachers" | [CHECK] | [Position] | [Snippet] | [Competitors] | [Date checked] |
| Google AIO | "Blooket vs Wayground" | [CHECK] | [Featured/Supporting/None] | [Snippet] | [Competitors] | [Location: US] |
| Google AIO | "Blooket or Wayground for assessment" | [CHECK] | [Position] | [Snippet] | [Competitors] | [Rich result?] |
| Copilot | "Wayground vs Blooket comparison" | [CHECK] | [Position] | [Snippet] | [Competitors] | [Edge browser] |
| Claude | "classroom game platforms" | [CHECK] | [Position] | [Snippet] | [Competitors] | [If web-enabled] |

**Repeat for all 14 target queries across 5 AI engines.**  
**Total baseline checks:** ~70 query-engine combinations (prioritize top 3 engines × primary queries)

---

## 3. SOV Calculation Methodology

### Formula

```
SOV = (Queries where Wayground is cited / Total target queries checked) × 100
```

**Per AI Engine:**
```
ChatGPT SOV = (Wayground citations in ChatGPT / Total queries tested in ChatGPT) × 100
```

**Overall SOV:**
```
Total SOV = (Total Wayground citations across all engines / Total queries tested across all engines) × 100
```

### Baseline Expectations (From F4 Analysis)

| Timeframe | Expected Status | SOV Target | Key Milestones |
|-----------|-----------------|------------|----------------|
| **Days 1-3** | Indexing in progress | 0% | Google crawl detected in GSC |
| **Days 3-7** | Indexed, not yet ranking | 0-5% | URL appears in Google index |
| **Days 7-14** | Early ranking signals | 5-15% | First organic traffic, possible ChatGPT/Perplexity pickup |
| **Days 14-21** | Rich results eligible | 15-25% | FAQ schema appears in SERPs, AI snippets begin |
| **Days 30-60** | Competitive positioning | 25-40% | Stable citations for primary queries |
| **Days 60-90** | Maturity phase | 40-60% | Strong SOV for comparison queries |

**Competitive Context:**
- Blooket has strong brand awareness (higher initial advantage)
- "vs Wayground" queries are lower volume than "vs Quizizz" (Wayground rebrand)
- Comparison articles typically take 30-60 days to gain AI citation traction

### Citation Position Weighting

Not all citations are equal. Track position:

| Position Type | Weight | Description |
|---------------|--------|-------------|
| **First/Primary Citation** | 1.0 | AI response opens with or primarily features Wayground |
| **Supporting Citation (Top 3)** | 0.7 | Wayground cited among first 3 sources |
| **Supporting Citation (4+)** | 0.4 | Wayground cited but lower in response |
| **Link-Only (No Excerpt)** | 0.2 | URL appears but no content quoted |
| **Not Cited** | 0.0 | No mention of Wayground |

**Weighted SOV Formula:**
```
Weighted SOV = Σ(Citation Position Weights) / Total Queries Checked
```

This better reflects citation quality, not just presence.

---

## 4. Competitor Benchmarking

### Primary Competitors to Track

**Direct Competitors (Also Cited):**
1. **Blooket** (blooket.com) — primary competitor in this comparison
2. **Kahoot** (kahoot.com) — established game platform
3. **Quizlet** (quizlet.com) — study tools platform
4. **Gimkit** (gimkit.com) — newer game platform
5. **Nearpod** (nearpod.com) — interactive lessons
6. **Edpuzzle** (edpuzzle.com) — video-based assessment

**Generic/Aggregate Sources:**
- EdTech listicles (Top 10 platforms)
- Reddit threads (r/Teachers recommendations)
- Blog posts from education influencers

### Competitor Citation Tracking

For each baseline check, record:
- **Which competitors are cited** alongside Wayground (or instead of Wayground)
- **How often each competitor appears** (competitive SOV)
- **What content they're cited for** (feature comparisons, pricing, use cases)
- **Citation position** (are they cited before/after Wayground?)

**Competitive SOV Dashboard (Example):**

| Competitor | Citations (Out of 14 Queries) | SOV % | Avg Position | Notes |
|------------|-------------------------------|-------|--------------|-------|
| Wayground | [TBD] | [TBD%] | [TBD] | This article |
| Blooket | [TBD] | [TBD%] | [TBD] | Official site + reviews |
| Kahoot | [TBD] | [TBD%] | [TBD] | Strong brand presence |
| Quizlet | [TBD] | [TBD%] | [TBD] | Different use case |
| Gimkit | [TBD] | [TBD%] | [TBD] | Niche but growing |

---

## 5. Pattern Analysis Framework

### Content Characteristics to Correlate with Citation

**Track which content elements get extracted most:**

1. **FAQ Answers** (7 FAQs)
   - Which FAQ questions get cited most by AI engines?
   - Are 40-60 word answers the optimal snippet length?
   - Do question-phrased headings improve citation rates?

2. **Comparison Table**
   - Does the feature comparison table get extracted by AI?
   - Which specific table rows/features are cited?

3. **Quick Answer Passages**
   - Are "key answer passages" (40-60 words after headings) being used?
   - Which sections have highest citation rates?

4. **Pricing Information**
   - Do AI engines cite the pricing comparison section?
   - Accuracy of pricing data (verify regularly)

5. **Use Case Recommendations**
   - Are grade-level recommendations being extracted?
   - Do "when to use" sections get cited?

### AI Engine Preferences to Identify

**Hypotheses to test:**

| AI Engine | Hypothesized Preference | Test Method |
|-----------|-------------------------|-------------|
| **ChatGPT** | Prefers structured FAQs, direct answers | Check FAQ citation rate vs body text |
| **Perplexity** | Prefers recent, cited sources | Track how often academic citations boost selection |
| **Google AIO** | Prefers FAQPage schema, featured snippets | Monitor if FAQ schema drives AIO appearance |
| **Copilot** | Requires <2s page load, prefers tables | Check if performance affects citation rate |
| **Claude** | Prefers authoritative, evidence-based content | Track citation of research-backed claims |

**Data to collect:**
- Which content blocks (by section) are most cited per engine?
- Do different engines extract different passages for the same query?
- Which schema types drive citations (Article vs FAQPage)?

---

## 6. Weekly Monitoring Cadence

### Week 1 Post-Publication (Days 7-14)

**Focus:** Baseline establishment

- [ ] Verify article is indexed (Google Search Console)
- [ ] Confirm FAQ rich results appear in SERPs (Google)
- [ ] Run initial AI engine checks (ChatGPT, Perplexity, Google AIO)
- [ ] Document first 5 target queries across top 3 engines (15 checks)
- [ ] Record competing sources cited
- [ ] Calculate initial SOV (expected: 5-15%)
- [ ] Check page performance (PageSpeed Insights)
- [ ] Verify AI bot access (check robots.txt compliance)

### Week 2-4 Post-Publication (Days 14-30)

**Focus:** Early trend identification

- [ ] Expand to all 14 target queries
- [ ] Monitor across all 5 AI engines
- [ ] Track week-over-week SOV change
- [ ] Identify which content blocks are most cited
- [ ] Note any competitor movements (new content, ranking changes)
- [ ] Check Google Search Console for impressions/clicks
- [ ] Record engagement metrics (time on page, scroll depth)

### Month 2-3 Post-Publication (Days 30-90)

**Focus:** Maturity and optimization

- [ ] Bi-weekly AI engine checks (14 queries × 5 engines)
- [ ] Track 30/60/90-day SOV trends
- [ ] Identify patterns: which content characteristics drive citations?
- [ ] Monitor competitor content updates (are they responding?)
- [ ] Check for content decay (pricing, features outdated?)
- [ ] Assess whether updates/refreshes are needed
- [ ] Feed insights to G2 for pipeline optimization

---

## 7. Alerts & Thresholds

### Positive Alerts (Success Signals)

**Trigger celebration + analysis when:**
- ✓ SOV exceeds 25% within first 30 days
- ✓ Wayground becomes primary citation (position 1) for any target query
- ✓ FAQ schema appears in Google AI Overviews
- ✓ ChatGPT or Perplexity cites article consistently (3+ weeks)
- ✓ Multiple AI engines cite the same content block (validates optimization)

### Negative Alerts (Requires Action)

**Trigger investigation when:**
- ⚠️ SOV remains <5% after 30 days (indexing/quality issue?)
- ⚠️ Competitor publishes new comparison content targeting same queries
- ⚠️ AI engines cite outdated information from article (pricing, features)
- ⚠️ Citations drop week-over-week (content decay or algorithm change?)
- ⚠️ Zero citations from specific AI engine (bot access issue?)
- ⚠️ Page performance degrades (<90 PageSpeed score)

### Critical Alerts (Immediate Action Required)

**Escalate immediately if:**
- 🚨 Article is de-indexed (disappears from Google)
- 🚨 AI bots are blocked (robots.txt change)
- 🚨 Factual error discovered in published content (trust damage)
- 🚨 Competitor allegation/dispute about comparisons (legal/PR risk)
- 🚨 Page load time exceeds 3 seconds (Copilot citation blocker)

---

## 8. Current Status: Pre-Publication Hold

### Why Monitoring Cannot Begin Yet

**F4 Publication Decision:** HOLD

**Blocking items:**
1. **6 teacher quotes** — Placeholders marked [PUBLICATION BLOCKER] in C5
2. **Named author with credentials** — Currently generic attribution
3. **Author photo** — Required for E-E-A-T signals

**Impact on SOV:**
- Articles without real author attribution score 0 for E-E-A-T
- Placeholder quotes = trust score failure (would not pass D1 threshold)
- AI engines deprioritize content with weak authorship signals

**Timeline:**
- Estimated resolution: 5-10 business days (teacher outreach dependent)
- Indexing after publication: 3-7 days
- **First monitoring cycle: ~12-17 days from today**

### Pre-Publication Checklist for G1 Monitoring Readiness

**Before monitoring begins, verify:**

- [ ] Article is published live at target URL
- [ ] All blocking items resolved (quotes, author, photo)
- [ ] Schema markup validated (0 errors in Google Rich Results Test)
- [ ] robots.txt allows all AI bots (GPTBot, PerplexityBot, ClaudeBot, etc.)
- [ ] Page performance meets targets (LCP <2s, CLS <0.1)
- [ ] FAQ schema appears in Google Search Console Enhancements
- [ ] URL submitted to Google Search Console
- [ ] Analytics tracking confirmed
- [ ] Sitemap updated with new URL

**Status:** ❌ NOT READY (0 of 9 items complete — article not published)

---

## 9. Recommended Actions

### Immediate (Today)

**For Editorial/Content Team:**
1. Prioritize sourcing 6 teacher quotes with full attribution
2. Assign named educator author with verifiable credentials
3. Prepare author bio (2-3 sentences) and upload photo (200×200px WebP)

**For G1 Agent (This Report):**
1. ✅ Monitoring framework established (this document)
2. ✅ Target queries defined (14 queries across 5 engines)
3. ✅ Baseline template created (ready for first monitoring cycle)
4. ✅ SOV calculation methodology documented

### Post-Publication (Within 7 Days)

**For SEO/Technical Team:**
1. Verify article is indexed in Google
2. Confirm robots.txt allows all AI bots
3. Validate schema markup (0 errors)
4. Submit URL to Google Search Console
5. Notify G1 agent that monitoring can begin

**For G1 Agent:**
1. Begin Week 1 baseline monitoring (7-10 days post-publication)
2. Run initial checks on top 3 AI engines (ChatGPT, Perplexity, Google AIO)
3. Test 5 primary queries per engine (15 total checks)
4. Document initial SOV baseline (expected: 5-15%)
5. Create first weekly SOV report

### Ongoing (Weeks 2-12)

**Weekly tasks:**
- Check all 14 target queries across 5 AI engines (~70 checks/week)
- Update SOV dashboard (weekly trend line)
- Track competitor citations (who's cited instead of/alongside Wayground)
- Identify content blocks with highest citation rates
- Monitor Google Search Console for impressions/clicks
- Check for performance degradation (monthly PageSpeed test)

**Bi-weekly tasks:**
- Analyze patterns (which content formats/lengths drive citations?)
- Test new query variations (user-generated questions from search)
- Check for content decay (pricing, features, statistics outdated?)
- Verify author page and social signals remain active

**Monthly tasks:**
- Generate full SOV report for G2 feedback loop
- Assess whether content updates/refreshes are needed
- Benchmark against competitor SOV
- Evaluate ROI (citation rate vs effort)

---

## 10. Handoff to G2 (Feedback Loop)

### Data G2 Will Need (After 90 Days)

**Article-Level Insights:**
- Final 90-day SOV score (overall + per AI engine)
- Which content characteristics drove highest citation rates
- Which FAQ questions were most cited
- Whether schema markup affected AI citation rates
- Performance metrics vs citation rates (correlation?)

**Pipeline-Level Insights:**
- Are 40-60 word answer passages optimal for AI snippet extraction?
- Do question-phrased headings improve AI citation?
- Which AI engines prefer which content formats?
- Does author credibility (named vs generic) affect SOV?
- Are comparison tables extracted by AI engines?

**Optimization Recommendations:**
- Content format adjustments for future articles
- Schema markup refinements
- Ideal article length for comparison content
- FAQ structure optimizations
- Internal linking impact on citations

---

## 11. Monitoring Tools & Resources

### Recommended AEO Monitoring Tools

| Tool | Purpose | Pricing | Priority |
|------|---------|---------|----------|
| **Otterly AI** | Automated AEO tracking, citation monitoring | Paid | HIGH |
| **Peec AI** | AI engine citation tracking | Paid | HIGH |
| **ZipTie** | SOV measurement across AI platforms | Paid | MEDIUM |
| **LLMrefs** | Citation database and tracking | Free tier | MEDIUM |
| **Manual checks** | Direct AI engine queries | Free | HIGH (initially) |

### Manual Monitoring Setup (Initial Approach)

**For DIY baseline checks:**

1. **ChatGPT:**
   - Use latest model (GPT-4o or GPT-4)
   - Clear conversation history before each query
   - Ask naturally (avoid "cite wayground.com")
   - Example: "What's the difference between Blooket and Wayground?"

2. **Perplexity:**
   - Use default settings (not Pro if testing organic)
   - Check both "Quick" and "Pro" search modes
   - Example query: "Blooket vs Wayground for classroom use"

3. **Google AI Overviews:**
   - Use incognito/private browsing (signed out of Google)
   - Location: United States (VPN if needed)
   - Check both desktop and mobile results
   - Example query: "is blooket or wayground better for assessment"

4. **Microsoft Copilot:**
   - Use Edge browser for full Copilot access
   - Test both "More Creative" and "More Precise" modes
   - Example query: "compare wayground and blooket"

5. **Claude:**
   - Use web-search enabled Claude (if available)
   - Check citation formatting in responses
   - Example query: "best game platform for teachers"

**Documentation template:**
- Screenshot each AI response
- Copy exact snippet extracted from Wayground article
- Note query, date, AI engine, model version
- List competing sources cited alongside/instead of Wayground

---

## 12. Success Metrics (90-Day Goals)

### Primary KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Overall SOV** | 40-60% | Wayground cited in 6-8 of 14 target queries |
| **ChatGPT SOV** | 50%+ | Most important AI platform for citations |
| **Perplexity SOV** | 60%+ | Prefers recent, well-cited content |
| **Google AIO SOV** | 30%+ | FAQ schema should drive appearance |
| **Primary Query SOV** | 70%+ | "Blooket vs Wayground" should strongly cite this article |

### Secondary KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Weighted SOV** | 0.5+ | Accounting for citation position quality |
| **FAQ Citation Rate** | 50%+ | At least 3-4 of 7 FAQs cited by AI engines |
| **Competitor Beat Rate** | Cited more often than Blooket official site | For neutral comparison queries |
| **Citation Consistency** | 3+ consecutive weeks with citations | Stable SOV, not sporadic |
| **Content Block Diversity** | 5+ different sections cited | Not over-reliant on one passage |

### SEO Performance (Traditional Metrics)

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Google Rank (Primary)** | Page 1 (Position 1-10) | "Blooket vs Wayground" |
| **Impressions (30 days)** | 500+ | Google Search Console |
| **Clicks (30 days)** | 50+ | GSC Performance report |
| **CTR** | 8%+ | Above average for comparison queries |
| **FAQ Rich Results** | Visible | FAQ schema in SERPs |

### Engagement Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Time on Page** | 5+ minutes | Google Analytics (12-min article) |
| **Scroll Depth** | 60%+ | Users reach FAQ section |
| **Bounce Rate** | <60% | Users engage with content |
| **FAQ Clicks** | 30%+ | Users interact with accordion |

---

## Summary: Monitoring Status

**Current State:** 🔴 **MONITORING NOT STARTED** (Article not yet published)

**Readiness:** 🟡 **FRAMEWORK READY** (Monitoring plan complete, awaiting publication)

**Next Actions:**
1. Wait for editorial team to resolve blocking items (quotes, author, photo)
2. Wait for article to be published live
3. Wait 7 days for indexing
4. **Begin Week 1 baseline monitoring**

**Estimated First Monitoring Cycle:** March 27-April 3, 2026 (assuming 5-day blocker resolution + 3-day indexing)

---

**G1 SOV Tracker Agent — Monitoring Framework Complete**  
**Status:** AWAITING PUBLICATION  
**Framework Prepared:** March 20, 2026  
**First Monitoring Cycle:** [PENDING PUBLICATION + 7 DAYS]

#### D1 Output

# AEO Score Card: Blooket vs Wayground: Which Is Better for Your Classroom?

> Stage 4 output — produced by D1 (AEO Evaluator)
> Source brief: content-brief-blooket-vs-wayground.md

## Metadata
| Field | Value |
|-------|-------|
| Article | Blooket vs Wayground: Which Is Better for Your Classroom? (2026 Comparison) |
| Target URL | `/learn/edtech-tools/blooket-vs-wayground` |
| Evaluator run | #3 |
| Date | 2026-03-19 |
| Result | **REVISE — ESCALATE TO HUMAN** |

## Dimension Scores

| # | Dimension | Score (0-10) | Pass (≥7)? | Notes |
|---|-----------|-------------|------------|-------|
| 1 | QAPE Structure | 8 | ✅ | Clear question in H1, direct answer in first paragraph (58 words), proof via Black & Wiliam citation + NCES reference + platform data, strong expansion across 15 sections. Answer is well-positioned but slightly diluted by immediate disclosure box before the comparison content begins. |
| 2 | EAR Coverage | 9 | ✅ | Covered: 18/21 attributes. All 15 must-cover present. Missing: #16 (accessibility detail beyond FERPA mention), #20 (offline capabilities — mentioned but not developed), #21 (student perspective). All 5 major differentiators addressed: content library, assessment depth, time investment, side-by-side table, rebrand narrative. |
| 3 | Extractability | 9 | ✅ | All 14 H2 headings phrased as questions. Paragraphs consistently 2-3 sentences. Key answer passages at section openings range 40-62 words (acceptable). Two well-formatted comparison tables. Bullets for pros/cons, use cases, grade-level, subject. FAQ answers are self-contained at 45-65 words each. No text walls detected. |
| 4 | Trust & Authority | 5 | ❌ | Stats: 3 verifiable (Black & Wiliam 1998 with full citation, NCES National Teacher and Principal Survey reference, 200M+ resources first-party). Quotes: 0 real — all 6 are [PUBLICATION BLOCKER] placeholders. First-person: 3 signals (disclosure box, "our teachers report," "we hear from teachers"). "According to [Source]" framing: 1 instance (Black & Wiliam). No author byline — placeholder only. The hedged first-party claims ("anecdotally," "teachers report") are appropriately transparent but score low on authority. |
| 5 | Intent Match | 9 | ✅ | Intent: Comparison + Transactional. Format: Side-by-side comparison table with 20 rows ✓, pricing table ✓, "Best For" recommendations by grade/subject ✓, pros/cons lists ✓, verdict with clear recommendation ✓, FAQ section with 7 items ✓. All required format elements for comparison intent present. |

**Composite Score:** 7.70 / 10
> Weights: QAPE 25% (2.00) + EAR 25% (2.25) + Extract 20% (1.80) + Trust 20% (1.00) + Intent 10% (0.90) = 7.95

*(Note: Composite is respectable overall, but the Trust dimension at 5/10 fails the ≥7 gate threshold.)*

<scores>{"qape": 8, "ear": 9, "extract": 9, "trust": 5, "intent": 9}</scores>

## Platform-Specific Checks

| Platform | Check | Status |
|----------|-------|--------|
| Google AIO | Schema markup present? | ✅ ComparisonTable + Product + FAQPage + Article schemas specified in brief |
| Google AIO | Named sourced citations? | ⚠️ Only 1 fully named external citation (Black & Wiliam). NCES referenced by survey name but no specific data point. Blooket.com linked but no specific stats cited from it. Falls well below the 5+ named sources threshold for AIO. |
| ChatGPT | Content-answer fit? | ✅ Direct answer in first paragraph (58 words) precisely matches query intent. Strong content-answer alignment. |
| ChatGPT | Freshness date present? | ✅ "Last updated: March 2026" included. Multiple "as of March 2026" qualifiers throughout. |
| Perplexity | Self-contained paragraphs? | ✅ Every paragraph stands alone as an extractable unit. No paragraph depends on prior context to make sense. |
| Perplexity | FAQ schema ready? | ✅ 7 FAQ items, answers 45-65 words each, self-contained. Ready for FAQPage schema markup. |

## Revision Notes (REVISE → ESCALATE)

### Gate Decision Rationale

This is evaluation run #3. The Trust & Authority dimension has scored below threshold across all three runs. Per gate logic: **max 2 revision loops before human escalation.** This article has now exceeded that limit.

**The Trust dimension failure is NOT something C-phase agents can fix.** The blockers require human action:
1. Real teacher quotes require outreach to the teacher network (human coordination)
2. Named author assignment requires an editorial decision (human decision)
3. Product feature verification requires research visits to blooket.com and wayground.com (could be C2/C4 but has been flagged across 3 revisions without resolution)

**Recommendation: ESCALATE to human review** with the following handoff.

### Dimension-Specific Feedback

**Trust & Authority (score: 5):**

**Issue 1 — Zero real teacher quotes (CRITICAL):**
All 6 teacher quote positions contain [PUBLICATION BLOCKER] placeholders. The scoring rubric requires minimum 3 expert quotes with attribution for a score of 7-8, and the content brief specifically requires at least one teacher who uses BOTH platforms. Zero real quotes is the single largest trust deficit in this article. C5 has correctly flagged these as publication blockers, but three revision cycles have not resolved them because quote sourcing requires human outreach.

**Issue 2 — Insufficient named external statistics:**
Only 1 fully cited external statistic (Black & Wiliam, 1998). The NCES reference is to a survey series rather than a specific finding. The rubric targets 3-4 statistics with sources for a 7-8 score. The article currently hedges all first-party claims with appropriate disclaimers, which is honest but scores poorly on authority. Specific, verifiable numbers are needed.

**Issue 3 — No named author:**
The byline is a placeholder. The rubric explicitly includes "author byline with credentials" as a trust signal. Generic or absent attribution scores zero on this criterion.

**Issue 4 — [VERIFY] flags throughout comparison table:**
The primary comparison table — the most important element for a comparison article — contains 12+ [VERIFY] flags on product features. An AI engine encountering unverified claims bracketed with uncertainty flags will not cite this content. These must be resolved with actual research before publication.

### What C5 Did Well (Preserved Strengths)

Credit where due — C5's revision #3 made genuine improvements:
- Elevated disclosure to intro (smart for AI trust signals)
- Removed unverifiable directional statistics rather than fabricating replacements
- Used appropriate hedging language ("anecdotally," "practitioner feedback, not a verified statistic")
- Applied [PUBLICATION BLOCKER] severity labels transparently
- Fixed Black & Wiliam citation consistency across body and FAQ

These are the right editorial choices. The problem is that honesty about gaps still results in gaps. The article is structurally excellent and editorially responsible — it just needs the real evidence inserted.

### Human Escalation: Required Actions

| # | Action | Owner | Priority | Impact on Trust Score |
|---|--------|-------|----------|----------------------|
| 1 | Source 3+ real teacher quotes with full attribution and consent — at least one dual-platform user | Teacher network coordinator | **P0 — Publication blocker** | +2 to +3 points |
| 2 | Assign named author with verifiable credentials (M.Ed. or equivalent, K-12 experience) | Editorial lead | **P0 — Publication blocker** | +0.5 to +1 point |
| 3 | Research and verify all [VERIFY] flags in comparison table (visit blooket.com, wayground.com) | C2/C4 or research assistant | **P0 — Publication blocker** | +0.5 to +1 point |
| 4 | Add 2-3 specific statistics with named sources (e.g., Blooket user count from their site, specific NCES finding, EdSurge or Common Sense review data) | C4 or research assistant | **P1 — Score improvement** | +0.5 to +1 point |
| 5 | Source 1-2 specific first-party Wayground statistics with methodology disclosure (e.g., "In a survey of X teachers conducted [date]...") | Wayground data/UXR team | **P1 — Score improvement** | +0.5 point |

**Projected Trust score after human actions:** 7.5-8.5 (PASS)
**Projected Composite score after human actions:** 8.5-9.0

### Passages Needing Attention

| Location | Issue | Suggested Fix |
|----------|-------|---------------|
| Comparison table (20 rows) | 12+ [VERIFY] flags on core product features | Research each flag at official platform sites; replace with verified data + "as of March 2026" qualifier |
| "Which Platform Drives Better Student Engagement?" | Placeholder quote where elementary teacher voice is needed | Replace [PUBLICATION BLOCKER] with real quote from teacher using Blooket game modes, including full name, grade, subject, years, consent |
| "How Do Content Libraries and Resources Compare?" | Placeholder quote where resource library testimonial is needed | Replace with real quote from teacher describing time savings, with attribution |
| "How Much Time Do Teachers Spend on Each Platform?" | Placeholder quote for time-savings testimonial | Replace with real quote; ideally quantify hours saved per week |
| "What Do Teachers Say..." section | All 3 testimonial slots are placeholders | This section is currently empty of real content — source all 3 quotes; lead with the dual-platform user quote |
| Author byline (end of article) | "[Author Name], [Credentials]" placeholder | Assign real author with verifiable education credentials |
| FAQ #7 (mobile apps) | "[VERIFY current app status]" — answer is vague | Research actual app availability on App Store/Google Play for both platforms |
| Pricing table | All pricing cells are placeholder text | Verify current pricing tiers at both platforms' pricing pages |

## Revision History
| Run | Date | Result | Composite | Notes |
|-----|------|--------|-----------|-------|
| #1 | 2026-03-18 | REVISE | ~5.85 | Initial evaluation — Trust scored low, multiple dimensions needed work |
| #2 | 2026-03-18 | REVISE | ~7.20 | Improved QAPE, EAR, Extractability. Trust improved from hedging fixes but still <7 (score: 6). Unverifiable stats removed. |
| #3 | 2026-03-19 | REVISE → **ESCALATE** | 7.95 | Trust still 5/10 — zero real quotes, insufficient named sources, no author. **3rd revision = exceeds 2-loop max. Escalating to human.** Structure, extractability, EAR, and intent are all strong (8-9 range). Trust is the sole blocker and requires human action to resolve. |

---

**Escalation Summary:** This article is structurally excellent (Extractability 9, EAR 9, Intent 9) and editorially responsible (honest about gaps, no fabrication). It fails exclusively on Trust & Authority because it lacks real teacher quotes, a named author, verified product data, and sufficient external citations — none of which can be resolved by further C-phase AI revision. Recommend human team action on the 5 items above, then a final D1 evaluation pass to confirm PASS status.

#### E1 Output
DECISION: Approved

## Reviewer Notes
- Note: This article was escalated after 2 revision loops (Trust dimension stayed below 7)
- Comparison content inherently has fewer third-party citations — Trust score of 5-6 is expected for this intent type
- Content quality is acceptable for publication with the understanding that comparison articles have lower citation density
- Approve to proceed through full pipeline for end-to-end validation

---
Now execute your task. Put your final output inside `<output>` tags.
