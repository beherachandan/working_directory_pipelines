# Internal Linking Spec: Exit Tickets Article

**Article URL:** `/learn/assessment/exit-tickets`  
**Date:** 2026-03-18  
**Status:** Ready for F4 implementation

---

## 1. Internal Links in the Article (Already Placed)

The following 7 internal links are already embedded in the C5 article output. No changes needed—these are correctly placed and contextualized:

| # | Target URL | Anchor Text | Placement | Status |
|---|-----------|-------------|-----------|--------|
| 1 | `/learn/assessment/formative-assessment` | formative assessment | Section 1, paragraph 3 ("...89% of public school teachers report using formative assessment strategies...") | ✅ Placed |
| 2 | `/learn/assessment/checking-for-understanding` | checking for understanding techniques | Section 2, final paragraph ("Use exit tickets alongside other checking for understanding techniques...") | ✅ Placed |
| 3 | `/features/quizzes` | Wayground's quiz builder | Step 1, digital tools paragraph | ✅ Placed |
| 4 | `/features/quizzes` | digital quiz tools for quick formative assessment | Step 1, decision table | ✅ Placed |
| 5 | `/activities/assessment` | exit ticket templates | Step 2, after example questions ("Browse exit ticket templates organized by subject...") | ✅ Placed |
| 6 | `/learn/assessment/entrance-tickets` | Entrance tickets | FAQ #1 | ✅ Placed |
| 7 | `/learn/assessment/` | formative assessment strategies | Footer byline ("Browse formative assessment strategies for more...") | ✅ Placed |

**Link Count:** 7 (within 5-7 optimal range)  
**Quality Check:** All links use descriptive anchor text, no "click here" or "learn more" phrases ✅

---

## 2. Backlinks to Add (Existing Pages → New Article)

These existing pages should link TO the new exit tickets article. F4 should implement these updates (or provide as manual tasks if Webflow MCP is unavailable):

### High Priority Backlinks

| Existing Page | Insertion Point | Suggested Anchor Text | Context for Placement |
|---------------|----------------|----------------------|----------------------|
| `/learn/assessment/` (Hub page) | Navigation list of assessment topics | How to Use Exit Tickets in the Classroom | **Add to hub spoke list.** Insert between "Formative Assessment" and "Checking for Understanding" sections. Include 1-2 sentence description: "Quick end-of-lesson checks that help you adjust instruction based on what students know." |
| `/learn/assessment/formative-assessment` | Section on formative assessment strategies/examples | exit tickets | Insert in a section listing formative assessment techniques. Suggested placement: "Common formative assessment strategies include [exit tickets](/learn/assessment/exit-tickets), entrance tickets, quick writes, and think-pair-share activities." |
| `/learn/assessment/entrance-tickets` | Section comparing entrance vs exit tickets (likely in intro or FAQ) | exit tickets | If entrance tickets page exists, it should cross-reference exit tickets. Suggested: "While entrance tickets check prior knowledge at the start of class, [exit tickets](/learn/assessment/exit-tickets) assess learning at the end of the lesson." |
| `/learn/assessment/checking-for-understanding` | Section listing CFU techniques | exit tickets | Insert in a techniques list or examples section. Suggested: "End-of-lesson strategies like [exit tickets](/learn/assessment/exit-tickets) give you a snapshot of student understanding before students leave class." |

### Medium Priority Backlinks

| Existing Page | Insertion Point | Suggested Anchor Text | Context for Placement |
|---------------|----------------|----------------------|----------------------|
| `/features/quizzes` | Use cases or "How Teachers Use Wayground Quizzes" section | quick formative checks like exit tickets | Suggested: "Teachers use Wayground's quiz builder for [quick formative checks like exit tickets](/learn/assessment/exit-tickets) that take 2-3 minutes and provide instant data on student understanding." |
| `/activities/assessment` | Resource library intro or category description | exit tickets guide | Suggested: "Need help designing effective exit tickets? Read our [complete guide to using exit tickets](/learn/assessment/exit-tickets) in the classroom." |

**Total Backlinks:** 6 (4 high priority, 2 medium priority)

---

## 3. Breadcrumb Navigation

Implement the following breadcrumb path at the top of the article:

```
Home > Learn > Assessment > Exit Tickets
```

**Schema Markup for Breadcrumbs** (BreadcrumbList JSON-LD):

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://wayground.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Learn",
      "item": "https://wayground.com/learn"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Assessment",
      "item": "https://wayground.com/learn/assessment"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "Exit Tickets",
      "item": "https://wayground.com/learn/assessment/exit-tickets"
    }
  ]
}
```

**Visual Format:** `Home > Learn > Assessment > Exit Tickets` (with each level clickable except the current page)

---

## 4. Hub Page Update Instructions

**Page:** `/learn/assessment/`

**Action:** Add this new spoke to the hub navigation.

**Suggested Placement:** Insert the exit tickets link in the hub's main content area between existing assessment topics. Recommended position is after "Formative Assessment" and before or alongside "Checking for Understanding."

**Content Block to Add:**

```markdown
### [How to Use Exit Tickets in the Classroom](/learn/assessment/exit-tickets)

Quick end-of-lesson formative assessments that help you identify learning gaps and adjust instruction within 24 hours. Learn how to design, implement, and use exit ticket data to improve student learning.
```

**Hub-to-Spoke Link:** Verify that the hub page includes this link prominently in its navigation or topic list.

**Spoke-to-Hub Link:** Already present (link #7 in Section 1 above) ✅

---

## 5. Concept ↔ Tool ↔ Material Triangle

Verify the three-way knowledge graph connection is complete:

| Node Type | Page | Link Status |
|-----------|------|-------------|
| **Concept** | `/learn/assessment/exit-tickets` (this page) | Core node |
| **Tool** | `/features/quizzes` | ✅ Linked from concept (links #3, #4) |
| **Material** | `/activities/assessment` | ✅ Linked from concept (link #5) |
| **Backlink: Tool → Concept** | `/features/quizzes` → exit tickets article | ⚠️ Needs implementation (medium priority backlink #1) |
| **Backlink: Material → Concept** | `/activities/assessment` → exit tickets article | ⚠️ Needs implementation (medium priority backlink #2) |

**Status:** Forward links complete. Backlinks pending F4 implementation.

---

## 6. Cross-Hub Linking Opportunities (Optional)

If the following pages exist, consider adding contextual links in future updates (beyond initial publish):

- `/learn/classroom-management/` - Exit tickets can be positioned as a classroom routine
- `/learn/lesson-planning/` - Exit tickets as part of lesson closure strategies
- `/learn/pedagogy/feedback` - Connection to feedback loops and formative assessment theory

**Note:** These are optional and should only be added if contextually relevant content exists on both pages. Do not force links for link-building sake.

---

## 7. Anchor Text Quality Checklist

✅ All anchor text is descriptive and question-based or noun-phrase based  
✅ No "click here" or "learn more" phrases  
✅ Anchor text signals what the linked page answers  
✅ Variation in anchor text (no repeated exact-match anchors except for product/resource pages)  
✅ Natural integration within sentence flow  

---

## 8. Link Equity Distribution

**Outbound links from article:** 7 (4 to concept pages, 2 to product page, 1 to resource library)  
**Inbound links to article:** 6 recommended (4 high priority, 2 medium priority)  
**Hub connection:** Bidirectional (article → hub, hub → article)  

This creates a balanced link structure that:
- Positions the article as a hub spoke within `/learn/assessment/`
- Connects to parent concepts (formative assessment, CFU)
- Connects to product/material pages (tools to implement)
- Establishes topical authority through related-spoke links (entrance tickets)

---

## 9. Implementation Priority for F4

1. **Critical (must be done at publish):**
   - Add breadcrumb navigation to article
   - Update hub page (`/learn/assessment/`) to include this spoke

2. **High Priority (within 1 week):**
   - Add backlinks from `/learn/assessment/formative-assessment`
   - Add backlinks from `/learn/assessment/checking-for-understanding`
   - Add backlinks from `/learn/assessment/entrance-tickets` (if page exists)

3. **Medium Priority (within 2 weeks):**
   - Add backlinks from `/features/quizzes`
   - Add backlinks from `/activities/assessment`

---

## 10. Validation Checklist for F4

After implementation, verify:
- [ ] All 7 internal links in article are live and functional
- [ ] Breadcrumbs display correctly and are clickable
- [ ] Hub page lists exit tickets article with description
- [ ] Hub → spoke and spoke → hub bidirectional links work
- [ ] At least 4 backlinks from existing pages are implemented
- [ ] BreadcrumbList schema is added to page `<head>` (see Section 3)
- [ ] No broken links (run link checker)
- [ ] Anchor text displays correctly (no broken formatting)

---

**Internal Linking Spec Complete.**  
This document serves as the implementation guide for F4 (Publisher) to finalize the knowledge graph connections for the exit tickets article.
