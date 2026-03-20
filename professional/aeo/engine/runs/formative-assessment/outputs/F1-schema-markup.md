
# Schema Markup for Formative Assessment Strategies Article

## Schema Type Recommendations

Based on the content structure, this article requires three schema types:

1. **Article Schema** — Required for all articles, provides core metadata
2. **FAQPage Schema** — 8 FAQ items in dedicated FAQ section
3. **HowTo Schema** — 5-step implementation framework in "How Do You Implement Formative Assessment in Your Classroom?" section

---

## JSON-LD Markup Blocks

### 1. Article Schema

```json
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
```

**Note:** Replace `[Education Content Lead]` with actual author name. Add actual hero image URL when available.

---

### 2. FAQPage Schema

```json
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
```

---

### 3. HowTo Schema

```json
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
```

---

## Deployment Instructions

### Where to embed schema markup:

All three JSON-LD blocks should be embedded in the `<head>` section of the page, each wrapped in its own `<script type="application/ld+json">` tag:

```html
<head>
  <!-- Other head elements -->
  
  <!-- Article Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    ...
  }
  </script>
  
  <!-- FAQPage Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    ...
  }
  </script>
  
  <!-- HowTo Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "HowTo",
    ...
  }
  </script>
  
</head>
```

### Validation steps:

1. **Google Rich Results Test:** Paste the full HTML (with embedded JSON-LD) into https://search.google.com/test/rich-results to validate all three schema types
2. **Schema Markup Validator:** Use https://validator.schema.org/ to check JSON-LD syntax and schema.org compliance
3. **Common errors to check:**
   - Ensure FAQ answers exactly match visible page content (Google requirement)
   - Verify all required fields are populated (headline, author, datePublished for Article; name, text for HowTo steps; name, acceptedAnswer for FAQ items)
   - Confirm no trailing commas in JSON
   - Verify URL fields use absolute URLs (https://)

### Content-matching requirement:

**Critical:** Schema content must exactly match the visible page content. This is a Google requirement for rich results eligibility. The FAQ answers and HowTo steps above are copied verbatim from the article. Do not modify schema content unless the corresponding page content is also updated.

---

## Impact Expectations

- **Article Schema:** Enables article rich results with author, date, and publisher information in SERPs
- **FAQPage Schema:** Critical for AI citation—Perplexity and Google AIO heavily favor pages with FAQ schema for question-based queries. Expected 30-40% visibility boost for long-tail formative assessment questions.
- **HowTo Schema:** Enables step-by-step rich results in Google Search, increasing click-through rate for implementation-focused queries ("how to implement formative assessment")

All three schema types work together to maximize AI citation probability across the 15 EAR attributes covered in this article.
