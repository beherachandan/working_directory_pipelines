# Talk Track: CTO / CIO / Tech Director Meeting
> Source: Amber request, Mar 10 2026. Engineering-founded positioning.
> Persona: IT / EdTech Director (see `personas/it-director.md`)

## Core Throughline: Engineering-Founded Credibility

Wayground is an **engineering-founded company**. This is the credibility wrapper that makes every claim land differently with technical buyers. Security, AI controls, and integrations weren't bolted on after product-market fit — they were foundational architectural decisions.

**Why this matters for CTOs/CIOs:** They've been burned by vendors where security was an afterthought, where integrations were hacked together, where "AI features" were rushed out without guardrails. An engineering-founded company signals peer credibility — "these people think like I do."

Use "engineering-founded" as a throughline across all three pillars below, not as a standalone talking point.

---

## The Three Pillars (CTO/CIO Meeting)

### Pillar 1: Security & Compliance — "Built Into the Architecture"

**Opening frame:** _"We're an engineering-founded company — security and data architecture weren't bolted on after product-market fit. They were foundational design decisions."_

**Key credentials:**
- ISO 27001:2022 certified (not "working toward" — certified)
- SOC 2 compliant (third-party audited enterprise-grade controls)
- FERPA and COPPA compliant (federal K-12 student data privacy)
- Common Sense Media Privacy approved (independent third-party evaluation)
- Student Data Privacy Consortium member
- ESSA Level 3 evidence

**What to say:**
> "Your nightmare is approving a tool that becomes a data breach headline. We lead with certs because we know that's your first gate — and we pass it before you even have to ask."

**What NOT to say:**
- Don't lead with pedagogy — that's not their lens
- Don't say "we take security seriously" — every vendor says that. Show credentials.

**Proof points:**
- Trusted by 90% of U.S. schools (organic adoption = implicit security vetting by thousands of districts)
- No known data breaches or security incidents

---

### Pillar 2: AI — "Teacher-Controlled, Not Wild"

**Opening frame:** _"Our engineering DNA means we built AI controls into the platform architecture — teacher approval gates, no student data in training pipelines, org-level feature toggles — rather than scrambling to add guardrails after a board complaint."_

**Key capabilities (use correct feature names):**
- **Wayground AI Create** — generates standards-aligned content; teacher reviews, edits, approves every item before students see it
- **Wayground AI Enhance** — differentiated versions (easy/medium/hard), reading level adjustment, translation (18+ languages)
- **Wayground AI Analyze** — insights from student responses for instructional adjustment
- **AI Answer Explanations** — step-by-step feedback on incorrect answers (transforms mistakes into learning moments)

**The three questions every CTO asks (and our answers):**

| Their Question | Our Answer |
|---|---|
| "Is student data used to train AI models?" | No. Student responses and PII are never used for AI model training. |
| "Can we control which AI features are on?" | Yes. AI features are optional — districts can enable/disable at org level. |
| "Does AI output reach students unsupervised?" | No. Teachers review and approve all AI-generated content before it reaches students. |

**What to say:**
> "CTOs are seeing districts ban AI tools outright because they can't control them. We give you the control lever — district-level toggles, teacher approval gates, zero student data in training. Your board gets the guardrails they need; your teachers get the AI tools they want."

**Competitive angle:**
- Most competitors rushed AI features to market without architectural guardrails
- Our engineering-first approach means controls are platform-level, not bolt-on patches

---

### Pillar 3: Integration & Consolidation — "Fewer Tools, Not Another One"

**Opening frame:** _"Because we're engineers first, we built for interoperability from day one — LTI, Clever, ClassLink, Google Classroom aren't afterthought integrations, they're core to the architecture."_

**Key integrations:**
- SSO + automated rostering via Clever and ClassLink (no CSV uploads, no duplicate accounts)
- LMS integration: Canvas (LTI), Google Classroom, Schoology — roster sync + grade passback
- Google/Microsoft SSO for teacher login
- Admin dashboard with district-wide reporting (no IT bottleneck for data requests)

**The consolidation play (this is where deals close):**

| Tool Category | Current Tools (Typical District) | Wayground Replaces |
|---|---|---|
| Formative assessment | Kahoot, Quizlet, Google Forms | ✅ |
| Interactive video | Edpuzzle, Nearpod | ✅ |
| Practice & review | IXL, Quizlet | ✅ |
| Reading comprehension | Newsela (partial) | ✅ |
| Test prep | Various point solutions | ✅ |
| Accommodations | Manual processes, separate tools | ✅ (25+ accommodations, permanently free for US educators) |

**What to say:**
> "Districts average 2,700+ tools per year. Every new tool you approve is a security review, a support ticket, and a vendor contract. Wayground replaces 5-7 single-purpose tools. Your net tool count goes DOWN, not up."

> "90% of US schools already have teachers using Wayground organically. This isn't a rollout — it's a formalization. You're bringing existing usage under IT governance, not deploying something new."

**IT-specific wins:**
- Fewer help desk tickets (one platform vs. 5-7)
- Fewer security reviews and vendor contracts
- Adoption analytics in admin dashboard — IT doesn't become bottleneck
- Teachers already using it = no change management burden

---

## The One-Liner (Meeting Opener or Closer)

_"We're an engineering-founded company — so security, AI controls, and integration aren't afterthoughts, they're architecture. ISO 27001 certified, AI is teacher-controlled with no student data training, and we plug into your existing stack through Clever, ClassLink, and LMS so you're consolidating tools, not adding one."_

---

## Objection Handling (CTO-Specific)

| Objection | Response |
|---|---|
| "We're cutting tools, not adding." | "That's exactly our pitch. We replace 5-7 tools you're already paying for. Net tool count goes down." |
| "What about our SIS/LMS?" | "Clever, ClassLink, Canvas LTI, Google Classroom, Schoology — we integrate with whatever you run. SSO, roster sync, grade passback." |
| "Teachers will just use the free version." | "They already are — 90% of US schools have organic users. A paid plan brings them under your IT umbrella with SSO, admin reporting, and central accommodations management." |
| "Our board hasn't approved AI tools." | "No problem. AI features are org-level toggleable. Turn them off entirely. Teachers still get the full assessment, practice, and instruction platform. Enable AI when your board is ready." |
| "Prove the consolidation." | Pull their specific tool overlap from BigQuery (organic usage data) + show side-by-side replacement matrix. |

---

## Discovery Questions (for the CTO/CIO conversation)

1. "How many edtech tools are currently in your approved stack? How many are actually being used?"
2. "What's your SSO/rostering setup — Clever, ClassLink, or manual?"
3. "Has your board taken a position on AI in instruction yet?"
4. "How are you currently handling assessment tool fragmentation — different tools for formative vs. summative?"
5. "What does your renewal/audit cycle look like for edtech subscriptions?"

---

## Stage-Specific Guidance

| Stage | Focus | Key Move |
|---|---|---|
| BDR Outreach | Consolidation hook + engineering cred | "Engineering-founded, replacing 5-7 tools, ISO certified" |
| Discovery | Three pillars deep dive | Ask discovery Qs, map their pain to our architecture |
| Demo | Show integration + admin dashboard + AI toggles | Live SSO, roster sync, AI on/off, admin reporting |
| Proposal | TCO comparison + security docs | Side-by-side cost, compliance packet, consolidation ROI |
| Close | Risk removal | "Net tool reduction, no rollout burden, security pre-cleared" |
