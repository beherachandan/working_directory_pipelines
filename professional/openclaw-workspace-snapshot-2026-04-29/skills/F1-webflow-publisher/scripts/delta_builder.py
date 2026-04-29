"""Build improvement delta from enhanced_changes_log for each article."""
import re


# Map changes_log tags → GEO dimensions they improve
_REC_DIM_MAP = {
    "ai_citability": "ai_citability",
    "eeat": "eeat",
    "platform_optimization": "platform_optimization",
    "brand_voice": "brand_voice",
    "seo_structure": "seo_structure",
    "schema_recommendations": "schema_recommendations",
}

_BRAND_DIM = "brand_voice"
_BRAND_SEO_RULES = {"title_case_headings", "heading_case", "heading_sentence_case",
                     "heading_title_case", "heading_case_sentence_case", "heading_case_final_h2",
                     "heading_case_title_case"}


def _parse_changes_log(changes_log: str) -> dict:
    """
    Parse changes_log into structured change counts.
    Returns:
      {
        dims_improved: set of dimension names that had explicit changes,
        brand_fixes: int,
        rec_changes: {dim: int},
        faq_added: bool,
        canonical_answer_added: bool,
        citations_added: int,
        heading_fixes: int,
      }
    """
    dims_improved = set()
    brand_fixes = 0
    rec_changes = {}
    faq_added = False
    canonical_answer_added = False
    citations_added = 0
    heading_fixes = 0

    for line in changes_log.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # Match [REC #N: dimension] lines
        rec_match = re.search(r"\[REC\s+#\d+:\s*([a-z_]+)\]", line, re.IGNORECASE)
        if rec_match:
            dim = rec_match.group(1).lower()
            mapped = _REC_DIM_MAP.get(dim)
            if mapped:
                dims_improved.add(mapped)
                rec_changes[mapped] = rec_changes.get(mapped, 0) + 1

        # Match [BRAND: rule] lines
        brand_match = re.search(r"\[BRAND:\s*([a-z_]+)\]", line, re.IGNORECASE)
        if brand_match:
            rule = brand_match.group(1).lower()
            brand_fixes += 1
            dims_improved.add(_BRAND_DIM)
            # Heading case fixes also improve SEO Structure
            if rule in _BRAND_SEO_RULES:
                heading_fixes += 1
                dims_improved.add("seo_structure")

        # Detect FAQ/canonical additions
        lower = line.lower()
        if "faq" in lower or "frequently asked question" in lower:
            faq_added = True
            dims_improved.add("platform_optimization")
            dims_improved.add("ai_citability")
        if "canonical answer" in lower:
            canonical_answer_added = True
            dims_improved.add("ai_citability")
            dims_improved.add("platform_optimization")
        if re.search(r"(citation|named citation|added citation|\(tomlinson|\(hattie|\(rand|named statistic)", lower):
            citations_added += 1

    return {
        "dims_improved": dims_improved,
        "brand_fixes": brand_fixes,
        "rec_changes": rec_changes,
        "faq_added": faq_added,
        "canonical_answer_added": canonical_answer_added,
        "citations_added": citations_added,
        "heading_fixes": heading_fixes,
    }


def build_improvement_delta(article_json: dict) -> dict:
    """
    Build the improvement delta for one article.

    Returns dict with:
      item_num, name, cluster, geo_composite_before,
      dim_scores_before{6 dims}, changes_summary,
      dims_improved[list], changes_count,
      brand_fixes, rec_changes, faq_added, canonical_answer_added, citations_added,
      changes_log_excerpt (first 500 chars)
    """
    item_num = article_json.get("item_num", "")
    name = article_json.get("name", "")
    cluster = article_json.get("cluster", "")
    sub_cluster = article_json.get("sub_cluster", "")
    geo_composite = article_json.get("geo_composite", 0)
    changes_log = article_json.get("enhanced_changes_log", "")

    dims = article_json.get("dimensions", {})
    dim_scores = {
        "ai_citability": dims.get("ai_citability", {}).get("score", 0),
        "eeat": dims.get("eeat", {}).get("score", 0),
        "platform_optimization": dims.get("platform_optimization", {}).get("score", 0),
        "brand_voice": dims.get("brand_voice", {}).get("score", 0),
        "seo_structure": dims.get("seo_structure", {}).get("score", 0),
        "schema_recommendations": dims.get("schema_recommendations", {}).get("score", 0),
    }

    parsed = _parse_changes_log(changes_log)

    # Build human-readable changes summary
    parts = []
    if parsed["rec_changes"]:
        for dim, count in parsed["rec_changes"].items():
            label = dim.replace("_", " ").title()
            parts.append(f"{count} {label} fix(es)")
    if parsed["brand_fixes"]:
        parts.append(f"{parsed['brand_fixes']} Brand fix(es)")
    if parsed["faq_added"]:
        parts.append("FAQ section added")
    if parsed["canonical_answer_added"]:
        parts.append("Canonical answer added")
    if parsed["citations_added"]:
        parts.append(f"{parsed['citations_added']} citation(s) added")
    changes_summary = "; ".join(parts) if parts else "Minor fixes"

    changes_log_lines = [l.strip() for l in changes_log.split("\n") if l.strip().startswith("-")]
    changes_count = len(changes_log_lines)
    changes_log_excerpt = "\n".join(changes_log_lines[:6])

    # Dim improvement labels (arrow indicators)
    dims_improved = sorted(parsed["dims_improved"])

    return {
        "item_num": item_num,
        "name": name,
        "cluster": cluster,
        "sub_cluster": sub_cluster,
        "geo_composite_before": geo_composite,
        "dim_scores_before": dim_scores,
        "changes_summary": changes_summary,
        "dims_improved": dims_improved,
        "changes_count": changes_count,
        "brand_fixes": parsed["brand_fixes"],
        "rec_changes": parsed["rec_changes"],
        "faq_added": parsed["faq_added"],
        "canonical_answer_added": parsed["canonical_answer_added"],
        "citations_added": parsed["citations_added"],
        "heading_fixes": parsed["heading_fixes"],
        "changes_log_excerpt": changes_log_excerpt,
    }
