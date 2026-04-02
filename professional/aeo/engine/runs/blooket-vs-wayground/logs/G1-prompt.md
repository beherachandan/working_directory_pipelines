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

**Topic:** Blooket vs Wayground comparison for classroom learning

### Upstream Agent Outputs

#### F4 Output

# F4 Deployment Report: Blooket vs Wayground Comparison

**Article URL:** `/learn/edtech-tools/blooket-vs-wayground`  
**Deployment Status:** READY FOR MANUAL CMS ENTRY  
**Deployment Mode:** Phase 1 (No MCP — Manual Publishing)  
**Date Prepared:** March 20, 2026

---

## Executive Summary

All article components are prepared and validated for manual CMS deployment. This report provides complete specifications for:
- CMS item creation in Webflow
- Schema markup embedding
- Technical SEO configuration
- Performance requirements
- AI bot access verification
- Post-publication monitoring

**Critical blockers before go-live:**
- 6 teacher quotes must be sourced and inserted (marked as [PUBLICATION BLOCKER] in C5 output)
- Author name, credentials, and bio must be assigned
- Product feature verification flags ([VERIFY]) should be resolved
- Author photo must be uploaded

---

## 1. CMS Deployment Specification

### Webflow CMS Collection: Articles
**Template:** Learn Hub Article

### Required CMS Fields & Values

| Field Name | Value | Notes |
|------------|-------|-------|
| **article-slug** | `blooket-vs-wayground` | URL path component |
| **full-url** | `/learn/edtech-tools/blooket-vs-wayground` | Complete path |
| **article-title** | Blooket vs Wayground: Which Is Better for Your Classroom? (2026 Comparison) | H1 text |
| **meta-title** | Blooket vs Wayground: Which Is Best? (2026 Guide) | 52 characters |
| **meta-description** | Compare Blooket vs Wayground (formerly Quizizz) for your classroom. Features, pricing, pros/cons, and grade-level recommendations. | 139 characters |
| **date-published** | 2026-03-20 | ISO format |
| **date-modified** | 2026-03-20 | ISO format |
| **category** | EdTech Tools | Taxonomy |
| **parent-hub** | `/learn/edtech-tools/` | Hub structure |
| **read-time** | 12 min read | Estimated |
| **author-name** | [ASSIGN BEFORE PUBLICATION] | Real educator with credentials |
| **author-credentials** | [ASSIGN BEFORE PUBLICATION] | e.g., "M.Ed., 10 years K-12" |
| **author-bio** | [ASSIGN BEFORE PUBLICATION] | 2-3 sentences |
| **author-photo-url** | [UPLOAD TO WEBFLOW ASSETS] | 200×200px WebP format |
| **author-linkedin** | [OPTIONAL] | Social proof |
| **author-twitter** | [OPTIONAL] | Social proof |
| **featured-image** | [UPLOAD COMPARISON VISUAL] | 1200×630px for social sharing |
| **word-count** | ~3,400 | For analytics |

### Article Body HTML
**Source:** Extract from F2 output, section `<article class="article-body">`

**Instructions:**
1. Copy full article body HTML from F2 output (lines after `<!-- Article Body -->`)
2. Replace all `[PUBLICATION BLOCKER]` teacher quote placeholders with real sourced quotes before publication
3. Replace `[Author Name]` and credential placeholders throughout
4. Verify all internal links resolve correctly:
   - `/learn/edtech-tools/` ✓
   - `/activities/math` ✓
   - `/learn/gamification/game-based-learning` ✓
   - `/activities/science` ✓
   - `/learn/assessments/formative` ✓
   - `/features/quizzes` ✓
   - `/features/lessons` ✓
5. Ensure external links have `rel="external nofollow"` for Blooket URLs

### Internal Links Verified (from F3 output - assumed complete)
**Total internal links:** 7 (target: 6-8) ✓

1. `/learn/edtech-tools/` — Early contextual link
2. `/activities/math` — After "What Is Wayground" section
3. `/learn/gamification/game-based-learning` — Engagement section
4. `/activities/science` — Content library section
5. `/learn/assessments/formative` — Assessment & reporting section
6. `/features/quizzes` — Assessment section
7. `/features/lessons` — Switching/using both section

**Status:** PASS (count within target range)

---

## 2. Schema Markup Embedding

### Location: Page `<head>` Section

Embed the following three JSON-LD blocks as separate `<script type="application/ld+json">` tags in the page head:

#### Block 1: Article Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Blooket vs Wayground: Which Is Better for Your Classroom? (2026 Comparison)",
  "description": "Compare Blooket vs Wayground (formerly Quizizz) for your classroom. Features, pricing, pros/cons, and grade-level recommendations.",
  "url": "https://wayground.com/learn/edtech-tools/blooket-vs-wayground",
  "datePublished": "2026-03-20T00:00:00Z",
  "dateModified": "2026-03-20T00:00:00Z",
  "author": {
    "@type": "Person",
    "name": "[INSERT AUTHOR NAME]",
    "description": "[INSERT AUTHOR CREDENTIALS]",
    "url": "https://wayground.com/authors/[author-slug]"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Wayground",
    "logo": {
      "@type": "ImageObject",
      "url": "https://wayground.com/images/wayground-logo.png",
      "width": "600",
      "height": "60"
    },
    "url": "https://wayground.com"
  },
  "image": {
    "@type": "ImageObject",
    "url": "https://wayground.com/images/blooket-vs-wayground-comparison.jpg",
    "width": "1200",
    "height": "630",
    "caption": "Blooket vs Wayground comparison for classroom learning"
  },
  "articleSection": "EdTech Tools",
  "keywords": ["Blooket", "Wayground", "Quizizz", "classroom technology", "educational games", "formative assessment", "K-12 edtech", "learning platforms"],
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://wayground.com/learn/edtech-tools/blooket-vs-wayground"
  }
}
```

**⚠️ REQUIRED BEFORE PUBLICATION:**
- Replace `[INSERT AUTHOR NAME]` with real author name
- Replace `[INSERT AUTHOR CREDENTIALS]` with credentials
- Replace `[author-slug]` with actual author page slug
- Upload and insert actual logo URL with correct dimensions
- Upload and insert featured image URL with correct dimensions

#### Block 2: FAQPage Schema

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Blooket or Wayground Better for Formative Assessment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wayground is the stronger choice for formative assessment. It provides 15+ question types, detailed question-level reporting, and standards alignment tracking that lets you pinpoint exactly where students need support. Research consistently shows that formative practices providing specific feedback on misconceptions—rather than just scores—lead to meaningful learning gains (Black & Wiliam, Assessment in Education: Principles, Policy & Practice, 5(1), 7-74, 1998). Blooket works for quick comprehension checks but lacks the analytics depth for data-driven instructional decisions."
      }
    },
    {
      "@type": "Question",
      "name": "Which Platform Is Easier to Learn and Set Up?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Blooket has a simpler interface and faster initial setup. You can create and launch your first game in under 10 minutes with no training required. Wayground has more features to explore, which means a slightly longer orientation period. However, the search function makes finding ready-made library content fast. Both platforms are user-friendly overall."
      }
    },
    {
      "@type": "Question",
      "name": "Can I Use Both Blooket and Wayground Together?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. Many teachers use Blooket for engagement-focused review games and Wayground for comprehensive assessment and content delivery. Both integrate with Google Classroom, so there's no technical conflict. Using each platform for its strengths gives you a more complete instructional toolkit than relying on either one alone."
      }
    },
    {
      "@type": "Question",
      "name": "Does Wayground Have the Same Game Modes as Blooket?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wayground offers game-based activity formats, but they're different from Blooket's themed modes. Blooket's 10+ specialized game modes (Tower Defense, Gold Quest, Racing) are more playful and competition-focused. Wayground's strength lies in combining game formats with quizzes, lessons, worksheets, and other activity types rather than specializing in game variety alone."
      }
    },
    {
      "@type": "Question",
      "name": "Which Platform Has Better Reporting and Analytics?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wayground provides significantly more detailed reporting. This includes question-level analytics, standards alignment tracking, performance trends over time, and data export in multiple formats. Blooket offers basic scoring and participation tracking. For teachers who use assessment data to make instructional decisions, Wayground's reporting capabilities are substantially more comprehensive."
      }
    },
    {
      "@type": "Question",
      "name": "Are Both Platforms FERPA and COPPA Compliant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both Blooket and Wayground are designed for K-12 educational use and state compliance with FERPA and COPPA in their privacy policies. However, compliance claims should be verified directly: check Blooket's privacy policy at blooket.com/privacy and Wayground's privacy policy page for current details. Educational data privacy requirements continue to evolve, and district procurement teams should conduct their own review before making institution-wide decisions."
      }
    },
    {
      "@type": "Question",
      "name": "Do Blooket and Wayground Have Mobile Apps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both platforms are accessible on mobile devices. Check the App Store and Google Play for current app availability and functionality for each platform, as mobile offerings are updated frequently. The mobile experience on both platforms supports students joining activities and completing work from tablets or phones."
      }
    }
  ]
}
```

**Status:** READY (all FAQ answers match article content exactly)

#### Block 3: Organization Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Wayground",
  "alternateName": "Quizizz",
  "url": "https://wayground.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://wayground.com/images/wayground-logo.png",
    "width": "600",
    "height": "60"
  },
  "description": "Wayground (formerly Quizizz) is a comprehensive learning platform with 200M+ educational resources including quizzes, lessons, worksheets, and flashcards for K-12 educators.",
  "sameAs": [
    "https://twitter.com/wayground",
    "https://facebook.com/wayground",
    "https://linkedin.com/company/wayground",
    "https://youtube.com/@wayground"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "Customer Support",
    "url": "https://wayground.com/support"
  }
}
```

**⚠️ ACTION REQUIRED:**
- Verify social media URLs are correct and active
- Remove any `sameAs` entries that don't exist
- Verify support page URL

### Schema Validation
**Before publication, validate all three blocks at:**
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/

**Expected validation status:** All schemas should pass with 0 errors

---

## 3. Sitemap Inclusion

### Action Required: Add to XML Sitemap

**File:** `/sitemap.xml` or `/sitemap-learn.xml` (if hub-specific sitemaps exist)

**Entry to add:**

```xml
<url>
  <loc>https://wayground.com/learn/edtech-tools/blooket-vs-wayground</loc>
  <lastmod>2026-03-20</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

**Priority rationale:** 0.8 (high priority — comparison content in active hub)

### Sitemap Verification Steps
1. Add entry to sitemap XML file
2. Verify sitemap is accessible at `https://wayground.com/sitemap.xml`
3. Check sitemap doesn't exceed 50MB or 50,000 URLs (Google limit)
4. If exceeded, use sitemap index file pointing to hub-specific sitemaps
5. Validate XML syntax at https://www.xml-sitemaps.com/validate-xml-sitemap.html

**Status after addition:** MANUAL VERIFICATION REQUIRED

---

## 4. Search Console Submission

### Google Search Console Indexing Request

**Manual submission steps:**

1. Log into Google Search Console: https://search.google.com/search-console
2. Select property: `wayground.com`
3. Navigate to: **URL Inspection tool** (left sidebar)
4. Enter URL: `https://wayground.com/learn/edtech-tools/blooket-vs-wayground`
5. Click: **Request Indexing**
6. Monitor: **Coverage report** for indexing status (typically 1-7 days)

**Expected outcome:**
- Initial crawl: Within 24-48 hours
- Indexed status: Within 3-7 days
- Rich results eligible: Within 7-14 days (after schema validation)

### Monitoring Dashboard
After submission, track in GSC:
- **Coverage:** Should show "Valid" status
- **Enhancements → FAQ:** Should detect 7 FAQ items
- **Performance:** Track impressions/clicks after indexing

**Status:** READY FOR MANUAL SUBMISSION (post-publication)

---

## 5. AI Bot Access Verification

### robots.txt Check

**File location:** `https://wayground.com/robots.txt`

**Required bot allowances for AI citation eligibility:**

```
# AI Bot Access - Required for AEO
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Applebot
Allow: /

User-agent: Googlebot
Allow: /
```

**⚠️ CRITICAL CHECK:**
- Verify NO disallow rules block `/learn/` paths for these bots
- Verify NO global `Disallow: /` for AI bots
- Check for any conflicting rules that would block this specific URL

### Bot Access Validation

**Status check (current):**

| Bot | Purpose | Required Status | Verification Method |
|-----|---------|-----------------|---------------------|
| GPTBot | ChatGPT citations | ✓ ALLOWED | Check robots.txt |
| PerplexityBot | Perplexity AI | ✓ ALLOWED | Check robots.txt |
| ClaudeBot | Claude AI | ✓ ALLOWED | Check robots.txt |
| Google-Extended | Google AI (Bard/Gemini) | ✓ ALLOWED | Check robots.txt |
| Bingbot | Copilot citations | ✓ ALLOWED | Check robots.txt |

**Action:** Manually verify at `https://wayground.com/robots.txt` before publication

**Status:** VERIFICATION REQUIRED (cannot auto-check without MCP)

---

## 6. Performance Verification

### Core Web Vitals Targets

| Metric | Target | Measurement Tool |
|--------|--------|------------------|
| **Largest Contentful Paint (LCP)** | <2.0 seconds | PageSpeed Insights |
| **First Contentful Paint (FCP)** | <1.2 seconds | PageSpeed Insights |
| **Time to Interactive (TTI)** | <2.5 seconds | Lighthouse |
| **Cumulative Layout Shift (CLS)** | <0.1 | PageSpeed Insights |
| **Total Page Weight** | <500KB (initial load) | Chrome DevTools Network tab |

### Performance Checklist

**Before going live:**

- [ ] **Images optimized:**
  - Author photo: 200×200px WebP format with JPEG fallback
  - Featured image: 1200×630px WebP format
  - All images use `loading="lazy"` except hero
  - Alt text on all images

- [ ] **Font loading optimized:**
  - Preload critical fonts with `<link rel="preload">`
  - Use `font-display: swap` to prevent FOIT (flash of invisible text)

- [ ] **JavaScript optimization:**
  - FAQ accordion uses vanilla JS (no jQuery)
  - Non-critical JS deferred with `defer` attribute
  - Total JS bundle <30KB gzipped

- [ ] **CSS optimization:**
  - Critical CSS inlined in `<head>`
  - Non-critical CSS loaded asynchronously
  - Unused CSS purged

- [ ] **Mobile optimization:**
  - Tables scroll horizontally on mobile
  - FAQ accordion has 60px min-height touch targets
  - Typography scales appropriately for mobile

- [ ] **Caching headers configured:**
  - HTML: `Cache-Control: public, max-age=3600`
  - CSS/JS: `Cache-Control: public, max-age=604800`
  - Images: `Cache-Control: public, max-age=31536000, immutable`

### Post-Publication Performance Testing

**Run within 24 hours of publication:**

1. **PageSpeed Insights:** https://pagespeed.web.dev/
   - Test both Mobile and Desktop
   - Target: 90+ score on both

2. **Lighthouse (Chrome DevTools):**
   - Performance: 90+
   - Accessibility: 95+
   - Best Practices: 95+
   - SEO: 100

3. **WebPageTest:** https://www.webpagetest.org/
   - Test from multiple locations
   - Verify <2s load time on 3G connection

**Status:** TESTING REQUIRED POST-PUBLICATION

---

## 7. Go-Live Checklist

### Pre-Publication (BLOCKING)

- [ ] **Content complete:**
  - [ ] All 6 teacher quotes sourced with real names, credentials, consent
  - [ ] Author name and credentials assigned
  - [ ] Author bio written (2-3 sentences)
  - [ ] Author photo uploaded (200×200px WebP)
  - [ ] All [VERIFY] flags on product features resolved
  - [ ] Pricing information verified at blooket.com and wayground.com

- [ ] **Technical setup:**
  - [ ] CMS item created in Webflow
  - [ ] All CMS fields populated (see Section 1)
  - [ ] Article body HTML inserted
  - [ ] All 7 internal links functional
  - [ ] External Blooket links have `rel="external nofollow"`

- [ ] **Schema markup:**
  - [ ] All three JSON-LD blocks embedded in page head
  - [ ] Author placeholders replaced with real data
  - [ ] Image URLs updated with actual assets
  - [ ] Validated with Google Rich Results Test (0 errors)
  - [ ] Validated with Schema.org validator (0 errors)

- [ ] **Images:**
  - [ ] Featured image uploaded (1200×630px)
  - [ ] Author photo uploaded (200×200px WebP)
  - [ ] All images have alt text
  - [ ] All images use `loading="lazy"` (except hero if present)

### Publication

- [ ] **Page published live at:** `https://wayground.com/learn/edtech-tools/blooket-vs-wayground`
- [ ] **Verify page loads:** No 404 errors, content displays correctly
- [ ] **Verify mobile rendering:** Test on iOS and Android devices

### Post-Publication (Within 24 Hours)

- [ ] **Sitemap:**
  - [ ] URL added to sitemap.xml
  - [ ] Sitemap accessible and valid XML
  - [ ] Sitemap resubmitted to Google Search Console

- [ ] **Search Console:**
  - [ ] URL submitted for indexing via URL Inspection tool
  - [ ] Monitoring enabled for coverage status

- [ ] **AI bot access:**
  - [ ] robots.txt verified to allow all required bots
  - [ ] No disallow rules block this URL

- [ ] **Performance:**
  - [ ] PageSpeed Insights run (mobile + desktop)
  - [ ] LCP <2 seconds confirmed
  - [ ] CLS <0.1 confirmed
  - [ ] Total page weight <500KB confirmed

- [ ] **Functionality:**
  - [ ] All 7 internal links click through correctly
  - [ ] FAQ accordion expands/collapses on click
  - [ ] Table of contents links scroll to sections
  - [ ] Mobile table scroll works correctly
  - [ ] CTA buttons link to correct destinations

- [ ] **Analytics:**
  - [ ] Page tracking confirmed in Google Analytics
  - [ ] Goal/conversion tracking configured (if applicable)

### Monitoring (First 7 Days)

- [ ] **Day 1:** Check GSC for crawl activity
- [ ] **Day 3:** Check for indexing status in GSC Coverage report
- [ ] **Day 7:** Check for rich results appearance (FAQ schema)
- [ ] **Day 7:** Review initial traffic in Analytics
- [ ] **Day 7:** Check for any crawl errors or mobile usability issues

**Status:** READY FOR PUBLICATION (pending content blockers)

---

## 8. Deployment Summary by Status

### ✅ READY (No Action Needed)
- Article content structure (from C5)
- Page design HTML/CSS specification (from F2)
- FAQPage schema (all 7 questions)
- Organization schema
- Internal linking strategy (7 links placed)
- Performance optimization guidelines
- Accessibility implementation
- Mobile responsiveness design

### ⚠️ READY PENDING MANUAL ACTION
- Sitemap entry (requires XML file edit)
- Google Search Console submission (requires manual URL inspection)
- robots.txt verification (requires file access check)
- Performance testing (requires post-publication tools)
- Author assignment (requires editorial decision)

### 🚫 BLOCKING PUBLICATION
- **6 teacher quotes** — Must source real educators with consent
- **Author name/credentials** — Must assign named author (not "Education Content Team")
- **Author photo** — Must upload 200×200px WebP image
- **Product feature verification** — [VERIFY] flags in C5 should be resolved
- **Schema placeholders** — Author name, logo URLs, featured image URLs must be real

---

## 9. Handoff to Downstream Agents

### For F5 (Distribution Agent)

**Article ready for distribution with:**
- Target URL: `https://wayground.com/learn/edtech-tools/blooket-vs-wayground`
- Primary keyword: "Blooket vs Wayground"
- Secondary keywords: "Blooket vs Quizizz", "Wayground comparison", "classroom game platforms"
- Target audience: K-12 teachers (elementary through high school)
- Content type: Comparison article (vs competitor)
- Internal promotion opportunities:
  - Cross-link from related comparison articles (Kahoot, Quizizz, Gimkit)
  - Feature in EdTech Tools hub newsletter
  - Share in teacher community channels
- External promotion:
  - Pinterest pins (comparison infographic)
  - Twitter thread (key takeaways)
  - LinkedIn article (teacher-focused)
  - Reddit r/Teachers (value-first discussion)

### For G1 (SOV Monitoring Agent)

**Track the following metrics:**

**SEO Performance:**
- Target keywords: "Blooket vs Wayground", "Blooket vs Quizizz", "Wayground vs Blooket"
- Google rank tracking: Check weekly for first 30 days, then monthly
- Impressions/clicks in GSC Performance report
- CTR optimization opportunities

**AI Citation Tracking:**
- ChatGPT: Monitor for citations when users ask "Blooket vs Wayground"
- Perplexity: Track SOV for comparison queries
- Google AI Overviews: Monitor for featured snippets from FAQ schema
- Claude/Copilot: Check for article mentions in education platform comparisons

**Engagement Metrics:**
- Time on page (target: >5 minutes for 12-min article)
- Scroll depth (target: >60% reach FAQ section)
- FAQ accordion interactions
- CTA click-through rate
- Bounce rate (target: <60%)

**Rich Results:**
- FAQ rich results appearance in SERPs (target: within 14 days)
- Article snippet features in Google Search

**Baseline expectations:**
- Indexing: 3-7 days
- First organic traffic: 7-14 days
- Rich results: 14-21 days
- Meaningful traffic: 30-60 days (competitive comparison query)

---

## 10. Risk Assessment & Mitigation

### High-Risk Items

**Risk: Teacher quotes are placeholders**
- **Impact:** Article cannot publish without real sourced quotes (trust dimension failure)
- **Mitigation:** Prioritize teacher outreach for quotes before any other publication steps
- **Owner:** Content/editorial team

**Risk: Product features marked [VERIFY] may be outdated**
- **Impact:** Inaccurate comparison data damages trust and credibility
- **Mitigation:** Manual verification at blooket.com and wayground.com before publication
- **Owner:** Research/fact-checking team

**Risk: Generic author attribution ("Education Content Team")**
- **Impact:** Zero E-E-A-T score from Google, reduced AI citation eligibility
- **Mitigation:** Assign named educator author with verifiable credentials
- **Owner:** Editorial team

### Medium-Risk Items

**Risk: Page load time exceeds 2 seconds**
- **Impact:** Copilot won't cite slow-loading pages; poor mobile UX
- **Mitigation:** Follow performance optimization checklist in Section 6; test post-publication
- **Owner:** Engineering/DevOps team

**Risk: Schema validation errors**
- **Impact:** No FAQ rich results; reduced SERP visibility
- **Mitigation:** Validate all JSON-LD before embedding; re-validate post-publication
- **Owner:** SEO/technical team

**Risk: AI bots blocked by robots.txt**
- **Impact:** Zero AI citation eligibility regardless of content quality
- **Mitigation:** Verify robots.txt allows all required bots (Section 5)
- **Owner:** SEO/DevOps team

---

## 11. Final Deployment Status

| Component | Status | Blocker Level | Owner |
|-----------|--------|---------------|-------|
| Article content (C5) | ✅ COMPLETE | — | — |
| Page design (F2) | ✅ COMPLETE | — | — |
| Schema markup (F1) | ⚠️ READY (needs placeholder replacement) | MEDIUM | SEO team |
| Internal links (F3) | ✅ COMPLETE (7 links) | — | — |
| CMS deployment | ⚠️ READY (manual entry required) | HIGH | Editorial/CMS team |
| Teacher quotes | 🚫 MISSING | **BLOCKING** | Content/outreach team |
| Author assignment | 🚫 MISSING | **BLOCKING** | Editorial team |
| Sitemap inclusion | ⚠️ READY (manual addition) | LOW | SEO team |
| GSC submission | ⚠️ READY (post-publication) | LOW | SEO team |
| AI bot access | ⚠️ NEEDS VERIFICATION | MEDIUM | DevOps/SEO team |
| Performance testing | ⚠️ POST-PUBLICATION | MEDIUM | Engineering team |

---

## 12. Recommended Next Steps

**Immediate (Before Publication):**
1. **Resolve blocking items:**
   - Source 6 teacher quotes with full attribution and consent
   - Assign named author with credentials and bio
   - Upload author photo (200×200px WebP)

2. **Verify product features:**
   - Check blooket.com for current game modes, pricing, features
   - Check wayground.com for current question types, integrations, pricing
   - Remove all [VERIFY] flags after confirmation

3. **Prepare assets:**
   - Create featured image (1200×630px) showing platform comparison
   - Ensure all image assets are WebP format with JPEG fallbacks
   - Write alt text for all images

**Pre-Launch (Day of Publication):**
1. Create CMS item in Webflow using Section 1 specifications
2. Embed all three JSON-LD schema blocks in page head
3. Replace all placeholders with real data
4. Validate schemas with Google Rich Results Test
5. Preview page in Webflow, test mobile rendering
6. Publish page live

**Post-Launch (Within 24 Hours):**
1. Add URL to sitemap.xml
2. Submit URL to Google Search Console for indexing
3. Verify robots.txt allows all AI bots
4. Run PageSpeed Insights (mobile + desktop)
5. Test all functionality (links, accordion, mobile tables)
6. Enable monitoring in GSC and Analytics

**First Week:**
1. Monitor GSC for crawl activity and indexing status
2. Check for rich results appearance (FAQ schema)
3. Review initial traffic and engagement metrics
4. Address any crawl errors or mobile usability issues
5. Hand off to F5 for distribution and G1 for SOV tracking

---

## Publication Decision: HOLD

**Recommendation:** Do NOT publish until all blocking items resolved.

**Blocking items:**
- 6 teacher quotes (marked [PUBLICATION BLOCKER] in C5)
- Named author with credentials
- Author photo

**Why hold:** Publishing with placeholder quotes or generic author attribution will result in:
- D1 trust score failure (would not pass 7/10 threshold)
- Zero E-E-A-T value from Google
- Reduced AI citation eligibility
- Potential credibility damage if discovered

**Estimated time to resolution:** 5-10 business days (dependent on teacher outreach response time)

---

## Contact for Deployment Questions

- **CMS/Webflow issues:** Engineering team
- **Content/quote sourcing:** Editorial/content team
- **Schema/SEO questions:** SEO team
- **Performance issues:** DevOps/engineering team
- **Author assignment:** Editorial leadership

---

**F4 Publisher Agent — Deployment Report Complete**
**Date:** March 20, 2026
**Status:** READY FOR MANUAL PUBLISHING (pending content blocker resolution)

---
Now execute your task. Put your final output inside `<output>` tags.
