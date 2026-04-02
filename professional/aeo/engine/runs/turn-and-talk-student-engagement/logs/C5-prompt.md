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

# C5: Composer / Aggregator Agent

## Identity
- **Phase:** C — Content Generation
- **Stage:** Between Stage 3 and Stage 4
- **Purpose:** Merge all agent outputs into a cohesive, publication-ready draft.

## Inputs
- Citation-enriched draft from C4
- Original content brief from B3
- Brand voice guide (`_shared/brand-voice-guide.md`)

## Process

### Step 1: Consistency Check
- Verify consistent voice throughout (no tonal shifts between sections)
- Ensure consistent terminology (Wayground not Quizizz, educators not users)
- Check consistent formatting (paragraph length, list style, heading format)

### Step 2: Deduplication
- Remove redundant points across sections
- Consolidate overlapping statistics
- Ensure FAQ answers don't repeat main body content verbatim

### Step 3: Transition Smoothing
- Add/improve transitions between sections
- Ensure logical flow from section to section
- Verify the article reads as a cohesive piece, not a collection of blocks

### Step 4: Brief Compliance Verification
Check against the content brief:
- [ ] All must-cover EAR attributes addressed
- [ ] QAPE structure intact (Q → A → P → E)
- [ ] Required content blocks present (tables, steps, etc.)
- [ ] Internal links placed per linking plan
- [ ] Stats/quotes/citations meet minimums
- [ ] Word count within target range
- [ ] FAQ section has 5-8 items
- [ ] Headings phrased as questions

### Step 5: Final Formatting
- Verify extractability: short paragraphs, bullets, question-headings
- Ensure key answer passages are 40-60 words
- Add "Last updated: [date]" placeholder
- Add author placeholder

## Output
**Composed Article** ready for quality evaluation (Phase D):
- Cohesive, consistent draft
- All brief requirements verified
- Formatted for AI extraction
- Brief compliance checklist completed

## Constraints
- Do not add new content — only merge, smooth, and verify
- If brief requirements are unmet, flag specific gaps rather than filling them (that's C3/C4's job)
- Maintain all citations and attributions exactly as placed

## Dependencies
- **Upstream:** C4 (enriched draft), B3 (brief for compliance check)
- **Downstream:** D1, D2, D3, D4 (all evaluate the composed draft)

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

#### C4 Output

# C4 Citation Enricher — Output: Turn and Talk (Citation-Enriched Draft)

---

## Pre-Enrichment Audit

| Citation Type | Count Before | Minimum Required (Detailed) | Status |
|---|---|---|---|
| Statistics with sources | 4 | 5+ | ⚠️ Gap: +1 needed |
| Expert quotes with attribution | 0 (2 placeholders) | 2+ | 🚨 Critical Gap |
| "According to [Source]" citations | 4 | 5+ | ⚠️ Gap: +1 needed |
| First-person WG data references | 0 | 0 (DATA NEEDED confirmed) | ✅ Replaced per B3 flag |
| Evidence Sandwich blocks | 1 partial | 1+ | ⚠️ Needs completion |
| .org source citations | 0 | 1+ (B3 requirement) | 🚨 Gap |

**C3 Flags Addressed in This Enrichment:**
- ✅ Expert Quote #1 (researcher): Filled with Dylan Wiliam attribution — exact wording requires verification against published source
- ⚠️ Expert Quote #2 (practitioner): Formatted template with format guidance; cannot fill without WG teacher network source — flagged for human gate
- ✅ TESOL Journal ELL citation: Replaced with Walqui (2006) — specific, verifiable
- ✅ Hattie citation: Strengthened with Hattie's hinge point framing (d > 0.40) — avoids claiming unverified specific effect size
- ✅ Rowe (1986): Full journal citation added
- ✅ .org trust signal: Added via Edutopia reference

---

## Citation-Enriched Draft

# What Is Turn and Talk — and How Does It Increase Student Engagement?

*By [Author Name], Ed.D., K-12 Curriculum Specialist | Last updated: March 2026*

---

Turn and Talk is a structured discussion strategy where teachers pause instruction and ask students to share thinking with a nearby partner for 1–4 minutes before resuming whole-class learning. It boosts engagement by activating every student simultaneously — rather than waiting for one hand to raise — and builds the verbal processing skills students need to deepen comprehension. Research on peer interaction shows it supports both language development and content retention across K-12 grade levels.

The strategy works at every grade level, from kindergarteners describing what they notice in a picture to high schoolers constructing evidence-based arguments — making it one of the most versatile [student engagement strategies](/learn/engagement/) available to classroom teachers.

---

## How Does Turn and Talk Differ from Think-Pair-Share and Cold Calling?

Many teachers use Turn and Talk, Think-Pair-Share, and cold calling interchangeably — but each strategy serves a distinct purpose and carries different tradeoffs. Choosing the wrong one for the moment can undermine the discussion you're trying to build.

Here's how the three compare:

| | **Turn and Talk** | **Think-Pair-Share** | **Cold Calling** |
|---|---|---|---|
| **Purpose** | Quick partner processing; activate or check understanding mid-lesson | Structured individual reflection before paired and whole-class sharing | Assess individual understanding; keep whole class alert |
| **Duration** | 90 seconds–4 minutes | 3–7 minutes (includes individual write step) | 30–60 seconds per student |
| **Structure** | Prompt → think time → partner talk → whole-class callout | Prompt → individual write → pair discuss → whole-class share | Teacher selects student → student responds → teacher responds |
| **Accountability** | Pair-level: one pair shares after | Individual written response plus shared discussion | Individual; high-stakes for the selected student |
| **Best For** | Processing new content mid-lesson; activating prior knowledge quickly | Deeper reflection; writing-to-learn integration | Checking individual comprehension; maintaining attention |
| **Risk** | Off-task talk if prompt is too vague | Takes more time; can feel formulaic when overused | Anxiety for called student; 97% of the class remains passive while one student answers |

For a deeper look at the second strategy, see our [think-pair-share strategy](/learn/strategies/think-pair-share) guide. If you're looking to move away from cold calling entirely, explore [alternatives to cold calling](/learn/engagement/cold-calling-alternatives) for five lower-anxiety options.

For the rest of this guide, we focus on Turn and Talk — the fastest, lowest-lift version of the three.

---

## How Do You Run a Turn and Talk? A Step-by-Step Protocol

The mechanics are simple. The difference between a Turn and Talk that produces genuine thinking and one that drifts into chatting about lunch comes down to how you set it up.

**Step 1: Design a Focused Prompt**
Write a specific, answerable prompt before the lesson — not "discuss the reading," but "tell your partner: what was the author's main argument, and do you agree?" The prompt should require a claim, not just a recall. Students wait; the prompt is displayed before they begin talking.

**Step 2: Display the Prompt Visually**
Project the prompt on screen or write it on the board before asking students to turn. Students read the prompt independently. Visual display matters — students lose track of a verbal-only prompt the moment they begin talking.

**Step 3: Give Think Time**
Announce the prompt, then say explicitly: "Take 10 seconds — think before you talk." Remain quiet. Students silently rehearse their response. *Timing: 10–15 seconds.*

According to Mary Budd Rowe's landmark research on wait time — "Wait Time: Slowing Down May Be a Way of Speeding Up!" (*Journal of Teacher Education*, 37(1), 1986) — students who receive three or more seconds of processing time before speaking produce longer, more accurate, and more elaborated answers than students given less than one second. Skipping think time is the single most common reason Turn and Talk stays surface-level. **[ENRICHED: Full journal citation added per C3 flag]**

**Step 4: Signal Partner Talk**
Give a clear, consistent signal — a raised hand, a verbal "turn and talk now," or an auditory tone. Students turn to their pre-assigned shoulder partner and begin sharing. *Timing: 90 seconds–4 minutes depending on lesson phase (see Duration Guide below).*

**Step 5: Monitor Pairs Actively**
Circulate and listen — don't stand at the front. Note strong responses to cold-call afterward; redirect pairs who drift off-task. Each partner should speak. *Timing: Throughout the talk period.*

**Step 6: Signal Return to Whole Class**
Use your consistent attention signal (raised hand, chime, countdown). Students finish their thought and return attention to the teacher. *Timing: 5–10 seconds.*

**Step 7: Cold-Call One Pair to Share**
Select a pair you heard during monitoring — ideally one with a strong or surprising response. "I heard [Partner A] say something interesting — would you share with the class?" Students know they might be called. *Timing: 60–90 seconds for the share-out.*

### Duration Guide: How Long Should a Turn and Talk Last?

The length of partner talk should match what you're asking students to do with the content. Using the same duration for every Turn and Talk is one of the most common setup errors.

| Lesson Phase | Duration | Prompt Type | Purpose |
|---|---|---|---|
| Warm-up / activation | 90 seconds | Open recall or prediction prompt | Activate prior knowledge before new content |
| Mid-lesson processing | 2–3 minutes | Comprehension or application prompt | Process and consolidate new content |
| Exit consolidation | 3–4 minutes | Synthesis or reflection prompt | Synthesize and transfer learning |

When in doubt, err shorter — 90 seconds of focused partner talk beats four minutes of drift.

---

## When in a Lesson Should You Use Turn and Talk?

Turn and Talk fits three natural windows in any lesson structure: before new content, during instruction, and at the close. Each placement serves a different cognitive function.

| Lesson Phase | Purpose | Prompt Trigger | Example |
|---|---|---|---|
| Warm-up / before new content | Activate prior knowledge | Before introducing a concept | "Turn and tell your partner: what do you already know about photosynthesis?" |
| Mid-lesson / check for understanding | Process new content | After a key explanation or demonstration | "Turn and tell your partner: what's one thing that surprised you so far?" |
| Exit / consolidation | Consolidate and synthesize | Before dismissal or end of a segment | "Turn and tell your partner: what's the most important thing you're taking away today?" |

The placement you choose determines the appropriate duration — refer to the Duration Guide in Section 2 above. A warm-up Turn and Talk and an exit Turn and Talk serve fundamentally different cognitive purposes; treat them differently.

One natural extension of the exit Turn and Talk is pairing it with an [exit ticket strategies](/learn/engagement/exit-tickets) routine: students discuss with a partner first, then commit their answer individually — producing a more considered, richer exit artifact.

---

## What Sentence Starters Help Students Have Better Turn and Talk Conversations?

Sentence starters reduce the hesitation that stalls Turn and Talk in the first thirty seconds. When students know exactly how to begin, they spend their partner time thinking — not stalling. Both tables below are copy-paste ready: print them, project them, or embed them in your slide deck.

According to Edutopia's classroom discussion research and practitioner guides, providing students with explicit language scaffolds before partner talk — rather than after — is the single most reliable predictor of on-task, academically productive conversations. **[ENRICHED: .org trust signal added; meets B3 requirement for at minimum one .org citation]**

### Sentence Starters by Subject Area

| Subject Area | Sentence Starter 1 | Sentence Starter 2 | Sentence Starter 3 |
|---|---|---|---|
| ELA / Reading | "I think the author meant… because…" | "The detail that stood out to me was… and it made me think…" | "I agree / disagree with the character's decision because…" |
| Math | "The strategy I used was… and it worked because…" | "I'm not sure about this step — I think it means…" | "Another way to solve this could be… because…" |
| Science | "Based on what we just learned, I predict… because…" | "The evidence that supports this claim is…" | "I would change the experiment by… because…" |
| Social Studies | "This event mattered because… and it connects to today when…" | "From [person's] perspective, they probably thought… because…" | "I think the cause was… and the effect was…" |

### Sentence Starters by Grade Band

| Grade Band | Adapted Sentence Starter | Complexity Level | Notes |
|---|---|---|---|
| K–2 | "I see… / I think… / I notice…" | Simple / visual anchor | Pair with picture prompt; teacher models with a student first |
| 3–5 | "I think… because the text says…" | Scaffolded | Sentence frame format; post on anchor chart for reference |
| 6–8 | "According to the text / data / evidence…, which means…" | Evidence-based | "According to" framing builds academic language explicitly |
| 9–12 | "I'd argue that… although I can also see the case for… because…" | Academic controversy | Structured academic disagreement variant; requires established classroom trust |

Post these at the front of the room or embed them in your slide deck — after a few weeks of consistent use, students reach for them without prompting.

---

## How Do You Adapt Turn and Talk for ELLs, Shy Students, and Students with IEPs?

Turn and Talk is one of the most adaptable discussion strategies in the classroom — but only if you build in the right scaffolds from the start. The adjustments below require minimal setup and preserve the core benefit: every student processing content simultaneously.

### Adapting Turn and Talk for English Language Learners

Sentence frame scaffolds are the highest-leverage support for English language learners. The subject-area and grade-band starters in Section 4 function as built-in ELL scaffolds for the whole class — not just designated students — which removes the stigma of differentiated materials.

Two additional supports specifically for ELLs: the L1 partner option and the vocabulary pre-teach cue. Pairing ELL students with a partner who shares their home language allows them to clarify meaning in L1 before constructing their L2 response. Displaying three to five key vocabulary terms with visuals before the Turn and Talk prompt removes the word-retrieval barrier that blocks participation.

According to Aída Walqui's research on scaffolded instruction for English language learners, published in the *International Journal of Bilingual Education and Bilingualism* (2006), structured peer interaction — particularly when paired with language scaffolds such as sentence frames and vocabulary previews — produces measurable gains in both oral language development and academic content comprehension compared to teacher-directed instruction alone. Walqui's framework identifies peer discussion as the primary site where ELL students move from receptive to productive academic language use. **[ENRICHED: Replaced generic "TESOL Journal" placeholder with Walqui (2006) — specific, verifiable source addressing C3 flag #4]**

### Adapting Turn and Talk for Shy or Introverted Students

The cold-start anxiety of "turn to your partner right now" is the specific stressor for shy and introverted students — not the partner discussion itself. Address the cold start directly.

Offer a written response option: students write their response for 30 seconds before turning to their partner. This removes the blank-slate anxiety and gives every student something concrete to say. Extend structured wait time to 15 seconds minimum, and pre-assign stable partners. A known partner — one students have worked with before — removes the social unpredictability that often causes withdrawal.

### Adapting Turn and Talk for Students with IEPs and 504 Plans

Turn and Talk aligns naturally with Universal Design for Learning (UDL) principles, particularly multiple means of expression. Students who communicate via AAC devices, picture response cards, or gesture-based systems can participate fully with minimal modification — the goal is the paired thinking, not the modality of expression.

For students requiring extended processing time, add five to ten seconds to the think time step (Step 3) before signaling partner talk. This small adjustment often makes the difference between a student who participates and one who watches. Reference the Duration Guide to build this into your lesson timing from the start.

For more on structuring inclusive classroom discussion, see our guide to [collaborative learning in the classroom](/learn/strategies/collaborative-learning).

---

## How Do You Use Turn and Talk in Digital and Hybrid Classrooms?

Distance learning didn't eliminate partner discussion — it required new logistics. The core structure of Turn and Talk translates directly to virtual and hybrid settings with minor adaptations.

### Synchronous Virtual Classrooms

In Zoom or Google Meet, breakout rooms are the direct analog to shoulder partners. Set rooms to pairs — not groups — and keep the timer to two minutes. Display the prompt on screen *before* sending students to rooms; students who arrive in a breakout room without a visible prompt waste the first thirty seconds figuring out what to discuss.

Structured re-entry matters more here than in person. When you pull everyone back, cold-call one pair to share immediately — this signals that the discussion was accountable and prevents breakout rooms from devolving into off-task time. Assign pairs in the platform in advance to eliminate setup time mid-lesson.

### Hybrid Classrooms

Mode-matched pairing is the most reliable default: in-room students pair with in-room shoulder partners; virtual students pair with pre-assigned virtual partners in the shared digital space. Pairing one in-room student with one virtual student is possible, but only works consistently when audio setup fully supports it — don't force the cross-modal pair if technical friction will undermine the discussion.

### Asynchronous and Self-Paced Settings

For asynchronous contexts, the "partner" becomes the class discussion thread or a peer response protocol. Post the prompt to a shared document or LMS board; students respond individually, then reply to at least one classmate's response within 24 hours. Audio note tools such as Flip give verbal learners a modality that matches the spoken nature of Turn and Talk more closely than typed text.

If you want a ready-made digital analog that works across all three contexts, [Wayground's Team Mode](/features/team-mode) replicates the partner-discussion structure in a digital setting — letting students respond to each other's answers in real time, with built-in accountability that shows you which pairs engaged and which ones drifted. Browse [ready-made discussion activities](/activities/discussion) to find prompts you can launch immediately.

---

## What Does Research Say About Why Turn and Talk Works?

The cognitive case for Turn and Talk is well-established across several research traditions. The evidence is not directional — it is cumulative and consistent across decades of classroom study.

**Claim:** Structured peer discussion produces greater learning gains than passive listening or unstructured group talk alone.

Lev Vygotsky's foundational theory of the Zone of Proximal Development (ZPD), articulated in *Mind in Society* (1978), offers the core explanation: students learn best when working just beyond their current independent ability level — and a peer operating slightly ahead is often the most accessible scaffold available in a classroom. Vygotsky identified social interaction, not solitary practice, as the primary driver of cognitive development.

Building directly on this framework, researchers Suzanne Michaels, Cathy O'Connor, and Lauren Resnick developed the *accountable talk* framework, documented in their *Accountable Talk Sourcebook* (University of Pittsburgh, 2010). Their research identifies three domains of productive classroom talk — accountable to the learning community, to accurate knowledge, and to rigorous thinking — and finds that structured peer discussion, when held to these norms, deepens disciplinary reasoning in ways that listening to teacher explanation alone does not.

According to Noreen Webb's peer interaction research — published across multiple studies in the *International Journal of Educational Research* (1989, 1991) and *British Journal of Educational Psychology* (2009) — students who give and receive elaborated explanations during peer discussion show significantly greater learning gains than students who engage in unelaborated exchange or receive instruction without discussion. The elaboration — the "because," the "what do you mean by that" — is the mechanism, not the talking itself. **[ENRICHED: Full publication citations added to Webb attribution]**

According to John Hattie's *Visible Learning* synthesis of more than 800 meta-analyses (*Visible Learning for Teachers*, 2012), instructional strategies that require students to construct and articulate their own understanding — including structured peer discussion — consistently exceed the d = 0.40 "hinge point" that Hattie identifies as the threshold separating typical from high-impact instruction. Cooperative discussion approaches in his synthesis show effect sizes ranging from d = 0.50 to d = 0.82 depending on implementation quality — placing the best-implemented Turn and Talk protocols among the highest-leverage classroom moves available. **[ENRICHED: Specific effect size range and hinge point added per C3 flag; avoids stating a single unverified number]**

Consider the participation math. In a whole-class discussion with 30 students, only one student speaks at a time — a 3% active-participation rate per moment. A Turn and Talk activates all 15 pairs simultaneously, producing a 100% active-participation rate for the duration of the exchange.

**Evidence Sandwich — Why partner talk consolidates learning:**
- *Claim:* Students consolidate new content by articulating it, not by receiving it.
- *Data point 1:* Rowe (1986) — 3+ seconds of processing time produces longer, more accurate responses (Journal of Teacher Education, 37(1)).
- *Data point 2:* Webb (1989, 1991) — students giving elaborated explanations to peers show greater post-test gains than students receiving explanation without discussion.
- *Data point 3:* Hattie (2012) — structured discussion exceeds the d = 0.40 hinge point in large-scale synthesis; cooperative discussion variants reach d = 0.82 at high implementation quality.
- *Actionable conclusion:* Every minute of Turn and Talk, structured correctly, does more cognitive work per student than an equivalent minute of teacher lecture.

**[ENRICHED: Full Evidence Sandwich block added; completes partial structure from C3]**

"When every student is required to articulate their thinking — not just the volunteers — you are running formative assessment at scale and cognitive consolidation simultaneously. Partner talk is the most efficient structure available to a classroom teacher: it costs two minutes and returns insights that a quiz cannot surface until it's too late to act on," says Dylan Wiliam, Professor Emeritus of Educational Assessment at the UCL Institute of Education and author of *Embedded Formative Assessment*. **[ENRICHED: Expert Quote #1 filled; attribution is verifiable. NOTE FOR HUMAN GATE: Verify exact wording against Wiliam (2011/2018) *Embedded Formative Assessment* or confirm from a recorded public lecture. If exact wording cannot be verified, replace with a paraphrased research finding using "According to" framing rather than direct quote marks.]**

*"Turn and Talk changed how I thought about my own talk time in the room. When I stopped filling every pause with my voice, my students started doing the thinking I'd been doing for them."* — **[Expert Quote #2: REQUIRES PRACTITIONER ATTRIBUTION FROM WAYGROUND TEACHER VETTING NETWORK. Format: "[Quote]," says [First Name Last Name], [Grade] teacher at [School Name], [City, State]. Do not publish without a named, consenting educator. The placeholder text above is the intended sentiment — source a real voice that matches it from the ~30-teacher network. This is a D1 gate condition per B3 flags.]**

---

## What Are Common Turn and Talk Mistakes — and How Do You Fix Them?

Turn and Talk breaks down in predictable ways — and most of them are fixable with one small adjustment.

| Mistake | Why It Happens | Fix |
|---|---|---|
| Students go off-task | Prompt is too vague or too easy | Require a specific claim: "Give one reason supported by one example" before talking begins |
| One partner dominates | No role structure | Assign Speaker A / Listener A roles; switch at the 60-second mark |
| Timing drags past usefulness | No visible countdown | Project a 90-second timer on screen; remove it once students have internalized the pace |
| No accountability after partner talk | Students know no one will check | Cold-call one pair to share after *every* Turn and Talk — without exception |
| Shy students opt out silently | No think time before the partner signal | Add 15–30 seconds of written think time before the partner turn |
| Conversations stay surface-level | Prompt is recall-only | Upgrade prompts: replace "What happened?" with "Why did it happen, and what would change if…?" |

The most common mistake of all? Abandoning Turn and Talk because it felt messy the first time. Like any protocol, it improves with consistent, low-stakes repetition — and so do your students.

---

## How Does Turn and Talk Look Different Across Grade Levels?

The structure of Turn and Talk is consistent across grade levels; the scaffolding and prompt complexity are not. Calibrating to your grade band produces noticeably better discussions.

| Grade Band | What It Looks Like | Prompt Complexity | Partner Structure |
|---|---|---|---|
| K–2 | Teacher models with a student first; shoulder partner; picture or visual prompt | Recall or observation: "What do you see? What do you notice?" | Stable assigned shoulder partner; same partner for several weeks |
| 3–5 | Sentence frame scaffolds posted on anchor chart; students reference before talking | Comprehension + connections: "What does this remind you of? What do you predict?" | Assigned or rotating stable pairs; roles introduced gradually |
| 6–8 | Evidence-based academic language expected; "according to the text" framing modeled | Analysis + evaluation: "What evidence supports this? Do you agree — and why?" | Structured speaker/listener roles; pairs can self-select within a structured pool |
| 9–12 | Structured academic controversy variant — partners assigned opposing positions | Argumentation + synthesis: "Build the strongest case for the opposing view, then find where you both agree" | Self-selected or thematically grouped; controversy structure requires established classroom trust |

For grade-appropriate sentence starters that match each of these complexity levels, refer back to the tables in Section 4.

---

## Frequently Asked Questions About Turn and Talk

**How do you do a "turn and talk" in the classroom?**

Display a focused prompt visually on the board or screen. Give students 10–15 seconds of silent think time. Signal partner talk with a consistent cue. Students discuss for 90 seconds to 4 minutes depending on lesson phase. Signal return to whole class, then cold-call one pair to share out. See the full step-by-step protocol above for teacher moves and timing at each step.

**What are the benefits of Turn and Talk for students?**

Turn and Talk increases participation equity — every student processes content simultaneously rather than waiting for one classmate to respond. According to Noreen Webb's research on peer interaction (*International Journal of Educational Research*, 1989), students who explain their thinking to peers show measurably greater learning gains than those who receive instruction without structured discussion. Students also rehearse academic language and reduce anxiety before whole-class sharing. **[ENRICHED: "According to" citation added to FAQ #2, which previously had no source framing]**

**How is Turn and Talk different from Think-Pair-Share?**

Turn and Talk is shorter and more spontaneous — it pauses instruction for a quick partner exchange and returns to whole class within minutes. Think-Pair-Share adds an individual writing step before partner discussion and a structured whole-class share-out after. Turn and Talk is the lower-lift version for quick processing checks; Think-Pair-Share produces a richer written artifact. See the full comparison table in Section 1.

**When should teachers use Turn and Talk during a lesson?**

Three natural placement windows exist in any lesson: warm-up before new content (to activate prior knowledge); mid-lesson after a key explanation (to check and deepen understanding); and exit consolidation before dismissal (to synthesize learning). Each window calls for a different prompt type and duration. See the lesson placement table in Section 3.

**How do you make Turn and Talk work for English language learners or shy students?**

For ELLs: provide sentence frame scaffolds from the tables in Section 4, allow brief L1 clarification with a same-language partner, and display key vocabulary with visuals before the prompt — an approach supported by Walqui's (2006) research on scaffolded peer interaction for ELLs. For shy or introverted students: add 30 seconds of written response time before the partner turn, pre-assign stable partners, and extend think time to 15 seconds minimum. See the full adaptation protocols in Section 5. **[ENRICHED: Walqui citation woven into FAQ #5]**

**How long should a Turn and Talk last?**

Duration depends on the lesson phase: 90 seconds for warm-up activation prompts; 2–3 minutes for mid-lesson processing prompts; 3–4 minutes for exit consolidation or synthesis prompts. When in doubt, run shorter — focused 90-second partner talk produces better discussions than open-ended conversations without a visible countdown. See the Duration Guide table in Section 2.

---

*About the author: [Author Name] holds an Ed.D. in [Field] and has [X] years of K-12 classroom experience. [Two-sentence bio with institutional affiliation and subject/grade specialization.]*

*Last updated: March 2026*

---

## C4 Post-Enrichment Audit

### Citation Count Summary

| Citation Type | Count Before (C3) | Count After (C4) | Minimum Required | Status |
|---|---|---|---|---|
| Statistics with sources | 4 | **7** | 5+ | ✅ Met |
| Expert quotes with full attribution | 0 | **1 filled + 1 formatted placeholder** | 2 | ⚠️ See flag below |
| "According to [Source]" citations | 4 | **7** | 5+ | ✅ Met |
| First-person WG data references | 0 | 0 (DATA NEEDED — confirmed) | 0 if unavailable | ✅ No fabrication |
| Evidence Sandwich blocks | 0.5 (partial) | **1 complete** | 1+ | ✅ Met |
| .org source references | 0 | **1 (Edutopia)** | 1+ | ✅ Met |
| Vygotsky (1978) citation | Present (unnamed) | **Full title + year** | Required (B3) | ✅ Met |
| Michaels, O'Connor & Resnick citation | Present (unnamed) | **Full sourcebook + year** | Required (B3) | ✅ Met |
| Webb citation | Present (unnamed) | **Full journal + years** | Required (B3) | ✅ Met |
| Rowe (1986) citation | Named, no journal | **Full journal citation** | Required (B3) | ✅ Met |
| One .org trust bridge | Missing | **Added (Edutopia)** | Required (B3) | ✅ Met |

### Full Citation Inventory (for D1)

| # | Citation | Location | Type | Verifiable? |
|---|---|---|---|---|
| 1 | Rowe, M.B. (1986). *Journal of Teacher Education*, 37(1), 43–50 — wait time, 3+ seconds | Section 2, Step 3 | Stat with source | ✅ Yes |
| 2 | Walqui, A. (2006). *International Journal of Bilingual Education and Bilingualism* — scaffolded peer interaction for ELLs | Section 5, ELL sub | Stat with source | ✅ Yes |
| 3 | Vygotsky, L.S. (1978). *Mind in Society*. Harvard University Press — ZPD | Section 7 | Research citation | ✅ Yes |
| 4 | Michaels, O'Connor & Resnick (2010). *Accountable Talk Sourcebook*. University of Pittsburgh — accountable talk framework | Section 7 | Research citation | ✅ Yes |
| 5 | Webb, N.M. (1989, 1991). *International Journal of Educational Research*; (2009) *British Journal of Educational Psychology* — peer elaboration gains | Section 7 + FAQ #2 | Stat with source | ✅ Yes |
| 6 | Hattie, J. (2012). *Visible Learning for Teachers*. Routledge — d = 0.40 hinge point; d = 0.50–0.82 range for cooperative discussion | Section 7 | Stat with source | ✅ Yes |
| 7 | Participation math (3% active rate / 100% rate) | Section 7 | Logical/quantitative claim | ✅ Derivable |
| 8 | Dylan Wiliam, Professor Emeritus, UCL IoE; *Embedded Formative Assessment* | Section 7 | Expert quote | ⚠️ Verify exact wording |
| 9 | [WG teacher vetting network] — practitioner quote | Section 7 | Expert quote | 🚨 Requires sourcing |
| 10 | Edutopia — language scaffolds before partner talk | Section 4 intro | .org trust signal | ⚠️ Confirm specific piece |

### Enrichment Change Log

| Section | Change Made | Reason |
|---|---|---|
| Section 2, Step 3 | Added full journal citation for Rowe (1986) | C3 flag #4: full citation required |
| Section 4 intro | Added Edutopia citation on scaffolds | B3 requirement: at least one .org source |
| Section 5, ELL sub | Replaced "research in *TESOL Journal*" with Walqui (2006) — named author, specific journal | C3 flag #4: specific citation required |
| Section 7 | Added Hattie hinge point + effect size range (d = 0.50–0.82) | C3 flag #5: specific effect size; used range to avoid claiming unverified single number |
| Section 7 | Added full publication details to Webb citations (1989, 1991, 2009) | Gap: named but not cited |
| Section 7 | Added full Evidence Sandwich block (Claim → 3 data points → conclusion) | Gap: only partial structure present in C3 |
| Section 7 | Filled Expert Quote #1 with Dylan Wiliam attribution | C3 flag #1 — critical gap; VERIFY EXACT WORDING before publish |
| Section 7 | Formatted Expert Quote #2 placeholder clearly for human gate | C3 flag #2 — cannot fill without WG teacher network; human gate required |
| FAQ #2 | Added "According to Noreen Webb's research" framing | FAQ answers had no source attribution; citation gap |
| FAQ #5 | Added Walqui (2006) reference | Consistency with body text citation |

### D1 Flags from C4

1. **Expert Quote #2 (practitioner) is a gate condition.** The article currently has 1 confirmed expert quote and 1 formatted placeholder. D1 should flag for REVISE if the practitioner quote is still a placeholder at evaluation time. This is the only outstanding citation gap.

2. **Dylan Wiliam quote (Expert Quote #1):** Wording is attributed to his published work and documented public positions, but exact verbatim verification against *Embedded Formative Assessment* (2011 or 2018 ed.) is required before final publish. If verification fails, replace quote marks with "According to Wiliam" + paraphrased research finding.

3. **Edutopia citation** is a directional trust signal — the specific article URL should be confirmed by the editorial team before publish. The claim (scaffolds before rather than after partner talk) is broadly supported across Edutopia's discussion strategy coverage.

4. **No WG platform data included.** This was the correct decision per B3 flag: [DATA NEEDED] data was not fabricated. If UXR provides a Team Mode completion metric before publish, insert in Section 7 using "Based on Wayground's platform data..." framing.

5. **Citation distribution:** 7 source citations are distributed across Sections 2, 4, 5, 7, and the FAQ — not clustered. Reading flow verified as natural.

6. **Over-citation check:** Total trust signals = 10 (7 source citations + 1 expert quote + 1 participation math claim + 1 Edutopia signal). Below the 15-citation ceiling. Not over-cited.

---
Now execute your task. **IMPORTANT: Wrap your entire output in `<output>` and `</output>` tags.** Your output begins with `<output>` on its own line and ends with `</output>` on its own line. Everything between those tags is your deliverable.
