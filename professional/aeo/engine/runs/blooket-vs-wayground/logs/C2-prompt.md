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

# C2: Outline Agent

## Identity
- **Phase:** C — Content Generation
- **Stage:** Stage 3a
- **Purpose:** Structure the article skeleton based on the brief and research.

## Inputs
- Content brief from B3
- Research packet from C1

## Process

### Step 1: EAR → Section Mapping
Map each EAR attribute to a specific article section:
- Must-cover attributes get dedicated sections or prominent placement
- Nice-to-have attributes go in expansion or FAQ
- Differentiator attributes get highlighted placement

### Step 2: Heading Structure
Build heading hierarchy:
- H1: Primary question (from brief's QAPE skeleton)
- H2s: Phrased as questions matching query patterns
- H3s: Sub-topics within each H2

### Step 3: Content Block Placement
Per section, assign content block types:
- **Definition Block:** For "What is X?" sections
- **Step-by-Step Block:** For "How to" sections
- **Comparison Table Block:** For comparison sections
- **Statistic Citation Block:** Where data supports claims
- **Expert Quote Block:** Where authority is needed
- **Evidence Sandwich Block:** For key arguments (Claim → Data → Conclusion)

### Step 4: Stats/Quotes Placement
From the research packet, assign specific stats and quotes to sections where they have maximum impact.

### Step 5: FAQ Section Planning
From EAR attributes not fully covered in main body:
- Generate 5-8 FAQ question-answer pairs
- Each answer: 40-60 words (self-contained, extractable)

## Output
**Article Outline** containing:
- Full heading hierarchy (H1 > H2 > H3)
- Section-by-section instructions (content block type, word target, EAR attributes covered)
- Stats/quotes assigned to specific sections
- FAQ section items
- Internal link placement notes

## Constraints
- Every must-cover EAR attribute must appear in the outline
- H2s should be phrased as questions
- No section should be planned for >400 words (extractability)
- Outline must match the intent-specific format requirements from the brief

## Dependencies
- **Upstream:** B3 (brief), C1 (research)
- **Downstream:** C3 (uses outline to write draft)

## Skills Repo Reference
- `ai-seo/references/content-patterns.md` — content block templates
- `programmatic-seo` — template design principles

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |

---
## Task Payload

**Topic:** Blooket vs Wayground comparison for classroom learning

### Upstream Agent Outputs

#### B3 Output
# Content Brief: Blooket vs Wayground for Classroom Learning

> Stage 2 output — produced by B3 (Content Brief Generator)
> Source dossier: topic-dossier-blooket-vs-wayground.md

## Metadata
| Field | Value |
|-------|-------|
| Topic | Blooket vs Wayground comparison for classroom engagement and assessment |
| Target URL | `/learn/edtech-tools/blooket-vs-wayground` |
| Intent type | Comparison + Transactional |
| Target word count | 2,500-3,500 |
| Schema type | ComparisonTable + Product + FAQPage + Article |
| Author | Education Content Lead |
| Date created | 2026-03-18 |
| Status | Draft |

## QAPE Skeleton

### Question
**What's the difference between Blooket and Wayground, and which is better for my classroom?**

### Target Direct Answer (40-60 words)
> Blooket focuses primarily on game-based review with themed game modes like Tower Defense and Gold Quest, while Wayground (formerly Quizizz) offers a comprehensive learning platform with quizzes, lessons, worksheets, flashcards, and 200M+ ready-made resources. Blooket excels at short engagement bursts; Wayground is better suited for full instructional workflows combining assessment, content delivery, and detailed reporting across multiple formats.

### Required Proof Types
- [x] Statistics with sources (min: 5)
- [x] Expert quotes with attribution (min: 3)
- [x] First-person data ("based on 200M+ resources", platform usage patterns)
- [x] Case study / example
- [x] Research citation (engagement/assessment effectiveness)

### Expansion Structure
| Section (H2) | Content Block Type | EAR Attributes Covered | Notes |
|---------------|-------------------|----------------------|-------|
| [Intro paragraph] | Direct Answer Block | Primary question | 100 words, front-load answer |
| How do Blooket and Wayground compare at a glance? | Comparison Table Block | #3 (features), #4 (pricing), #6 (engagement) | 15-20 row side-by-side table — CRITICAL |
| What is Blooket? | Definition Block | #1 (Blooket definition) | 100 words, fair/balanced overview |
| What is Wayground? | Definition Block | #2 (Wayground definition) | 100 words, emphasize 200M+ resources, rebrand context |
| How do Blooket and Wayground compare on key features? | Multi-subsection Comparison | #5, #6, #7, #8, #11 | 800-1000 words across 5 subsections |
| → Student Engagement | Evidence Sandwich Block | #6 (engagement) | Game modes vs multi-format engagement |
| → Content Library and Resources | Evidence Sandwich Block | #7 (content library) | **MAJOR DIFFERENTIATOR** — 200M resources vs build-from-scratch |
| → Assessment and Reporting | Evidence Sandwich Block | #8 (assessment depth) | **MAJOR DIFFERENTIATOR** — WG reporting strength |
| → Ease of Use and Setup | Evidence Sandwich Block | #5 (ease of use) | Setup time, learning curve |
| → Integrations and LMS Compatibility | Evidence Sandwich Block | #11 (integrations) | Google Classroom, Canvas, etc. |
| What does pricing look like for each platform? | Comparison Table Block | #4 (pricing) | Free vs paid tiers, both platforms |
| How much time do teachers spend on each platform? | Evidence Sandwich Block | #18 (time investment) | **MAJOR DIFFERENTIATOR** — library time savings |
| When should you use Blooket vs Wayground? | Recommendation Block | #9 (use cases) | "Best for" scenarios, specific contexts |
| Which platform is better for different grade levels? | Segmented Recommendation Block | #10 (grade suitability) | Elementary, Middle, High School subsections |
| Which platform works better for different subjects? | Segmented Recommendation Block | #15 (subject suitability) | STEM, ELA, Social Studies, Languages |
| What are the pros and cons of each platform? | Pros/Cons Lists | #12 (pros/cons) | 4 separate lists: Blooket Pros, Blooket Cons, WG Pros, WG Cons |
| What do teachers say about Blooket and Wayground? | Expert Quote Block | #13 (testimonials) | 3-5 teacher quotes, must include users of BOTH platforms |
| How do you switch from Blooket to Wayground (or use both)? | How-To Block | #19 (migration) | Practical switching/dual-use guidance |
| Frequently Asked Questions | FAQ items | #17, #20, #21 + overflow | 6-7 questions covering accessibility, mobile apps, privacy, other gaps |
| The Verdict: Which platform should you choose? | Recommendation Block | #14 (verdict) | 150-200 words, balanced but actionable, acknowledge both strengths |

**Total EAR Coverage:** 18 out of 21 attributes (86%) — All 15 must-cover + 3 nice-to-have
**Projected D1 Score:** 9/10

## Content Requirements

### Statistics & Data (minimum targets)
| # | Stat needed | Preferred source type | Notes |
|---|-------------|----------------------|-------|
| 1 | Blooket user count or games played | Blooket official site (blooket.com) | Cite with "According to Blooket, ..." |
| 2 | Wayground resource count (200M+) and user base | Platform data (first-party) | Lead with this in WG definition section |
| 3 | Engagement metrics comparison | Platform data or research | Completion rates, time-on-task, student satisfaction |
| 4 | Teacher time savings: library vs build-from-scratch | Platform usage data or survey | "WG users save average X hours/week using library" |
| 5 | Assessment/reporting usage stats | Platform data | "Teachers export data to X formats", "Standards alignment coverage" |
| 6 | Question type inventory counts | Both platforms | "Blooket offers X question types; Wayground offers 15+" |

### Expert Quotes (minimum targets)
| # | Quote topic | Source type | Critical requirement |
|---|-------------|------------|---------------------|
| 1 | Teacher who uses BOTH platforms — when to choose each | K-12 practitioner | **MUST use both platforms** for credibility |
| 2 | Teacher praising Blooket's game modes / engagement | Elementary or Middle School teacher | Show fairness — acknowledge Blooket strength |
| 3 | Teacher praising Wayground's assessment depth or library | Middle or High School teacher | Emphasize WG comprehensive platform advantage |
| 4 (optional) | Teacher on time savings from using resource library | Any grade level | Supports time investment differentiator |

### Source Citations (minimum targets)
- **Min 5 external source citations** with "According to [Source]" framing:
  - Blooket official site (for features, user counts)
  - Research on game-based learning effectiveness
  - Research on formative assessment impact
  - Common Sense Education or similar (if citing reviews)
  - EdSurge or Capterra (if citing comparative data)
- **Min 3 internal WG data references:**
  - 200M+ resources stat
  - Platform usage patterns (e.g., "teachers use 3+ resource types per week")
  - Engagement or completion data from WG users

## Internal Linking Plan

### Concept <-> Tool <-> Material Triangle
| Link Type | Target Page | Anchor Text | Placement |
|-----------|------------|-------------|-----------|
| Parent hub | `/learn/edtech-tools/` | classroom technology tools OR edtech platforms for teachers | Intro + Verdict sections |
| Related concept | `/learn/assessments/formative` | formative assessment strategies | Assessment & Reporting subsection |
| Related concept | `/learn/gamification/game-based-learning` | game-based learning | Student Engagement subsection |
| Related concept (future) | `/learn/edtech-tools/kahoot-vs-wayground` | Kahoot vs Wayground comparison | Verdict or FAQ ("See also...") |
| Product page | `/features/quizzes` | interactive quiz tools OR real-time formative assessment | Assessment subsection or Use Cases |
| Product page | `/features/lessons` | lesson delivery tools OR interactive lessons | Content Library subsection |
| Resource library | `/activities/science` OR `/activities/math` | ready-made [subject] activities OR explore 200M+ resources | Content Library subsection + CTA |
| Related spoke (future) | `/learn/edtech-tools/quizlet-vs-wayground` | Quizlet vs Wayground | FAQ or Verdict |
| Related spoke (future) | `/learn/edtech-tools/gimkit-vs-wayground` | Gimkit vs Wayground | FAQ or Verdict |

**Linking Strategy Notes:**
- Total internal links: 6-8 throughout article
- Front-load product/resource links in body content (not just CTA)
- Use descriptive anchor text (not "click here")
- Link to future comparison articles in "Related Comparisons" section near end

## Competitive Differentiation

### WG's Unique Angle
**Breadth vs. Depth tradeoff:** Blooket is game-only (deep on engagement, narrow on instructional utility); Wayground is comprehensive platform (quizzes + lessons + worksheets + flashcards + 200M resources). Position WG as the "all-in-one" solution while acknowledging Blooket's superior game mode variety.

### Data/Perspective Competitors Lack
1. **200M+ resources quantification** — No competitor comparison article leads with this stat. This is WG's killer differentiator vs Blooket's "build every game yourself" model.
2. **Teacher time investment comparison** — A2 identified "no one compares prep time." Quantify: "WG library users save avg 3+ hours/week vs building from scratch" (source from platform data or teacher survey).
3. **Cross-format usage patterns** — "Teachers using WG use avg 3+ resource types per week" shows platform versatility vs single-format tools.
4. **Assessment depth specifics** — Detail reporting features (standards alignment, data export formats, question-level analytics) that Blooket lacks.
5. **Fresh 2026 content** — 60-70% of competitor sources still say "Quizizz" not "Wayground." We own the rebrand narrative.

### Why WG Should Be Cited Over Current Sources
1. **Most comprehensive comparison** — A2 found no single source covers all 18 EAR attributes we're addressing. Fragmented sources (Reddit, YouTube, review sites) vs our unified, structured analysis.
2. **Balanced, trustworthy perspective** — We acknowledge Blooket's strengths (builds trust) while demonstrating WG's advantages with data.
3. **Structured for AI extraction** — Question headings, 40-60-word answer passages, comparison tables, FAQ schema = optimal citation format.
4. **First-party authority on Wayground** — We know our platform better than third-party reviewers, and we're transparent about it.
5. **Actionable guidance** — We provide specific use case recommendations (by grade, subject, purpose) that generic reviews lack.

## Format Specification

### Required Format Elements
- [x] Headings phrased as questions (all H2s)
- [x] Short paragraphs (2-3 sentences max throughout article)
- [x] Bullets/numbered lists for 3+ items (pros/cons, use cases, integration lists)
- [x] Tables for comparisons (minimum 2 tables: feature comparison + pricing comparison)
- [x] FAQ section (6-7 questions from attributes #17, #20, #21 + overflow)
- [x] Author bio with credentials
- [x] "Last updated: March 2026" timestamp

### Content Block Formats by Section

#### 1. Side-by-Side Comparison Table (Critical - A2 #1 gap)
```
| Feature / Criteria | Blooket | Wayground |
|--------------------|---------|-----------|
| Primary focus | Game-based review | Comprehensive assessment platform |
| Activity formats | Games only | Quizzes, Lessons, Worksheets, Flashcards, Games |
| Content library | Build-your-own | 200M+ ready-made resources |
| Game modes | 10+ themed modes (Tower Defense, Gold Quest, etc.) | Multiple game formats + non-game activities |
| Question types | 5 basic types | 15+ types including open-ended |
| Reporting depth | Basic scores | Advanced analytics, standards alignment, data export |
| LMS integrations | Google Classroom | Google Classroom, Canvas, Schoology, more |
| Free tier limits | [Specify] | [Specify] |
| Paid plans start at | [Price] | [Price] |
| Best for | Quick engagement, review games | Full instructional cycle, formative assessment |
```
**Minimum 15 rows, use ✓ / ✗ / ⚠️ symbols where appropriate**

#### 2. Pricing Comparison Table
```
| Plan Tier | Blooket | Wayground |
|-----------|---------|-----------|
| Free | [Features] | [Features] |
| Individual Paid | $X/month - [Features] | $X/month - [Features] |
| School/District | Custom - [Features] | Custom - [Features] |
```

#### 3. Pros/Cons Lists
**Format:** 4 separate sections
- **Blooket Pros:** 5-7 specific bullets (e.g., "10+ game modes keep students highly engaged" not "good engagement")
- **Blooket Cons:** 4-5 honest bullets (e.g., "Limited to 5 basic question types" not "some limitations")
- **Wayground Pros:** 6-8 specific bullets emphasizing differentiators
- **Wayground Cons:** 3-4 honest bullets (builds trust — e.g., "Game modes less playful than Blooket's themed experiences")

#### 4. Use Case Recommendations
**Format:** Two subsections with bullet lists
- **"When to Choose Blooket":** 4-5 specific scenarios with context (grade, subject, timing, purpose)
  - Example: "Elementary math review sessions where high energy and competition drive practice"
  - Example: "Friday end-of-week review activities (10-15 minutes) for any subject"
- **"When to Choose Wayground":** 5-6 specific scenarios emphasizing comprehensive needs
  - Example: "Formative assessment throughout instruction with detailed reporting for data-driven decisions"
  - Example: "When you need quiz + lesson + worksheet for a complete unit (all in one platform)"

#### 5. Grade Level Guidance
**Format:** 3 subsections (100 words each)
- **Elementary (K-5):** Recommendation with rationale
- **Middle School (6-8):** Recommendation with rationale
- **High School (9-12):** Recommendation with rationale
Each should acknowledge both platforms' viability but guide toward best fit

#### 6. Teacher Testimonials
**Format:** Blockquotes with attribution
```
"[Quote text — 2-3 sentences about specific use case]"
— [Name], [Grade/Subject] Teacher, [Years Experience], [Location if relevant]
```
**Critical:** At least one quote must compare both platforms (e.g., "I use Blooket for Friday review games, but Wayground for my weekly formative checks because I need the detailed reporting")

#### 7. FAQ Section
**Format:** H3 questions with 40-60 word answers
Minimum 6 questions covering:
- Is Blooket or Wayground better for formative assessment?
- Which platform is easier to learn and set up?
- Can I use both Blooket and Wayground together?
- Does Wayground have the same game modes as Blooket?
- Which has better reporting and analytics?
- Are both platforms FERPA/COPPA compliant?
- Do both have mobile apps?

### Schema Markup Requirements
1. **ComparisonTable schema** for side-by-side feature table
2. **Product schema** for both Blooket and Wayground (name, aggregateRating if available, offers/price)
3. **FAQPage schema** for FAQ section (Question/Answer pairs)
4. **Article schema** with headline, author, datePublished, dateModified
5. **Organization schema** for Wayground with logo, url, sameAs (social profiles)

### Tone & Voice Guidelines
- **Sound like:** A knowledgeable teaching colleague who has used both platforms and is giving honest advice
- **NOT:** A Wayground sales rep, a generic review site, an academic paper
- **Acknowledge Blooket strengths prominently** — e.g., "Blooket's Tower Defense mode gets incredible engagement in elementary classrooms" (specific, fair, builds trust)
- **Position WG advantages with data** — e.g., "Wayground's 200M+ resource library means you can find ready-made content for virtually any topic, saving hours of creation time" (quantified, specific, value-focused)
- **Use first-person for WG data** — "Based on Wayground users..." or "We tested..." (transparency about first-party perspective)
- **Use "you" for teacher-direct address** — "If you need detailed reporting..." "When you're short on prep time..."

### SEO/AEO Optimization Notes
- **H1:** "Blooket vs Wayground: Which Is Better for Your Classroom? (2026 Comparison)"
- **Meta description (155 chars):** "Compare Blooket and Wayground (formerly Quizizz) for classroom engagement and assessment. See features, pricing, pros/cons, and which is best for your grade level."
- **URL slug:** `/learn/edtech-tools/blooket-vs-wayground`
- **Image alt text:** Include "Blooket vs Wayground comparison" in primary comparison table screenshot
- **Include "formerly Quizizz" in first 100 words** — captures legacy brand search traffic
- **Internal link at least 6-8 times** to related WG content
- **External links:** Cite blooket.com (shows fairness), link to research sources, optionally link to Common Sense Education or EdSurge reviews (shows transparency)

## Risk Mitigation

### Risk: Appearing Biased (Brand-Owned Content)
**Mitigation tactics:**
1. Lead Blooket strengths prominently in Pros section
2. Include teacher quote praising Blooket for specific use case
3. Link to blooket.com official site (shows we're not hiding their info)
4. Honest WG cons (e.g., "Blooket's game modes are more playful/themed")
5. Use data and specifics, not subjective claims ("15 question types" vs "better questions")

### Risk: Outdated Blooket Information (Fabrication Concern)
**Mitigation tactics:**
1. Cite blooket.com with "as of March 2026" timestamp
2. Never fabricate Blooket stats — use "[Stat]" placeholder for C4 agent to research if needed
3. Include disclaimer near pricing: "Platform features and pricing change; verify on official sites"
4. Avoid absolute statements ("Blooket has exactly 10 game modes") — use "as of [date]" qualifiers

### Risk: AI Engines Preferring Third-Party Aggregators
**Mitigation tactics:**
1. Match or exceed aggregator structure quality (we have better tables, more comprehensive coverage)
2. Include teacher testimonials (peer authority signal)
3. Use schema markup extensively (ComparisonTable especially)
4. Optimize for featured snippet extraction (40-60 word passages, question headings)
5. Build parallel third-party presence (note for growth team: update EdSurge, solicit Common Sense Education review)

## Success Criteria for D1 Evaluation

### Must-Pass Requirements (Score ≥7)
- [ ] All 15 must-cover attributes present (per B2 analysis)
- [ ] Side-by-side comparison table with minimum 15 rows
- [ ] Major differentiators addressed: Content library (#7), Assessment depth (#8), Time investment (#18)
- [ ] Balanced tone: Blooket strengths acknowledged
- [ ] Question-phrased H2 headings
- [ ] 40-60 word extractable answer passages
- [ ] No fabricated statistics
- [ ] Teacher testimonials include user of BOTH platforms

### Target Score Requirements (Score 9/10)
- [ ] 18/21 attributes covered (all must-cover + 3 nice-to-have)
- [ ] All format elements present (tables, lists, FAQ, quotes)
- [ ] Statistics with proper attribution (minimum 5)
- [ ] Expert quotes with credentials (minimum 3)
- [ ] Internal linking plan executed (6-8 links)
- [ ] Schema markup ready (ComparisonTable, Product, FAQPage, Article)
- [ ] Competitive differentiation clearly articulated
- [ ] Honest WG cons included (trust signal)

### Exceptional Score Requirements (Score 10/10)
- [ ] 20-21/21 attributes covered
- [ ] All above plus: migration guide, subject-specific recommendations, accessibility details
- [ ] 6+ statistics, 4+ quotes
- [ ] Video embed or visual comparison (if available)
- [ ] External links to blooket.com + research sources (transparency)

## Content Generation Notes for C-Phase Agents

### For C1 (Structure Builder)
- Use expansion structure table above — 15 major sections
- Allocate word count: 
  - Intro: 100 words
  - Quick comparison table: 150 words + table
  - Definitions: 200 words (100 each)
  - Feature comparison (5 subsections): 1000 words (200 each)
  - Pricing: 200 words + table
  - Time investment: 200 words
  - Use cases: 300 words
  - Grade level: 300 words
  - Subject: 200 words
  - Pros/cons: 400 words
  - Testimonials: 300 words
  - Migration: 200 words
  - FAQ: 350 words
  - Verdict: 200 words
  - **Total: ~3,500 words**

### For C2 (Research Specialist) & C4 (Citation Enricher)
- **Priority research tasks:**
  1. Blooket official site: user count, game mode count, question types, pricing (cite with date)
  2. Research on game-based learning effectiveness (for engagement section)
  3. Research on formative assessment reporting value (for assessment section)
  4. Verify WG stats: 200M+ resources current? User base stats? Question type count?
- **Never fabricate:** If you can't find a Blooket stat, use placeholder "[According to Blooket, X users]" and flag for review

### For C3 (Drafter) & C5 (Expert Quote Sourcer)
- **Critical voice requirement:** Teacher-to-teacher, specific, balanced
- **Quote sourcing:** Contact WG teacher network for quotes. **Must find at least one teacher who has used BOTH platforms.**
- **Example quote format:** 
  - ✅ GOOD: "I use Blooket every Friday for math review—my 5th graders go crazy for Gold Quest. But for my unit assessments, I use Wayground because I need detailed data on which standards students are struggling with."
  - ❌ BAD: "I like Wayground better because it has more features."
- **Blooket acknowledgment examples:**
  - "Blooket's 10+ game modes offer more variety than Wayground's game options"
  - "For pure engagement and excitement, Blooket's themed games (Tower Defense, Racing) often edge out Wayground's formats"
  - "Elementary teachers consistently report that Blooket's visual, fast-paced games work better for younger students' attention spans"

### For D1 (AEO Evaluator)
Use B2's scoring rubric:
- **PASS threshold:** 12/15 must-cover attributes + 3/5 major differentiators + balanced tone = Score 7
- **Target:** 15/15 must-cover + 5/5 major differentiators + 3 nice-to-have = Score 9
- **Flag for REVISION if:**
  - Missing attributes #3 (table), #7 (library), #8 (assessment), or #14 (verdict)
  - Tone is one-sided (no Blooket strengths acknowledged)
  - Statistics appear fabricated (no sources)
  - No teacher testimonials or none from dual users
- **Flag for ESCALATION if:** <10/15 must-cover attributes

## Metadata

| Field | Value |
|-------|-------|
| Brief created by | B3 (Content Brief Generator) |
| Date | 2026-03-18 |
| Input sources | A1 (dossier), A2 (citation audit), B1 (intent classifier), B2 (EAR decomposer) |
| Target word count | 2,500-3,500 |
| EAR attributes mapped | 18/21 (86%) |
| Major differentiators | 5 (Content library, Assessment depth, Time investment, Side-by-side table, WG rebrand) |
| Projected D1 score | 9/10 |
| Ready for C-phase? | ✅ Yes |
| Approval status | Draft — pending review |

---

**Brief Status:** Complete and ready for downstream agents (C1-C5). All upstream inputs (A1, A2, B1, B2) have been synthesized into actionable content requirements. This brief provides sufficient detail for content generation without additional context.

#### C1 Output
# Research Packet: Blooket vs Wayground Comparison
> C1 Research Agent Output
> Topic: Blooket vs Wayground for Classroom Learning
> Date: 2026-03-19
> Status: Research Framework (requires source verification)

## Executive Summary
This research packet outlines the statistics, expert quotes, and supporting evidence required for the comparison article. **CRITICAL NOTE:** Due to access limitations, this packet provides a research framework with specific sourcing instructions rather than pre-gathered data. All statistics marked with `[VERIFY]` must be researched and verified before use in content generation.

---

## Section 1: Required Statistics with Source Instructions

### 1.1 Platform Scale & Reach Statistics

#### Stat #1: Blooket User Base
- **What to find:** Total registered users OR total games played OR schools using platform
- **Primary source:** blooket.com official site (About page, Press page, or footer stats)
- **Secondary sources:** Blooket social media (Twitter/X, LinkedIn company page)
- **Date requirement:** Must be 2025-2026 data
- **Citation format:** "According to Blooket, [X million] users have played [Y billion] games as of [Month Year]."
- **Backup if unavailable:** "Blooket has gained significant adoption in K-12 classrooms since its launch in 2020" (cite launch date from official source)

**PLACEHOLDER FOR C2/C4:**
```
[VERIFY: Blooket user/games statistics from blooket.com]
Source URL: [TO BE ADDED]
Date accessed: [TO BE ADDED]
Publication date: [TO BE ADDED]
```

#### Stat #2: Wayground Resource Library & User Base
- **What to find:** 
  - 200M+ resources (confirm current number)
  - Total registered users or teachers
  - Monthly active users (if available)
- **Primary source:** Internal platform data (first-party)
- **Secondary verification:** Wayground.com official site, press releases, LinkedIn company page
- **Citation format:** "Wayground's library contains more than 200 million ready-made resources, used by [X million] teachers across [Y] countries."
- **First-person framing:** "Based on Wayground platform data, teachers access an average of [X] resources per week..."

**PLACEHOLDER FOR C2/C4:**
```
[VERIFY: Wayground 200M+ resources stat - confirm current count]
[VERIFY: Wayground teacher user base]
[VERIFY: Platform usage patterns - resources accessed per teacher]
Source: Internal platform analytics
Date: March 2026
```

### 1.2 Feature Inventory Statistics

#### Stat #3: Blooket Game Modes & Question Types
- **What to find:**
  - Exact count of game modes (Tower Defense, Gold Quest, Racing, etc.)
  - Question types supported (multiple choice, true/false, etc.)
  - Free vs paid feature limits
- **Primary source:** blooket.com feature pages, help documentation
- **Citation format:** "As of March 2026, Blooket offers [X] game modes, including Tower Defense, Gold Quest, and Racing."

**PLACEHOLDER FOR C2/C4:**
```
[VERIFY: Blooket game mode count from blooket.com]
[VERIFY: Blooket question type count and types]
Source URL: [TO BE ADDED]
Date: March 2026
```

#### Stat #4: Wayground Question Types & Activity Formats
- **What to find:**
  - Question type count (brief claims "15+ types including open-ended")
  - Activity format count (quizzes, lessons, worksheets, flashcards, games)
- **Primary source:** Internal product documentation
- **Citation format:** "Wayground supports 15+ question types, including multiple choice, open-ended, fill-in-the-blank, polls, and drawing responses."

**PLACEHOLDER FOR C2/C4:**
```
[VERIFY: Wayground question type count - confirm "15+" claim]
[VERIFY: Activity format breakdown]
Source: Internal product team
Date: March 2026
```

### 1.3 Engagement & Effectiveness Statistics

#### Stat #5: Game-Based Learning Effectiveness Research
- **What to find:** Recent research on game-based learning impact on engagement, retention, or learning outcomes
- **Preferred sources:**
  - Peer-reviewed journals (Journal of Educational Technology, Computers & Education)
  - Meta-analyses on gamification in education
  - Government education research (IES, What Works Clearinghouse)
- **Date requirement:** 2022-2026 preferred
- **Citation format:** "According to a [Year] study published in [Journal], game-based learning increased student engagement by [X]% compared to traditional methods."

**PLACEHOLDER FOR C2/C4:**
```
[VERIFY: Research on game-based learning effectiveness]
Suggested search terms: "game-based learning effectiveness 2024-2026" "gamification education research" "digital game-based learning meta-analysis"
Source type: Peer-reviewed research
```

#### Stat #6: Formative Assessment & Reporting Impact Research
- **What to find:** Research on the value of detailed assessment data for improving student outcomes
- **Preferred sources:**
  - Education research journals
  - NCTM, NSTA, or other subject-specific association research
  - Brookings, RAND education studies
- **Citation format:** "Research from [Organization] found that teachers using detailed formative assessment data improved student achievement by [X]% over those using basic scoring alone."

**PLACEHOLDER FOR C2/C4:**
```
[VERIFY: Research on formative assessment reporting effectiveness]
Suggested search terms: "formative assessment data-driven instruction effectiveness" "assessment analytics teacher impact"
Source type: Education policy research
```

### 1.4 Time Savings & Efficiency Statistics

#### Stat #7: Teacher Time Investment - Resource Creation vs Library Use
- **What to find:**
  - Average time teachers spend creating activities from scratch
  - Time savings from using pre-made resources
- **Preferred sources:**
  - Internal Wayground user survey data
  - External teacher workload studies (NCES, EdWeek Research Center)
  - Teacher time use research
- **Citation format:** "Based on Wayground user surveys, teachers using the platform's library save an average of [X] hours per week compared to building activities from scratch."

**PLACEHOLDER FOR C2/C4:**
```
[VERIFY: Teacher time savings data]
Option A: Internal WG user survey (preferred - first-party data)
Option B: General teacher time use research + estimate
Source: [TO BE DETERMINED]
Date: 2025-2026
```

#### Stat #8: Content Freshness & AI Citation Preference
- **What to find:** Research showing AI systems prefer recent content
- **Note:** Brief mentions "ChatGPT favors 30-day-old content 3.2x more"
- **Action required:** Verify this statistic or find similar research on content freshness in AI citation
- **Citation format:** "According to [Source/Study], AI language models are [X]x more likely to cite content published within the last 30 days compared to older sources."

**PLACEHOLDER FOR C2/C4:**
```
[VERIFY: "3.2x more likely" statistic - find original source]
Suggested search: "AI citation content freshness research" "ChatGPT content recency preference"
CRITICAL: Do not use this stat if source cannot be verified
```

### 1.5 Pricing Statistics

#### Stat #9: Platform Pricing Comparison
- **What to find:**
  - Blooket free tier limits and paid plan pricing
  - Wayground free tier limits and paid plan pricing
  - School/district pricing structures (if publicly available)
- **Primary sources:**
  - blooket.com/pricing
  - wayground.com/pricing
- **Date requirement:** Current as of March 2026
- **Format:** Will be presented in comparison table format

**PLACEHOLDER FOR C2/C4:**
```
[VERIFY: Blooket pricing from blooket.com/pricing]
[VERIFY: Wayground pricing from wayground.com/pricing]
Source URLs: [TO BE ADDED]
Date verified: March 2026
Note: Include disclaimer that pricing subject to change
```

---

## Section 2: Expert Quotes & Testimonials

### Critical Sourcing Requirements
- **All quotes must be real and attributable** - no fabrication
- **At least one teacher must have used BOTH platforms** - this is essential for credibility
- **Full attribution required:** Name, Grade/Subject, School/District (if allowed), Years of Experience
- **Consent required:** All quoted teachers must consent to being quoted

### 2.1 Required Quote #1: Dual-Platform User (CRITICAL)

**Quote topic:** Teacher who has experience with both Blooket and Wayground, describing when to use each

**Desired content:**
- Acknowledges strengths of both platforms
- Provides specific use case for each
- Shows nuanced understanding (e.g., "I use Blooket for X, but Wayground for Y")

**Example format:**
```
"[Quote comparing both platforms with specific use cases - 2-3 sentences]"
— [Name], [Grade] [Subject] Teacher, [X] years experience, [Location]
```

**Sourcing instructions for C5:**
1. Contact Wayground teacher network/community managers
2. Search for teachers who mention both platforms in reviews, Reddit, Twitter
3. Request testimonials through teacher advisory board
4. Ensure written permission for quote usage

**PLACEHOLDER FOR C5:**
```
[QUOTE NEEDED: Teacher with Blooket + Wayground experience]
Status: TO BE SOURCED
Priority: CRITICAL - cannot publish without this
```

### 2.2 Required Quote #2: Blooket Advocate

**Quote topic:** Teacher praising Blooket's game modes or engagement features

**Desired content:**
- Specific game mode mentioned (Tower Defense, Gold Quest, etc.)
- Grade level context
- Concrete engagement outcome or student reaction

**Target source types:**
- Elementary or Middle School teacher
- Teacher reviews on Common Sense Education
- Blooket user testimonials (with permission)
- Reddit r/Teachers posts (with permission)

**PLACEHOLDER FOR C5:**
```
[QUOTE NEEDED: Teacher praising Blooket engagement/games]
Status: TO BE SOURCED
Grade level: Elementary or Middle School preferred
```

### 2.3 Required Quote #3: Wayground Assessment Advocate

**Quote topic:** Teacher praising Wayground's assessment depth, reporting, or resource library

**Desired content:**
- Specific feature mentioned (standards alignment, data export, resource library)
- How it improved their teaching or saved time
- Grade/subject context

**Target source types:**
- Middle or High School teacher preferred
- Wayground case studies
- Internal teacher network
- Wayground user testimonials

**PLACEHOLDER FOR C5:**
```
[QUOTE NEEDED: Teacher praising WG assessment/library features]
Status: TO BE SOURCED
Grade level: Middle or High School preferred
Feature focus: Assessment reporting OR resource library time savings
```

### 2.4 Optional Quote #4: Time Savings Testimonial

**Quote topic:** Teacher describing time saved by using resource library vs building from scratch

**Desired content:**
- Quantified time savings (e.g., "saves me 2-3 hours per week")
- Specific workflow description
- Grade/subject context

**PLACEHOLDER FOR C5:**
```
[QUOTE OPTIONAL: Teacher on time savings]
Status: Nice-to-have if available from teacher network
```

---

## Section 3: Supporting Evidence by Article Section

### 3.1 Student Engagement Section

**Evidence needed:**
- Research on game-based learning engagement vs traditional methods
- Platform engagement metrics (completion rates, time on task)
- Student satisfaction data

**Sources to pursue:**
- Journal of Educational Technology & Society
- "Digital Game-Based Learning" meta-analyses
- Platform-specific engagement data (internal)

**Citation examples:**
- "According to [Year] research in [Journal], students using game-based learning platforms showed [X]% higher engagement compared to traditional practice methods."
- "Based on Wayground platform data, students complete an average of [X] activities per week, with [Y]% completion rates."

**PLACEHOLDER FOR C2:**
```
[VERIFY: Game-based learning engagement research]
[VERIFY: Platform engagement metrics - internal data]
```

### 3.2 Content Library & Resources Section

**Evidence needed:**
- 200M+ resources stat (confirmed)
- Resource creation time vs library browsing time
- Resource diversity statistics (subjects, grades, formats)
- Teacher adoption rates of library resources

**Sources to pursue:**
- Internal platform analytics (first-party)
- Teacher time-use research (NCES, EdWeek)
- Platform usage patterns

**Citation examples:**
- "Wayground's library includes more than 200 million educator-created resources spanning all major subjects and grade levels K-12."
- "On average, teachers using Wayground access [X] pre-made resources per week, saving an estimated [Y] hours of creation time."

**PLACEHOLDER FOR C2:**
```
[VERIFY: WG resource library statistics - subjects, grades, types]
[VERIFY: Library usage patterns - resources used per teacher]
[VERIFY: Time savings calculations]
```

### 3.3 Assessment & Reporting Section

**Evidence needed:**
- Question type inventory (both platforms)
- Reporting feature comparison (standards alignment, data export formats, analytics depth)
- Research on data-driven instruction effectiveness
- Teacher usage of reporting features

**Sources to pursue:**
- Platform feature documentation (both platforms)
- Internal product specs for Wayground
- Education research on formative assessment data use

**Citation examples:**
- "Wayground offers 15+ question types including open-ended responses, while Blooket focuses on 5 core question formats optimized for fast-paced gameplay."
- "Research from [Organization] found that teachers with access to detailed, standards-aligned assessment data improved student outcomes by [X]%."

**PLACEHOLDER FOR C2:**
```
[VERIFY: Question type counts - both platforms]
[VERIFY: Reporting feature comparison - detailed specs]
[VERIFY: Formative assessment research]
```

### 3.4 Ease of Use & Setup Section

**Evidence needed:**
- Setup time comparison (creating first activity on each platform)
- Learning curve data
- Teacher onboarding statistics
- User experience research or reviews

**Sources to pursue:**
- User reviews (Common Sense Education, Capterra, G2)
- Internal onboarding data (Wayground)
- Teacher testimonials on ease of use

**Citation examples:**
- "According to teacher reviews on [Platform], Blooket's interface receives an average rating of [X]/5 for ease of use."
- "New Wayground teachers create their first activity within an average of [X] minutes of signing up."

**PLACEHOLDER FOR C2:**
```
[VERIFY: User reviews - ease of use ratings]
[VERIFY: Setup time data - both platforms if available]
```

### 3.5 Integrations & LMS Compatibility Section

**Evidence needed:**
- Integration lists (both platforms)
- Google Classroom, Canvas, Schoology compatibility details
- SSO options
- Data sync capabilities

**Sources to pursue:**
- Platform integration documentation (both platforms)
- Feature pages on official websites

**Citation examples:**
- "As of March 2026, Blooket integrates with Google Classroom, allowing teachers to import rosters and sync grades."
- "Wayground supports integrations with Google Classroom, Canvas, Schoology, Clever, and [X] other LMS platforms."

**PLACEHOLDER FOR C2:**
```
[VERIFY: Blooket integration list - blooket.com]
[VERIFY: Wayground integration list - wayground.com or internal docs]
Date: March 2026
```

### 3.6 Pricing & Value Section

**Evidence needed:**
- Free tier feature limits (both platforms)
- Paid plan pricing and features (both platforms)
- School/district pricing models
- ROI data if available

**Sources to pursue:**
- Official pricing pages (both platforms)
- Sales documentation (if available)

**PLACEHOLDER FOR C2:**
```
[VERIFY: Complete pricing comparison - both platforms]
Source: Official pricing pages
Date: March 2026
Include disclaimer: "Pricing and features subject to change; visit official sites for current information"
```

---

## Section 4: Wayground-Specific First-Party Data

### 4.1 Platform Usage Patterns (Internal Data Required)

**Data points needed:**
1. Average number of resource types used per teacher per week
2. Most popular activity formats (quizzes vs lessons vs worksheets)
3. Average resources accessed per teacher per week
4. Time spent browsing library vs creating content
5. Student completion rates by activity type

**Citation format:** "Based on Wayground platform data from [timeframe], teachers use an average of [X] different resource types per week..."

**PLACEHOLDER FOR C2:**
```
[VERIFY: Internal platform analytics - usage patterns]
Source: Wayground product/analytics team
Timeframe: Last 6-12 months preferred
Permission: Ensure data can be publicly shared
```

### 4.2 Teacher Feedback & Survey Data (Internal)

**Data points needed:**
1. Teacher satisfaction scores
2. Time savings self-reported data
3. Feature usage statistics
4. NPS scores if available

**PLACEHOLDER FOR C2:**
```
[VERIFY: Teacher survey data or feedback]
Source: UXR team, customer success team
Recent survey results: 2025-2026
```

### 4.3 Content Quality & Vetting

**Data points needed:**
1. Number of teacher-vetted resources
2. Vetting process description
3. Quality control statistics

**Note from product-context:** "~30 articles already through teacher vetting loop"

**Citation format:** "All Wayground content undergoes review by our network of [X] educators before publication."

**PLACEHOLDER FOR C2:**
```
[VERIFY: Content vetting process and statistics]
Source: Content team, teacher network managers
```

---

## Section 5: External Source Verification Requirements

### 5.1 Blooket Official Sources

**Must verify from blooket.com:**
- Platform overview and positioning statement
- Feature list (game modes, question types)
- Pricing information
- User statistics if available
- Integration list

**URL targets:**
- blooket.com
- blooket.com/pricing
- blooket.com/features or /how-it-works
- Blooket help documentation
- Blooket blog (for statistics or updates)

**PLACEHOLDER FOR C2:**
```
[VERIFY: All Blooket information from official sources]
Date accessed: March 2026
Rationale: Shows fairness, prevents misinformation about competitor
```

### 5.2 Third-Party Reviews & Aggregators

**Optional sources for balanced perspective:**
- Common Sense Education reviews (both platforms)
- Capterra reviews and ratings
- G2 reviews
- EdSurge product profiles
- Reddit r/Teachers discussions

**Use for:**
- User ratings and satisfaction scores
- Teacher testimonials (with permission)
- Common praise/criticism themes
- Comparative sentiment

**PLACEHOLDER FOR C2:**
```
[OPTIONAL: Third-party review aggregation]
Purpose: Provide independent validation of claims
Note: Must verify review authenticity and recency
```

---

## Section 6: Research Quality Standards

### Source Credibility Hierarchy

**Tier 1 - Highest Credibility:**
- Peer-reviewed academic research
- Government education data (NCES, IES)
- Official platform statistics (first-party)
- Major education research organizations (RAND, Brookings)

**Tier 2 - High Credibility:**
- Industry research (EdWeek Research Center)
- Education association research (NCTM, NSTA, ASCD)
- Verified teacher testimonials
- Reputable education news sources (EdSurge, EdWeek)

**Tier 3 - Moderate Credibility:**
- Review platforms (Common Sense Education, Capterra)
- Education blogs with clear author credentials
- Platform help documentation
- Social media from verified educators

**DO NOT USE:**
- Unverified statistics
- Anonymous testimonials
- Marketing copy without substantiation
- Fabricated data or quotes

### Date Requirements

- **Platform features/pricing:** Must be current as of March 2026
- **Research studies:** 2022-2026 preferred; 2020+ acceptable if seminal
- **Statistics:** Clearly dated; include "as of [date]" qualifiers
- **Quotes:** Recent (2024-2026) unless historical context

### Citation Format Standards

**For statistics:**
```
"According to [Source], [Statistic] as of [Date]."
```

**For research:**
```
"A [Year] study published in [Journal/Organization] found that [Finding]."
```

**For platform data:**
```
"Based on [Platform Name] data from [Timeframe], [Statistic]."
```

**For quotes:**
```
"[Quote]," says [Name], [Title/Role], [Organization/Location].
```

---

## Section 7: Research Gaps & Flags

### CRITICAL GAPS (Must resolve before draft)

1. **Blooket user statistics** - No verified source yet
   - **Action:** Research blooket.com official site and social media
   - **Backup:** Use descriptive language instead of specific numbers if unavailable

2. **Dual-platform teacher testimonial** - Required but not yet sourced
   - **Action:** C5 must prioritize this through teacher network outreach
   - **Backup:** Cannot proceed to publish without this

3. **AI content freshness research (3.2x stat)** - Mentioned in brief but not verified
   - **Action:** Find original source or remove this claim
   - **Risk:** If fabricated, must not use

### MODERATE GAPS (Can proceed with placeholders)

4. **Time savings quantification** - Need survey data or research
   - **Action:** Internal survey or external teacher workload research
   - **Backup:** Use qualitative descriptions if quantitative data unavailable

5. **Platform engagement metrics** - Would strengthen engagement section
   - **Action:** Request from analytics team
   - **Backup:** Focus on external research instead

### NICE-TO-HAVE

6. **Third-party review ratings** - Would add external validation
7. **Subject-specific usage patterns** - Would support subject recommendations
8. **Grade-level adoption data** - Would support grade recommendations

---

## Section 8: Source Credibility Notes

### Wayground First-Party Data Transparency

**Strategy:** Be explicit about first-party perspective to build trust
- ✅ "Based on Wayground platform data..."
- ✅ "According to internal user surveys..."
- ✅ "We tested..."
- ❌ Avoid: Presenting first-party data as if it's third-party research

**Rationale:** Transparency about being brand-owned content builds credibility with both human readers and AI systems evaluating E-E-A-T signals.

### Blooket Information Fairness

**Strategy:** Link to Blooket official sources when citing their features/data
- Shows we're not hiding competitor information
- Prevents misinformation about competitor
- Builds trust with readers who will fact-check

**Implementation:** Every Blooket statistic or feature claim should cite blooket.com with date accessed.

---

## Section 9: Research Execution Checklist

**For C2 (Research Specialist) & C4 (Citation Enricher):**

- [ ] Verify all Blooket statistics from blooket.com (features, pricing, game modes)
- [ ] Confirm Wayground 200M+ resources current count
- [ ] Research game-based learning effectiveness (peer-reviewed source)
- [ ] Research formative assessment reporting impact (peer-reviewed source)
- [ ] Gather internal Wayground usage statistics (product/analytics team)
- [ ] Verify or remove "3.2x content freshness" claim
- [ ] Complete pricing comparison (both platforms, current as of March 2026)
- [ ] Gather integration lists (both platforms)
- [ ] Request teacher time savings data (survey or research)
- [ ] Flag any gaps that cannot be filled with verified sources

**For C5 (Expert Quote Sourcer):**

- [ ] **CRITICAL:** Source teacher with both Blooket and Wayground experience
- [ ] Source teacher testimonial praising Blooket (elementary/middle school)
- [ ] Source teacher testimonial praising Wayground assessment/library
- [ ] Obtain written permission for all quotes
- [ ] Verify teacher credentials and attributions
- [ ] Optional: Source time savings testimonial

---

## Appendix: Research Methodology Notes

### Why This Approach

This research packet takes a **framework approach** rather than providing pre-gathered data because:

1. **No fabrication principle:** I cannot access external sources currently, and creating fake statistics would violate the core constraint
2. **Verifiability requirement:** All statistics must be traceable to credible sources
3. **Transparency:** Better to clearly mark what needs verification than to guess

### Next Steps for C2/C4 Agents

1. Use web search and source access to fill in `[VERIFY]` placeholders
2. Replace all bracketed placeholders with actual data and citations
3. Remove any statistics that cannot be verified rather than fabricating
4. Document all sources with URLs, dates accessed, and publication dates
5. Flag any claims in the brief that cannot be substantiated

### Quality Control

Before passing to C3 (Drafter):
- Every statistic must have a verified source URL
- Every quote must have full attribution and consent
- Any unverifiable claims must be removed or reframed
- Date stamps must be current (March 2026)

---

**Research Packet Status:** Framework complete — requires source verification before content generation

**Critical Path:** C2/C4 must complete verification → C5 must source dual-platform teacher quote → C3 can begin draft

**Risk Level:** MODERATE - Several key statistics need verification, particularly competitor data and dual-platform testimonial

---
Now execute your task. Put your final output inside `<output>` tags.
