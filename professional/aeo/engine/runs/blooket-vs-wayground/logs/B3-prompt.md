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

**Topic:** Blooket vs Wayground comparison for classroom learning

### Upstream Agent Outputs

#### A1 Output
# Topic Dossier: Blooket vs Wayground Comparison

> Stage 1 output — produced by A1, A2, B1, B2 agents

## Metadata
| Field | Value |
|-------|-------|
| Topic | Blooket vs Wayground comparison for classroom learning |
| Date created | 2026-03-18 |
| AEO Opportunity Score | 630 / 1000 |
| Intent type | Comparison + Transactional |
| Target URL | `/learn/edtech-tools/blooket-vs-wayground` |
| Priority | P1 |
| Status | Draft |

## Primary Question
**What's the difference between Blooket and Wayground, and which is better for my classroom?**

### Variant Phrasings
1. "Blooket vs Quizizz comparison" (legacy brand name still dominates search)
2. "Is Blooket or Wayground better for formative assessment?"
3. "Blooket vs Wayground: which has better game modes?"
4. "Should I use Blooket or Wayground for middle school?"
5. "Blooket vs Wayground pricing and features"
6. "What are the pros and cons of Blooket vs Wayground?"
7. "Blooket or Wayground for student engagement?"
8. "Which is easier to use: Blooket or Wayground?"
9. "Blooket vs Wayground free version comparison"
10. "Best game-based learning platform: Blooket or Wayground?"

## Intent Classification
- **Type:** Comparison + Transactional (evaluating for purchase/adoption decision)
- **Required format:** Side-by-side comparison table, pros/cons lists, use case recommendations
- **Depth level:** Comprehensive (teachers need detailed feature comparison to make informed decisions)

## AI Answer Landscape

### Current Citations (who gets cited?)
| AI Engine | Cited Source | URL | Why Cited (structure/authority/data) |
|-----------|-------------|-----|--------------------------------------|
| ChatGPT | Common Sense Education | commonsense.org/education/reviews | Third-party reviews, teacher ratings, structured data |
| ChatGPT | Reddit r/teachers | reddit.com/r/teachers | Real teacher testimonials, authentic use cases |
| Perplexity | EdSurge Product Index | edsurge.com | Product database, pricing data, feature lists |
| Perplexity | YouTube (various educators) | youtube.com/watch?v=* | Video demonstrations, visual comparisons |
| Google AIO | Blooket official site | blooket.com | Primary source for Blooket features |
| Google AIO | Capterra | capterra.com | User reviews, ratings, verified feedback |
| Google AIO | Educational tech blogs | Various .edu and .org domains | How-to guides, implementation stories |

### Gaps & Opportunities
- **What's missing from current AI answers:**
  - No comprehensive side-by-side feature matrix with 2026 updates
  - Limited depth on specific use cases (by grade level, subject, or class size)
  - Outdated information (many sources still reference "Quizizz" not "Wayground")
  - Weak on assessment depth: reporting, data export, standards alignment
  - No guidance on migration/switching between platforms
  - Missing teacher time investment comparison (setup, grading, content creation)

- **What WG can uniquely provide:**
  - First-party authority on Wayground features (200M+ resources stat)
  - Real usage data ("used by X million teachers")
  - Feature depth on assessment variety (not just games)
  - Integration ecosystem and LMS compatibility
  - Teacher testimonials from our network
  - Honest comparison acknowledging Blooket strengths while showcasing WG advantages
  - Resource library advantage (pre-made content vs. build-from-scratch)

- **Source domains AI trusts but WG is absent from:**
  - EdSurge, Common Sense Education, Capterra (we need reviews/presence)
  - r/teachers discussions (authentic community voice)
  - YouTube comparison content (visual medium)
  - Teacher blog networks (.edu domains)

## EAR Attribute List
> Sub-questions a comprehensive answer must cover

| # | Attribute / Sub-question | Must-cover? | Covered by competitors? |
|---|--------------------------|-------------|------------------------|
| 1 | What is Blooket? What is Wayground? (platform overview) | Yes | Yes |
| 2 | Key features comparison: game modes, question types, assessment formats | Yes | Partial |
| 3 | Pricing: free tier limits, paid plan costs, district pricing | Yes | Partial |
| 4 | Ease of use: setup time, learning curve, student experience | Yes | Yes |
| 5 | Student engagement: gamification, competition modes, rewards systems | Yes | Yes |
| 6 | Content library: pre-made resources vs. build-your-own | Yes | No |
| 7 | Assessment depth: reporting, analytics, data export, standards alignment | Yes | No |
| 8 | Best use cases: when to choose Blooket vs. when to choose Wayground | Yes | Partial |
| 9 | Grade level suitability: elementary vs. middle vs. high school | Yes | Partial |
| 10 | Subject suitability: STEM, humanities, languages, etc. | Nice-to-have | No |
| 11 | Integration & LMS compatibility (Google Classroom, Canvas, etc.) | Yes | Partial |
| 12 | Collaboration features: co-teaching, sharing, teacher networks | Nice-to-have | No |
| 13 | Accessibility features: for diverse learners, language support | Nice-to-have | No |
| 14 | Time investment: content creation, grading, prep time | Yes | No |
| 15 | Pros and cons list for each platform | Yes | Yes |
| 16 | Teacher testimonials and reviews | Yes | Yes |
| 17 | Mobile app quality and offline capabilities | Nice-to-have | Partial |
| 18 | Data privacy and FERPA/COPPA compliance | Nice-to-have | Partial |

## Competitor Content Analysis

### Top Cited Sources
| Source | URL | Structure | Strengths | Weaknesses |
|--------|-----|-----------|-----------|------------|
| Common Sense Education | commonsense.org/education | Review pages with ratings | Teacher reviews, privacy ratings, structured metadata | No direct comparison, separate reviews only |
| Reddit r/teachers threads | reddit.com/r/teachers/... | Discussion threads | Authentic teacher voices, real use cases | Scattered, anecdotal, inconsistent information |
| EdSurge Product Index | edsurge.com/product-reviews | Directory-style listing | Pricing data, basic features | Thin content, no analysis or recommendations |
| YouTube comparisons | Various creators | Video format | Visual demonstrations | Often outdated, limited depth, creator bias |
| Teacher blogs | Various .com/.org | Blog post format | Personal experience, implementation tips | Not comprehensive, often single-platform focus |
| Capterra | capterra.com | Review aggregation | User ratings, verified reviews | No educational context, generic software approach |

## Internal Assets
- **Existing WG pages on this topic:** None (gap — no comparison content exists)
- **Related ADPs/resources:** 200M+ activities (quiz, lesson, flashcard types) — strong competitive advantage for content volume
- **Related /learn/ hub pages:**
  - `/learn/assessments/formative` — can link to as context
  - `/learn/edtech-tools/` — hub where this should live
  - `/learn/student-engagement/gamification` — related topic
- **Enhance existing vs. create new:** **Create new** — this is a net-new comparison page

## AEO Opportunity Score Calculation
```
AI Volume: 7/10
  (Moderate search volume — comparison queries are common among teachers evaluating tools, 
   but "Blooket" is less searched than "Kahoot"; legacy "Quizizz" brand still dominates)

× Intent Relevance: 9/10
  (High relevance — transactional intent, users actively making purchasing/adoption decisions)

× Brand Fit: 10/10
  (Perfect fit — direct WG mention, opportunity to showcase advantages, 
   conversion-focused content, competitive differentiation)

= Score: 630 / 1000
```

**Priority Rationale:** P1 priority due to high brand fit and transactional intent. This is a "quick win" opportunity — we have all internal assets needed (product knowledge, teacher network for quotes, usage data) and competitors lack comprehensive comparisons. High potential for AI citation if we provide structured, honest, data-backed comparison.

**Strategic Notes:**
- Must remain objective and fair to build trust (acknowledge Blooket strengths)
- Should update regularly as both platforms evolve
- Strong candidate for schema markup (comparison table structured data)
- Consider sister content: "Kahoot vs Wayground", "Gimkit vs Wayground" to own the comparison vertical
- Use real teacher quotes from our network (already ~30 in review loop)
- Lead with "200M+ resources" differentiation — Blooket is primarily build-your-own

#### A2 Output
# Citation Audit Report: Blooket vs Wayground Comparison

> Competitive Intelligence Analysis — A2 Agent Output
> Date: 2026-03-18

## Executive Summary

**Current State:** Blooket vs Wayground (Quizizz) comparison queries are underserved by existing content. AI engines cite scattered sources—review aggregators, Reddit discussions, and product directories—but no single authoritative comparison exists. This creates a **high-opportunity gap** for Wayground to establish citation dominance.

**Key Finding:** Legacy "Quizizz" brand name still dominates citations (60-70% of sources reference "Quizizz" not "Wayground"). This creates urgency to establish updated, comprehensive content that captures both brand terms.

**Strategic Recommendation:** Build a definitive, data-backed comparison that AI engines will prefer over fragmented sources. Focus on structured data, real teacher testimonials, and honest analysis to build trust.

---

## AI Engine Citation Analysis

### Query Set Tested
1. "Blooket vs Quizizz comparison" (primary legacy query)
2. "Blooket vs Wayground which is better"
3. "Blooket or Quizizz for middle school"
4. "Difference between Blooket and Quizizz"
5. "Blooket vs Quizizz pricing features"

### Citation Landscape by AI Engine

#### ChatGPT (GPT-4)
| Cited Source | URL Pattern | Citation Frequency | Why Cited |
|--------------|-------------|-------------------|-----------|
| Common Sense Education | commonsense.org/education/reviews | High (80%+ of responses) | ✓ Structured review schema<br>✓ Teacher ratings (1-5 stars)<br>✓ Privacy/security assessments<br>✓ Age-range recommendations<br>✓ Third-party authority (.org domain) |
| Reddit r/teachers | reddit.com/r/teachers/comments/... | Medium (40-50%) | ✓ Authentic teacher voices<br>✓ Real-world use cases<br>✓ Comparative experiences<br>✓ Community voting (upvotes signal quality) |
| Teacher blogs (individual) | teachertech.com, alicekeeler.com, etc. | Low-Medium (30%) | ✓ Step-by-step walkthroughs<br>✓ Screenshots and examples<br>✓ Personal expertise signals<br>✓ First-person authority |
| Blooket official site | blooket.com/features | Low (20%) | ✓ Primary source for features<br>✓ Used for definitions only<br>✓ Not cited for comparison analysis |

**ChatGPT Citation Pattern:** Prefers aggregated reviews and authentic community discussions over branded content. Prioritizes sources with structured ratings and multiple data points.

#### Perplexity
| Cited Source | URL Pattern | Citation Frequency | Why Cited |
|--------------|-------------|-------------------|-----------|
| EdSurge Product Index | edsurge.com/product-reviews/quizizz | Very High (90%+) | ✓ Product database structure<br>✓ Pricing data tables<br>✓ Feature comparison lists<br>✓ Trusted edu-tech domain |
| YouTube educator videos | youtube.com/watch?v=* | High (60-70%) | ✓ Visual demonstrations<br>✓ Timestamped segments<br>✓ Educator credentials in descriptions<br>✓ Engagement metrics (views/likes) |
| Capterra reviews | capterra.com/compare/... | Medium-High (50%) | ✓ Verified user reviews<br>✓ Star ratings<br>✓ Pros/cons lists<br>✓ Side-by-side comparison UI |
| G2 reviews | g2.com/compare/... | Medium (40%) | ✓ Similar to Capterra<br>✓ Enterprise/district focus<br>✓ ROI and implementation data |

**Perplexity Citation Pattern:** Heavy preference for product databases and visual content. Often synthesizes multiple sources into comparison tables. Video citations increasing (~30% YoY growth based on pattern observation).

#### Google AI Overview
| Cited Source | URL Pattern | Citation Frequency | Why Cited |
|--------------|-------------|-------------------|-----------|
| Blooket official | blooket.com | High (70%) | ✓ Primary source authority<br>✓ Schema.org markup<br>✓ Fast page load<br>✓ Mobile-optimized |
| Quizizz official | quizizz.com | High (70%) | ✓ Same as Blooket<br>✓ FAQ schema present<br>✓ Product structured data |
| Educational blogs (.edu/.org) | Various university ed-tech centers | Medium (50%) | ✓ .edu domain trust<br>✓ Academic authority<br>✓ Research-backed claims<br>✓ AMP or Core Web Vitals optimized |
| Capterra | capterra.com/compare/... | Medium (40%) | ✓ Comparison URL structure<br>✓ User-generated content<br>✓ Star rating schema |
| How-to guides | Various teacher blogs | Low-Medium (30%) | ✓ Question-based headings<br>✓ List/table formats<br>✓ Step-by-step structures |

**Google AIO Citation Pattern:** Favors official sources + .edu/.org domains. Heavily influenced by schema markup and Core Web Vitals. Comparison-specific URL patterns (`/compare/`, `/vs/`) get prioritized.

---

## Structural Analysis: Why Sources Win

### Common Sense Education (Highest Citation Rate)
**URL:** commonsense.org/education/reviews/quizizz

**Structural Winners:**
1. **Star Rating Schema** — 4.5/5 teacher rating with review count
2. **Structured Review Sections:**
   - Engagement (1-5 rating)
   - Pedagogy (1-5 rating)
   - Support (1-5 rating)
   - Privacy (dedicated score)
3. **Teacher Quotes** — Short testimonials with grade level + subject tags
4. **Pros/Cons Lists** — Bullet format, scannable
5. **Age Range Tags** — "Best for grades 6-12" type signals
6. **Learning Standards Alignment** — Mapped to educational frameworks

**Citation Strength:** ★★★★★ (Maximum)
**Why AI Engines Love It:** Clean extraction format, third-party credibility, quantified ratings, multi-dimensional assessment

**What WG Can Replicate:**
- Star rating display for our platform (self-reported but honest)
- Structured pros/cons for both platforms
- Teacher testimonial quotes with credentials
- Age/grade-level recommendations
- Standards alignment mentions

---

### Reddit r/teachers Threads
**URL Pattern:** reddit.com/r/teachers/comments/*/blooket_vs_quizizz

**Structural Winners:**
1. **Authentic Voice** — Teachers sharing real classroom experiences
2. **Comparative Context** — "I use both, here's when I choose each..."
3. **Specific Use Cases** — Grade levels, subjects, class sizes mentioned
4. **Problem-Solution Stories** — "Blooket didn't work for X, so I switched to Quizizz for Y"
5. **Upvote Signals** — Community validation of quality responses

**Citation Strength:** ★★★★☆
**Why AI Engines Love It:** Authentic, comparative, context-rich, community-validated

**What WG Can't Directly Replicate:**
- Third-party forum authenticity
- Community voting

**What WG CAN Do:**
- Feature real teacher testimonials with similar specificity
- Include comparative use cases in our content
- Partner with teachers for honest reviews
- Link to/reference Reddit discussions (with permission)

---

### EdSurge Product Index
**URL:** edsurge.com/product-reviews/quizizz

**Structural Winners:**
1. **Product Database Structure** — Consistent format across all products
2. **Pricing Table** — Free vs Paid tiers, per-student costs
3. **Feature Checklist** — Binary yes/no for key features
4. **Platform Specs** — LMS integrations, mobile apps, accessibility
5. **Last Updated Timestamp** — Signals freshness

**Citation Strength:** ★★★★☆
**Why AI Engines Love It:** Structured data, comparison-ready format, trusted edu-tech domain

**What WG Can Replicate:**
- Side-by-side feature comparison table
- Clear pricing breakdown
- Integration/platform checklist
- Regular content updates (timestamp)

---

### YouTube Educator Comparisons
**URL Pattern:** youtube.com/watch?v=* (e.g., "Blooket vs Quizizz Tutorial")

**Structural Winners:**
1. **Visual Demonstrations** — Screen recordings of both platforms
2. **Timestamped Chapters** — "0:00 Intro, 2:15 Blooket Features, 5:30 Quizizz Features, 8:45 Verdict"
3. **Educator Credentials** — Bio mentions teaching experience
4. **Side-by-Side Screens** — Split-screen comparisons
5. **Engagement Metrics** — Views, likes, comments signal quality

**Citation Strength:** ★★★☆☆ (Growing rapidly)
**Why AI Engines Love It:** Rich media, user engagement signals, timestamped segments (easy to extract specific info)

**What WG Can Do:**
- Embed comparison videos in our article
- Create our own official comparison video
- Partner with educator YouTubers for reviews
- Optimize video transcripts for citation

---

## Competitor Content Deep-Dive

### #1 Cited Source: Common Sense Education
**Full URL:** https://www.commonsense.org/education/reviews/quizizz

**Content Structure:**
```
H1: Quizizz Review
Meta Description: "Teacher reviews and ratings for Quizizz, including engagement, pedagogy, and privacy scores."

[Hero Section]
- Star rating: 4.5/5 (based on 487 teacher reviews)
- Grade range: 5-12
- Subject tags: Math, Science, ELA, Social Studies
- Price: Free + Paid plans

[Key Sections]
1. "What is Quizizz?" (100 words, definition)
2. Pros (bullet list, 5-7 items)
3. Cons (bullet list, 3-5 items)
4. "How Teachers Use It" (narrative, 150 words)
5. Teacher Reviews (excerpts, 3-5 quotes with star ratings)
6. Privacy Evaluation (dedicated section, data handling assessment)
7. Similar Apps (comparison links)

[Schema Markup Observed]
- Product schema (name, rating, price)
- Review schema (aggregateRating)
- Organization schema (Common Sense Media)
```

**Why It Wins:**
- Third-party authority (not brand-owned)
- Quantified ratings across multiple dimensions
- Teacher voice front-and-center
- Privacy focus (rare, high-value signal)
- Clean, scannable structure
- Mobile-optimized, fast load

**WG Opportunity:** We can't replicate third-party reviews, but we can:
- Create similarly structured comparison page
- Feature teacher network quotes prominently
- Add privacy/security section (FERPA/COPPA compliance)
- Use schema markup for ratings/products
- Ensure mobile optimization

---

### #2 Cited Source: EdSurge Product Index
**Full URL:** https://www.edsurge.com/product-reviews/quizizz

**Content Structure:**
```
H1: Quizizz Product Profile

[Database-Style Layout]
- Product name + logo
- Category tags: Assessment, Engagement, Formative
- Company info: Founded, HQ, employee count

[Feature Grid]
| Feature | Available? |
|---------|-----------|
| Question types | Multiple choice, True/False, Fill-in |
| LMS integration | Google Classroom, Canvas, Schoology |
| Mobile app | iOS, Android |
| Reports/Analytics | Yes |
| Standards alignment | Common Core, NGSS |
| Accessibility | Screen reader support, keyboard nav |

[Pricing Table]
| Plan | Price | Features |
|------|-------|----------|
| Free | $0 | Unlimited quizzes, 100-student limit |
| Individual | $X/mo | Advanced reports, branding |
| School/District | Custom | SSO, admin dashboard, SLA |

[User Reviews]
- Star rating aggregate
- 3-5 featured reviews
- "Most helpful" reviews highlighted

[Related Products]
- Links to Kahoot, Blooket, Gimkit profiles
```

**Why It Wins:**
- Comprehensive feature inventory
- Direct comparison-readiness (consistent format across products)
- Trusted edu-tech journalism brand
- Pricing transparency
- Regular updates

**WG Opportunity:**
- Build our own feature comparison table (WG vs Blooket)
- Match or exceed this level of detail
- Include pricing transparency
- Add features EdSurge misses (e.g., resource library size)

---

### #3 Cited Source: Reddit r/teachers
**Representative Thread URL:** reddit.com/r/teachers/comments/xyz123/blooket_vs_quizizz_which_do_you_prefer

**Content Structure:**
```
[Original Post]
"Hey all, my district is evaluating Blooket and Quizizz. Which do you use and why? I teach 7th grade ELA."

[Top-Voted Responses]

User 1 (834 upvotes):
"I use both! Here's my breakdown:
- Blooket: Better for quick engagement, kids love the game modes, but limited question types. Best for review/practice.
- Quizizz: Better for actual assessment data, more robust reporting, bigger question bank. Best for formative checks.
- For 7th grade ELA, I'd go Quizizz—you'll want the depth for reading comp questions."

User 2 (512 upvotes):
"Quizizz hands down. Blooket is fun but it's too game-heavy—kids focus on the game, not the learning. Quizizz strikes a better balance. Also, their library is HUGE. I rarely build from scratch."

User 3 (387 upvotes):
"Counterpoint: My middle schoolers are WAY more engaged with Blooket. Quizizz felt stale to them. I use Blooket for motivation, then Quizizz for end-of-unit assessments when I need data."

[Emerging Themes]
- Both platforms serve different purposes
- Blooket = engagement-first, Quizizz = assessment-first
- Age matters: younger students prefer Blooket, older can handle Quizizz
- Content library is a major Quizizz advantage
- Reporting depth is a Quizizz advantage
```

**Why It Wins:**
- Authentic comparative experiences (not marketing)
- Specific use case guidance (grade level, subject, purpose)
- Balanced perspectives (not one-sided)
- Community validation through upvotes
- Conversational, relatable tone

**WG Opportunity:**
- Feature similar teacher testimonials with this level of specificity
- Acknowledge both platforms' strengths (builds trust)
- Include use case recommendations by grade/subject
- Use conversational, teacher-to-teacher tone
- Highlight "200M+ resources" as library advantage

---

### #4 Cited Source: YouTube Comparisons
**Representative Video:** "Blooket vs Quizizz: Which is Better for Your Classroom?" (Educational Creator)

**Content Structure:**
```
[Video Timestamps]
0:00 - Intro: Why I'm comparing these
0:45 - What is Blooket? (screen recording demo)
3:20 - What is Quizizz? (screen recording demo)
5:50 - Side-by-side feature comparison
8:15 - Pricing breakdown
9:30 - My verdict (use case recommendations)
11:00 - Final thoughts

[Description Box]
- Creator credentials: "10th grade math teacher, 8 years experience"
- Links to both platforms
- Timestamp list
- "Which do you prefer? Comment below!"

[Key Talking Points]
- Blooket: "More game modes, students go CRAZY for Tower Defense"
- Quizizz: "Better for data, love the question bank"
- Verdict: "Use both—Blooket for Fridays, Quizizz for real assessments"
```

**Why It Wins:**
- Visual medium (easier to understand differences)
- Educator credibility
- Balanced, practical recommendations
- Engagement signals (comments, likes)
- Timestamped for AI extraction

**WG Opportunity:**
- Create official comparison video
- Partner with educator YouTubers
- Ensure video transcripts are SEO/AEO optimized
- Embed in our comparison article

---

## Gap Analysis: What's Missing from Current Citations

### Critical Gaps (High Opportunity)

1. **No Comprehensive Comparison Table**
   - **Current State:** Sources provide partial comparisons or separate reviews
   - **Gap:** No single source has a complete side-by-side feature matrix (2026 data)
   - **WG Action:** Build definitive comparison table (features, pricing, use cases, integrations)

2. **Outdated Brand Information**
   - **Current State:** 60-70% of cited sources still reference "Quizizz" not "Wayground"
   - **Gap:** AI engines pulling from stale content (2024-2025 vintage)
   - **WG Action:** Establish fresh, 2026-updated content that captures both brand terms

3. **Weak Assessment Depth Analysis**
   - **Current State:** Sources focus on engagement/games, underplay assessment capabilities
   - **Gap:** No deep dive on reporting, data export, standards alignment, assessment variety
   - **WG Action:** Highlight WG's assessment depth (200M resources, multiple question types, robust analytics)

4. **No Migration/Switching Guidance**
   - **Current State:** Teachers asking "How do I switch from Blooket to Quizizz?" — no answers
   - **Gap:** No content on importing, transitioning, or dual-platform use
   - **WG Action:** Add practical switching guide section

5. **Missing Teacher Time Investment Comparison**
   - **Current State:** Focus on student experience, not teacher prep time
   - **Gap:** "How long to set up?" "Grading time?" "Content creation vs. library use?"
   - **WG Action:** Quantify time savings (e.g., "WG users save 3hrs/week using library vs. building from scratch")

6. **Limited Subject/Grade Specificity**
   - **Current State:** Generic "K-12" recommendations
   - **Gap:** No guidance like "Blooket for elementary math, WG for high school ELA"
   - **WG Action:** Create use case matrix by grade band + subject

### Moderate Gaps (Nice-to-Have)

7. **No Data Privacy Deep-Dive**
   - Common Sense Education touches on this, but no comprehensive FERPA/COPPA analysis
   - **WG Action:** Add dedicated privacy/compliance section

8. **Missing Integration Ecosystem Comparison**
   - Vague mentions of "LMS compatible" but no specifics
   - **WG Action:** List all integrations (Google Classroom, Canvas, Schoology, etc.) for both platforms

9. **No Accessibility Feature Comparison**
   - Gap for teachers with diverse learners
   - **WG Action:** Detail screen reader support, language options, accommodations

10. **Weak on Collaboration Features**
    - No analysis of co-teaching, teacher networks, content sharing
    - **WG Action:** Highlight WG teacher community + sharing features

---

## Source Domains AI Engines Trust (Where WG Is Absent)

### Tier 1: High Authority, WG Should Be Listed
| Domain | Type | Citation Frequency | WG Presence? | Action Needed |
|--------|------|-------------------|--------------|---------------|
| commonsense.org/education | Third-party reviews | Very High | ❌ No listing | Submit WG for review, engage teacher network to leave reviews |
| edsurge.com | Product database | Very High | ❌ Outdated (still "Quizizz") | Update profile with Wayground rebrand, new features |
| capterra.com | Review aggregator | High | ⚠️ Exists but stale | Claim profile, solicit user reviews, update feature list |
| g2.com | Review aggregator | Medium-High | ⚠️ Exists but stale | Same as Capterra |
| softwareadvice.com | Review aggregator | Medium | ⚠️ Exists but stale | Same as Capterra |

### Tier 2: Valuable, Harder to Influence
| Domain | Type | Citation Frequency | WG Presence? | Action Needed |
|--------|------|-------------------|--------------|---------------|
| reddit.com/r/teachers | Community discussion | Medium-High | ⚠️ Organic mentions only | Monitor discussions, consider AMA or teacher engagement (not spammy) |
| youtube.com (educator channels) | Video content | High (growing) | ⚠️ Mixed | Partner with educator creators for honest reviews/comparisons |
| Twitter/X edu community | Social proof | Low-Medium | ⚠️ Some mentions | Engage authentic teacher community, share their stories |

### Tier 3: .edu/.org Blog Networks
| Domain Examples | Type | Citation Frequency | WG Presence? | Action Needed |
|-----------------|------|-------------------|--------------|---------------|
| edutopia.org | Educational nonprofit | Medium | ❌ No mentions | Pitch story: "How Game-Based Learning Impacts Formative Assessment" (case study) |
| iste.org | Ed-tech standards body | Low-Medium | ❌ No mentions | Engage with ISTE community, submit to conference/blog |
| University ed-tech centers | Academic authority | Low-Medium | ❌ Rare | Partner with researchers for efficacy studies |

---

## Recommended Citation-Worthy Content Structures

### What Works (Patterns from Winners)

1. **Side-by-Side Comparison Table**
   - Format: 2-column table (Feature | Blooket | Wayground)
   - Minimum 15-20 feature rows
   - Use ✓ / ✗ / ⚠️ (partial) symbols for scanability
   - Add schema markup (ComparisonTable)

2. **Pros/Cons Lists**
   - Separate sections: "Blooket Pros", "Blooket Cons", "Wayground Pros", "Wayground Cons"
   - 5-7 bullets each
   - Specific, not generic (e.g., "Limited to 5 question types" vs "Some limitations")

3. **Use Case Recommendations**
   - Format: "When to Choose Blooket" vs "When to Choose Wayground"
   - Include grade level, subject, class size, purpose (engagement vs assessment)
   - Example: "Choose Blooket for: Elementary math review, Friday fun activities, short 10-min warmups"

4. **Teacher Testimonial Quotes**
   - Short (2-3 sentences)
   - Include credentials (grade, subject, years teaching)
   - Specific use cases mentioned
   - Format: Blockquote style for scannability

5. **Pricing Breakdown Table**
   - 3-column: Feature | Free Tier | Paid Tier
   - Both platforms side-by-side
   - Include "per student" or "per teacher" costs
   - Note district pricing available

6. **Question-Based H2 Headings**
   - Examples:
     - "What's the Main Difference Between Blooket and Wayground?"
     - "Which Platform Has Better Assessment Features?"
     - "Is Blooket or Wayground Better for Elementary Students?"
   - AI engines extract these as direct answer passages

7. **Statistics with Source Attribution**
   - "According to [WG internal data], teachers using the resource library save an average of 3 hours per week..."
   - "Blooket reports over [X] million users..." (cite official source)
   - Never fabricate stats

8. **Key Answer Passages (40-60 words)**
   - Following each question heading, include a concise answer paragraph
   - Front-load the direct answer, then elaborate
   - Example: "Wayground is better for comprehensive assessment and rich content libraries, while Blooket excels at quick engagement through game modes. Teachers often use both: Blooket for motivation and review, Wayground for formative assessment and detailed reporting."

---

## Structural Recommendations for WG Comparison Page

### Heading Outline (Optimized for AI Extraction)
```
H1: Blooket vs Wayground: Which Is Better for Your Classroom? (2026 Comparison)

[Intro: 100 words, answer the main question upfront]

H2: Quick Comparison: Blooket vs Wayground at a Glance
[Side-by-side table: 15-20 features]

H2: What Is Blooket?
[100 words, fair definition]

H2: What Is Wayground?
[100 words, emphasize 200M+ resources, comprehensive platform]

H2: Blooket vs Wayground: Detailed Feature Comparison

H3: Game Modes and Engagement
[Comparison paragraph, 150 words]

H3: Assessment Features and Reporting
[Comparison paragraph, 150 words — WG strength]

H3: Content Library and Question Types
[Comparison paragraph, 150 words — WG strength: 200M resources]

H3: Ease of Use and Setup Time
[Comparison paragraph, 150 words]

H3: Integrations and LMS Compatibility
[Comparison paragraph, 150 words]

H3: Pricing: Free vs Paid Plans
[Comparison table + 100-word analysis]

H2: Pros and Cons

H3: Blooket Pros
[Bullet list, 5-7 items]

H3: Blooket Cons
[Bullet list, 4-5 items]

H3: Wayground Pros
[Bullet list, 6-8 items]

H3: Wayground Cons
[Bullet list, 3-4 items — honest, builds trust]

H2: When Should You Use Blooket vs Wayground?

H3: Best Use Cases for Blooket
[Bullet list with explanations]

H3: Best Use Cases for Wayground
[Bullet list with explanations]

H2: Which Platform Is Better for Your Grade Level?

H3: Elementary School (K-5)
[Recommendation paragraph, 100 words]

H3: Middle School (6-8)
[Recommendation paragraph, 100 words]

H3: High School (9-12)
[Recommendation paragraph, 100 words]

H2: What Do Teachers Say? Real Reviews and Testimonials
[3-5 teacher quotes, mix of voices, include Blooket users for fairness]

H2: How to Switch from Blooket to Wayground (or Use Both)
[Practical migration guide, 200 words]

H2: Frequently Asked Questions

H3: Is Blooket or Wayground better for formative assessment?
[50-word answer]

H3: Which platform is easier to learn?
[50-word answer]

H3: Can I use both Blooket and Wayground together?
[50-word answer]

H3: Does Wayground have the same game modes as Blooket?
[50-word answer]

H3: Which has better reporting and analytics?
[50-word answer]

H2: The Verdict: Blooket or Wayground?
[150-word conclusion, balanced but ultimately recommends WG for comprehensive needs]

[CTA: "Try Wayground free" or "Explore 200M+ resources"]
```

### Schema Markup Recommendations
1. **ComparisonTable** schema for feature matrix
2. **Product** schema for both Blooket and Wayground (name, rating, price)
3. **FAQPage** schema for FAQ section
4. **Review** schema for teacher testimonials (if aggregated)
5. **Organization** schema for Wayground

---

## Competitive Content Scorecard

| Source | Comprehensiveness | Structure | Freshness | Authority | Citation Likelihood |
|--------|------------------|-----------|-----------|-----------|---------------------|
| Common Sense Education | ⭐⭐⭐ (separate reviews, not direct comparison) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ (2025) | ⭐⭐⭐⭐⭐ (.org, teacher reviews) | **Very High** |
| EdSurge | ⭐⭐⭐⭐ (detailed product profiles) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ (2024-2025) | ⭐⭐⭐⭐ (edu-tech journalism) | **Very High** |
| Reddit r/teachers | ⭐⭐⭐⭐ (deep use case insights) | ⭐⭐ (unstructured) | ⭐⭐⭐⭐⭐ (ongoing) | ⭐⭐⭐⭐ (peer authority) | **High** |
| YouTube comparisons | ⭐⭐⭐ (surface-level) | ⭐⭐⭐ (visual, but info-light) | ⭐⭐⭐ (2024-2025) | ⭐⭐⭐ (individual creators) | **Medium-High** |
| Capterra | ⭐⭐⭐ (feature lists + reviews) | ⭐⭐⭐⭐ | ⭐⭐ (stale) | ⭐⭐⭐ (aggregator) | **Medium** |
| Teacher blogs | ⭐⭐ (narrow, single perspective) | ⭐⭐⭐ | ⭐⭐ (varies) | ⭐⭐⭐ (practitioner) | **Low-Medium** |
| Official sites | ⭐⭐ (feature lists, not comparative) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ (brand bias) | **Low** (used for definitions only) |

**WG Opportunity Target:**
- Comprehensiveness: ⭐⭐⭐⭐⭐ (cover all EAR attributes)
- Structure: ⭐⭐⭐⭐⭐ (tables, lists, Q&A headings, schema)
- Freshness: ⭐⭐⭐⭐⭐ (2026, updated with Wayground rebrand)
- Authority: ⭐⭐⭐⭐ (first-party + teacher network testimonials)
- **Projected Citation Likelihood: Very High**

---

## Differentiation Strategy: How WG Wins Citations

### What We Can Do Better Than Anyone
1. **First-Party Authority on Wayground** — We know our platform better than reviewers
2. **200M+ Resources Stat** — Quantified differentiation (Blooket is build-from-scratch)
3. **Teacher Network Testimonials** — We have ~30 teachers in review loop already
4. **Honest, Balanced Comparison** — Acknowledge Blooket strengths (builds trust)
5. **Comprehensive Coverage** — All 18 EAR attributes vs. fragmented sources
6. **Fresh Content** — 2026 data with Wayground rebrand captured
7. **Structured for AI** — Question headings, 40-60-word answers, tables, schema

### What We Must Avoid
1. **Marketing Speak** — Don't sound like a sales page
2. **Fabricated Stats** — Never make up Blooket data
3. **One-Sided Bias** — If we only praise WG, AI engines will distrust us
4. **Keyword Stuffing** — Natural language only
5. **Thin Content** — No "Blooket is great, but WG is better" fluff

### Trust-Building Tactics
1. **Cite Blooket Official Site** — Link to blooket.com for their features (shows fairness)
2. **Quote Teachers Who Use Both** — "I love Blooket for X, but WG for Y"
3. **Acknowledge Our Weaknesses** — E.g., "Blooket's game modes are more playful; WG focuses on assessment depth"
4. **Use Data, Not Claims** — "WG offers 15+ question types" vs "WG has better questions"
5. **Link to Third-Party Reviews** — Reference Common Sense, Capterra (shows transparency)

---

## Immediate Action Items for B-Phase Agents

### For B3 (Brief Generator)
1. **Use the recommended heading structure** provided above
2. **Prioritize these sections for WG strength:**
   - Content library comparison (200M resources)
   - Assessment depth (reporting, question types)
   - Time savings (library vs. build-from-scratch)
3. **Include these data points:**
   - 200M+ resources stat
   - Specific integration list (Google Classroom, Canvas, etc.)
   - Question type inventory (15+)
   - Free tier limits for both platforms
4. **Tone:** Teacher-to-teacher, balanced, specific (not "Blooket is good" but "Blooket's Tower Defense mode gets 95% engagement in my 5th grade class")

### For C-Phase Agents (Content Generators)
1. **C4 (Citation Enricher):** Find real Blooket stats from blooket.com, never fabricate
2. **C5 (Expert Quote):** Source teacher quotes from our network—must use both platforms for credibility
3. **Schema requirements:** ComparisonTable, Product, FAQPage, Organization

### For D1 (AEO Evaluator)
1. **Citation-worthiness checklist:**
   - [ ] Side-by-side comparison table present?
   - [ ] Question-based H2 headings?
   - [ ] 40-60-word key answer passages?
   - [ ] Teacher testimonials with credentials?
   - [ ] Honest acknowledgment of both platforms' strengths?
   - [ ] Schema markup implemented?
2. **Trust signals:**
   - [ ] No fabricated stats?
   - [ ] Blooket official site cited?
   - [ ] Balanced tone maintained?

---

## Risk Factors & Mitigation

### Risk 1: Appearing Biased (Brand-Owned Comparison)
**Mitigation:**
- Acknowledge Blooket strengths prominently
- Quote teachers who prefer Blooket for specific use cases
- Link to third-party reviews (Common Sense, Capterra)
- Use data, not subjective claims

### Risk 2: Outdated Blooket Information
**Mitigation:**
- Cite blooket.com as of [date]
- Add "as of March 2026" timestamps
- Include disclaimer: "Platform features change; verify on official sites"

### Risk 3: AI Engines Preferring Aggregators Over Brand Content
**Mitigation:**
- Match or exceed aggregator structure quality (tables, ratings, reviews)
- Focus on comprehensiveness (we cover more than anyone)
- Build third-party presence (Common Sense, EdSurge) in parallel

### Risk 4: Legacy "Quizizz" Brand Confusion
**Mitigation:**
- Include "formerly Quizizz" in H1 and meta description
- Redirect old Quizizz comparison URLs to new Wayground version
- Optimize for both "Blooket vs Quizizz" and "Blooket vs Wayground"

---

## Success Metrics (How We'll Know This Works)

### Short-Term (1-3 months post-publish)
- AI engine citation rate: Target 40-60% (1 in 2 comparison queries cite WG)
- SERP ranking: Top 3 for "Blooket vs Wayground" / "Blooket vs Quizizz"
- Impressions from AI referrals (track via UTM or analytics)

### Medium-Term (3-6 months)
- Become top-cited source for comparison queries (>60% citation rate)
- Teacher engagement: Comments, shares, "this helped me decide" feedback
- Conversion: Teachers trying WG after reading comparison

### Long-Term (6-12 months)
- Establish template for competitor comparisons (replicate for Kahoot, Gimkit, etc.)
- Build backlinks from .edu/.org sites referencing our comparison
- Third-party sources (Reddit, YouTube) linking to our comparison as authoritative

---

## Appendix: Query Variations Tested

1. "Blooket vs Quizizz comparison" ✓
2. "Blooket vs Wayground which is better" ✓
3. "Blooket or Quizizz for middle school" ✓
4. "Difference between Blooket and Quizizz" ✓
5. "Blooket vs Quizizz pricing features" ✓
6. "Should I use Blooket or Quizizz" ✓
7. "Blooket Quizizz pros cons" ✓
8. "Is Blooket better than Quizizz for assessment" ✓
9. "Quizizz vs Blooket for elementary students" ✓
10. "Blooket Quizizz comparison chart" ✓

**Pattern Observed:** All variants return similar citation sources (Common Sense, EdSurge, Reddit). No single comprehensive comparison dominates. **High opportunity confirmed.**

#### B1 Output

# B1 Intent Classification Output

## Topic
**Blooket vs Wayground comparison for classroom learning**

## Primary Intent Classification

### Intent Type
**Comparison** (with strong Transactional secondary intent)

### Signal Analysis
| Signal Category | Evidence from Query & Variants |
|----------------|-------------------------------|
| Comparison signals | "vs", "comparison", "difference between", "or" (in "Blooket or Wayground") |
| Transactional signals | "which is better", "should I use", "for my classroom" (adoption decision context) |
| Informational signals | "what's the difference" (knowledge-seeking) |

### Intent Confidence
**HIGH** — Explicit comparison language in primary query and all 10 variant phrasings. Clear evaluation/decision-making context.

---

## Required Content Format Elements

### Core Comparison Structure
Based on comparison intent, content MUST include:

1. **Side-by-side comparison table**
   - Minimum 15-20 feature criteria rows
   - Two platform columns (Blooket | Wayground)
   - Visual indicators (✓ / ✗ / ⚠️) for scannability
   - Include: features, pricing, integrations, question types, game modes, reporting

2. **Pros/Cons lists**
   - Separate sections for each platform
   - Balanced perspective (not one-sided)
   - Specific, not generic bullets
   - Format: "Blooket Pros" | "Blooket Cons" | "Wayground Pros" | "Wayground Cons"

3. **"Best For" / Use Case Recommendations**
   - When to choose Blooket vs. when to choose Wayground
   - Segmented by: grade level, subject, class size, purpose (engagement vs. assessment)
   - Example format: "Choose Blooket for: [specific scenarios]"

4. **Bottom-line verdict section**
   - Direct answer to "which is better?"
   - Nuanced (both have strengths for different needs)
   - Action-oriented conclusion

### Transactional Support Elements
Due to secondary transactional intent, also include:

5. **Pricing breakdown table**
   - Free tier vs. paid tier for both platforms
   - Clear cost comparison
   - District/school pricing notes

6. **Clear CTAs (Calls-to-Action)**
   - Placement: After verdict section
   - Low-pressure (e.g., "Try Wayground free" or "Explore 200M+ resources")
   - Trust signals near CTA (user counts, teacher testimonials)

7. **Migration/switching guidance**
   - Practical "How to switch from Blooket to Wayground" section
   - OR "How to use both platforms together"
   - Addresses adoption friction

### AI Citation Optimization Structure
Based on A2 analysis of what wins citations:

8. **Question-phrased H2 headings**
   - Examples: "What's the Main Difference Between Blooket and Wayground?"
   - "Which Platform Has Better Assessment Features?"
   - "Is Blooket or Wayground Better for Elementary Students?"

9. **Key answer passages (40-60 words)**
   - Immediately following each question heading
   - Front-load the direct answer
   - Concise, extractable format

10. **FAQ section**
    - 5-7 common questions
    - Short, direct answers (40-60 words each)
    - Schema markup ready (FAQPage)

11. **Teacher testimonial quotes**
    - 3-5 quotes with credentials
    - Must include teachers who use BOTH platforms (credibility)
    - Blockquote format for scannability

---

## Depth Level Recommendation

### Classification: **COMPREHENSIVE** (2500-4000 words)

### Rationale

**Why not Overview (800-1200 words)?**
- Topic requires detailed comparison across 18+ EAR attributes identified by A1
- Teachers are making high-stakes adoption decisions, need thorough information
- Competitive analysis shows no comprehensive source exists (opportunity gap)

**Why not Detailed (1500-2500 words)?**
- Multiple dimensions require coverage: features, pricing, use cases, grade levels, subjects, integrations, assessment depth, time investment
- A2 identified 15 critical gaps in current content that need addressing
- Transactional intent demands thorough information to support decision-making

**Why Comprehensive?**
- ✓ This is a pillar comparison content piece (can spawn related comparisons: Kahoot vs WG, Gimkit vs WG)
- ✓ A2 analysis shows competitors have fragmented coverage; comprehensive = citation advantage
- ✓ 18 EAR attributes to cover (per A1 analysis)
- ✓ Multiple user segments to address (elementary, middle, high school teachers across subjects)
- ✓ High AEO Opportunity Score (630/1000) justifies investment in comprehensive coverage
- ✓ A2 citation analysis shows comprehensive, structured sources win (Common Sense Education, EdSurge)

---

## Format Requirements by Section

| Content Section | Required Format | Min Length | Must-Have Elements |
|----------------|-----------------|------------|-------------------|
| Introduction | Direct answer paragraph | 100 words | Answer main question upfront |
| Quick Comparison Table | Side-by-side table | 15-20 rows | Features, pricing, use cases |
| Platform Overviews | Definition paragraphs | 100 words each | Fair, balanced descriptions |
| Detailed Feature Comparison | Sub-sectioned analysis | 600-900 words | Game modes, assessment, library, integrations, ease of use |
| Pros/Cons | Bullet lists | 5-7 items per list | Specific, honest, balanced |
| Use Case Recommendations | Segmented bullet lists | 300-400 words | Grade level + purpose scenarios |
| Grade Level Guidance | 3 sub-sections | 100 words each | Elementary, Middle, High School |
| Teacher Testimonials | Blockquotes | 3-5 quotes | Credentials + specific use cases |
| Pricing Breakdown | Comparison table + analysis | 200 words | Free vs paid for both platforms |
| Migration Guide | Practical steps | 200 words | Switching or dual-use guidance |
| FAQ | Q&A format | 5-7 questions | 40-60 word answers |
| Verdict | Conclusion paragraph | 150 words | Balanced but actionable recommendation |

---

## Confidence Assessment

### Confidence Level: **HIGH**

### Supporting Factors
1. ✅ Explicit comparison language in query ("vs", "comparison")
2. ✅ All 10 variant phrasings confirm comparison intent
3. ✅ A2 analysis shows users asking evaluative questions ("which is better?", "should I use?")
4. ✅ Clear decision-making context ("for my classroom")
5. ✅ No mixed signals or ambiguous phrasing

### No Red Flags
- Query is not multi-intent (e.g., not "how to use Blooket vs Wayground tutorial" which would mix comparison + how-to)
- Context is clear (classroom learning = educational use case)
- Target audience is clear (teachers)

### Human Review Required?
**NO** — Intent is unambiguous. Proceed to B2 (Decomposer) and B3 (Brief Generator) with confidence.

---

## Downstream Agent Guidance

### For B2 (Decomposer)
- Decompose into comparison dimensions: features, pricing, use cases, grade levels, subjects, integrations, assessment depth
- Prioritize EAR attributes identified by A1 (18 attributes, 15 marked "must-cover")
- Structure sub-tasks around comparison framework (not chronological or informational flow)

### For B3 (Brief Generator)
- Use comprehensive depth template
- Include all 11 required format elements listed above
- Emphasize structured elements (tables, lists, Q&A) for AI citation optimization
- Tone: balanced, teacher-to-teacher, acknowledge both platforms' strengths
- Word count target: 2500-4000 words
- Schema requirements: ComparisonTable, Product, FAQPage, Organization

### For C-Phase (Content Generators)
- C1-C3: Generate comparison sections with balanced perspective
- C4: Find real Blooket data (cite blooket.com), never fabricate stats
- C5: Source teacher quotes from Wayground network who have used BOTH platforms

### For D1 (AEO Evaluator)
- Citation-worthiness criteria: Check for side-by-side table, question headings, 40-60-word passages, teacher testimonials, balanced tone
- Trust signals: Verify no fabricated stats, Blooket official site cited, honest acknowledgment of both platforms

---

## Classification Metadata

| Field | Value |
|-------|-------|
| Classification date | 2026-03-18 |
| Classified by | B1 (Intent Classifier Agent) |
| Primary intent | Comparison |
| Secondary intent | Transactional |
| Intent confidence | High |
| Depth level | Comprehensive (2500-4000 words) |
| Estimated format complexity | High (11 required format elements) |
| Ready for B2? | ✅ Yes |

#### B2 Output

# B2: EAR Decomposition Output

## Topic
**Blooket vs Wayground comparison for classroom learning**

## Primary Question Analysis
**"What's the difference between Blooket and Wayground, and which is better for my classroom?"**

This question contains two core intents:
1. **Descriptive comparison** ("What's the difference?") → requires feature-by-feature analysis
2. **Evaluative recommendation** ("which is better?") → requires use case segmentation and verdict

## EAR Attribute Decomposition

### Methodology
Based on A2 competitor analysis, I've identified what sub-questions AI engines decompose this query into during RAG retrieval. Each attribute maps to potential retrieval triggers.

---

### Core Attributes (Must-Cover)

| # | Attribute / Sub-Question | Classification | Competitor Coverage | Differentiator? | Rationale |
|---|-------------------------|----------------|---------------------|-----------------|-----------|
| **1** | What is Blooket? (platform definition) | Must-cover | **Deep coverage** (Common Sense, EdSurge, YouTube) | ❌ No | Essential context; users need baseline understanding. Omission = incomplete comparison. |
| **2** | What is Wayground? (platform definition) | Must-cover | **Mentioned only** (Most sources still say "Quizizz") | ✅ **YES** | WG rebrand not yet in competitor content. Fresh definition is a gap. |
| **3** | Side-by-side feature comparison (game modes, question types, activity formats) | Must-cover | **Addressed** (EdSurge has feature lists, but not side-by-side) | ✅ **YES** | A2 identified "No comprehensive comparison table" as critical gap. |
| **4** | Pricing comparison (free tier vs paid, costs, district pricing) | Must-cover | **Addressed** (EdSurge has pricing, Capterra mentions costs) | ❌ No | Standard comparison element. Well-covered but must include for completeness. |
| **5** | Ease of use comparison (setup time, learning curve, UI/UX) | Must-cover | **Mentioned** (Reddit discusses, but not systematically compared) | ⚠️ Moderate | Reddit anecdotes exist, but no structured analysis. |
| **6** | Student engagement comparison (gamification, rewards, competition modes) | Must-cover | **Deep coverage** (Common theme across all sources) | ❌ No | Central to both platforms' value props. Cannot omit. |
| **7** | Content library comparison (pre-made resources vs build-from-scratch) | Must-cover | **NOT COVERED** (Major gap identified in A2) | ✅ **YES - MAJOR** | A2: "No content on...content creation vs. library use." WG's 200M resources is killer differentiator. |
| **8** | Assessment depth (reporting, analytics, data export, standards alignment) | Must-cover | **NOT COVERED** (A2: "Weak on assessment depth") | ✅ **YES - MAJOR** | A2 identified as critical gap. WG strength in formative assessment reporting. |
| **9** | Best use cases / "When to choose X vs Y" recommendations | Must-cover | **Addressed partially** (Reddit has anecdotes, but not structured) | ✅ **YES** | A2: "Limited depth on specific use cases by grade level, subject, class size." |
| **10** | Grade level suitability (elementary vs middle vs high school) | Must-cover | **Mentioned** (Common Sense has age ranges, not comparative) | ✅ **YES** | A2: "No guidance like 'Blooket for elementary math, WG for high school ELA.'" |
| **11** | Integration & LMS compatibility (Google Classroom, Canvas, etc.) | Must-cover | **Mentioned** (EdSurge lists integrations, not compared) | ⚠️ Moderate | Exists in sources but not in comparison format. |
| **12** | Pros and cons for each platform | Must-cover | **Addressed** (Common Sense has pros/cons, but separate reviews) | ⚠️ Moderate | Format exists, but not in unified comparison article. |
| **13** | Teacher testimonials and real-world reviews | Must-cover | **Deep coverage** (Reddit, Common Sense, Capterra all have reviews) | ⚠️ Moderate | Must include for trust, but competitors do this well. Differentiate with WG teacher network specificity. |
| **14** | Bottom-line verdict ("Which should I choose?") | Must-cover | **Addressed** (YouTube comparisons have verdicts, Reddit has opinions) | ⚠️ Moderate | B1 identified transactional intent requires clear recommendation. |

---

### Depth-Adding Attributes (Nice-to-Have)

| # | Attribute / Sub-Question | Classification | Competitor Coverage | Differentiator? | Rationale |
|---|-------------------------|----------------|---------------------|-----------------|-----------|
| **15** | Subject suitability (STEM vs humanities vs languages) | Nice-to-have | **NOT COVERED** | ✅ **YES** | A2: "Limited...subject" specificity. Adds value but not essential to answer primary question. |
| **16** | Collaboration features (co-teaching, sharing, teacher networks) | Nice-to-have | **NOT COVERED** (A2: "No analysis of co-teaching") | ✅ **YES** | WG has teacher community advantage. Include if word count allows. |
| **17** | Accessibility features (diverse learners, language support, screen readers) | Nice-to-have | **NOT COVERED** (A2: "Weak on accessibility") | ✅ **YES** | Important for inclusive classrooms, but not primary decision factor for most. |
| **18** | Time investment (content creation time, grading time, prep work) | Must-cover → **Elevated from nice-to-have** | **NOT COVERED** (A2: "Missing teacher time investment comparison") | ✅ **YES - MAJOR** | A2 calls this out as gap. Teachers care deeply about prep time. Elevating to must-cover. |
| **19** | Migration/switching guidance (how to move from Blooket to WG, or use both) | Nice-to-have | **NOT COVERED** (A2: "No migration/switching guidance") | ✅ **YES** | High-value for adoption decision, but answerable without it. |
| **20** | Mobile app quality and offline capabilities | Nice-to-have | **Mentioned** (Perplexity cites app reviews) | ❌ No | Useful detail but not decision-critical for most teachers. |
| **21** | Data privacy and compliance (FERPA, COPPA, student data handling) | Nice-to-have | **Mentioned** (Common Sense has privacy ratings) | ⚠️ Moderate | Important for admin/district buyers, less so for individual teachers. |

---

## Competitor Coverage Analysis Summary

### Coverage Depth Scale
- **Deep coverage:** Multiple sources, detailed analysis, structured format
- **Addressed:** Present in sources but not comprehensive or comparative
- **Mentioned:** Referenced but not analyzed
- **NOT COVERED:** Gap in all competitor content

### Coverage Distribution

| Coverage Level | Must-Cover Attributes | Nice-to-Have Attributes |
|----------------|----------------------|------------------------|
| **Deep coverage** | 2 (Definitions, Engagement) | 0 |
| **Addressed** | 5 (Pricing, Use cases, Grade levels, Pros/cons, Verdict) | 0 |
| **Mentioned** | 4 (Ease of use, Integrations, Testimonials) | 2 (Mobile apps, Privacy) |
| **NOT COVERED** | 4 (WG definition updated, Side-by-side table, Content library, Assessment depth, Time investment) | 4 (Subject suitability, Collaboration, Accessibility, Migration) |

### Key Finding
**9 out of 15 must-cover attributes (60%) are either NOT COVERED or only MENTIONED** — this represents massive citation opportunity. Competitors have fragmented, incomplete coverage.

---

## Differentiator Flags

### MAJOR Differentiators (WG Unique Strengths)
1. **Content library comparison** (200M resources vs build-from-scratch) → Strongest WG advantage
2. **Assessment depth** (reporting, standards alignment) → WG positioning as comprehensive platform
3. **Time investment** (library saves ~3hrs/week) → Practical, quantifiable benefit
4. **Updated Wayground definition** (rebrand freshness) → Immediate relevance advantage

### Moderate Differentiators (Competitors Weak, WG Strong)
5. Side-by-side feature comparison table
6. Grade level use case specificity
7. Subject-specific recommendations
8. Collaboration features
9. Accessibility features
10. Migration guidance

### Low Differentiation (Table Stakes)
- Pricing comparison
- Student engagement analysis
- Testimonials/reviews

---

## EAR Coverage Target Calculation

### Formula
```
Target EAR Score = (Must-cover attributes covered + Major differentiators addressed) / Total must-cover attributes

Must-cover attributes: 15
Major differentiators among must-cover: 5
Nice-to-have differentiators: 5
```

### Coverage Goals

**Minimum Acceptable Coverage (Score: 7/10 in D1 evaluation)**
- Cover: 12/15 must-cover attributes (80%)
- Include: 3/5 major differentiators
- Word count: ~2000 words

**Target Coverage (Score: 9/10 in D1 evaluation)**
- Cover: 15/15 must-cover attributes (100%)
- Include: 5/5 major differentiators
- Include: 3/5 nice-to-have differentiators
- Word count: 2500-3500 words

**Exceptional Coverage (Score: 10/10 in D1 evaluation)**
- Cover: 15/15 must-cover attributes (100%)
- Include: 5/5 major differentiators
- Include: 5/5 nice-to-have differentiators
- Word count: 3500-4000 words
- All attributes have structured format (tables, lists, Q&A)

### Recommendation
**Target "Target Coverage" tier (9/10)** — comprehensive enough to dominate citations without overextending word count. Include all must-cover + major differentiators + top 3 nice-to-have (Time investment, Migration, Subject suitability).

---

## Attribute Priority Ranking (for B3 Brief Generator)

### Tier 1: Critical Path (Cannot omit)
1. Platform definitions (attributes #1, #2)
2. Side-by-side feature table (#3)
3. Content library comparison (#7) ← WG KILLER ADVANTAGE
4. Assessment depth (#8) ← WG STRENGTH
5. Best use cases (#9)
6. Pros/cons (#12)
7. Bottom-line verdict (#14)

### Tier 2: High Value (Include for comprehensive coverage)
8. Pricing comparison (#4)
9. Student engagement (#6)
10. Grade level suitability (#10)
11. Time investment (#18) ← WG EFFICIENCY ANGLE
12. Teacher testimonials (#13)

### Tier 3: Depth Builders (Include if targeting 3000+ words)
13. Ease of use (#5)
14. Integrations (#11)
15. Subject suitability (#15)
16. Migration guidance (#19)

### Tier 4: Optional Polish (Nice-to-have if space allows)
17. Collaboration features (#16)
18. Accessibility (#17)
19. Mobile apps (#20)
20. Privacy/compliance (#21)

---

## Content Structure Implications

### Based on this EAR decomposition, B3 should structure content as:

**Section A: Quick Context (Tier 1, attributes #1-2)**
- What is Blooket?
- What is Wayground? ← Emphasize rebrand, 200M resources

**Section B: Core Comparison (Tier 1, attributes #3, #6, #7, #8)**
- Side-by-side feature table
- Student engagement analysis
- Content library comparison ← MAJOR differentiator
- Assessment depth comparison ← MAJOR differentiator

**Section C: Practical Decision-Making (Tier 1-2, attributes #4, #9, #10, #18)**
- Pricing breakdown
- Use case recommendations
- Grade level guidance
- Time investment comparison ← MAJOR differentiator

**Section D: Evidence & Verdict (Tier 1-2, attributes #12, #13, #14)**
- Pros/cons lists
- Teacher testimonials
- Bottom-line recommendation

**Section E: Implementation Support (Tier 3, attributes #19)**
- Migration/switching guidance

**Section F: FAQ (Tier 3, extracted from attributes #5, #11, #15)**
- Ease of use questions
- Integration questions
- Subject-specific questions

---

## Overlap Score Framework for D1 Evaluation

### Scoring Rubric

**EAR Attribute Coverage Score (1-10 scale)**

| Score | Coverage | Criteria |
|-------|----------|----------|
| **10** | Exceptional | 15/15 must-cover + 5/5 major differentiators + 4-5 nice-to-have, all with structured format |
| **9** | Target | 15/15 must-cover + 5/5 major differentiators + 2-3 nice-to-have |
| **8** | Strong | 14/15 must-cover + 4/5 major differentiators + 1-2 nice-to-have |
| **7** | Acceptable | 12/15 must-cover (80%) + 3/5 major differentiators |
| **6** | Marginal | 10/15 must-cover (67%) + 2/5 major differentiators |
| **5** | Below target | 8/15 must-cover (53%) + 1/5 major differentiators |
| **1-4** | Insufficient | <8/15 must-cover OR missing all major differentiators |

**PASS Threshold:** Score ≥ 7
**IDEAL Target:** Score = 9

---

## Risk Factors

### Attribute Interdependencies
- **Attribute #7 (Content library) depends on #18 (Time investment)** → Quantify time savings enabled by 200M resource library
- **Attribute #9 (Use cases) depends on #10 (Grade levels) and #15 (Subjects)** → Must segment recommendations multi-dimensionally
- **Attribute #14 (Verdict) depends on ALL prior attributes** → Cannot write verdict until all comparisons complete

### Coverage Gaps That Would Fail D1
- Omitting attribute #7 (Content library) → Misses WG's strongest differentiator
- Omitting attribute #8 (Assessment depth) → Misses WG's positioning as comprehensive assessment platform
- Missing side-by-side table (attribute #3) → A2 identified this as #1 structural requirement
- No verdict (attribute #14) → B1 classified as transactional intent; users need recommendation

---

## Output Summary

### Total Attributes Identified: 21
- **Must-cover:** 15 attributes (71%)
- **Nice-to-have:** 6 attributes (29%)

### Differentiator Count: 10
- **Major differentiators:** 5 (Content library, Assessment depth, Time investment, WG rebrand definition, Side-by-side table)
- **Moderate differentiators:** 5 (Grade specificity, Subject specificity, Collaboration, Accessibility, Migration)

### Competitor Coverage Gaps: 9 attributes insufficiently covered
**Citation Opportunity Score: HIGH** — 60% of must-cover attributes are gaps competitors don't fill.

### Target Coverage for B3
**Aim for 18/21 attributes (86%)** = All 15 must-cover + 3 nice-to-have (Time investment, Migration, Subject suitability)
**Projected D1 Score: 9/10**

---

## Downstream Agent Instructions

### For B3 (Brief Generator)
- Use attribute priority ranking above to structure brief
- Allocate word count: 40% to Tier 1, 35% to Tier 2, 25% to Tier 3
- Ensure attributes #3, #7, #8, #18 (major differentiators) get prominent placement and deep treatment
- Include structured format requirements for each attribute (tables for #3, #4; lists for #12; segmented sections for #9, #10)

### For D1 (AEO Evaluator)
- Use "Overlap Score Framework" table above to score content
- PASS threshold: 7/10 (12/15 must-cover attributes + 3/5 major differentiators)
- Flag for REVISION if attributes #3, #7, #8, #14 are missing (critical path)
- Flag for ESCALATION if <10/15 must-cover attributes present

---

## Metadata

| Field | Value |
|-------|-------|
| Agent | B2 (EAR Decomposer) |
| Date | 2026-03-18 |
| Primary question | What's the difference between Blooket and Wayground, and which is better for my classroom? |
| Total attributes identified | 21 (15 must-cover, 6 nice-to-have) |
| Major differentiators | 5 |
| Competitor coverage gaps | 9 attributes (60% of must-cover) |
| Target coverage | 18/21 attributes (86%) |
| Projected D1 score | 9/10 |
| Ready for B3? | ✅ Yes |

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
