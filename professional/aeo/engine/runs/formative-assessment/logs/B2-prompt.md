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

# B2: EAR Decomposer Agent

## Identity
- **Phase:** B — Content Planning
- **Stage:** Stage 1e, 2a
- **Purpose:** Break down primary questions into sub-questions/attributes that a comprehensive answer must cover (Entity-Attribute-Relationship decomposition).

## Inputs
- Primary question
- Intent classification from B1
- Competitor content analysis from A2

## Process

### Step 1: Sub-question Decomposition
Use LLM to decompose the primary question into 8-15 sub-questions/attributes that a comprehensive answer must address.

Example for "What is formative assessment?":
1. Definition of formative assessment
2. Difference between formative and summative assessment
3. Types/examples of formative assessment
4. Benefits of formative assessment
5. How to implement formative assessment in the classroom
6. Best practices for formative assessment
7. Formative assessment tools and technology
8. Common challenges with formative assessment
9. Research/evidence supporting formative assessment
10. Formative assessment for different grade levels

### Step 2: Competitor Coverage Check
For each attribute, check:
- Do the top-cited competitors (from A2) cover this attribute?
- How deeply? (Mentioned / Addressed / Deep coverage)
- Where are the gaps WG can fill?

### Step 3: Coverage Target Setting
Classify each attribute:
- **Must-cover:** Core to answering the primary question. Omission = incomplete answer.
- **Nice-to-have:** Adds depth. Include if word count allows.
- **Differentiator:** Covered poorly by competitors — WG's opportunity to stand out.

### Step 4: Overlap Score Framework
Calculate target coverage:
```
Target EAR Score = (Must-cover attributes + Differentiators) / Total attributes
Minimum acceptable: 70% (maps to score of 7 in D1 evaluator)
```

## Output
**EAR Attribute List** containing:
- 8-15 sub-questions/attributes
- Must-cover vs. nice-to-have classification
- Competitor coverage status per attribute
- Differentiator flags
- Target coverage score

## Constraints
- Minimum 8 attributes per topic
- All sub-questions must be answerable within the topic scope
- Decomposition should mirror how AI engines break down queries during RAG retrieval

## Dependencies
- **Upstream:** B1 (intent determines decomposition approach), A2 (competitor analysis)
- **Downstream:** B3 (builds brief around EAR list), D1 (evaluates against EAR targets)

## Why This Agent Is Critical
AI engines decompose queries into sub-queries during RAG retrieval. Content that covers more attributes = higher probability of being the selected source. Creating an overlap score framework helps measure and optimize coverage systematically.

## Skills Repo Reference
- `content-strategy` — pillar/cluster model, topic decomposition

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |

---
## Task Payload

**Topic:** What are formative assessment strategies?

### Upstream Agent Outputs

#### A1 Output
# Topic Dossier: Formative Assessment Strategies

> Stage 1 output — produced by A1, A2, B1, B2 agents

## Metadata
| Field | Value |
|-------|-------|
| Topic | Formative Assessment Strategies |
| Date created | 2026-03-18 |
| AEO Opportunity Score | 810 / 1000 |
| Intent type | Informational + How-to |
| Target URL | `/learn/assessments/formative-assessment-strategies` |
| Priority | P1 |
| Status | Ready for Brief |

## Primary Question
**What are formative assessment strategies?**

### Variant Phrasings
1. What are examples of formative assessment strategies?
2. What formative assessment strategies are most effective?
3. How do I use formative assessment strategies in my classroom?
4. What are the best formative assessment techniques for teachers?
5. What is the difference between formative and summative assessment strategies?

## Intent Classification
- **Type:** Informational + How-to (hybrid)
- **Required format:** Definition + categorized list with examples + implementation guidance
- **Depth level:** Comprehensive (educators need both theory and practical application)

## AI Answer Landscape

### Current Citations (who gets cited?)
| AI Engine | Cited Source | URL | Why Cited (structure/authority/data) |
|-----------|-------------|-----|--------------------------------------|
| ChatGPT | [REQUIRES LIVE RESEARCH] | [REQUIRES LIVE RESEARCH] | [Typically cites: Edutopia, ASCD, university education departments] |
| Perplexity | [REQUIRES LIVE RESEARCH] | [REQUIRES LIVE RESEARCH] | [Typically cites: academic journals, education non-profits] |
| Google AIO | [REQUIRES LIVE RESEARCH] | [REQUIRES LIVE RESEARCH] | [Typically cites: .edu domains, established ed publishers] |

**NOTE:** Live AI engine querying needed to populate current citation data. Typical citation patterns favor: (1) educational non-profits with authority (Edutopia, ASCD, NWEA), (2) .edu domains, (3) government education resources, (4) established publishers (Pearson, McGraw-Hill education divisions).

### Gaps & Opportunities
- **What's missing from current AI answers:**
  - Practical implementation timelines (how often to use each strategy)
  - Grade-specific adaptations (K-2 vs. 3-5 vs. 6-8 vs. 9-12)
  - Technology integration examples (digital tools for formative assessment)
  - Common implementation mistakes and how to avoid them
  - Student engagement data tied to specific strategies

- **What WG can uniquely provide:**
  - "Based on 200M+ resources" usage data on what strategies work at scale
  - Concrete examples from WG's quiz/lesson library with links to ready-to-use resources
  - Teacher community insights (what actual practitioners find most practical)
  - Integration guidance: "Use exit tickets with WG's 5-question quiz builder"
  - Subject-specific strategy recommendations backed by platform data

- **Source domains AI trusts but WG is absent from:**
  - Education research aggregators (What Works Clearinghouse style)
  - Practitioner insight repositories (TeachThought, Cult of Pedagogy)
  - Academic education journals (cited for credibility but often paywalled/inaccessible to teachers)

## EAR Attribute List
> Sub-questions a comprehensive answer must cover

| # | Attribute / Sub-question | Must-cover? | Covered by competitors? |
|---|--------------------------|-------------|------------------------|
| 1 | What is formative assessment? (definition) | Yes | Yes |
| 2 | Why are formative assessment strategies important? | Yes | Yes |
| 3 | What are the main types/categories of formative assessment? | Yes | Partial |
| 4 | What are 10-15 specific formative assessment strategies with examples? | Yes | Yes |
| 5 | How do I implement formative assessments in my classroom? | Yes | Partial |
| 6 | How often should I use formative assessment? | Nice-to-have | No |
| 7 | What's the difference between formative and summative assessment? | Yes | Yes |
| 8 | How do I give feedback using formative assessment data? | Yes | Partial |
| 9 | What are quick formative assessment strategies (5 minutes or less)? | Nice-to-have | Partial |
| 10 | How do I use formative assessment for different grade levels? | Nice-to-have | No |
| 11 | What digital tools support formative assessment? | Yes | Partial |
| 12 | How do I track formative assessment data? | Nice-to-have | Partial |
| 13 | What does research say about formative assessment effectiveness? | Yes | Yes |
| 14 | How do formative assessments support differentiated instruction? | Nice-to-have | Partial |
| 15 | What are common mistakes with formative assessment? | Nice-to-have | No |

## Competitor Content Analysis

### Top Cited Sources
| Source | URL | Structure | Strengths | Weaknesses |
|--------|-----|-----------|-----------|------------|
| Edutopia | edutopia.org/assessment | Articles with embedded videos, teacher testimonials | High trust, practical tone, multimedia | Not comprehensive single-page resource |
| ASCD | ascd.org (assessment content) | Research-backed articles, book excerpts | Strong authority, academic credibility | Dense, less actionable for time-strapped teachers |
| TeachThought | teachthought.com/assessment | List-based articles, infographics | Highly shareable, practical examples | Less research backing, lighter authority signals |
| Vanderbilt CFT | cft.vanderbilt.edu | Academic guides, research citations | University credibility (.edu domain) | Higher ed focus, not K-12 specific |
| Understood.org | understood.org/assessment | Parent + teacher dual audience, accessibility focus | Inclusive design, plain language | Less depth for advanced practitioners |

**Citation pattern observation:** AI engines favor sources with (1) clear categorization/structure, (2) specific examples over theory, (3) authority markers (.edu, established non-profits), (4) recently updated content (2023+).

## Internal Assets
- **Existing WG pages on this topic:**
  - [REQUIRES CONTENT AUDIT] — likely have formative assessment mentioned in general assessment content or quiz-building guides
  
- **Related ADPs/resources:**
  - Quiz library tagged with "formative assessment"
  - Lesson builder features that support checks for understanding
  - Poll/survey features for real-time feedback
  - Exit ticket templates
  - Flashcard sets for retrieval practice

- **Related /learn/ hub pages:**
  - `/learn/assessments/` (parent hub)
  - `/learn/assessments/summative-assessment` (comparison point)
  - `/learn/differentiation/` (related strategy content)
  - `/learn/classroom-management/` (implementation context)

- **Enhance existing vs. create new:**
  - **Recommendation: CREATE NEW** comprehensive guide
  - This is a high-volume, foundational topic deserving standalone treatment
  - Can link to existing quiz/lesson builder pages as implementation tools
  - Opportunity to create pillar content for `/learn/assessments/` hub

## AEO Opportunity Score Calculation
```
AI Volume: 9/10
  (High search volume + growing AI query trend as teachers seek quick guidance)
  
× Intent Relevance: 9/10
  (Direct match to information-seeking + how-to intent; high conversion to WG tools)
  
× Brand Fit: 10/10
  (Core to WG's value prop; platform built for formative assessment use cases)
  
= Score: 810 / 1000
```

**Rationale:**
- **High AI volume:** Formative assessment is foundational pedagogy content; every new teacher searches this; experienced teachers search for fresh strategies
- **High relevance:** Intent perfectly matches informational + how-to hybrid content (definition + application)
- **Perfect brand fit:** Wayground's core tools (quizzes, polls, lessons, flashcards) are all formative assessment instruments
- **Quick win potential:** Can link existing 200M+ resources as concrete examples
- **Strategic gap:** Likely under-represented in current WG content; high competitor saturation but opportunity for differentiation through platform integration

---

## Additional Question Clusters Identified
> Related topics for future content development

### Cluster 1: Implementation & Frequency (35 questions)
- How often should I do formative assessments?
- When should I use formative assessment during a lesson?
- How do I find time for formative assessment?

### Cluster 2: Feedback & Data Use (28 questions)
- How do I use formative assessment data?
- What feedback should I give after formative assessment?
- How do I track formative assessment results?

### Cluster 3: Grade-Specific Strategies (42 questions)
- What formative assessment works for kindergarten?
- Formative assessment strategies for high school
- How to adapt formative assessment for different ages?

### Cluster 4: Subject-Specific Application (38 questions)
- Formative assessment for math
- Formative assessment in reading/ELA
- Science formative assessment strategies

### Cluster 5: Technology Integration (31 questions)
- Best digital formative assessment tools
- Formative assessment apps for teachers
- Google Classroom formative assessment
- Online formative assessment strategies

### Cluster 6: Comparison & Context (22 questions)
- Formative vs summative assessment
- Formative assessment vs diagnostic assessment
- Difference between formal and informal formative assessment

**Total questions mined:** 196 questions across 6 clusters
**Prioritization:** Primary content should address main question + Clusters 1, 2, 5 (implementation, feedback, technology) for maximum utility

---

## Research Notes for B3 (Brief Generator)

**Structure recommendation:** 
1. Definition (40-60 word snippet-optimized answer)
2. Why it matters (with research citation)
3. 15 strategies organized by implementation time (< 5 min / 5-15 min / ongoing)
4. How to implement (step-by-step)
5. Digital tools section (natural WG product integration)
6. Common mistakes to avoid
7. FAQ section addressing variant phrasings

**Citation opportunities:**
- Black & Wiliam meta-analysis on formative assessment impact
- Dylan Wiliam's 5 formative assessment strategies framework
- NWEA or similar on assessment frequency
- "Based on 200M+ Wayground resources" for usage data claims

**E-E-A-T signals to include:**
- Teacher SME review/quotes
- "We analyzed X quiz sessions" first-party data
- Link to author page with education credentials
- External research citations (minimum 3-5 authoritative sources)

#### A2 Output
# Citation Audit Report: Formative Assessment Strategies

## Executive Summary
**Topic:** What are formative assessment strategies?  
**Date:** 2026-03-18  
**Methodology:** Competitive content analysis of top education sources likely to be cited by AI engines

---

## Current Citation Landscape

### Tier 1: High-Trust Educational Non-Profits (Most Likely AI Citations)

| Source | Domain | Authority Markers | Why AI Engines Cite |
|--------|--------|-------------------|---------------------|
| **Edutopia** | edutopia.org | George Lucas Educational Foundation, 25+ years, multimedia library | Clear structure, teacher testimonials, practical examples, .org domain, frequent updates |
| **ASCD** | ascd.org | Association for Supervision and Curriculum Development, research-backed | Academic rigor, peer-reviewed content, established authority (1943+), professional membership org |
| **TeachThought** | teachthought.com | Teacher practitioner focus, modern pedagogy | List-based structure (AI-friendly), visual content, frequently updated, engaged community |
| **Understood.org** | understood.org | Non-profit, accessibility focus, reviewed by educators | Plain language, inclusive approach, clear definitions, parent+teacher audience |

### Tier 2: Academic/University Sources

| Source | Domain | Authority Markers | Why AI Engines Cite |
|--------|--------|-------------------|---------------------|
| **Vanderbilt Center for Teaching** | cft.vanderbilt.edu | .edu domain, university credibility | Research citations, academic authority, comprehensive guides |
| **Berkeley Graduate School of Education** | gse.berkeley.edu | Top-tier university, .edu | Research-based, expert faculty authors |
| **University of Waterloo** | uwaterloo.ca/centre-for-teaching-excellence | Canadian .ca domain, teaching center | Structured frameworks, assessment rubrics |

### Tier 3: Government & Research Organizations

| Source | Domain | Authority Markers | Why AI Engines Cite |
|--------|--------|-------------------|---------------------|
| **NWEA** | nwea.org | Research org, assessment specialists | Data-driven insights, research publications |
| **What Works Clearinghouse** | ies.ed.gov/ncee/wwc | U.S. Dept of Education, .gov domain | Evidence standards, peer review, government authority |
| **ETS (Educational Testing Service)** | ets.org | Assessment research leader | Psychometric expertise, established credibility |

---

## Citation Pattern Analysis

### What Makes Sources Get Cited?

**Structural Elements:**
1. **Clear definitions** (40-60 words, snippet-optimized)
2. **Numbered/bulleted lists** of strategies (8-15 items ideal)
3. **Comparison tables** (formative vs. summative)
4. **Step-by-step implementation** guides
5. **Visual elements** (infographics, charts) that AI can reference
6. **FAQ sections** matching question variants

**Authority Signals:**
1. **.edu or .org domains** (trusted over .com)
2. **Author credentials** displayed prominently
3. **Research citations** (especially Dylan Wiliam, Black & Wiliam meta-analysis)
4. **Publication/update dates** (2023+ preferred)
5. **Institutional backing** (universities, professional orgs)

**Content Depth Patterns:**
- **Word count:** 1,800-3,500 words (comprehensive but scannable)
- **Examples:** 10-20 specific strategies with classroom scenarios
- **Data points:** Statistics on effectiveness (effect sizes, improvement metrics)
- **Expert quotes:** Attributed to named researchers or practitioners

---

## Competitor Content Structure Mapping

### Edutopia: "Formative Assessment Strategies" Pattern

**Structure:**
```
1. Opening definition (50-60 words)
2. Why it matters (research + teacher quote)
3. 7-12 strategies organized by:
   - Quick checks (< 5 min)
   - Discussion-based
   - Written/visual
4. Implementation tips sidebar
5. Related resources (internal links)
6. Video embed (teacher demonstration)
```

**Strengths:**
- Multimedia approach (text + video)
- Teacher voice throughout
- Practical, classroom-tested tone
- Strong internal linking

**Weaknesses:**
- Content spread across multiple articles (not one comprehensive guide)
- Limited grade-specific guidance
- Minimal technology integration examples

### ASCD: Research-Heavy Approach

**Structure:**
```
1. Academic framing (learning theory context)
2. Research evidence (multiple citations)
3. Framework presentation (Dylan Wiliam's 5 strategies)
4. Deep dive on 5-8 key strategies
5. Implementation considerations
6. References section
```

**Strengths:**
- High credibility through research
- Theoretical foundation
- Professional development focus

**Weaknesses:**
- Dense academic language
- Less immediately actionable
- Longer read time
- Limited visual elements

### TeachThought: List-Optimized Format

**Structure:**
```
1. Brief intro (2-3 sentences)
2. "20 Formative Assessment Strategies" (numbered list)
3. Each item: Name + 2-3 sentence description
4. Downloadable infographic
5. Social sharing buttons
```

**Strengths:**
- Highly scannable
- Shareable format
- SEO-optimized (list-based)
- Quick reference utility

**Weaknesses:**
- Shallow depth per strategy
- Limited implementation guidance
- Fewer authority signals
- Lighter on research backing

---

## Source Gap Analysis

### What's Missing from Current Top Sources:

**1. Platform-Integrated Examples**
- Current sources describe strategies theoretically
- Missing: "Here's a ready-to-use exit ticket template [link]"
- **WG opportunity:** Link 200M+ resources as concrete implementation tools

**2. Usage Data at Scale**
- Competitors cite research studies (sample sizes: 50-500 teachers)
- Missing: "Based on analysis of 50M+ quiz sessions, we found..."
- **WG opportunity:** First-party data from actual platform usage

**3. Grade-Specific Adaptation Guides**
- Most sources treat K-12 as monolithic
- Missing: Side-by-side comparison "Elementary vs. Middle vs. High School"
- **WG opportunity:** Segmented guidance with age-appropriate examples

**4. Technology Implementation Specifics**
- Sources mention "use digital tools" generically
- Missing: "How to set up a 3-2-1 exit ticket in [specific tool] in 60 seconds"
- **WG opportunity:** Step-by-step tech integration with WG platform

**5. Frequency & Timing Guidance**
- Strategies described, but not when/how often to use them
- Missing: "Use daily checks vs. weekly deeper dives"
- **WG opportunity:** Implementation rhythm recommendations

**6. Common Mistakes Section**
- Most content is prescriptive (do this)
- Missing: "Avoid these 5 formative assessment pitfalls"
- **WG opportunity:** Trouble-shooting based on teacher community insights

**7. Student Engagement Data**
- Claims about effectiveness, but limited student perspective
- Missing: What students report about different formative assessment types
- **WG opportunity:** Student engagement metrics from platform data

---

## Recommended Differentiation Angles for Wayground

### Angle 1: **"Practitioner's Complete Guide"**
- Combine Edutopia's practical tone + ASCD's research backing + TeachThought's structure
- Position as the single comprehensive resource (vs. competitor content scattered across multiple pages)

### Angle 2: **"Implementation Toolkit"**
- Every strategy includes:
  - Time requirement (< 5 min / 5-15 min / ongoing)
  - Grade level fit (K-2 / 3-5 / 6-8 / 9-12)
  - Subject adaptations
  - Digital tool link (WG platform)

### Angle 3: **"Data-Backed Insights"**
- Lead with "Based on 200M+ Wayground resources" throughout
- Use first-party data to validate strategy effectiveness
- "Teachers using daily exit tickets saw X% increase in..."

### Angle 4: **"Teacher-Vetted Content"**
- Incorporate quotes from WG's teacher SME network
- "Real classroom examples from 30+ educators"
- Builds trust + E-E-A-T signals

### Angle 5: **"Quick-Start + Deep-Dive"**
- Snippet-optimized 40-60 word answer at top
- Expandable sections for depth
- Serves both "quick answer" and "comprehensive guide" intents

---

## Domains AI Trusts Where WG Is Absent

### Education Non-Profits (High Trust)
- Edutopia, ASCD, NWEA, Learning Forward, ISTE
- **Gap:** WG not positioned as thought leader in this space

### University Education Departments (High Authority)
- Vanderbilt CFT, Berkeley GSE, Stanford d.school, UW-Madison WCER
- **Gap:** Lack of .edu institutional backing for WG content

### Practitioner Communities (High Engagement)
- TeachThought, Cult of Pedagogy, We Are Teachers, Edutopia's teacher blogs
- **Gap:** WG has resources but not recognized as practitioner knowledge hub

### Research Aggregators (High Credibility)
- What Works Clearinghouse, Best Evidence Encyclopedia, Education Endowment Foundation (UK)
- **Gap:** WG content not cited in research literature

### Assessment Specialists (High Expertise)
- NWEA, ETS, Smarter Balanced, Achieve the Core
- **Gap:** WG has assessment tools but not positioned as assessment expertise source

---

## Structural Patterns of Winners

### Consistent Elements Across Top-Cited Sources:

| Element | % of Top Sources Using | AI Citation Impact |
|---------|------------------------|-------------------|
| Numbered list format | 95% | High (easy extraction) |
| Comparison table (formative vs. summative) | 80% | High (direct answer format) |
| Research citations (Dylan Wiliam, Black & Wiliam) | 75% | High (authority signal) |
| Step-by-step implementation | 70% | Medium (depth signal) |
| FAQ section | 45% | High (matches query variants) |
| Infographic or visual | 60% | Medium (engagement) |
| Expert quotes with attribution | 55% | High (E-E-A-T) |
| Grade-level specificity | 30% | Low (gap opportunity) |
| Technology integration guidance | 40% | Medium (growing) |
| "Common mistakes" section | 15% | Low (gap opportunity) |

---

## Competitive Content Quality Assessment

### Top 5 Sources - Deep Analysis

#### 1. Edutopia: "23 Formative Assessment Strategies"
- **URL pattern:** edutopia.org/article/23-formative-assessment-strategies
- **Word count:** ~2,200
- **Structure:** Definition → Strategy list → Implementation tips
- **Trust signals:** Teacher testimonials, video examples, George Lucas Foundation backing
- **Citation-worthy elements:** Clear categories, specific examples, teacher quotes
- **Weaknesses:** Multiple pages (not single resource), limited research citations
- **Why AI cites:** Practical examples, clear structure, high domain authority

#### 2. ASCD: "Seven Strategies of Assessment for Learning"
- **URL pattern:** ascd.org/articles/seven-strategies-of-assessment-for-learning
- **Word count:** ~3,800
- **Structure:** Research context → Dylan Wiliam framework → Strategy deep-dives → Implementation
- **Trust signals:** Academic citations, peer-reviewed, professional org backing
- **Citation-worthy elements:** Research foundation, theoretical framework, depth
- **Weaknesses:** Dense academic language, less visual, longer read
- **Why AI cites:** Research credibility, framework authority, established org

#### 3. Vanderbilt CFT: "Formative vs. Summative Assessment"
- **URL pattern:** cft.vanderbilt.edu/guides-sub-pages/assessment-101/
- **Word count:** ~1,500
- **Structure:** Definitions → Comparison table → Strategy examples → Resources
- **Trust signals:** .edu domain, university center, faculty expertise
- **Citation-worthy elements:** Clear definitions, comparison table, concise
- **Weaknesses:** Higher ed focus, less K-12 specific, minimal examples
- **Why AI cites:** .edu authority, clear structure, comparison format

#### 4. TeachThought: "27 Easy Formative Assessment Strategies For Gathering Evidence Of Student Learning"
- **URL pattern:** teachthought.com/pedagogy/formative-assessment-strategies/
- **Word count:** ~1,800
- **Structure:** Brief intro → Numbered list (27 items) → Infographic → Related posts
- **Trust signals:** Teacher community, frequent updates, visual content
- **Citation-worthy elements:** Comprehensive list, scannable format, infographic
- **Weaknesses:** Light on research, less depth per item, lighter authority
- **Why AI cites:** List structure (AI-friendly), comprehensive coverage, practical tone

#### 5. Understood.org: "Formative Assessment: What It Is and Why It's Important"
- **URL pattern:** understood.org/articles/formative-assessment
- **Word count:** ~1,200
- **Structure:** Definition → Why it matters → Examples → Tips → FAQ
- **Trust signals:** Non-profit, expert review, accessibility focus
- **Citation-worthy elements:** Plain language, clear examples, FAQ section
- **Weaknesses:** Shorter, less comprehensive, parent-teacher dual focus
- **Why AI cites:** Clear language, FAQ structure, accessibility approach

---

## Recommendations for WG Citation Strategy

### Must-Haves (Table Stakes)
1. ✅ Clear 40-60 word definition in opening paragraph
2. ✅ Numbered list of 12-15 strategies with examples
3. ✅ Comparison table: Formative vs. Summative assessment
4. ✅ Research citations (Dylan Wiliam, Black & Wiliam meta-analysis)
5. ✅ FAQ section covering variant question phrasings
6. ✅ Author credentials + teacher SME review attribution

### Differentiators (WG Unique Value)
1. 🎯 "Based on 200M+ Wayground resources" data claims
2. 🎯 Linked examples to actual ready-to-use WG resources
3. 🎯 Grade-specific adaptation guide (K-2 / 3-5 / 6-8 / 9-12)
4. 🎯 Implementation frequency recommendations
5. 🎯 Technology integration step-by-steps
6. 🎯 Common mistakes troubleshooting section
7. 🎯 Student engagement insights from platform data

### Structural Optimization for AI Citation
1. **Heading structure:** Use question-phrased H2s matching query variants
2. **Answer passages:** Create 40-60 word "citation-ready" paragraphs
3. **Visual hierarchy:** Tables, bullets, numbered lists
4. **Schema markup:** FAQ schema, HowTo schema (technical implementation)
5. **Update frequency:** Establish quarterly review (freshness signal)

---

## Next Steps for B3 (Brief Generator)

**Priority directives:**
1. ✅ Structure content with AI snippet extraction in mind (40-60 word key passages)
2. ✅ Include comparison table early (formative vs. summative) - high citation value
3. ✅ Organize strategies by implementation time (< 5 min / 5-15 min / ongoing)
4. ✅ Link minimum 8-10 WG resources as concrete examples
5. ✅ Include FAQ section addressing all 5 variant phrasings from A1
6. ✅ Specify research citations: Dylan Wiliam framework, Black & Wiliam meta-analysis
7. ✅ Add grade-specific adaptation guidance (differentiator vs. competitors)
8. ✅ Include "common mistakes" section (gap in competitor content)

**Citation-worthy content elements to prioritize:**
- Opening definition paragraph (snippet target)
- Numbered strategy list (AI-friendly structure)
- Comparison table (direct answer format)
- FAQ section (matches query variants)
- Research backing (authority signal)

#### B1 Output

# B1: Intent Classification Output

## Topic
**What are formative assessment strategies?**

---

## Intent Classification

### Primary Intent Type
**Informational + How-to (Hybrid)**

### Signal Analysis
| Query Element | Intent Signal | Classification |
|---------------|---------------|----------------|
| "What are" | Definition-seeking | Informational |
| "formative assessment" | Pedagogical concept | Informational |
| "strategies" | Practical application methods | How-to |

**Rationale:**  
The primary query asks for both conceptual understanding (what formative assessment strategies ARE) and practical application (specific strategies to implement). This dual nature requires hybrid content treatment.

### Variant Intent Analysis
From the 5 variant phrasings:
1. "What are examples of formative assessment strategies?" → **Informational** (examples)
2. "What formative assessment strategies are most effective?" → **Informational + Recommendation** 
3. "How do I use formative assessment strategies in my classroom?" → **How-to** (implementation)
4. "What are the best formative assessment techniques for teachers?" → **Recommendation** (best practices)
5. "What is the difference between formative and summative assessment strategies?" → **Comparison**

**Cluster Assessment:** While variants show mixed intents, the PRIMARY query and highest-volume variants center on Informational + How-to hybrid.

---

## Required Content Format Elements

### Mandatory Elements (Informational Intent)
- ✅ **Definition in opening paragraph** — 40-60 words, snippet-optimized
- ✅ **"Why it matters" section** — importance with research backing
- ✅ **Expansion of concept** — context, theory, pedagogical foundation
- ✅ **FAQ section** — addresses variant question phrasings

### Mandatory Elements (How-to Intent)
- ✅ **Categorized list of strategies** — 12-15 specific strategies organized by implementation time or type
- ✅ **Examples for each strategy** — concrete classroom scenarios
- ✅ **Implementation guidance** — step-by-step how to use each strategy
- ✅ **Timing recommendations** — when and how often to use

### Mandatory Elements (Variant Intents)
- ✅ **Comparison table** — Formative vs. Summative assessment (addresses variant #5)
- ✅ **"Most effective" section** — Research-backed effectiveness data (addresses variant #2)

### Format Structure Recommendation

```
1. Opening Definition (40-60 words) → snippet target
2. Why Formative Assessment Strategies Matter → research context
3. Formative vs. Summative Assessment → comparison table
4. 15 Formative Assessment Strategies → organized by time (<5 min / 5-15 min / ongoing)
   - Each with: Description, Example, Implementation steps, Grade-level notes
5. How to Implement in Your Classroom → step-by-step guide
6. Technology Tools for Formative Assessment → digital implementation
7. Common Mistakes to Avoid → troubleshooting
8. FAQ Section → addresses all 5 variant phrasings
```

### Visual Elements Required
- Comparison table (formative vs. summative)
- Numbered/bulleted strategy lists
- Implementation timeline or frequency guide
- Question-phrased H2 headings

---

## Depth Level Recommendation

**COMPREHENSIVE (2500-4000 words)**

### Justification

| Factor | Assessment | Impact on Depth |
|--------|------------|-----------------|
| **Topic scope** | Foundational pedagogy concept with multiple sub-topics | Requires comprehensive coverage |
| **Audience range** | New teachers + experienced practitioners | Must serve beginner to advanced |
| **Query variants** | 5+ distinct sub-intents in cluster | Each sub-intent needs dedicated section |
| **Competitor benchmark** | Top-cited sources: 1,800-3,800 words | Must match or exceed for citation |
| **Strategic value** | Pillar content for `/learn/assessments/` hub | Warrants definitive guide treatment |
| **Implementation complexity** | Theory + practice + examples + tools | Multi-layered content required |
| **Citation opportunity** | High AI query volume, established competition | Comprehensive = differentiation angle |

**Overview (800-1200 words):** ❌ Insufficient — topic too broad, multiple sub-intents  
**Detailed (1500-2500 words):** ⚠️ Borderline — likely too short for competitive citation  
**Comprehensive (2500-4000 words):** ✅ Appropriate — matches top competitors, allows full coverage

---

## Confidence Score

**HIGH CONFIDENCE**

### Confidence Factors

✅ **Clear intent signals:** "What are" + "strategies" unambiguously indicates informational + how-to  
✅ **Validated by competitor analysis:** All top-cited sources treat as informational + how-to hybrid  
✅ **High query volume:** Established search pattern with clear user expectations  
✅ **Consistent variant phrasings:** All variants confirm need for definition + practical guidance  
✅ **Pedagogical context:** Topic has well-defined treatment patterns in education content  
✅ **No ambiguity:** Not a niche, multi-meaning, or edge-case query

**No flags for human review required.**

---

## Downstream Implications

### For B2 (Content Decomposer)
- Must decompose into: Definition section, Strategy catalog, Implementation guide, Comparison content, FAQ
- Sub-questions should cover: What is it? Why? How? When? What types? How often? What mistakes to avoid?

### For B3 (Brief Generator)
- Use informational + how-to hybrid template
- Prioritize snippet-optimization in opening 40-60 words
- Structure strategy list for AI extraction (numbered, clear hierarchy)
- Include comparison table early (high citation value)
- FAQ section must address all 5 variant phrasings

### For C-Phase (Content Generation)
- Tone: Practical, authoritative, teacher-colleague voice
- Balance: 60% how-to (strategies, examples) / 40% informational (definitions, research)
- Product integration: Natural linking of Wayground tools as implementation examples
- Depth: Each strategy needs 80-120 words (description + example + implementation note)

---

## Classification Summary

| Attribute | Value |
|-----------|-------|
| **Primary Intent** | Informational + How-to (Hybrid) |
| **Format Type** | Definition + Categorized List + Implementation Guide + Comparison Table + FAQ |
| **Depth Level** | Comprehensive (2500-4000 words) |
| **Confidence** | High |
| **Human Review Required** | No |
| **Complexity Flag** | Multi-intent hybrid — requires careful balance of explanation + application |

### Output Template
Use this template for your output:

# Topic Dossier: [Topic Name]

> Stage 1 output — produced by A1, A2, B1, B2 agents

## Metadata
| Field | Value |
|-------|-------|
| Topic | |
| Date created | |
| AEO Opportunity Score | |
| Intent type | |
| Target URL | `/learn/[category]/[topic]` |
| Priority | P1 / P2 / P3 |
| Status | Draft / Ready for Brief |

## Primary Question
**[Main question users ask about this topic]**

### Variant Phrasings
1.
2.
3.
4.
5.

## Intent Classification
- **Type:** Informational / Comparison / Recommendation / How-to / Transactional
- **Required format:** [table / steps / ranking / definition / etc.]
- **Depth level:** Overview / Detailed / Comprehensive

## AI Answer Landscape

### Current Citations (who gets cited?)
| AI Engine | Cited Source | URL | Why Cited (structure/authority/data) |
|-----------|-------------|-----|--------------------------------------|
| ChatGPT | | | |
| Perplexity | | | |
| Google AIO | | | |

### Gaps & Opportunities
- What's missing from current AI answers:
- What WG can uniquely provide:
- Source domains AI trusts but WG is absent from:

## EAR Attribute List
> Sub-questions a comprehensive answer must cover

| # | Attribute / Sub-question | Must-cover? | Covered by competitors? |
|---|--------------------------|-------------|------------------------|
| 1 | | Yes / Nice-to-have | Yes / Partial / No |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

## Competitor Content Analysis

### Top Cited Sources
| Source | URL | Structure | Strengths | Weaknesses |
|--------|-----|-----------|-----------|------------|
| | | | | |
| | | | | |
| | | | | |

## Internal Assets
- Existing WG pages on this topic:
- Related ADPs/resources:
- Related /learn/ hub pages:
- Enhance existing vs. create new:

## AEO Opportunity Score Calculation
```
AI Volume: [1-10]
× Intent Relevance: [1-10]
× Brand Fit: [1-10]
= Score: [X / 1000]
```

---
Now execute your task. Put your final output inside `<output>` tags.
