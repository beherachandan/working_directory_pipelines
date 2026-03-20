Looking at the task payload, I need to classify the intent for "Blooket vs Wayground comparison for classroom learning" based on the A1 priority question and A2 citation data.

Let me analyze the query patterns and user needs:

<output>

# B1 Intent Classification Output

## Topic
**Blooket vs Wayground comparison for classroom learning**

## Primary Intent Classification

### Intent Type
**Comparison** (with strong Transactional secondary intent)

### Signal Analysis
| Signal Category | Evidence from Query & Variants |
|----------------|-------------------------------|
| Comparison signals | "vs", "comparison", "difference between", "or" (in "Blooket or Wayground") |
| Transactional signals | "which is better", "should I use", "for my classroom" (adoption decision context) |
| Informational signals | "what's the difference" (knowledge-seeking) |

### Intent Confidence
**HIGH** — Explicit comparison language in primary query and all 10 variant phrasings. Clear evaluation/decision-making context.

---

## Required Content Format Elements

### Core Comparison Structure
Based on comparison intent, content MUST include:

1. **Side-by-side comparison table**
   - Minimum 15-20 feature criteria rows
   - Two platform columns (Blooket | Wayground)
   - Visual indicators (✓ / ✗ / ⚠️) for scannability
   - Include: features, pricing, integrations, question types, game modes, reporting

2. **Pros/Cons lists**
   - Separate sections for each platform
   - Balanced perspective (not one-sided)
   - Specific, not generic bullets
   - Format: "Blooket Pros" | "Blooket Cons" | "Wayground Pros" | "Wayground Cons"

3. **"Best For" / Use Case Recommendations**
   - When to choose Blooket vs. when to choose Wayground
   - Segmented by: grade level, subject, class size, purpose (engagement vs. assessment)
   - Example format: "Choose Blooket for: [specific scenarios]"

4. **Bottom-line verdict section**
   - Direct answer to "which is better?"
   - Nuanced (both have strengths for different needs)
   - Action-oriented conclusion

### Transactional Support Elements
Due to secondary transactional intent, also include:

5. **Pricing breakdown table**
   - Free tier vs. paid tier for both platforms
   - Clear cost comparison
   - District/school pricing notes

6. **Clear CTAs (Calls-to-Action)**
   - Placement: After verdict section
   - Low-pressure (e.g., "Try Wayground free" or "Explore 200M+ resources")
   - Trust signals near CTA (user counts, teacher testimonials)

7. **Migration/switching guidance**
   - Practical "How to switch from Blooket to Wayground" section
   - OR "How to use both platforms together"
   - Addresses adoption friction

### AI Citation Optimization Structure
Based on A2 analysis of what wins citations:

8. **Question-phrased H2 headings**
   - Examples: "What's the Main Difference Between Blooket and Wayground?"
   - "Which Platform Has Better Assessment Features?"
   - "Is Blooket or Wayground Better for Elementary Students?"

9. **Key answer passages (40-60 words)**
   - Immediately following each question heading
   - Front-load the direct answer
   - Concise, extractable format

10. **FAQ section**
    - 5-7 common questions
    - Short, direct answers (40-60 words each)
    - Schema markup ready (FAQPage)

11. **Teacher testimonial quotes**
    - 3-5 quotes with credentials
    - Must include teachers who use BOTH platforms (credibility)
    - Blockquote format for scannability

---

## Depth Level Recommendation

### Classification: **COMPREHENSIVE** (2500-4000 words)

### Rationale

**Why not Overview (800-1200 words)?**
- Topic requires detailed comparison across 18+ EAR attributes identified by A1
- Teachers are making high-stakes adoption decisions, need thorough information
- Competitive analysis shows no comprehensive source exists (opportunity gap)

**Why not Detailed (1500-2500 words)?**
- Multiple dimensions require coverage: features, pricing, use cases, grade levels, subjects, integrations, assessment depth, time investment
- A2 identified 15 critical gaps in current content that need addressing
- Transactional intent demands thorough information to support decision-making

**Why Comprehensive?**
- ✓ This is a pillar comparison content piece (can spawn related comparisons: Kahoot vs WG, Gimkit vs WG)
- ✓ A2 analysis shows competitors have fragmented coverage; comprehensive = citation advantage
- ✓ 18 EAR attributes to cover (per A1 analysis)
- ✓ Multiple user segments to address (elementary, middle, high school teachers across subjects)
- ✓ High AEO Opportunity Score (630/1000) justifies investment in comprehensive coverage
- ✓ A2 citation analysis shows comprehensive, structured sources win (Common Sense Education, EdSurge)

---

## Format Requirements by Section

| Content Section | Required Format | Min Length | Must-Have Elements |
|----------------|-----------------|------------|-------------------|
| Introduction | Direct answer paragraph | 100 words | Answer main question upfront |
| Quick Comparison Table | Side-by-side table | 15-20 rows | Features, pricing, use cases |
| Platform Overviews | Definition paragraphs | 100 words each | Fair, balanced descriptions |
| Detailed Feature Comparison | Sub-sectioned analysis | 600-900 words | Game modes, assessment, library, integrations, ease of use |
| Pros/Cons | Bullet lists | 5-7 items per list | Specific, honest, balanced |
| Use Case Recommendations | Segmented bullet lists | 300-400 words | Grade level + purpose scenarios |
| Grade Level Guidance | 3 sub-sections | 100 words each | Elementary, Middle, High School |
| Teacher Testimonials | Blockquotes | 3-5 quotes | Credentials + specific use cases |
| Pricing Breakdown | Comparison table + analysis | 200 words | Free vs paid for both platforms |
| Migration Guide | Practical steps | 200 words | Switching or dual-use guidance |
| FAQ | Q&A format | 5-7 questions | 40-60 word answers |
| Verdict | Conclusion paragraph | 150 words | Balanced but actionable recommendation |

---

## Confidence Assessment

### Confidence Level: **HIGH**

### Supporting Factors
1. ✅ Explicit comparison language in query ("vs", "comparison")
2. ✅ All 10 variant phrasings confirm comparison intent
3. ✅ A2 analysis shows users asking evaluative questions ("which is better?", "should I use?")
4. ✅ Clear decision-making context ("for my classroom")
5. ✅ No mixed signals or ambiguous phrasing

### No Red Flags
- Query is not multi-intent (e.g., not "how to use Blooket vs Wayground tutorial" which would mix comparison + how-to)
- Context is clear (classroom learning = educational use case)
- Target audience is clear (teachers)

### Human Review Required?
**NO** — Intent is unambiguous. Proceed to B2 (Decomposer) and B3 (Brief Generator) with confidence.

---

## Downstream Agent Guidance

### For B2 (Decomposer)
- Decompose into comparison dimensions: features, pricing, use cases, grade levels, subjects, integrations, assessment depth
- Prioritize EAR attributes identified by A1 (18 attributes, 15 marked "must-cover")
- Structure sub-tasks around comparison framework (not chronological or informational flow)

### For B3 (Brief Generator)
- Use comprehensive depth template
- Include all 11 required format elements listed above
- Emphasize structured elements (tables, lists, Q&A) for AI citation optimization
- Tone: balanced, teacher-to-teacher, acknowledge both platforms' strengths
- Word count target: 2500-4000 words
- Schema requirements: ComparisonTable, Product, FAQPage, Organization

### For C-Phase (Content Generators)
- C1-C3: Generate comparison sections with balanced perspective
- C4: Find real Blooket data (cite blooket.com), never fabricate stats
- C5: Source teacher quotes from Wayground network who have used BOTH platforms

### For D1 (AEO Evaluator)
- Citation-worthiness criteria: Check for side-by-side table, question headings, 40-60-word passages, teacher testimonials, balanced tone
- Trust signals: Verify no fabricated stats, Blooket official site cited, honest acknowledgment of both platforms

---

## Classification Metadata

| Field | Value |
|-------|-------|
| Classification date | 2026-03-18 |
| Classified by | B1 (Intent Classifier Agent) |
| Primary intent | Comparison |
| Secondary intent | Transactional |
| Intent confidence | High |
| Depth level | Comprehensive (2500-4000 words) |
| Estimated format complexity | High (11 required format elements) |
| Ready for B2? | ✅ Yes |

</output>
