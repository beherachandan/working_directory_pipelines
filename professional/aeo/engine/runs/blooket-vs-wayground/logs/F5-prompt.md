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

# F5: Distribution Strategist Agent

## Identity
- **Phase:** F — Publish & Distribute
- **Stage:** WF4
- **Purpose:** Plan which off-site channels to activate for each piece of content to build multi-source frequency.

## Why This Agent Is Critical
Core AEO insight: "frequency across sources beats single #1 ranking."
Multi-source presence is Tier 2 factor (#6). Without distribution, content only exists on-site and lacks the corroboration AI engines use to build trust.

## Inputs
- Published page URL
- Topic and target queries
- Content type and intent

## Process

### Step 1: Channel Scoring
Score each channel's relevance for this specific topic (1-10):
- **Reddit:** Is there an active subreddit? (r/teachers, r/edtech, r/education)
- **YouTube:** Is this topic visual/demonstrable?
- **EdTech aggregators:** Does it fit TPT, edtech directories?
- **Medium/guest blogs:** Is there a thought leadership angle?
- **Quora:** Are there unanswered questions on this topic?
- **LinkedIn:** Professional audience relevance?
- **Wikipedia:** Can WG be cited as a source?
- **Email newsletter:** Does this serve existing subscribers?

### Step 2: Prioritization
Rank channels using the hierarchy:
1. Own site (already done)
2. YouTube (high authority, long-lasting)
3. Reddit (authentic community presence)
4. Tier-1 affiliates / EdTech aggregators
5. Industry blogs / Medium
6. Forums / Quora

### Step 3: Distribution Plan Creation
For each selected channel:
- Specific goal (awareness, backlink, citation surface)
- Content format needed (F6 will create)
- Timeline (Week 1-4)
- Success metric

### Step 4: Multi-Source Frequency Target
Set target: WG mentioned in X distinct sources within 30 days.
- Minimum: 3 sources (own site + 2 others)
- Target: 5+ sources for priority topics

## Output
**Distribution Plan** (using `templates/distribution-plan.md` template):
- Channel prioritization with scores
- Channel-specific plans
- Timeline
- Multi-source frequency targets

## Constraints
- Quality over quantity — don't spam channels
- Reddit/forum presence must be authentic and helpful (not promotional)
- Distribution should amplify the content's value, not just link-drop
- Budget considerations for paid channels

## Dependencies
- **Upstream:** F4 (page must be live first)
- **Downstream:** F6 (creates channel-specific content)

## Skills Repo Reference
- `social-content` — social media content creation

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

#### C5 Output

# C5 Composed Article: Blooket vs Wayground (Revision #3)

---

## C5 Composition Notes

### Actions Taken

**Consistency fixes:**
- Fixed FAQ Black & Wiliam reference to match corrected body text (was still citing "8 months" — now consistent with hedged framing)
- Standardized all first-party data disclosure language across sections (was inconsistent between engagement and time-investment sections)
- Ensured "Wayground (formerly Quizizz)" appears in first 100 words; all subsequent references use "Wayground" only
- Removed duplicate "Bottom line" transition patterns (5 of 7 subsections used identical phrasing — varied 2 for readability)

**Trust-specific fixes (addressing 6/10 score):**
- Elevated Transparency & Source Notes from end-of-article to a brief disclosure box in the intro (AI engines scan early content for trust signals)
- Added explicit "[PUBLICATION BLOCKER]" severity labels to all placeholder quotes (stronger than previous "[PLACEHOLDER]" flags)
- Removed remaining directional first-party claim in engagement section that lacked any specificity ("higher student completion rates") — replaced with transparent framing
- Added named author placeholder with credential requirements (generic "Education Content Team" scores zero on trust rubric)
- Strengthened FERPA/COPPA language with direct URL pointers

**Deduplication:**
- Consolidated overlapping "resource library" mentions (appeared 14 times; reduced to 10 contextually distinct uses)
- FAQ answer on formative assessment no longer repeats body text verbatim — rewritten for complementary angle

**Transition smoothing:**
- Added bridge sentence between definition sections and feature comparison
- Improved flow from pricing section into time-investment section
- Added brief transition into Verdict from FAQ

**Brief compliance issues flagged (cannot fix at C5 — upstream responsibility):**
- ⚠️ All 6 teacher quotes remain placeholders — **this is the primary trust blocker**
- ⚠️ [VERIFY] flags on product features remain — need research pass
- ⚠️ Pricing specifics still TBD

---

## Brief Compliance Checklist

- [x] All 15 must-cover EAR attributes addressed
- [x] QAPE structure intact (Q → A → P → E)
- [x] Required content blocks present (2 comparison tables, pros/cons, use cases, grade-level, subject, FAQ, verdict)
- [x] Internal links placed per linking plan (7 internal links, target 6-8)
- [x] Word count within target range (~3,400 words, target 2,500-3,500)
- [x] FAQ section has 7 items (target 6-8)
- [x] Headings phrased as questions (14/14 H2s)
- [ ] ⚠️ Stats/quotes/citations — stats meet minimum with hedging; **quotes are ALL placeholders (0/3 real)**
- [ ] ⚠️ Product feature verification incomplete ([VERIFY] flags remain)

---

# Blooket vs Wayground: Which Is Better for Your Classroom? (2026 Comparison)

**Title tag:** `Blooket vs Wayground: Which Is Best? (2026 Guide)` *(52 characters)*
**Meta description:** `Compare Blooket vs Wayground (formerly Quizizz) for your classroom. Features, pricing, pros/cons, and grade-level recommendations.` *(139 characters)*

---

Blooket is a game-based learning platform focused on review and practice through themed game modes like Tower Defense and Gold Quest. Wayground (formerly Quizizz) is a comprehensive learning platform offering quizzes, lessons, worksheets, flashcards, and 200M+ ready-made resources. Blooket excels at short engagement bursts. Wayground is better suited for full instructional workflows combining assessment, content delivery, and detailed reporting across multiple formats.

In this comparison, we break down features, pricing, pros and cons, and which platform fits your grade level and subject area — so you can make the right call for your students.

> **Disclosure:** This comparison is published by Wayground. We acknowledge Blooket's strengths throughout and clearly label all Wayground data as first-party. External research is cited with full publication details. Teacher quotes are sourced from real educators with documented consent. We link to [blooket.com](https://blooket.com) so you can verify their information directly.

*[Internal link: [classroom technology tools](/learn/edtech-tools/)]*

---

## How Do Blooket and Wayground Compare at a Glance?

Both Blooket and Wayground are widely used in K-12 classrooms, but they serve different instructional needs. The table below gives you a quick side-by-side view before we dig into the details.

| Feature / Criteria | Blooket | Wayground |
|--------------------|---------|-----------|
| **Primary focus** | Game-based review and practice | Comprehensive assessment and learning platform |
| **Activity formats** | Games only | Quizzes, Lessons, Worksheets, Flashcards, Games |
| **Content library** | Teacher-built question sets, community sharing | 200M+ ready-made resources across subjects and grades |
| **Game modes** | 10+ themed modes (Tower Defense, Gold Quest, Racing, Crazy Kingdom, etc.) [VERIFY at blooket.com] | Multiple game formats + non-game activity types |
| **Question types** | ~5 basic types (multiple choice, true/false, short answer) [VERIFY at blooket.com] | 15+ types including open-ended, equations, graphing, audio/video response [VERIFY at wayground.com] |
| **Reporting depth** | Basic scores and participation tracking | Advanced analytics, question-level data, standards alignment, data export |
| **Standards alignment** | ✗ Not available [VERIFY] | ✓ Built-in standards alignment tracking [VERIFY] |
| **LMS integrations** | Google Classroom [VERIFY current list at blooket.com] | Google Classroom, Canvas, Schoology, and more [VERIFY current list at wayground.com] |
| **Data export** | ⚠️ Limited [VERIFY] | ✓ Multiple formats (CSV, PDF, gradebook sync) [VERIFY] |
| **Free tier** | ✓ Generous free plan for teachers | ✓ Free plan with core features |
| **Paid plans** | Blooket Plus [VERIFY pricing at blooket.com/pricing] | Individual and School/District plans [VERIFY pricing at wayground.com/pricing] |
| **Mobile apps** | [VERIFY at blooket.com] | [VERIFY at wayground.com] |
| **Student accounts required** | Optional (join via game code) | Optional (join via activity code) |
| **Real-time feedback** | ✓ During gameplay | ✓ During activities + post-activity analytics |
| **Customization** | Create/edit question sets | Search, use, or customize from library resources |
| **Offline capability** | ⚠️ Limited | ⚠️ Limited |
| **FERPA/COPPA compliance** | [VERIFY at blooket.com/privacy] | [VERIFY at wayground.com/privacy] |
| **Best for (grade level)** | Elementary and Middle School | Elementary through High School |
| **Best use case** | Engagement-focused review and practice games | Full instructional cycle: content delivery, assessment, and reporting |
| **Teacher community** | Community-shared question sets | Large creator community with 200M+ shared resources |

*Note: Feature details are based on publicly available information as of March 2026. Platforms update frequently — verify specific capabilities on official sites before making purchasing decisions.*

---

## What Is Blooket?

[Blooket](https://blooket.com) is a game-based learning platform built around the idea that review and practice should feel like play. Teachers create question sets (or find community-shared ones), then launch themed game modes where students answer questions to earn points, collect items, or compete against classmates.

What sets Blooket apart is its variety of game modes — over 10 options including Tower Defense, Gold Quest, Racing, Battle Royale, and Crazy Kingdom. Each mode changes the gameplay mechanics, so students stay engaged even when reviewing the same content.

The visual, fast-paced format is especially popular with elementary and middle school students. Blooket's primary use case is short-burst review and practice sessions, typically 10-15 minutes. It's designed for engagement first, making it a go-to tool for teachers who want to energize review time.

---

## What Is Wayground?

Wayground is a comprehensive learning platform that goes well beyond quizzes. With 200M+ ready-made educational resources spanning quizzes, lessons, worksheets, flashcards, and game-based activities, Wayground is designed to support the full instructional cycle — from content delivery through assessment and reporting.

The platform offers 15+ question types, including open-ended responses, equation editors, graphing questions, drag-and-drop, matching, and audio/video responses. This breadth makes it suitable for everything from quick formative checks to in-depth summative assessments across all subjects and grade levels.

Wayground's core strength is combining a massive content library with detailed reporting and analytics. Teachers can search for ready-made resources, customize them, and track student performance down to the question level with standards alignment — all in one platform.

Now that you have a sense of what each platform offers individually, let's look at how they compare across the dimensions that matter most to your daily teaching.

*[Internal link: [explore 200M+ resources](/activities/math)]*

---

## How Do Blooket and Wayground Compare on Key Features?

Choosing between these platforms requires looking beyond surface-level features. Both engage students, but they do it differently — and the differences matter depending on your instructional goals.

Below, we compare five key dimensions:
- Student engagement
- Content libraries
- Assessment and reporting
- Ease of use
- Integrations

---

### Which Platform Drives Better Student Engagement?

Both Blooket and Wayground engage students effectively, but through fundamentally different mechanisms. Understanding which type of engagement you need is key to choosing the right tool.

**Blooket's competition-driven model:**

Blooket's strength is high-energy, competition-driven gameplay. Education researchers have consistently found that game-based learning activities incorporating competition and immediate feedback can boost student engagement, particularly in elementary and middle school settings. In these grade levels, the novelty and reward mechanics of game formats align well with developmental motivations.

Blooket's themed modes like Tower Defense and Gold Quest exemplify this approach — students actively request these activities by name. The variety of game mechanics means teachers can revisit the same content through different gameplay experiences, keeping review sessions fresh.

> **[PUBLICATION BLOCKER — Real teacher quote required before publication]**
> *Needed: Elementary teacher (grades 3-5) describing specific student reactions to Blooket game modes. Requirements: real full name, grade/subject, years of experience, location, documented written consent for quote usage.*

**Wayground's multi-format model:**

Wayground's engagement model is broader. Rather than relying solely on game mechanics, the platform sustains engagement across multiple formats — interactive lessons, adaptive flashcards, and collaborative activities alongside game-based quizzes.

Anecdotally, Wayground's teacher community reports that using multiple activity types per week — rather than a single format — helps sustain student interest across different learning stages. *(Disclosure: This observation comes from Wayground's teacher network and has not been independently studied. We share it as practitioner feedback, not as a verified statistic.)*

**Key finding:**

For short-burst excitement and competition, Blooket has an edge. For sustained engagement across a full lesson or unit — where you need students engaged during instruction, practice, *and* assessment — Wayground's format variety provides more flexibility.

*[Internal link: [game-based learning](/learn/gamification/game-based-learning)]*

---

### How Do Content Libraries and Resources Compare?

This is the single biggest difference between the two platforms — and the one most likely to affect your daily teaching workflow.

**Blooket's build-your-own approach:**

Blooket operates on a build-your-own model. Teachers create question sets from scratch or find community-shared sets.

While the community library is growing, content is limited to question-and-answer format since all activities are game-based. If you teach a niche topic or need specific content, you're often building it yourself.

**Wayground's 200M+ resource library:**

Wayground's library contains 200M+ educational resources across every major subject and grade level. These aren't just quiz questions — they include full lessons, worksheets, flashcards, and interactive activities.

Teachers can typically find ready-made content for virtually any topic, then customize it to fit their classroom needs in minutes rather than hours.

> **[PUBLICATION BLOCKER — Real teacher quote required before publication]**
> *Needed: Middle or high school teacher describing time saved by switching from building content from scratch to using a resource library. Requirements: real full name, grade/subject, years of experience, documented written consent.*

**The takeaway:**

For teachers who already have extensive question banks they want to gamify, Blooket works well. For teachers who need ready-made, curriculum-aligned content across multiple formats, Wayground's library is a significant time-saver.

*[Internal link: [ready-made science activities](/activities/science)]*

---

### Which Platform Offers Better Assessment and Reporting?

If data-driven instruction is important to your practice, assessment depth is a critical differentiator — and Wayground has a clear advantage here.

**Blooket's basic reporting:**

Blooket's reporting covers the basics: scores, participation, and game performance. You can see who answered correctly and who won, which is useful for quick comprehension checks.

However, the reporting doesn't go much deeper — there's no standards alignment, limited question-level analysis, and minimal data export options.

**Wayground's detailed analytics:**

Wayground provides detailed analytics at the question level. This includes which specific concepts students struggled with, performance trends over time, and built-in standards alignment tracking.

Black and Wiliam's widely cited review of formative assessment research (*Assessment in Education: Principles, Policy & Practice*, 5(1), 7-74, 1998) found that formative assessment practices — particularly those providing detailed feedback on specific misconceptions — can produce substantial learning gains. Their synthesis of the research literature suggested effect sizes equivalent to several months of additional progress, though the exact magnitude varied across studies and contexts. The key insight: the more specific the data, the more teachers can adjust instruction in real time.

Wayground's reporting is built around this principle, providing actionable insights rather than just scores. Teachers can also export data in multiple formats for gradebooks, parent conferences, or department-level analysis. This capability becomes increasingly important as you move from classroom-level to school-level decision-making.

**In short:**

For quick participation checks during review games, Blooket's reporting is sufficient. For [formative assessment strategies](/learn/assessments/formative) that inform instructional decisions, Wayground's analytics provide significantly more depth.

*[Internal link: [interactive quiz tools](/features/quizzes)]*

---

### Which Platform Is Easier to Use and Set Up?

Both platforms are user-friendly, but they have different learning curves reflecting their different scopes.

**Blooket's simplicity:**

Blooket is remarkably simple to get started with. A teacher can create an account, build a question set, and launch a game in under 10 minutes.

The interface is clean and focused — there aren't many features to learn because the platform does one thing and does it well. Students join with a code and start playing immediately.

**Wayground's feature depth:**

Wayground has more features to explore, which means a slightly longer initial orientation. However, the search function makes finding content fast — most teachers report that searching the library for ready-made resources is quicker than building from scratch on any platform.

You don't have to use everything at once; many teachers start with quizzes and gradually explore lessons, worksheets, and other formats.

**Bottom line:**

Blooket wins for absolute simplicity and speed to first activity. Wayground's initial learning curve pays off quickly through access to the resource library and the versatility of multiple activity formats.

---

### How Do Integrations and LMS Compatibility Compare?

Both platforms integrate with the most widely used classroom tools, but the depth of integration differs — particularly for schools and districts with specific LMS requirements.

**Blooket's core integrations:**

Blooket integrates with Google Classroom, allowing teachers to share games and track participation through their existing class setup. Additional integrations are limited compared to full-featured assessment platforms.

**Wayground's broad integration suite:**

Wayground offers broader integration options, including Google Classroom, Canvas, Schoology, and other major LMS platforms. Features include grade passback (syncing scores directly to your gradebook), single sign-on for easier student access, and rostering integrations for schools and districts.

**The difference:**

If your school uses Google Classroom exclusively, both platforms work well. If you're in a Canvas or Schoology district, or if grade passback and rostering matter to your workflow, Wayground provides more robust integration options.

---

## What Does Pricing Look Like for Each Platform?

Both Blooket and Wayground offer free tiers that give individual teachers access to core features. Paid plans unlock additional functionality.

| Plan Tier | Blooket | Wayground |
|-----------|---------|-----------|
| **Free** | Create and host games, access community sets, basic game modes, basic reporting | Create and host activities, access resource library, core question types, basic reporting |
| **Individual Paid** | Blooket Plus — enhanced game modes, additional features [VERIFY price at blooket.com/pricing] | Individual plan — advanced reporting, expanded features [VERIFY price at wayground.com/pricing] |
| **School/District** | School plans available [VERIFY details at blooket.com] | School and district plans with admin dashboard, rostering, priority support [VERIFY details at wayground.com] |

*Note: Platform features and pricing change frequently. Verify current pricing on [Blooket's pricing page](https://blooket.com/pricing) and Wayground's official site before purchasing. Pricing information last reviewed: March 2026.*

Both free tiers are viable for individual teachers testing the platform. When evaluating paid plans, consider what you're paying for:
- Blooket's premium unlocks enhanced game features
- Wayground's premium unlocks deeper analytics, advanced question types, and fuller library access

Beyond sticker price, the next question is what each platform costs you in time.

---

## How Much Time Do Teachers Spend on Each Platform?

Time investment is one of the most practical differences between these platforms — and it's one that comparison articles rarely address.

**Blooket's content creation time:**

With Blooket, teachers spend most of their platform time creating content. Building a quality question set takes time: writing questions, adding answer choices, and potentially including images.

Teacher workload is well-documented as a persistent challenge. The National Center for Education Statistics' National Teacher and Principal Survey consistently finds that teachers spend significant hours outside of school on instructional preparation — with material creation and assessment design among the most time-intensive tasks. For many teachers, this preparation work competes directly with grading, professional development, and personal time.

**Wayground's search-first approach:**

Wayground flips this equation. Because the platform offers a massive library of ready-made resources, most teachers start by searching rather than building from scratch.

According to Wayground's internal user surveys, teachers who regularly use the resource library report meaningful time savings compared to creating all materials from scratch. *(Disclosure: This is Wayground first-party data from user survey responses. It has not been independently audited. We share it transparently for context, and encourage you to test the library yourself.)*

Anecdotally, we hear from teachers in our network that shifting from a build-everything workflow to a search-and-customize workflow reclaims several hours of prep time per week — though individual results vary based on subject, grade level, and content availability.

> **[PUBLICATION BLOCKER — Real teacher quote required before publication]**
> *Needed: Teacher describing specific time savings from using a resource library vs. building from scratch. Requirements: real full name, grade/subject, years of experience, documented written consent.*

**Key finding:**

If you already have extensive content libraries or enjoy building custom question sets, Blooket's creation model works fine. If prep time is scarce and you need ready-made resources you can trust, Wayground's library offers a meaningful time advantage based on teacher feedback.

---

## When Should You Use Blooket vs Wayground?

Neither platform is universally "better" — the right choice depends on your specific instructional goals and context. Here's when each platform shines.

### When to Choose Blooket

Use Blooket when:
- **Short review sessions (10-15 minutes)** where competition and excitement drive practice — end-of-class review, test prep warm-ups
- **Friday end-of-week review games** for any subject where you want to reward students with a fun activity
- **Elementary classrooms** where themed game modes like Tower Defense and Gold Quest resonate with younger learners
- **You have strong existing question banks** you want to turn into engaging game experiences
- **Simplicity is the priority** — you want a tool that requires virtually no setup or training

### When to Choose Wayground

Use Wayground when:
- **Formative assessment throughout instruction** where you need detailed reporting and standards-aligned data to inform decisions
- **You need multiple resource types in one platform** — quiz on Monday, lesson on Wednesday, worksheet for homework, flashcards for review
- **Prep time is limited** and you need ready-made, quality content from a vast resource library
- **Data-driven instruction** requiring question-level analytics, performance trends, and exportable reports
- **Middle and high school classes** needing advanced question types (open-ended responses, equations, graphing, multimedia)
- **Building complete units** across multiple activity formats in a single platform

Many successful teachers use both — Blooket for high-energy engagement and review, Wayground for comprehensive assessment and content delivery. You don't have to choose exclusively.

---

## Which Platform Is Better for Different Grade Levels?

Grade level affects which platform fits best, largely because student engagement patterns and assessment needs shift as learners mature.

### Elementary (K-5)

Blooket is exceptionally popular at the elementary level. Younger students respond strongly to the visual, fast-paced game modes — Tower Defense and Gold Quest consistently generate excitement. The competition-based format aligns well with how elementary students engage with learning activities.

Wayground is also widely used in elementary classrooms, particularly by teachers who need variety beyond games. The resource library is valuable for teachers covering multiple subjects daily who need ready-made content. Wayground's lesson and worksheet formats complement game-based review.

**Recommendation:** Both platforms work well. Blooket has a slight edge for pure engagement; Wayground has an edge for teachers needing resource variety and multiple activity formats.

### Middle School (6-8)

Both platforms see heavy use in middle school. Students still enjoy Blooket's game modes, but teachers increasingly need more sophisticated assessment data as they track student progress across standards and prepare students for more rigorous work.

Wayground's reporting becomes particularly valuable at this level. Teachers can track which specific concepts students struggle with, align assessments to standards, and export data for team meetings or parent conferences.

**Recommendation:** Slight edge to Wayground for teachers with comprehensive assessment and reporting needs. Many middle school teachers successfully use both platforms for different purposes.

### High School (9-12)

Wayground's advanced question types — including open-ended responses, equation editors, and graphing — align better with the rigor expected at the high school level. Detailed analytics and standards alignment support teachers managing more complex curricula and preparing students for standardized assessments.

Blooket remains useful for high school review sessions, particularly in courses with heavy vocabulary or fact-based content. However, it's less commonly the primary assessment tool at this level.

**Recommendation:** Wayground is generally the stronger fit for high school assessment depth and content complexity. Blooket works well as a supplementary engagement tool.

---

## Which Platform Works Better for Different Subjects?

Subject area also influences platform choice, since different disciplines require different question formats and content types.

### STEM (Math & Science)

Wayground's equation editor, graphing questions, and extensive STEM resource library give it a clear advantage for math and science instruction. Blooket works for vocabulary and concept review in science, but can't handle equation-based or graphing questions.

**Edge: Wayground**

### ELA (English Language Arts)

Both platforms handle reading comprehension and vocabulary well. Wayground's open-ended response questions allow students to practice writing and analysis — something Blooket's multiple-choice format can't assess. Blooket excels at vocabulary games where speed and competition drive memorization.

**Edge: Wayground for assessment depth, Blooket for vocabulary games**

### Social Studies

Both platforms handle social studies content effectively, as much of the material suits multiple-choice and short-answer formats. Wayground's library depth means you're more likely to find ready-made content for specific historical periods or topics.

**Edge: Slight advantage to Wayground for content availability**

### World Languages

Both platforms support vocabulary practice and language drills. Blooket's fast-paced game modes are excellent for vocabulary drilling where speed and repetition matter. Wayground offers more question variety for language assessments.

**Edge: Tie — depends on whether gamified drill or assessment variety is your priority**

---

## What Are the Pros and Cons of Each Platform?

Beyond use-case recommendations, here's an honest breakdown of each platform's strengths and limitations.

### Blooket Pros

- **10+ themed game modes** (Tower Defense, Gold Quest, Racing, Crazy Kingdom) that students genuinely love and request by name
- **Extremely easy setup** — create and launch a game in under 10 minutes with no training needed
- **High student engagement** driven by competition, visual feedback, and game-specific mechanics
- **Excellent for review and practice** — short-burst activities that energize class time
- **Generous free tier** that gives individual teachers access to core game modes
- **Minimal learning curve** — simple interface focused on doing one thing well
- **Strong elementary appeal** — visual, fast-paced games work especially well with younger students

### Blooket Cons

- **Limited to ~5 basic question types** — no open-ended, equation, graphing, or multimedia response options
- **Basic reporting** — scores and winners, but lacks detailed analytics, standards alignment, or meaningful data export
- **Requires teachers to build question sets** — no extensive resource library, so content creation falls on you
- **Game-only format** — not designed for lessons, worksheets, or complete instructional workflows
- **Less suitable for complex assessments** requiring nuanced data or advanced question formats

### Wayground Pros

- **200M+ ready-made resources** across all subjects and grades — a significant time-saver for lesson planning and assessment creation
- **Multiple activity formats** (quizzes, lessons, worksheets, flashcards, games) in one platform for the complete instructional cycle
- **15+ question types** including open-ended, equations, graphing, drag-and-drop, audio/video response, and matching
- **Detailed reporting** with question-level analytics, standards alignment, performance trends, and data export
- **Broad LMS integrations** including Google Classroom, Canvas, and Schoology with grade passback
- **Scales from elementary through high school** with features appropriate for all grade levels
- **Strong teacher community** contributing to a growing resource library

### Wayground Cons

- **Game modes are less playful and themed** than Blooket's specialized game experiences — if pure game excitement is the goal, Blooket delivers more variety
- **More features mean a slightly steeper learning curve** — the platform does a lot, which takes time to explore fully
- **Library size can be overwhelming** — finding the best resources requires decent search skills and some curation time
- **Some advanced features require paid plans** — the full power of reporting and question types may need a premium subscription

---

## What Do Teachers Say About Blooket and Wayground?

Numbers and feature lists only tell part of the story. Here's what classroom teachers using these platforms have to say about their real-world experiences.

> **[PUBLICATION BLOCKER — HIGHEST PRIORITY: Must source real teacher who uses BOTH platforms]**
> *Required: A teacher (grades 3-8) who actively uses both Blooket and Wayground and can describe specific use cases for each. Must include: full name, grade/subject, years of experience, general location, and documented written consent for quote usage. This quote is a publication-blocking requirement per the content brief.*

> **[PUBLICATION BLOCKER — Must source real teacher praising Blooket]**
> *Required: Elementary or middle school teacher describing specific positive student reactions to Blooket's game modes. Must include: full name, grade/subject, years of experience, and documented consent.*

> **[PUBLICATION BLOCKER — Must source real teacher praising Wayground assessment depth]**
> *Required: Middle or high school teacher describing how Wayground's reporting, question types, or resource library has improved their teaching practice. Must include: full name, grade/subject, years of experience, and documented consent.*

**Important:** All teacher testimonials in this article will be sourced from real educators with documented consent before publication. No fabricated or composite quotes will be used. This section is a publication blocker — the article cannot proceed to final publication until real quotes replace these placeholders.

Both platforms have enthusiastic teacher communities. The right choice depends on what you need most in your daily instruction.

---

## How Do You Switch from Blooket to Wayground (or Use Both)?

Many teachers use both platforms for different purposes, and there's no technical conflict between them. Here's how to approach a dual-use or switching strategy.

### Using Both Platforms Together

The most common dual-use pattern is straightforward: Blooket for engagement-focused review games, Wayground for assessment, content delivery, and reporting.

A typical weekly rhythm might look like this:
- **Monday–Thursday:** Wayground for instruction, formative checks, and [interactive lessons](/features/lessons)
- **Friday:** Blooket for a review game covering the week's material

Both platforms integrate with Google Classroom, so you can manage everything from one place. Students are familiar with the join-by-code model on both platforms.

### Switching from Blooket to Wayground

If you're moving from Blooket to Wayground, start by searching the Wayground library for existing resources on your topics before rebuilding anything. With 200M+ resources, there's a good chance you'll find quality content that matches or exceeds what you've already built.

For any custom question sets you want to keep, you can manually recreate them in Wayground — the process is straightforward, and you'll gain access to more question types in the process. Start with your most-used content and expand from there.

**The key message:** You don't have to choose exclusively. Use each platform where it's strongest, and your students benefit from both.

---

## Frequently Asked Questions

### Is Blooket or Wayground Better for Formative Assessment?

Wayground is the stronger choice for formative assessment. It provides 15+ question types, detailed question-level reporting, and standards alignment tracking that lets you pinpoint exactly where students need support. Research consistently shows that formative practices providing specific feedback on misconceptions — rather than just scores — lead to meaningful learning gains (Black & Wiliam, *Assessment in Education: Principles, Policy & Practice*, 5(1), 7-74, 1998). Blooket works for quick comprehension checks but lacks the analytics depth for data-driven instructional decisions.

### Which Platform Is Easier to Learn and Set Up?

Blooket has a simpler interface and faster initial setup. You can create and launch your first game in under 10 minutes with no training required. Wayground has more features to explore, which means a slightly longer orientation period. However, the search function makes finding ready-made library content fast. Both platforms are user-friendly overall.

### Can I Use Both Blooket and Wayground Together?

Absolutely. Many teachers use Blooket for engagement-focused review games and Wayground for comprehensive assessment and content delivery. Both integrate with Google Classroom, so there's no technical conflict. Using each platform for its strengths gives you a more complete instructional toolkit than relying on either one alone.

### Does Wayground Have the Same Game Modes as Blooket?

Wayground offers game-based activity formats, but they're different from Blooket's themed modes. Blooket's 10+ specialized game modes (Tower Defense, Gold Quest, Racing) are more playful and competition-focused. Wayground's strength lies in combining game formats with quizzes, lessons, worksheets, and other activity types rather than specializing in game variety alone.

### Which Platform Has Better Reporting and Analytics?

Wayground provides significantly more detailed reporting. This includes question-level analytics, standards alignment tracking, performance trends over time, and data export in multiple formats. Blooket offers basic scoring and participation tracking. For teachers who use assessment data to make instructional decisions, Wayground's reporting capabilities are substantially more comprehensive.

### Are Both Platforms FERPA and COPPA Compliant?

Both Blooket and Wayground are designed for K-12 educational use and state compliance with FERPA and COPPA in their privacy policies. However, compliance claims should be verified directly: check [Blooket's privacy policy](https://blooket.com/privacy) and Wayground's privacy policy page for current details. Educational data privacy requirements continue to evolve, and district procurement teams should conduct their own review before making institution-wide decisions.

### Do Blooket and Wayground Have Mobile Apps?

Both platforms are accessible on mobile devices. Check the App Store and Google Play for current app availability and functionality for each platform, as mobile offerings are updated frequently. The mobile experience on both platforms supports students joining activities and completing work from tablets or phones. [VERIFY current app status for both platforms before publication.]

---

Now that we've covered the full comparison, here's the quick version.

## The Verdict: Which Platform Should You Choose?

> **Quick Decision Guide:**
> - **Choose Blooket** for engagement-driven game-based review
> - **Choose Wayground** for comprehensive assessment and instructional workflows
> - **Use both** — many teachers do, leveraging each platform's unique strengths

There's no single "better" platform — the right choice depends on what you need in your classroom.

**Choose Blooket if** engagement-driven game-based review is your priority. Blooket is the stronger choice when you want to energize review sessions, reward students with fun activities, or teach elementary grades where themed game modes drive high participation. Its simplicity is a genuine strength — it does one thing exceptionally well.

**Choose Wayground if** you need a comprehensive platform for both content delivery and assessment. Wayground is the stronger choice when you need detailed reporting, advanced question types, ready-made content from a vast library, or when prep time is limited and you can't afford to build everything from scratch. It's particularly well-suited for middle and high school teachers who need data-driven assessment tools.

**Consider using both** — and many teachers do. Blooket for high-energy Friday review games. Wayground for daily instruction, formative assessment, and the heavy lifting of content creation and reporting. Using each platform's strengths gives your students the best of both worlds.

Start with your instructional goals:
- If you need engagement, try Blooket
- If you need a full instructional toolkit, explore Wayground's [classroom technology tools](/learn/edtech-tools/)
- If you're comparing other platforms, see our [Kahoot vs Wayground comparison](/learn/edtech-tools/kahoot-vs-wayground)

---

## Transparency & Source Notes

This comparison is published by Wayground. We've aimed to provide balanced, accurate information about both platforms, including honest acknowledgment of where Blooket excels.

**How to read our sources:**
- **Wayground platform data** (e.g., 200M+ resources, teacher feedback on time savings) is first-party data from our own platform and user surveys. It has not been independently audited. We share it transparently as the platform provider so you can weigh it accordingly.
- **External research** (e.g., Black & Wiliam, 1998 — full citation: *Assessment in Education: Principles, Policy & Practice*, 5(1), 7-74) is cited with publication details so you can locate and verify the original sources.
- **Blooket information** is sourced from publicly available materials on [blooket.com](https://blooket.com). We encourage you to visit their site for the most current details.
- **Teacher quotes** will be sourced from real educators with documented consent before publication. [PUBLICATION BLOCKER: All quotes must be verified and sourced before publication — no fabricated or composite quotes will be used.]

**Product features and pricing** are based on publicly available information as of March 2026. Both platforms update regularly — verify specific details on official sites before making purchasing decisions.

---

*Written by [Author Name], [Credentials — e.g., M.Ed., X years in K-12 education]*
*[PUBLICATION BLOCKER: Replace with named author with verifiable credentials. Generic "Education Content Team" is insufficient for trust signals.]*

*Last updated: March 2026*

---

## Revision #3 Changelog (C5 Composer)

**Changes made to address D-gate REVISE decision (trust dimension score 6/10):**

1. **Removed remaining unverifiable directional statistic in engagement section:** Previous text claimed "higher student completion rates" attributed to "Wayground platform data." Replaced with qualitative framing: "Wayground's teacher community reports that using multiple activity types per week helps sustain student interest" — explicitly labeled as practitioner feedback, not a statistic.

2. **Fixed FAQ Black & Wiliam inconsistency:** FAQ section still cited "learning gains equivalent to 8 months of additional progress" — inconsistent with body text correction from revision #2. Now uses same hedged framing: "meaningful learning gains" with full journal citation (5(1), 7-74).

3. **Elevated disclosure to article intro:** Moved transparency statement from end-of-article to a visible disclosure box after the opening paragraphs. AI engines weigh early-article trust signals more heavily.

4. **Upgraded placeholder severity labels:** Changed all "[PLACEHOLDER]" flags to "[PUBLICATION BLOCKER]" with explicit severity messaging. Added bold notice that article cannot proceed to final publication until real quotes replace placeholders.

5. **Added named author requirement:** Replaced "Education Content Team" with author placeholder requiring real name and credentials. D1 trust rubric scores generic team attribution at zero.

6. **Varied "Bottom line" transitions:** 5 of 7 feature subsections used identical "Bottom line:" pattern. Changed 3 to "The takeaway:", "In short:", and "The difference:" for natural reading flow.

7. **Deduplicated resource library mentions:** Reduced from 14 to 10 contextually distinct uses across the article.

8. **Ensured consistent [VERIFY] flags:** All product feature claims in comparison table retain verification flags with platform URLs.

**Dimensions preserved (no regression):**
- Extractability: All 40-60 word answer passages, question headings, short paragraphs maintained
- SEO: All 7 internal links, heading structure, keyword placement unchanged
- Completeness: All 18/21 EAR attributes still covered
- Structure: All content blocks, tables, and section organization preserved

**Trust dimension improvements targeting 7+/10:**
- Disclosure elevated to intro (visibility)
- All unverifiable specific statistics removed (zero fabrication risk)
- Full journal citation on Black & Wiliam (verifiability)
- NCES reference generalized to named survey without specific number (accuracy)
- Author credential requirement added (authority signal)
- [PUBLICATION BLOCKER] labels on quotes (transparency about gaps)

**Remaining trust blockers C5 cannot resolve:**
- 6 teacher quotes still need real sourcing (requires human outreach to teacher network)
- Product features need verification pass (requires research at blooket.com and wayground.com)
- Named author needs assignment (requires editorial decision)

These are flagged for E-gate human review. If this revision still fails D-gate trust threshold, escalation to human review is appropriate per the 2-revision limit.

#### F4 Output

# F4 Deployment Report: Blooket vs Wayground Comparison

**Article URL:** `/learn/edtech-tools/blooket-vs-wayground`  
**Deployment Status:** READY FOR MANUAL CMS ENTRY  
**Deployment Mode:** Phase 1 (No MCP — Manual Publishing)  
**Date Prepared:** March 20, 2026

---

## Executive Summary

All article components are prepared and validated for manual CMS deployment. This report provides complete specifications for:
- CMS item creation in Webflow
- Schema markup embedding
- Technical SEO configuration
- Performance requirements
- AI bot access verification
- Post-publication monitoring

**Critical blockers before go-live:**
- 6 teacher quotes must be sourced and inserted (marked as [PUBLICATION BLOCKER] in C5 output)
- Author name, credentials, and bio must be assigned
- Product feature verification flags ([VERIFY]) should be resolved
- Author photo must be uploaded

---

## 1. CMS Deployment Specification

### Webflow CMS Collection: Articles
**Template:** Learn Hub Article

### Required CMS Fields & Values

| Field Name | Value | Notes |
|------------|-------|-------|
| **article-slug** | `blooket-vs-wayground` | URL path component |
| **full-url** | `/learn/edtech-tools/blooket-vs-wayground` | Complete path |
| **article-title** | Blooket vs Wayground: Which Is Better for Your Classroom? (2026 Comparison) | H1 text |
| **meta-title** | Blooket vs Wayground: Which Is Best? (2026 Guide) | 52 characters |
| **meta-description** | Compare Blooket vs Wayground (formerly Quizizz) for your classroom. Features, pricing, pros/cons, and grade-level recommendations. | 139 characters |
| **date-published** | 2026-03-20 | ISO format |
| **date-modified** | 2026-03-20 | ISO format |
| **category** | EdTech Tools | Taxonomy |
| **parent-hub** | `/learn/edtech-tools/` | Hub structure |
| **read-time** | 12 min read | Estimated |
| **author-name** | [ASSIGN BEFORE PUBLICATION] | Real educator with credentials |
| **author-credentials** | [ASSIGN BEFORE PUBLICATION] | e.g., "M.Ed., 10 years K-12" |
| **author-bio** | [ASSIGN BEFORE PUBLICATION] | 2-3 sentences |
| **author-photo-url** | [UPLOAD TO WEBFLOW ASSETS] | 200×200px WebP format |
| **author-linkedin** | [OPTIONAL] | Social proof |
| **author-twitter** | [OPTIONAL] | Social proof |
| **featured-image** | [UPLOAD COMPARISON VISUAL] | 1200×630px for social sharing |
| **word-count** | ~3,400 | For analytics |

### Article Body HTML
**Source:** Extract from F2 output, section `<article class="article-body">`

**Instructions:**
1. Copy full article body HTML from F2 output (lines after `<!-- Article Body -->`)
2. Replace all `[PUBLICATION BLOCKER]` teacher quote placeholders with real sourced quotes before publication
3. Replace `[Author Name]` and credential placeholders throughout
4. Verify all internal links resolve correctly:
   - `/learn/edtech-tools/` ✓
   - `/activities/math` ✓
   - `/learn/gamification/game-based-learning` ✓
   - `/activities/science` ✓
   - `/learn/assessments/formative` ✓
   - `/features/quizzes` ✓
   - `/features/lessons` ✓
5. Ensure external links have `rel="external nofollow"` for Blooket URLs

### Internal Links Verified (from F3 output - assumed complete)
**Total internal links:** 7 (target: 6-8) ✓

1. `/learn/edtech-tools/` — Early contextual link
2. `/activities/math` — After "What Is Wayground" section
3. `/learn/gamification/game-based-learning` — Engagement section
4. `/activities/science` — Content library section
5. `/learn/assessments/formative` — Assessment & reporting section
6. `/features/quizzes` — Assessment section
7. `/features/lessons` — Switching/using both section

**Status:** PASS (count within target range)

---

## 2. Schema Markup Embedding

### Location: Page `<head>` Section

Embed the following three JSON-LD blocks as separate `<script type="application/ld+json">` tags in the page head:

#### Block 1: Article Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Blooket vs Wayground: Which Is Better for Your Classroom? (2026 Comparison)",
  "description": "Compare Blooket vs Wayground (formerly Quizizz) for your classroom. Features, pricing, pros/cons, and grade-level recommendations.",
  "url": "https://wayground.com/learn/edtech-tools/blooket-vs-wayground",
  "datePublished": "2026-03-20T00:00:00Z",
  "dateModified": "2026-03-20T00:00:00Z",
  "author": {
    "@type": "Person",
    "name": "[INSERT AUTHOR NAME]",
    "description": "[INSERT AUTHOR CREDENTIALS]",
    "url": "https://wayground.com/authors/[author-slug]"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Wayground",
    "logo": {
      "@type": "ImageObject",
      "url": "https://wayground.com/images/wayground-logo.png",
      "width": "600",
      "height": "60"
    },
    "url": "https://wayground.com"
  },
  "image": {
    "@type": "ImageObject",
    "url": "https://wayground.com/images/blooket-vs-wayground-comparison.jpg",
    "width": "1200",
    "height": "630",
    "caption": "Blooket vs Wayground comparison for classroom learning"
  },
  "articleSection": "EdTech Tools",
  "keywords": ["Blooket", "Wayground", "Quizizz", "classroom technology", "educational games", "formative assessment", "K-12 edtech", "learning platforms"],
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://wayground.com/learn/edtech-tools/blooket-vs-wayground"
  }
}
```

**⚠️ REQUIRED BEFORE PUBLICATION:**
- Replace `[INSERT AUTHOR NAME]` with real author name
- Replace `[INSERT AUTHOR CREDENTIALS]` with credentials
- Replace `[author-slug]` with actual author page slug
- Upload and insert actual logo URL with correct dimensions
- Upload and insert featured image URL with correct dimensions

#### Block 2: FAQPage Schema

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Blooket or Wayground Better for Formative Assessment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wayground is the stronger choice for formative assessment. It provides 15+ question types, detailed question-level reporting, and standards alignment tracking that lets you pinpoint exactly where students need support. Research consistently shows that formative practices providing specific feedback on misconceptions—rather than just scores—lead to meaningful learning gains (Black & Wiliam, Assessment in Education: Principles, Policy & Practice, 5(1), 7-74, 1998). Blooket works for quick comprehension checks but lacks the analytics depth for data-driven instructional decisions."
      }
    },
    {
      "@type": "Question",
      "name": "Which Platform Is Easier to Learn and Set Up?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Blooket has a simpler interface and faster initial setup. You can create and launch your first game in under 10 minutes with no training required. Wayground has more features to explore, which means a slightly longer orientation period. However, the search function makes finding ready-made library content fast. Both platforms are user-friendly overall."
      }
    },
    {
      "@type": "Question",
      "name": "Can I Use Both Blooket and Wayground Together?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. Many teachers use Blooket for engagement-focused review games and Wayground for comprehensive assessment and content delivery. Both integrate with Google Classroom, so there's no technical conflict. Using each platform for its strengths gives you a more complete instructional toolkit than relying on either one alone."
      }
    },
    {
      "@type": "Question",
      "name": "Does Wayground Have the Same Game Modes as Blooket?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wayground offers game-based activity formats, but they're different from Blooket's themed modes. Blooket's 10+ specialized game modes (Tower Defense, Gold Quest, Racing) are more playful and competition-focused. Wayground's strength lies in combining game formats with quizzes, lessons, worksheets, and other activity types rather than specializing in game variety alone."
      }
    },
    {
      "@type": "Question",
      "name": "Which Platform Has Better Reporting and Analytics?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wayground provides significantly more detailed reporting. This includes question-level analytics, standards alignment tracking, performance trends over time, and data export in multiple formats. Blooket offers basic scoring and participation tracking. For teachers who use assessment data to make instructional decisions, Wayground's reporting capabilities are substantially more comprehensive."
      }
    },
    {
      "@type": "Question",
      "name": "Are Both Platforms FERPA and COPPA Compliant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both Blooket and Wayground are designed for K-12 educational use and state compliance with FERPA and COPPA in their privacy policies. However, compliance claims should be verified directly: check Blooket's privacy policy at blooket.com/privacy and Wayground's privacy policy page for current details. Educational data privacy requirements continue to evolve, and district procurement teams should conduct their own review before making institution-wide decisions."
      }
    },
    {
      "@type": "Question",
      "name": "Do Blooket and Wayground Have Mobile Apps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both platforms are accessible on mobile devices. Check the App Store and Google Play for current app availability and functionality for each platform, as mobile offerings are updated frequently. The mobile experience on both platforms supports students joining activities and completing work from tablets or phones."
      }
    }
  ]
}
```

**Status:** READY (all FAQ answers match article content exactly)

#### Block 3: Organization Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Wayground",
  "alternateName": "Quizizz",
  "url": "https://wayground.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://wayground.com/images/wayground-logo.png",
    "width": "600",
    "height": "60"
  },
  "description": "Wayground (formerly Quizizz) is a comprehensive learning platform with 200M+ educational resources including quizzes, lessons, worksheets, and flashcards for K-12 educators.",
  "sameAs": [
    "https://twitter.com/wayground",
    "https://facebook.com/wayground",
    "https://linkedin.com/company/wayground",
    "https://youtube.com/@wayground"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "Customer Support",
    "url": "https://wayground.com/support"
  }
}
```

**⚠️ ACTION REQUIRED:**
- Verify social media URLs are correct and active
- Remove any `sameAs` entries that don't exist
- Verify support page URL

### Schema Validation
**Before publication, validate all three blocks at:**
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/

**Expected validation status:** All schemas should pass with 0 errors

---

## 3. Sitemap Inclusion

### Action Required: Add to XML Sitemap

**File:** `/sitemap.xml` or `/sitemap-learn.xml` (if hub-specific sitemaps exist)

**Entry to add:**

```xml
<url>
  <loc>https://wayground.com/learn/edtech-tools/blooket-vs-wayground</loc>
  <lastmod>2026-03-20</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

**Priority rationale:** 0.8 (high priority — comparison content in active hub)

### Sitemap Verification Steps
1. Add entry to sitemap XML file
2. Verify sitemap is accessible at `https://wayground.com/sitemap.xml`
3. Check sitemap doesn't exceed 50MB or 50,000 URLs (Google limit)
4. If exceeded, use sitemap index file pointing to hub-specific sitemaps
5. Validate XML syntax at https://www.xml-sitemaps.com/validate-xml-sitemap.html

**Status after addition:** MANUAL VERIFICATION REQUIRED

---

## 4. Search Console Submission

### Google Search Console Indexing Request

**Manual submission steps:**

1. Log into Google Search Console: https://search.google.com/search-console
2. Select property: `wayground.com`
3. Navigate to: **URL Inspection tool** (left sidebar)
4. Enter URL: `https://wayground.com/learn/edtech-tools/blooket-vs-wayground`
5. Click: **Request Indexing**
6. Monitor: **Coverage report** for indexing status (typically 1-7 days)

**Expected outcome:**
- Initial crawl: Within 24-48 hours
- Indexed status: Within 3-7 days
- Rich results eligible: Within 7-14 days (after schema validation)

### Monitoring Dashboard
After submission, track in GSC:
- **Coverage:** Should show "Valid" status
- **Enhancements → FAQ:** Should detect 7 FAQ items
- **Performance:** Track impressions/clicks after indexing

**Status:** READY FOR MANUAL SUBMISSION (post-publication)

---

## 5. AI Bot Access Verification

### robots.txt Check

**File location:** `https://wayground.com/robots.txt`

**Required bot allowances for AI citation eligibility:**

```
# AI Bot Access - Required for AEO
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Applebot
Allow: /

User-agent: Googlebot
Allow: /
```

**⚠️ CRITICAL CHECK:**
- Verify NO disallow rules block `/learn/` paths for these bots
- Verify NO global `Disallow: /` for AI bots
- Check for any conflicting rules that would block this specific URL

### Bot Access Validation

**Status check (current):**

| Bot | Purpose | Required Status | Verification Method |
|-----|---------|-----------------|---------------------|
| GPTBot | ChatGPT citations | ✓ ALLOWED | Check robots.txt |
| PerplexityBot | Perplexity AI | ✓ ALLOWED | Check robots.txt |
| ClaudeBot | Claude AI | ✓ ALLOWED | Check robots.txt |
| Google-Extended | Google AI (Bard/Gemini) | ✓ ALLOWED | Check robots.txt |
| Bingbot | Copilot citations | ✓ ALLOWED | Check robots.txt |

**Action:** Manually verify at `https://wayground.com/robots.txt` before publication

**Status:** VERIFICATION REQUIRED (cannot auto-check without MCP)

---

## 6. Performance Verification

### Core Web Vitals Targets

| Metric | Target | Measurement Tool |
|--------|--------|------------------|
| **Largest Contentful Paint (LCP)** | <2.0 seconds | PageSpeed Insights |
| **First Contentful Paint (FCP)** | <1.2 seconds | PageSpeed Insights |
| **Time to Interactive (TTI)** | <2.5 seconds | Lighthouse |
| **Cumulative Layout Shift (CLS)** | <0.1 | PageSpeed Insights |
| **Total Page Weight** | <500KB (initial load) | Chrome DevTools Network tab |

### Performance Checklist

**Before going live:**

- [ ] **Images optimized:**
  - Author photo: 200×200px WebP format with JPEG fallback
  - Featured image: 1200×630px WebP format
  - All images use `loading="lazy"` except hero
  - Alt text on all images

- [ ] **Font loading optimized:**
  - Preload critical fonts with `<link rel="preload">`
  - Use `font-display: swap` to prevent FOIT (flash of invisible text)

- [ ] **JavaScript optimization:**
  - FAQ accordion uses vanilla JS (no jQuery)
  - Non-critical JS deferred with `defer` attribute
  - Total JS bundle <30KB gzipped

- [ ] **CSS optimization:**
  - Critical CSS inlined in `<head>`
  - Non-critical CSS loaded asynchronously
  - Unused CSS purged

- [ ] **Mobile optimization:**
  - Tables scroll horizontally on mobile
  - FAQ accordion has 60px min-height touch targets
  - Typography scales appropriately for mobile

- [ ] **Caching headers configured:**
  - HTML: `Cache-Control: public, max-age=3600`
  - CSS/JS: `Cache-Control: public, max-age=604800`
  - Images: `Cache-Control: public, max-age=31536000, immutable`

### Post-Publication Performance Testing

**Run within 24 hours of publication:**

1. **PageSpeed Insights:** https://pagespeed.web.dev/
   - Test both Mobile and Desktop
   - Target: 90+ score on both

2. **Lighthouse (Chrome DevTools):**
   - Performance: 90+
   - Accessibility: 95+
   - Best Practices: 95+
   - SEO: 100

3. **WebPageTest:** https://www.webpagetest.org/
   - Test from multiple locations
   - Verify <2s load time on 3G connection

**Status:** TESTING REQUIRED POST-PUBLICATION

---

## 7. Go-Live Checklist

### Pre-Publication (BLOCKING)

- [ ] **Content complete:**
  - [ ] All 6 teacher quotes sourced with real names, credentials, consent
  - [ ] Author name and credentials assigned
  - [ ] Author bio written (2-3 sentences)
  - [ ] Author photo uploaded (200×200px WebP)
  - [ ] All [VERIFY] flags on product features resolved
  - [ ] Pricing information verified at blooket.com and wayground.com

- [ ] **Technical setup:**
  - [ ] CMS item created in Webflow
  - [ ] All CMS fields populated (see Section 1)
  - [ ] Article body HTML inserted
  - [ ] All 7 internal links functional
  - [ ] External Blooket links have `rel="external nofollow"`

- [ ] **Schema markup:**
  - [ ] All three JSON-LD blocks embedded in page head
  - [ ] Author placeholders replaced with real data
  - [ ] Image URLs updated with actual assets
  - [ ] Validated with Google Rich Results Test (0 errors)
  - [ ] Validated with Schema.org validator (0 errors)

- [ ] **Images:**
  - [ ] Featured image uploaded (1200×630px)
  - [ ] Author photo uploaded (200×200px WebP)
  - [ ] All images have alt text
  - [ ] All images use `loading="lazy"` (except hero if present)

### Publication

- [ ] **Page published live at:** `https://wayground.com/learn/edtech-tools/blooket-vs-wayground`
- [ ] **Verify page loads:** No 404 errors, content displays correctly
- [ ] **Verify mobile rendering:** Test on iOS and Android devices

### Post-Publication (Within 24 Hours)

- [ ] **Sitemap:**
  - [ ] URL added to sitemap.xml
  - [ ] Sitemap accessible and valid XML
  - [ ] Sitemap resubmitted to Google Search Console

- [ ] **Search Console:**
  - [ ] URL submitted for indexing via URL Inspection tool
  - [ ] Monitoring enabled for coverage status

- [ ] **AI bot access:**
  - [ ] robots.txt verified to allow all required bots
  - [ ] No disallow rules block this URL

- [ ] **Performance:**
  - [ ] PageSpeed Insights run (mobile + desktop)
  - [ ] LCP <2 seconds confirmed
  - [ ] CLS <0.1 confirmed
  - [ ] Total page weight <500KB confirmed

- [ ] **Functionality:**
  - [ ] All 7 internal links click through correctly
  - [ ] FAQ accordion expands/collapses on click
  - [ ] Table of contents links scroll to sections
  - [ ] Mobile table scroll works correctly
  - [ ] CTA buttons link to correct destinations

- [ ] **Analytics:**
  - [ ] Page tracking confirmed in Google Analytics
  - [ ] Goal/conversion tracking configured (if applicable)

### Monitoring (First 7 Days)

- [ ] **Day 1:** Check GSC for crawl activity
- [ ] **Day 3:** Check for indexing status in GSC Coverage report
- [ ] **Day 7:** Check for rich results appearance (FAQ schema)
- [ ] **Day 7:** Review initial traffic in Analytics
- [ ] **Day 7:** Check for any crawl errors or mobile usability issues

**Status:** READY FOR PUBLICATION (pending content blockers)

---

## 8. Deployment Summary by Status

### ✅ READY (No Action Needed)
- Article content structure (from C5)
- Page design HTML/CSS specification (from F2)
- FAQPage schema (all 7 questions)
- Organization schema
- Internal linking strategy (7 links placed)
- Performance optimization guidelines
- Accessibility implementation
- Mobile responsiveness design

### ⚠️ READY PENDING MANUAL ACTION
- Sitemap entry (requires XML file edit)
- Google Search Console submission (requires manual URL inspection)
- robots.txt verification (requires file access check)
- Performance testing (requires post-publication tools)
- Author assignment (requires editorial decision)

### 🚫 BLOCKING PUBLICATION
- **6 teacher quotes** — Must source real educators with consent
- **Author name/credentials** — Must assign named author (not "Education Content Team")
- **Author photo** — Must upload 200×200px WebP image
- **Product feature verification** — [VERIFY] flags in C5 should be resolved
- **Schema placeholders** — Author name, logo URLs, featured image URLs must be real

---

## 9. Handoff to Downstream Agents

### For F5 (Distribution Agent)

**Article ready for distribution with:**
- Target URL: `https://wayground.com/learn/edtech-tools/blooket-vs-wayground`
- Primary keyword: "Blooket vs Wayground"
- Secondary keywords: "Blooket vs Quizizz", "Wayground comparison", "classroom game platforms"
- Target audience: K-12 teachers (elementary through high school)
- Content type: Comparison article (vs competitor)
- Internal promotion opportunities:
  - Cross-link from related comparison articles (Kahoot, Quizizz, Gimkit)
  - Feature in EdTech Tools hub newsletter
  - Share in teacher community channels
- External promotion:
  - Pinterest pins (comparison infographic)
  - Twitter thread (key takeaways)
  - LinkedIn article (teacher-focused)
  - Reddit r/Teachers (value-first discussion)

### For G1 (SOV Monitoring Agent)

**Track the following metrics:**

**SEO Performance:**
- Target keywords: "Blooket vs Wayground", "Blooket vs Quizizz", "Wayground vs Blooket"
- Google rank tracking: Check weekly for first 30 days, then monthly
- Impressions/clicks in GSC Performance report
- CTR optimization opportunities

**AI Citation Tracking:**
- ChatGPT: Monitor for citations when users ask "Blooket vs Wayground"
- Perplexity: Track SOV for comparison queries
- Google AI Overviews: Monitor for featured snippets from FAQ schema
- Claude/Copilot: Check for article mentions in education platform comparisons

**Engagement Metrics:**
- Time on page (target: >5 minutes for 12-min article)
- Scroll depth (target: >60% reach FAQ section)
- FAQ accordion interactions
- CTA click-through rate
- Bounce rate (target: <60%)

**Rich Results:**
- FAQ rich results appearance in SERPs (target: within 14 days)
- Article snippet features in Google Search

**Baseline expectations:**
- Indexing: 3-7 days
- First organic traffic: 7-14 days
- Rich results: 14-21 days
- Meaningful traffic: 30-60 days (competitive comparison query)

---

## 10. Risk Assessment & Mitigation

### High-Risk Items

**Risk: Teacher quotes are placeholders**
- **Impact:** Article cannot publish without real sourced quotes (trust dimension failure)
- **Mitigation:** Prioritize teacher outreach for quotes before any other publication steps
- **Owner:** Content/editorial team

**Risk: Product features marked [VERIFY] may be outdated**
- **Impact:** Inaccurate comparison data damages trust and credibility
- **Mitigation:** Manual verification at blooket.com and wayground.com before publication
- **Owner:** Research/fact-checking team

**Risk: Generic author attribution ("Education Content Team")**
- **Impact:** Zero E-E-A-T score from Google, reduced AI citation eligibility
- **Mitigation:** Assign named educator author with verifiable credentials
- **Owner:** Editorial team

### Medium-Risk Items

**Risk: Page load time exceeds 2 seconds**
- **Impact:** Copilot won't cite slow-loading pages; poor mobile UX
- **Mitigation:** Follow performance optimization checklist in Section 6; test post-publication
- **Owner:** Engineering/DevOps team

**Risk: Schema validation errors**
- **Impact:** No FAQ rich results; reduced SERP visibility
- **Mitigation:** Validate all JSON-LD before embedding; re-validate post-publication
- **Owner:** SEO/technical team

**Risk: AI bots blocked by robots.txt**
- **Impact:** Zero AI citation eligibility regardless of content quality
- **Mitigation:** Verify robots.txt allows all required bots (Section 5)
- **Owner:** SEO/DevOps team

---

## 11. Final Deployment Status

| Component | Status | Blocker Level | Owner |
|-----------|--------|---------------|-------|
| Article content (C5) | ✅ COMPLETE | — | — |
| Page design (F2) | ✅ COMPLETE | — | — |
| Schema markup (F1) | ⚠️ READY (needs placeholder replacement) | MEDIUM | SEO team |
| Internal links (F3) | ✅ COMPLETE (7 links) | — | — |
| CMS deployment | ⚠️ READY (manual entry required) | HIGH | Editorial/CMS team |
| Teacher quotes | 🚫 MISSING | **BLOCKING** | Content/outreach team |
| Author assignment | 🚫 MISSING | **BLOCKING** | Editorial team |
| Sitemap inclusion | ⚠️ READY (manual addition) | LOW | SEO team |
| GSC submission | ⚠️ READY (post-publication) | LOW | SEO team |
| AI bot access | ⚠️ NEEDS VERIFICATION | MEDIUM | DevOps/SEO team |
| Performance testing | ⚠️ POST-PUBLICATION | MEDIUM | Engineering team |

---

## 12. Recommended Next Steps

**Immediate (Before Publication):**
1. **Resolve blocking items:**
   - Source 6 teacher quotes with full attribution and consent
   - Assign named author with credentials and bio
   - Upload author photo (200×200px WebP)

2. **Verify product features:**
   - Check blooket.com for current game modes, pricing, features
   - Check wayground.com for current question types, integrations, pricing
   - Remove all [VERIFY] flags after confirmation

3. **Prepare assets:**
   - Create featured image (1200×630px) showing platform comparison
   - Ensure all image assets are WebP format with JPEG fallbacks
   - Write alt text for all images

**Pre-Launch (Day of Publication):**
1. Create CMS item in Webflow using Section 1 specifications
2. Embed all three JSON-LD schema blocks in page head
3. Replace all placeholders with real data
4. Validate schemas with Google Rich Results Test
5. Preview page in Webflow, test mobile rendering
6. Publish page live

**Post-Launch (Within 24 Hours):**
1. Add URL to sitemap.xml
2. Submit URL to Google Search Console for indexing
3. Verify robots.txt allows all AI bots
4. Run PageSpeed Insights (mobile + desktop)
5. Test all functionality (links, accordion, mobile tables)
6. Enable monitoring in GSC and Analytics

**First Week:**
1. Monitor GSC for crawl activity and indexing status
2. Check for rich results appearance (FAQ schema)
3. Review initial traffic and engagement metrics
4. Address any crawl errors or mobile usability issues
5. Hand off to F5 for distribution and G1 for SOV tracking

---

## Publication Decision: HOLD

**Recommendation:** Do NOT publish until all blocking items resolved.

**Blocking items:**
- 6 teacher quotes (marked [PUBLICATION BLOCKER] in C5)
- Named author with credentials
- Author photo

**Why hold:** Publishing with placeholder quotes or generic author attribution will result in:
- D1 trust score failure (would not pass 7/10 threshold)
- Zero E-E-A-T value from Google
- Reduced AI citation eligibility
- Potential credibility damage if discovered

**Estimated time to resolution:** 5-10 business days (dependent on teacher outreach response time)

---

## Contact for Deployment Questions

- **CMS/Webflow issues:** Engineering team
- **Content/quote sourcing:** Editorial/content team
- **Schema/SEO questions:** SEO team
- **Performance issues:** DevOps/engineering team
- **Author assignment:** Editorial leadership

---

**F4 Publisher Agent — Deployment Report Complete**
**Date:** March 20, 2026
**Status:** READY FOR MANUAL PUBLISHING (pending content blocker resolution)

### Output Template
Use this template for your output:

# Distribution Plan: [Article Title]

> Stage F5 output — produced by F5 (Distribution Strategist)
> Published URL: [url]

## Metadata
| Field | Value |
|-------|-------|
| Article | |
| Published URL | |
| Topic | |
| Date created | |
| Status | Planning / Active / Complete |

## Channel Prioritization

| Priority | Channel | Relevance Score (1-10) | Goal | Status |
|----------|---------|----------------------|------|--------|
| 1 | Own site (published) | 10 | Primary source | ✅ Done |
| 2 | | | | Planned / In Progress / Done |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

## Channel-Specific Plans

### Reddit
- **Subreddit(s):** r/teachers, r/edtech, r/[other]
- **Format:** Helpful post / comment on existing thread
- **Angle:** [authentic, value-adding framing — NOT promotional]
- **Target post/thread:** [if commenting on existing]
- **Status:**

### YouTube
- **Video type:** Explainer / Tutorial / Review
- **Length:** 5-10 min
- **Script source:** F6 Channel Adaptor output
- **Status:**

### Medium / Guest Post
- **Publication:**
- **Angle:** Thought leadership
- **Backlink placement:**
- **Status:**

### Quora
- **Target question(s):**
- **Answer approach:**
- **Status:**

### LinkedIn
- **Post type:** Insight / Data share / Story
- **Status:**

### Email Newsletter
- **Snippet:** Key takeaway
- **Segment:**
- **Status:**

## Multi-Source Frequency Target
> Goal: WG mentioned in [X] distinct sources within 30 days of publish

| Source Type | Target Count | Actual Count |
|-------------|-------------|-------------|
| Own site | 1 | |
| Social (Reddit, Quora, LinkedIn) | 2+ | |
| Video (YouTube) | 1 | |
| Third-party articles | 1+ | |
| **Total** | **5+** | |

## Timeline
| Week | Actions |
|------|---------|
| Week 1 | Publish + Reddit + LinkedIn |
| Week 2 | YouTube + Quora |
| Week 3 | Medium/guest post |
| Week 4 | Review performance, adjust |

---
Now execute your task. Put your final output inside `<output>` tags.
