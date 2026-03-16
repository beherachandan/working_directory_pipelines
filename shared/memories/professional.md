# Professional Context — Wayground

## Company
- **Wayground** (formerly Quizizz) — education platform
- 200M+ total resources; ~11–12M pass Base Layer (BL) filters
- Target market: US (primary)

## SEO — Programmatic Sitemap
- Sitemap went through multiple de-indexation cycles (down to ~1.4M indexed as of Jan 2024)
- **V1** (LIVE since Mar 3, 2026): Weekly BL add/remove via cron
- **V2** (mid-April 2026): Clustering pipeline with weighted scoring
  - Teacher hosts 0.3, Recency 0.1, SEO traffic 0.1, Clicks 0.1, Question types 0.1, Creator score 0.1, Registrations 0.1, Activations 0.05, Is cloned 0.05
- **V3** (future): Full hierarchy classification, breadcrumbs, recommendations
- Data tables: sitemap_base_table, sitemap_daily_updated, sitemap_quarterly_updated, sitemap_master_table, sitemap_xml_table
- 12 sitemaps across 5 categories (UGC long-form, programmatic hierarchy, blogs/articles, product, marketing hub)

## AEO — Content Strategy
- 8-stage pipeline: KW identification → Relevancy & winning potential → Content strategy → Content generation → AEO readiness check → Teacher/SME vetting → Page design → Production
- Goal: Build authority in AI-driven search (ChatGPT, Perplexity, Google AI Overviews)

## Key Decisions
- Workspace at `~/Desktop/checking_claude/professional/`
- Source docs stored in `seo/reference/` (not at root)
- Separate folders per sitemap category under `seo/sitemaps/`
