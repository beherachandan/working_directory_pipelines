"""Extract and validate <scores> JSON and <output> narrative from Claude responses."""
import json
import re


class ParseError(Exception):
    pass


def extract_scores_block(raw_response: str) -> dict:
    """
    Find the <scores>...</scores> block and parse as JSON.
    Raises ParseError if not found or invalid JSON.
    """
    match = re.search(r"<scores>\s*(.*?)\s*</scores>", raw_response, re.DOTALL)
    if not match:
        raise ParseError("No <scores> block found in response")

    json_str = match.group(1).strip()
    # Strip any markdown code fences if Claude wrapped in them
    json_str = re.sub(r"^```(?:json)?\s*", "", json_str)
    json_str = re.sub(r"\s*```$", "", json_str)

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ParseError(f"Invalid JSON in <scores> block: {e}\nContent: {json_str[:500]}")


def extract_output_block(raw_response: str) -> str:
    """
    Find the <output>...</output> block and return as string.
    Falls back to the full response if no output block found.
    """
    match = re.search(r"<output>\s*(.*?)\s*</output>", raw_response, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_response.strip()


def merge_geo_and_brand(
    geo_scores: dict,
    brand_scores: dict,
    geo_weights: dict,
) -> dict:
    """
    Merge brand_score into geo_scores and recompute GEO composite.

    If brand evaluation failed (brand_scores is empty/None), recalculate
    GEO composite over remaining 5 dimensions with renormalized weights,
    and set brand_eval_failed: true.
    """
    result = {**geo_scores}

    if not brand_scores:
        result["brand_eval_failed"] = True
        result["brand_verdict"] = "UNKNOWN"
        # Renormalize weights over 5 dimensions (exclude brand_voice 15%)
        remaining_total = sum(v for k, v in geo_weights.items() if k != "brand_voice")
        scale = 1.0 / remaining_total
        geo_composite = 0.0
        dims = result.get("dimensions", {})
        for dim, weight in geo_weights.items():
            if dim == "brand_voice":
                continue
            score = dims.get(dim, {}).get("score", 0) if isinstance(dims.get(dim), dict) else 0
            geo_composite += score * weight * scale
        result["geo_composite"] = round(geo_composite, 1)
        if "dimensions" not in result:
            result["dimensions"] = {}
        result["dimensions"]["brand_voice"] = {"score": None, "note": "brand evaluation failed"}
        return result

    brand_score = brand_scores.get("brand_score", 0)
    brand_verdict = brand_scores.get("verdict", "UNKNOWN")

    result["brand_verdict"] = brand_verdict
    result["brand_issues"] = brand_scores.get("issues", [])
    result["brand_positive_signals"] = brand_scores.get("positive_signals", [])
    result["brand_eval_failed"] = False

    if "dimensions" not in result:
        result["dimensions"] = {}
    result["dimensions"]["brand_voice"] = {
        "score": brand_score,
        "verdict": brand_verdict,
        "hard_fail_rules": brand_scores.get("hard_fail_rules_violated", []),
        "vocabulary_check": brand_scores.get("vocabulary_check", {}),
        "tone_check": brand_scores.get("tone_check", {}),
        "format_check": brand_scores.get("format_check", {}),
    }

    # Recompute full GEO composite with brand included
    dims = result.get("dimensions", {})
    geo_composite = 0.0
    for dim, weight in geo_weights.items():
        if dim == "brand_voice":
            score = brand_score
        else:
            dim_data = dims.get(dim, {})
            score = dim_data.get("score", 0) if isinstance(dim_data, dict) else 0
        geo_composite += score * weight

    result["geo_composite"] = round(geo_composite, 1)
    # Remove the partial composite if present
    result.pop("geo_composite_partial", None)

    return result


def validate_article_result(result: dict) -> list[str]:
    """
    Return list of validation warnings for an article result.
    Empty list means all required fields are present and in range.
    """
    warnings = []
    required_top = ["geo_composite", "qapeds_composite", "dimensions", "qapeds", "platform_flags",
                    "strengths", "recommendations", "pre_publish_checklist"]
    for field in required_top:
        if field not in result:
            warnings.append(f"Missing required field: {field}")

    if "geo_composite" in result:
        v = result["geo_composite"]
        if not isinstance(v, (int, float)) or not (0 <= v <= 100):
            warnings.append(f"geo_composite out of range: {v}")

    if "qapeds_composite" in result:
        v = result["qapeds_composite"]
        if not isinstance(v, (int, float)) or not (0 <= v <= 10):
            warnings.append(f"qapeds_composite out of range: {v}")

    dims = result.get("dimensions", {})
    for dim in ["ai_citability", "eeat", "platform_optimization", "seo_structure", "schema_recommendations"]:
        if dim not in dims:
            warnings.append(f"Missing dimension: {dim}")
        elif isinstance(dims[dim], dict):
            score = dims[dim].get("score")
            if score is not None and not (0 <= score <= 100):
                warnings.append(f"Dimension {dim} score out of range: {score}")

    return warnings


def build_article_output(
    article,  # ArticleRecord
    merged_result: dict,
    geo_narrative: str,
    brand_narrative: str,
    fetch_warning: str,
) -> dict:
    """
    Build the final persisted article result dict, combining metadata + scores + narratives.
    """
    return {
        # Metadata
        "item_num": article.item_num,
        "name": article.name,
        "cluster": article.cluster,
        "sub_cluster": article.sub_cluster,
        "gdoc_url": article.gdoc_url,
        "url_slug": article.url_slug,
        "creation_notes": article.creation_notes[:300] if article.creation_notes else "",
        "fetch_warning": fetch_warning,
        # Scores (merged)
        **merged_result,
        # Narratives
        "geo_narrative": geo_narrative,
        "brand_narrative": brand_narrative,
    }
