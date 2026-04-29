# geo-query — KNOWLEDGE.md
_Platform-specific citation behavior and routing config. Updated by calibration runs._
_Last updated: 2026-04-27_

---

## Platform Status

| Platform | Status | Key | Notes |
|---|---|---|---|
| ChatGPT | ✅ Active | Portkey `VwFslTtBMP/j3m4i/HkmvyEv/mlR` → `@azure-openai-bbfaac` | Must append "Search the web and cite your sources." to trigger web search |
| Gemini | ✅ Active (quota-limited) | `AIzaSyCuBfskGih3UchLQ4LrrX1622sRqbfVpQk` | Direct AI Studio API only — Portkey strips groundingMetadata |
| Perplexity | ⏸ Parked | Needs $5 credit at perplexity.ai/settings/api | Model: `@perplexity-ai/sonar-pro` |

---

## Calibration Results Summary

| Topic | Platform | Gold URLs | Top cited |
|---|---|---|---|
| Formative assessment | ChatGPT | 1 | Black & Wiliam PDF (67%) |
| Retrieval practice | ChatGPT | 2 | learningscientists.org, Dunlosky PDF (50% each) |
| Exit tickets | ChatGPT | 6 | Edutopia (83%), ThirdSpace (75%) |
| Growth mindset | ChatGPT | 1 | Stanford CTL (50%) |
| Differentiated instruction | ChatGPT | 2 | ASCD Tomlinson PDF (83%), Edutopia DI hub (58%) |

**Pattern:** Academic PDFs and .edu domains cited most consistently. Practitioner brand pages (Edutopia) cited on brand authority. Stats-rich pages cited more than stats-poor pages regardless of structure.

---

## Known Technical Issues

- **Azure content filter** blocks "in education explained" variation — use "teaching X to students" instead
- **Cloudflare blocks** Python urllib without proper User-Agent — set `Mozilla/5.0 (compatible; WaymarkBot/1.0)`
- **Gemini free tier** ~15 RPM — wait 10+ min between burst sessions
- **ChatGPT Responses API** timeout ~90s — use `timeout=90` in http_post
- **Gold threshold auto-scaling** — with 12 runs (4 vars × 3), threshold scales to ~43% from 70%

---

## SEMrush SERP Step
- Key: `0b65acb5365171a4803c87e0de927328`
- API: `https://api.semrush.com/?type=url_organic&key=...`
- SERP classification: rank 1–10 = HIGH, 11–20 = LOW, not ranked = NOT_RANKED
- Note: PDFs and topic hubs often show NOT_RANKED even when frequently cited — expected behaviour
