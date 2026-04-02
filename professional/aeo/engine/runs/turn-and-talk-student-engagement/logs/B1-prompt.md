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

# B1: Intent Classifier Agent

## Identity
- **Phase:** B — Content Planning
- **Stage:** Stage 1b
- **Purpose:** Classify the intent behind each target query to determine the required content format.

## Inputs
- Priority question from A1
- Current AI answers and citation data from A2

## Process

### Step 1: Intent Classification
Classify each query into one of:

| Intent Type | Signal Words | Example |
|------------|-------------|---------|
| **Informational** | "what is", "definition", "explain" | "What is formative assessment?" |
| **Comparison** | "vs", "versus", "compared to", "difference" | "Kahoot vs Blooket for classrooms" |
| **Recommendation** | "best", "top", "recommended" | "Best formative assessment tools for teachers" |
| **How-to** | "how to", "steps", "guide", "tutorial" | "How to create a formative assessment" |
| **Transactional** | "pricing", "signup", "free", "download" | "Wayground pricing for schools" |

### Step 2: Required Format Mapping
Based on intent, define required content elements:

| Intent | Required Format Elements |
|--------|------------------------|
| Informational | Definition in first paragraph, expansion, FAQ section |
| Comparison | Comparison table with criteria rows, "Best For" row, bottom-line verdict |
| Recommendation | Ranked list, criteria explanation, top pick highlighted |
| How-to | Numbered steps, bolded step names, outcome per step |
| Transactional | CTA placement, pricing/feature info, trust signals |

### Step 3: Depth Assessment
Determine required depth:
- **Overview:** 800-1200 words — broad topic, surface-level
- **Detailed:** 1500-2500 words — specific topic, moderate depth
- **Comprehensive:** 2500-4000 words — pillar content, full coverage

## Output
- Intent label (one of 5 types)
- Required content format elements
- Depth level recommendation
- Confidence score (high/medium/low)

## Constraints
- A query can have mixed intents — classify by PRIMARY intent
- When confidence is low, flag for human review
- Intent classification directly determines format — getting this wrong cascades downstream

## Dependencies
- **Upstream:** A1 (questions), A2 (AI answer context)
- **Downstream:** B2 (uses intent for decomposition), B3 (uses intent for brief format)

## Skills Repo Reference
- `content-strategy` — buyer stage mapping

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |

---
## Task Payload

**Topic:** Turn and Talk: A Quick Guide to Increasing Student Engagement

### Upstream Agent Outputs

#### A1 Output

# Topic Dossier: Turn and Talk: A Quick Guide to Increasing Student Engagement

> Stage 1 output — produced by A1 agent

## Metadata
| Field | Value |
|-------|-------|
| Topic | Turn and Talk: A Quick Guide to Increasing Student Engagement |
| Date created | 2026-03-20 |
| AEO Opportunity Score | 432 / 1000 |
| Intent type | How-to / Informational |
| Target URL | `/learn/engagement/turn-and-talk` |
| Priority | P2 |
| Status | Ready for Brief |

> **Data note:** DataForSEO API calls were not authorized during this run. Volume estimates, competitor URLs, and citation data below are based on domain research and AI engine behavioral patterns for this topic cluster. Live data pull recommended before final scoring.

---

## Primary Question
**What is the "Turn and Talk" strategy and how does it increase student engagement?**

### Variant Phrasings
1. How do you do a "turn and talk" in the classroom?
2. What are the benefits of turn and talk for students?
3. How is turn and talk different from think-pair-share?
4. When should teachers use turn and talk during a lesson?
5. How do you make turn and talk work for English language learners or shy students?

---

## Intent Classification
- **Type:** How-to / Informational
- **Required format:** Definition → steps → use cases → variations → tips — a hybrid guide format with scannable sections
- **Depth level:** Detailed

---

## AI Answer Landscape

### Current Citations (who gets cited?)
| AI Engine | Cited Source | URL | Why Cited (structure/authority/data) |
|-----------|-------------|-----|--------------------------------------|
| ChatGPT | Edutopia | edutopia.org/article/discussion-strategies-classroom | High domain authority, long-standing trust signal, well-structured definition + steps |
| ChatGPT | Cult of Pedagogy | cultofpedagogy.com/speaking-listening-technique | Practitioner voice, specific step-by-step, widely linked |
| Perplexity | TeachThought | teachthought.com/pedagogy/turn-and-talk | Pedagogical depth, question framing, research references |
| Perplexity | Reading Rockets | readingrockets.org | Literacy-specific authority, .org TLD trust boost |
| Google AIO | Edutopia | edutopia.org | Appears in AI Overviews for "classroom discussion strategies" cluster |
| Google AIO | Understood.org | understood.org | Differentiation angle (UDL / diverse learners) cited for accessibility angle |

> **Citation confidence:** Medium. Requires live ChatGPT/Perplexity query verification. Pattern inferred from AI citation behavior for comparable pedagogy-strategy topics.

### Gaps & Opportunities
- **What's missing from current AI answers:**
  - Concrete timing guidance (how many minutes for turn-and-talk vs. full discussion)
  - Structured prompts teachers can copy-paste immediately
  - Adaptation protocols for ELLs, introverted students, and students with IEPs
  - Data or research backing the engagement lift (most sources cite theory, not numbers)
  - Digital/hybrid classroom implementation — most advice assumes in-person only

- **What WG can uniquely provide:**
  - Integration of Wayground's collaborative activity types (e.g., live Q&A, team mode) as a natural digital analog to turn and talk
  - "We tested with X teachers" framing if UXR data exists
  - Ready-made Wayground activity links teachers can use immediately after reading
  - Teacher community quotes / testimonials from Wayground's existing network (~30 vetted teachers)

- **Source domains AI trusts but WG is absent from:**
  - Edutopia (link-earning opportunity via contributed content or backlinks)
  - TeachThought (guest post or citation opportunity)
  - ReadingRockets (literacy-specific, less applicable but high trust)

---

## EAR Attribute List
> Sub-questions a comprehensive answer must cover

| # | Attribute / Sub-question | Must-cover? | Covered by competitors? |
|---|--------------------------|-------------|------------------------|
| 1 | What is turn and talk? (clear 1-paragraph definition) | Yes | Yes — but often vague |
| 2 | How does it differ from think-pair-share? | Yes | Partial — few sources draw a clean distinction |
| 3 | Step-by-step implementation (exact teacher moves) | Yes | Yes — Cult of Pedagogy does this well |
| 4 | When in a lesson is it most effective? (warm-up, mid-lesson, exit) | Yes | Partial |
| 5 | How long should a turn-and-talk last? (timing guidance) | Yes | No — consistently missing |
| 6 | Adaptations for ELLs, shy students, students with IEPs | Yes | Partial — Understood.org covers IEPs loosely |
| 7 | How to use turn and talk in hybrid/digital classrooms | Yes | No — strong gap |
| 8 | Sentence starters / discussion prompts teachers can use immediately | Yes | Partial — few include copy-paste-ready prompts |
| 9 | Research backing: why it works (cognitive load, retrieval, social learning) | Nice-to-have | Partial — cited loosely, not sourced |
| 10 | Common mistakes and how to avoid them | Nice-to-have | No — consistent gap across all sources |

---

## Competitor Content Analysis

### Top Cited Sources
| Source | URL | Structure | Strengths | Weaknesses |
|--------|-----|-----------|-----------|------------|
| Edutopia | edutopia.org/article/discussion-strategies-classroom | Long-form listicle; turn-and-talk is one of many strategies | High E-E-A-T, widely cited, trusted by AI | Turn-and-talk is buried — not the focus; no timing guidance |
| Cult of Pedagogy | cultofpedagogy.com | Step-by-step practitioner guide | Warmly written, teacher-voice, specific steps | No research citations; limited adaptations for diverse learners |
| TeachThought | teachthought.com | Conceptual + how-to hybrid | Strong on pedagogy rationale | Abstract; limited practical prompts |
| Understood.org | understood.org | Differentiated learning focus | Excellent UDL / IEP angle | Narrow focus; not a comprehensive turn-and-talk guide |
| ReadingRockets | readingrockets.org | Literacy strategy framing | High domain authority (.org) | Literacy-only lens; not generalist enough |

---

## Internal Assets
- **Existing WG pages on this topic:** None confirmed — no `/learn/engagement/turn-and-talk` or equivalent indexed page identified
- **Related ADPs/resources:** Wayground likely has collaborative quiz/discussion activity templates that serve as a digital turn-and-talk analog (e.g., Team Mode, Live Q&A activities) — verify in product catalog
- **Related /learn/ hub pages:** `/learn/engagement/` hub (if live); `/learn/strategies/collaborative-learning`
- **Enhance existing vs. create new:** **Create new** — no existing WG asset to enhance; this is a net-new content opportunity in a gap the competitors haven't fully closed

---

## AEO Opportunity Score Calculation
```
AI Volume:         6 / 10
  (Moderate — "turn and talk" is queried regularly in teacher/pedagogy 
   AI prompts; not a top-10 edu topic but steady demand in 
   classroom strategy clusters)

× Intent Relevance: 8 / 10
  (Strong fit — informational + how-to intent maps cleanly to 
   Wayground's educator audience and /learn/ content model)

× Brand Fit:        9 / 10
  (Excellent — WG has collaborative learning tools that directly 
   instantiate this strategy; clear product connection without 
   being forced)

= Score: 432 / 1000
```

**Scoring rationale:** AI volume is the main ceiling here — "turn and talk" is a mid-tier pedagogy term, not a breakout query. But the intent-brand alignment is very high, and the **content gap is real**: no single source fully covers timing, digital adaptation, and copy-paste prompts in one place. A comprehensive WG article could realistically become the best resource on the web for this specific query cluster, which is the citation capture play.

**Priority: P2** — Proceed to brief, but sequence after any P1 items in the engagement cluster. If teacher community testimonials or UXR data are available, elevate to P1.

#### A2 Output

# Topic Dossier: Turn and Talk: A Quick Guide to Increasing Student Engagement

> Stage 1 output — produced by A1, A2 agents

## Metadata
| Field | Value |
|-------|-------|
| Topic | Turn and Talk: A Quick Guide to Increasing Student Engagement |
| Date created | 2026-03-20 |
| AEO Opportunity Score | 432 / 1000 (A1 baseline; see A2 adjustments below) |
| Intent type | How-to / Informational |
| Target URL | `/learn/engagement/turn-and-talk` |
| Priority | P2 |
| Status | Ready for Brief |

> **A2 Data note:** DataForSEO and AI scraper APIs were not authorized during this run. The citation audit below is reconstructed from (a) A1 upstream data, (b) direct structural knowledge of the cited domains, and (c) AI engine citation behavioral patterns for this pedagogy strategy cluster. All competitor structure analysis is based on known content of these domains as of early 2026. Live query verification recommended before final scoring.

---

## Primary Question
**What is the "Turn and Talk" strategy and how does it increase student engagement?**

### Variant Phrasings
1. How do you do a "turn and talk" in the classroom?
2. What are the benefits of turn and talk for students?
3. How is turn and talk different from think-pair-share?
4. When should teachers use turn and talk during a lesson?
5. How do you make turn and talk work for English language learners or shy students?

---

## Intent Classification
- **Type:** How-to / Informational
- **Required format:** Definition → steps → use cases → variations → tips — hybrid guide with scannable sections, copy-paste prompts, and a comparison table
- **Depth level:** Comprehensive

---

## AI Answer Landscape

### Current Citations (who gets cited?)

| AI Engine | Cited Source | URL | Why Cited (structure/authority/data) |
|-----------|-------------|-----|--------------------------------------|
| ChatGPT | Edutopia | edutopia.org/article/discussion-strategies-classroom | Domain authority ~75+, cited by AI for virtually all classroom discussion strategy queries; turn-and-talk appears as one named strategy in a listicle format AI can extract |
| ChatGPT | Cult of Pedagogy | cultofpedagogy.com/speaking-listening-technique | Practitioner voice with a clearly structured "how to run it" section; widely backlinked from teacher blogs; strong first-person authority signals |
| ChatGPT | ThoughtCo | thoughtco.com/think-pair-share-p2-3110824 | Comparison queries surface this page because it defines think-pair-share cleanly — AI conflates/connects the two strategies |
| Perplexity | TeachThought | teachthought.com/pedagogy/turn-and-talk | Explicit pedagogy rationale; heading structure matches question-phrased queries; references Vygotsky and ZPD (trust signal for AI) |
| Perplexity | Reading Rockets | readingrockets.org | .org TLD, NICHD-funded, literacy authority; cited for "turn and talk during read-aloud" sub-query; very clean extractable definitions |
| Perplexity | The Classroom Key | theclassroomkey.com | Elementary-specific practitioner blog; cited for "turn and talk primary grades" variants; specific grade-level examples |
| Google AIO | Edutopia | edutopia.org | Consistently appears in AI Overviews for the "classroom discussion strategies" cluster; Google trusts Edutopia for all K-12 pedagogy queries |
| Google AIO | Understood.org | understood.org/articles/classroom-strategies-for-students-with-learning-disabilities | UDL/differentiation angle; cited specifically for "turn and talk for students with learning differences"; .org + non-profit trust halo |
| Google AIO | Colorín Colorado | colorincolorado.org | ELL-specific authority; cited for "turn and talk for English language learners"; bilingual education focus gives it a lane competitors can't match |

---

### Citation Pattern Analysis

**What these sources have in common structurally:**

| Structural Signal | Edutopia | Cult of Pedagogy | TeachThought | Understood.org | Reading Rockets |
|-------------------|----------|-----------------|--------------|----------------|-----------------|
| Question-phrased H2s | Partial | Yes | Yes | Yes | No |
| Extractable definition block (40-80 words) | Yes | Yes | Partial | Yes | Yes |
| Numbered step list | No | Yes | Partial | No | No |
| Named research citations | Partial | No | Yes (Vygotsky) | Yes | Yes |
| Sentence starters / prompts | No | Yes | No | No | Partial |
| Timing guidance | No | No | No | No | No |
| Differentiation section | No | No | No | Yes | No |
| Digital classroom adaptation | No | No | No | No | No |
| Schema / structured data | Basic | Basic | None | Basic | Basic |
| Author credential display | Yes | Yes | No | Yes | No |

**Key insight:** No single cited source scores above 4/10 on this combined rubric. The citation field is fragmented — AI engines are stitching together answers from multiple sources because no one page covers the full terrain.

---

### Gaps & Opportunities

**What's missing from current AI answers:**
- Concrete timing guidance — how many minutes is optimal for turn-and-talk vs. think-pair-share vs. Socratic seminar? (Absent across all top 5 sources)
- Structured sentence starters teachers can copy-paste immediately (only Cult of Pedagogy offers any; none are comprehensive)
- Explicit protocol for shy or introverted students beyond "choose partners carefully"
- Adaptation protocols for ELLs with scaffolded L1 → L2 progression guidance
- IEP/504 accommodation examples for turn-and-talk in inclusive classrooms
- Digital and hybrid classroom implementation (none of the top sources address synchronous online or async variants)
- Research citations with actual effect size data (most sources cite Vygotsky conceptually, not quantitatively)
- Common implementation mistakes with specific corrective moves (no source covers this)
- Grade-band differentiation (what works in K-2 vs. 6-8 vs. 9-12 looks very different; sources are mostly elementary-centric)

**What Wayground can uniquely provide:**
- Wayground's Team Mode and Live Q&A activity types are a digital analog to turn-and-talk — WG can own the "digital turn-and-talk" lane with a product connection that is genuinely value-adding
- "We tested this with X teachers" authority framing if UXR data or teacher community feedback exists (the ~30-teacher vetting network is the differentiator here)
- Ready-to-use Wayground activity links as the "try it now" CTA — no competitor can offer this
- Teacher community quotes from real educators with name + school attribution (trust signal competitors cannot replicate)
- The only comprehensive resource covering: timing + prompts + ELL adaptations + digital implementation + IEP accommodations in one place

**Source domains AI trusts but WG is absent from:**
- Edutopia — highest leverage; a backlink or cited contribution here would create a trust bridge
- Colorín Colorado — niche but strong for ELL sub-query; worth monitoring
- Reading Rockets — literacy angle; less relevant to WG's general engagement frame but worth noting
- TeachThought — open to guest contributors; an A2-identified link-earning opportunity

---

## EAR Attribute List
> Sub-questions a comprehensive answer must cover

| # | Attribute / Sub-question | Must-cover? | Covered by competitors? | A2 Priority |
|---|--------------------------|-------------|------------------------|-------------|
| 1 | What is turn and talk? (clean 1-paragraph definition, AI-extractable) | Yes | Yes — but vague or buried | Rewrite the definition. 40-60 word extractable block. |
| 2 | How does it differ from think-pair-share? (comparison) | Yes | Partial — ThoughtCo touches it, no clean comparison table exists | Own this with a 3-column comparison table |
| 3 | Step-by-step implementation (exact teacher moves, numbered) | Yes | Cult of Pedagogy does this reasonably well | Match depth + add timing column |
| 4 | When in a lesson is it most effective? (warm-up / mid-lesson / exit) | Yes | Partial — most sources don't specify placement | Create a lesson-placement decision tree |
| 5 | How long should a turn-and-talk last? (specific timing guidance) | Yes | No — consistently absent across all sources | First-mover advantage: own this with specific ranges |
| 6 | Sentence starters and discussion prompts (copy-paste ready) | Yes | Partial — only CoP offers any | Provide 10-15 categorized by subject/grade |
| 7 | Adaptations for ELLs (scaffolded language support) | Yes | Partial — Colorín Colorado covers this narrowly | Full section with L1/L2 scaffold strategy |
| 8 | Adaptations for shy/introverted students and students with IEPs | Yes | Partial — Understood.org covers IEPs loosely | Practical UDL-aligned adaptations |
| 9 | How to use turn and talk in hybrid and digital classrooms | Yes | No — strong gap, no source covers this | Digital-specific section; connect to Wayground Team Mode |
| 10 | Research backing: effect sizes, cognitive rationale | Nice-to-have | Partial — Vygotsky cited conceptually, no quantitative data | 2-3 sourced citations with effect direction if available |
| 11 | Common mistakes and corrective moves | Nice-to-have | No — consistent gap | Mistake → fix pairs; high shareability |
| 12 | Grade-band differentiation (K-2 vs. 3-5 vs. 6-8 vs. 9-12) | Nice-to-have | No — most sources default to elementary | Quick band-specific tips table |

---

## Competitor Content Analysis

### Top Cited Sources — Deep Structure Map

**1. Edutopia — `edutopia.org/article/discussion-strategies-classroom`**
| Attribute | Detail |
|-----------|--------|
| Structure | Long-form listicle: ~12 discussion strategies, turn-and-talk is #3 of 12 |
| Word count (estimated) | 2,200–2,800 words total; ~180 words on turn-and-talk specifically |
| Turn-and-talk coverage | Definition + 1 example; no steps, no timing, no adaptations |
| Trust signals | Author byline with credentials (Ed.D. or equivalent), publication date, Edutopia brand |
| Schema markup | Article schema; no FAQ schema |
| AEO extractability | Medium — definition block is extractable but not optimized; AI pulls it because of domain trust, not content quality |
| Wayground gap to close | High — Edutopia's turn-and-talk section would score ~2/10 on the EAR attribute list. WG can outperform on content depth dramatically. |

---

**2. Cult of Pedagogy — `cultofpedagogy.com/speaking-listening-technique`**
| Attribute | Detail |
|-----------|--------|
| Structure | Single-strategy guide: intro → rationale → how-to steps → variations |
| Word count (estimated) | 1,400–1,800 words |
| Turn-and-talk coverage | Dedicated page — best single-topic coverage in the competitive set |
| Trust signals | Jennifer Gonzalez author voice; practitioner credibility; heavily linked by teacher blogs |
| Schema markup | None observed |
| AEO extractability | High — numbered steps are clean AI extraction targets; the "how to run it" section is likely what ChatGPT cites |
| Gaps | No research citations, no timing specifics, no ELL/IEP adaptations, no digital implementation, no sentence starters beyond 2-3 examples |
| Wayground gap to close | Medium — CoP has the best structure in the set but leaves 7 of 12 EAR attributes uncovered. WG beats it by covering the full attribute list. |

---

**3. TeachThought — `teachthought.com/pedagogy/turn-and-talk`**
| Attribute | Detail |
|-----------|--------|
| Structure | Conceptual overview + rationale + brief how-to |
| Word count (estimated) | 900–1,200 words |
| Turn-and-talk coverage | Dedicated page; pedagogical framing references ZPD/Vygotsky |
| Trust signals | Vygotsky citation; established edtech brand; referenced in teacher Twitter/X |
| Schema markup | Minimal |
| AEO extractability | Medium — question-phrased headings help; content is abstract and harder to extract into step sequences |
| Gaps | Abstract; no sentence starters, no timing, no adaptations, limited practical application |
| Wayground gap to close | Low effort — TeachThought sets the bar low on practical depth |

---

**4. Understood.org — `understood.org`**
| Attribute | Detail |
|-----------|--------|
| Structure | Differentiated learning strategy pages; turn-and-talk appears within UDL strategy collections |
| Word count (estimated) | 600–900 words per strategy |
| Turn-and-talk coverage | Partial — framed through the lens of supporting students with learning differences |
| Trust signals | Non-profit, .org TLD, expert advisory board, NCLD affiliation |
| Schema markup | Basic article schema |
| AEO extractability | High for differentiation queries specifically; narrow lane |
| Gaps | Not a comprehensive turn-and-talk guide; misses typical classroom implementation; no digital angle |
| Wayground gap to close | Low for the differentiation lane — WG should include an equal-depth differentiation section to neutralize Understood.org's advantage |

---

**5. Reading Rockets — `readingrockets.org`**
| Attribute | Detail |
|-----------|--------|
| Structure | Literacy strategy database entry format; very clean, short, extractable |
| Word count (estimated) | 300–500 words |
| Turn-and-talk coverage | Partial — framed as a read-aloud discussion strategy, not a general engagement tool |
| Trust signals | NICHD/federally funded, .org TLD, university partnerships |
| Schema markup | None observed |
| AEO extractability | High for literacy-specific queries; narrow lane |
| Gaps | Literacy-only lens; not applicable to math, science, social studies contexts; no digital angle |
| Wayground gap to close | Wayground should include a cross-subject framing that Reading Rockets cannot offer |

---

### Citation Concentration Map

```
High AI Trust + Broad Coverage:    Edutopia         → WG must outperform on depth
High AI Trust + Narrow Lane:       Understood.org   → WG must match on differentiation
Moderate Trust + Best Structure:   Cult of Pedagogy → WG must match structure + exceed scope
Moderate Trust + Best Rationale:   TeachThought     → WG should cite research more rigorously
Niche Authority:                   Reading Rockets  → WG should include literacy framing, not ignore
                                   Colorín Colorado → WG should include ELL section to capture this lane
```

---

## Internal Assets
- **Existing WG pages on this topic:** None confirmed — no `/learn/engagement/turn-and-talk` page exists; net-new opportunity
- **Related ADPs/resources:** Wayground Team Mode (digital analog to turn-and-talk partner work), Live Q&A activity type (structured whole-class discussion → turn-and-talk transition), collaborative quiz activities
- **Related /learn/ hub pages:** `/learn/engagement/` hub (verify if live); `/learn/strategies/collaborative-learning`; `/learn/strategies/think-pair-share` (if exists, link bidirectionally)
- **Enhance existing vs. create new:** **Create new** — no existing WG asset to enhance; this is a net-new content creation opportunity with a clear competitive gap to close

---

## AEO Opportunity Score

### A2 Adjustment to A1 Scoring

| Dimension | A1 Score | A2 Adjustment | Rationale |
|-----------|----------|---------------|-----------|
| AI Volume | 6/10 | → 6/10 | Confirmed: moderate query volume; steady but not breakout |
| Intent Relevance | 8/10 | → 8/10 | Confirmed: how-to intent maps cleanly to WG educator audience |
| Brand Fit | 9/10 | → 9/10 | Confirmed: WG Team Mode is a direct digital instantiation of the strategy |
| **Citation Gap Bonus** | n/a | **+0.5 (applied to score)** | No single source covers the full attribute list (12/12). First-mover to full coverage has real citation capture upside. |

```
AI Volume:         6 / 10
× Intent Relevance: 8 / 10
× Brand Fit:        9 / 10
= Base Score: 432 / 1000

Citation Gap Bonus: Applied qualitatively — 
  gap coverage potential upgrades realistic citation 
  capture probability from "possible" to "likely"
  if article covers all 12 EAR attributes.

Adjusted Priority: P2 (confirm P1 if teacher testimonial 
  or UXR data is available to add first-person authority signal)
```

---

## A2 Strategic Recommendations for Brief

1. **Structure the article to win the timing gap first.** The single highest-value addition across all competitors is specific timing guidance. A table like "Turn-and-Talk Duration by Lesson Phase" will be the most-cited passage.

2. **Build a 3-column comparison table: Turn-and-Talk vs. Think-Pair-Share vs. Cold Calling.** ThoughtCo currently owns the "how is it different" query loosely. A clean table takes that query away.

3. **Include 12-15 copy-paste sentence starters organized by subject area and grade band.** This is the single most shareable, linkable asset and has zero presence in the current citation landscape.

4. **Lead the digital classroom section with Wayground Team Mode.** This is the only place WG has a genuine product connection — one paragraph, natural mention, direct link to a relevant activity. Do not mention WG elsewhere unless a second natural fit appears.

5. **Cite Vygotsky's Zone of Proximal Development and at least one peer-reviewed study** (e.g., Michaels, O'Connor & Resnick on accountable talk, or Webb on peer interaction and learning). This closes the research gap TeachThought opens but doesn't fulfill.

6. **Structure for extraction:** Every major section should have a 40-60 word summary paragraph at the top. Question-phrased H2s throughout. One FAQ section at the bottom covering the 5 variant phrasings from A1.

7. **Priority link-earning targets identified:** Edutopia (high authority), TeachThought (open to external references), Colorín Colorado (ELL citation lane, possible outreach).

### Output Template
Use this template for your output:

# Topic Dossier: [Topic Name]

> Stage 1 output — produced by A1, A2, B1, B2 agents

## Metadata
| Field | Value |
|-------|-------|
| Topic | |
| Date created | |
| AEO Opportunity Score | |
| Intent type | |
| Target URL | `/learn/[category]/[topic]` |
| Priority | P1 / P2 / P3 |
| Status | Draft / Ready for Brief |

## Primary Question
**[Main question users ask about this topic]**

### Variant Phrasings
1.
2.
3.
4.
5.

## Intent Classification
- **Type:** Informational / Comparison / Recommendation / How-to / Transactional
- **Required format:** [table / steps / ranking / definition / etc.]
- **Depth level:** Overview / Detailed / Comprehensive

## AI Answer Landscape

### Current Citations (who gets cited?)
| AI Engine | Cited Source | URL | Why Cited (structure/authority/data) |
|-----------|-------------|-----|--------------------------------------|
| ChatGPT | | | |
| Perplexity | | | |
| Google AIO | | | |

### Gaps & Opportunities
- What's missing from current AI answers:
- What WG can uniquely provide:
- Source domains AI trusts but WG is absent from:

## EAR Attribute List
> Sub-questions a comprehensive answer must cover

| # | Attribute / Sub-question | Must-cover? | Covered by competitors? |
|---|--------------------------|-------------|------------------------|
| 1 | | Yes / Nice-to-have | Yes / Partial / No |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

## Competitor Content Analysis

### Top Cited Sources
| Source | URL | Structure | Strengths | Weaknesses |
|--------|-----|-----------|-----------|------------|
| | | | | |
| | | | | |
| | | | | |

## Internal Assets
- Existing WG pages on this topic:
- Related ADPs/resources:
- Related /learn/ hub pages:
- Enhance existing vs. create new:

## AEO Opportunity Score Calculation
```
AI Volume: [1-10]
× Intent Relevance: [1-10]
× Brand Fit: [1-10]
= Score: [X / 1000]
```

---
Now execute your task. **IMPORTANT: Wrap your entire output in `<output>` and `</output>` tags.** Your output begins with `<output>` on its own line and ends with `</output>` on its own line. Everything between those tags is your deliverable.
