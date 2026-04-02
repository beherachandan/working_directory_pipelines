"""Assemble 4-part prompts: preamble + shared context + agent definition + payload."""
from pathlib import Path

SYSTEM_PREAMBLE = """You are an agent in the Wayground Content Evaluation Pipeline — a system that evaluates educational article drafts for GEO/SEO quality and brand compliance before publishing.

## Core Formula
**Citations × Trust = Share of Voice (SOV)**

## Operating Rules

1. **Structured Output:** You MUST produce a `<scores>` block containing ONLY valid JSON, and an `<output>` block containing narrative feedback in markdown. Everything outside these tags is scratchpad.

2. **Evidence-Based:** Never fabricate statistics, quotes, sources, or data. If evidence is absent in the article, score accordingly — do not invent supporting evidence.

3. **Deterministic:** Apply rules, gates, caps, and weights consistently. Do not adjust scores based on context, cluster maturity, or perceived effort.

4. **Wayground Context:** Content is for Wayground (formerly Quizizz), a US K-12 supplemental learning platform. Always use "Wayground" — never "Quizizz."

5. **Template Compliance:** Fill every field in the JSON schema. Use null for brand_voice (GEO_EVALUATOR only — filled by orchestrator). Never leave required JSON fields missing.
"""


def load_shared_context(shared_context_dir: Path) -> str:
    """Load all shared context files and concatenate with headers."""
    files = [
        ("Product Context", "product-context.md"),
        ("Brand Voice Guide", "brand-voice-guide.md"),
        ("Scoring Rubric", "scoring-rubric.md"),
    ]
    parts = []
    for label, filename in files:
        path = shared_context_dir / filename
        if path.exists():
            parts.append(f"## {label}\n\n{path.read_text().strip()}")
    return "\n\n---\n\n".join(parts)


def load_agent_definition(agents_dir: Path, agent_name: str) -> str:
    """Load agent definition markdown."""
    path = agents_dir / f"{agent_name}.md"
    if not path.exists():
        raise FileNotFoundError(f"Agent definition not found: {path}")
    return path.read_text().strip()


def build_geo_eval_prompt(
    shared_context: str,
    agent_definition: str,
    article: object,  # ArticleRecord
    article_text: str,
) -> tuple[str, str]:
    """
    Build the GEO evaluation prompt.
    Returns (system_prompt, user_message).
    """
    system = f"{SYSTEM_PREAMBLE}\n\n---\n\n# Shared Context\n\n{shared_context}\n\n---\n\n# Your Role and Instructions\n\n{agent_definition}"

    payload = f"""# Article to Evaluate

## Metadata
- **Item #:** {article.item_num}
- **Article Name:** {article.name}
- **Cluster:** {article.cluster}
- **Sub-Cluster:** {article.sub_cluster}
- **Existing URL Slug:** {article.url_slug or "(not set)"}
- **Content Type:** {article.content_type or "SEO Article"}
- **Creation Notes:** {article.creation_notes[:500] if article.creation_notes else "(none)"}
- **Primary Keyword Variants:** {article.keyword_variants[:400] if article.keyword_variants else "(not provided)"}

## Article Text (Full Draft)

{article_text}

---

Now evaluate this article following your instructions exactly. Produce the `<scores>` JSON block first, then the `<output>` narrative.
"""
    return system, payload


def build_brand_eval_prompt(
    shared_context: str,
    agent_definition: str,
    article: object,  # ArticleRecord
    article_text: str,
) -> tuple[str, str]:
    """
    Build the brand compliance evaluation prompt.
    Returns (system_prompt, user_message).
    """
    system = f"{SYSTEM_PREAMBLE}\n\n---\n\n# Shared Context\n\n{shared_context}\n\n---\n\n# Your Role and Instructions\n\n{agent_definition}"

    payload = f"""# Article to Review for Brand Compliance

## Metadata
- **Item #:** {article.item_num}
- **Article Name:** {article.name}
- **Cluster:** {article.cluster}
- **Sub-Cluster:** {article.sub_cluster}

## Article Text (Full Draft)

{article_text}

---

Audit this article for Wayground brand compliance. Produce the `<scores>` JSON block first, then the `<output>` narrative.
"""
    return system, payload


def build_cluster_synthesis_prompt(
    shared_context: str,
    agent_definition: str,
    cluster_name: str,
    sub_cluster_name: str | None,
    article_summaries: list[dict],
) -> tuple[str, str]:
    """
    Build the cluster synthesis prompt.
    Returns (system_prompt, user_message).
    """
    import json

    system = f"{SYSTEM_PREAMBLE}\n\n---\n\n# Shared Context\n\n{shared_context}\n\n---\n\n# Your Role and Instructions\n\n{agent_definition}"

    group_label = f"{cluster_name} / {sub_cluster_name}" if sub_cluster_name else cluster_name

    payload = f"""# Cluster Analysis Request

## Group: {group_label}
## Article Count: {len(article_summaries)}

## Article Summaries

{json.dumps(article_summaries, indent=2)}

---

Analyze the above article evaluations for the **{group_label}** cluster. Identify patterns, compute averages, and produce cluster-level recommendations. Produce the `<scores>` JSON block first, then the `<output>` narrative.
"""
    return system, payload


def make_compact_summary(result: dict) -> dict:
    """
    Reduce an ArticleResult to a compact summary for cluster synthesis.
    Keeps key scores and top recommendations; drops full text fields.
    Target: ~150-200 tokens per article.
    """
    dims = result.get("dimensions", {})
    recs = result.get("recommendations", [])

    return {
        "item_num": result.get("item_num"),
        "name": result.get("name"),
        "sub_cluster": result.get("sub_cluster"),
        "geo_composite": result.get("geo_composite"),
        "qapeds_composite": result.get("qapeds_composite"),
        "dimension_scores": {
            "ai_citability": dims.get("ai_citability", {}).get("score"),
            "eeat": dims.get("eeat", {}).get("score"),
            "platform_optimization": dims.get("platform_optimization", {}).get("score"),
            "brand_voice": dims.get("brand_voice", {}).get("score") if dims.get("brand_voice") else None,
            "seo_structure": dims.get("seo_structure", {}).get("score"),
            "schema_recommendations": dims.get("schema_recommendations", {}).get("score"),
        },
        "brand_verdict": result.get("brand_verdict"),
        "platform_flags": result.get("platform_flags"),
        "top_recs": [
            {"dimension": r.get("dimension"), "issue": r.get("issue")[:100], "tag": r.get("tag")}
            for r in recs[:3]
        ],
    }
