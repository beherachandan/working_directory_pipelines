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

# C3: Draft Agent

## Identity
- **Phase:** C — Content Generation
- **Stage:** Stage 3a-3e
- **Purpose:** Generate the full article draft following the outline, brief, and AEO best practices.

## Inputs
- Article outline from C2
- Research packet from C1
- Content brief from B3
- Brand voice guide (`_shared/brand-voice-guide.md`)

## Process

### Step 3a: Section-by-Section Writing
Write each section following:
- The outline's content block type assignment
- QAPE structure (Question heading → Direct Answer → Proof → Expansion)
- Voice: knowledgeable teaching colleague (per brand voice guide)

### Step 3b: Extractability Formatting
Apply formatting rules throughout:
- Short paragraphs: 2-3 sentences max
- Bulleted/numbered lists for 3+ items
- Headings phrased as questions
- Tables for any comparison content
- No walls of text
- Key answer passages: 40-60 words (optimal for AI snippet extraction)

### Step 3c: Trust Signal Injection
Weave in authority signals:
- First-person voice: "we tested", "based on X users", "our teachers report"
- Data references with "According to [Source]" framing
- Expert quotes with full attribution
- Authorship signals
- Consistent terminology (per brand voice guide)

### Step 3d: Internal Link Placement
Per the brief's linking plan:
- Link to parent `/learn/` hub
- Link to relevant product pages
- Link to resource library
- Use descriptive anchor text (never "click here")

### Step 3e: FAQ Section
Generate 5-8 FAQ items:
- Questions from EAR attributes not fully covered in main body
- Each answer: direct, self-contained, 40-60 words
- Suitable for FAQ schema markup

## Output
**Draft Article** (markdown format) containing:
- Full article with QAPE structure
- All EAR attributes addressed
- Stats, quotes, and citations placed
- Internal links inserted
- FAQ section
- Ready for citation enrichment (C4)

## Constraints
- Follow brand voice guide strictly
- Never exceed 4-sentence paragraphs
- Every section must have at least one trust signal (stat, quote, or first-person data)
- Product mentions: max 2-3 per article, always value-adding
- No superlatives without evidence
- No filler phrases ("In today's digital age...")

## Dependencies
- **Upstream:** C2 (outline), C1 (research), B3 (brief)
- **Downstream:** C4 (enriches citations), C5 (composes final draft)

## Skills Repo Reference
- `copywriting` — seven-sweep editing framework, benefits-over-features
- `ai-seo/references/content-patterns.md` — content block templates

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |

---
## Task Payload

**Topic:** What are formative assessment strategies?

### Upstream Agent Outputs

#### B3 Output
# Content Brief: Formative Assessment Strategies

> Stage 2 output — produced by B3 (Content Brief Generator)
> Source dossier: topic-dossier-formative-assessment-strategies.md

## Metadata
| Field | Value |
|-------|-------|
| Topic | What are formative assessment strategies? |
| Target URL | `/learn/assessments/formative-assessment-strategies` |
| Intent type | Informational + How-to (Hybrid) |
| Target word count | 2,500-3,000 |
| Schema type | FAQPage + HowTo + Article |
| Author | Education Content Lead |
| Date created | 2026-03-18 |
| Status | Approved |

## QAPE Skeleton

### Question
**What are formative assessment strategies, and how do teachers use them to improve learning?**

### Target Direct Answer (1-3 sentences)
> Formative assessment strategies are techniques teachers use during instruction to check student understanding and adjust teaching in real time. Common strategies include exit tickets, think-pair-share, quick polls, and observation checklists. Research shows formative assessment can produce learning gains equivalent to 8 months of additional progress when implemented consistently.

*[60 words — optimized for AI snippet extraction]*

### Required Proof Types
- [x] Statistics with sources (min: 8)
- [x] Expert quotes with attribution (min: 3)
- [x] First-person data ("we tested", "based on X users")
- [x] Case study / example
- [x] Research citation

### Expansion Structure
| Section (H2) | Content Block Type | EAR Attributes Covered | Notes |
|---------------|-------------------|----------------------|-------|
| What is formative assessment? | Definition Block | #1 (definition) | Lead with 40-60 word extractable definition; include etymology/pedagogical context |
| Why does formative assessment matter? | Evidence Sandwich Block | #2 (importance), #9 (research) | Include Hattie effect size (d=0.7), Black & Wiliam meta-analysis, learning gains data |
| How is formative assessment different from summative assessment? | Comparison Table Block | #3 (comparison) | Side-by-side table with 6-8 criteria rows (purpose, timing, stakes, feedback loop, examples) |
| What are the most effective formative assessment strategies? | Organized List Block | #4 (strategies), #5 (categorization), #7 (quick checks) | 15 strategies organized by time: <5 min (6 strategies) / 5-15 min (5 strategies) / Ongoing (4 strategies). Each strategy: name, 2-3 sentence description, classroom example, grade-level fit |
| How do you implement formative assessment in your classroom? | Step-by-Step Block + Grade-Level Guide | #6 (implementation), #12 (grade-level) | 5-step implementation framework + table showing K-2 / 3-5 / 6-8 / 9-12 adaptations for top 5 strategies |
| How often should you use formative assessment? | Frequency Guidance Block | #11 (frequency/timing) | Daily vs. weekly vs. unit-level rhythm; implementation calendar example; **MAJOR DIFFERENTIATOR** |
| How do you use formative assessment data? | Feedback Framework Block | #8 (feedback), #15 (tracking), #14 (differentiation) | Feedback loops, data tracking approaches (spreadsheet/app/observation notes), link to differentiation |
| What tools support formative assessment? | Comparison Table Block | #10 (digital tools) | Compare 5 tools (Wayground, Kahoot, Nearpod, Google Forms, Plickers) — natural WG integration; **MAJOR DIFFERENTIATOR** with step-by-step tech setup |
| What are common mistakes with formative assessment? | Troubleshooting Block | #13 (common mistakes) | 5-7 pitfalls with how to avoid each; **MAJOR DIFFERENTIATOR** |
| FAQ | FAQ items | Remaining variants | 6-8 items from uncovered EAR sub-questions and query variants |

## Content Requirements

### Statistics & Data (minimum targets)
| # | Stat needed | Preferred source type |
|---|-------------|----------------------|
| 1 | Effect size of formative assessment on learning (Hattie: d=0.7 or 8 months gain) | Research (Hattie Visible Learning, Black & Wiliam) |
| 2 | % of teachers using formative assessment regularly vs. effectiveness gap | Survey (NCES, Teach Plus, or Gates Foundation research) |
| 3 | Student performance improvement with consistent feedback loops | Research (Hattie, Marzano, or peer-reviewed study) |
| 4 | Time savings from digital formative assessment vs. paper-based | Survey data or edtech research |
| 5 | Engagement increase with game-based formative assessment | Platform data (Wayground: "Based on 200M+ resources, quick polls show 34% higher completion") |
| 6 | Optimal feedback timing (within 24-48 hours for maximum impact) | Research (Shute 2008, Hattie & Timperley) |
| 7 | % of students who improve with targeted interventions from formative data | Research or platform data |
| 8 | Cross-format usage patterns (teachers using 3+ formative assessment types per week) | Platform data (Wayground first-party data) |

### Expert Quotes (minimum targets)
| # | Quote topic | Source type |
|---|-------------|------------|
| 1 | Importance of real-time feedback in learning / formative assessment vs. summative | Researcher (Dylan Wiliam, John Hattie, or assessment specialist) |
| 2 | Practical classroom experience with formative assessment strategies | Practitioner (K-12 teacher from WG teacher network) |
| 3 | Digital tools' impact on formative assessment accessibility or frequency | Educator or edtech researcher |

### Source Citations (minimum targets)
- Min 8 external source citations with "According to [Source]" framing
- Min 3 internal WG data references ("Based on 200M+ Wayground resources..." or "Analysis of X quiz sessions...")

## Internal Linking Plan

### Concept <-> Tool <-> Material Triangle
| Link Type | Target Page | Anchor Text |
|-----------|------------|-------------|
| Parent hub | `/learn/assessments/` | assessment strategies for teachers |
| Related concept | `/learn/assessments/summative-assessment` | summative assessment (compare/contrast) |
| Related concept | `/learn/differentiation/differentiated-instruction` | differentiated instruction using formative data |
| Related concept | `/learn/classroom-management/feedback-strategies` | effective feedback strategies |
| Related spoke | `/learn/assessments/exit-tickets` | exit ticket strategies and templates |
| Related spoke | `/learn/assessments/diagnostic-assessment` | diagnostic assessment |
| Product page | `/features/quizzes` | real-time quiz tools for formative assessment |
| Product page | `/features/lessons` | interactive lessons with embedded checks for understanding |
| Product page | `/features/polls` | quick polls for instant feedback |
| Resource library | `/activities/math` | formative assessment activities for math |
| Resource library | `/worksheets/assessment-templates` | ready-to-use formative assessment templates |
| Resource library | `/activities/science` | science formative assessment examples |

**Internal linking strategy:**
- Link 10-15 specific WG resources as concrete examples within strategy descriptions
- Each of 15 strategies should link to 1-2 relevant ADPs or resource pages where applicable
- Natural product mentions in "What tools support formative assessment?" section (2-3 references)
- Hub-spoke linking: this page becomes pillar content for `/learn/assessments/` hub

## Competitive Differentiation

### WG's unique angle:
- **Practitioner-scale platform data** that no competitor has: "Based on analysis of 50M+ quiz sessions on Wayground, exit tickets show 42% higher completion rates when limited to 3 questions vs. 5+"
- **Complete implementation guide** covering grade-level adaptations, frequency recommendations, and common mistakes — areas where competitors have gaps or shallow coverage
- **Technology integration specifics** with step-by-step setup guidance for digital tools (vs. competitors' generic "use digital tools" mentions)

### Data/perspective competitors lack:
- **Cross-format usage patterns:** "Teachers using 3+ formative assessment formats per week see 28% higher student engagement" (from 200M+ WG resources)
- **Grade-specific adaptation table:** K-2 vs. 3-5 vs. 6-8 vs. 9-12 comparison for top strategies (competitors treat K-12 as monolithic)
- **Frequency/timing guidance:** Daily vs. weekly vs. unit-level rhythm recommendations with implementation calendar (only 15% of competitors address)
- **Common mistakes section:** Troubleshooting based on teacher community insights (competitive gap per A2 analysis)
- **Teacher SME network quotes:** Real practitioner voices from 30+ educators in vetting loop

### Why WG should be cited over current sources:
1. **Most comprehensive single-page resource:** Covers all 15 EAR attributes vs. competitors' 8-12, giving higher overlap with AI sub-query decomposition
2. **Unique sub-query ownership:** WG is the definitive source for frequency guidance (#11), grade-level adaptation (#12), digital tool implementation (#10), and common mistakes (#13) — AI engines will cite WG when these sub-queries arise
3. **Research + practice combination:** Balances academic credibility (Dylan Wiliam, Hattie citations) with practitioner-scale data (200M+ resources)
4. **Actionable implementation focus:** Every strategy includes time requirement, grade-level fit, and link to ready-to-use resource (vs. competitors' theoretical descriptions)

## Format Specification

### Structure Requirements
- [x] Headings phrased as questions (all H2s in question format matching search intent)
- [x] Short paragraphs (2-3 sentences max for extractability)
- [x] Bullets/numbered lists for 3+ items (especially 15 strategies section)
- [x] Tables for comparisons:
  - Formative vs. Summative assessment (6-8 criteria rows)
  - Grade-level adaptation guide (4 grade bands × 5 strategies)
  - Digital tools comparison (5 tools × 5 criteria)
- [x] FAQ section (6-8 items from query variants + uncovered sub-questions)
- [x] Author bio with education credentials and teaching experience
- [x] "Last updated" date with quarterly review commitment (freshness signal)

### Content Block Specifications

**15 Strategies Section (Core of Article):**
- Organize by implementation time: <5 min (6 items) / 5-15 min (5 items) / Ongoing (4 items)
- Each strategy entry format:
  ```
  **[Strategy Name]** (Time: X min | Grades: X-X)
  [2-3 sentence description with pedagogical rationale]
  *Example:* [Specific classroom scenario with grade/subject context]
  [Link to WG resource: "Try this [exit ticket template] on Wayground"]
  ```
- Target 80-120 words per strategy × 15 = 1,200-1,800 words for this section alone

**Evidence Sandwich Pattern (Section 2: Why it matters):**
- Lead with research claim + citation
- Follow with platform data supporting claim
- Close with practitioner quote validating both
- Example structure: "According to [Hattie], formative assessment has effect size of 0.7... Based on Wayground's 200M+ resources, we observed... 'In my classroom,' says [Teacher Name], [Quote]..."

**Step-by-Step Implementation (Section 5):**
- 5 steps, each 40-60 words
- Each step includes: What to do, Why it matters, Example
- Step 5 links to Section 7 (frequency guidance) for sustainability

**Grade-Level Adaptation Table (Section 5):**
- Rows: Top 5 most versatile strategies
- Columns: K-2 | 3-5 | 6-8 | 9-12
- Cells: 20-30 word adaptation notes per grade band

**Common Mistakes Section (Section 9):**
- 5-7 mistakes in numbered list
- Each: **Mistake name** → Why it happens → How to avoid (2-3 sentences each)

**FAQ Section:**
- 6-8 items covering:
  - How long does formative assessment take? (#11 variant)
  - Can I use formative assessment for grading? (summative confusion)
  - What if students don't take it seriously? (implementation challenge)
  - How do I formatively assess remote/hybrid students? (context adaptation)
  - What's the difference between formal and informal formative assessment? (terminology)
  - How do I store formative assessment data? (#15 variant)
  - Plus 2 others from query variant analysis

### Schema Markup Requirements
- **FAQPage schema:** For FAQ section (6-8 questions)
- **HowTo schema:** For step-by-step implementation section (5 steps)
- **Article schema:** Overall page with author, datePublished, dateModified

### Visual/Formatting Elements
- Pull quote: Dylan Wiliam or Hattie research finding (snippet-optimized)
- Comparison table: Formative vs. Summative (early in article, high citation value)
- Implementation calendar graphic (optional, if design resources available)
- Grade-level table: 5 strategies × 4 grade bands

### E-E-A-T Signals
- Author byline with credentials: "[Author Name], [Education credentials], [Years teaching/ed leadership]"
- Teacher SME attribution: "[Quote]" says [Full Name], [Grade/Subject] teacher at [District/School type]"
- Research citations: Minimum 5 authoritative sources (Dylan Wiliam, John Hattie, Black & Wiliam, Marzano, peer-reviewed journals)
- First-person data: "Based on 200M+ resources on Wayground..." / "We analyzed 50M+ quiz sessions..."
- Update commitment: "Last updated: [Date] | Reviewed quarterly by education team"
- Related credentials link: Link to author page with full bio, publications, teaching background

### Target Word Count Allocation
| Section | Target Words | % of Total |
|---------|-------------|------------|
| Definition (Section 1) | 150-200 | 6% |
| Why it matters (Section 2) | 300-400 | 13% |
| Formative vs. Summative (Section 3) | 200-250 | 8% |
| 15 Strategies (Section 4) | 1,200-1,500 | 48% |
| Implementation (Section 5) | 300-400 | 13% |
| Frequency (Section 6) | 150-200 | 6% |
| Data use (Section 7) | 150-200 | 6% |
| Tools (Section 8) | 200-250 | 8% |
| Common mistakes (Section 9) | 200-250 | 8% |
| FAQ (Section 10) | 300-400 | 13% |
| **TOTAL** | **2,650-3,250** | **100%** |

*Target zone: 2,800-3,000 words (allows flexibility while staying within B1's comprehensive range)*

---

## Additional Specifications for C-Phase Agents

### For C1 (Definition Specialist)
- Section 1 must be snippet-optimized: 40-60 words, self-contained, no pronouns referencing prior context
- Include brief etymology or pedagogical roots (formative = forming/shaping learning in progress)

### For C2 (List Curator)
- 15 strategies must include mix of: observation-based, question-based, written, discussion-based, digital, kinesthetic
- Avoid duplicating TeachThought's "27 strategies" list — choose strategies based on WG platform fit and platform data
- Prioritize strategies that link to existing WG resources (quizzes, polls, lessons, flashcards, worksheets)

### For C3 (Research Integrator) — Requires Opus Model
- Must cite: Dylan Wiliam (5 formative assessment strategies framework), Black & Wiliam meta-analysis, John Hattie (Visible Learning effect sizes)
- Research integration should follow Evidence Sandwich pattern: Research claim → WG data → Practitioner quote

### For C4 (Citation Enricher)
- Minimum 8 external citations, 3 internal WG data points
- Citation format: "According to [Source, Year], [finding]" OR "[Finding], according to [Source]"
- Sources must be recent (2020+) except for seminal research (Hattie, Black & Wiliam acceptable older)

### For C5 (Example Writer) — Requires Opus Model
- Each of 15 strategies needs concrete classroom example with grade + subject context
- Examples should span: K-2, 3-5, 6-8, 9-12 and subjects (math, science, ELA, social studies)
- At least 5 examples should reference WG platform features naturally ("The teacher used Wayground's poll feature to...")

### For D1 (AEO Evaluator)
- Must verify all 15 EAR attributes are covered (100% target)
- Snippet optimization check: Opening definition is 40-60 words and self-contained
- Differentiation check: Attributes #10, #11, #12, #13 (major differentiators) are executed in-depth

---

## Success Criteria

**Minimum viable (D1 PASS threshold):**
- 14/15 EAR attributes covered (93%)
- 2,500+ words
- 6+ stats with citations
- 2+ expert quotes
- Formative vs. Summative comparison table present
- 12+ strategies listed with examples
- FAQ section with 5+ items

**Competitive citation target (D1 HIGH PASS):**
- 15/15 EAR attributes covered (100%)
- 2,800-3,000 words
- 8+ stats with citations
- 3+ expert quotes
- All 4 major differentiators (#10, #11, #12, #13) executed in-depth
- 15 strategies with 10+ linked WG resources
- FAQ section with 6-8 items
- Grade-level adaptation table present

**Definitive guide status:**
- Exceeds all HIGH PASS criteria
- First-party WG data in 3+ sections
- Teacher SME quotes from WG network (2-3 quotes)
- All required tables present (3 tables)
- Schema markup specifications met
- Update commitment and author credentials displayed

#### C1 Output
I need web search access to gather verified statistics, expert quotes, and sources for this research packet. This is essential for the C1 Research Agent role — I must find real, verifiable data rather than fabricating sources.

May I proceed with web searches to find:
- John Hattie's formative assessment research and effect sizes
- Dylan Wiliam quotes and research on formative assessment
- Black & Wiliam meta-analysis findings
- Teacher usage statistics from recent surveys
- Research on feedback timing and student improvement
- Digital vs. paper-based assessment data

#### C2 Output
# Article Outline: What Are Formative Assessment Strategies?

## Article Metadata
- **Target URL:** `/learn/assessments/formative-assessment-strategies`
- **Target Word Count:** 2,800-3,000 words
- **Schema Types:** FAQPage + HowTo + Article
- **Author Byline:** [Education Content Lead name], [Credentials], [Years of teaching/ed leadership experience]
- **Update Commitment:** "Last updated: 2026-03-18 | Reviewed quarterly by education team"

---

## Full Heading Hierarchy

### H1: What are formative assessment strategies, and how do teachers use them to improve learning?

**Target Direct Answer Block** (60 words, snippet-optimized)
- Place immediately after H1, before first H2
- Self-contained, no forward references
- Include: definition + 3-4 strategy examples + research impact stat
- **STAT PLACEMENT:** Hattie effect size or "8 months additional progress" finding (Stat #1 from brief)

---

### H2: What is formative assessment?

**Content Block Type:** Definition Block  
**Word Target:** 150-200 words  
**EAR Attributes:** #1 (definition)

**Section Structure:**
1. **Opening paragraph** (40-60 words):
   - Core definition: techniques used DURING instruction to check understanding and adjust teaching
   - Distinguish from assessment OF learning vs. assessment FOR learning
   - Etymology note: "formative" = forming/shaping learning in progress

2. **Second paragraph** (50-70 words):
   - Key characteristics: low-stakes, frequent, actionable, timely feedback loop
   - Not graded, used to inform next instructional steps
   
3. **Third paragraph** (40-60 words):
   - Brief historical/pedagogical context: roots in Bloom's mastery learning, formalized by Black & Wiliam research
   - **RESEARCH CITATION PLACEMENT:** Black & Wiliam foundational work

**Stats/Quotes:** None primary (save for Section 2)

---

### H2: Why does formative assessment matter?

**Content Block Type:** Evidence Sandwich Block  
**Word Target:** 300-400 words  
**EAR Attributes:** #2 (importance), #9 (research backing)

**Section Structure:**

#### H3: The research behind formative assessment

**Paragraph 1** (60-80 words):
- **STAT PLACEMENT #1:** Hattie effect size (d=0.7) = 8 months additional learning gain
- **RESEARCH CITATION:** According to John Hattie's Visible Learning research...
- Context: ranks among most effective teaching interventions

**Paragraph 2** (60-80 words):
- **STAT PLACEMENT #2:** Black & Wiliam meta-analysis findings on student achievement gains
- **RESEARCH CITATION:** According to Black & Wiliam [year], formative assessment...

#### H3: Real-world impact

**Paragraph 3** (60-80 words):
- **STAT PLACEMENT #5:** Wayground platform data - "Based on analysis of 200M+ resources, teachers using formative assessment see X% higher completion rates..."
- **STAT PLACEMENT #3:** Student performance improvement with consistent feedback loops (Marzano or other research)

**Paragraph 4** (60-80 words):
- **EXPERT QUOTE PLACEMENT #1:** Dylan Wiliam quote on importance of real-time feedback / formative vs. summative distinction
- Attribution format: "[Quote]," says Dylan Wiliam, Emeritus Professor at University College London

**Paragraph 5** (40-60 words):
- **EXPERT QUOTE PLACEMENT #2:** Practitioner quote from WG teacher network on classroom experience with formative assessment
- Attribution: "[Quote]," says [Teacher Name], [Grade/Subject] teacher at [District/School type]

---

### H2: How is formative assessment different from summative assessment?

**Content Block Type:** Comparison Table Block  
**Word Target:** 200-250 words  
**EAR Attributes:** #3 (comparison with summative)

**Section Structure:**

**Opening paragraph** (40-60 words):
- Lead-in explaining both are essential, serve different purposes
- Preview table comparing 8 key criteria

**Comparison Table:**
| Criteria | Formative Assessment | Summative Assessment |
|----------|---------------------|---------------------|
| **Purpose** | [20-30 words] | [20-30 words] |
| **Timing** | During instruction | End of unit/term/year |
| **Stakes** | Low/no stakes | High stakes |
| **Feedback** | Immediate, actionable | Delayed, evaluative |
| **Function** | Assessment FOR learning | Assessment OF learning |
| **Grading** | Typically ungraded | Graded/scored |
| **Frequency** | Daily to weekly | Periodic (unit/term/annual) |
| **Examples** | Exit tickets, polls, observation | Final exams, standardized tests, end-of-unit projects |

**Closing paragraph** (40-60 words):
- Both needed: formative guides instruction, summative measures outcomes
- Internal link opportunity: Link to `/learn/assessments/summative-assessment` page

---

### H2: What are the most effective formative assessment strategies?

**Content Block Type:** Organized List Block (categorized by time)  
**Word Target:** 1,200-1,500 words (CORE SECTION - 48% of article)  
**EAR Attributes:** #4 (strategies list), #5 (categorization), #7 (quick checks)

**Section Opening** (60-80 words):
- Overview of 15 strategies organized by implementation time
- Note: strategies span observation, questioning, written, discussion, digital, and kinesthetic formats
- **STAT PLACEMENT #8:** Cross-format usage stat - "Teachers using 3+ formative assessment formats per week see X% higher student engagement" (WG data)

---

#### H3: Quick checks (under 5 minutes)

**Strategy format for each:**
```
**[Strategy Name]** (Time: X min | Grades: X-X)
[2-3 sentence description with pedagogical rationale]
*Example:* [Specific classroom scenario with grade/subject context]
[Link to WG resource where applicable]
```

**6 Strategies to include:**

1. **Exit Tickets** (Time: 3-4 min | Grades: K-12)
   - 80-120 word entry
   - Example: [Grade-specific scenario]
   - Link: `/learn/assessments/exit-tickets` + link to WG exit ticket template

2. **Fist to Five** (Time: 1 min | Grades: K-8)
   - 80-120 word entry
   - Example: [Elementary classroom scenario]

3. **Quick Polls/Clicker Questions** (Time: 2-3 min | Grades: 3-12)
   - 80-120 word entry
   - Example: [Middle school science scenario]
   - Link to WG poll feature
   - **STAT PLACEMENT #5 (variant):** "Based on 200M+ Wayground resources, quick polls show 34% higher completion rates when..."

4. **Think-Pair-Share** (Time: 3-5 min | Grades: 2-12)
   - 80-120 word entry
   - Example: [High school humanities scenario]

5. **Whiteboard Flash** (Time: 2-3 min | Grades: K-12)
   - 80-120 word entry
   - Example: [Elementary math scenario]

6. **Traffic Light Cards** (Time: 1-2 min | Grades: K-8)
   - 80-120 word entry
   - Example: [Primary classroom scenario]

---

#### H3: Deeper checks (5-15 minutes)

**5 Strategies to include:**

7. **Entrance Tickets** (Time: 5-7 min | Grades: 3-12)
   - 80-120 word entry
   - Example: scenario

8. **Four Corners** (Time: 10-12 min | Grades: 3-12)
   - 80-120 word entry
   - Example: scenario

9. **Gallery Walk** (Time: 10-15 min | Grades: 4-12)
   - 80-120 word entry
   - Example: scenario

10. **One-Minute Essay** (Time: 5-7 min | Grades: 6-12)
    - 80-120 word entry
    - Example: scenario

11. **Socratic Seminar Snapshot** (Time: 10-15 min | Grades: 7-12)
    - 80-120 word entry
    - Example: scenario

---

#### H3: Ongoing formative assessment strategies

**4 Strategies to include:**

12. **Observation Checklists** (Time: Ongoing | Grades: K-12)
    - 80-120 word entry
    - Example: scenario with teacher tracking tool
    - **LINK OPPORTUNITY:** WG resource for observation templates

13. **Learning Journals/Reflection Logs** (Time: Ongoing | Grades: 3-12)
    - 80-120 word entry
    - Example: scenario

14. **Peer Assessment** (Time: Ongoing | Grades: 4-12)
    - 80-120 word entry
    - Example: scenario with rubric

15. **Digital Quizzes/Adaptive Practice** (Time: Ongoing | Grades: 3-12)
    - 80-120 word entry
    - Example: scenario using WG quiz platform
    - **STAT PLACEMENT #4:** Time savings from digital vs. paper-based formative assessment
    - Natural WG product integration

---

### H2: How do you implement formative assessment in your classroom?

**Content Block Type:** Step-by-Step Block (HowTo schema) + Grade-Level Adaptation Table  
**Word Target:** 300-400 words  
**EAR Attributes:** #6 (implementation steps), #12 (grade-level adaptations)

**Section Opening** (40-60 words):
- Overview: 5-step framework for building formative assessment practice
- Note: adaptations provided for K-2, 3-5, 6-8, 9-12

---

#### H3: Five steps to build your formative assessment practice

**Step 1: Start with one strategy** (40-60 words)
- What: Choose 1 strategy from quick checks, practice for 2 weeks
- Why: Mastery before expansion prevents overwhelm
- Example: "Begin with exit tickets 2x/week"

**Step 2: Build your question bank** (40-60 words)
- What: Collect 10-15 key understanding checkpoints per unit
- Why: Pre-planning reduces cognitive load during instruction
- Example: "Create question bank aligned to learning objectives"

**Step 3: Create a feedback loop** (40-60 words)
- What: Decide how you'll track responses and adjust instruction
- Why: Data only matters if it informs action
- Example: "Use simple spreadsheet or WG analytics dashboard"
- Link to Section 7 (data use)

**Step 4: Add variety gradually** (40-60 words)
- What: After 1 strategy is routine, add 1-2 more formats
- Why: Multi-modal assessment reaches all learners
- Example: "Add think-pair-share to complement exit tickets"

**Step 5: Build a sustainable rhythm** (40-60 words)
- What: Establish which strategies are daily, weekly, unit-level
- Why: Consistency yields better data than sporadic use
- Example: "Daily quick check + weekly deeper check + unit-level reflection"
- Forward reference to Section 6 (frequency guidance)

---

#### H3: Grade-level adaptations for top strategies

**Grade-Level Adaptation Table:**

| Strategy | K-2 | 3-5 | 6-8 | 9-12 |
|----------|-----|-----|-----|------|
| **Exit Tickets** | [20-30 words: drawing/emoji-based, 1 question] | [20-30 words: 2-3 questions, sentence responses] | [20-30 words: 3 questions, paragraph option] | [20-30 words: synthesis question, self-assessment component] |
| **Think-Pair-Share** | [20-30 words: partner talk with sentence frames] | [20-30 words: structured protocol, note-taking] | [20-30 words: evidence-based discussion, peer feedback] | [20-30 words: Socratic approach, devil's advocate roles] |
| **Quick Polls** | [20-30 words: yes/no, thumbs up/down, visual options] | [20-30 words: multiple choice, ranking] | [20-30 words: complex scenarios, justification required] | [20-30 words: application problems, real-world contexts] |
| **Observation Checklists** | [20-30 words: skill-based, behavior indicators] | [20-30 words: process + product, collaboration skills] | [20-30 words: critical thinking indicators, depth markers] | [20-30 words: disciplinary thinking, transfer indicators] |
| **Digital Quizzes** | [20-30 words: game-based, image-heavy, audio options] | [20-30 words: mixed formats, instant feedback] | [20-30 words: adaptive branching, hint systems] | [20-30 words: complex problem sets, auto-grading essays] |

**Table caption:** Adapt these five versatile strategies across all grade levels by adjusting complexity, response format, and scaffolding.

---

### H2: How often should you use formative assessment?

**Content Block Type:** Frequency Guidance Block  
**Word Target:** 150-200 words  
**EAR Attributes:** #11 (frequency/timing) — **MAJOR DIFFERENTIATOR**

**Section Structure:**

**Paragraph 1** (50-70 words):
- Three rhythm levels: Daily micro-checks, weekly deeper checks, unit-level reflection
- **STAT PLACEMENT #6:** Optimal feedback timing - "Research shows feedback within 24-48 hours has maximum impact" (Shute 2008, Hattie & Timperley)

**Paragraph 2** (50-70 words):
- Daily: 1-2 quick checks (<5 min) per lesson
- Weekly: 1 deeper check (5-15 min) to assess progress on complex skills
- Unit-level: 1 ongoing strategy (journals, observation) + 1 entrance ticket at unit start

**Paragraph 3** (50-70 words):
- Implementation calendar example: "Week 1 of unit: entrance ticket + 4 exit tickets + observation checklist"
- Avoid: every-minute checking (diminishing returns), sporadic use (insufficient data)

---

### H2: How do you use formative assessment data?

**Content Block Type:** Feedback Framework Block  
**Word Target:** 150-200 words  
**EAR Attributes:** #8 (feedback loops), #15 (data tracking), #14 (differentiation link)

**Section Structure:**

**Paragraph 1** (50-70 words):
- Formative data → immediate instructional response cycle
- Same-day adjustment examples: re-teach, small group pullout, advance faster
- **STAT PLACEMENT #7:** % of students improving with targeted interventions from formative data

**Paragraph 2** (50-70 words):
- Tracking approaches: simple (sticky notes, checklist), moderate (spreadsheet), advanced (platform analytics like WG dashboard)
- Key: system matches teacher's workflow, not aspirational complexity
- **Link opportunity:** WG analytics feature for automatic data aggregation

**Paragraph 3** (50-70 words):
- Differentiation link: formative data identifies who needs what
- Forward to next action: group formation, intervention assignment, enrichment pathways
- **Internal link:** `/learn/differentiation/differentiated-instruction` page

---

### H2: What tools support formative assessment?

**Content Block Type:** Comparison Table Block + Implementation Guide  
**Word Target:** 200-250 words  
**EAR Attributes:** #10 (digital tools) — **MAJOR DIFFERENTIATOR**

**Section Opening** (40-60 words):
- Digital tools increase frequency and reduce grading burden
- **STAT PLACEMENT #4:** Time savings from digital formative assessment vs. paper-based
- **EXPERT QUOTE PLACEMENT #3:** Educator or edtech researcher on digital tools' impact on assessment accessibility/frequency

---

#### H3: Comparing digital formative assessment tools

**Tool Comparison Table:**

| Feature | Wayground | Kahoot | Nearpod | Google Forms | Plickers |
|---------|-----------|--------|---------|--------------|----------|
| **Real-time results** | [10-15 words] | [10-15 words] | [10-15 words] | [10-15 words] | [10-15 words] |
| **Question types** | [10-15 words] | [10-15 words] | [10-15 words] | [10-15 words] | [10-15 words] |
| **Pre-built content** | 200M+ resources | [10-15 words] | [10-15 words] | None (template library) | None |
| **Free tier** | [10-15 words] | [10-15 words] | [10-15 words] | Fully free | Fully free |
| **Best for** | [15-20 words] | [15-20 words] | [15-20 words] | [15-20 words] | [15-20 words] |

**Paragraph after table** (60-80 words):
- Natural WG integration: step-by-step setup guidance
- "To create a formative quiz on Wayground: [3-4 step micro-tutorial with links to `/features/quizzes`]"
- Emphasize: ease of use, pre-built content library, instant feedback dashboard

---

### H2: What are common mistakes with formative assessment?

**Content Block Type:** Troubleshooting Block  
**Word Target:** 200-250 words  
**EAR Attributes:** #13 (common mistakes/pitfalls) — **MAJOR DIFFERENTIATOR**

**Section Opening** (40-60 words):
- Even experienced teachers fall into these traps
- Based on WG teacher network insights and 200M+ platform resources

**Numbered List of Mistakes (7 items):**

**1. Using formative data for grades**
- [30-40 words: Why it happens, why it's problematic, how to avoid]
- "If students know it's graded, they won't risk showing confusion"

**2. Collecting data but not adjusting instruction**
- [30-40 words: Why it happens, why it's problematic, how to avoid]
- "Data without action is just paperwork"

**3. Asking too many questions at once**
- [30-40 words: Why it happens, why it's problematic, how to avoid]
- **STAT REFERENCE:** "Based on 50M+ quiz sessions on Wayground, exit tickets with 3 questions show 42% higher completion vs. 5+ questions"

**4. Waiting too long to give feedback**
- [30-40 words: Why it happens, why it's problematic, how to avoid]
- Reference Stat #6 (24-48 hour window)

**5. Only assessing the same students**
- [30-40 words: Why it happens (hand-raisers), why it's problematic, how to avoid (random selection, digital tools ensure all respond)]

**6. Making it too complicated**
- [30-40 words: Why it happens (Pinterest syndrome), why it's problematic, how to avoid (start simple)]

**7. Formative assessing content students haven't been taught yet**
- [30-40 words: diagnostic vs. formative distinction, timing matters]
- **Internal link:** `/learn/assessments/diagnostic-assessment` page

---

### H2: Frequently asked questions about formative assessment

**Content Block Type:** FAQ items (FAQPage schema)  
**Word Target:** 300-400 words  
**EAR Attributes:** Remaining query variants and sub-questions

**8 FAQ Items (each 40-60 words):**

**Q1: How long does formative assessment take?**
- A: [40-60 words addressing #11 variant - quick checks 1-5 min, deeper checks 5-15 min, ongoing strategies integrated into existing instruction, daily time investment 5-10 minutes for high-frequency practice]

**Q2: Can I use formative assessment for grading?**
- A: [40-60 words addressing summative confusion - technically yes but defeats purpose, loses safety to show confusion, consider "practice points" or completion credit rather than accuracy grading]

**Q3: What if students don't take it seriously?**
- A: [40-60 words addressing implementation challenge - build culture of growth mindset, model how you use data to help them, gamification increases engagement, show them their progress over time]

**Q4: How do I formatively assess remote or hybrid students?**
- A: [40-60 words addressing context adaptation - digital tools essential (polls, quizzes, breakout rooms for think-pair-share), chat/emoji responses, async options like discussion boards or recorded explanations]

**Q5: What's the difference between formal and informal formative assessment?**
- A: [40-60 words addressing terminology - formal = planned/structured (exit tickets, quizzes), informal = observational/spontaneous (cold calling, monitoring during work time), both valuable, informal requires strong mental tracking system]

**Q6: How do I store and organize formative assessment data?**
- A: [40-60 words addressing #15 variant - match system to volume: low-tech (sticky notes, notebook), mid-tech (spreadsheet with student roster), high-tech (platform like WG with auto-aggregation), key is consistency over sophistication]

**Q7: Can formative assessment work for all subjects?**
- A: [40-60 words addressing versatility - absolutely, strategies adapt across disciplines, STEM uses problem-solving checks, humanities uses discussion/writing checks, arts uses critique/self-assessment, PE uses skill demonstration checklists]

**Q8: How is formative assessment different from diagnostic assessment?**
- A: [40-60 words addressing diagnostic vs. formative - diagnostic = BEFORE instruction to identify starting point, formative = DURING instruction to adjust teaching, summative = AFTER to measure outcomes, all three needed at different times]
- **Internal link:** `/learn/assessments/diagnostic-assessment` page

---

## Internal Linking Plan (10-15 links throughout article)

### Hub-Spoke Links
- Parent hub: `/learn/assessments/` (anchor: "assessment strategies for teachers") — place in intro
- Related concept: `/learn/assessments/summative-assessment` (anchor: "summative assessment") — place in Section 3
- Related concept: `/learn/differentiation/differentiated-instruction` (anchor: "differentiated instruction using formative data") — place in Section 7
- Related concept: `/learn/classroom-management/feedback-strategies` (anchor: "effective feedback strategies") — place in Section 2 or 7
- Related spoke: `/learn/assessments/exit-tickets` (anchor: "exit ticket strategies and templates") — place in Section 4
- Related spoke: `/learn/assessments/diagnostic-assessment` (anchor: "diagnostic assessment") — place in FAQ Q8

### Product Pages
- `/features/quizzes` (anchor: "real-time quiz tools for formative assessment") — place in Section 8
- `/features/lessons` (anchor: "interactive lessons with embedded checks for understanding") — place in Section 4 or 8
- `/features/polls` (anchor: "quick polls for instant feedback") — place in Section 4, Strategy #3

### Resource Library (specific examples within strategies)
- `/activities/math` (anchor: "formative assessment activities for math") — place in Section 4, math example
- `/worksheets/assessment-templates` (anchor: "ready-to-use formative assessment templates") — place in Section 4, exit ticket strategy
- `/activities/science` (anchor: "science formative assessment examples") — place in Section 4, science example

---

## Stats/Quotes Placement Summary

### Statistics (8 required, mapped to sections):
1. **Stat #1** (Hattie d=0.7 / 8 months gain) → Target Direct Answer + Section 2, Para 1
2. **Stat #2** (Teacher usage vs. effectiveness gap) → Section 2, Para 2 OR Section 9 (context for mistakes)
3. **Stat #3** (Student improvement with feedback loops) → Section 2, Para 3
4. **Stat #4** (Time savings digital vs. paper) → Section 8, opening
5. **Stat #5** (Engagement with game-based/polls) → Section 4, opening OR Strategy #3
6. **Stat #6** (Optimal feedback timing 24-48 hrs) → Section 6, Para 1
7. **Stat #7** (Student improvement with targeted interventions) → Section 7, Para 1
8. **Stat #8** (Cross-format usage patterns) → Section 4, opening

### Expert Quotes (3 required, mapped to sections):
1. **Quote #1** (Researcher - Wiliam or Hattie on importance/formative vs. summative) → Section 2, Para 4
2. **Quote #2** (Practitioner - K-12 teacher from WG network) → Section 2, Para 5
3. **Quote #3** (Educator/edtech researcher on digital tools) → Section 8, opening

### Wayground First-Party Data (3+ references):
- Section 2, Para 3: "Based on 200M+ resources..."
- Section 4, Strategy #3: "Based on 200M+ Wayground resources, quick polls show..."
- Section 4, opening: Cross-format usage stat
- Section 9, Mistake #3: "Based on 50M+ quiz sessions on Wayground, exit tickets..."

---

## Content Block Instructions for C3 (Draft Writer)

### Section 1 (Definition)
- **Critical:** Opening paragraph MUST be 40-60 words, snippet-optimized, self-contained
- Include etymology/pedagogical framing (formative = shaping in progress)
- No forward references or pronouns without clear antecedents

### Section 4 (15 Strategies - CORE SECTION)
- Each strategy: Name + Time/Grade in header + 80-120 word description + classroom example + WG link where applicable
- Examples must span: K-2 (min 2), 3-5 (min 3), 6-8 (min 3), 9-12 (min 3)
- Examples must span subjects: math (min 3), science (min 2), ELA (min 3), social studies (min 2)
- At least 10 strategies should link to specific WG resources (ADPs, templates, features)
- Avoid duplicating TeachThought's "27 strategies" list — choose based on WG platform fit

### Section 5 (Implementation)
- Use HowTo schema markup for 5-step process
- Each step: 40-60 words with What/Why/Example structure
- Grade-level table: exactly 5 strategies × 4 grade bands, 20-30 words per cell

### Section 8 (Tools)
- Table must compare exactly 5 tools: Wayground, Kahoot, Nearpod, Google Forms, Plickers
- Balanced tone: highlight WG strengths without denigrating competitors
- Include 3-4 step micro-tutorial for setting up formative assessment on WG platform
- Natural product integration (2-3 mentions max)

### Section 9 (Common Mistakes)
- All 7 mistakes must follow pattern: **Mistake name** → Why it happens → How to avoid (30-40 words each)
- Tone: helpful colleague, not judgmental
- Include WG platform data in Mistake #3 (question overload stat)

### Section 10 (FAQ)
- Each answer: 40-60 words, self-contained (could be extracted independently)
- Q8 must include internal link to diagnostic assessment page

---

## Schema Markup Specifications for Technical Implementation

### FAQPage Schema (Section 10)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[FAQ Q1]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[FAQ A1]"
      }
    }
    // ... 8 total FAQ items
  ]
}
```

### HowTo Schema (Section 5, 5-step process)
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to implement formative assessment in your classroom",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Start with one strategy",
      "text": "[Step 1 full text]"
    }
    // ... 5 total steps
  ]
}
```

### Article Schema (Overall page)
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What are formative assessment strategies, and how do teachers use them to improve learning?",
  "author": {
    "@type": "Person",
    "name": "[Author Name]"
  },
  "datePublished": "2026-03-18",
  "dateModified": "2026-03-18"
}
```

---

## Word Count Allocation by Section

| Section | H2 Heading | Target Words | % of Total |
|---------|-----------|--------------|------------|
| Intro | Target Direct Answer | 60 | 2% |
| 1 | What is formative assessment? | 150-200 | 6% |
| 2 | Why does formative assessment matter? | 300-400 | 13% |
| 3 | How is formative assessment different from summative? | 200-250 | 8% |
| 4 | What are the most effective formative assessment strategies? | 1,200-1,500 | 48% |
| 5 | How do you implement formative assessment? | 300-400 | 13% |
| 6 | How often should you use formative assessment? | 150-200 | 6% |
| 7 | How do you use formative assessment data? | 150-200 | 6% |
| 8 | What tools support formative assessment? | 200-250 | 8% |
| 9 | What are common mistakes with formative assessment? | 200-250 | 8% |
| 10 | FAQ | 300-400 | 13% |
| **TOTAL** |  | **2,710-3,310** | **100%** |

**Target zone: 2,800-3,000 words (allows for variance in section execution)**

---

## Success Criteria Checklist for D1 Evaluation

### Minimum Viable (PASS threshold):
- [ ] 14/15 EAR attributes covered (93%)
- [ ] 2,500+ words
- [ ] 6+ stats with citations
- [ ] 2+ expert quotes
- [ ] Formative vs. Summative comparison table present
- [ ] 12+ strategies listed with examples
- [ ] FAQ section with 5+ items

### Competitive Citation Target (HIGH PASS):
- [ ] 15/15 EAR attributes covered (100%)
- [ ] 2,800-3,000 words
- [ ] 8+ stats with citations
- [ ] 3+ expert quotes
- [ ] All 4 major differentiators (#10, #11, #12, #13) executed in-depth
- [ ] 15 strategies with 10+ linked WG resources
- [ ] FAQ section with 6-8 items
- [ ] Grade-level adaptation table present

### Definitive Guide Status:
- [ ] Exceeds all HIGH PASS criteria
- [ ] First-party WG data in 3+ sections
- [ ] Teacher SME quotes from WG network (2-3 quotes)
- [ ] All required tables present (3 tables: formative vs. summative, grade-level adaptations, digital tools comparison)
- [ ] Schema markup specifications met (FAQPage + HowTo + Article)
- [ ] Update commitment and author credentials displayed

---

## Notes for Downstream Agents

**For C3 (Draft Writer - REQUIRES OPUS):**
- Section 4 is your heaviest lift (1,200-1,500 words = 48% of article)
- Budget 80-120 words per strategy × 15 strategies
- Each strategy needs: name, time/grade, description, example, link (where applicable)
- Use this outline's structure exactly — do not reorganize sections

**For C4 (Citation Enricher):**
- Wait for C1's research packet to arrive before enriching citations
- You need 8 external stats + 3 expert quotes + 3 WG first-party data points
- Citation format: "According to [Source, Year], [finding]" OR "[Finding], according to [Source]"
- All sources must be real and verifiable — C1 will provide these

**For C5 (Example Writer - REQUIRES OPUS):**
- 15 strategies need 15 classroom examples (1 per strategy in Section 4)
- Examples must include: grade level, subject, specific scenario, student response
- At least 5 examples should naturally reference WG platform features
- Examples should span K-12 and all major subjects

**For D1 (AEO Evaluator):**
- This outline covers all 15/15 EAR attributes per B3's expansion structure table
- Major differentiators are Sections 6 (#11), 8 (#10), 5 table (#12), 9 (#13)
- If C3 executes this outline as specified, article should achieve HIGH PASS threshold

---
Now execute your task. Put your final output inside `<output>` tags.
