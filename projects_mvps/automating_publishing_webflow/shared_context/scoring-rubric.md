# Combined GEO + QAPEDS Scoring Rubric

This rubric is used by the GEO_EVALUATOR agent to score article text for AI Engine Optimization (AEO/GEO) readiness.

**Core Formula: Citations × Trust = Share of Voice (SOV)**

---

## GEO Composite Score (0–100)

The GEO Composite is the primary output. It is the weighted sum of 6 dimensions:

| Dimension | Weight | Description |
|-----------|--------|-------------|
| AI Citability | 25% | How extractable and citation-ready is the content? |
| Content E-E-A-T | 20% | Experience, Expertise, Authoritativeness, Trustworthiness signals |
| Platform Optimization | 20% | Readiness for Google AIO, ChatGPT, Perplexity, Gemini, Bing Copilot |
| Brand Voice | 15% | Wayground brand compliance (evaluated separately by BRAND_REVIEWER) |
| SEO Structure | 10% | Heading hierarchy, keyword placement, title/meta/slug |
| Schema Recommendations | 10% | What structured data to add at publish |

**Formula:**
`GEO_Composite = (AI_Citability × 0.25) + (E_E_A_T × 0.20) + (Platform_Opt × 0.20) + (Brand_Voice × 0.15) + (SEO_Structure × 0.10) + (Schema_Recs × 0.10)`

Each dimension is scored 0–100. Brand Voice score comes from BRAND_REVIEWER and is merged in by the orchestrator.

---

## Dimension 1: AI Citability (0–100)

Measures how easily AI systems can extract, chunk, and cite specific passages.

Sub-component weights (from geo-seo-claude citability framework):

| Sub-component | Weight | What to assess |
|---------------|--------|----------------|
| Answer Block Quality | 30% | Are there direct-answer blocks (1-3 sentences, 40-60 words) that directly address the primary query? Do headings introduce them? |
| Self-Containment | 25% | Can blocks be understood without surrounding context? Optimal block length: 134-167 words. |
| Structural Readability | 20% | Proper heading hierarchy (H1→H2→H3), bullet/table usage for key info, no walls of text |
| Statistical Density | 15% | Named stats with attribution, percentages with dates, research references with source names |
| Uniqueness Signals | 10% | Original data, first-party research, first-person practitioner insight ("we tested", "based on X teachers") |

Score each sub-component 0–100. AI Citability = weighted sum.

**Citation Grade:** A (80+), B (65+), C (50+), D (35+), F (<35)

---

## Dimension 2: Content E-E-A-T (0–100)

Google's quality evaluator framework: Experience, Expertise, Authoritativeness, Trustworthiness.

| Sub-component | Weight | What to assess |
|---------------|--------|----------------|
| Experience | 25% | First-hand classroom examples, practitioner perspective, "Ms. Rodriguez found that...", specific scenarios |
| Expertise | 25% | Subject knowledge depth, accurate use of educational terminology, correct frameworks cited |
| Authoritativeness | 25% | Named sources, institutional references, expert quotes with full attribution, research backing |
| Trustworthiness | 25% | Factual accuracy, no unsupported superlatives, balanced view (pros/cons where relevant), transparent limitations |

Score each sub-component 0–100. E-E-A-T = average of four.

**Flag "AI content indicators":** generic phrasing ("In today's fast-paced world"), hedging overload ("it could be argued"), perfect structure with empty substance. These reduce E-E-A-T.

---

## Dimension 3: Platform Optimization (0–100)

Readiness for each AI citation platform. Score each platform 0–100, then average.

| Platform | Weight | Key Signals |
|----------|--------|-------------|
| Google AIO | 25% | Schema markup recommended? Named sourced citations? E-E-A-T signals? Direct answer in first paragraph? FAQ-structured sections? |
| ChatGPT | 25% | Content-answer fit (does the article directly answer its title question)? Freshness signals (year/month in content)? Domain authority signals? |
| Perplexity | 20% | Self-contained paragraphs? FAQ schema recommended? Factual density (stats + named sources per 500 words)? |
| Gemini | 15% | Google ecosystem alignment? Structured data? E-E-A-T? Clear entity definitions? |
| Bing Copilot | 15% | Structured content? Technical SEO basics? Clear entity relationships? |

Platform Optimization = (Google_AIO × 0.25) + (ChatGPT × 0.25) + (Perplexity × 0.20) + (Gemini × 0.15) + (Bing_Copilot × 0.15)

**Platform flags (boolean):**
- `aio_ready`: content has direct answer block + at least one named citation + structured headings
- `chatgpt_ready`: content directly answers the title question with clear factual density
- `perplexity_ready`: has FAQ-structured sections + factual density ≥ 2 named stats per 500 words

---

## Dimension 4: Brand Voice (0–100)

**This dimension is scored by BRAND_REVIEWER, not GEO_EVALUATOR.**
Leave as null in the GEO_EVALUATOR output. The orchestrator fills it in.

---

## Dimension 5: SEO Structure (0–100)

Pre-publish structural recommendations.

| Sub-component | Weight | What to assess |
|---------------|--------|----------------|
| Title Tag quality | 25% | Is the provided title 50-60 chars, includes primary keyword, no clickbait? Suggest optimized version. |
| URL Slug | 20% | Is existing slug SEO-friendly (lowercase, hyphens, keyword-rich, ≤60 chars)? Suggest if missing/poor. |
| Meta Description | 20% | 150-160 chars, includes keyword, has clear value proposition? Suggest one. |
| Heading Hierarchy | 20% | H1 present? H2s every 2-3 paragraphs? H3s for sub-points? Question-phrased or clear topic statements? |
| Keyword Placement | 15% | Primary keyword in H1, first 100 words, at least 2 H2s, conclusion? Natural, not stuffed? |

Score 0–100.

---

## Dimension 6: Schema Recommendations (0–100)

What structured data should be added at publish time.

| Score | Criteria |
|-------|----------|
| 90-100 | Article schema + 2+ additional schemas recommended with complete field mappings |
| 70-89 | Article schema + 1 additional schema recommended |
| 50-69 | Only Article schema recommended |
| 30-49 | Schema recommendations possible but article structure needs work first |
| 0-29 | Cannot recommend schemas until fundamental structural issues are fixed |

**Schema types relevant to education content:**
- `Article` (always) — name, description, author, datePublished, image, publisher
- `FAQPage` — if article has Q&A sections (each question ≥ 40 words)
- `HowTo` — if article is a step-by-step guide (Note: HowTo removed from rich results Sep 2023 but still useful for AI)
- `DefinedTerm` / `EducationalOccupationalCredential` — for definition articles
- `LearningResource` — for educational content targeting teachers

---

## QAPEDS Composite Score (0–10) — Secondary Layer

The QAPEDS score is a secondary evaluation that runs in parallel with GEO dimensions. It is NOT a direct input to GEO Composite — it is a signal reported separately for diagnostic purposes.

### HARD GATING RULES (apply before scoring)

**Gate 1 — Explicit Question Gate**
PASS if: a single, explicit interrogative sentence stating the primary question appears in the title OR within the first 120 words. One question only, human-readable, unambiguous.
FAIL if: intent is implied, title is instructional only, or multiple competing questions exist.
→ If FAIL: Q Score is capped at ≤5

**Gate 2 — Direct Answer Gate**
PASS if: a canonical answer of 1–3 sentences appears within the first 150 words, is structurally isolatable, and can be extracted without surrounding context.
FAIL if: answer is distributed across the article, embedded in narrative, or requires scrolling.
→ If FAIL: A Score is capped at ≤5; S (Structure) Answer Isolation attribute is capped at ≤1

### Scoring (each dimension 0–10)

**Q — Explicit Question (weight: 0.20)**
Does an explicit interrogative question anchor the article? Is it specific, aligned to the target query, uses user language, and singular?

**A — Direct Answer (weight: 0.25)**
Is there a canonical answer within the first 150 words? Is it ≤3 sentences, complete, factually clear, and extractable without context?

**P — Proof / Authority (weight: 0.20)**
Are there named citations, institutional sources, explicit attribution, current data, and practitioner insight? Note: "research shows" without a source caps Evidence Presence at ≤1.

**E — Expansion (weight: 0.15)**
Does the article layer from simple to advanced logically? Is it scannable (headers, bullets, tables)? No redundancy? Natural follow-ups covered?

**D — Decision Enablement (weight: 0.10)**
Are options/paths presented? Trade-offs explicit? Scenario-specific guidance? Clear action steps? Caveats acknowledged?

**S — Structure for Machine Extraction (weight: 0.10)**
Proper header hierarchy? Canonical answer isolatable? Key info in lists/tables? Entities explicitly defined? No fluff?

**QAPEDS Formula:**
`QAPEDS = (Q × 0.20) + (A × 0.25) + (P × 0.20) + (E × 0.15) + (D × 0.10) + (S × 0.10)`

**QAPEDS Verdict:** Strong (≥8.0) | Moderate (6.0–7.9) | Weak (<6.0)

---

## Reference Data (from GEO Research)
- GEO Paper (arXiv:2311.09735): Quotations +41%, Statistics +33%, Citations +28%, Fluency +29%
- H2 opener under 40 words = 2.7× more AI citations
- Anti-pattern: Keyword stuffing = -8% visibility
- FAQ schema critical for Perplexity citations
- sameAs schema is the single most impactful addition for GEO entity recognition
