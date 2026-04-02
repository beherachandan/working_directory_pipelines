# GTM Jargons & Terminology

Read this file BEFORE generating any GTM output. These terms have specific meanings in the Wayground sales context.

## Sales & Revenue Terms

| Term | Definition |
|------|-----------|
| **ACV** | Annual Contract Value — total annual revenue from a single contract |
| **ARR** | Annual Recurring Revenue — total annualized recurring subscription revenue |
| **ASP** | Average Selling Price — mean deal size across closed-won deals |
| **TCV** | Total Contract Value — full value across multi-year deals |
| **NRR** | Net Revenue Retention — revenue retained from existing customers including expansion/contraction |

## Pipeline & Lead Terms

| Term | Definition |
|------|-----------|
| **ICP** | Ideal Customer Profile — characteristics of the best-fit accounts (for Wayground: US K-12 districts with 5+ active teachers) |
| **MQL** | Marketing Qualified Lead — lead that meets marketing criteria (e.g., downloaded whitepaper, attended webinar) |
| **SQL** | Sales Qualified Lead — lead vetted by sales as having real potential |
| **PQA** | Pre-Qualified Adopter — Wayground-specific: US org with 5+ active teachers on free plan. Strongest pipeline signal |
| **PQL** | Product Qualified Lead — lead showing buying intent through product usage (paywall hits, feature exploration) |
| **BANT** | Budget, Authority, Need, Timeline — qualification framework. Board meeting data includes AI-scored BANT |

## Roles

| Term | Definition |
|------|-----------|
| **BDR** | Business Development Rep — outbound prospecting, books meetings for AEs |
| **AE** | Account Executive — runs discovery, demos, negotiation, closes deals |
| **CS** | Customer Success — post-sale: adoption, renewal, expansion |
| **SE** | Sales Engineer — technical support during demos and evaluations |
| **Champion** | Internal advocate (usually a teacher) who drives the purchase. #1 win reason: teacher requests (619/1,030 won deals) |

## Wayground-Specific Terms

| Term | Definition |
|------|-----------|
| **Paywall Hit** | Teacher tried to access a premium feature on the free plan. Strong buying signal — indicates feature need |
| **Active Teacher** | Teacher with `occupation = 'teacher'` AND `is_classroom_game = TRUE` — real classroom usage |
| **PQA Threshold** | 5+ active teachers = Pre-Qualified Adopter. These accounts convert at highest rates |
| **Closed-Won Fingerprint** | Statistical profile of winning deals built from 1,030 won deals. Used to score pipeline |
| **Discovery Prep Brief** | Pre-call account research document combining product data + board insights + messaging |
| **Board Meeting Notes** | AI-summarized district board meeting minutes stored in `wayagent_GTM.account_feature_store`. 29K items across 787 accounts |
| **GTM Relevance Score** | AI-assigned score indicating how relevant a board meeting topic is to Wayground's value props |
| **Common Assessment (CA)** | District-wide standardized assessments. Key product feature for curriculum directors |
| **Game Changer** | User flag (`is_game_changer`) indicating power user / advocate status |

## Deal Stage Terms

| Term | Definition |
|------|-----------|
| **Discovery** | First substantive conversation — understanding needs, pain, timeline |
| **Demo** | Product demonstration tailored to buyer's use case |
| **Proposal** | Formal pricing/packaging presented to decision maker |
| **Negotiation** | Terms discussion — pricing, contract length, scope |
| **Closed-Won** | Deal signed. Average profile: teacher-driven, 5+ active teachers, board alignment |
| **Closed-Lost** | Deal lost. Top reasons: cold/unresponsive (843), no budget (588), competitor (IXL, MagicSchool) |

## Metrics & Signals

| Term | Definition |
|------|-----------|
| **WAT** | Weekly Active Teachers — teachers who ran at least one classroom game in the past 7 days |
| **MAT** | Monthly Active Teachers — teachers who ran at least one classroom game in the past 30 days |
| **Organic Growth** | Teacher adoption without sales involvement — indicates product-market fit |
| **Land & Expand** | Strategy: win a small deal (school/department) then grow to district-wide |
| **Multi-threading** | Engaging multiple stakeholders in an account (not just one champion) |
| **Whitespace** | Untapped potential within an existing account (more schools, departments, grade levels) |

## Data Sources Referenced

| Source | What It Contains |
|--------|-----------------|
| `clean.*` | Product usage: games, users, quizzes, orgs — source of truth |
| `clean.salesforce_*` | CRM data: opportunities, accounts, contacts, leads |
| `wayagent_GTM.account_feature_store` | 129K accounts with board meetings, usage, contacts, demographics, funding |
| `clean.paid_org` | Paid subscription data — check for existing contracts |
| `clean.org` | Organization entities — districts and schools with `district_id` |
