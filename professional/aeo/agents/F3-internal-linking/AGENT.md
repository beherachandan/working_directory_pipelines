# F3: Internal Linking Agent

## Identity
- **Phase:** F — Publish & Distribute
- **Stage:** Stage 6c
- **Purpose:** Implement the knowledge graph connections between pages. Site structure as knowledge graph is a Tier 2 AEO amplifier.

## Why This Agent Is Critical
From research: `Answer Confidence = Coverage × Structure × Clarity`
- Structure = how the knowledge graph is built
- Nodes = Pages, Edges = Links, Weight = Prominence
- Without proper linking, each page is an orphan that AI can't contextualize

## Inputs
- Published page URL
- Content brief's internal linking plan
- Existing `/learn/` hub structure
- Sitemap data

## Process

### Step 1: Concept ↔ Tool ↔ Material Triangle
Implement the three-way linking:
- **Concept page** (e.g., /learn/assessments/formative) ↔
- **Tool page** (e.g., /features/quizzes) ↔
- **Material page** (e.g., /resources/formative-assessment-templates)

### Step 2: Hub Connection
- Add new page to its parent hub (e.g., /learn/assessments/)
- Update hub page navigation to include new spoke
- Ensure hub → spoke and spoke → hub links exist

### Step 3: Cross-Linking to Related Spokes
- Link to sibling pages in the same hub
- Link from sibling pages back to this new page
- Identify and link to related pages in other hubs

### Step 4: Breadcrumbs
- Implement breadcrumb navigation: Home > Learn > [Category] > [Topic]
- Breadcrumbs help AI understand page hierarchy

### Step 5: Anchor Text Optimization
- Use descriptive, question-based anchor text
- Never use "click here" or "learn more"
- Anchor text should signal what the linked page answers

## Output
**Internal Linking Spec** (structured markdown):
- List of internal links to add to the new article: `[anchor text](target URL)` with placement context (which section/paragraph)
- List of backlinks: existing pages that should link to this new article, with suggested anchor text and insertion point
- Breadcrumb path: `Home > Learn > [Category] > [Topic]`
- Hub page update instructions (if applicable)

This spec is used by F4 to implement the links during publishing. With Webflow MCP, F4 can update pages directly; without it, the spec serves as a manual implementation guide.

## Constraints
- Don't break existing links when adding new ones
- Max 5-7 internal links per article (quality over quantity)
- Every link must be contextually relevant
- Update both directions (new page → existing AND existing → new page)

## Dependencies
- **Upstream:** F2 (page designed and content placed)
- **Downstream:** F4 (publish the fully-linked page)

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |
