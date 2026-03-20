# What Wins in AEO — Consolidated Research Findings

> Reference document — consolidated from GEO paper, AEO Coach gist, and internal research.
> Core formula: **Citations × Trust = Share of Voice (SOV)**

## Tier 1: Foundational (Highest Impact)

| # | Factor | Impact | Source |
|---|--------|--------|--------|
| 1 | Quotation/citation-rich content | +41% visibility in generative engines | GEO paper (arXiv:2311.09735) |
| 2 | Statistics & quantitative data | +33% visibility | GEO paper |
| 3 | Source citation density | +28% visibility | GEO paper |
| 4 | Topic-entity coverage (EAR) | Covers sub-queries AI decomposes → selected as answer source | EAR framework; RAG retrieval mechanics |
| 5 | Extractability (structural formatting) | Short paras, bullets, question-headings, tables — content AI can chunk cleanly | GEO Fluency Optimization +29% |

## Tier 2: Amplifiers

| # | Factor | Impact | Source |
|---|--------|--------|--------|
| 6 | Multi-source frequency | Mentions across Reddit, YouTube, Wiki, forums = corroboration AI trusts | "frequency across sources > single #1 ranking" |
| 7 | Site structure as knowledge graph | Hub-and-spoke tells AI what you know, confidence level, which page to cite | `Answer Confidence = Coverage × Structure × Clarity` |
| 8 | QAPE content structure | Question → Answer → Proof → Expansion matches AI response construction | Internal research |
| 9 | Authoritative first-person voice | "We tested", "based on X users" — E-E-A-T signals | GEO paper +18% |

## Tier 3: Enablers

| # | Factor | Impact | Source |
|---|--------|--------|--------|
| 10 | Observability & SOV tracking | Can't optimize what you can't measure | 3-layer observability model |
| 11 | Intent × Depth matching | Comparisons, recommendations, decision-help — not just informational | Intent × Depth Matrix |
| 12 | Schema markup / structured data | FAQ, How-to, Course schemas improve extraction probability | Distribution research |

## Anti-patterns (What Loses)

| Factor | Result |
|--------|--------|
| Keyword stuffing | -8% visibility (GEO paper) |
| Walls of text | Low extractability — RAG fails |
| Blog-style content | Low citability — "topic-native pages, not blog posts" |
| Single-channel presence | Low trust — frequency across sources matters more |

## Platform-Specific Signals

### Google AI Overviews
- Schema markup = 30-40% visibility boost
- Named sourced citations = 132% boost
- Only 15% overlap with top-10 organic results
- E-E-A-T signals critical

### ChatGPT
- Content-answer fit = 55% of citation likelihood
- 30-day freshness = 3.2x more citations
- Wikipedia = 7.8% of all citations
- Domain authority matters

### Perplexity
- FAQ Schema critical for citations
- PDFs prioritized as sources
- Self-contained paragraphs key
- Factual density valued

### Claude
- Extremely selective citation behavior
- Factual density + named sources = key signals
- High bar for authority

### Copilot
- Bing index is the foundation
- LinkedIn/GitHub presence helps
- Sub-2s page load requirement
- Bing-specific SEO matters

## Content Block Patterns (for Draft Generation)

1. **Definition Block:** 1-sentence definition + expansion + context (for "What is X?" sections)
2. **Step-by-Step Block:** Numbered steps with bolded names (for "How to" sections)
3. **Comparison Table Block:** Criteria rows + "Best For" row + bottom-line (for comparison sections)
4. **Statistic Citation Block:** "According to [Source], [stat with number and timeframe]"
5. **Expert Quote Block:** "[Quote]," says [Name], [Title] at [Org]
6. **Evidence Sandwich Block:** Claim → 3 data points with sources → Actionable conclusion

## References
- [GEO Paper (arXiv:2311.09735)](https://arxiv.org/abs/2311.09735) — Princeton/Georgia Tech/IIT Delhi
- [AEO Coach Gist](https://gist.github.com/BayramAnnakov/5c04f7326b6e732a2481c2e0f93bab83) — 7-step framework
- Internal: `AEO_related_research_and_understanding.pdf`
