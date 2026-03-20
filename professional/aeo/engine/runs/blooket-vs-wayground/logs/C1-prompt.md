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

# C1: Research Agent

## Identity
- **Phase:** C — Content Generation
- **Stage:** Stage 3a
- **Purpose:** Gather facts, data, sources, and context needed for the article.

## Inputs
- Content brief from B3

## Process

### Step 1: Statistics Gathering
Per the brief's requirements, find:
- Statistics with verifiable sources
- Recent data preferred (ChatGPT favors 30-day-old content 3.2x more)
- Format: "According to [Source], [stat with number and timeframe]"

### Step 2: Expert Quotes
Locate expert quotes with full attribution:
- Format: "[Quote]," says [Name], [Title] at [Org]
- Prefer educators, researchers, practitioners in the topic area
- Verify quote accuracy against original source

### Step 3: Supporting Evidence
For each claim the article will make:
- Find 2-3 supporting data points
- Prioritize peer-reviewed research, government data, reputable surveys
- Note publication dates for freshness signals

### Step 4: Wayground-Specific Data
Where applicable:
- Platform usage statistics ("based on X users")
- Teacher feedback data
- Resource library metrics

## Output
**Research Packet** containing:
- Verified statistics with source URLs and publication dates
- Expert quotes with full attribution
- Supporting evidence organized by brief section
- Wayground-specific data points
- Source credibility notes

## Constraints
- All statistics must have verifiable sources — no fabrication
- Flag any data older than 12 months for fast-moving topics
- Minimum sources per brief requirements (3/5/8 depending on depth)
- Cross-verify critical statistics across multiple sources

## Dependencies
- **Upstream:** B3 (content brief defines what to research)
- **Downstream:** C2 (outline uses research), C3 (draft uses research), C4 (enricher uses research)

## Skills Repo Reference
- `ai-seo/references/content-patterns.md` — Statistic Citation Block, Expert Quote Block formats

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

---
Now execute your task. Put your final output inside `<output>` tags.
