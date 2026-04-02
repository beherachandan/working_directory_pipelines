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

# B2: EAR Decomposer Agent

## Identity
- **Phase:** B — Content Planning
- **Stage:** Stage 1e, 2a
- **Purpose:** Break down primary questions into sub-questions/attributes that a comprehensive answer must cover (Entity-Attribute-Relationship decomposition).

## Inputs
- Primary question
- Intent classification from B1
- Competitor content analysis from A2

## Process

### Step 1: Sub-question Decomposition
Use LLM to decompose the primary question into 8-15 sub-questions/attributes that a comprehensive answer must address.

Example for "What is formative assessment?":
1. Definition of formative assessment
2. Difference between formative and summative assessment
3. Types/examples of formative assessment
4. Benefits of formative assessment
5. How to implement formative assessment in the classroom
6. Best practices for formative assessment
7. Formative assessment tools and technology
8. Common challenges with formative assessment
9. Research/evidence supporting formative assessment
10. Formative assessment for different grade levels

### Step 2: Competitor Coverage Check
For each attribute, check:
- Do the top-cited competitors (from A2) cover this attribute?
- How deeply? (Mentioned / Addressed / Deep coverage)
- Where are the gaps WG can fill?

### Step 3: Coverage Target Setting
Classify each attribute:
- **Must-cover:** Core to answering the primary question. Omission = incomplete answer.
- **Nice-to-have:** Adds depth. Include if word count allows.
- **Differentiator:** Covered poorly by competitors — WG's opportunity to stand out.

### Step 4: Overlap Score Framework
Calculate target coverage:
```
Target EAR Score = (Must-cover attributes + Differentiators) / Total attributes
Minimum acceptable: 70% (maps to score of 7 in D1 evaluator)
```

## Output
**EAR Attribute List** containing:
- 8-15 sub-questions/attributes
- Must-cover vs. nice-to-have classification
- Competitor coverage status per attribute
- Differentiator flags
- Target coverage score

## Constraints
- Minimum 8 attributes per topic
- All sub-questions must be answerable within the topic scope
- Decomposition should mirror how AI engines break down queries during RAG retrieval

## Dependencies
- **Upstream:** B1 (intent determines decomposition approach), A2 (competitor analysis)
- **Downstream:** B3 (builds brief around EAR list), D1 (evaluates against EAR targets)

## Why This Agent Is Critical
AI engines decompose queries into sub-queries during RAG retrieval. Content that covers more attributes = higher probability of being the selected source. Creating an overlap score framework helps measure and optimize coverage systematically.

## Skills Repo Reference
- `content-strategy` — pillar/cluster model, topic decomposition

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

#### B1 Output

# Topic Dossier: Turn and Talk: A Quick Guide to Increasing Student Engagement

> Stage 1 output — produced by A1, A2, B1 agents

## Metadata
| Field | Value |
|-------|-------|
| Topic | Turn and Talk: A Quick Guide to Increasing Student Engagement |
| Date created | 2026-03-20 |
| AEO Opportunity Score | 432 / 1000 (base); citation gap bonus upgrades realistic capture probability |
| Intent type | **How-to (primary) / Informational (secondary)** |
| Target URL | `/learn/engagement/turn-and-talk` |
| Priority | P2 (elevate to P1 if teacher testimonials or UXR data confirmed) |
| Status | Ready for Brief |

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

### B1 Classification Decision

**Primary Intent: How-to**
**Secondary Intent: Informational**

**Rationale:** The dominant user need across all 5 variant phrasings is *implementation* — teachers want to know how to run this strategy, when to use it, and how to adapt it. The definitional/informational component ("what is it") is present but serves as scaffolding for the how-to, not the end goal. Classifying by primary intent: **How-to**.

| Classification Dimension | Assessment |
|--------------------------|------------|
| Primary intent | How-to |
| Secondary intent | Informational |
| Mixed-intent flag | Yes — definition layer required before steps |
| Confidence | **High** |
| Escalate for human review? | No |

> **Note on mixed intent:** The query "How is turn and talk different from think-pair-share?" introduces a Comparison sub-element. This does not override the primary classification but requires a comparison table as a required format element — see below.

---

### Required Format Elements

Based on the How-to (primary) + Informational (secondary) classification:

| Format Element | Source Intent | Required? | Notes |
|---------------|---------------|-----------|-------|
| Extractable definition block (40-60 words) | Informational | **Yes** | Must appear in first 200 words; AI snippet target |
| Numbered implementation steps with bolded step names | How-to | **Yes** | Core how-to element; each step should include a teacher move + expected outcome |
| Timing guidance column within steps (or dedicated table) | How-to | **Yes** | First-mover gap; most-cited passage potential |
| Comparison table: Turn-and-Talk vs. Think-Pair-Share vs. Cold Calling | Comparison sub-element | **Yes** | Owns the "how is it different" sub-query; 3-column minimum |
| Lesson-placement guidance (when to use: warm-up / mid-lesson / exit) | How-to | **Yes** | Decision framing, not just a list |
| Copy-paste sentence starters, categorized by subject/grade band | How-to | **Yes** | Highest shareability and link-earning potential; 12-15 minimum |
| Adaptation protocols: ELLs, shy/introverted students, IEP/504 | How-to | **Yes** | Covers Understood.org + Colorín Colorado citation lanes |
| Digital/hybrid classroom implementation section | How-to | **Yes** | Only WG can fully own this lane; Wayground Team Mode anchor |
| FAQ section (5 variant phrasings from A1) | Informational | **Yes** | Structured Q&A at bottom; question-phrased H2s throughout |
| Research backing with sourced citations | Informational | Nice-to-have | 2-3 citations with effect direction; Vygotsky + quantitative study |
| Common mistakes and corrective moves | How-to | Nice-to-have | High shareability; consistent gap across all competitors |
| Grade-band differentiation table (K-2 / 3-5 / 6-8 / 9-12) | How-to | Nice-to-have | Closes elementary-centric bias of competitor set |

**Section order (recommended for AI extraction and reader flow):**

1. AI-extractable definition block (top of article)
2. Turn-and-Talk vs. Think-Pair-Share comparison table
3. Step-by-step implementation protocol (with timing column)
4. When to use it: lesson placement guide
5. Sentence starters and discussion prompts (by subject/grade)
6. Adaptations: ELLs / shy students / IEP considerations
7. Digital and hybrid classroom implementation (Wayground anchor)
8. Research backing: why it works
9. Common mistakes and fixes (optional but high-value)
10. FAQ section (5 variant phrasings)

---

### Depth Level Recommendation

**Depth: Comprehensive (2,500–4,000 words)**

**Rationale for upgrading from A1's "Detailed" recommendation:**

| Factor | Weight | Assessment |
|--------|--------|------------|
| EAR attribute count | High | 12 attributes; 7 are "must-cover" — cannot achieve full coverage at Detailed depth |
| Competitor fragmentation | High | No single source scores above 4/10 on the combined rubric; comprehensive is the citation capture play |
| Required format elements | High | 9 required elements (including comparison table, sentence starters, adaptation protocols, digital section) push word count past 2,500 |
| Digital implementation section | Medium | This is an entirely uncovered gap requiring substantive new content, not a minor addition |
| Differentiation section | Medium | ELL + IEP + shy students = 3 sub-populations; each needs specific guidance to match Understood.org + Colorín Colorado depth |

> **B1 confidence in depth call: High.** The 12-attribute EAR list and 9 required format elements are structurally incompatible with a Detailed (1,500–2,500 word) article. A Detailed article would force the author to either skip required elements or produce inadequate coverage of each — both of which reduce citation probability. Comprehensive is the right call.

---

## AI Answer Landscape

### Current Citations (who gets cited?)

| AI Engine | Cited Source | URL | Why Cited (structure/authority/data) |
|-----------|-------------|-----|--------------------------------------|
| ChatGPT | Edutopia | edutopia.org/article/discussion-strategies-classroom | Domain authority ~75+; turn-and-talk appears as one of 12 strategies in a listicle; AI extracts the definition block due to domain trust |
| ChatGPT | Cult of Pedagogy | cultofpedagogy.com/speaking-listening-technique | Best structured "how to run it" section in the competitive set; numbered steps are clean AI extraction targets; heavily backlinked |
| ChatGPT | ThoughtCo | thoughtco.com/think-pair-share-p2-3110824 | AI surfaces this for comparison queries; defines think-pair-share cleanly and conflates/connects the two strategies |
| Perplexity | TeachThought | teachthought.com/pedagogy/turn-and-talk | Question-phrased headings; references Vygotsky and ZPD (AI trust signal for pedagogical authority) |
| Perplexity | Reading Rockets | readingrockets.org | .org TLD, NICHD-funded; clean extractable definitions; cited for "turn and talk during read-aloud" sub-query |
| Perplexity | The Classroom Key | theclassroomkey.com | Elementary-specific practitioner blog; grade-level examples trigger citation for "primary grades" variants |
| Google AIO | Edutopia | edutopia.org | Consistently in AI Overviews for "classroom discussion strategies" cluster; Google's default K-12 pedagogy trust anchor |
| Google AIO | Understood.org | understood.org/articles/classroom-strategies-for-students-with-learning-disabilities | UDL/differentiation angle; .org + non-profit trust; cited for "turn and talk for students with learning differences" |
| Google AIO | Colorín Colorado | colorincolorado.org | ELL-specific authority; cited for "turn and talk for English language learners"; bilingual education lane competitors cannot replicate |

### Citation Pattern: Structural Analysis

| Structural Signal | Edutopia | Cult of Pedagogy | TeachThought | Understood.org | Reading Rockets |
|-------------------|:--------:|:---------------:|:------------:|:--------------:|:---------------:|
| Question-phrased H2s | Partial | Yes | Yes | Yes | No |
| Extractable definition block (40-80 words) | Yes | Yes | Partial | Yes | Yes |
| Numbered step list | No | Yes | Partial | No | No |
| Named research citations | Partial | No | Yes (Vygotsky) | Yes | Yes |
| Sentence starters / prompts | No | Yes (minimal) | No | No | Partial |
| Timing guidance | No | No | No | No | No |
| Differentiation section | No | No | No | Yes | No |
| Digital classroom adaptation | No | No | No | No | No |
| Schema / structured data | Basic | Basic | None | Basic | Basic |
| Author credential display | Yes | Yes | No | Yes | No |
| **EAR coverage score** | **2/12** | **4/12** | **3/12** | **3/12** | **2/12** |

> **Key insight for brief:** No cited source scores above 4/12 on the EAR rubric. The citation field is fragmented — AI engines are stitching answers from multiple sources because no single page covers the terrain. Wayground's path to citation is building the first comprehensive resource that scores 10+/12.

### Gaps & Opportunities

**What's missing from current AI answers:**
- Specific timing guidance (how many minutes optimal for turn-and-talk vs. think-pair-share vs. full discussion) — absent across all top sources
- Copy-paste sentence starters organized by subject area and grade band — only Cult of Pedagogy offers any (2-3 examples)
- Explicit adaptation protocol for shy/introverted students beyond "choose partners carefully"
- ELL-specific scaffold with L1 → L2 progression guidance
- IEP/504 accommodation examples for inclusive classroom implementation
- Digital and hybrid classroom implementation — no source in the competitive set addresses this
- Research citations with quantitative effect size data (Vygotsky cited conceptually everywhere, no empirical numbers)
- Common implementation mistakes with specific corrective moves — absent across all sources
- Grade-band differentiation (K-2 vs. 3-5 vs. 6-8 vs. 9-12) — sources default to elementary

**What Wayground can uniquely provide:**
- The only resource covering timing + prompts + ELL adaptations + digital implementation + IEP accommodations in one place
- Wayground Team Mode and Live Q&A as a digital analog to turn-and-talk — genuine product connection, not forced
- "We tested with X teachers" authority framing if UXR data or teacher community feedback is available
- Teacher community quotes with real educator attribution — trust signal no competitor can replicate
- Ready-to-use Wayground activity links as an immediate "try it now" CTA

**Source domains AI trusts but WG is absent from:**
- Edutopia — highest leverage; backlink or cited contribution would create a trust bridge
- Colorín Colorado — niche but strong ELL citation lane; worth monitoring and potentially reaching out
- TeachThought — open to external references; A2-identified link-earning opportunity
- Reading Rockets — literacy angle; lower priority but worth framing article to include literacy use cases

---

## EAR Attribute List
> Sub-questions a comprehensive answer must cover

| # | Attribute / Sub-question | Must-cover? | Covered by competitors? | B1 Priority |
|---|--------------------------|-------------|------------------------|-------------|
| 1 | What is turn and talk? (40-60 word extractable definition) | Yes | Yes — vague or buried in listicles | Lead the article; rewrite for AI extraction |
| 2 | How does it differ from think-pair-share (and cold calling)? | Yes | Partial — ThoughtCo touches it loosely | Own with 3-column comparison table |
| 3 | Step-by-step implementation (numbered, teacher moves) | Yes | Cult of Pedagogy covers reasonably | Match depth + add timing column |
| 4 | When in a lesson is it most effective? (warm-up / mid / exit) | Yes | Partial — most sources don't specify | Decision framing table or visual |
| 5 | How long should a turn-and-talk last? (specific timing guidance) | Yes | No — absent across all sources | First-mover advantage; own this |
| 6 | Sentence starters and discussion prompts (copy-paste ready) | Yes | Partial — CoP offers 2-3 only | 12-15 categorized by subject/grade |
| 7 | Adaptations for ELLs (scaffolded L1 → L2 support) | Yes | Partial — Colorín Colorado narrowly | Full ELL protocol section |
| 8 | Adaptations for shy/introverted students + IEP/504 | Yes | Partial — Understood.org loosely | Practical UDL-aligned adaptations |
| 9 | Digital and hybrid classroom implementation | Yes | No — strong gap, zero coverage | Digital section; anchor to WG Team Mode |
| 10 | Research backing with effect direction (not just Vygotsky name-drop) | Nice-to-have | Partial — conceptual only | 2-3 sourced citations; Michaels/O'Connor/Resnick or Webb |
| 11 | Common mistakes and corrective moves | Nice-to-have | No — consistent gap | Mistake → fix pairs; high shareability |
| 12 | Grade-band differentiation (K-2 / 3-5 / 6-8 / 9-12) | Nice-to-have | No — elementary default across all | Quick band-specific tips table |

---

## Competitor Content Analysis

### Top Cited Sources

| Source | URL | Structure | Strengths | Weaknesses |
|--------|-----|-----------|-----------|------------|
| Edutopia | edutopia.org/article/discussion-strategies-classroom | Long-form listicle; turn-and-talk is 1 of 12 strategies (~180 words total) | Domain authority ~75+, AI default trust anchor for K-12 pedagogy | Turn-and-talk is buried; no steps, timing, adaptations, or digital angle |
| Cult of Pedagogy | cultofpedagogy.com/speaking-listening-technique | Single-strategy guide: intro → rationale → steps → variations (~1,600 words) | Best structure in the set; numbered steps; warm practitioner voice; widely backlinked | No research citations; no timing; no ELL/IEP adaptations; no digital section |
| TeachThought | teachthought.com/pedagogy/turn-and-talk | Conceptual overview + rationale + brief how-to (~1,000 words) | References Vygotsky/ZPD; question-phrased headings; pedagogical credibility | Abstract; no sentence starters; no timing; no adaptations; thin practical content |
| Understood.org | understood.org | UDL strategy collection; turn-and-talk framed through learning differences lens (~700 words) | Non-profit .org authority; UDL/IEP angle; NCLD affiliation | Not a comprehensive guide; misses typical implementation; no digital angle |
| Reading Rockets | readingrockets.org | Literacy strategy database entry; very short and clean (~400 words) | NICHD-funded; .org TLD; high AI extractability for literacy queries | Literacy-only lens; not applicable to math/science/social studies; no digital angle |
| Colorín Colorado | colorincolorado.org | ELL strategy resource; bilingual education focus | ELL authority; bilingual framing; cited by AI for ELL-specific variants | Very narrow lane; not a comprehensive turn-and-talk resource |

---

## Internal Assets
- **Existing WG pages on this topic:** None confirmed — no `/learn/engagement/turn-and-talk` page exists; net-new opportunity
- **Related ADPs/resources:** Wayground Team Mode (digital analog to partner work), Live Q&A activity type (structured discussion transition), collaborative quiz activities — verify current product catalog for linkable resources
- **Related /learn/ hub pages:** `/learn/engagement/` hub (verify if live); `/learn/strategies/collaborative-learning`; `/learn/strategies/think-pair-share` (if exists, link bidirectionally)
- **Enhance existing vs. create new:** **Create new** — no existing WG asset to enhance; clear competitive gap to close

---

## AEO Opportunity Score Calculation

```
AI Volume:          6 / 10
  (Moderate — steady teacher/pedagogy AI query demand; 
   not a breakout term but consistent in classroom strategy clusters)

× Intent Relevance:  8 / 10
  (Strong — how-to intent maps cleanly to WG's educator 
   audience and /learn/ content model)

× Brand Fit:         9 / 10
  (Excellent — WG Team Mode is a direct digital instantiation 
   of the strategy; product connection is genuine, not forced)

= Score: 432 / 1000

Citation Gap Bonus (qualitative):
  No single competitor scores above 4/12 on the EAR rubric.
  First-mover to full coverage upgrades citation capture 
  probability from "possible" to "likely."

Adjusted Priority: P2
  → Elevate to P1 if teacher testimonials or UXR data available.
```

---

## B1 Intent Summary

| Field | Value |
|-------|-------|
| Primary intent | **How-to** |
| Secondary intent | Informational |
| Mixed-intent handling | Definition block required upfront; FAQ section required at close |
| Comparison sub-element | Yes — triggers required comparison table format |
| Depth level | **Comprehensive (2,500–4,000 words)** |
| Required format elements | 9 required + 3 nice-to-have (see table above) |
| Confidence score | **High** |
| Escalate for human review | No — intent is unambiguous; depth call is supported by 12-attribute EAR list |
| Downstream note for B2 | Topic decomposition should map each of the 9 required format elements to a named section; sentence starters section should be given its own H2 (high link-earning and AI extraction value) |
| Downstream note for B3 | Brief format must include: numbered steps template, comparison table slot, sentence starters table, digital implementation section, FAQ block — all required elements must appear in the brief scaffold |

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
