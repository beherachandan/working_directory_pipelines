# OpenClaw Workspace Snapshot — 2026-04-29

Snapshot of the OpenClaw workspace (`~/.openclaw/workspace`) taken before restructuring the content generation pipeline.

## What's here

```
skills/          ← All OpenClaw agent skills as of 2026-04-29
  A1-query-intelligence/    ← RETIRING: replaced by topic-researcher
  B2-ear-decomposer/        ← RETIRING
  B3-content-brief-generator/ ← RETIRING
  C4-citation-enricher/     ← RETIRING
  C5-content-enhancer/      ← KEEPING (revision loop)
  D1-aeo-evaluator/         ← KEEPING
  D2-url-evaluator/         ← KEEPING
  D3-competitor-gap/        ← KEEPING
  E1-brand-reviewer/        ← KEEPING
  E2-icp-reviewer/          ← KEEPING
  F1-webflow-publisher/     ← KEEPING
  KW-content-auditor/       ← KEEPING
  KW-keyword-researcher/    ← KEEPING
  geo-query/                ← KEEPING
  marketing-director/       ← UPDATING
  slack-url-eval/           ← KEEPING
  trends-researcher/        ← KEEPING

aeo/             ← AEO context files, run outputs, article drafts
  context/       ← Scoring rubric v1.1, brand voice, product context
  runs/          ← All pipeline run artifacts (B3→C3→C4→D1→C5→E1→E2)

PROJECTS.md      ← Pipeline state at time of snapshot
MEMORY.md        ← Long-term agent memory at time of snapshot
IDENTITY.md      ← Agent role definition
CAPABILITIES.md  ← Capability map
TOOLS.md         ← Tool config notes
```

## Why this snapshot exists

The content generation pipeline (A1→B2→B3→C4) was not performing well enough.
Replacing with: **topic-researcher → content-strategist → content-writer → D1 → C5 → E1 → E2 → F1**

New skills will be wired in after this snapshot is committed.

## Pipeline state at snapshot

- 1 article READY_FOR_PUBLISH: `critical-thinking-exercises` (D1: 8.02/10, E2 PASS)
- Several articles mid-pipeline in `aeo/runs/`
- 22 keywords queued for content generation
- Calibration system live: rubric v1.1, 5 topics, 30-URL corpus
