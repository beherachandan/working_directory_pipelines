# SEO — Programmatic Sitemap Management

## Overview
Managing Wayground's sitemap ecosystem to maximize indexation of high-quality resources. Out of 200M+ total resources, ~11–12M pass Base Layer (BL) filters. The sitemap has gone through multiple de-indexation cycles (down to ~1.4M indexed as of Jan 2024).

---

## Sitemap Inventory

| Sitemap | Pages | Category | Notes |
|---------|------:|----------|-------|
| `contents/index.xml` | 19,200,000 | UGC Long-form | Main content index |
| `contents/science_index.xml` | 1,050,000 | UGC Long-form | Science-specific |
| `worksheets-new/index.xml` | 333,000 | Programmatic Hierarchy | Worksheet pages |
| `library_pages/index.xml` | 244,000 | Programmatic Hierarchy | Library pages |
| `worksheet-locales.xml` | 92,700 | Programmatic Hierarchy | Locale variants |
| `resource_library/index.xml` | 62,300 | Programmatic Hierarchy | Resource library |
| `video_library_sitemap.xml` | 1,832 | Programmatic Hierarchy | Video content |
| `standards.xml` | 1,686 | Programmatic Hierarchy | Standards pages |
| `roleplay_sitemap.xml` | 72 | Blogs & Articles | Roleplay content |
| `owned_content/learn_pages.xml` | 48 | Blogs & Articles | Owned learn pages |
| `marketing-sitemap.xml` | 25 | Marketing Hub | Marketing pages |
| `ai_generators.xml` | 9 | Product | AI generator tools |

### Categories
- **UGC Long-form** — User-generated quizzes/content (~20.25M pages)
- **Programmatic Hierarchy** — Structured worksheet, library, and standards pages (~735K pages)
- **Blogs & Articles** — Owned editorial content (~120 pages)
- **Product** — Tool/feature pages (9 pages)
- **Marketing Hub** — Marketing landing pages (25 pages)

---

## Version Roadmap

### V1 — Weekly BL Add/Remove (LIVE as of Mar 3, 2026)
- Weekly cron: add resources that newly pass BL → sitemap; remove resources that no longer pass
- Maintains master table for tracking
- Simple binary: in sitemap or not

### V2 — Clustering Pipeline (Target: mid-April 2026)
- Groups resources into clusters for smarter sitemap inclusion
- **Scoring weights:**
  | Signal | Weight |
  |--------|-------:|
  | Teacher hosts | 0.30 |
  | Recency | 0.10 |
  | SEO traffic | 0.10 |
  | Clicks | 0.10 |
  | Question types | 0.10 |
  | Creator score | 0.10 |
  | Registrations | 0.10 |
  | Activations | 0.05 |
  | Is cloned | 0.05 |

### V3 — Full Hierarchy & Classification (Future)
- Full hierarchy classification engine
- Breadcrumb generation
- Recommendation system
- Consolidation of sitemap structure

---

## Base Layer (BL) Filters
Resources must pass these filters to be eligible for sitemap inclusion:
- Minimum quality thresholds (content completeness, question count, etc.)
- ~11–12M resources pass BL out of 200M+ total

---

## Data Tables

| Table | Purpose |
|-------|---------|
| `sitemap_base_table` | Core resource data with BL pass/fail |
| `sitemap_daily_updated` | Daily refresh of key signals |
| `sitemap_quarterly_updated` | Quarterly refresh of slower-moving signals |
| `sitemap_master_table` | Current sitemap membership tracking |
| `sitemap_xml_table` | Generated XML sitemap data |

---

## Reference Docs
Source documents are in [`reference/`](./reference/):
- `programmatic_sitemap.docx` — V1/V2 logic and implementation
- `sitemap_consolidation.docx` — V3 consolidation vision
- `sitemap_pipeline.xlsx` — Pipeline data flow
- `sitemap_screenshots/` — GSC screenshots
