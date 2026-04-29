---
name: KW-content-auditor
description: AEO content auditor for Wayground. Use when crawling and indexing all existing Wayground content to build a topic coverage map. Required prerequisite before running keyword discovery — accurately calculates gap factors so keyword-researcher avoids false positives and surfaces true content gaps. Triggers on phrases like "audit wayground content", "rebuild content index", "refresh content index", "run content audit".
model: claude-sonnet-4-6
temperature: 0.2
---

# KW — Content Auditor

See full agent spec in `AGENT.md` (same directory).

<!-- Thin wrapper so OpenClaw skill discovery can register this agent. All logic in AGENT.md. -->
