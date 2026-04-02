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

**Topic:** Turn and Talk: A Quick Guide to Increasing Student Engagement

### Upstream Agent Outputs

#### B3 Output

# Content Brief: Turn and Talk — A Quick Guide to Increasing Student Engagement

> Stage 2 output — produced by B3 (Content Brief Generator)
> Source dossier: topic-dossier-turn-and-talk.md (compiled from A1 + A2 + B1 + B2)

## Metadata
| Field | Value |
|-------|-------|
| Topic | Turn and Talk: A Quick Guide to Increasing Student Engagement |
| Target URL | `/learn/engagement/turn-and-talk` |
| Intent type | How-to (primary) / Informational (secondary) |
| Target word count | 2,800–3,500 words |
| Schema type | FAQPage + HowTo |
| Author | [Education Content Lead — educator credentials required; Ed.D. or classroom practitioner preferred] |
| Date created | 2026-03-20 |
| Status | Draft |

---

## QAPE Skeleton

### Question
**What is the "Turn and Talk" strategy and how does it increase student engagement?**

### Target Direct Answer (1-3 sentences)
> Turn and Talk is a structured discussion strategy where teachers pause instruction and ask students to share thinking with a nearby partner for 1–4 minutes before resuming whole-class learning. It boosts engagement by activating every student simultaneously — rather than waiting for one hand to raise — and builds the verbal processing skills students need to deepen comprehension. Research on peer interaction shows it supports both language development and content retention across K-12 grade levels.

*(Word count: 58 — at the upper edge of the 40-60 target; trim one clause if the writer needs sub-55. This block must appear within the first 200 words of the article as a standalone, extractable paragraph.)*

### Required Proof Types
- [x] Statistics with sources (min: 5)
- [x] Expert quotes with attribution (min: 2)
- [x] First-person data ("we tested", "based on X users") — include if UXR or teacher community data available; flag as [DATA NEEDED] if not confirmed
- [ ] Case study / example — use a classroom scenario vignette (can be illustrative, clearly labeled as example)
- [x] Research citation (min: 3 peer-reviewed or institutional sources)

---

### Expansion Structure

| # | Section (H2 — question-phrased) | Content Block Type | EAR Attributes Covered | Word Count Target | Notes |
|---|----------------------------------|-------------------|----------------------|-------------------|-------|
| 1 | *[Above-the-fold, no H2]* — Definition block | Definition Block | #1 (what is turn and talk) | 80–100 words | Must be first content in article; standalone extractable paragraph; no heading needed — let it open cold |
| 2 | **How does Turn and Talk differ from Think-Pair-Share and Cold Calling?** | Comparison Table Block | #2 (comparison to TPS) | 200–300 words + table | 3-column table (Turn-and-Talk / Think-Pair-Share / Cold Calling); rows: Purpose, Duration, Structure, Accountability, Best For, Risk; brief prose before and after table |
| 3 | **How do you run a Turn and Talk? A step-by-step protocol** | Step-by-Step Block (HowTo schema) | #3 (teacher moves), #5 (timing) | 400–500 words | Numbered 5-7 steps; each step: bold step name + teacher action + expected student behavior + timing range; incorporate the Duration Guide sub-table inside this section OR as its own H3 |
| 4 | **When in a lesson should you use Turn and Talk?** | Decision Framework Block | #4 (lesson placement) | 200–300 words + table | Lesson-placement table: Phase (warm-up / mid-lesson / exit) × Purpose (activate / process / consolidate) × Prompt type; brief prose framing before table |
| 5 | **What sentence starters help students have better Turn and Talk conversations?** | Resource Block (tables) | #6 (sentence starters) | 350–450 words + tables | Flagship shareability asset; two tables — Table A: by subject area (ELA / Math / Science / Social Studies) with 3 starters each; Table B: by grade band (K-2 / 3-5 / 6-8 / 9-12) with adapted language; brief intro paragraph; signal to teachers these are copy-paste ready |
| 6 | **How do you adapt Turn and Talk for ELLs, shy students, and students with IEPs?** | Adaptation Block | #7 (ELL adaptations), #8 (IEP/shy) | 350–450 words | Three named sub-sections (H3): ELLs (sentence frame scaffold + L1 partner option + vocabulary pre-teach cue); Shy/introverted students (written response option + structured wait time + partner pre-assignment); Students with IEPs/504s (UDL framing + AAC/nonverbal options + extended processing time); name-check UDL principles once |
| 7 | **How do you use Turn and Talk in digital and hybrid classrooms?** | Digital Implementation Block | #9 (digital/hybrid) | 300–400 words | Three formats: synchronous virtual (breakout rooms, 2-min timer, structured re-entry), hybrid (in-room + digital partner pairing), async (written chat prompt + recorded voice response); **Wayground Team Mode product anchor goes here** — one paragraph, direct link, framed as a ready-made digital analog; this is the only product mention |
| 8 | **What does research say about why Turn and Talk works?** | Evidence Sandwich Block | #10 (research) | 200–300 words | Lead with Vygotsky ZPD framing (1 sentence), then 2 empirical citations with effect direction; Michaels, O'Connor & Resnick on accountable talk; Webb on peer interaction and learning gains; "According to [Source]" framing throughout; close with a practitioner quote |
| 9 | **What are common Turn and Talk mistakes — and how do you fix them?** | Mistake → Fix Block | #11 (common mistakes) | 250–350 words | 5–6 "Mistake → Fix" pairs in a two-column table or bulleted pairs; examples: students off-task → structured prompt required / one partner dominates → assign roles (speaker/recorder) / timing too long → 90-second max for warm-up / no accountability → cold-call one pair to share after; high shareability; include a brief intro sentence |
| 10 | **How does Turn and Talk look different across grade levels?** | Grade-Band Table | #12 (grade differentiation) | 150–200 words + table | Optional if word count is tight; quick table: Grade Band × What It Looks Like × Prompt Complexity × Partner Structure; K-2 (shoulder partner, picture prompts), 3-5 (sentence frame scaffolds), 6-8 (evidence-based prompts), 9-12 (structured academic controversy variant) |
| 11 | **Frequently Asked Questions** | FAQ Block | Variant phrasings from A1; residual EAR attributes | 300–400 words | 5–6 Q&A items; question-phrased; each answer 40-60 words (AI extraction format); see FAQ spec below |

---

## Content Requirements

### Statistics & Data (minimum targets)

| # | Stat needed | Preferred source type | Fallback if unavailable |
|---|-------------|----------------------|------------------------|
| 1 | Effect size of structured peer discussion on student achievement (e.g., Hattie meta-analysis or comparable) | Peer-reviewed meta-analysis | Report direction: "research consistently shows positive effect sizes for structured peer talk on content retention" |
| 2 | % of students who engage verbally during whole-class discussion vs. turn-and-talk format (participation equity data) | Research study or classroom survey | Estimate from instructional design literature — "in a class of 30, only 1 student speaks at a time in whole-class discussion; turn-and-talk activates all 15 pairs simultaneously" |
| 3 | Learning gains for ELL students when given L1/L2 scaffolded discussion opportunities | NICHD or bilingual education research | Colorín Colorado or TESOL Journal citation |
| 4 | Wait time research — increased response quality with 3+ seconds of processing before speaking (Rowe, 1986 or comparable) | Classic educational research | "According to research on wait time, students who are given 3+ seconds before responding produce longer, more accurate answers" |
| 5 | Engagement or participation rate data from Wayground platform (collaborative activity completion rates, Team Mode usage) | **[DATA NEEDED — internal WG platform data; flag for UXR team]** | Omit and replace with teacher community quote if unavailable |

### Expert Quotes (minimum targets)

| # | Quote topic | Source type | Suggested attribution format |
|---|-------------|------------|------------------------------|
| 1 | Why structured peer discussion (accountable talk) improves learning — cognitive rationale | Researcher; ideal: Sarah Michaels or Lauren Resnick (accountable talk), Noreen Webb (peer interaction), or Dylan Wiliam (formative assessment and discussion) | "[Quote]," says [Name], [Title] at [Institution] |
| 2 | Practical classroom experience using turn-and-talk — what makes it work | K-12 practitioner teacher; ideal: member of Wayground's ~30-teacher vetting network with name + school attribution | "[Quote]," says [Name], [Grade] teacher at [School], [City] |
| 3 | (Optional) ELL-specific benefit of structured partner talk | ELL specialist or bilingual educator | Same attribution format |

### Source Citations (minimum targets)
- **Min 5 external source citations** with "According to [Source]" framing
- **Min 2 internal WG data references** ("Based on Wayground's platform data..." or "In our teacher community..." — use only if UXR data is confirmed; otherwise replace with teacher quote)
- **Required citations to include:**
  - Vygotsky (1978) — Zone of Proximal Development — for research backing section
  - Michaels, O'Connor & Resnick — accountable talk framework — for research backing section
  - Webb, N.M. — peer interaction and learning — for research backing section
  - Rowe (1986) — wait time research — for timing/step section
  - At minimum one .org source (Edutopia, Understood.org, or Reading Rockets) — for trust signaling

---

## Internal Linking Plan

### Concept ↔ Tool ↔ Material Triangle

| Link Type | Target Page | Anchor Text | Notes |
|-----------|------------|-------------|-------|
| Parent hub | `/learn/engagement/` | student engagement strategies | Contextualizes T&T within a broader engagement cluster |
| Related concept (comparison) | `/learn/strategies/think-pair-share` | think-pair-share strategy | Link bidirectionally if page exists; if not, flag for creation |
| Related concept (sibling) | `/learn/strategies/collaborative-learning` | collaborative learning in the classroom | High-authority internal link target |
| Related concept (sibling) | `/learn/engagement/cold-calling-alternatives` | alternatives to cold calling | Connects to comparison section (Attr 2); creates spoke for the cluster |
| Product page (Wayground anchor) | `/features/team-mode` or equivalent Team Mode URL | Wayground's Team Mode activities | Used exclusively in the digital implementation section; natural product connection |
| Resource library | `/activities/discussion` or `/activities/collaborative` | ready-made discussion activities | Provides immediate CTA after digital section; verify URL before draft |
| Related spoke (future) | `/learn/engagement/exit-tickets` | exit ticket strategies | Reference in the "lesson placement" section (Attr 4) — when T&T works as an exit ramp |
| External trust bridge (earned, not CTA) | `edutopia.org` | [not a CTA — link-earning target; outreach recommended post-publish] | Highest leverage backlink opportunity; flag for content team |

---

## Competitive Differentiation

- **WG's unique angle:** Wayground is the first platform to publish a single resource covering all six under-served attributes simultaneously — timing guidance, copy-paste sentence starters, ELL scaffold protocol, IEP/UDL adaptations, digital implementation, and common mistakes. No competitor combines these in one article.

- **Data/perspective competitors lack:**
  - Specific minute-range guidance per lesson phase (Attrs 5) — entirely absent from all 6 top-cited sources; first-mover advantage
  - A structured ELL protocol with L1→L2 progression framing (beyond Colorín Colorado's narrow bilingual lens)
  - A digital/hybrid implementation guide anchored to a real product (Wayground Team Mode) that teachers can click through and use immediately
  - If UXR data exists: "We tested this with [X] teachers in Wayground's educator community" is a trust signal no competitor can replicate

- **Why WG should be cited over current sources:**
  - Edutopia covers 1/12 EAR attributes; Cult of Pedagogy covers 4/12; no source exceeds 4/12. Wayground's article targets 11/12.
  - The three most-citable passages — Duration Guide table, sentence starters table, digital implementation protocol — do not exist anywhere in the current citation landscape.
  - WG's practitioner-voice author with educator credentials + teacher community quotes creates the E-E-A-T profile AI engines favor for how-to strategy content.

---

## Format Specification

- [x] **Extractable definition block in first 200 words** — standalone paragraph, no H2, 40-60 words, AI snippet target
- [x] **Headings phrased as questions (H2s)** — all 9 main sections
- [x] **Short paragraphs (2-3 sentences max)** — enforced throughout; no paragraph exceeds 4 sentences
- [x] **Numbered steps** for the implementation protocol (Step 1–Step N format with bolded step names)
- [x] **Tables for all structured data:**
  - Comparison table: T&T vs. Think-Pair-Share vs. Cold Calling (3 columns, 6+ rows)
  - Duration Guide table: Lesson phase × Duration range × Prompt type
  - Lesson placement table: Phase × Purpose × Trigger condition
  - Sentence starters tables: by subject and by grade band
  - Grade-band differentiation table (if word count allows)
  - Mistake → Fix pairs (table or formatted bullets)
- [x] **FAQ section (5-6 items)** — question-phrased, each answer 40-60 words; covers A1 variant phrasings
- [x] **Author bio with credentials** — Ed.D., current or former K-12 classroom practitioner preferred
- [x] **"Last updated" date** — include in byline
- [x] **HowTo schema markup** — implementation steps qualify; combine with FAQPage schema for FAQ section
- [x] **One product mention maximum** — Wayground Team Mode, in the digital implementation section only, value-framed ("Wayground's Team Mode replicates the partner-discussion structure of Turn and Talk in a digital setting, letting students respond to each other's answers in real time")

---

## FAQ Section Specification

*Each FAQ answer must be 40-60 words — optimized for AI extraction. Question text matches variant phrasings from A1.*

| # | Question | EAR Attribute | Answer focus |
|---|----------|---------------|-------------|
| 1 | How do you do a "turn and talk" in the classroom? | #3 (steps) | Compressed 3-step version: pose the question → give processing time → signal partner talk → call back the group; link to full protocol section above |
| 2 | What are the benefits of Turn and Talk for students? | #10 (research) | Engagement + verbal processing + comprehension; cite one research direction; 40-55 words |
| 3 | How is Turn and Talk different from Think-Pair-Share? | #2 (comparison) | Core distinction: T&T is shorter and more spontaneous; TPS adds an individual writing step and a structured share-out; reference comparison table above |
| 4 | When should teachers use Turn and Talk during a lesson? | #4 (lesson placement) | Three-phase answer: warm-up activation / mid-lesson processing check / exit consolidation; reference placement table above |
| 5 | How do you make Turn and Talk work for English language learners or shy students? | #7, #8 (adaptations) | Sentence frames + L1 partner pairing for ELLs; written option + pre-assigned partners for shy students; reference full adaptation section above |
| 6 | (Optional) How long should a Turn and Talk last? | #5 (timing) | 90 seconds for warm-up, 2-3 minutes for mid-lesson processing, up to 4 minutes for exit consolidation; reference Duration Guide table above |

---

## B3 Flags and Downstream Notes

### For C1-C5 (Draft and Enrichment Agents)

1. **Do not fabricate WG platform statistics.** The UXR data point (Attr 5 stat target #5 in the data table) is flagged as [DATA NEEDED]. If not confirmed by the time drafting begins, replace with a teacher community quote or remove entirely. Do not invent a percentage.

2. **The sentence starters section (Attr 6) is the primary link-earning asset.** Treat it as a standalone resource: it should be scannable as a table, formatted for copy-paste, and cover all four core subject areas. Under-serving this section reduces shareability and backlink probability.

3. **The digital section (Attr 9) is the only Wayground anchor.** One paragraph. One link. Frame it as a tool recommendation from a knowledgeable colleague, not a sales pitch. If Team Mode is not the right product page, confirm the correct URL before drafting — do not link to a generic features page.

4. **The comparison table (Attr 2) must use exactly these three columns:** Turn-and-Talk, Think-Pair-Share, Cold Calling. ThoughtCo currently owns the TPS comparison sub-query loosely; a structured 3-column table takes that query away. Do not collapse to a 2-column table.

5. **Expert quote sourcing:** Aim for at least one real, named practitioner from Wayground's teacher network. A named teacher quote ("says Maria Chen, 4th grade teacher at Jefferson Elementary, Portland") carries more E-E-A-T signal than a generic "many teachers find..." framing.

### For D1 (AEO Evaluator)

- **Minimum PASS:** 9/12 EAR attributes covered at "Addressed" depth or better
- **Target PASS with distinction:** 11/12 at "Addressed" depth; Attrs 5, 6, 9 at "Deep"
- **Auto-ESCALATE condition:** If Attrs 5 (timing Duration Guide table) AND 9 (digital implementation section) are both absent or reduced to "Mentioned" depth — escalate regardless of overall score
- **Comparison table check:** Attr 2 must be a structured table with ≥3 columns; prose comparison does not score full credit
- **Product mention audit:** Verify exactly one Wayground product mention; escalate if zero (missed brand value) or more than one (brand voice violation)
- **Definition block check:** First 200 words must contain a standalone 40-60 word extractable paragraph; if buried or missing, flag for revision

#### C1 Output


#### C2 Output

# Article Outline: Turn and Talk — A Quick Guide to Increasing Student Engagement

> Produced by C2 (Outline Agent) | Stage 3a
> Source: B3 Content Brief | C1 Research Packet: **⚠️ NOT RECEIVED — outline built from B3 spec; C3 must flag if C1 research contradicts any placement below**

---

## Meta

| Field | Value |
|-------|-------|
| Target URL | `/learn/engagement/turn-and-talk` |
| H1 | What Is Turn and Talk — and How Does It Increase Student Engagement? |
| Intent | How-to (primary) / Informational (secondary) |
| Schema | FAQPage + HowTo |
| Target word count | 2,800–3,500 words |
| EAR attributes total | 12 |
| Must-cover (dedicated sections) | #1, #2, #3, #4, #5, #6, #7, #8, #9, #10 |
| FAQ / expansion | #11 (variant phrasings), #12 (grade diff) |

---

## Outline Structure

---

### BLOCK 0 — Definition Block (no heading, above fold)

| Element | Spec |
|---------|------|
| Block type | Definition Block |
| Word target | 80–100 words (first paragraph ~58 words extractable; balance in supporting sentence) |
| EAR attributes | #1 — What is Turn and Talk |
| Schema role | Likely extracted as AI direct answer / featured snippet |
| Placement rule | **Must appear within first 200 words; no H2 above it** |

**Content instructions for C3:**
- Open with the target direct answer from B3 QAPE (58-word extractable paragraph) — do not modify structure
- Follow immediately with one supporting sentence expanding on grade range applicability
- No heading. No intro sentence before the definition. Drop the reader straight in.
- This block functions as the article's "topic sentence" at scale

**Internal link:** No links in this block — keep it clean for extraction

**Stats to place here:** None — definition block must stand alone without citations (citation framing breaks extractability)

---

### SECTION 1 — H2: How Does Turn and Talk Differ from Think-Pair-Share and Cold Calling?

| Element | Spec |
|---------|------|
| Block type | Comparison Table Block |
| Word target | 200–300 words (including table) |
| EAR attributes | #2 — Comparison to Think-Pair-Share |
| H3s | None required |
| Schema role | FAQ candidate (Q3 maps here) |

**Heading:** `## How Does Turn and Talk Differ from Think-Pair-Share and Cold Calling?`

**Content instructions for C3:**
- Brief framing prose (2-3 sentences): establish why teachers mix up these three strategies and what the stakes are
- **3-column comparison table** (required — do not collapse to 2 columns per B3 flag):

| Row | Turn and Talk | Think-Pair-Share | Cold Calling |
|-----|---------------|-----------------|--------------|
| Purpose | | | |
| Duration | | | |
| Structure | | | |
| Accountability | | | |
| Best For | | | |
| Risk | | | |

- 1-2 sentences after table connecting back to the article: "For the rest of this guide, we focus on Turn and Talk — the fastest, lowest-lift version of the three."

**Internal links:**
- Anchor: "think-pair-share strategy" → `/learn/strategies/think-pair-share` (bidirectional if page exists; flag for creation if not)
- Anchor: "alternatives to cold calling" → `/learn/engagement/cold-calling-alternatives`

**Stats/quotes to place here:** None required; table is the authoritative element

---

### SECTION 2 — H2: How Do You Run a Turn and Talk? (Step-by-Step Protocol)

| Element | Spec |
|---------|------|
| Block type | Step-by-Step Block (HowTo schema) |
| Word target | 400–500 words |
| EAR attributes | #3 (teacher moves), #5 (timing) |
| H3s | `### Duration Guide: How Long Should Each Turn and Talk Last?` |
| Schema role | HowTo schema — step items map directly |

**Heading:** `## How Do You Run a Turn and Talk? A Step-by-Step Protocol`

**Content instructions for C3:**
- 1 sentence framing before the steps (keep short — don't bury steps)
- **5–7 numbered steps**, each formatted as:
  - **Bold step name** (e.g., **Step 1: Design a Focused Prompt**)
  - Teacher action (what the teacher does)
  - Expected student behavior (what students do)
  - Timing range (how long this step takes)
- Steps to cover: design prompt → display it visually → give think/processing time (Rowe wait time goes here) → signal partner talk → monitor pairs → signal return → cold-call one pair to share

**H3 — Duration Guide:**

`### Duration Guide: How Long Should a Turn and Talk Last?`

- Introduce the sub-table with 1 sentence
- **Duration Guide table:**

| Lesson Phase | Duration | Prompt Type | Purpose |
|-------------|----------|-------------|---------|
| Warm-up / activation | 90 seconds | Open recall or prediction prompt | Activate prior knowledge |
| Mid-lesson processing | 2–3 minutes | Comprehension or application prompt | Process new content |
| Exit consolidation | 3–4 minutes | Synthesis or reflection prompt | Consolidate learning |

- 1 closing sentence: "When in doubt, err shorter — 90 seconds of focused partner talk beats four minutes of drift."

**Stats to place here:**
- Rowe (1986) wait time stat — place inside Step 3 (think time step): "According to Mary Budd Rowe's foundational research on wait time, students who receive 3 or more seconds of processing time before speaking produce longer, more accurate answers."

**Quotes to place here:** Optional practitioner quote on timing — hold for C1 research confirmation

**Internal links:** None required in this section

---

### SECTION 3 — H2: When in a Lesson Should You Use Turn and Talk?

| Element | Spec |
|---------|------|
| Block type | Decision Framework Block |
| Word target | 200–300 words (including table) |
| EAR attributes | #4 — Lesson placement |
| H3s | None required |
| Schema role | FAQ candidate (Q4 maps here) |

**Heading:** `## When in a Lesson Should You Use Turn and Talk?`

**Content instructions for C3:**
- 2 sentences framing the three placement windows (warm-up / mid-lesson / exit)
- **Lesson placement table:**

| Lesson Phase | Purpose | Prompt Trigger | Example |
|-------------|---------|----------------|---------|
| Warm-up / before new content | Activate prior knowledge | Before introducing a concept | "Turn and tell your partner: what do you already know about photosynthesis?" |
| Mid-lesson / check for understanding | Process new content | After a key explanation or demo | "Turn and tell your partner: what's one thing that surprised you so far?" |
| Exit / consolidation | Consolidate and synthesize | Before dismissal or end of segment | "Turn and tell your partner: what's the most important thing you're taking away?" |

- 1-2 sentences after table: signal to the reader that timing matters and link to the Duration Guide above
- Optional: short callout referencing exit ticket connection

**Internal links:**
- Anchor: "exit ticket strategies" → `/learn/engagement/exit-tickets` (reference in prose, not table)

**Stats/quotes to place here:** None required — table carries the section

---

### SECTION 4 — H2: What Sentence Starters Help Students Have Better Turn and Talk Conversations?

| Element | Spec |
|---------|------|
| Block type | Resource Block (tables — flagship shareability asset) |
| Word target | 350–450 words (including both tables) |
| EAR attributes | #6 — Sentence starters |
| H3s | `### Sentence Starters by Subject Area` / `### Sentence Starters by Grade Band` |
| Schema role | High share / backlink target; extractable as resource |

**Heading:** `## What Sentence Starters Help Students Have Better Turn and Talk Conversations?`

**Content instructions for C3:**
- 2-sentence intro: explain why sentence starters matter (reduce hesitation, scaffold academic language) and signal that these tables are copy-paste ready
- ⚠️ **This is the primary link-earning asset** — do not under-serve it; tables must be complete

**H3: Sentence Starters by Subject Area**

`### Sentence Starters by Subject Area`

| Subject Area | Sentence Starter 1 | Sentence Starter 2 | Sentence Starter 3 |
|-------------|-------------------|--------------------|-------------------|
| ELA / Reading | | | |
| Math | | | |
| Science | | | |
| Social Studies | | | |

*(C3: fill starters using C1 research + domain knowledge; each starter should be a complete sentence stem, e.g., "I think the author meant… because…")*

**H3: Sentence Starters by Grade Band**

`### Sentence Starters by Grade Band`

| Grade Band | Adapted Sentence Starter | Complexity Level | Notes |
|-----------|--------------------------|-----------------|-------|
| K–2 | | Simple / visual anchor | Can pair with picture prompt |
| 3–5 | | Scaffolded | Sentence frame format |
| 6–8 | | Evidence-based | "According to the text…" framing |
| 9–12 | | Academic controversy | Structured academic disagreement variant |

- 1 closing sentence after second table: "Post these at the front of the room or embed them in your slide deck — students refer to them without prompting after a few weeks."

**Stats/quotes to place here:** Optional — if C1 surface ELL language acquisition data on scaffolded sentence frames, place here with "According to [Source]" framing

**Internal links:** None required in this section

---

### SECTION 5 — H2: How Do You Adapt Turn and Talk for ELLs, Shy Students, and Students with IEPs?

| Element | Spec |
|---------|------|
| Block type | Adaptation Block |
| Word target | 350–450 words |
| EAR attributes | #7 (ELL adaptations), #8 (IEP/shy) |
| H3s | Three required — ELLs / Shy-Introverted / IEPs and 504s |
| Schema role | FAQ candidate (Q5 maps here) |

**Heading:** `## How Do You Adapt Turn and Talk for ELLs, Shy Students, and Students with IEPs?`

**Content instructions for C3:**
- 1 framing sentence: "Turn and Talk is one of the most adaptable discussion strategies in the classroom — but only if you build in the right scaffolds from the start."
- Three H3 sub-sections, each 100-130 words:

**H3: For English Language Learners**

`### Adapting Turn and Talk for English Language Learners`

- Sentence frame scaffolds (connect to Section 4 sentence starters)
- L1 partner pairing option — allow brief L1 clarification before L2 response
- Vocabulary pre-teach cue (display key terms with visuals before turn prompt)
- Cite ELL learning gains stat here (NICHD or bilingual education research from C1)

**H3: For Shy or Introverted Students**

`### Adapting Turn and Talk for Shy or Introverted Students`

- Written response option: students write their response first, then share with partner (removes cold-start anxiety)
- Structured wait time: 10-15 seconds think time before partner signal
- Pre-assigned stable partners (known partner removes social uncertainty)
- Avoid randomizing pairs for shy students until trust is established

**H3: For Students with IEPs and 504 Plans**

`### Adapting Turn and Talk for Students with IEPs and 504 Plans`

- UDL framing: Turn and Talk supports multiple means of expression
- AAC / nonverbal options: gesture-based response, picture response card, device-assisted communication
- Extended processing time: allow extra think time before partner signal
- Note: name-check UDL principles once only (avoid jargon-heavy framing)

**Stats to place here:**
- ELL learning gains stat (Attr stat #3) — place in ELL sub-section with "According to [Source]" framing
- "According to research on wait time..." — reference Rowe here briefly (link back to Section 2 for full treatment)

**Internal links:** None required in this section

---

### SECTION 6 — H2: How Do You Use Turn and Talk in Digital and Hybrid Classrooms?

| Element | Spec |
|---------|------|
| Block type | Digital Implementation Block |
| Word target | 300–400 words |
| EAR attributes | #9 — Digital/hybrid |
| H3s | Three named formats: synchronous virtual / hybrid / async |
| Schema role | Product anchor section — single Wayground mention |

**Heading:** `## How Do You Use Turn and Talk in Digital and Hybrid Classrooms?`

**Content instructions for C3:**
- 1-2 framing sentences: distance learning didn't kill partner discussion — it just required new logistics
- Three named H3 sub-sections, each ~80-100 words:

**H3: Synchronous Virtual (e.g., Zoom / Google Meet)**

`### Synchronous Virtual Classrooms`

- Breakout rooms in pairs (2-minute timer)
- Display the prompt on screen before sending to rooms
- Structured re-entry: bring all back, cold-call one pair to share
- Tip: assign breakout pairs in advance to save time

**H3: Hybrid Classrooms**

`### Hybrid Classrooms`

- In-room students: shoulder partner as usual
- Digital students: pre-assigned digital partner in the same virtual space
- Pair one in-room + one virtual student only if audio setup supports it; otherwise pair by mode

**H3: Asynchronous and Self-Paced**

`### Asynchronous and Self-Paced Settings`

- Written chat prompt: student writes their response to a shared doc or LMS discussion thread
- Recorded voice response: audio note tool for verbal learners
- Partner responds within 24 hours (structured async dialogue)

**⚠️ Wayground product anchor — ONE paragraph, placed after the three H3s:**
- Frame as a tool recommendation, not a sales pitch
- Suggested framing: "Wayground's Team Mode replicates the partner-discussion structure of Turn and Talk in a digital setting, letting students respond to each other's answers in real time — with built-in accountability that shows you which pairs engaged and which ones drifted."
- Link: `/features/team-mode` (confirm URL before draft goes to C3 — do not link to generic features page per B3 flag)
- Follow with resource library link: anchor "ready-made discussion activities" → `/activities/discussion` or `/activities/collaborative` (verify URL)

**Internal links:**
- Product anchor: "Wayground's Team Mode" → `/features/team-mode`
- Resource CTA: "ready-made discussion activities" → `/activities/discussion`

---

### SECTION 7 — H2: What Does Research Say About Why Turn and Talk Works?

| Element | Spec |
|---------|------|
| Block type | Evidence Sandwich Block |
| Word target | 200–300 words |
| EAR attributes | #10 — Research backing |
| H3s | None required |
| Schema role | Trust signal / E-E-A-T anchor; citation density maximized here |

**Heading:** `## What Does Research Say About Why Turn and Talk Works?`

**Content instructions for C3:**
- Lead with Vygotsky ZPD framing (1 sentence only — don't over-explain): "Lev Vygotsky's theory of the Zone of Proximal Development (ZPD) offers a foundational explanation: students learn best when they work just beyond their current ability level — and a more capable peer is often the most accessible scaffold."
- Then: 2 empirical citations with effect direction:
  - Michaels, O'Connor & Resnick — accountable talk framework; name the framework explicitly
  - Webb, N.M. — peer interaction and learning gains; cite effect direction
- Hattie meta-analysis or equivalent (Attr stat #1) — place here: "According to [Source], structured peer discussion shows an effect size of [X] on student achievement — placing it among the more powerful instructional moves available to classroom teachers."
- Participation equity data (Attr stat #2) — place here: the "1 of 30" framing: "In a whole-class discussion with 30 students, only one student speaks at a time — a 3% participation rate. Turn and Talk activates all 15 pairs simultaneously."
- Close with practitioner quote (Expert Quote #2 from B3): named teacher from Wayground's vetting network if available

**Stats to place here (priority):**
- Stat #1: Effect size of structured peer discussion (Hattie or comparable)
- Stat #2: Participation equity / "1 of 30" framing
- Vygotsky (1978) ZPD — required citation
- Michaels, O'Connor & Resnick — required citation
- Webb, N.M. — required citation

**Quotes to place here:**
- Expert Quote #1: Researcher (Michaels, Resnick, Webb, or Wiliam) — cognitive rationale for peer discussion
- Expert Quote #2: K-12 practitioner — what makes it work in real classrooms

**Internal links:** None — keep trust signal clean

---

### SECTION 8 — H2: What Are Common Turn and Talk Mistakes — and How Do You Fix Them?

| Element | Spec |
|---------|------|
| Block type | Mistake → Fix Block |
| Word target | 250–350 words |
| EAR attributes | #11 (common mistakes) |
| H3s | None required |
| Schema role | High shareability; FAQ adjacent |

**Heading:** `## What Are Common Turn and Talk Mistakes — and How Do You Fix Them?`

**Content instructions for C3:**
- 1 intro sentence: "Turn and Talk breaks down in predictable ways — and most of them are fixable with one small adjustment."
- **Mistake → Fix table (5–6 rows):**

| Mistake | Why It Happens | Fix |
|---------|---------------|-----|
| Students go off-task | Prompt is too vague or too easy | Require a specific claim or evidence before talking |
| One partner dominates | No role structure | Assign roles: Speaker first / Listener first; switch at midpoint |
| Timing drags | No visible countdown | Display a 90-second timer on screen |
| No accountability | Students know no one will check | Cold-call one pair to share out after every turn |
| Shy students opt out silently | No think time before partner signal | Add 10-second written think time before talking |
| Conversations stay surface-level | Prompt is recall-only | Upgrade prompts to analysis: "Why?" / "What's your evidence?" |

- 1-2 closing sentences: "The most common mistake of all? Abandoning Turn and Talk because it felt messy the first time. Like any protocol, it improves with consistent, low-stakes repetition."

**Stats/quotes to place here:** None required — table carries the section

**Internal links:** None required

---

### SECTION 9 — H2: How Does Turn and Talk Look Different Across Grade Levels?

| Element | Spec |
|---------|------|
| Block type | Grade-Band Table |
| Word target | 150–200 words + table |
| EAR attributes | #12 — Grade differentiation |
| H3s | None required |
| Schema role | Supplementary; include if word count allows (target range: keep if under 3,400 without it) |
| Priority | Lower — include if word count allows; C3 may compress or move to FAQ if tight |

**Heading:** `## How Does Turn and Talk Look Different Across Grade Levels?`

**Content instructions for C3:**
- 1-2 framing sentences
- **Grade-band differentiation table:**

| Grade Band | What It Looks Like | Prompt Complexity | Partner Structure |
|-----------|-------------------|------------------|-----------------|
| K–2 | Shoulder partner, teacher models first | Picture prompt / recall | Stable assigned partner |
| 3–5 | Sentence frame scaffolds | Comprehension + make connections | Assigned or rotating stable pairs |
| 6–8 | Evidence-based academic language | Analysis + evaluation | Structured roles (speaker/listener) |
| 9–12 | Structured academic controversy variant | Argumentation + synthesis | Self-selected or thematic grouping |

- 1 closing sentence connecting grade-band variation back to sentence starters in Section 4

**Internal links:** Reference back to sentence starters section inline

---

### SECTION 10 — H2: Frequently Asked Questions

| Element | Spec |
|---------|------|
| Block type | FAQ Block |
| Word target | 300–400 words (total across all 6 Q&As) |
| EAR attributes | Variant phrasings from A1; residual attributes |
| Schema role | FAQPage schema — each Q&A pair is a schema item |
| Answers | 40–60 words each (AI extraction format — strict) |

**Heading:** `## Frequently Asked Questions About Turn and Talk`

**FAQ items (6):**

| # | Question (schema: `name`) | EAR Attr | Answer focus | Word target |
|---|--------------------------|---------|-------------|-------------|
| FAQ 1 | How do you do a "turn and talk" in the classroom? | #3 | 3-step compressed protocol: pose prompt → give think time → signal partner talk → call back; link to full protocol section | 40–55 words |
| FAQ 2 | What are the benefits of Turn and Talk for students? | #10 | Engagement equity + verbal processing + comprehension gains; cite 1 research direction; no fabricated stats | 40–55 words |
| FAQ 3 | How is Turn and Talk different from Think-Pair-Share? | #2 | Core distinction: T&T is shorter and more spontaneous; TPS adds individual write step and structured share-out; reference comparison table | 40–55 words |
| FAQ 4 | When should teachers use Turn and Talk during a lesson? | #4 | Three-phase answer: warm-up / mid-lesson check / exit consolidation; reference placement table | 40–55 words |
| FAQ 5 | How do you make Turn and Talk work for English language learners or shy students? | #7, #8 | Sentence frames + L1 partner for ELLs; written option + pre-assigned partners for shy students; reference adaptation section | 45–60 words |
| FAQ 6 | How long should a Turn and Talk last? | #5 | 90 seconds warm-up; 2–3 minutes mid-lesson; up to 4 minutes exit consolidation; reference Duration Guide table | 40–55 words |

**C3 instruction:** Each answer must be self-contained — a reader should get the core answer from the FAQ alone, without needing to read the full section. Link back to full sections where relevant.

---

## Stats and Quotes Placement Summary

| Asset | Section | Citation format |
|-------|---------|----------------|
| Rowe (1986) wait time | Section 2 (steps) — Step 3 think time | "According to Mary Budd Rowe's research on wait time…" |
| Hattie / peer discussion effect size | Section 7 (research) | "According to [Source], structured peer discussion shows an effect size of [X]…" |
| Participation equity ("1 of 30") | Section 7 (research) | Inline framing — no formal citation needed if framed as math |
| ELL learning gains stat | Section 5 (ELL H3) | "According to [Source]…" |
| Vygotsky (1978) ZPD | Section 7 (research) | Narrative reference — "Lev Vygotsky's theory of the Zone of Proximal Development…" |
| Michaels, O'Connor & Resnick — accountable talk | Section 7 (research) | "According to Michaels, O'Connor, and Resnick…" |
| Webb — peer interaction | Section 7 (research) | "According to Noreen Webb's research on peer interaction…" |
| Expert Quote #1 (researcher) | Section 7 (research) — closing | Full attribution format |
| Expert Quote #2 (practitioner teacher) | Section 7 (research) — closing | "[Quote]," says [Name], [Grade] teacher at [School], [City] |
| Expert Quote #3 optional (ELL specialist) | Section 5 (ELL H3) | "[Quote]," says [Name], [Title] at [Org] — if sourced by C1 |

---

## Internal Link Placement Summary

| Anchor text | Target URL | Section | Notes |
|-------------|-----------|---------|-------|
| student engagement strategies | `/learn/engagement/` | Article meta / intro prose | Parent hub — place naturally in first 300 words |
| think-pair-share strategy | `/learn/strategies/think-pair-share` | Section 1 | Bidirectional if page exists; flag for creation if not |
| alternatives to cold calling | `/learn/engagement/cold-calling-alternatives` | Section 1 | After comparison table |
| collaborative learning in the classroom | `/learn/strategies/collaborative-learning` | Section 5 or Section 7 prose | High-authority internal link; place naturally |
| exit ticket strategies | `/learn/engagement/exit-tickets` | Section 3 prose | After placement table; reference only |
| Wayground's Team Mode | `/features/team-mode` | Section 6 — product anchor | **Confirm URL** — only product mention in article |
| ready-made discussion activities | `/activities/discussion` | Section 6 — resource CTA after product anchor | **Confirm URL** |

---

## EAR Attribute Coverage Map

| Attr # | Description | Section | Depth |
|--------|-------------|---------|-------|
| #1 | What is Turn and Talk | Block 0 (Definition) | Deep |
| #2 | Comparison to TPS / Cold Calling | Section 1 | Deep (table) |
| #3 | Teacher moves / steps | Section 2 | Deep (HowTo) |
| #4 | Lesson placement | Section 3 | Deep (table) |
| #5 | Timing / Duration Guide | Section 2 H3 | Deep (table) |
| #6 | Sentence starters | Section 4 | Deep (two tables) |
| #7 | ELL adaptations | Section 5 H3 | Addressed |
| #8 | IEP/shy adaptations | Section 5 H3 | Addressed |
| #9 | Digital/hybrid | Section 6 | Deep (3 formats) |
| #10 | Research backing | Section 7 | Addressed |
| #11 | Common mistakes | Section 8 | Addressed (table) |
| #12 | Grade differentiation | Section 9 | Addressed (table) |

**Projected D1 score:** 11/12 at Addressed or above; Attrs 5, 6, 9 at Deep. Attr #12 at Addressed (lower priority; may be compressed if word count tight).

---

## Flags for C3 (Draft Agent)

1. **C1 research packet not received.** Stats and quotes marked with "[Source]" placeholders must be filled from C1 output before draft is finalized. Do not fabricate citations.

2. **WG platform stat (Attr stat #5) is [DATA NEEDED].** Replace with a teacher community quote if UXR data is not confirmed. Do not invent a percentage.

3. **Product URL confirmation required.** Verify `/features/team-mode` is the correct Team Mode URL before drafting Section 6. Do not link to a generic features page.

4. **Sentence starters tables (Section 4) must be fully populated.** These are the primary link-earning asset. Under-serving them reduces shareability and backlink probability.

5. **Definition block word count.** The QAPE target direct answer is 58 words — at the upper edge of the 40-60 target. C3 may trim one clause to reach sub-55 if needed, but do not restructure the core answer.

6. **Section 9 (grade-band table) is conditional.** Include if total word count allows; skip or move to FAQ if draft runs long. It is the only section marked lower priority.

7. **One product mention only.** Wayground Team Mode appears in Section 6 only. Zero or two mentions is a D1 escalation condition.

---
Now execute your task. **IMPORTANT: Wrap your entire output in `<output>` and `</output>` tags.** Your output begins with `<output>` on its own line and ends with `</output>` on its own line. Everything between those tags is your deliverable.
