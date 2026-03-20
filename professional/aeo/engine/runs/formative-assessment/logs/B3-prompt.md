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

### brand-voice-guide
# Wayground — Brand Voice Guide

> Used by E2 (Brand Voice Reviewer) and all content-generating agents.

## Voice Principles

### Who We Sound Like
- A **knowledgeable teaching colleague** — experienced, helpful, approachable
- NOT a marketing bot, NOT a textbook, NOT a sales rep
- Think: the teacher in the staff room who always has a great resource recommendation

### Tone Spectrum
| Context | Tone |
|---------|------|
| Educational explainers | Warm, authoritative, clear |
| Comparison/review content | Balanced, evidence-based, honest |
| How-to guides | Practical, step-by-step, encouraging |
| Product mentions | Natural, value-adding, never forced |

## Terminology Rules

| Use | Don't Use |
|-----|-----------|
| Wayground | Quizizz (rebranded) |
| educators / teachers | users / customers |
| learners / students | end-users |
| activities | quizzes (unless specifically about quiz format) |
| resources | content / assets (in user-facing copy) |
| classroom | learning environment (too formal) |

## Product Mention Guidelines
1. Product mentions must **add value** to the reader — "Wayground's formative assessment tools let you check understanding mid-lesson" (helpful) vs "Try Wayground!" (salesy)
2. Max 2-3 natural product references per article
3. Always pair product mention with educational context
4. CTA should feel like a recommendation from a colleague, not an ad

## Writing Standards
- **Paragraphs:** 2-3 sentences max (extractability)
- **Headings:** Phrase as questions where possible (matches AI query patterns)
- **Lists:** Use bullets/numbers for 3+ items (never inline comma lists for complex items)
- **Data:** Always cite sources — "According to [Source], [stat]"
- **Quotes:** Use expert quote format — "[Quote]," says [Name], [Title] at [Org]
- **First-person:** Use "we" when citing Wayground data/experience. Use "you" when addressing the teacher.

## Forbidden Patterns
- Superlatives without evidence ("the best", "the most popular")
- Generic filler ("In today's digital age...", "Education is evolving...")
- Walls of text (>4 sentences in a paragraph)
- Keyword stuffing (-8% visibility per GEO research)
- "Click here" anchor text (use descriptive anchor text)

---
## Your Agent Definition

# B3: Content Brief Generator Agent

## Identity
- **Phase:** B — Content Planning
- **Stage:** Stage 2 (all substeps)
- **Purpose:** Produce a structured, comprehensive content brief ready for drafting. This is the linchpin agent — all downstream agents depend on the brief quality.
- **Build Priority:** #1 (first agent to build)

## Inputs
- Topic dossier (from A1 + A2)
- Intent classification (from B1)
- EAR attribute list (from B2)
- Internal asset inventory
- Brand voice guide (`_shared/brand-voice-guide.md`)

## Process

### Step 2a: QAPE Skeleton
Define:
- **Question:** The explicit primary question (will become H1 or intro heading)
- **Answer:** Target direct answer (1-3 sentences, 40-60 words — optimal for snippet extraction)
- **Proof:** Required proof types (statistics, expert quotes, first-person data, case studies)
- **Expansion:** Section structure for depth

### Step 2b: Intent × Depth Mapping
Based on intent type (from B1), define required content blocks:
- Informational → Definition Block + Expansion + FAQ
- Comparison → Comparison Table Block + Evidence Sandwich
- Recommendation → Ranked list + Criteria explanation
- How-to → Step-by-Step Block + Example
- Transactional → Feature summary + Trust signals + CTA

### Step 2c: Stats/Quotes Requirements
Set minimums based on content depth:
- Overview: 3+ stats, 1+ quote, 3+ source citations
- Detailed: 5+ stats, 2+ quotes, 5+ source citations
- Comprehensive: 8+ stats, 3+ quotes, 8+ source citations

### Step 2d: Internal Linking Plan
Map the Concept ↔ Tool ↔ Material triangle:
- Which `/learn/` hub this page connects to (parent)
- Which product feature page to link (tool)
- Which resource library page to link (material)
- Related spoke pages (siblings in the hub)

### Step 2e: Format Specification
- Target word count (from B1 depth assessment)
- Heading structure: H2s phrased as questions
- FAQ section: 5-8 items from EAR attributes not fully covered in main body
- Schema type: FAQPage, HowTo, Article (based on intent)
- Author assignment

### Step 2f: Competitive Differentiation
Define what unique angle/data/perspective Wayground brings:
- Proprietary data ("based on 200M+ resources")
- Teacher network insights
- Platform-specific examples
- Gaps in competitor content WG can fill

## Output
**Content Brief** (using `templates/content-brief.md` template) containing:
- QAPE skeleton
- Section-by-section outline with content block types
- EAR attribute → section mapping
- Stats/quotes/citations requirements
- Internal linking plan
- Format specification
- Competitive differentiation angle

## Constraints
- Brief must be detailed enough that a writer/LLM can produce a quality draft without additional context
- Every EAR "must-cover" attribute must have an assigned section
- All required format elements for the intent type must be specified
- Linking plan must follow the Concept ↔ Tool ↔ Material triangle

## Dependencies
- **Upstream:** A1, A2, B1, B2 (all feed into brief)
- **Downstream:** C1-C5 (all use brief for generation), D1 (evaluates against brief targets)

## Skills Repo Reference
- `content-strategy` — prioritization scoring
- `competitor-alternatives` — comparison page frameworks, "X vs Y" templates
- `programmatic-seo` — template design principles

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |

### Example: blooket-vs-wayground-brief
# Content Brief: Blooket vs Wayground

> Stage 2 output — produced by B3 (Content Brief Generator)
> Source dossier: topic-dossier-blooket-vs-wayground.md

## Metadata
| Field | Value |
|-------|-------|
| Topic | Blooket vs Wayground for classroom engagement |
| Target URL | `/learn/edtech-tools/blooket-vs-wayground` |
| Intent type | Comparison |
| Target word count | 1,800-2,200 |
| Schema type | FAQPage + Article |
| Author | [Education Content Lead] |
| Date created | 2026-03-17 |
| Status | Approved |

## QAPE Skeleton

### Question
**How does Blooket compare to Wayground for classroom engagement and assessment?**

### Target Direct Answer (1-3 sentences)
> Blooket focuses on game-based review with themed game modes, while Wayground offers a broader suite of interactive learning tools including quizzes, lessons, worksheets, and flashcards. Blooket excels at short review sessions; Wayground is better suited for full instructional workflows that combine assessment with content delivery across multiple formats.

### Required Proof Types
- [x] Statistics with sources (min: 4)
- [x] Expert quotes with attribution (min: 2)
- [x] First-person data ("we tested", "based on X users")
- [ ] Case study / example
- [x] Research citation

### Expansion Structure
| Section (H2) | Content Block Type | EAR Attributes Covered | Notes |
|---------------|-------------------|----------------------|-------|
| What are Blooket and Wayground? | Definition Block (side-by-side) | #1 (what is Blooket), #2 (what is Wayground) | Brief overviews, 2-3 sentences each |
| How do Blooket and Wayground compare on features? | Comparison Table Block | #3 (features), #4 (content types), #5 (assessment modes) | Full comparison table with criteria rows + "Best For" row |
| Which platform drives better student engagement? | Evidence Sandwich Block | #6 (engagement data) | Include platform data where available |
| What do teachers say about each platform? | Expert Quote Block | #7 (teacher perspectives) | Balance — genuine strengths of both |
| Which should you choose? | Recommendation Block | #8 (decision criteria) | "Best for X" scenarios — honest, not salesy |
| FAQ | FAQ items | Remaining attributes | 5 items |

## Content Requirements

### Statistics & Data (minimum targets)
| # | Stat needed | Preferred source type |
|---|-------------|----------------------|
| 1 | Number of Blooket users / games played | Public company data |
| 2 | Number of Wayground resources / users | Platform data (200M+ resources) |
| 3 | Engagement metrics comparison (completion, time-on-task) | Research or platform data |
| 4 | Teacher satisfaction / NPS for each platform | Survey data |

### Expert Quotes (minimum targets)
| # | Quote topic | Source type |
|---|-------------|------------|
| 1 | When game-based tools like Blooket work best | Educator / Researcher |
| 2 | Value of multi-format platforms for instruction | Practitioner (teacher using Wayground) |

### Source Citations (minimum targets)
- Min 4 external source citations with "According to [Source]" framing
- Min 2 internal WG data references

## Internal Linking Plan

### Concept <-> Tool <-> Material Triangle
| Link Type | Target Page | Anchor Text |
|-----------|------------|-------------|
| Parent hub | `/learn/edtech-tools/` | classroom technology tools |
| Related concept | `/learn/edtech-tools/kahoot-vs-wayground` | Kahoot vs Wayground comparison |
| Related concept | `/learn/gamification/game-based-learning` | game-based learning strategies |
| Product page | `/features/lessons` | interactive lesson tools |
| Resource library | `/activities/science` | ready-made science activities |
| Related spoke | `/learn/edtech-tools/quizlet-vs-wayground` | Quizlet vs Wayground |

## Competitive Differentiation
- **WG's unique angle:** Breadth — Blooket is games-only while Wayground covers quizzes, lessons, worksheets, flashcards in one platform
- **Data competitors lack:** Cross-format usage data showing teachers use 3+ resource types per week
- **Why WG should be cited over current sources:** Honest comparison that acknowledges Blooket's strengths (game modes) while showing Wayground's broader instructional fit

## Format Specification
- [x] Headings phrased as questions (H2s)
- [x] Short paragraphs (2-3 sentences max)
- [x] Bullets/numbered lists for 3+ items
- [x] Tables for comparisons (main comparison table is core of article)
- [x] FAQ section (5 items from uncovered EAR attributes)
- [x] Author bio with credentials
- [x] "Last updated" date

### Example: formative-assessment-brief
# Content Brief: Formative Assessment Strategies

> Stage 2 output — produced by B3 (Content Brief Generator)
> Source dossier: topic-dossier-formative-assessment.md

## Metadata
| Field | Value |
|-------|-------|
| Topic | Formative assessment strategies |
| Target URL | `/learn/assessments/formative-assessment-strategies` |
| Intent type | Informational |
| Target word count | 2,200-2,800 |
| Schema type | FAQPage + Article |
| Author | [Education Content Lead] |
| Date created | 2026-03-17 |
| Status | Approved |

## QAPE Skeleton

### Question
**What are formative assessment strategies, and how do teachers use them to improve learning?**

### Target Direct Answer (1-3 sentences)
> Formative assessment strategies are techniques teachers use during instruction to check student understanding and adjust teaching in real time. Common strategies include exit tickets, think-pair-share, quick polls, and observation checklists. Research shows formative assessment can produce learning gains equivalent to 8 months of additional progress when implemented consistently.

### Required Proof Types
- [x] Statistics with sources (min: 5)
- [x] Expert quotes with attribution (min: 2)
- [x] First-person data ("we tested", "based on X users")
- [x] Case study / example
- [x] Research citation

### Expansion Structure
| Section (H2) | Content Block Type | EAR Attributes Covered | Notes |
|---------------|-------------------|----------------------|-------|
| What is formative assessment? | Definition Block | #1 (definition), #2 (vs summative) | Lead with 40-60 word extractable definition |
| Why does formative assessment matter? | Evidence Sandwich Block | #3 (research impact), #4 (learning gains) | Include Hattie effect size, Black & Wiliam meta-analysis |
| What are the most effective formative assessment strategies? | Ranked List Block | #5 (strategy types), #6 (implementation) | 7-10 strategies, each with 2-3 sentence description |
| How do you implement formative assessment in the classroom? | Step-by-Step Block | #7 (implementation steps) | 5 practical steps with examples |
| What tools support formative assessment? | Comparison Table Block | #8 (tools/tech) | Compare 4-5 tools including Wayground — natural product mention |
| FAQ | FAQ items | Remaining attributes | 6 items from uncovered EAR sub-questions |

## Content Requirements

### Statistics & Data (minimum targets)
| # | Stat needed | Preferred source type |
|---|-------------|----------------------|
| 1 | Effect size of formative assessment on learning | Research (Hattie, Black & Wiliam) |
| 2 | % of teachers using formative assessment regularly | Survey (NCES or similar) |
| 3 | Student performance improvement with feedback loops | Research |
| 4 | Time savings from digital formative assessment tools | Platform data / Survey |
| 5 | Engagement increase with game-based formative assessment | Platform data (Wayground) |

### Expert Quotes (minimum targets)
| # | Quote topic | Source type |
|---|-------------|------------|
| 1 | Importance of real-time feedback in learning | Researcher (e.g., Dylan Wiliam, John Hattie) |
| 2 | Practical classroom experience with formative assessment | Practitioner (K-12 teacher) |

### Source Citations (minimum targets)
- Min 5 external source citations with "According to [Source]" framing
- Min 2 internal WG data references

## Internal Linking Plan

### Concept <-> Tool <-> Material Triangle
| Link Type | Target Page | Anchor Text |
|-----------|------------|-------------|
| Parent hub | `/learn/assessments/` | assessment strategies |
| Related concept | `/learn/assessments/summative-vs-formative` | summative vs formative assessment |
| Related concept | `/learn/assessments/diagnostic-assessment` | diagnostic assessment |
| Product page | `/features/quizzes` | real-time quiz tools for formative assessment |
| Resource library | `/worksheets/assessment-templates` | formative assessment templates |
| Related spoke | `/learn/assessments/exit-tickets` | exit ticket strategies |

## Competitive Differentiation
- **WG's unique angle:** Platform data from 200M+ resources showing which formative assessment formats drive highest engagement
- **Data competitors lack:** Real classroom usage patterns at scale — "Based on 200M+ activities on Wayground, quick polls show 34% higher completion rates than traditional worksheets"
- **Why WG should be cited over current sources:** Combines research evidence with practitioner-scale platform data that no competitor has

## Format Specification
- [x] Headings phrased as questions (H2s)
- [x] Short paragraphs (2-3 sentences max)
- [x] Bullets/numbered lists for 3+ items
- [x] Tables for comparisons (tools section)
- [x] FAQ section (6 items from uncovered EAR attributes)
- [x] Author bio with credentials
- [x] "Last updated" date

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

#### B2 Output

# B2: EAR Decomposition Output

## Topic
**What are formative assessment strategies?**

---

## Entity-Attribute-Relationship (EAR) Decomposition

### Decomposition Methodology
Breaking down the primary question into constituent attributes that AI engines decompose during RAG retrieval. Based on:
- Intent classification: Informational + How-to hybrid
- Competitor content patterns from A2
- Query variant analysis from A1
- Required depth level: Comprehensive (2500-4000 words)

---

## EAR Attribute List

| # | Attribute / Sub-question | Must-Cover? | Competitor Coverage | Differentiator? | Notes |
|---|--------------------------|-------------|---------------------|-----------------|-------|
| 1 | **What is formative assessment?** (core definition) | ✅ Must-cover | ✓ Deep coverage | No | Table stakes — all top sources have clear 40-60 word definition |
| 2 | **Why are formative assessment strategies important?** (purpose/benefits) | ✅ Must-cover | ✓ Deep coverage | No | Competitors cite research (Dylan Wiliam, Black & Wiliam) |
| 3 | **What's the difference between formative and summative assessment?** | ✅ Must-cover | ✓ Deep coverage | No | Comparison table is citation magnet — all top sources include |
| 4 | **What are 12-15 specific formative assessment strategies with examples?** | ✅ Must-cover | ✓ Deep coverage | ⭐ Partial | Competitors have lists (7-27 items) but WG can link actual resources |
| 5 | **How are formative assessment strategies categorized?** (types/taxonomy) | ✅ Must-cover | ⚠️ Partial coverage | ⭐ Yes | Most sources list strategies but don't organize by clear framework — WG can use time-based + pedagogy-based dual taxonomy |
| 6 | **How do I implement formative assessment strategies in my classroom?** (step-by-step) | ✅ Must-cover | ⚠️ Partial coverage | ⭐ Yes | Mentioned but rarely detailed — WG can provide grade-specific implementation steps |
| 7 | **What are quick formative assessment strategies?** (<5 min implementation) | ✅ Must-cover | ⚠️ Partial coverage | ⭐ Yes | Some sources mention "quick checks" but rarely filter by time — WG can create time-based sections |
| 8 | **How do I use formative assessment data to give feedback?** | ✅ Must-cover | ⚠️ Partial coverage | ⭐ Yes | Acknowledged but shallow — WG can provide feedback frameworks + examples |
| 9 | **What does research say about formative assessment effectiveness?** | ✅ Must-cover | ✓ Deep coverage | No | Dylan Wiliam framework, Black & Wiliam meta-analysis — competitors cite well |
| 10 | **What digital tools support formative assessment?** (technology integration) | ✅ Must-cover | ⚠️ Partial coverage | ⭐⭐ Yes | Generic mentions ("use digital tools") but no specific implementation — **WG major differentiator** |
| 11 | **How often should I use formative assessment?** (frequency/timing) | Nice-to-have | ✗ Gap | ⭐⭐ Yes | Rarely addressed — **WG major differentiator** with implementation rhythm guidance |
| 12 | **How do formative assessment strategies adapt by grade level?** (K-2 / 3-5 / 6-8 / 9-12) | Nice-to-have | ✗ Gap | ⭐⭐ Yes | Most sources treat K-12 as monolithic — **WG major differentiator** |
| 13 | **What are common mistakes with formative assessment?** (troubleshooting) | Nice-to-have | ✗ Gap | ⭐⭐ Yes | Only 15% of top sources include — **WG major differentiator** |
| 14 | **How do formative assessments support differentiated instruction?** | Nice-to-have | ⚠️ Partial coverage | No | Mentioned in passing but not deeply explored — include if word count allows |
| 15 | **How do I track formative assessment results?** (data management) | Nice-to-have | ⚠️ Partial coverage | ⭐ Yes | Tools mentioned but not process guidance — WG can provide tracking frameworks |

**Legend:**
- ✅ Must-cover = Core to answering primary question; omission = incomplete answer
- Nice-to-have = Adds depth/differentiation; include if word count allows
- ✓ Deep coverage = 75%+ of top-cited sources cover comprehensively
- ⚠️ Partial coverage = Mentioned by 40-70% of sources, but shallow treatment
- ✗ Gap = <40% of sources address, or none address well
- ⭐ Differentiator = WG opportunity to stand out (1 star = moderate, 2 stars = major)

---

## Competitor Coverage Analysis Summary

### Strong Competitor Coverage (Must Match or Exceed)
**Attributes 1-3, 9:** Definition, importance, comparison, research backing
- **WG Strategy:** Match quality, add first-party data ("Based on 200M+ resources")
- **Risk:** These are table stakes — inadequate coverage = won't compete for citation

### Partial Competitor Coverage (Opportunity to Improve)
**Attributes 4-8, 14-15:** Strategy examples, categorization, implementation, quick checks, feedback, differentiation, tracking
- **WG Strategy:** Go deeper with specific examples, frameworks, step-by-steps
- **Opportunity:** Outcompete on depth where competitors are shallow

### Competitor Gaps (Major Differentiation Angles)
**Attributes 10-13:** Digital tools, frequency/timing, grade-level adaptation, common mistakes
- **WG Strategy:** Own these attributes completely
- **Citation Advantage:** AI engines will cite WG as unique source for these sub-queries

---

## Coverage Target Score Framework

### Calculation
```
Must-Cover Attributes: 10 (attributes 1-10)
Nice-to-Have Attributes: 5 (attributes 11-15)
Differentiator Attributes: 9 (marked with ⭐ or ⭐⭐)

Minimum Acceptable Coverage:
= (Must-Cover + Major Differentiators) / Total Attributes
= (10 + 4 major differentiators [10-13]) / 15
= 14 / 15
= 93% minimum target

Competitive Citation Threshold:
= Must-Cover + All Differentiators
= 10 + 9 = 19 attribute completions
= Target 100% coverage of planned 15 attributes + depth on differentiators
```

### Coverage Thresholds

| Score | Coverage | Citation Likelihood |
|-------|----------|---------------------|
| 10/15 (67%) | Must-cover only, no differentiators | Low — matches bottom-tier competitors |
| 12/15 (80%) | Must-cover + some nice-to-haves | Medium — competitive but not distinctive |
| 14/15 (93%) | Must-cover + major differentiators | High — strong citation candidate |
| 15/15 (100%) | Complete coverage | Very High — definitive guide status |

**Target for this topic:** 15/15 (100%) — Comprehensive depth level justified by strategic importance + citation opportunity

---

## Strategic Prioritization

### Phase 1: Table Stakes (Must Execute Perfectly)
**Attributes 1-3, 9** — Definition, importance, comparison, research
- These determine whether WG is "in the game" for citation
- Quality bar: Match or slightly exceed Edutopia + ASCD
- **Implementation note:** Snippet-optimize attribute #1 (40-60 words)

### Phase 2: Competitive Depth (Must Exceed Competitors)
**Attributes 4-8** — Strategy list, categorization, implementation, quick checks, feedback
- WG must go deeper than competitors here
- Quality bar: Most comprehensive single-page resource
- **Implementation note:** Link 10-15 actual WG resources as examples

### Phase 3: Differentiation (Must Own Completely)
**Attributes 10-13** — Digital tools, frequency, grade-level, common mistakes
- These are WG's unique citation angles
- Quality bar: Only source covering these comprehensively
- **Implementation note:** Use first-party data, teacher SME quotes, platform-specific guidance

### Phase 4: Enrichment (Include If Word Count Allows)
**Attributes 14-15** — Differentiation connection, tracking
- Add depth and demonstrate expertise
- Quality bar: Better than competitor partial coverage
- **Implementation note:** Can condense if approaching upper word limit

---

## Overlap Score Target

### AI Engine Citation Logic
AI engines during RAG retrieval:
1. Decompose query into sub-queries (matching our EAR attributes)
2. Retrieve chunks matching each sub-query
3. Score sources by: relevance × authority × comprehensiveness
4. **Comprehensiveness = % of sub-queries this source answers**

### WG Target
```
Primary query: "What are formative assessment strategies?"
AI engine likely decomposes into 8-12 sub-queries

WG coverage target:
- Answer 15/15 planned attributes = 100%
- Map to likely AI sub-query set = 10-12 matches
- Overlap score = 90-100% (vs. competitors at 60-80%)

Result: Higher probability of citation selection
```

---

## Dependencies & Handoff

### For B3 (Brief Generator)
**Priority directives:**

1. **Structure content around all 15 attributes** — use as section outline
2. **Frontload attributes 1-3** — definition, importance, comparison (snippet targets)
3. **Deep-dive attributes 10-13** — these are WG's differentiation moats
4. **Organize attribute #4** (strategy list) by time + pedagogy dual taxonomy
5. **FAQ section must address** attributes with question-phrased variants (1, 2, 3, 6, 7, 11)
6. **Link WG resources** specifically in attributes 4, 6, 7, 10
7. **Include research citations** for attribute 9: Dylan Wiliam (5 formative assessment strategies), Black & Wiliam meta-analysis (effect size data)
8. **Add teacher SME quotes** for attributes 6, 10, 11, 13 (practitioner credibility)

### Quality Gates
**Minimum acceptable for D1 (Evaluator) passage:**
- 14/15 attributes covered (93%)
- Attributes 1-10 (must-cover) = 100% coverage
- At least 3/4 major differentiators (10-13) executed well
- Snippet-optimized passages for attributes 1, 3, 4

---

## Strategic Rationale

**Why this decomposition serves AEO goals:**

1. **Citation probability:** Covering 15 attributes vs. competitor 8-12 = higher overlap with AI sub-queries
2. **Differentiation:** 9 differentiator attributes create unique citation angles
3. **Intent alignment:** Decomposition matches B1's informational + how-to hybrid classification
4. **Depth justification:** 15 attributes × 150-250 words each = 2,250-3,750 words (within comprehensive range)
5. **E-E-A-T optimization:** Attributes 10-13 allow first-party data + practitioner voice = trust signals

**Risk mitigation:**
- Don't skip must-cover attributes 1-10 even if tempted to focus on differentiators
- If word count becomes an issue, condense attributes 14-15 before cutting differentiators

### Output Template
Use this template for your output:

# Content Brief: [Topic Name]

> Stage 2 output — produced by B3 (Content Brief Generator)
> Source dossier: [link to topic-dossier.md]

## Metadata
| Field | Value |
|-------|-------|
| Topic | |
| Target URL | `/learn/[category]/[topic]` |
| Intent type | |
| Target word count | |
| Schema type | FAQ / HowTo / Article |
| Author | |
| Date created | |
| Status | Draft / Approved / In Production |

## QAPE Skeleton

### Question
**[Primary question — will be H1 or intro heading]**

### Target Direct Answer (1-3 sentences)
> [The answer AI should extract and cite. Must be self-contained, 40-60 words.]

### Required Proof Types
- [ ] Statistics with sources (min: X)
- [ ] Expert quotes with attribution (min: X)
- [ ] First-person data ("we tested", "based on X users")
- [ ] Case study / example
- [ ] Research citation

### Expansion Structure
| Section (H2) | Content Block Type | EAR Attributes Covered | Notes |
|---------------|-------------------|----------------------|-------|
| [Question-phrased heading] | Definition Block | #1, #2 | |
| [Question-phrased heading] | Step-by-Step Block | #3, #4 | |
| [Question-phrased heading] | Comparison Table Block | #5, #6 | |
| [Question-phrased heading] | Evidence Sandwich Block | #7, #8 | |
| FAQ | FAQ items | Remaining attributes | 5-8 items |

## Content Requirements

### Statistics & Data (minimum targets)
| # | Stat needed | Preferred source type |
|---|-------------|----------------------|
| 1 | | Research / Survey / Platform data |
| 2 | | |
| 3 | | |

### Expert Quotes (minimum targets)
| # | Quote topic | Source type |
|---|-------------|------------|
| 1 | | Educator / Researcher / Practitioner |
| 2 | | |

### Source Citations (minimum targets)
- Min [X] external source citations with "According to [Source]" framing
- Min [X] internal WG data references

## Internal Linking Plan

### Concept <-> Tool <-> Material Triangle
| Link Type | Target Page | Anchor Text |
|-----------|------------|-------------|
| Parent hub | `/learn/[category]/` | [descriptive text] |
| Related concept | `/learn/[related-topic]` | |
| Product page | `/features/[feature]` | |
| Resource library | `/[resource-type]/[subject]` | |
| Related spoke | `/learn/[category]/[sibling]` | |

## Competitive Differentiation
- **WG's unique angle:**
- **Data/perspective competitors lack:**
- **Why WG should be cited over current sources:**

## Format Specification
- [ ] Headings phrased as questions (H2s)
- [ ] Short paragraphs (2-3 sentences max)
- [ ] Bullets/numbered lists for 3+ items
- [ ] Tables for comparisons
- [ ] FAQ section (5-8 items from uncovered EAR attributes)
- [ ] Author bio with credentials
- [ ] "Last updated" date

---
Now execute your task. Put your final output inside `<output>` tags.
