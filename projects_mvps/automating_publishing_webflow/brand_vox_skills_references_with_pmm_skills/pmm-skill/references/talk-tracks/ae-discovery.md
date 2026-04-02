# Talk Track: AE Discovery

## When to Use
First substantive conversation with a prospect. Goal: understand their needs, qualify the opportunity, and set up the right demo.

## Pre-Call Prep (MANDATORY)
Before every discovery call, generate a Discovery Prep Brief using:
1. **Account data** from BigQuery (active teachers, games, paywall hits, growth)
2. **Board meeting context** from `wayagent_GTM.account_feature_store`
3. **CRM history** from `clean.salesforce_*` (prior touches, deal history)
4. **Persona identification** — who are you talking to?

## Discovery Framework: DATA Method

### D — District Context
Understand their world before pitching yours.

**Questions:**
- "Can you walk me through your current instructional technology landscape? What tools are teachers using for assessment and engagement?"
- "What are the top 2-3 priorities for your [district/school] this year?"
- "I noticed your board discussed [topic from board data] — how is that shaping your instructional strategy?"

**Data hooks:** Reference board meeting topics, strategic plan themes, state mandates

### A — Assessment & Adoption
Understand their current assessment approach and tool adoption patterns.

**Questions:**
- "How are you currently handling formative assessment across [buildings/classrooms]?"
- "Do you have a Common Assessment strategy, or is each building doing their own thing?"
- "When you adopt a new instructional tool, what does that process look like? Who needs to be involved?"

**Data hooks:** "We see [X] teachers already using Wayground for classroom assessments — is that something you're aware of?"

### T — Teacher Experience
Understand teacher pain points and capacity.

**Questions:**
- "What's the biggest time drain for your teachers right now?"
- "How do teachers typically discover and adopt new instructional tools?"
- "Are teachers creating their own assessments, or mainly using publisher content?"

**Data hooks:** "Your teachers have created [X] quizzes with [Y] questions — they're clearly invested in creating their own content"

### A — Admin Visibility
Understand what data/visibility they need.

**Questions:**
- "What instructional data do you currently have access to? What's missing?"
- "How do you track whether instructional tools are actually being used across your [district/buildings]?"
- "If you could see one data point from every classroom tomorrow, what would it be?"

**Data hooks:** "Right now, [X] teachers are active — premium gives you a dashboard showing all of this"

## Persona-Specific Openers

### Superintendent
> "Thanks for making time. I wanted to share some interesting data — [X] teachers across [District] are already using Wayground in their classrooms. Before I get into what we can do, I'd love to understand what your board's priorities are this year and how instructional technology fits in."

### Curriculum Director
> "I appreciate the time. I know you're focused on [assessment/curriculum initiative from board data]. [X] teachers are already using Wayground for formative assessment — I'd love to understand how that fits with your broader instructional strategy."

### Principal
> "Thanks for chatting. I noticed [X] teachers at [School] are already using Wayground — your building has some of the most active teachers in the district. I'd love to understand what's driving that adoption and what would help you support them better."

### Teacher Champion
> "Hey [Name], you're clearly a power user — [X] games, [Y] students, [Z] quizzes created. I'd love to hear what you love about the platform and what you wish it could do that it can't on the free plan."

## CA-Specific Discovery (Common Assessments)
> Source: Nalin Mujumdar, Mar 6 2026
> Use when: CA is a potential upsell, or the district shows CA-like behavior

When CA is on the table, weave these into the DATA framework. They map naturally:

### CA Persona (fits in D — District Context)
- "Who at your district/sites coordinates these assessments?"
- "Which leader personas view the data from these assessments?"
- "Who finally approves the purchase?"

### CA Use-Case (fits in A — Assessment & Adoption)
- "What's the nature of the common assessments in your district?"
- "How has your experience been conducting CAs?" *(focus on process and outcome learnings, not the tool)*

### CA Tools (fits in A — Assessment & Adoption)
- "Which tools are you currently using for common assessments?"
- "How has your experience been? What's working well? What's not?"

### CA Assessment Development (fits in T — Teacher Experience)
- "How does your school/district build these assessments?"
- **If item banks are a must-have, probe deeper:**
  - Standards alignment requirements?
  - DoK (Depth of Knowledge) coverage?
  - TEI (Technology-Enhanced Items) coverage?
  - Ability to edit/adapt items?
  - Specific item bank brand preference?
  - Efficacy studies or psychometric validity/reliability requirements?
- **Key intel:** Item banks are "nice to have" not "need to have" for most districts (22/26 in our survey). If they insist on item banks, dig into exactly what they need — often it's less than they think.

### CA Success Criteria (fits in A — Admin Visibility)
- "What specific goals do you want to achieve during a CA pilot or implementation?"

### Third-Party Assessment Data (if applicable)
- "Which external assessment data do you want to bring in?"
- **What we support/plan to support:**
  - CSV uploads (student IDs aligned with Clever/Classlink records)
  - State Assessment data for top 10 priority states
  - Universal Screeners like NWEA MAP Growth

### CA Discovery Pre-Fill (Waygent can help)
Before the call, I can pre-fill partial answers using:
- **BigQuery** — CA-like behavior detection (same quiz, 2+ teachers, same school/month)
- **AFS board meetings** — Assessment-related discussions, strategic plan themes
- **SF contacts** — Assessment coordinators, curriculum directors in the account
- **Starbridge** — Current vendor contracts, RFPs, state assessment mandates

## Qualification Checklist (BANT)
By end of discovery, confirm:
- [ ] **Budget:** Is there budget available? When is the budget cycle?
- [ ] **Authority:** Who makes the final decision? Who else needs to be involved?
- [ ] **Need:** What specific problem are they solving? Is it urgent?
- [ ] **Timeline:** When do they need a solution? What's driving the timeline?

## Red Flags
- No specific need identified — just "exploring"
- Single stakeholder with no path to decision maker
- "We just renewed with [competitor] for 3 years"
- No teacher usage data (cold account with no organic adoption)
- Budget cycle doesn't align (just spent their tech budget)

## Next Step Framing
> "Based on what you've shared, I think a [personalized demo / pilot proposal / admin walkthrough] would be the right next step. I'll prepare something focused on [their specific priorities] and we can reconvene [proposed time]. Does that work?"
