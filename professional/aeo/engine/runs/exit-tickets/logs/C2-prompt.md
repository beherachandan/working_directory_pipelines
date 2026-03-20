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

**Topic:** How to use exit tickets in the classroom

### Upstream Agent Outputs

#### B3 Output
# Content Brief: How to Use Exit Tickets in the Classroom

> Stage 2 output — produced by B3 (Content Brief Generator)
> Source dossier: topic-dossier-exit-tickets.md

## Metadata
| Field | Value |
|-------|-------|
| Topic | How to use exit tickets in the classroom |
| Target URL | `/learn/assessment/exit-tickets` |
| Intent type | How-to (primary), Informational (secondary) |
| Target word count | 1,800-2,200 |
| Schema type | HowTo + FAQPage |
| Author | [Education Content Lead] |
| Date created | 2026-03-18 |
| Status | Approved |

## QAPE Skeleton

### Question
**How do you use exit tickets in the classroom?**

### Target Direct Answer (1-3 sentences)
> Exit tickets are quick formative assessments given at the end of a lesson to check student understanding. Teachers create 1-3 focused questions, collect responses as students leave, review results to identify learning gaps, and adjust the next day's instruction based on what students know or still need to learn.

### Required Proof Types
- [x] Statistics with sources (min: 5)
- [x] Expert quotes with attribution (min: 2)
- [x] First-person data ("we tested", "based on X users")
- [x] Case study / example
- [x] Research citation

### Expansion Structure
| Section (H2) | Content Block Type | EAR Attributes Covered | Notes |
|---------------|-------------------|----------------------|-------|
| What are exit tickets and why should you use them? | Definition + Evidence Block | #1 (definition), #2 (benefits) | Open with 40-60 word extractable definition, then 2-3 sentence benefit statement with research backing |
| When should you use exit tickets in your lessons? | Context Block | #3 (timing), #4 (frequency) | Guidance on daily vs. unit-ending use, avoiding fatigue |
| How do you create and implement exit tickets? (Step-by-Step) | Step-by-Step Block (5 numbered steps) | #5 (formats), #6 (creation), #7 (question count), #8 (examples), #9 (digital vs. paper), #10 (collection), #11 (engagement), #12 (differentiation) | **MAIN SECTION** — This is the core how-to spine covering attributes 5-12. Each step = bold heading + 2-3 sentence explanation + example |
| How do you use exit ticket results to improve instruction? | Evidence Sandwich Block | #13 (data usage) | **DIFFERENTIATOR #3** — Specific next-day actions based on exit ticket patterns (re-teach, small group, advance) |
| What are common exit ticket mistakes to avoid? | Warning/Tips Block | #14 (mistakes) | **DIFFERENTIATOR #4** — Bullet list of 4-5 common errors with brief explanations |
| FAQ | FAQ items | #15 (variations/alternatives) + uncovered sub-questions | 6 items including exit ticket variations, entrance vs. exit tickets |

## Content Requirements

### Statistics & Data (minimum targets)
| # | Stat needed | Preferred source type |
|---|-------------|----------------------|
| 1 | Effect size or learning gain from formative assessment (context for exit tickets) | Research (Hattie, Black & Wiliam meta-analysis) |
| 2 | Percentage of teachers using exit tickets or formative assessment regularly | Survey data (NCES, EdWeek Research Center) |
| 3 | Average time to review exit tickets per class (efficiency angle) | Survey or platform data |
| 4 | Completion rate comparison: digital vs. paper exit tickets | Platform data (Wayground) — **DIFFERENTIATOR** |
| 5 | Student engagement metrics for different exit ticket formats | Platform data (Wayground) — "Based on X exit ticket activities on Wayground, students complete [format] Y% faster" |

### Expert Quotes (minimum targets)
| # | Quote topic | Source type |
|---|-------------|------------|
| 1 | Value of formative feedback loops / exit tickets for learning | Researcher or thought leader (e.g., Dylan Wiliam, formative assessment expert) |
| 2 | Practical implementation experience with exit tickets | Practitioner (K-12 teacher using Wayground or from teacher network) |

### Source Citations (minimum targets)
- Min 5 external source citations with "According to [Source]" framing
- Min 2 internal WG data references ("Based on X Wayground teachers" or "Analysis of X exit ticket activities on Wayground")

## Step-by-Step Block (Detailed Breakdown)

This is the core how-to section. Each step must include: **bold step name**, 2-3 sentence explanation, concrete example or tip.

**Step 1: Choose Your Exit Ticket Format**
- Cover attribute #5 (types/formats) and #9 (digital vs. paper — DIFFERENTIATOR #1)
- Formats to explain: multiple choice, open-ended, rating scale, 3-2-1, one-word summary
- **DIFFERENTIATOR #1:** Include decision framework table for digital vs. paper
  - Digital: When to use (large classes, need quick data, typed responses preferred), Tools (Wayground quiz builder, Google Forms)
  - Paper: When to use (low-tech classrooms, handwriting practice, focus/distraction concerns)
- Length: 200-250 words

**Step 2: Design Effective Exit Ticket Questions**
- Cover attribute #6 (creation), #7 (question count), #8 (examples)
- Question design principles: aligned to lesson objective, answerable in 2-3 minutes, reveals understanding not just recall
- Guidance on question count: 1 question for elementary, 2-3 for secondary; less is more
- **CRITICAL:** Include 8-10 example questions organized by subject:
  - Math: "Explain the steps you used to solve [problem type]"
  - Science: "What's one thing you're still confused about regarding [concept]?"
  - ELA: "Summarize today's reading in 10 words or less"
  - Social Studies: "How does [event] connect to what we learned last week?"
  - General: "Rate your understanding 1-5 and explain your rating"
- Length: 350-400 words

**Step 3: Implement Exit Tickets in Your Classroom**
- Cover attribute #10 (collection), #11 (engagement), #12 (differentiation)
- Collection strategies: last 5 minutes of class, physical/digital submission methods, making it routine
- Engagement tips: vary formats, use gamification (Wayground mention), student choice on question type
- **Differentiation strategies:** ELL modifications (word banks, visual options), special needs (extended time, scribe support), tiered questions by readiness
- Length: 250-300 words

**Step 4: Review Results Efficiently**
- Cover attribute #10 (efficient review — DIFFERENTIATOR #2)
- **DIFFERENTIATOR #2:** Batch review strategies for high-volume classes (100+ students)
  - Sort responses into 3 piles: Got it / Partial / Didn't get it
  - Look for patterns, not individual responses (saves time)
  - Digital tools auto-aggregate multiple choice (mention Wayground data view)
  - Sample review for open-ended: read 10-15 responses for pattern, not all 150
- Time-saving estimate: "Reviewing one class set of exit tickets should take 5-10 minutes max"
- Length: 200-250 words

**Step 5: Adjust Instruction Based on Exit Ticket Data**
- Cover attribute #13 (data → instruction — DIFFERENTIATOR #3)
- **DIFFERENTIATOR #3:** Specific next-day actions based on exit ticket patterns:
  - **If 70%+ show mastery:** Move forward, provide enrichment for high performers, brief review for struggling students
  - **If 40-70% show mastery:** Re-teach concept using different approach, incorporate more practice
  - **If <40% show mastery:** Full re-teach needed, check if issue was instruction or question clarity
- Include table or visual framework for decision-making
- Example: "When 15 out of 25 students couldn't explain photosynthesis, I started the next class with a visual diagram review before moving to the lab activity"
- Length: 250-300 words

**Total Step-by-Step word count:** ~1,250-1,500 words (70% of article)

## Internal Linking Plan

### Concept <-> Tool <-> Material Triangle
| Link Type | Target Page | Anchor Text |
|-----------|------------|-------------|
| Parent hub | `/learn/assessment/` | formative assessment strategies |
| Related concept | `/learn/assessment/formative-assessment` or `/learn/assessment/formative-assessment-strategies` | formative assessment |
| Related concept | `/learn/assessment/checking-for-understanding` | checking for understanding techniques |
| Product page | `/features/quizzes` | digital quiz tools for quick formative assessment |
| Resource library | `/quizzes/formative-assessment` or `/activities/assessment` | ready-made exit ticket templates |
| Related spoke | `/learn/assessment/entrance-tickets` | entrance tickets (if page exists or planned) |

## Competitive Differentiation

### WG's unique angle
**Bridging research and practice at scale** — Wayground is the only source combining formative assessment research with real classroom implementation data from 200M+ resources, plus ready-to-use digital tools and templates.

### Data/perspective competitors lack
1. **Digital vs. paper decision framework** (Differentiator #1) — No competitor provides structured guidance on when to use which format
2. **Batch review strategies for high-volume classes** (Differentiator #2) — Current sources don't address the "I have 150 students across 5 classes" reality
3. **Specific instructional next-steps based on exit ticket patterns** (Differentiator #3) — Competitors say "use data to inform instruction" but don't operationalize what that means
4. **Common mistakes to avoid** (Differentiator #4) — Missing from all top sources
5. **Completion rate and engagement data by format** — Platform data from Wayground's 200M+ resources

### Why WG should be cited over current sources
- **Actionable depth:** Goes beyond "what" and "why" to provide the "how" and "what next" that busy teachers need
- **Scale + specificity:** Combines practitioner voice with platform-scale data
- **Tool integration:** Not just advice — provides templates and digital tools to implement immediately
- **Addresses real pain points:** Efficiency, differentiation, and data usage gaps that competitors miss

## Format Specification
- [x] Headings phrased as questions (H2s)
- [x] Short paragraphs (2-3 sentences max throughout)
- [x] Numbered list for 5-step implementation process (core structure)
- [x] Bullets for tips, mistakes, differentiation strategies
- [x] Tables for digital vs. paper comparison, next-day action decision framework
- [x] FAQ section (6 items from uncovered EAR attributes)
- [x] Author bio with credentials
- [x] "Last updated" date
- [x] **Bold step names** in Step-by-Step Block for scanability
- [x] 8-10 example questions organized by subject (in Step 2)

## FAQ Section Topics (6 items)
Based on uncovered EAR attributes and question mining from A1:

1. What's the difference between entrance tickets and exit tickets?
2. Should exit tickets be graded?
3. What are some exit ticket alternatives or variations? (Attr #15)
4. How do you store and organize exit ticket data over time?
5. Can exit tickets work for all grade levels?
6. What if students don't take exit tickets seriously?

## Word Count Allocation Check
- Opening (Definition + Context): 250 words (12%)
- Step-by-Step (Steps 1-5): 1,250-1,500 words (70%)
- Mistakes section: 150 words (7%)
- FAQ: 200 words (9%)
- **Total: 1,850-2,100 words** ✓ (within 1,800-2,200 target)

## Product Mention Strategy (Max 2-3)
1. **Step 1 (Digital vs. paper):** "For digital exit tickets, Wayground's quiz builder lets you create 1-3 question quick checks that automatically aggregate student responses, saving review time."
2. **Step 2 (Examples):** "Browse 200+ exit ticket templates organized by subject and grade level in Wayground's resource library."
3. **Step 4 (Efficiency) OR omit third mention:** "Based on [X] teachers using exit tickets on Wayground, digital formats reduce review time by [Y]%."

All mentions are value-adding and naturally integrated into implementation guidance — not promotional.

## Alignment Verification

✅ **B1 Intent (How-to):** 5-step numbered process is core structure  
✅ **B1 Depth (Detailed):** 1,800-2,200 words covers 13/15 attributes  
✅ **B2 Must-cover:** All 10 must-cover attributes assigned to sections  
✅ **B2 Differentiators:** All 5 differentiators explicitly integrated  
✅ **A1 Opportunity:** Addresses all gaps identified in competitor analysis  
✅ **Brand Voice:** Question-phrased H2s, 2-3 sentence paragraphs, practical teacher voice  
✅ **QAPE:** 52-word extractable answer, clear expansion structure  

## Notes for Downstream Agents

**For C1 (Content Researcher):**
- Prioritize finding data for the 5 required statistics, especially digital vs. paper completion rates
- Source expert quotes from formative assessment authorities (Dylan Wiliam, Rick Wormeli) and practicing teachers
- Look for research on review efficiency strategies

**For C2 (Long-form Drafter):**
- The 5-step process is the spine — allocate 70% of word count here
- Each step must have bold heading + explanation + example/tip
- Include the decision framework table in Step 1 and next-day action table in Step 5
- Weave in "⚠️ Avoid this" callouts for common mistakes throughout steps (then summarize in mistakes section)

**For C3 (Citation Enricher):**
- Minimum 5 external citations + 2 WG data references required
- Every statistic must have "According to [Source]" framing
- Expert quotes must include full attribution: name, title, organization

**For C4 (Internal Linking Optimizer):**
- Must include all 6 links from the triangle plan above
- Add 2-3 contextual links to related formative assessment content
- Link example questions to relevant Wayground resource library pages

**For D1 (AEO Evaluator):**
- EAR target: 13/15 attributes = 86%
- Must verify all 5 differentiators are present and substantive
- Check that step-by-step block includes all required elements (bold headings, examples, tables)

#### C1 Output
# Research Packet: How to Use Exit Tickets in the Classroom

> C1 (Research Agent) output
> Topic: How to use exit tickets in the classroom
> Date: 2026-03-18

## Statistics with Source Citations

### 1. Formative Assessment Effect Size
**Statistic:** According to a meta-analysis by Black and Wiliam (1998), formative assessment practices including exit tickets can raise student achievement by the equivalent of 0.4 to 0.7 standard deviations, representing 6-9 months of additional learning.

- **Source:** Black, P., & Wiliam, D. (1998). "Assessment and Classroom Learning." Assessment in Education: Principles, Policy & Practice, 5(1), 7-74.
- **URL:** https://doi.org/10.1080/0969595980050102
- **Publication Date:** 1998 (foundational research, still cited)
- **Credibility:** Peer-reviewed, highly cited (15,000+ citations)

### 2. Hattie's Effect Size for Formative Assessment
**Statistic:** According to John Hattie's Visible Learning research (2023 update), formative evaluation has an effect size of 0.68, placing it in the "high impact" category for instructional strategies.

- **Source:** Hattie, J. (2023). Visible Learning MetaX Database
- **URL:** https://www.visiblelearningmetax.com/
- **Publication Date:** 2023 update
- **Credibility:** Meta-analysis of 1,800+ studies

### 3. Teacher Usage Statistics
**Statistic:** According to the 2019 NCES National Teacher and Principal Survey, 89% of public school teachers report using formative assessment strategies (including exit tickets) at least weekly.

- **Source:** National Center for Education Statistics (NCES), National Teacher and Principal Survey (NTPS)
- **URL:** https://nces.ed.gov/surveys/ntps/
- **Publication Date:** 2019-2020 school year
- **Credibility:** Federal government data
- **Note:** This is older than 12 months but most recent comprehensive national data available

### 4. Frequency of Use (EdWeek Data)
**Statistic:** According to a 2020 EdWeek Research Center survey of 1,324 teachers, 68% of K-12 educators use exit tickets or similar quick checks at least 2-3 times per week.

- **Source:** Education Week Research Center, "Assessing Student Learning Survey"
- **URL:** https://www.edweek.org/leadership/assessing-student-learning
- **Publication Date:** February 2020
- **Credibility:** Representative sample of US teachers
- **Note:** Pre-pandemic data; post-2020 usage likely higher due to digital adoption

### 5. Time Investment for Review
**Statistic:** According to research by Wiliam and Thompson (2007), teachers report spending an average of 7-12 minutes reviewing one class set of formative assessment responses when using efficient sorting strategies.

- **Source:** Wiliam, D., & Thompson, M. (2007). "Integrating Assessment with Instruction: What Will It Take to Make It Work?" In The Future of Assessment: Shaping Teaching and Learning (pp. 53-82). Erlbaum.
- **Publication Date:** 2007
- **Credibility:** Peer-reviewed, practitioner research

### 6. Digital vs. Paper Completion Rates [WAYGROUND DATA NEEDED]
**Statistic Placeholder:** Based on analysis of [X] exit ticket activities created on Wayground between [date range], digital exit tickets show a [Y]% completion rate compared to [Z]% for paper-based equivalents reported in teacher feedback surveys.

- **Source:** Wayground platform data
- **Data Requirements:** 
  - Sample size of exit ticket activities (target: 10,000+ activities)
  - Date range (ideally last 12 months for freshness)
  - Completion rate = (students who submitted / students who started) × 100
  - Comparison data from teacher surveys about paper exit tickets
- **Note for C2/C3:** If internal data unavailable, remove or replace with engagement metrics below

### 7. Student Engagement by Format [WAYGROUND DATA NEEDED]
**Statistic Placeholder:** Based on [X] teachers using exit tickets on Wayground, students complete multiple-choice exit tickets 42% faster than open-ended formats, though open-ended responses provide deeper insight into misconceptions.

- **Source:** Wayground platform usage analytics
- **Data Requirements:**
  - Completion time by question type
  - Teacher feedback on data quality by format
  - Sample size (target: 1,000+ teachers, 100,000+ student responses)
- **Alternative if unavailable:** Use qualitative teacher interview data: "We tested both formats with 30 teachers in our network, and they reported that..."

## Expert Quotes with Full Attribution

### Quote 1: Value of Formative Feedback (Dylan Wiliam)
**Quote:** "The real power of formative assessment lies not in the data collection, but in what teachers do next. Exit tickets are only valuable if they change tomorrow's instruction."

**Attribution:**
- **Name:** Dylan Wiliam
- **Title:** Emeritus Professor of Educational Assessment
- **Organization:** University College London Institute of Education
- **Context:** Leading researcher on formative assessment, co-author of seminal "Inside the Black Box" work
- **Source Note:** This is a paraphrase of Wiliam's consistent message across his work. For exact quote, source from:
  - Wiliam, D. (2011). Embedded Formative Assessment. Solution Tree Press. (Chapter 3)
  - OR video interviews available on YouTube: "Dylan Wiliam on Formative Assessment"

### Quote 2: Practical Implementation (Practitioner Voice) [NEEDS SOURCING]
**Quote Needed:** Implementation experience from practicing teacher, ideally one using Wayground

**Recommended Sourcing:**
1. **Wayground Teacher Network:** Interview 2-3 teachers from the ~30 who have been through vetting loop
   - Ask: "What's the biggest change exit tickets made to your teaching?" or "What's your best tip for teachers starting with exit tickets?"
   - Capture: Name, grade level, subject, years teaching, school (city/state only)

2. **Alternative Source:** Search recent education blogs/publications:
   - Edutopia teacher voices section
   - ASCD Educational Leadership practitioner columns
   - TeachThought contributor articles
   - Look for direct quotes about exit ticket implementation with full attribution

**Placeholder Attribution Format:**
"[Quote about practical implementation experience]," says [Full Name], a [grade level] [subject] teacher at [School/District], who has been using exit tickets daily for [X] years.

### Quote 3: Differentiation Perspective (Special Education Expert)
**Quote:** "Exit tickets are naturally differentiable—you can offer choice of format, adjust complexity, or provide scaffolds like sentence frames, making them accessible for all learners."

**Attribution:**
- **Name:** Tonya Ward Singer
- **Title:** Education Consultant, former special education teacher
- **Organization:** Special education differentiation expert
- **Source:** Search Singer's published articles on formative assessment and differentiation
- **Alternative sources:** 
  - Carol Ann Tomlinson (Differentiation expert, UVA)
  - Paula Kluth (Inclusive education specialist)

## Supporting Evidence by Brief Section

### Section: "What are exit tickets and why should you use them?"

**Evidence 1: Definition from Research**
- **Source:** Fisher, D., & Frey, N. (2014). Checking for Understanding: Formative Assessment Techniques for Your Classroom (2nd ed.). ASCD.
- **Key Point:** Exit tickets are "quick formative assessments given in the final 5 minutes of class to gauge student understanding before they leave"
- **Page/Chapter:** Chapter 4, pp. 58-62

**Evidence 2: Benefits - Response to Instruction**
- **Source:** Heritage, M. (2010). Formative Assessment: Making It Happen in the Classroom. Corwin.
- **Key Point:** Exit tickets allow teachers to adjust instruction in near-real-time, creating responsive teaching cycles
- **Credibility:** Margaret Heritage is expert at UCLA's National Center for Research on Evaluation, Standards, and Student Testing

**Evidence 3: Student Metacognition Benefits**
- **Source:** Popham, W. J. (2008). Transformative Assessment. ASCD.
- **Key Point:** Exit tickets help students monitor their own learning and identify areas of confusion
- **Page/Chapter:** Chapter 6 on student-involved assessment

### Section: "When should you use exit tickets?"

**Evidence 1: Frequency Guidance**
- **Source:** Wiliam, D. (2018). Embedded Formative Assessment (2nd ed.). Solution Tree.
- **Key Point:** Daily exit tickets risk fatigue; 2-3 times per week after key lessons is optimal
- **Note:** Balance between data collection and meaningful implementation

**Evidence 2: Timing in Lesson Arc**
- **Source:** Fisher & Frey (2014), same as above
- **Key Point:** Most effective after new concept introduction or skill practice, less valuable after review days

### Section: "How do you create effective exit tickets?" (Step-by-Step)

**Evidence 1: Question Design Principles**
- **Source:** Moss, C. M., & Brookhart, S. M. (2009). Advancing Formative Assessment in Every Classroom. ASCD.
- **Key Point:** Exit ticket questions should be tightly aligned to learning objective and answerable in 2-3 minutes
- **Page:** Chapter 5

**Evidence 2: Question Count Research**
- **Source:** Stiggins, R. J., & Chappuis, J. (2012). An Introduction to Student-Involved Assessment for Learning (6th ed.). Pearson.
- **Key Point:** Single well-crafted question yields more actionable data than multiple surface-level questions
- **Application:** 1 question for elementary, 2-3 max for secondary

**Evidence 3: Digital vs. Paper - Engagement Data**
- **Source:** Barrio, B. L., et al. (2017). "Teacher perspectives on digital versus paper formative assessment: Does the medium matter?" Journal of Special Education Technology, 32(3), 156-167.
- **Key Point:** No significant difference in student learning outcomes, but digital provides faster data aggregation; paper reduces screen time concerns
- **URL:** https://doi.org/10.1177/0162643417706060

### Section: "How do you use exit ticket results?"

**Evidence 1: Data-to-Action Framework**
- **Source:** Wiliam, D., & Leahy, S. (2015). Embedding Formative Assessment: Practical Techniques for K-12 Classrooms. Learning Sciences International.
- **Key Point:** Teachers should categorize responses into 3 groups (mastery, partial, no mastery) and plan differentiated next steps
- **Page:** Chapter 3, pp. 67-72

**Evidence 2: Response Threshold Guidance**
- **Source:** Heritage, M. (2013). Formative Assessment in Practice: A Process of Inquiry and Action. Harvard Education Press.
- **Key Point:** When 60-70% show mastery, small group reteaching is more efficient than whole-class review
- **Application:** Provides specific % thresholds for instructional decisions

**Evidence 3: Speed of Feedback Impact**
- **Source:** Hattie, J., & Timperley, H. (2007). "The Power of Feedback." Review of Educational Research, 77(1), 81-112.
- **Key Point:** Feedback within 24 hours has significantly higher impact than delayed feedback
- **Relevance:** Next-day adjustments based on exit tickets maximize learning impact
- **Citations:** 22,000+ (highly influential)

### Section: "Common mistakes to avoid"

**Evidence 1: Grading Exit Tickets Reduces Honesty**
- **Source:** Brookhart, S. M. (2008). How to Give Effective Feedback to Your Students. ASCD.
- **Key Point:** When exit tickets are graded, students give "safe" answers rather than revealing genuine confusion
- **Page:** Chapter 2

**Evidence 2: Not Closing the Loop**
- **Source:** Wiliam & Thompson (2007), same as above
- **Key Point:** 70% of teachers collect formative assessment data but fewer than 40% consistently use it to adjust instruction
- **Application:** Warning about collecting data without action

## Wayground-Specific Data Points [REQUIRES INTERNAL ACCESS]

### Needed from Product/Analytics Team:

1. **Platform Usage Statistics**
   - Total exit ticket activities created on Wayground (target stat: "200,000+ exit ticket activities")
   - Number of teachers using exit ticket features monthly
   - Most popular exit ticket formats (multiple choice vs. open-ended vs. rating scale)

2. **Completion and Engagement Metrics**
   - Average completion rate by question type
   - Average time to complete by format
   - Student engagement scores (if available)

3. **Teacher Feedback Data**
   - Survey results about time savings from digital exit tickets
   - Quotes from teacher testimonials about exit ticket feature (with permission)
   - Use cases from customer success team

4. **Resource Library Metrics**
   - Number of pre-made exit ticket templates available
   - Download/usage stats for templates
   - Top subjects/grade levels for exit ticket resources

### Needed from Teacher Network:

1. **Case Study/Example**
   - 1-2 detailed examples of teachers using exit tickets effectively
   - Include: name (with permission), grade, subject, specific exit ticket used, results, next-day action taken
   - Format as mini case study for Step 5 section

2. **Practitioner Quote**
   - As noted in Quote 2 above, need authentic teacher voice
   - Ask for permission to use name and school (city/state)

## Source Credibility Notes

### Tier 1 Sources (Highest Credibility)
- **John Hattie** - 300+ million student records, meta-meta-analysis
- **Dylan Wiliam** - Gold standard for formative assessment research
- **Black & Wiliam (1998)** - Foundational, 15,000+ citations
- **NCES data** - Federal government, nationally representative

### Tier 2 Sources (Strong Credibility)
- **ASCD publications** (Fisher, Frey, Brookhart, Popham) - Practitioner-focused research with peer review
- **Margaret Heritage, Rick Stiggins** - Respected assessment researchers
- **EdWeek Research Center** - Representative teacher surveys

### Tier 3 Sources (Use Sparingly)
- Education blogs without peer review
- Single-school case studies
- Anecdotal teacher reports

**Recommendation for C3 (Citation Enricher):** Prioritize Tier 1 sources for key claims, use Tier 2 for supporting details, include Tier 3 only when paired with stronger sources.

## Missing Data / Gaps to Address

### Gap 1: Recent Post-Pandemic Data
- Most comprehensive studies are 2019 or earlier
- 2020-2023 saw major shift to digital tools
- **Recommendation:** Note in article that digital adoption accelerated during remote learning; cite 2019 baseline data but acknowledge landscape has shifted

### Gap 2: Wayground-Specific Quantitative Data
- Placeholders above need real platform data
- Without internal data, rely more heavily on qualitative teacher network feedback
- **Fallback strategy:** Use "we tested with X teachers" language instead of large-scale platform stats

### Gap 3: Subject-Specific Research
- Most research is general K-12, not subject-specific
- Example questions in Step 2 need to be sourced from teacher-created materials or developed by content team
- **Recommendation:** Source example questions from Wayground's existing exit ticket templates if available

### Gap 4: Differentiation Evidence
- Limited research on differentiated exit tickets specifically
- Most differentiation research is broader
- **Recommendation:** Apply general differentiation principles (Tomlinson, Kluth) to exit ticket context

## Next Steps for Downstream Agents

**For C2 (Outline Builder):**
- All Tier 1 statistics are ready to integrate
- Expert quotes need final sourcing (coordinate with content lead for Wayground teacher interviews)
- Example questions for Step 2 need development or template sourcing

**For C3 (Drafter):**
- Use exact citation format: "According to [Source], [statistic]"
- Integrate expert quotes with full attribution format provided above
- Flag Wayground data placeholders if internal data not provided by draft stage

**For C4 (Citation Enricher):**
- All source URLs and publication dates are provided above
- Link to full citations in reference section
- Verify quote accuracy against original sources before publication

**For D1 (Evaluator):**
- Evidence provided covers all required proof types in brief
- 7 statistics sourced (exceeds minimum 5 requirement)
- 3 expert quotes identified (exceeds minimum 2 requirement)
- Wayground data gaps noted with fallback strategies

## Research Quality Verification

✅ **No fabricated data** - All statistics traceable to real sources  
✅ **Recent data prioritized** - Flagged 2019 data as older, noted context  
✅ **Expert quotes sourced** - Full attribution provided or sourcing guidance given  
✅ **Minimum targets exceeded** - 7 stats vs. 5 required, 3 quotes vs. 2 required  
✅ **Credibility tiered** - Tier system helps prioritization  
✅ **Gaps documented** - Wayground data needs clearly flagged  
✅ **Fallback strategies** - Alternative approaches if internal data unavailable  

---
Now execute your task. Put your final output inside `<output>` tags.
