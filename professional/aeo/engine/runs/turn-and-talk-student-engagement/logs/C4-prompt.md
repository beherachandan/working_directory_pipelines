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

# C4: Citation Enricher Agent

## Identity
- **Phase:** C — Content Generation
- **Stage:** Stage 3c
- **Purpose:** Ensure the draft has sufficient statistics, expert quotes, and source citations to maximize AI citability. This is the single highest-impact AEO lever.
- **Build Priority:** #3 (third agent to build)

## Why This Agent Is Critical
GEO research data:
- Quotations/citation-rich content: **+41% visibility**
- Statistics & quantitative data: **+33% visibility**
- Source citation density: **+28% visibility**

This is the #1 lever for AEO and needs a dedicated agent to ensure no article ships under-cited.

## Inputs
- Draft from C3
- Research packet from C1
- Content brief from B3 (minimum citation requirements)

## Process

### Step 1: Citation Audit
Count in the current draft:
- Number of statistics with sources
- Number of expert quotes with attribution
- Number of "According to [Source]" citations
- Number of first-person data references
- Number of Evidence Sandwich blocks

### Step 2: Gap Analysis
Compare audit counts against brief's minimums:
- Overview articles: 3+ stats, 1+ quote, 3+ citations
- Detailed articles: 5+ stats, 2+ quotes, 5+ citations
- Comprehensive articles: 8+ stats, 3+ quotes, 8+ citations

### Step 3: Enrichment
Where gaps exist:
1. **Statistics injection:** Find and add relevant statistics using "According to [Source], [stat with number and timeframe]" format
2. **Expert quote injection:** Add expert quote blocks: "[Quote]," says [Name], [Title] at [Org]
3. **Evidence Sandwich insertion:** Where claims lack backing, add: Claim → 3 data points with sources → Actionable conclusion
4. **Source citation addition:** Add "According to" references throughout

### Step 4: Verification
- Verify all added citations have real, verifiable sources
- Ensure citations are contextually relevant (not shoehorned)
- Check citation density feels natural, not stuffed

## Output
**Citation-Enriched Draft** with:
- All citation minimums met or exceeded
- Citations distributed naturally throughout (not clustered)
- Every major claim backed by data
- Audit counts documented for D1 evaluator

## Constraints
- Never fabricate statistics or quotes
- Citations must be contextually relevant — not shoehorned
- Maintain natural reading flow — enrichment shouldn't feel forced
- All sources must be verifiable and credible
- Avoid over-citation (diminishing returns above ~15 citations per article)

## Dependencies
- **Upstream:** C3 (draft to enrich), C1 (research packet for additional sources)
- **Downstream:** C5 (composer merges enriched draft)

## Skills Repo Reference
- `ai-seo/references/content-patterns.md` — Statistic Citation Block, Expert Quote Block, Evidence Sandwich Block

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |

### Example: before-after-enrichment
# C4 Citation Enrichment Example: Formative Assessment Strategies

This example shows a section BEFORE and AFTER citation enrichment, demonstrating the audit → gap analysis → enrichment process.

---

## Citation Audit (Before)

**Section analyzed:** "Why does formative assessment matter?"

**Current counts:**
- Statistics with sources: 1 (vague — "studies show")
- Expert quotes with attribution: 0
- "According to [Source]" citations: 0
- First-person data references: 0
- Evidence Sandwich blocks: 0

**Brief requirements (Detailed depth):**
- Min 5 stats, 2 quotes, 5 citations overall
- This section should carry at least 2 stats and 1 quote

**Gap:** Missing 1+ stat with source, 1 expert quote, "According to" framing

---

## BEFORE (Under-cited Draft)

> ### Why Does Formative Assessment Matter?
>
> Formative assessment is one of the most impactful teaching practices available. Studies show that it significantly improves student learning outcomes.
>
> When teachers check understanding during a lesson rather than only at the end, they can catch misconceptions early and adjust their approach. This leads to better results for students across all grade levels.
>
> Formative assessment also increases student engagement. Students who receive regular feedback tend to be more motivated and take greater ownership of their learning.

**Problems:**
- "Studies show" — no specific source
- No statistics with numbers
- No expert quotes
- No "According to" framing
- No first-person WG signals
- Claims without evidence backing

---

## AFTER (Citation-Enriched Draft)

> ### Why Does Formative Assessment Matter?
>
> Formative assessment is one of the most impactful teaching strategies available. According to John Hattie's meta-analysis of over 1,400 studies, formative evaluation has an effect size of 0.73 — placing it among the top 10 influences on student achievement.
>
> When teachers check understanding during a lesson rather than only at the end, they can catch misconceptions early and adjust their approach. A landmark meta-analysis by Black and Wiliam (1998) found that formative assessment practices produced learning gains equivalent to 8 months of additional progress, with the largest effects for lower-achieving students.
>
> "The most powerful single modification that enhances achievement is feedback," says Professor John Hattie, Director of the Melbourne Education Research Institute. "But it must be feedback that helps students understand where they are and where they need to go."
>
> Formative assessment also increases student engagement. According to a 2023 EdWeek Research Center survey, 78% of teachers who use formative assessment daily report higher student participation compared to those who assess only at unit's end. Based on 200M+ activities on Wayground, educators who use quick polls and exit tickets see 34% higher completion rates than traditional end-of-unit tests.

**What changed:**
1. **Statistic injection:** Added Hattie effect size (0.73) with source attribution
2. **Statistic injection:** Added Black & Wiliam finding (8 months progress) with year
3. **Expert quote injection:** Added Hattie quote with full attribution (name, title, org)
4. **"According to" framing:** Added for EdWeek survey with specific number (78%)
5. **First-person data:** Added Wayground platform stat ("Based on 200M+ activities")
6. **Evidence density:** Section went from 0 citations to 5 trust signals

---

## Enrichment Principles Demonstrated

### 1. Statistic Citation Block
**Pattern:** "According to [Source] ([Year/Context]), [specific finding with number]."
```
According to John Hattie's meta-analysis of over 1,400 studies, formative evaluation
has an effect size of 0.73.
```

### 2. Expert Quote Block
**Pattern:** "[Insight quote]," says [Full Name], [Title] at [Organization].
```
"The most powerful single modification that enhances achievement is feedback,"
says Professor John Hattie, Director of the Melbourne Education Research Institute.
```

### 3. Evidence Sandwich
**Pattern:** Claim → 2-3 data points with sources → Actionable conclusion.
```
Claim: Formative assessment increases engagement.
Data 1: EdWeek survey — 78% of daily users report higher participation.
Data 2: Wayground data — 34% higher completion with polls/exit tickets.
Conclusion: (implied) Regular formative checks drive measurably better engagement.
```

### 4. First-Person Signal
**Pattern:** "Based on [WG data point], [finding]."
```
Based on 200M+ activities on Wayground, educators who use quick polls and exit
tickets see 34% higher completion rates.
```

---

## Post-Enrichment Audit

**Updated counts for this section:**
- Statistics with sources: 4 ✅ (was 0)
- Expert quotes with attribution: 1 ✅ (was 0)
- "According to [Source]" citations: 2 ✅ (was 0)
- First-person data references: 1 ✅ (was 0)
- Evidence Sandwich blocks: 1 ✅ (was 0)

**Verification checklist:**
- [x] All statistics are from real, verifiable sources
- [x] Citations are contextually relevant (not shoehorned)
- [x] Reading flow feels natural, not stuffed
- [x] Expert quote adds genuine insight, not filler
- [x] First-person data is specific and credible

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


#### C3 Output

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

According to Mary Budd Rowe's foundational research on wait time, students who receive three or more seconds of processing time before speaking produce longer, more accurate, and more elaborated answers. Skipping think time is the single most common reason Turn and Talk stays surface-level.

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

According to research published in the *TESOL Journal*, scaffolded peer discussion — where ELL students receive structured language supports before producing academic language — produces measurable gains in both oral language development and content comprehension compared to teacher-directed instruction alone.

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

The cognitive case for Turn and Talk is well-established across several research traditions.

Lev Vygotsky's theory of the Zone of Proximal Development (ZPD) offers a foundational explanation: students learn best when they work just beyond their current independent ability level — and a more capable peer is often the most accessible scaffold available in a classroom. Building directly on this framework, researchers Suzanne Michaels, Cathy O'Connor, and Lauren Resnick developed the *accountable talk* framework, which identifies structured peer discussion as central to disciplinary reasoning. Their research documents how purposeful talk — accountable to the community, to accurate knowledge, and to rigorous thinking — deepens comprehension in ways that listening alone does not.

According to Noreen Webb's research on peer interaction and learning gains, students who give and receive elaborated explanations during peer discussion show significantly greater learning gains than students who engage in unelaborated exchange or receive instruction without discussion. The elaboration — the "because," the "what do you mean by that" — is the mechanism, not the talking itself.

According to John Hattie's *Visible Learning* synthesis of more than 800 meta-analyses, classroom discussion ranks among the more effective instructional strategies available to teachers — a finding that holds across subject areas and grade levels.

Consider the participation math. In a whole-class discussion with 30 students, only one student speaks at a time — a 3% active-participation rate per moment. A Turn and Talk activates all 15 pairs simultaneously, producing a 100% active-participation rate for the duration of the exchange.

*"The research is unambiguous: students consolidate new learning by talking through it, not just by hearing it. Peer discussion is not an add-on — it is the mechanism by which instruction becomes learning."* — **[Expert Quote #1: Attribution required — suggested source: Dylan Wiliam, Noreen Webb, or Lauren Resnick; format: [Quote], [Name], [Title], [Institution]; to be confirmed from published source or Wayground teacher vetting network]**

*"Turn and Talk changed how I thought about my own talk time in the room. When I stopped filling every pause with my voice, my students started doing the thinking I'd been doing for them."* — **[Expert Quote #2: Practitioner attribution required — [Name], [Grade] teacher at [School], [City]; to be sourced from Wayground's teacher vetting network]**

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

Turn and Talk increases participation equity — every student processes content simultaneously rather than waiting for one classmate to respond. Research on peer interaction consistently shows positive effects on content comprehension and verbal reasoning. Students also rehearse academic language, reduce anxiety before whole-class sharing, and practice the listening and responding habits that transfer across every subject area.

**How is Turn and Talk different from Think-Pair-Share?**

Turn and Talk is shorter and more spontaneous — it pauses instruction for a quick partner exchange and returns to whole class within minutes. Think-Pair-Share adds an individual writing step before partner discussion and a structured whole-class share-out after. Turn and Talk is the lower-lift version for quick processing checks; Think-Pair-Share produces a richer written artifact. See the full comparison table in Section 1.

**When should teachers use Turn and Talk during a lesson?**

Three natural placement windows exist in any lesson: warm-up before new content (to activate prior knowledge); mid-lesson after a key explanation (to check and deepen understanding); and exit consolidation before dismissal (to synthesize learning). Each window calls for a different prompt type and duration. See the lesson placement table in Section 3.

**How do you make Turn and Talk work for English language learners or shy students?**

For ELLs: provide sentence frame scaffolds from the tables in Section 4, allow brief L1 clarification with a same-language partner, and display key vocabulary with visuals before the prompt. For shy or introverted students: add 30 seconds of written response time before the partner turn, pre-assign stable partners, and extend think time to 15 seconds minimum. See the full adaptation protocols in Section 5.

**How long should a Turn and Talk last?**

Duration depends on the lesson phase: 90 seconds for warm-up activation prompts; 2–3 minutes for mid-lesson processing prompts; 3–4 minutes for exit consolidation or synthesis prompts. When in doubt, run shorter — focused 90-second partner talk produces better discussions than open-ended conversations without a visible countdown. See the Duration Guide table in Section 2.

---

*About the author: [Author Name] holds an Ed.D. in [Field] and has [X] years of K-12 classroom experience. [Two-sentence bio with institutional affiliation and subject/grade specialization.]*

*Last updated: March 2026*

---

## C3 Draft Flags for Downstream Agents

> **[C3 → C4, C5, D1]** The following items require confirmation or sourcing before the draft is finalized:

1. **Expert Quote #1** (Section 7) — Researcher attribution required. Suggested sources: Dylan Wiliam, Noreen Webb, Lauren Resnick. Format: `"[Quote]," says [Name], [Title], [Institution].` Source from published work or Wayground's educator network.

2. **Expert Quote #2** (Section 7) — Practitioner attribution required. Format: `"[Quote]," says [Name], [Grade] teacher at [School], [City].` Must come from Wayground's ~30-teacher vetting network for E-E-A-T signal.

3. **WG Platform Stat** (B3 Attr #5) — [DATA NEEDED]. Both instances where this was planned have been replaced with research-backed framing. If UXR data becomes available ("X% of Team Mode sessions had 90%+ pair completion"), insert in Section 7 with "Based on Wayground's platform data…" framing.

4. **TESOL Journal citation** (Section 5, ELL subsection) — The citation is directionally accurate but requires a specific article reference. C4 should verify: Swain & Lapkin (1998), or comparable scaffolded peer discussion ELL study from TESOL Quarterly or Bilingual Research Journal.

5. **Hattie effect size** (Section 7) — Referenced as "among the more effective strategies" per *Visible Learning*. C4 may insert the specific effect size for classroom discussion (d = 0.82, Hattie 2009/2012) if confirmed against the current edition.

6. **Product URL** — `/features/team-mode` used as specified in B3. Confirm this URL resolves before final publish.

7. **Internal link targets** — `/learn/strategies/think-pair-share`, `/learn/engagement/cold-calling-alternatives`, `/learn/strategies/collaborative-learning`, `/learn/engagement/exit-tickets`, `/activities/discussion` — all flagged for URL verification before publish per B3 guidance.

8. **Word count estimate** — Approximately 2,900–3,100 words. Within target range (2,800–3,500). Section 9 (grade-band table) was included; compress or move to FAQ if D1 review identifies any sections as over-specified.

---
Now execute your task. **IMPORTANT: Wrap your entire output in `<output>` and `</output>` tags.** Your output begins with `<output>` on its own line and ends with `</output>` on its own line. Everything between those tags is your deliverable.
