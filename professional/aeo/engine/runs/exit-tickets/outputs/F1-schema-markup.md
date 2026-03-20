
# F1 Schema Markup Output: Exit Tickets Article

## Schema Types Generated
Based on the article content and brief requirements:
1. ✅ **Article** (always required)
2. ✅ **FAQPage** (6 FAQ items present)
3. ✅ **HowTo** (5-step tutorial structure)

---

## 1. Article Schema (JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Use Exit Tickets in the Classroom",
  "description": "Exit tickets are quick formative assessments given at the end of a lesson to check student understanding. Teachers create one to three focused questions, collect responses as students leave, review results to identify learning gaps, and adjust the next day's instruction based on what students know or still need to learn.",
  "author": {
    "@type": "Person",
    "name": "[Education Content Lead]",
    "url": "https://wayground.com/authors/[author-slug]"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Wayground",
    "url": "https://wayground.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://wayground.com/logo.png"
    }
  },
  "datePublished": "2026-03-18",
  "dateModified": "2026-03-18",
  "image": "https://wayground.com/images/exit-tickets-classroom.jpg",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://wayground.com/learn/assessment/exit-tickets"
  }
}
```

**Implementation Note:** Replace `[Education Content Lead]` and `[author-slug]` with actual author name and URL. Replace image URL with actual hero image path once selected.

---

## 2. FAQPage Schema (JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What's the difference between entrance tickets and exit tickets?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Entrance tickets assess prior knowledge at the start of class, while exit tickets measure learning at the end. Entrance tickets help you gauge what students already know so you can adjust your lesson plan. Exit tickets check whether students understood what you just taught. Both are formative assessments, but they serve different timing purposes within the lesson cycle."
      }
    },
    {
      "@type": "Question",
      "name": "Should exit tickets be graded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Exit tickets should not be graded for correctness. They are formative tools designed to reveal what students understand and where they're still confused. Grade them for completion only, or skip grading entirely. When students fear a bad score, they give safe answers instead of honest ones—which defeats the purpose of checking for understanding."
      }
    },
    {
      "@type": "Question",
      "name": "What are some exit ticket alternatives or variations?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Popular variations include the 3-2-1 prompt (three things learned, two questions, one connection), one-word summary, emoji confidence rating, muddiest point (what's still confusing?), and quick sketches or diagrams. Digital tools like Wayground offer poll-style exit tickets with instant response aggregation. Varying formats keeps students engaged and lets you assess different types of thinking."
      }
    },
    {
      "@type": "Question",
      "name": "How do you store and organize exit ticket data over time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For paper exit tickets, use labeled folders or bins sorted by class period and date. Digital platforms automatically save response data you can access anytime. Keep exit tickets for two to four weeks to track learning progressions and spot recurring misconceptions. You don't need to archive every exit ticket permanently—formative data is most useful in the short term."
      }
    },
    {
      "@type": "Question",
      "name": "Can exit tickets work for all grade levels?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Adjust the format and complexity to match the age group. Elementary students can use drawings, emojis, thumbs up/down, or one-word responses. Middle school students handle one to two short-answer questions well. High school students can tackle brief explanations, analysis prompts, or connections to prior learning. The principle stays the same across grades—check understanding before students leave."
      }
    },
    {
      "@type": "Question",
      "name": "What if students don't take exit tickets seriously?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Make exit tickets routine, keep them genuinely low-stakes, and show students their responses matter. When students see you actually change tomorrow's lesson based on what they wrote, engagement increases. Vary formats to prevent boredom, keep questions brief and focused, and occasionally share anonymous responses with the class to validate student input and demonstrate its impact."
      }
    }
  ]
}
```

**Implementation Note:** FAQPage schema is critical for Perplexity and Google AIO citations. All answer text exactly matches article FAQ section.

---

## 3. HowTo Schema (JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Use Exit Tickets in the Classroom",
  "description": "A step-by-step guide to creating, implementing, and using exit tickets to improve instruction through formative assessment.",
  "totalTime": "PT15M",
  "supply": [
    {
      "@type": "HowToSupply",
      "name": "Digital device or paper materials (index cards, sticky notes, or half-sheets)"
    },
    {
      "@type": "HowToSupply",
      "name": "Exit ticket questions aligned to lesson objectives"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Choose Your Exit Ticket Format",
      "text": "Select a format based on your learning objective and classroom setup. Common formats include multiple choice, open-ended short answer, rating scales, 3-2-1 prompts, or one-word summaries. Decide between digital tools (like Wayground quiz builder or Google Forms) for quick data aggregation in large classes, or paper materials (index cards, sticky notes) for low-tech classrooms. Digital formats provide instant results and auto-scoring, while paper requires no devices and offers tactile engagement.",
      "position": 1
    },
    {
      "@type": "HowToStep",
      "name": "Design Effective Exit Ticket Questions",
      "text": "Create one to three focused questions aligned to your lesson objective that students can answer in two to three minutes. Aim for DOK Level 2 questions that reveal understanding rather than simple recall. Keep the question count low—one question works well for elementary students, two to three is the maximum for secondary students. Use questions like 'Explain the steps you used to solve a two-step equation today' or 'What's one thing you're still confused about regarding photosynthesis?' Vary question types week to week to maintain engagement.",
      "position": 2
    },
    {
      "@type": "HowToStep",
      "name": "Implement Exit Tickets in Your Classroom",
      "text": "Administer exit tickets in the last five minutes of class by posting the question on your board or screen. For paper, place a basket by the door for collection. For digital, have students submit on their devices before packing up. Make it routine and low-stakes so students know exit tickets aren't graded for correctness. Differentiate by providing word banks or sentence frames for English Language Learners, offering extended time or verbal responses for students with IEPs, and creating tiered questions by readiness level.",
      "position": 3
    },
    {
      "@type": "HowToStep",
      "name": "Review Results Efficiently",
      "text": "Sort responses into three groups: Got it, Partial understanding, and Didn't get it. This takes about five minutes for a class set of 25 to 30 students. Look for patterns rather than grading individual responses. For large classes with 100-plus students, use a sampling strategy—read 10 to 15 responses per class period to identify recurring themes. Digital tools speed this up by auto-aggregating multiple-choice responses, showing you instantly whether students understood or where misconceptions exist.",
      "position": 4
    },
    {
      "@type": "HowToStep",
      "name": "Adjust Instruction Based on Exit Ticket Data",
      "text": "Use this decision framework: If 70% or more show mastery, move forward with new content and provide enrichment. If 40 to 70% show mastery, reteach the concept using a different approach and incorporate more practice. If below 40% show mastery, conduct a full reteach and check whether the issue was instruction or question clarity. Make these adjustments within 24 hours for maximum impact. Use formative data to form flexible groups—students who showed mastery work independently while you pull a small group for targeted reteaching.",
      "position": 5
    }
  ]
}
```

**Implementation Note:** The `totalTime` estimate (PT15M = 15 minutes) represents the time to create and review one exit ticket session, not the student completion time (2-3 minutes).

---

## Deployment Instructions

### Where to Embed
All three JSON-LD blocks should be embedded in the `<head>` section of the page at `/learn/assessment/exit-tickets`, each wrapped in separate `<script>` tags:

```html
<head>
  <!-- Other head elements -->
  
  <script type="application/ld+json">
  [Article Schema JSON-LD here]
  </script>
  
  <script type="application/ld+json">
  [FAQPage Schema JSON-LD here]
  </script>
  
  <script type="application/ld+json">
  [HowTo Schema JSON-LD here]
  </script>
</head>
```

### Pre-Deployment Checklist
- [ ] Replace `[Education Content Lead]` and `[author-slug]` with actual author information
- [ ] Replace placeholder image URL with actual hero image path
- [ ] Verify publisher logo URL is correct
- [ ] Validate all three JSON-LD blocks using [Google Rich Results Test](https://search.google.com/test/rich-results)
- [ ] Confirm schema content exactly matches visible page content (Google requirement)

### Validation
After deployment, validate using:
1. **Google Rich Results Test:** https://search.google.com/test/rich-results
2. **Schema Markup Validator:** https://validator.schema.org/

### Expected Rich Results
- **Article:** Enhanced snippets in Google Search with author, date, publisher
- **FAQPage:** Expandable FAQ accordions in Google Search results (30-40% visibility boost for AI engines)
- **HowTo:** Step-by-step rich results with estimated time in Google Search
