
# AEO Score Card: What Is Turn and Talk — and How Does It Increase Student Engagement?

> Stage 4 output — produced by D1 (AEO Evaluator)
> Source brief: content-brief-turn-and-talk.md (B3)

## Metadata
| Field | Value |
|-------|-------|
| Article | What Is Turn and Talk — and How Does It Increase Student Engagement? |
| Target URL | `/learn/engagement/turn-and-talk` |
| Evaluator run | #1 |
| Date | 2026-03-20 |
| Result | **PASS** |

---

## Dimension Scores

| # | Dimension | Score (0-10) | Pass (≥7)? | Notes |
|---|-----------|-------------|------------|-------|
| 1 | QAPE Structure | 9 | ✅ | Question in H1 ✓; direct answer in first standalone paragraph (58 words — at upper edge of 40-60 target but within brief spec) ✓; proof via 7 "According to [Source]" citations and 4+ peer-reviewed studies ✓; expansion across 11 sections ✓. Minor: the direct answer paragraph could trim one clause to fall closer to 50 words — non-blocking. |
| 2 | EAR Coverage | 9 | ✅ | Covered: 12/12 attributes. Attrs 5 (Duration Guide), 6 (sentence starters), 9 (digital implementation) confirmed at "Deep" per B3 target. Attrs 4, 7, 8, 11, 12 at "Addressed" depth — sufficient for PASS threshold. Auto-escalate condition (Attrs 5 + 9 absent/mentioned-only) not triggered. |
| 3 | Extractability | 8 | ✅ | All 9 H2s question-phrased ✓; 6 FAQ answers trimmed to 40-60 words in C5 pass ✓; 7 tables covering all structured data ✓; paragraphs ≤3 sentences throughout except research section (max 4, permitted by brief) ✓. Minor deduction: research section prose blocks (Vygotsky, Webb, Hattie paragraphs) run dense with citation-heavy compound sentences — extractable but AI chunking is easier in adjacent sections. Not a failure condition. |
| 4 | Trust & Authority | 7 | ✅ | Stats with named sources: 7 (Rowe 1986, Webb 1989/1991, Hattie 2012, Walqui 2006, Vygotsky 1978, Michaels/O'Connor/Resnick 2010, participation math calculation) ✓; "According to [Source]" framings: 7 ✓; Expert quotes: 1 verified pending wording (Wiliam) ⚠️, 1 placeholder (practitioner — 🚨 gate condition) ❌; First-person WG signals: 0 (correctly omitted — no UXR data confirmed) ⚠️; Author byline: placeholder ⚠️. Score reflects strong citation infrastructure against absent practitioner quote and unverified Wiliam wording. This is the ceiling at 7 until gate conditions resolve at E-phase. |
| 5 | Intent Match | 9 | ✅ | Primary intent: How-to. Format: Numbered steps (1-7) with bolded step names ✓, teacher action + timing at each step ✓, Duration Guide table ✓. Secondary intent: Informational. Format: Definition in first paragraph ✓, FAQ section (6 items) ✓. Schema: FAQPage + HowTo — specified in brief and implemented structurally ✓. Comparison intent (sub-query): 3-column table present ✓. All required format elements for both intent types present. |

**Composite Score:** 8.40 / 10
> Weights: QAPE 25% (2.25) + EAR 25% (2.25) + Extract 20% (1.60) + Trust 20% (1.40) + Intent 10% (0.90) = **8.40**

---

## Platform-Specific Checks

| Platform | Check | Status |
|----------|-------|--------|
| Google AIO | Schema markup present? | ✅ FAQPage + HowTo schema specified in brief; 7-step protocol and 6-item FAQ are structurally implemented |
| Google AIO | Named sourced citations? | ✅ 7 "According to [Source]" framings with full author/year/publication; no "studies show" generics |
| ChatGPT | Content-answer fit? | ✅ 58-word definition block answers H1 query directly and completely in first 200 words |
| ChatGPT | Freshness date present? | ✅ "Last updated: March 2026" in byline |
| Perplexity | Self-contained paragraphs? | ✅ Adaptation, mistake/fix, grade-band, FAQ, and lesson-placement sections all self-contained; research section slightly denser but acceptable |
| Perplexity | FAQ schema ready? | ✅ 6 FAQ items, all answers 40-60 words (verified trimmed in C5 pass) |

---

## B3 Special Gate Conditions — Verified

| Condition | Status |
|---|---|
| Attrs 5 (Duration Guide) AND 9 (digital) both present at "Deep" — auto-escalate NOT triggered | ✅ Both at Deep |
| Comparison table (Attr 2): structured table with ≥3 columns | ✅ 3 columns, 6 rows |
| Product mention audit: exactly 1 | ✅ Team Mode, digital section only |
| Definition block in first 200 words: standalone, 40-60 words | ✅ 58 words |
| Min EAR PASS: 9/12 attributes at Addressed depth or better | ✅ 12/12 |

---

## Revision Notes

N/A — All 5 dimensions score ≥ 7. Article **PASSES** D-gate.

**Open items carried forward to E-phase human gate (non-blocking for D1 but require resolution before publish):**

1. 🚨 **Practitioner quote (Expert Quote #2)** — currently a placeholder. B3 flags this as a publish gate condition. Trust score would increase to 8 once a named, attributed educator from Wayground's teacher vetting network is inserted. E1 must surface this for the reviewing educator.

2. ⚠️ **Dylan Wiliam quote** — verbatim verification required against *Embedded Formative Assessment* (2011/2018). C5 specifies a paraphrase fallback ("According to Wiliam" + paraphrase). Editorial team to confirm before final publish.

3. ⚠️ **Edutopia citation** — direction confirmed ("sentence starters and language scaffolds before partner talk"); specific article URL to be confirmed by editorial team before final publish. If URL cannot be located, remove the Edutopia citation and replace with an additional practitioner-voice sentence — do not publish with a bare domain reference.

4. ⚠️ **Author byline** — credential placeholder must be filled with an educator holding Ed.D. or equivalent classroom practitioner standing. This affects E-E-A-T signal for Google AIO.

**Minor suggestions for future improvement (non-blocking):**
- QAPE: Trim the definition block from 58 to 52-55 words for cleaner AI snippet extraction — cutting the phrase "across K-12 grade levels" from the last sentence achieves this without information loss.
- Trust: If UXR team can surface any Wayground platform participation data (even directional — "teachers using collaborative activities in Wayground report..."), inserting one first-person signal in the digital section would push Trust to 8 and composite to 8.60.
- Extractability: The Hattie paragraph in the research section runs to 4 dense sentences. Consider splitting at "Cooperative discussion approaches..." into a second short paragraph for cleaner AI chunking — non-blocking given the brief's 4-sentence permission in this section.

---

## Revision History

| Run | Date | Result | Composite | Notes |
|-----|------|--------|-----------|-------|
| #1 | 2026-03-20 | **PASS** | 8.40 | All 5 dimensions ≥7. 12/12 EAR attributes covered. 3 open items flagged for E-phase human gate — none block D1 PASS. |

---

<scores>{"qape": 9, "ear": 9, "extract": 8, "trust": 7, "intent": 9}</scores>
