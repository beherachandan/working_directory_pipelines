---
name: pmm
description: Product Marketing skill for GTM teams. Provides personas, value propositions, talk tracks, objection handling, and board meeting keyword mappings for Wayground's educational technology platform. Use when generating account briefs, discovery prep, call scorecards, competitive positioning, or any sales/CS output that needs GTM messaging combined with product data. Works in tandem with the BigQuery skill.
---

# PMM (Product Marketing) Skill

Generates sales-ready GTM output by combining product data (via BigQuery skill) with positioning, personas, and messaging frameworks.

## How This Skill Works

PMM works **in tandem** with BigQuery and Google Drive:
- **BigQuery skill** = what the data shows (product usage, games, teachers, pipeline)
- **Google Drive (gog skill)** = living knowledge base (messaging docs, battle cards, rubrics from EPMM team)
- **PMM skill** = what to say (positioning, personas, talk tracks, objection handling)
- **Together** = sales-ready output (discovery prep briefs, call scorecards, competitive battle cards)

## Product Feature Reference

**ALWAYS consult `references/product-features.md` before writing any external-facing content.**

This is the authoritative product reference (from Carrie, brand owner). It contains:
- Correct feature names (Wayground AI Create/Enhance/Analyze, not generic "AI engine")
- All 20+ question types with auto-grading status
- Session/assignment modes (Teacher-Led, Student-Paced, Test Mode, Paper Mode, Mastery Mode, Mastery Peak, Focus Mode)
- 25+ accommodations (permanently free for US educators)
- Content formats (Assessment, Lesson, Interactive Video, Passage, Flashcard)
- Terminology reference (what to say vs what to avoid)
- Plans & pricing tiers
- Common Assessments details
- Integration capabilities

**Source Google Doc:** `https://docs.google.com/document/d/1it360Gj9rmjcAJ-z8JdcuCRyMbOw2F1f`

## Google Drive Integration

The PMM skill uses a shared Google Drive folder as a living knowledge base. The EPMM team adds/updates docs there, and this skill reads them automatically — no code changes needed.

### Setup
- **Service account:** `waygent-openclaw@quizizz-org.iam.gserviceaccount.com`
- **Shared folder:** `Waygent` (ID: `1QFxefyRAaS3mW7FXWRzHvEy3OdGhQNf2`)
- **CLI:** `gog` (Google Workspace CLI via gog skill)

### Drive Commands
```bash
# List all files in the Waygent folder
gog drive list 1QFxefyRAaS3mW7FXWRzHvEy3OdGhQNf2 --json

# Search for specific content
gog drive search "name contains 'battle card'" --max 10

# Read a Google Doc
gog docs cat <docId>

# Export a doc to text
gog docs export <docId> --format txt --out /tmp/doc.txt

# Download a file
gog drive download <fileId> --out /tmp/file.pdf
```

### When to Check Drive
- **Before generating any brief or talk track** — check for updated messaging docs
- **When competitive positioning is needed** — look for latest battle cards
- **When user mentions a doc they uploaded** — search the Waygent folder
- **Periodically** — the folder is the team's way to feed new knowledge without intervention

### Folder Structure (expected)
The EPMM team will organize content in subfolders. Check what's available:
```bash
gog drive list 1QFxefyRAaS3mW7FXWRzHvEy3OdGhQNf2 --json
```
Content types to expect: messaging docs (PDF/Docs), battle cards, enablement rubrics, talk track refinements, competitive intel updates.

## Workflow (MANDATORY)

### Step 1: Acknowledge
- React with 👀 emoji to show you're processing the request

### Step 1b: Competitor & Policy Intel Pre-Flight (Mandatory — Added 2026-03-23)
> Run this BEFORE Step 2. Takes 2 minutes. Prevents stale positioning and missed deal signals.

**Before generating any GTM output** (talk tracks, battlecards, discovery briefs, positioning, objection handling), check:

#### Competitor Intel
1. Read `references/competitor-intel-weekly.md` (workspace: `/home/ec2-user/.openclaw/workspace/references/competitor-intel-weekly.md`)
2. Note the **THIS WEEK** section — identify any 🔴 HIGH threat moves relevant to this output
3. For each competitor in the request (or in the deal context), pull:
   - Latest move (date + what happened)
   - Verbatim talk track from the weekly file
   - Full battlecard if needed: `references/battlecards/<competitor>.md` (IXL, Mastery Connect, Kahoot seeded)
4. **If generating a competitive battlecard:** The battlecard files in `references/battlecards/` are the primary source — they are pre-built with strengths, weaknesses, talk tracks, and objection handling. Read the relevant one before generating output.

#### Policy & Funding Context
1. Read `references/federal-state-policy.md` (workspace: `/home/ec2-user/.openclaw/workspace/references/federal-state-policy.md`) — check Section 9 (Sales Playbook) for this week's active talk tracks
2. Apply context to GTM output:
   - **CA districts:** $22B funding (record per-student funding, budget season NOW) + labor dispute context
   - **ESSER timing:** March 30 cliff — consolidation pitch is live conversation
   - **Evidence-based mandates (16 states):** Formative assessment angle is legislatively backed
   - **Phone-ban states:** Engagement tools on managed devices angle
3. Cite policy context with date and source when including in talk tracks (don't present stale info as current)

#### Rule
Every PMM output that involves competitive positioning, talk tracks, or account briefs must include:
- Intel freshness date (from `competitor-intel-weekly.md` "Last updated" field)
- At least one relevant policy/funding signal if state-specific context is known
- A note if intel is >2 weeks old ("⚠️ Intel may be stale — check for updated Rue brief")

---

### Step 2: Run Pre-Flight Checklist (MANDATORY — NO SHORTCUTS)
- Identify the output type from the request (see checklists below)
- Read EVERY file in that checklist BEFORE generating any output
- If a file isn't available, say so explicitly — do NOT fill in with plausible-sounding content
- **"I don't know" is always better than a hallucinated answer**

### Step 3: Pull Account Data (when account-specific)
- Use BigQuery to query product usage (active teachers, games, feature adoption)
- Query `wayagent_GTM.account_feature_store` for board meetings, BANT scores, contacts
- Query `clean.salesforce_*` for pipeline and deal history
- Use `UNNEST(board_meetings)` to access meeting data

### Step 4: Check Google Drive for Latest Content
- List the Waygent folder: `gog drive list 1QFxefyRAaS3mW7FXWRzHvEy3OdGhQNf2 --json`
- Look for recently updated docs relevant to the request
- Drive content takes precedence over static references when newer/more specific

### Step 5: Generate Output with Source Citations
- Every factual claim MUST cite its source file (e.g., "Lockdown browser is CA-only — source: pricing-packaging-privileges.md")
- Every data point must come from BigQuery (no unsupported assertions)
- Discovery questions should reference specific data points the rep can cite
- If information is not in any file, state: "I don't have this in my reference files — verify with [suggested person/source]"

---

## Pre-Flight Checklists by Output Type

### 📋 Discovery Prep Brief
```
MANDATORY READS (do ALL before generating):
☐ references/jargons/info.md — terminology
☐ references/personas/[target persona].md — buyer profile, objections, win triggers
☐ references/signal-to-pillar-decision-tree.md — route signals → pillar
☐ references/product-features.md — correct feature names, capabilities
☐ references/pricing/rate-card.md — pricing tiers, bundles, constraints
☐ references/funding/sources.md — funding pathways for deal sizing
☐ references/competitive/[relevant competitor].md — if competitor in play
☐ references/board-keywords/info.md — map board priorities → value props
☐ workspace references/k12-marketing-calendar.md — current month's persona mindset, product value, channels

CONDITIONAL READS (if applicable):
☐ references/enablement/ca-discovery-questions.md — if CA opportunity
☐ references/deal-structuring/escalation-logic.md — if pricing discussion expected
☐ workspace references/ca-product-knowledge.md — if CA positioning needed
```

### 📋 Talk Track / Objection Response
```
MANDATORY READS:
☐ references/jargons/info.md — terminology
☐ references/personas/[target persona].md — language, objections, win triggers
☐ references/objections/info.md — standard objection responses
☐ references/product-features.md — correct feature names
☐ references/sales-agent-reference-guide.md — talk track frameworks, proof points
☐ workspace references/k12-marketing-calendar.md — seasonal context for time-relevant talk tracks

CONDITIONAL READS:
☐ references/competitive/[competitor].md — if competitive objection
☐ references/pricing/rate-card.md — if pricing objection
☐ references/enablement/sko-objection-roundrobin.md — if common objection pattern
```

### 📋 Competitive Battlecard / Positioning
```
MANDATORY READS:
☐ references/jargons/info.md — terminology
☐ references/best-in-class-frameworks.md — Klue/Gong/Lavender methodology synthesis (empathy checks, stage checks, quality bar)
☐ references/competitive/deal-first-playbook.md — DEAL-FIRST competitive playbook (Klue framework, transcript-grounded, stage-aware)
☐ references/competitive/[target competitor].md — existing battlecard (detailed features)
☐ references/competitive/info.md — master competitive overview
☐ references/product-features.md — our capabilities for comparison
☐ references/pricing/rate-card.md — our pricing for TCO comparison

CONDITIONAL READS:
☐ references/personas/[relevant persona].md — persona-specific positioning
☐ references/signal-to-pillar-decision-tree.md — competitor mention response guide (Section 3)
☐ workspace references/ca-competitive-landscape.md — if CA category competitor
☐ workspace/pmm/deal-journey-notes.md — 22 deal journeys with patterns and lessons
```

### 📋 Deal Structuring / Pricing
```
MANDATORY READS:
☐ references/pricing/rate-card.md — volume tiers, bundles, duration, constraints
☐ references/deal-structuring/escalation-logic.md — AE authority vs. escalation
☐ references/funding/sources.md — funding pathways, creative patterns
☐ references/jargons/info.md — deal terminology

CONDITIONAL READS:
☐ references/enablement/sko-2026-messaging-pricing.md — packaging context
☐ references/competitive/[competitor].md — if competitive displacement pricing
☐ workspace references/pricing-packaging-privileges.md — plan tiers, feature gating, paywalling
```

### 📋 Call Scorecard / Discovery Evaluation
```
MANDATORY READS:
☐ references/enablement/ae-bdr-discovery-rubrics.md — scoring frameworks
☐ references/personas/[target persona].md — expected discovery depth
☐ references/signal-to-pillar-decision-tree.md — signal validation
☐ references/enablement/customer-journey-bts-2026.md — stage context

CONDITIONAL READS:
☐ references/jargons/info.md — verify terminology usage
☐ references/product-features.md — verify feature claims made on call
```

### 📋 Expansion / Renewal Brief
```
MANDATORY READS:
☐ references/jargons/info.md — terminology
☐ references/personas/[relevant persona].md — renewal buyer profile
☐ references/pricing/rate-card.md — upsell pricing, bundle opportunities
☐ references/product-features.md — features for upsell pitch

CONDITIONAL READS:
☐ references/enablement/customer-journey-bts-2026.md — expansion stage
☐ references/competitive/[competitor].md — if competitive pressure
☐ references/funding/sources.md — funding for expanded scope
```

### 📋 Brand-Polished External Content (Vox handoff)
```
MANDATORY READS:
☐ references/product-features.md — correct feature names, terminology
☐ references/jargons/info.md — terminology
☐ references/personas/[target audience].md — audience-appropriate language

NOTE: After generating, hand off to Vox for brand voice polish.
Vox has its own checklist (see Vox SKILL.md).
```

---

## HQIM Positioning Rule (NON-NEGOTIABLE — Amber, Mar 10 2026)

**Wayground is NOT HQIM. We SUPPORT the implementation of HQIM.**
- Never position Wayground as a core curriculum or as HQIM itself
- We are the supplemental layer that makes HQIM implementation work: engagement, practice, formative assessment, differentiation, progress monitoring
- When districts adopt Eureka, Bridges, IM, CKLA, Amplify, etc. — we help teachers implement it effectively
- Reps must have strong mastery of this pedagogical distinction

---

## Terminology Matching Rules (NON-NEGOTIABLE — Amber, Mar 9 2026)

When preparing briefs, discovery prep, talk tracks, or any account-specific output, **match the district's own terminology**. Do not default to Wayground's preferred terms.

### EL/ELL/MLL
Districts vary. Some say "English Learners," some say "English Language Learners," some say "Multilingual Learners." Match what THEY use.
- **How to determine:** Check Salesforce notes, board meeting minutes (AFS), district website language, state terminology (e.g., California uses "English Learner," New York uses "Multilingual Learner")
- **If unknown:** Use the state's official term. WIDA states tend toward "EL." New York, California, and equity-forward districts increasingly use "MLL."
- **In our own marketing/brand copy:** Always "multilingual" (Carrie's brand rule). But in account-specific prep for a rep? Mirror the district.

### Intervention Protocols
Districts may call their framework "RTI," "MTSS," "MTSS-B" (behavioral), "MTSS-R" (reading), "tiered supports," "intervention framework," or something district-specific.
- **How to determine:** Check board meeting notes, strategic plan references in AFS, Starbridge research, district website
- **If unknown:** Use "tiered supports" as the generic safe term, then ask the rep what the district calls it

### General Rule
**Sound like someone who's done their homework on THIS district, not someone reading from a playbook.** If Houston ISD says "Multilingual" and Dallas ISD says "EL," two briefs for those districts should use different terminology even though they're 4 hours apart.

---

## Anti-Hallucination Rules (NON-NEGOTIABLE)

1. **Every claim needs a source.** If you can't point to a file, a BigQuery result, or a board meeting note, don't say it.
2. **"I don't have this" > making it up.** Say: _"This isn't in my reference files. Check with [Cody/Carrie/Amber/Starbridge] for current intel."_
3. **Pricing is sacred.** Never improvise pricing numbers. Always read rate-card.md. If a scenario isn't covered, flag it for escalation.
4. **Feature claims must match product-features.md.** If a feature isn't listed there, don't claim we have it. Flag it as "verify with product team."
5. **Competitor claims must come from battlecards.** Don't invent competitor weaknesses or pricing. If the battlecard doesn't cover it, say so.
6. **Released vs. WIP (BTS 2026).** ALWAYS distinguish what's live today vs. what's coming. Never present roadmap as current capability. Check workspace references/bts-2026-product-commitments.md if unsure.
7. **Board meeting data has a cutoff.** AFS board meeting data stops at Jan 29 2026. If referencing board context, note the data freshness.

## Key Rules

1. **ALWAYS** read jargons before generating any GTM output
2. **ALWAYS** identify the target persona before selecting messaging
3. **ALWAYS** incorporate board meeting data when it exists for a district
4. **ALWAYS** back claims with BigQuery data — never assert without evidence
5. Map board priorities → Wayground value props using board-keywords reference
6. Discovery questions must reference specific data points the rep can cite
7. Talk tracks must be persona-appropriate (superintendent ≠ teacher champion)
8. When generating briefs, use `scripts/generate-brief.sh` as the template structure

## Pre-Flight Checklist: Academic / Thought Partner Question
```
MANDATORY READS (do ALL before generating):
☐ references/academic/info.md — index and thought-partner mode guidelines
☐ references/academic/[relevant domain].md — the specific academic domain being asked about
☐ references/product-features.md — for natural product connections (NOT forced)

CONDITIONAL READS:
☐ references/personas/[relevant persona].md — if question is in context of a specific buyer
☐ references/academic/[adjacent domain].md — if question spans multiple domains (e.g., MTSS + assessment)
```

### When to Use Thought Partner Mode
- Rep asks a conceptual/educational question (not "prep me for a call" but "what is MTSS?")
- Rep needs to understand a topic to speak credibly, not pitch it
- Customer asked a question the rep doesn't know how to answer
- Anyone prepping for a conversation with an assessment director, C&I lead, or curriculum specialist

### Thought Partner Output Pattern
1. **Explain the concept** — Like an expert colleague would. Clear, thorough, no jargon without definition.
2. **Connect to our world** — Where Wayground fits naturally. Honest about what we do and don't do.
3. **Arm the rep** — Conversation starters, signals to listen for, how to respond when this topic comes up.
4. **Don't pitch** — If there's no natural product connection, that's fine. Being helpful builds trust.

---

## Output Types

| Output | When to Use | Key Inputs |
|--------|------------|------------|
| Discovery Prep Brief | Before first call with account | Account data + board meetings + persona |
| Talk Track | Preparing for specific conversation | Stage + persona + competitive context |
| Objection Response | Rep hit a blocker | Objection type + persona + account data |
| Battle Card | Competing against specific vendor | Competitor + persona + value props |
| Call Scorecard | Evaluating a completed call | Call notes + persona + stage criteria |
| Expansion Brief | Upsell/renewal opportunity | Usage data + contract info + growth signals |
| Deal Structure | Creative pricing + funding proposal | Student count + district profile + funding sources + product mix |

## Reference Files

All reference materials are indexed in `references/info.md`. Key files:

### Pricing & Deal Structuring (Added Mar 6, 2026)
- `references/pricing/rate-card.md` — **AY26-27 rate card, volume discounts, duration discounts, bundle rules, minimums/maximums, PD pricing, discount stacking rules.** Use for deal sizing, quote building, and creative deal structuring.
- `references/funding/sources.md` — **US K-12 funding sources mapped to Wayground products.** Federal (Title I/II/III/IV, IDEA, Perkins V, CSI/TSI), state (IMTA, assessment funds, CTE matching), and local (general fund, curriculum budget, bonds). Includes 8 creative deal structuring patterns and a deal sizing calculator.

### Core References

#### Personas (9 total - all with value prop mapping, problem statements, pillar routing)
- `references/personas/teacher-champion.md` — **#1 driver of closed deals** (60% of wins). Teachers request paid features. Decision driver: paywall hits, peer adoption, feature need, admin support.
- `references/personas/superintendent.md` — **Financial approver, C-suite.** Cares about: district outcomes, budget stewardship, board presentation, teacher retention. Decision driver: board alignment, peer validation, ROI data.
- `references/personas/curriculum-director.md` — **Academic buyer, owns instructional budget.** Cares about: standards alignment, assessment strategy, instructional quality, PD. Decision driver: curriculum adoption cycle, CA need, PLC culture, teacher feedback.
- `references/personas/principal.md` — **Building-level champion, school improvement driver.** Cares about: teacher adoption, student engagement, proof of impact, ROI. Decision driver: teacher enthusiasm, visible engagement, low implementation friction, peer principal validation.
- `references/personas/instructional-coach.md` — **Critical influencer, tool consolidator.** Cares about: one platform to master, teacher adoption success, measurable impact, PD efficiency. Decision driver: tool fatigue, adoption failure, impact mandate, teacher love.
- `references/personas/assessment-director.md` — **Evidence gatekeeper, CA decision maker.** Cares about: assessment integrity, data accuracy, standards mastery, state test correlation, board reporting. Decision driver: legacy tool pain, CA-like behavior detection, failed CA adoption, data fragmentation.
- `references/personas/it-director.md` — **Risk manager, gatekeeper.** Cares about: tool proliferation, security/compliance, integration, budget waste. Decision driver: consolidation opportunity, security incident, SSO pain, teacher bypass concern.
- `references/personas/chief-academic-officer.md` — **Academic buyer (C-suite), second to superintendent.** Cares about: program fidelity, teacher buy-in, pacing consistency, evidence of learning, board presentations, subgroup progress. Decision driver: accountability pressure, subgroup gaps, post-adoption evaluation, PLC investment.
- `references/personas/*.md` — All personas include: role/title, decision authority, language they use, objection patterns, win triggers, data points that matter, value prop mapping (table format), problem statements, how to engage, and pillar routing (PLAN/TEACH/MEASURE).

#### Competitive (16 battlecards - CA category + engagement consolidation)
**CA-Category Competitors (Tier 1 - Direct):**
- `references/competitive/mastery-connect.md` — Deep standards mastery tracking, Canvas integration, bubble sheet scanning. Weakness: teacher adoption (low), reliability issues post-Instructure acquisition, stagnant product development. Win: teacher daily use, engagement drives completion, reliability, platform consolidation.
- `references/competitive/performance-matters.md` — Comprehensive benchmarking, PowerSchool integration, item bank depth. Weakness: only 16% of teachers create assessments, heavy admin setup, aging UX, clinical interface. Win: teacher authoring, daily classroom presence, student engagement, modern UX.
- `references/competitive/illuminate.md` — Assessment + MTSS/intervention workflows, strong dashboards, ELD tracking. Weakness: technical reliability issues, complex setup, no engagement, post-HMH neglect. Win: teacher daily use, technical reliability, simplicity, engagement = better data.
- `references/competitive/renaissance-dna.md` — Robust item bank, standards alignment, Renaissance suite breadth (Star + AR + DnA + Nearpod). Weakness: separate products ≠ platform, DnA clinical feel, no daily classroom use, expensive. Win: unified platform vs. portfolio, daily engagement, unified data stream.

**Formative Assessment (Tier 2):**
- `references/competitive/formative.md` — Real-time formative assessment, show-your-work (drawing), live student monitoring. Weakness: point solution, no gamification, no CA, no engagement, no lockdown security. Win: full platform vs. point solution, student engagement, CA capability, assessment integrity (lockdown browser).
- `references/competitive/pear-assessment.md` — Free tier, good question types (TEI), Google Classroom integration. Weakness: limited brand recognition, no gamification, assessment-only, small scale. Win: full platform vs. assessment only, engagement, AI creation, accommodations depth, consolidation.

**Regional/Niche (Tier 2):**
- `references/competitive/eduphoria.md` — Texas-dominant, bundles assessment + PD + walkthroughs + appraisals. Weakness: Texas-specific, aging UX, no engagement. Win: national platform vs. regional, daily classroom use, teacher experience.
- `references/competitive/linkit.md` — Northeast regional (NJ/NY), benchmark assessment + predictive analytics for state test scores. Weakness: regional only, no engagement, benchmark-window only. Win: national platform, daily engagement drives scores vs. predicting them.
- `references/competitive/edugence.md` — Smaller assessment + data analytics player. Weakness: limited recognition, basic UX, small team. Win: standard platform value story (everything Edugence does + more).

**Engagement/Lesson Delivery (Consolidation Competitors):**
- `references/competitive/nearpod.md` — **#1 displacement target.** Interactive lessons, VR field trips, Renaissance acquisition. Weakness: product stagnation (3 years, no major features), AI gap, separate from Star assessment data, not a platform. Win: full platform consolidation (Nearpod + Kahoot + Edpuzzle + assessment tool = Wayground), product evolution, unified instruction-to-assessment data, AI leadership.
- `references/competitive/newsela.md` — Leveled reading content platform (170+ articles). Weakness: content library only, no engagement/games, no teacher-created content, no assessment depth. Win: platform vs. library, teacher agency, engagement beyond reading, assessment depth + standards reporting.

**Device Management (Different Category):**
- `references/competitive/goguardian.md` — Device management + classroom monitoring (Beacon, Admin, Teacher, DNS filtering). Acquired Pear Deck, bundled "free." Weakness: different category (device mgmt ≠ instruction), Pear Deck stagnation, no formative assessment/CA/accommodations. Win: don't fight GoGuardian (keep it), show Pear Deck doesn't solve instruction/assessment/engagement problems.

#### Academic Knowledge Base (Added Mar 9, 2026 — Amber)
- `references/academic/info.md` — Index and thought-partner mode guidelines
- `references/academic/assessment-fundamentals.md` — Assessment hierarchy (screener → formative → benchmark → summative), psychometrics (validity, reliability, IRT, CTT), standards alignment, vocabulary reference
- `references/academic/intervention-frameworks.md` — RTI (3 tiers), MTSS (whole-child), PBIS (behavioral), progress monitoring deep dive, conversation starters by signal
- `references/academic/pedagogical-frameworks.md` — UDL, differentiated instruction, standards-based grading, competency-based education, PLCs, backward design (UbD)
- `references/academic/ai-in-education.md` — District AI policies, AI literacy frameworks, responsible AI, AI in assessment, competitor AI positioning
- `references/academic/udl-guidelines.md` — CAST UDL Guidelines 3.0 deep dive, three principles with checkpoints, July 2024 updates (identity, equity, joy/play), Wayground feature mapping
- `references/academic/math-nctm.md` — NCTM Principles & Standards, Principles to Actions (8 Teaching Practices), Catalyzing Change, position statements on assessment/technology/equity, math-specific talking points
- `references/academic/ela-science-of-reading.md` — Science of Reading, 5 Big Ideas of Beginning Reading, structured literacy vs. balanced literacy, Simple View of Reading, 40+ state SoR legislation, MTSS-R, ELA-specific talking points
- `references/academic/urban-districts-cgcs.md` — Council of the Great City Schools (80+ largest urban districts), policy positions, NAEP/TUDA analysis, newcomer/SLIFE guidance, equity frameworks, using CGCS in enterprise sales
- `references/academic/multilingual-learners-el-mll.md` — WIDA framework (6 proficiency levels, ELD standards, Can Do philosophy), EL Success Forum, Title III funding connection, EL/MLL terminology guide, accommodation alignment
- `references/academic/professional-development.md` — Gates Foundation "Teachers Know Best" (2014, BCG), $18B PD market analysis, only 29% teacher satisfaction, PLC/coaching effectiveness gaps, strong collaboration models (7% of schools), PD budget as Wayground funding source, conversation starters by PD signal
- `references/academic/instructional-materials-hqim.md` — Core vs. supplemental positioning, buyer/user/specialist tension reconciliation, RAND 2021 6,000-teacher study on engagement/challenge/usability, EdReports 3-pillar rubric framework, 90% teacher curation rate (NASBE), supplemental platform quality ratings, must-haves vs. delighters, state-specific procurement processes (TX/OH/FL), competitive landscape (BrainPop/Mystery Science/Desmos), grade-level differences in curation

#### Original References
- `references/jargons/info.md` — GTM terminology (read FIRST before ANY external-facing content)
- `references/value-props/*.md` — 5 value props: assessment, engagement, time-savings, differentiation, data-visibility
- `references/talk-tracks/*.md` — Stage-specific conversation frameworks
- `references/objections/info.md` — Top objections with persona-specific responses
- `references/competitive/info.md` — Master competitive overview (legacy, see individual battlecards above)
- `references/board-keywords/info.md` — Board meeting topic → value prop mapping
- `references/product-features.md` — Authoritative product feature reference
- `references/feedback/log.md` — Feedback log for continuous improvement

### K-12 Seasonality & Marketing Calendar (Added Mar 10, 2026 — Carrie)
- `workspace references/k12-marketing-calendar.md` — **Month-by-month K-12 seasonality guide.** Maps every month of the school year across 4 personas (Students, Teachers, Principals, District Admins) with their mindset/needs, marketing channels, product value props, and holidays/events. Use for: seasonal talk track selection, campaign timing, discovery prep (what's top of mind for this persona RIGHT NOW), content calendar planning, and layering temporal context onto any GTM output.
  - Source: https://docs.google.com/spreadsheets/d/17_iFZZF8HmchzrvtXsriYn51wWQOphH4m8jfaNCs2Zo/edit
  - Full path: `/home/ec2-user/.openclaw/workspace/references/k12-marketing-calendar.md`

### Carrie's PMM Resources (Added Mar 6, 2026)
These four docs form the foundation of the prep-to-demo workflow. Three work together: Reference Guide is the foundation, Decision Tree routes the angle, Brief Template activates it per account.

- `references/sales-agent-reference-guide.md` — **THE foundational knowledge base.** Persona profiles, value prop mapping by pillar (PLAN/TEACH/MEASURE), full talk tracks, competitive positioning, objection handling, subject-specific messaging, discovery problem statements, customer proof points. This is the source material everything else pulls from.
  - Source: https://docs.google.com/document/d/1SSM-KbVKKStHjUUmljbz8REU_xcPEvEB/edit

- `references/signal-to-pillar-decision-tree.md` — **The translation layer.** Maps observable district signals (board minutes, CRM history, tech stack, usage data) to which messaging pillar to lead with (PLAN/TEACH/MEASURE), opening message, features to anchor, best demo moment, and objection to prep. Query this in real time during brief generation.
  - Source: https://docs.google.com/document/d/1PddFb-yPck_sl0M99apJDm4_C7-QQdjs/edit

- `references/demo-handoff-brief-template.md` — **Per-account brief template.** Packages discovery findings into structured brief for demo specialists. Sections: account snapshot, lead pillar, discovery signals, ordered demo flow (max 5 features), objection prep (Acknowledge → Reframe → Bridge), proof points, closing script, and feedback loop.
  - Source: https://docs.google.com/document/d/13Cd6Yvu4kyK2PgWUpsS75RSNcXMAcu6z/edit

- `references/us-k12-education-reference.md` — **US Education Reference Guide.** Generic understanding of US K-12 terminology, grade structures, school types, standards/testing, district sizes, data privacy, subject-by-subject messaging, buyer personas, and an educator phrase cheat sheet. Helps reps newer to edtech understand context.
  - Source: https://docs.google.com/document/d/1P5YGAn5N69I0TQfI_OCGgu84eYX5fRSW/edit

## Scripts

- `scripts/generate-brief.sh` — Generate account brief from `wayagent_GTM.account_feature_store`

## Data Foundation (from Win/Loss Analysis)

These patterns inform all messaging in this skill:

### Closed-Won Fingerprint
- **1,030 won deals** analyzed against 3,223 lost deals
- **#1 win reason:** Teacher requests (619 deals) — champions drive purchases
- **Key signals:** High teacher count, organic adoption, paywall hits, active usage

### Loss Patterns
- **#1 loss:** Cold/unresponsive (843 deals) — never engaged
- **#2 loss:** No budget (588 deals) — timing/funding issue
- **Competitor losses:** IXL (math practice positioning), MagicSchool (AI tools)
- **Feature gaps:** Screen blocking, longitudinal student growth tracking, PLC data

### What Winners Look Like
- District has 5+ active teachers already using free version (PQA)
- Teacher champion actively requesting paid features
- Board/admin priorities align with Wayground value props
- Budget cycle timing matches (Q2-Q3 for school year planning)
