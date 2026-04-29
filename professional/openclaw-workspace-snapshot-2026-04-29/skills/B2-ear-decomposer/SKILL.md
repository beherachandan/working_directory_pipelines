---
name: B2-ear-decomposer
description: AEO EAR decomposer for Wayground. Use when breaking a selected content theme into the entities, attributes, and relationships an article must cover. Produces a structured EAR map with must-cover attributes, sub-questions, relationship links, and adjacent reader questions. Required input for B3 content brief generation.
model: claude-sonnet-4-6
---

# B2 — EAR Decomposer

> Breaks a content theme into the full set of Entities, Attributes, and Relationships that the article must cover to achieve high AEO EAR score.

## Role
Answer: **"What does this article need to cover to be complete?"**

## Inputs
- `theme` — selected theme object from A1 (title, slug, intent type, rationale)
- `topic_pillar` — parent pillar
- `product_context` — from `_shared/product-context.md`
- `scoring_rubric` — from `_shared/aeo-scoring-rubric.md` (EAR dimension)

## Output
EAR Map — structured decomposition of must-cover attributes for the article.

## EAR Framework

**Entity:** The main subject (e.g. "formative assessment")
**Attributes:** Properties, characteristics, types, use cases, comparisons, how-tos
**Relationships:** How the entity connects to other concepts (e.g. "formative assessment" → "summative assessment", "student feedback", "learning objectives")

## Process

### Step 1: Define Primary Entity
- State the core entity for this article
- Identify its canonical definition (1-2 sentences)
- Identify Wayground's unique angle on this entity

### Step 2: Attribute Mining
Generate all attributes an authoritative article should cover:

**Standard attribute categories to check:**
- Definition / What is it?
- Types / Variants
- Benefits / Why it matters
- How to implement / Steps
- Examples (classroom-ready)
- Common mistakes / Misconceptions
- Comparison with related concepts
- Tools / Resources (where Wayground fits)
- Metrics / How to measure success
- Grade-level / Context variations (K-5 vs 6-8 vs 9-12)

For each attribute, mark:
- `must-cover` — article fails EAR without this
- `should-cover` — improves score, not blocking
- `nice-to-have` — depth/expansion content

### Step 3: Relationship Mapping
Identify 3-5 related concepts/entities:
- What does this topic connect to in the Wayground content graph?
- Which internal `/learn/` pages should this article link to or from?
- What adjacent queries might a reader have after reading this?

### Step 4: Sub-Question Generation
Convert must-cover attributes into explicit questions (used by B3 for QAPE structure):

Format: `"[Attribute]" → "[Question a teacher would ask]"`

Example:
- Types → "What are the main types of formative assessment?"
- Implementation → "How do you implement formative assessment in a classroom?"
- Comparison → "What's the difference between formative and summative assessment?"

## Output Format

```markdown
## EAR Map: [Theme Title]

**Primary Entity:** [entity name]
**Canonical Definition:** [1-2 sentences]
**Wayground Angle:** [what makes Wayground's take unique]

### Must-Cover Attributes
- [Attribute 1] → Q: "[Sub-question]"
- [Attribute 2] → Q: "[Sub-question]"
- ...

### Should-Cover Attributes
- [Attribute] → Q: "[Sub-question]"
- ...

### Nice-to-Have
- [Attribute]
- ...

### Relationships / Internal Links
- Connects to: [related concept] → [suggested /learn/ URL]
- Connects to: [related concept] → [suggested /learn/ URL]

### Adjacent Reader Questions
- [Question a reader might have next]
- [Question a reader might have next]
```

## EAR Coverage Target
- Must-cover attributes: aim for 5-8 per article (enough to hit EAR ≥ 7)
- Total attributes (must + should): 8-15

## Dependencies
- Reads: `aeo/context/product-context.md`, `aeo/context/aeo-scoring-rubric.md`
- Input from: O1 (theme selection)
- Output to: B3 (Content Brief Generator)
