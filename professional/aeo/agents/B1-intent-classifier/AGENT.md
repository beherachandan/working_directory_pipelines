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
