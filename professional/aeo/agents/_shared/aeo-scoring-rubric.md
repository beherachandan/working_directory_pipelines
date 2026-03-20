# AEO Scoring Rubric

> Used by D1 (AEO Evaluator) and referenced by all content-generating agents.
> Core formula: **Citations × Trust = Share of Voice (SOV)**

## 5-Dimension Scoring (0-10 each)

### 1. QAPE Score
**Question → Answer → Proof → Expansion**

| Score | Criteria |
|-------|----------|
| 9-10 | Crystal clear: explicit question in heading, direct answer in first 1-3 sentences, proof with data/quotes, expansion with depth |
| 7-8 | All QAPE elements present but one is weak (e.g., answer not in first sentences, proof lacks specific data) |
| 5-6 | Missing one QAPE element or structure is implicit rather than explicit |
| 3-4 | Question is unclear or answer is buried; proof is anecdotal |
| 0-2 | No discernible QAPE structure |

### 2. EAR Coverage
**Entity-Attribute-Relationship coverage of sub-queries**

| Score | Criteria |
|-------|----------|
| Formula | `(attributes covered / total target attributes) × 10` |
| 9-10 | ≥90% of target attributes covered with depth |
| 7-8 | 70-89% coverage; all must-cover attributes present |
| 5-6 | 50-69% coverage; some must-cover attributes missing |
| 3-4 | 30-49% coverage; significant gaps |
| 0-2 | <30% coverage |

### 3. Extractability
**Can AI chunk and extract clean answers?**

| Score | Criteria |
|-------|----------|
| 9-10 | Short paragraphs (2-3 lines), bullets/tables where appropriate, question-headings, key passages 40-60 words, no text walls, self-contained answer blocks |
| 7-8 | Mostly extractable; 1-2 long paragraphs or missing question-headings |
| 5-6 | Mixed — some sections extractable, others are prose walls |
| 3-4 | Predominantly long-form prose; few structural aids |
| 0-2 | Wall of text; no structural formatting |

### 4. Trust & Authority
**First-hand signals, statistics, citations, authorship**

| Score | Criteria |
|-------|----------|
| 9-10 | 5+ statistics with sources, 3+ expert quotes with attribution, first-person signals ("we tested", "based on X users"), author byline with credentials |
| 7-8 | 3-4 statistics, 2+ quotes, some first-person signals |
| 5-6 | 1-2 statistics, 1 quote, limited authority signals |
| 3-4 | Claims without backing; no expert attribution |
| 0-2 | No statistics, no quotes, no authority signals |

### 5. Intent Match
**Does content format match the query intent type?**

| Intent Type | Required Format Elements |
|-------------|------------------------|
| Informational ("What is X?") | Definition in first paragraph, expansion, FAQ |
| Comparison ("X vs Y") | Comparison table, criteria rows, "Best For" row, bottom-line |
| Recommendation ("Best X for Y") | Ranked list, criteria explanation, top pick highlighted |
| How-to ("How to X") | Numbered steps, bolded step names, outcome per step |
| Transactional | CTA placement, pricing/feature info, trust signals |

| Score | Criteria |
|-------|----------|
| 9-10 | Perfect format match; all required elements for intent type present |
| 7-8 | Correct format but missing 1 element |
| 5-6 | Partially correct format; key element missing (e.g., comparison without table) |
| 3-4 | Wrong format for intent (e.g., prose essay for a comparison query) |
| 0-2 | No format consideration for intent |

## Gate Logic
- **PASS:** All 5 scores ≥ 7 → proceed to Stage 5 (SME/Teacher vetting)
- **REVISE:** Any score < 7 → return to Stage 3 with specific feedback on failed dimensions
- **Max 2 revision loops** before human escalation
- **Composite score** (for tracking): weighted average — QAPE 25%, EAR 25%, Extract 20%, Trust 20%, Intent 10%

## Platform-Specific Checks (Supplementary)

| Platform | Key Signals | Weight |
|----------|------------|--------|
| Google AIO | Schema markup present? Named sourced citations? E-E-A-T? | Schema = 30-40% boost |
| ChatGPT | Content-answer fit? Freshness date? Domain authority? | Content-answer fit = 55% of citation likelihood |
| Perplexity | Self-contained paragraphs? FAQ schema? Factual density? | FAQ schema critical |
| Claude | Factual density? Named sources? | Extremely selective |
| Copilot | Bing indexed? LinkedIn/GitHub presence? Page load <2s? | Sub-2s load threshold |

## Reference Data
- GEO Paper (arXiv:2311.09735): Quotations +41%, Statistics +33%, Citations +28%, Fluency +29%
- Anti-pattern: Keyword stuffing = -8% visibility
