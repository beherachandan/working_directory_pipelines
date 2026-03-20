You are an agent in the Wayground AEO (AI Engine Optimization) Content Engine — a pipeline that produces educational articles optimized for AI citation.

## Core Formula
**Citations × Trust = Share of Voice (SOV)**

## Your Operating Rules

1. **Structured Output:** Wrap your final output in `<output>` tags. Everything outside these tags is treated as scratchpad/reasoning and will not be passed downstream.

2. **Markdown Format:** All output must be well-formatted markdown. Use tables, bullets, headings as appropriate.

3. **Template Compliance:** If a template is provided, fill every field. Use `[NOT AVAILABLE]` for fields you genuinely cannot complete — never leave fields blank or skip them.

4. **Evidence-Based:** Never fabricate statistics, quotes, sources, or data. If you cannot find real data, say so explicitly rather than inventing it.

5. **Wayground Context:** You are producing content for Wayground (formerly Quizizz), an education platform with 200M+ resources. Content lives under `/learn/` and targets US educators (K-12). Always use "Wayground" — never "Quizizz."

6. **Brand Voice:** Sound like a knowledgeable teaching colleague — warm, authoritative, clear. Never sound like a marketing bot. Max 2-3 product mentions per article, always value-adding.

7. **AEO Best Practices:**
   - Short paragraphs (2-3 sentences)
   - Question-phrased headings
   - Key answer passages: 40-60 words (optimal for AI snippet extraction)
   - Statistics with "According to [Source]" framing
   - Expert quotes with full attribution
   - No walls of text, no keyword stuffing, no filler phrases

8. **Upstream Trust:** Treat upstream agent outputs as working material. Build on them, but flag contradictions or quality issues rather than silently propagating errors.

---
## Shared Context

### product-context
# Wayground — Product Context

> All agents in the AEO engine read this file. Keep it current.

## Company
- **Name:** Wayground (formerly Quizizz — rebranded)
- **Product:** Education platform with 200M+ total resources
- **Core offering:** Interactive learning tools — quizzes, lessons, worksheets, flashcards, game-based activities
- **Target market:** US (primary), expanding globally
- **Users:** Teachers (K-12), students, school administrators, district-level buyers
- **Revenue model:** Freemium — free tier for teachers, paid plans for schools/districts

## Key Positioning
- Wayground is a **comprehensive learning platform**, not just a quiz tool
- Differentiation: breadth of resource types, ease of use, gamification, teacher community
- Competitors: Kahoot, Blooket, Edpuzzle, Nearpod, Quizlet, Gimkit

## Content Domain
- All AEO content focuses on **education topics**: pedagogy, assessment types, teaching strategies, classroom management, edtech tools, curriculum design
- Content lives under `/learn/` hub structure (e.g., `/learn/assessments/formative`)
- Content should position Wayground as a knowledgeable, helpful resource for educators — NOT a sales channel

## Internal Asset Types
- **Activity Detail Pages (ADPs):** Individual resource pages (quizzes, lessons)
- **Resource Library pages:** Searchable collections by subject/grade/type
- **Learn hub pages:** Educational content organized by topic (`/learn/`)
- **Product pages:** Feature-specific pages (e.g., /features/quizzes)

## E-E-A-T Signals
- Author pages with credentials and social profiles
- Teacher network providing SME vetting (~30 articles through review loop)
- UXR team for user research backing
- "Based on X users" and "we tested" first-person authority signals

---
## Your Agent Definition

# G1: SOV Tracker Agent

## Identity
- **Phase:** G — Monitor & Learn
- **Stage:** WF5
- **Purpose:** Monitor whether published content gets cited by AI engines and track Share of Voice trends.

## Why This Agent Is Critical
"Can't optimize what you can't measure" — Observability is Tier 3 enabler (#10).
Without tracking, the pipeline operates blind. This agent closes the loop between "published" and "working."

## Inputs
- Published page URLs
- Target queries (from content briefs)
- AI engine access (ChatGPT, Perplexity, Google AIO)

## Process

### Step 1: AI Engine Monitoring (Weekly)
For each target query, run through:
- ChatGPT (latest model)
- Perplexity
- Google AI Overview
- Claude (if testable)
- Copilot

Record:
- Is Wayground cited? (Yes/No)
- Which URL is cited?
- What passage/snippet is used?
- Position in the AI response (first citation, supporting, etc.)

### Step 2: Citation Attribution
Track per published page:
- Which AI engines cite it
- For which queries
- How the citation is framed
- What competing sources are also cited

### Step 3: SOV Calculation
```
SOV = (Queries where WG is cited / Total target queries) × 100
```
Track over 30 / 60 / 90 day windows.

### Step 4: Pattern Analysis
Identify:
- Which content characteristics correlate with citation (format, depth, citations, schema)
- Which platforms cite WG most/least
- Which topics have highest citation rates
- Which content blocks get extracted most

## Output
**SOV Monitoring Report** (structured markdown):

```
## SOV Monitoring Report — {article slug}
### Monitoring Setup
- Target Queries: [list from content brief]
- Published URL: [from F4]
- Monitoring Start Date: [publish date]

### Baseline Check (AI Engine Citation Status)
| AI Engine | Query | Cited? | Position | Snippet Used | Competing Sources |
|-----------|-------|--------|----------|-------------|-------------------|
| ChatGPT   | ...   | ...    | ...      | ...         | ...               |

### SOV Summary
- Current SOV: X% (Y of Z target queries citing Wayground)
- 30-day trend: [baseline → current]

### Pattern Analysis
- Content characteristics correlated with citation
- Best-performing content blocks
- Engines with highest/lowest citation rates

### Alerts
- Citations gained/lost since last check
- Competitor movements

### Recommended Actions
- Specific next steps for G2 feedback loop
```

When running as an LLM agent: produces the report structure with baseline checks using available search/web tools. For ongoing weekly monitoring, the report template guides manual or automated follow-up checks.

## Constraints
- AI engine outputs change — timestamp and version-note all captures
- Monitor at consistent intervals (weekly minimum)
- Don't game AI engines — monitor naturally
- Manual monitoring is acceptable initially; automate as scale requires

## Tools
- Otterly AI
- Peec AI
- ZipTie
- LLMrefs
- DIY manual checks (initial approach)

## Dependencies
- **Upstream:** F4 (published pages to monitor)
- **Downstream:** G2 (analyzes SOV data for pipeline feedback)

## Changelog
| Date | Change |
|------|--------|
| 2026-03-16 | Initial agent definition |

---
## Task Payload

**Topic:** What are formative assessment strategies?

### Upstream Agent Outputs

#### F4 Output

# F4 Deployment Report: Formative Assessment Strategies Article

**Article Title:** What Are Formative Assessment Strategies, and How Do Teachers Use Them to Improve Learning?  
**Target URL:** `https://wayground.com/learn/assessments/formative-assessment-strategies`  
**Deployment Mode:** Manual (Phase 1 - No MCP)  
**Date Prepared:** 2026-03-18  
**Status:** READY FOR MANUAL CMS ENTRY

---

## Executive Summary

All content, schema markup, and technical specifications are prepared and ready for manual deployment to Webflow CMS. This report provides step-by-step instructions for:

1. Creating the CMS item with all content fields
2. Embedding schema markup for AI citation optimization
3. Configuring internal links and navigation
4. Submitting for indexing and verification
5. Post-launch validation checklist

**Estimated Manual Entry Time:** 45-60 minutes

---

## 1. CMS DEPLOYMENT CHECKLIST

### Step 1.1: Create New CMS Collection Item

**Collection:** Learn Hub Articles  
**Action:** Create new item

| Field Name | Value | Status |
|------------|-------|--------|
| **Title** | What Are Formative Assessment Strategies, and How Do Teachers Use Them to Improve Learning? | MANUAL |
| **URL Slug** | `formative-assessment-strategies` | MANUAL |
| **Category** | Assessments | MANUAL |
| **Parent Hub Path** | `/learn/assessments/` | MANUAL |
| **Date Published** | 2026-03-18 | MANUAL |
| **Date Modified** | 2026-03-18 (auto-update on future edits) | MANUAL |
| **Reading Time** | 14 min | MANUAL |
| **Word Count** | 3,100 | MANUAL |
| **Target Grade Levels** | K-12 (all grades) | MANUAL |

**Instructions:**
1. Navigate to Webflow CMS → Learn Hub Articles collection
2. Click "Create New Article"
3. Fill in all fields above exactly as specified
4. Verify slug generates correct URL: `/learn/assessments/formative-assessment-strategies`

---

### Step 1.2: Add Meta Fields for SEO

| Meta Field | Value | Character Count | Status |
|------------|-------|----------------|--------|
| **Meta Title** | What Are Formative Assessment Strategies? 15 Proven Techniques \| Wayground | 75 chars | MANUAL |
| **Meta Description** | Formative assessment strategies are techniques teachers use during instruction to check student understanding and adjust teaching in real time. Discover 15 proven strategies with examples. | 195 chars | MANUAL |
| **Meta Keywords** | formative assessment, exit tickets, assessment strategies, teacher assessment, classroom assessment | N/A | MANUAL |

**Instructions:**
1. In CMS item settings, locate SEO section
2. Paste meta title and description exactly as shown
3. Verify character counts (title <80, description <200)

---

### Step 1.3: Add Article Content Body

**Source:** C5 Output (composed article)

**Instructions:**
1. Copy the ENTIRE article content from the C5 output section (starting with the opening paragraph "Formative assessment strategies are techniques..." through the final FAQ section)
2. Paste into the Rich Text Editor field in Webflow
3. **Critical:** Verify all formatting is preserved:
   - Bold headings (H2, H3, H4)
   - Bullet lists and numbered lists
   - Blockquotes (pull quotes)
   - Tables (3 tables total)
   - Internal links (15 links - see Section 3 below for verification)

**Content Sections to Include (verify all present):**
- ✅ Opening key answer paragraph
- ✅ Section 1: What Is Formative Assessment?
- ✅ Section 2: Why Does Formative Assessment Matter?
- ✅ Section 3: How Is Formative Assessment Different? (with comparison table)
- ✅ Section 4: 15 Strategies (organized by time: quick checks, deeper checks, ongoing)
- ✅ Section 5: Implementation (with 5-step framework + grade-level table)
- ✅ Section 6: Frequency
- ✅ Section 7: Data Use
- ✅ Section 8: Digital Tools (with tools comparison table)
- ✅ Section 9: Common Mistakes (7 pitfalls)
- ✅ Section 10: FAQ (8 questions in accordion format)

---

### Step 1.4: Embed Schema Markup in Page Head

**Schema Types Required:** Article, FAQPage, HowTo

**Instructions:**
1. In Webflow page settings, locate "Custom Code" → "Head Code" section
2. Paste ALL THREE schema blocks below into the `<head>` section
3. Each block must be wrapped in `<script type="application/ld+json">` tags

#### Schema Block 1: Article Schema

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What Are Formative Assessment Strategies, and How Do Teachers Use Them to Improve Learning?",
  "description": "Formative assessment strategies are techniques teachers use during instruction to check student understanding and adjust teaching in real time. Learn 15 proven strategies organized by time, implementation steps, and grade-level adaptations backed by research from John Hattie, Dylan Wiliam, and platform data from 200M+ resources.",
  "image": "https://wayground.com/images/formative-assessment-strategies-hero.jpg",
  "author": {
    "@type": "Person",
    "name": "[Education Content Lead]",
    "jobTitle": "Education Content Lead",
    "description": "M.Ed., 12 years in K-12 education and instructional leadership"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Wayground",
    "logo": {
      "@type": "ImageObject",
      "url": "https://wayground.com/logo.png"
    }
  },
  "datePublished": "2026-03-18",
  "dateModified": "2026-03-18",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://wayground.com/learn/assessments/formative-assessment-strategies"
  }
}
</script>
```

**Action Item:** Replace `[Education Content Lead]` with actual author name before publishing.

#### Schema Block 2: FAQPage Schema

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does formative assessment take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most formative assessments take 1-5 minutes for quick checks (exit tickets, polls, fist to five) and 5-15 minutes for deeper checks (gallery walks, one-minute essays). Ongoing strategies like observation checklists integrate into existing instruction with no additional time. A realistic daily investment is 5-10 minutes total for a high-frequency formative practice."
      }
    },
    {
      "@type": "Question",
      "name": "Can I use formative assessment for grading?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Technically yes, but doing so undermines its purpose. When students know a check counts toward their grade, they prioritize looking correct over revealing confusion—and you lose the honest data you need. If you want accountability, consider completion credit or practice points rather than accuracy-based grading."
      }
    },
    {
      "@type": "Question",
      "name": "What if students don't take formative assessment seriously?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Build a classroom culture where showing confusion is safe and valued. Explain to students that you use their responses to help them—share how you adjusted a lesson based on their exit tickets. Gamification also helps: platforms like Wayground increase engagement through game-based formative checks. Over time, show students their own progress data so they see the value."
      }
    },
    {
      "@type": "Question",
      "name": "How do I formatively assess remote or hybrid students?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Digital tools are essential for remote formative assessment. Use quick polls for instant feedback, digital exit tickets, and chat-based responses (thumbs up/down emoji) for synchronous sessions. For asynchronous learning, discussion board prompts, recorded video explanations, and self-paced quizzes on platforms like Wayground provide formative data even when students aren't online simultaneously."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between formal and informal formative assessment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Formal formative assessments are planned and structured—exit tickets, quizzes, written reflections—with documented student responses. Informal formative assessments are observational and spontaneous—listening to student conversations, asking probing questions while circulating, noting body language during instruction. Both are valuable; informal assessment requires a strong mental or physical tracking system to be actionable."
      }
    },
    {
      "@type": "Question",
      "name": "How do I store and organize formative assessment data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Match your system to your volume and comfort level. Low-tech: sticky notes sorted by student or a notebook with one page per student. Mid-tech: a spreadsheet with student names as rows and skills as columns. High-tech: a platform like Wayground with automatic data aggregation and analytics dashboards. The key is consistency over sophistication—pick a system you'll actually maintain."
      }
    },
    {
      "@type": "Question",
      "name": "Can formative assessment work for all subjects?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. The strategies adapt across every discipline. STEM subjects use problem-solving checks and error analysis. Humanities use discussion-based assessments and written reflections. Arts use critique protocols and self-assessment. Physical education uses skill demonstration checklists and peer feedback. The core principle—check understanding and adjust instruction—is universal."
      }
    },
    {
      "@type": "Question",
      "name": "How is formative assessment different from diagnostic assessment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Diagnostic assessment happens before a unit begins to identify students' starting points, prior knowledge, and potential misconceptions. Formative assessment happens during instruction to monitor progress and adjust teaching. Summative assessment happens after instruction to evaluate outcomes. All three serve different purposes and are needed at different points in the learning cycle."
      }
    }
  ]
}
</script>
```

#### Schema Block 3: HowTo Schema

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Implement Formative Assessment in Your Classroom",
  "description": "A five-step framework for building a formative assessment practice that works across grade levels, from choosing your first strategy to establishing a sustainable rhythm.",
  "totalTime": "PT2W",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Start with one strategy",
      "text": "Choose one quick check from the list above—exit tickets are a strong starting point—and use it consistently for two weeks. Mastering one strategy before adding more prevents overwhelm and lets you build the habit of acting on the data you collect.",
      "position": 1
    },
    {
      "@type": "HowToStep",
      "name": "Build your question bank",
      "text": "Identify 10-15 key understanding checkpoints for your current unit, aligned directly to learning objectives. Pre-planning your formative questions reduces cognitive load during instruction so you can focus on teaching and responding rather than improvising prompts.",
      "position": 2
    },
    {
      "@type": "HowToStep",
      "name": "Create a feedback loop",
      "text": "Decide how you'll track student responses and translate them into instructional adjustments. Data only matters if it informs your next move—whether that's a quick re-teach, a small group pullout, or moving ahead. A simple spreadsheet or Wayground's analytics dashboard both work.",
      "position": 3
    },
    {
      "@type": "HowToStep",
      "name": "Add variety gradually",
      "text": "Once your first strategy is routine—typically after 3-4 weeks—add one or two more formats. Multi-modal assessment reaches all learners: pair exit tickets with think-pair-share, or add quick polls alongside observation checklists.",
      "position": 4
    },
    {
      "@type": "HowToStep",
      "name": "Build a sustainable rhythm",
      "text": "Establish which strategies are daily (quick checks), weekly (deeper checks), and unit-level (ongoing strategies). Consistency yields better data than sporadic use.",
      "position": 5
    }
  ]
}
</script>
```

**Validation Required:** After pasting all three blocks, validate using Google Rich Results Test (see Step 5.1).

---

### Step 1.5: Configure Author Information

**Author Fields:**

| Field | Value | Status |
|-------|-------|--------|
| **Author Name** | [Education Content Lead] (replace with actual name) | MANUAL |
| **Author Credentials** | M.Ed., 12 years in K-12 education and instructional leadership | MANUAL |
| **Author Bio** | [Full bio paragraph - see F2 output author section] | MANUAL |
| **Author Photo** | Upload author headshot (120×120px, optimized <30KB) | MANUAL |
| **LinkedIn URL** | https://www.linkedin.com/in/[author-linkedin] | MANUAL |
| **Twitter URL** | https://twitter.com/[author-twitter] | MANUAL |

**Instructions:**
1. If Author collection exists in Webflow: Create/link author profile
2. If not: Add author information directly to article template fields
3. Ensure author photo is optimized (WebP format preferred, JPEG fallback)

---

## 2. SITEMAP INCLUSION

### Step 2.1: Add to XML Sitemap

**Target Sitemap:** `https://wayground.com/sitemap.xml`

**Instructions:**
1. Verify Webflow auto-generates sitemap entries for CMS collection items
2. If manual sitemap: Add the following entry:

```xml
<url>
  <loc>https://wayground.com/learn/assessments/formative-assessment-strategies</loc>
  <lastmod>2026-03-18</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

**Priority Rationale:** 0.8 (high priority) — pillar content for assessments hub

**Status:** MANUAL - Verify after publish

---

### Step 2.2: Verify Sitemap Accessibility

**Action:** After publish, test sitemap access

1. Navigate to: `https://wayground.com/sitemap.xml`
2. Verify page URL appears in sitemap
3. Check sitemap size: Must be <50MB and <50,000 URLs (Google requirement)
4. If sitemap is split: Ensure this page is in the correct sitemap segment

**Status:** MANUAL - Post-publish verification required

---

## 3. INTERNAL LINKING CONFIGURATION

### Step 3.1: Verify Internal Links in Article

**Total Internal Links:** 15 instances across 12 unique pages

**Verification Checklist:**

| # | Anchor Text | Target URL | Section | Status |
|---|-------------|------------|---------|--------|
| 1 | formative assessment | /learn/assessments/ | Section 1 | MANUAL |
| 2 | assessment strategies for teachers | /learn/assessments/ | Section 3 | MANUAL |
| 3 | summative assessment | /learn/assessments/summative-assessment | Section 3 | MANUAL |
| 4 | exit ticket strategies and templates | /learn/assessments/exit-tickets | Section 4, Strategy #1 | MANUAL |
| 5 | ready-to-use formative assessment templates | /worksheets/assessment-templates | Section 4, Strategy #1 | MANUAL |
| 6 | quick poll | /features/polls | Section 4, Strategy #3 | MANUAL |
| 7 | ready-to-use formative assessment templates | /worksheets/assessment-templates | Section 4, Strategy #12 | MANUAL |
| 8 | formative assessment quiz on Wayground | /features/quizzes | Section 4, Strategy #15 | MANUAL |
| 9 | interactive lessons with embedded checks | /features/lessons | Section 4, Strategy #15 | MANUAL |
| 10 | formative assessment activities for math | /activities/math | Section 4, Strategy #15 | MANUAL |
| 11 | differentiated instruction using formative data | /learn/differentiation/differentiated-instruction | Section 7 | MANUAL |
| 12 | effective feedback strategies | /learn/classroom-management/feedback-strategies | Section 7 | MANUAL |
| 13 | real-time quiz tools for formative assessment | /features/quizzes | Section 8 | MANUAL |
| 14 | science formative assessment examples | /activities/science | Section 10, FAQ #7 | MANUAL |
| 15 | diagnostic assessment | /learn/assessments/diagnostic-assessment | Section 10, FAQ #8 (2 instances) | MANUAL |

**Action Required:**
1. After pasting content, verify each link is clickable and points to correct URL
2. Test all 15 links before publishing
3. Use relative URLs (e.g., `/learn/assessments/` not full `https://wayground.com/learn/assessments/`)

**Status:** MANUAL - Verification required after content entry

---

### Step 3.2: Add Breadcrumb Navigation

**Breadcrumb Path:** Home > Learn > Assessments > Formative Assessment Strategies

**Schema Markup for Breadcrumb:**

```html
<nav aria-label="Breadcrumb">
  <ol itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/">
        <span itemprop="name">Home</span>
      </a>
      <meta itemprop="position" content="1" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/learn/">
        <span itemprop="name">Learn</span>
      </a>
      <meta itemprop="position" content="2" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/learn/assessments/">
        <span itemprop="name">Assessments</span>
      </a>
      <meta itemprop="position" content="3" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <span itemprop="name">Formative Assessment Strategies</span>
      <meta itemprop="position" content="4" />
    </li>
  </ol>
</nav>
```

**Instructions:**
1. Add breadcrumb component to article template if not auto-generated
2. Paste breadcrumb markup above article title
3. Verify all breadcrumb links are functional

**Status:** MANUAL - Template configuration required

---

### Step 3.3: Update Hub Page (Critical)

**Target Page:** `/learn/assessments/` (Assessments Hub)

**Action Required:** Add this article as a featured spoke in the hub navigation

**Recommended Hub Entry Text:**

```markdown
### [Formative Assessment Strategies](/learn/assessments/formative-assessment-strategies)

Learn 15 proven formative assessment strategies backed by research from John Hattie and Dylan Wiliam. Includes grade-level adaptations (K-2, 3-5, 6-8, 9-12), implementation guides, digital tool comparisons, and classroom examples. Discover how to use exit tickets, quick polls, think-pair-share, and 12 other techniques to monitor learning in real time.

**Key Topics:** Exit tickets, observation checklists, digital quizzes, think-pair-share, gallery walks, feedback loops, formative vs. summative assessment
```

**Instructions:**
1. Navigate to `/learn/assessments/` in Webflow CMS
2. Add the hub entry above to the main navigation section
3. Position as primary or secondary spoke (pillar content)
4. Save and publish hub page update

**Status:** MANUAL - Hub page edit required

---

### Step 3.4: Add Backlinks (Priority Order)

**High-Priority Backlinks** (complete within 48 hours of publish):

| Source Page | Action | Priority |
|-------------|--------|----------|
| `/learn/assessments/` | Add featured spoke entry (Step 3.3) | CRITICAL |
| `/learn/assessments/summative-assessment` | Add link in introduction or comparison section | HIGH |
| `/learn/assessments/exit-tickets` | Add link positioning exit tickets as one strategy | HIGH |
| `/learn/assessments/diagnostic-assessment` | Add link clarifying distinction | HIGH |

**Medium-Priority Backlinks** (complete within 1 week):

| Source Page | Suggested Link Context |
|-------------|----------------------|
| `/learn/differentiation/differentiated-instruction` | "Use [formative assessment strategies] to gather data for differentiation" |
| `/learn/classroom-management/feedback-strategies` | "Effective feedback begins with [formative assessment strategies]" |
| `/features/quizzes` | "Teachers use quizzes to implement [formative assessment strategies]" |
| `/features/lessons` | "Build [formative assessment strategies] into lessons" |
| `/features/polls` | "Quick polls are a core [formative assessment strategy]" |

**Status:** MANUAL - Requires editing 12 existing pages (see F3 output Section 2 for detailed instructions)

---

## 4. SEARCH CONSOLE SUBMISSION

### Step 4.1: Submit URL for Indexing

**Platform:** Google Search Console

**Instructions:**

1. Log into Google Search Console: https://search.google.com/search-console
2. Select property: wayground.com
3. Navigate to URL Inspection tool (left sidebar)
4. Enter URL: `https://wayground.com/learn/assessments/formative-assessment-strategies`
5. Click "Request Indexing"
6. Wait for confirmation message (typically appears within 1-2 minutes)
7. Monitor indexing status (can take 24-48 hours for page to appear in search results)

**Expected Timeline:**
- Request submitted: Immediate
- Crawled by Googlebot: 1-7 days
- Indexed and ranking: 3-14 days

**Status:** MANUAL - Post-publish action required

---

### Step 4.2: Monitor for Crawl Errors

**Action:** Check Google Search Console for errors 48 hours after indexing request

**Common errors to check:**
- 404 (Page not found) - Verify URL is live
- 500 (Server error) - Check page loads correctly
- Redirect errors - Ensure no unintended redirects
- Mobile usability errors - Test mobile rendering
- Schema validation errors - Re-run Rich Results Test

**Status:** MANUAL - Post-publish monitoring required

---

## 5. AI BOT ACCESS VERIFICATION

### Step 5.1: Verify robots.txt Configuration

**Target File:** `https://wayground.com/robots.txt`

**Required AI Bot User-Agents (must NOT be blocked):**

```
User-agent: GPTBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Googlebot
Allow: /
```

**Verification Steps:**

1. Navigate to: `https://wayground.com/robots.txt`
2. Verify NO disallow rules block the bots above
3. Verify `/learn/` path is not blocked
4. Check for wildcard blocks that might affect AI bots

**Common Blocking Patterns to Avoid:**
- ❌ `User-agent: * / Disallow: /learn/`
- ❌ `User-agent: GPTBot / Disallow: /`
- ❌ Blocking all bots except Googlebot

**If robots.txt blocks AI bots:**
1. Contact dev team to update robots.txt
2. Remove restrictive disallow rules
3. Re-test after update
4. Wait 24-48 hours for bots to re-crawl robots.txt

**Status:** MANUAL - Verify current robots.txt configuration

**Current Status Check:**
- [ ] GPTBot allowed
- [ ] PerplexityBot allowed
- [ ] ClaudeBot allowed
- [ ] Google-Extended allowed
- [ ] Bingbot allowed
- [ ] No wildcard blocks affecting AI bots

---

### Step 5.2: Test AI Bot Crawlability

**Manual Test Options:**

1. **Google Rich Results Test** (validates schema + crawlability):
   - URL: https://search.google.com/test/rich-results
   - Paste full page URL after publish
   - Verify all 3 schema types validate (Article, FAQPage, HowTo)
   - Check for crawl errors or blocked resources

2. **Schema Markup Validator** (validates JSON-LD syntax):
   - URL: https://validator.schema.org/
   - Paste page URL or schema JSON directly
   - Verify no syntax errors
   - Check all required fields present

3. **Mobile-Friendly Test** (ensures mobile crawlability):
   - URL: https://search.google.com/test/mobile-friendly
   - Enter page URL
   - Verify page is mobile-friendly (Copilot requires <2s load on mobile)

**Status:** MANUAL - Run all 3 tests post-publish

---

## 6. PERFORMANCE VERIFICATION

### Step 6.1: Page Load Speed Check

**Target:** <2 seconds (Copilot threshold for citation eligibility)

**Test Tools:**
1. **Google PageSpeed Insights:** https://pagespeed.web.dev/
2. **WebPageTest:** https://www.webpagetest.org/
3. **GTmetrix:** https://gtmetrix.com/

**Key Metrics to Check:**

| Metric | Target | Critical For |
|--------|--------|-------------|
| First Contentful Paint (FCP) | <1.2s | User experience |
| Largest Contentful Paint (LCP) | <2.0s | Core Web Vitals, AI citation |
| Time to Interactive (TTI) | <2.5s | Engagement |
| Total Page Load | <2.0s | Copilot eligibility |

**If page load >2 seconds:**

**Optimization Actions:**
1. Optimize images (WebP format, lazy loading, compression)
2. Minify CSS/JS files
3. Enable Gzip/Brotli compression
4. Use CDN for static assets
5. Reduce third-party scripts
6. Implement critical CSS inlining

**Status:** MANUAL - Test after publish, optimize if needed

---

### Step 6.2: Mobile Rendering Verification

**Action:** Test page on mobile devices (70%+ of traffic is mobile)

**Test Checklist:**
- [ ] All 3 tables render correctly (responsive table layout or horizontal scroll)
- [ ] FAQ accordion expands/collapses on tap
- [ ] All internal links are tappable (44×44px minimum)
- [ ] Images load and display correctly
- [ ] Text is readable without zooming (16px minimum)
- [ ] CTA buttons are tappable and functional
- [ ] No horizontal overflow or cut-off content

**Test Devices:**
- iPhone (Safari)
- Android phone (Chrome)
- Tablet (iPad or Android)

**Status:** MANUAL - Physical device testing required

---

### Step 6.3: Broken Link Check

**Action:** Verify all 15 internal links are functional

**Tools:**
- **Manual:** Click each link and verify destination loads
- **Automated:** Use broken link checker tools
  - W3C Link Checker: https://validator.w3.org/checklink
  - Broken Link Checker Chrome Extension
  - Screaming Frog SEO Spider (desktop app)

**Status:** MANUAL - Test all 15 links post-publish

---

## 7. GO-LIVE CHECKLIST

### Master Go-Live Checklist

| Item | Requirement | Status | Notes |
|------|------------|--------|-------|
| **1. CMS Entry** | Article content, meta fields, author info entered | MANUAL | Complete Steps 1.1-1.5 |
| **2. Schema Markup** | 3 JSON-LD blocks embedded in page head | MANUAL | Validate with Rich Results Test |
| **3. Internal Links** | All 15 links functional, pointing to correct URLs | MANUAL | Click-test each link |
| **4. Breadcrumb** | Breadcrumb navigation with schema present | MANUAL | Verify 4-level path |
| **5. Hub Update** | Featured spoke added to /learn/assessments/ hub | MANUAL | Critical for discoverability |
| **6. Sitemap** | Page URL in sitemap.xml, sitemap accessible | MANUAL | Verify after publish |
| **7. GSC Submission** | URL submitted to Google Search Console | MANUAL | Submit within 24h of publish |
| **8. robots.txt** | AI bots NOT blocked (GPTBot, Perplexity, Claude, Google-Extended, Bingbot) | MANUAL | Verify current config |
| **9. Page Load** | Load time <2 seconds on 3G | MANUAL | Test with PageSpeed Insights |
| **10. Mobile** | Mobile rendering correct, no usability issues | MANUAL | Test on real devices |
| **11. Schema Valid** | All 3 schema types pass Rich Results Test | MANUAL | Run validation post-publish |
| **12. Links Test** | No broken links (internal or external) | MANUAL | Use link checker tool |
| **13. Author Page** | Author profile linked with credentials | MANUAL | Verify author page live |
| **14. Images** | All images optimized, load correctly, have alt text | MANUAL | Check hero image, author photo |
| **15. Backlinks** | High-priority backlinks added (4 pages) | MANUAL | Complete within 48h |

**Go-Live Decision:**
- ✅ **PROCEED TO PUBLISH** if items 1-5 are COMPLETE
- ⚠️ **PUBLISH WITH MONITORING** if items 6-14 will be completed post-publish
- ❌ **DO NOT PUBLISH** if any items 1-5 are incomplete

---

## 8. POST-PUBLISH MONITORING (24-48 Hours)

### Monitoring Tasks

| Task | Timeline | Action |
|------|----------|--------|
| **Indexing Status** | 24 hours | Check GSC → Coverage report for page URL |
| **Crawl Errors** | 48 hours | Check GSC → Coverage → Errors tab |
| **Schema Validation** | 24 hours | Re-run Rich Results Test, verify no errors |
| **Mobile Usability** | 48 hours | Check GSC → Mobile Usability report |
| **Page Load** | 24 hours | Re-test PageSpeed Insights, optimize if >2s |
| **Internal Links** | 24 hours | Verify no broken link reports |
| **AI Bot Crawls** | 7 days | Monitor server logs for GPTBot, PerplexityBot, ClaudeBot visits |

**Status:** MANUAL - Scheduled monitoring required

---

## 9. HANDOFF SUMMARY

### For F5 (Distribution Agent)

**Page Status:** Ready for distribution once published

**Distribution Channels to Activate:**
1. **Social Media:** Share article on Wayground Twitter, LinkedIn, Facebook
2. **Email Newsletter:** Feature in next "Learn Hub Update" newsletter
3. **Teacher Network:** Share with 30+ teacher vetting network for feedback/amplification
4. **Educator Communities:** Post in relevant Facebook groups, Reddit r/Teachers, WeAreTeachers
5. **Partnerships:** Share with education influencers, K-12 blogs for potential backlinks

**Distribution Assets Needed:**
- Social media snippet (40-60 word summary with link)
- Email newsletter blurb (100-150 words)
- Featured image for social sharing (1200×630px)

**Priority:** HIGH (pillar content for assessments hub)

---

### For G1 (SOV Monitoring Agent)

**Tracking Setup Required:**

**Primary Keywords to Monitor:**
1. "formative assessment strategies"
2. "what are formative assessment strategies"
3. "formative assessment examples"
4. "exit tickets formative assessment"
5. "how to use formative assessment"
6. "formative vs summative assessment"
7. "formative assessment tools"
8. "classroom assessment strategies"

**Monitoring Platforms:**
- Perplexity.ai (query all 8 keywords monthly)
- ChatGPT Search (query all 8 keywords monthly)
- Google AIO (query when available)
- Microsoft Copilot (query all 8 keywords monthly)

**Success Metrics:**
- Citation appearance rate: Target 40%+ (cited in 3+ out of 8 queries)
- Position in citation list: Target top 3 citations
- Attribution quality: Full title + URL displayed
- Time to first citation: Baseline 7-14 days post-index

**Baseline Measurement:**
- Run initial queries 14 days after Google indexing confirmation
- Document citation rate before distribution push (F5)
- Re-measure 30 days post-distribution to assess lift

**Alert Triggers:**
- Citation rate <20% after 30 days → Investigate content gaps or technical issues
- Zero citations after 45 days → Escalate to content team for review

---

## 10. DEPLOYMENT SUMMARY

### Current Status: READY FOR MANUAL CMS ENTRY

**Prepared Deliverables:**
- ✅ Complete article content (3,100 words, 15 strategies, 8 FAQs)
- ✅ 3 schema markup blocks (Article, FAQPage, HowTo)
- ✅ 15 internal links verified and specified
- ✅ Complete HTML/design specification (F2)
- ✅ Breadcrumb navigation markup
- ✅ Meta title and description (SEO-optimized)
- ✅ Author information fields specified
- ✅ Go-live checklist with validation steps

**Estimated Time to Publish:**
- CMS entry: 45-60 minutes
- Post-publish validation: 30 minutes
- Total: 75-90 minutes

**Critical Path:**
1. Complete Steps 1.1-1.5 (CMS entry + schema)
2. Verify Steps 3.1-3.2 (internal links + breadcrumb)
3. Complete Step 3.3 (hub page update) ← CRITICAL
4. Publish page
5. Complete Step 4.1 (GSC submission) within 24 hours
6. Monitor checklist items 24-48 hours post-publish

**Blocking Issues:** NONE - All content and specifications ready

**Next Action:** Assign to CMS editor for manual entry following this deployment report

---

## APPENDIX A: Quick Reference URLs

| Resource | URL |
|----------|-----|
| **Target Page** | https://wayground.com/learn/assessments/formative-assessment-strategies |
| **Parent Hub** | https://wayground.com/learn/assessments/ |
| **Sitemap** | https://wayground.com/sitemap.xml |
| **robots.txt** | https://wayground.com/robots.txt |
| **Google Search Console** | https://search.google.com/search-console |
| **Rich Results Test** | https://search.google.com/test/rich-results |
| **Schema Validator** | https://validator.schema.org/ |
| **PageSpeed Insights** | https://pagespeed.web.dev/ |
| **Mobile-Friendly Test** | https://search.google.com/test/mobile-friendly |

---

## APPENDIX B: Contact Information for Issues

| Issue Type | Contact |
|-----------|---------|
| CMS/Webflow access | Dev team / Webflow admin |
| Schema validation errors | SEO team / Technical lead |
| robots.txt updates | Dev team / Infrastructure |
| Content questions | Education Content Lead / Content team |
| Author information | HR / Content team |
| Performance optimization | Dev team / Performance engineer |
| Search Console access | SEO team / Marketing |

---

**Report Prepared By:** F4 Publisher Agent  
**Date:** 2026-03-18  
**Status:** COMPLETE - Ready for manual deployment  
**Approval Required:** Content lead sign-off before publish  

**Questions?** Refer to upstream agent outputs:
- C5 for complete article text
- F1 for detailed schema specifications
- F2 for full HTML/design specifications
- F3 for comprehensive internal linking strategy

---
Now execute your task. Put your final output inside `<output>` tags.
