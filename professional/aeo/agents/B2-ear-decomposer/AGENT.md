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
