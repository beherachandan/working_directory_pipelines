# B3: Content Brief Generator Agent

## Identity
- **Phase:** B — Content Planning
- **Stage:** Stage 2 (all substeps)
- **Purpose:** Produce a structured, comprehensive content brief ready for drafting. This is the linchpin agent — all downstream agents depend on the brief quality.
- **Build Priority:** #1 (first agent to build)

## Inputs
- Topic dossier (from A1 + A2)
- Intent classification (from B1)
- EAR attribute list (from B2)
- Internal asset inventory
- Brand voice guide (`_shared/brand-voice-guide.md`)

## Process

### Step 2a: QAPE Skeleton
Define:
- **Question:** The explicit primary question (will become H1 or intro heading)
- **Answer:** Target direct answer (1-3 sentences, 40-60 words — optimal for snippet extraction)
- **Proof:** Required proof types (statistics, expert quotes, first-person data, case studies)
- **Expansion:** Section structure for depth

### Step 2b: Intent × Depth Mapping
Based on intent type (from B1), define required content blocks:
- Informational → Definition Block + Expansion + FAQ
- Comparison → Comparison Table Block + Evidence Sandwich
- Recommendation → Ranked list + Criteria explanation
- How-to → Step-by-Step Block + Example
- Transactional → Feature summary + Trust signals + CTA

### Step 2c: Stats/Quotes Requirements
Set minimums based on content depth:
- Overview: 3+ stats, 1+ quote, 3+ source citations
- Detailed: 5+ stats, 2+ quotes, 5+ source citations
- Comprehensive: 8+ stats, 3+ quotes, 8+ source citations

### Step 2d: Internal Linking Plan
Map the Concept ↔ Tool ↔ Material triangle:
- Which `/learn/` hub this page connects to (parent)
- Which product feature page to link (tool)
- Which resource library page to link (material)
- Related spoke pages (siblings in the hub)

### Step 2e: Format Specification
- Target word count (from B1 depth assessment)
- Heading structure: H2s phrased as questions
- FAQ section: 5-8 items from EAR attributes not fully covered in main body
- Schema type: FAQPage, HowTo, Article (based on intent)
- Author assignment

### Step 2f: Competitive Differentiation
Define what unique angle/data/perspective Wayground brings:
- Proprietary data ("based on 200M+ resources")
- Teacher network insights
- Platform-specific examples
- Gaps in competitor content WG can fill

## Output
**Content Brief** (using `templates/content-brief.md` template) containing:
- QAPE skeleton
- Section-by-section outline with content block types
- EAR attribute → section mapping
- Stats/quotes/citations requirements
- Internal linking plan
- Format specification
- Competitive differentiation angle

## Constraints
- Brief must be detailed enough that a writer/LLM can produce a quality draft without additional context
- Every EAR "must-cover" attribute must have an assigned section
- All required format elements for the intent type must be specified
- Linking plan must follow the Concept ↔ Tool ↔ Material triangle

## Dependencies
- **Upstream:** A1, A2, B1, B2 (all feed into brief)
- **Downstream:** C1-C5 (all use brief for generation), D1 (evaluates against brief targets)

## Skills Repo Reference
- `content-strategy` — prioritization scoring
- `competitor-alternatives` — comparison page frameworks, "X vs Y" templates
- `programmatic-seo` — template design principles

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |
