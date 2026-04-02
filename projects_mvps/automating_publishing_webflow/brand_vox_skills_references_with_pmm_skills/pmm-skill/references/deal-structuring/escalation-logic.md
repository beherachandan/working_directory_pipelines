# Deal Structuring: Escalation Logic & Manager Justification Framework
# Source: Amber (Enablement) + AY26-27 Pricing Protocols — March 2026
# ⚠️ CONFIDENTIAL — Internal Use Only
#
# Purpose: Help AEs know when they can close on their own vs. when to build a
# case for manager approval on creative deal structures.

## Decision Framework Overview

```
Standard Stack (AE owns)          Escalation Zone (manager case)         Hard Stop
─────────────────────────────    ──────────────────────────────────    ──────────────
Volume discount (automatic)       >5% sales discretionary               Below $3.00/student
Bundle (10% or 15%)               Competitive price-match               Below $1,850/school
Duration (5% 2yr / 10% 3yr)      Phased expansion commitments          Free/zero-cost deals
Sales discretionary (≤5%)         Multi-funding timing structures       Matching free competitors
Research partner (5%)             4+ year term commitments
                                  Strategic/lighthouse accounts
```

---

## TIER 1: Standard Stack — AE Closes Without Escalation

These are all within the AE's authority. Apply in order:

### Step 1: Volume Discount (automatic)
Look up the student count tier:
| Students | Core WG | CA | Library |
|----------|---------|-----|---------|
| 1–2,499 | $9.95 | $3.00 | $1.00 |
| 2,500–4,999 | $8.96 | $2.70 | $0.90 |
| 5,000–9,999 | $8.06 | $2.43 | $0.81 |
| 10,000–19,999 | $7.25 | $2.19 | $0.73 |
| 20,000–39,999 | $6.53 | $1.97 | $0.66 |
| 40,000–99,999 | $5.88 | $1.77 | $0.59 |
| 100,000+ | $5.29 | $1.59 | $0.53 |

### Step 2: Bundle Discount
- WG + CA → 10% off combined per-student price
- WG + CA + 1 subject library (All-In) → 15% off combined price
- Additional libraries beyond the first added at volume-discounted rate

### Step 3: Duration Discount (after volume)
- 1 year → 0%
- 2 years → 5%
- 3 years → 10%

### Step 4: Additional Discounts
- Sales discretionary → up to 5% (no approval needed)
- Research partner (data exchange) → 5% (district agrees to share anonymized data)

### Step 5: Constraint Check
- Is the final per-student price ≥ $3.00? → If no, STOP. Cannot go lower.
- Is a single-school deal ≥ $1,850 and ≤ $9,999? → If outside range, adjust.

**If the standard stack gets the deal done → close it. No escalation needed.**

---

## TIER 2: Escalation Signals — "Build the Case for Your Manager"

When standard stack isn't enough, Artie should flag the deal for creative structuring AND generate the justification. Here are the trigger conditions:

### Signal 1: Budget Gap After Max Standard Stack
**Trigger:** Standard stack puts you at $X/student but the prospect needs $Y, and the gap exceeds 5% sales discretionary.
**What Artie does:**
- Calculate exact gap ($X − $Y) and the additional discount % needed
- Check: is $Y still above $3.00 floor? If yes → escalation is possible. If no → hard stop.
- Generate justification with total contract value and strategic rationale
**Manager question:** "Can I get an additional X% beyond my discretionary to close a $[TCV] deal?"

### Signal 2: Competitive Displacement
**Trigger:** Prospect has an existing contract with a named competitor, and standard pricing doesn't beat or match it.
**What Artie does:**
- Reference competitive pricing ranges:
  - IXL: ~$5–8/student (practice-focused, math-heavy)
  - Nearpod: ~$3.50–7.50/student (lesson delivery)
  - i-Ready: ~$5–10/student (diagnostic + adaptive)
  - Amplify: ~$8–15/student (full curriculum)
  - Kahoot/Gimkit/Blooket: Free teacher tier (NOT comparable — reposit on value, don't price-match free)
- Calculate what price point displaces the competitor
- Frame the total displaced contract value ("winning this displaces $X of competitor revenue")
- Build the consolidation case: "We replace N tools with one platform"
**Manager question:** "Can I match/beat [competitor] at $X/student to displace a $[competitor contract value] deal?"

### Signal 3: Strategic / Lighthouse Account
**Trigger:** District meets one or more strategic criteria:
- Top 50 district in state by enrollment
- 50+ teachers already on free tier (strong PQA signal)
- Named district in a target market or vertical
- Potential reference account or case study candidate
- Board priorities explicitly align with Wayground value props
**What Artie does:**
- Pull account data: enrollment, active teachers, games played, organic growth trend
- Pull board meeting context (from account_feature_store) showing strategic alignment
- Calculate "reference value" — what this account's name is worth in adjacent sales
- Model pipeline impact: "This district connects to X neighboring districts in the same ESC/region"
**Manager question:** "Can I go deeper on a strategic account that will unlock $[pipeline value] in adjacent deals?"

### Signal 4: Extended Term (4+ Years)
**Trigger:** Prospect is willing to commit beyond the standard 3-year max, but the standard duration discount only goes to 10%.
**What Artie does:**
- Model the total contract value at 4 or 5 years
- Calculate the implied annual discount needed to close
- Show the guaranteed revenue: "4 years at $X = $[TCV] locked in vs. annual renewal risk"
**Manager question:** "Can I offer 12-15% duration discount for a 4-5 year commitment worth $[TCV]?"

### Signal 5: Phased Expansion Commitment
**Trigger:** District wants to start with a subset of schools now and expand later, but wants the full-district volume pricing from Day 1.
**What Artie does:**
- Model two scenarios:
  - (A) Price Year 1 schools at their actual student count tier (higher per-student)
  - (B) Price Year 1 at the full-district tier (lower per-student, contingent on expansion)
- Calculate the discount gap between A and B
- Build expansion commitment terms: "Year 1: 5 schools at district rate. If not expanded to 20 schools by Year 2, pricing reverts to school tier."
**Manager question:** "Can I price Phase 1 at district volume, contingent on Phase 2 expansion commitment?"

### Signal 6: Multi-Source Funding Timing Mismatch
**Trigger:** District has budget from multiple sources but they hit at different times (e.g., Title I available now, general fund available in Q3, bond money available in January).
**What Artie does:**
- Map the funding sources and their availability windows
- Propose creative contract structures:
  - Deferred start for portion of the deal
  - Phased billing aligned to funding availability
  - Pilot now ($950) → full purchase when funding releases
- Calculate the cash flow timeline vs. the contract start date
**Manager question:** "Can we structure billing to align with the district's funding release schedule?"

### Signal 7: Consortium / Multi-District Deal
**Trigger:** Multiple districts want to purchase together (through a co-op, ESC, or consortium) for additional volume leverage.
**What Artie does:**
- Aggregate total students across all participating districts
- Look up the combined volume tier (likely higher = deeper discount)
- Model the per-district savings vs. individual purchasing
- Flag: consortium deals may need VP-level approval depending on total value
**Manager question:** "Can I extend consortium volume pricing to X districts purchasing through [co-op name]?"

---

## TIER 3: Hard Stops — Do Not Escalate, Redirect Instead

These are non-negotiable. Do not bring them to your manager — redirect the conversation.

### Hard Stop 1: Below $3.00/Student Floor
- **Rule:** $3.00 is the absolute minimum. No exceptions, no escalation path.
- **Redirect:** "If we're below floor, the conversation needs to shift. What else can we add to the deal to make the per-student economics work? More schools? Longer term? Additional products?"
- **Alternative:** Can we reduce scope (fewer students/schools) to stay above floor?

### Hard Stop 2: Below $1,850 School Minimum
- **Rule:** Single-school deals cannot go below $1,850.
- **Redirect:** "For smaller schools, we can explore a 6-week pilot ($950, credited back) as an entry point, or look at whether there's a district-level deal that includes this school."

### Hard Stop 3: Free or Zero-Cost Deals
- **Rule:** Wayground has a free tier for that. Paid products have a cost.
- **Redirect:** "Teachers can use Core Wayground free forever — 20 resources, all basic features. The paid tier unlocks [specific features they need]. Which features are driving this conversation?"

### Hard Stop 4: Matching Free Competitor Pricing
- **Rule:** We don't compete on price with free tools (Kahoot free, Gimkit free, Blooket free).
- **Redirect:** Reposition on value: "Those tools solve engagement. We solve engagement + assessment + accommodations + admin reporting + standards alignment. You're comparing a flashlight to a lighthouse."

---

## Manager Justification Template

When Artie recommends escalation, generate this case:

```
DEAL ESCALATION REQUEST
═══════════════════════════════════════════════════════

Account:          [District Name]
Students:         [count]
AE:               [name]
Current Stage:    [pipeline stage]

PRODUCT MIX
───────────────────────────────────────────────────────
Core Wayground:   [yes/no]
Common Assessment:[yes/no]
Subject Libraries:[list]
PD Services:      [list + prices]

STANDARD STACK PRICING
───────────────────────────────────────────────────────
Volume tier:      [tier] → $[X]/student
Bundle:           [type] → $[X]/student
Duration:         [years] → $[X]/student
Discretionary:    [%] → $[X]/student
Research partner: [yes/no] → $[X]/student
─────────────────────────
Standard price:   $[X]/student
Annual value:     $[X]
Total contract:   $[X] over [Y] years

PROSPECT'S TARGET
───────────────────────────────────────────────────────
Target price:     $[Y]/student
Budget source:    [funding sources]
Budget constraint:[explanation]

THE GAP
───────────────────────────────────────────────────────
Gap:              $[X-Y]/student ([Z]% additional discount needed)
Above floor?      ✅ $[Y] > $3.00  [or ❌ HARD STOP]

ESCALATION REASON
───────────────────────────────────────────────────────
[Signal type from Tier 2]
[1-2 sentence summary]

STRATEGIC JUSTIFICATION
───────────────────────────────────────────────────────
• [Data point 1 — e.g., organic adoption: 85 teachers on free]
• [Data point 2 — e.g., competitive displacement: $180K IXL contract]
• [Data point 3 — e.g., board priority: "tool consolidation" in Q1 minutes]
• [Data point 4 — e.g., reference value: top 10 district in state]
• [Data point 5 — e.g., expansion: 45 schools, only piloting with 5]

PIPELINE IMPACT
───────────────────────────────────────────────────────
This deal at target price:     $[TCV]
Adjacent pipeline potential:   $[estimate] (neighboring districts, ESC region)
Competitor displaced:          [name], $[contract value]

RECOMMENDATION
───────────────────────────────────────────────────────
Approve additional [X]% beyond discretionary
Final price: $[Y]/student
Total contract: $[TCV]

This represents [X]% off list price, [Y]% above floor,
with $[TCV] guaranteed over [Z] years.
```

---

## Artie's Deal Structuring Workflow

When an AE asks for deal structuring help:

1. **Gather inputs:** Student count, product mix, contract term, budget constraints, competitive context, funding sources
2. **Run standard stack:** Calculate the best price within AE authority
3. **Check:** Does standard stack close the gap?
   - **Yes** → Present the deal structure with funding source recommendations. Done.
   - **No** → Continue to step 4.
4. **Check floor:** Is the prospect's target above $3.00/student?
   - **No** → Hard stop. Redirect the conversation (scope, term, products).
   - **Yes** → Continue to step 5.
5. **Identify escalation signal(s):** Which Tier 2 trigger applies?
6. **Pull supporting data:** Account_feature_store, BigQuery usage data, competitive context, board meetings
7. **Generate justification:** Fill out the Manager Justification Template
8. **Present to AE:** "Here's your standard stack price. Here's the gap. Here's the case to bring to your manager, with the data to back it up."

---

## Key Principles

1. **AEs should exhaust standard levers first** — don't escalate prematurely
2. **Every escalation needs a business case** — not "they want it cheaper" but "here's why it's worth it"
3. **The floor is the floor** — $3.00 is non-negotiable
4. **Data wins** — usage metrics, competitive displacement value, and pipeline impact are what managers need
5. **Time kills deals** — Artie should help AEs prepare the escalation case FAST so the manager conversation happens same-day
6. **Creative ≠ cheaper** — sometimes creativity means restructuring (phased, multi-source, expansion commitment) rather than just deeper discounts
