"""Write evaluation results to Google Sheets via gspread."""
import json
import logging
import time
from pathlib import Path

logger = logging.getLogger(__name__)


def get_sheets_client(service_account_json: str):
    """Return an authenticated gspread client."""
    import gspread
    from google.oauth2.service_account import Credentials

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = Credentials.from_service_account_file(service_account_json, scopes=scopes)
    return gspread.authorize(creds)


def get_or_create_spreadsheet(gc, sheet_name: str, share_email: str = "", sheet_id: str = ""):
    """Open spreadsheet by ID (preferred), by name, or create a new one."""
    import gspread

    if sheet_id:
        spreadsheet = gc.open_by_key(sheet_id)
        logger.info(f"Opened spreadsheet by ID: {sheet_id}")
    else:
        try:
            spreadsheet = gc.open(sheet_name)
            logger.info(f"Opened existing spreadsheet: {sheet_name}")
        except gspread.SpreadsheetNotFound:
            spreadsheet = gc.create(sheet_name)
            logger.info(f"Created new spreadsheet: {sheet_name}")

    if share_email:
        try:
            spreadsheet.share(share_email, perm_type="user", role="writer", notify=False)
            logger.info(f"Shared with {share_email}")
        except Exception as e:
            logger.warning(f"Could not share with {share_email}: {e}")

    return spreadsheet


def get_or_create_tab(spreadsheet, tab_name: str, headers: list[str]):
    """Get or create a worksheet tab with given headers."""
    import gspread

    try:
        ws = spreadsheet.worksheet(tab_name)
        logger.info(f"Using existing tab: {tab_name}")
    except gspread.WorksheetNotFound:
        ws = spreadsheet.add_worksheet(title=tab_name, rows=200, cols=len(headers) + 5)
        ws.append_row(headers, value_input_option="RAW")
        logger.info(f"Created tab: {tab_name}")

    return ws


# ─── Column Headers ────────────────────────────────────────────────────────────

ARTICLE_HEADERS = [
    "Item #", "Article Name", "Cluster", "Sub-Cluster", "URL Slug",
    "GEO Composite", "QAPEDS Composite",
    "AI Citability", "E-E-A-T", "Platform Optimization", "Brand Voice", "SEO Structure", "Schema Recommendations",
    "Brand Verdict", "Brand Issues",
    "AIO Ready", "ChatGPT Ready", "Perplexity Ready", "Gemini Ready", "Bing Copilot Ready",
    "Strength 1", "Strength 2", "Strength 3",
    "Rec 1 (Dimension | Fix)", "Rec 2", "Rec 3", "Rec 4", "Rec 5",
    "Schema to Add", "Title Tag Suggestion", "Meta Description", "Slug Recommendation",
    "QAPEDS: Q", "QAPEDS: A", "QAPEDS: P", "QAPEDS: E", "QAPEDS: D", "QAPEDS: S",
    "Gate 1 Pass", "Gate 2 Pass",
    "Validation Warnings", "GDoc URL",
]

CLUSTER_HEADERS = [
    "Cluster", "Sub-Cluster", "Article Count",
    "Avg GEO Composite", "Avg QAPEDS Composite",
    "Weakest Dimension", "Strongest Dimension",
    "Avg AI Citability", "Avg E-E-A-T", "Avg Platform Optimization",
    "Avg Brand Voice", "Avg SEO Structure", "Avg Schema Recommendations",
    "AIO Ready %", "ChatGPT Ready %", "Perplexity Ready %",
    "Brand PASS", "Brand WARN", "Brand FAIL", "Common Brand Issues",
    "Recurring Issue 1", "Recurring Issue 2", "Recurring Issue 3",
    "Cluster Rec 1", "Cluster Rec 2", "Cluster Rec 3",
    "Strongest Article", "Weakest Article",
]

META_HEADERS = ["Field", "Value"]


def _yn(val) -> str:
    if val is True:
        return "YES"
    if val is False:
        return "NO"
    return ""


def _safe(val, default="") -> str:
    if val is None:
        return default
    return str(val)


def build_article_row(result: dict) -> list:
    """Convert an article result dict to a flat list for Sheets."""
    dims = result.get("dimensions", {})
    qapeds = result.get("qapeds", {})
    flags = result.get("platform_flags", {})
    strengths = result.get("strengths", [])
    recs = result.get("recommendations", [])
    checklist = result.get("pre_publish_checklist", {})
    brand_issues = result.get("brand_issues", [])

    def fmt_brand_issue(i):
        parts = [i.get("rule", "")]
        instances = i.get("instances", [])
        if instances:
            parts.append("e.g. " + str(instances[0]))
        fix = i.get("fix", "")
        if fix:
            parts.append(f"FIX: {fix}")
        return " → ".join(p for p in parts if p)

    brand_issues_str = "\n".join(
        fmt_brand_issue(i) for i in brand_issues if isinstance(i, dict)
    ) if brand_issues else ""
    warnings = result.get("validation_warnings", [])

    def dim_score(key):
        d = dims.get(key, {})
        return _safe(d.get("score") if isinstance(d, dict) else None)

    def rec_str(r):
        if not r:
            return ""
        parts = []
        if r.get("rank"):
            parts.append(f"#{r['rank']}")
        if r.get("tag"):
            parts.append(f"[{r['tag']}]")
        if r.get("dimension"):
            parts.append(r["dimension"].upper())
        if r.get("issue"):
            parts.append(r["issue"])
        if r.get("fix"):
            parts.append(f"FIX: {r['fix']}")
        return " | ".join(p for p in parts if p)

    schema_to_add = checklist.get("schema_to_add", [])

    return [
        _safe(result.get("item_num")),
        _safe(result.get("name")),
        _safe(result.get("cluster")),
        _safe(result.get("sub_cluster")),
        _safe(result.get("url_slug")),
        _safe(result.get("geo_composite")),
        _safe(result.get("qapeds_composite")),
        dim_score("ai_citability"),
        dim_score("eeat"),
        dim_score("platform_optimization"),
        dim_score("brand_voice"),
        dim_score("seo_structure"),
        dim_score("schema_recommendations"),
        _safe(result.get("brand_verdict")),
        brand_issues_str,
        _yn(flags.get("aio_ready")),
        _yn(flags.get("chatgpt_ready")),
        _yn(flags.get("perplexity_ready")),
        _yn(flags.get("gemini_ready")),
        _yn(flags.get("bing_copilot_ready")),
        _safe(strengths[0] if len(strengths) > 0 else ""),
        _safe(strengths[1] if len(strengths) > 1 else ""),
        _safe(strengths[2] if len(strengths) > 2 else ""),
        rec_str(recs[0] if len(recs) > 0 else None),
        rec_str(recs[1] if len(recs) > 1 else None),
        rec_str(recs[2] if len(recs) > 2 else None),
        rec_str(recs[3] if len(recs) > 3 else None),
        rec_str(recs[4] if len(recs) > 4 else None),
        ", ".join(schema_to_add) if isinstance(schema_to_add, list) else _safe(schema_to_add),
        _safe(checklist.get("title_tag")),
        _safe(checklist.get("meta_description")),
        _safe(checklist.get("slug_recommendation")),
        _safe(qapeds.get("Q")),
        _safe(qapeds.get("A")),
        _safe(qapeds.get("P")),
        _safe(qapeds.get("E")),
        _safe(qapeds.get("D")),
        _safe(qapeds.get("S")),
        _yn(qapeds.get("gate1_pass")),
        _yn(qapeds.get("gate2_pass")),
        "; ".join(warnings) if warnings else "",
        _safe(result.get("gdoc_url")),
    ]


def build_cluster_row(result: dict) -> list:
    """Convert a cluster result dict to a flat list for Sheets."""
    dim_avg = result.get("dimension_averages", {})
    platform = result.get("platform_readiness", {})
    brand_sum = result.get("brand_summary", {})
    recurring = result.get("recurring_issues", [])
    recs = result.get("cluster_recommendations", [])
    strongest = result.get("strongest_article", {})
    weakest = result.get("weakest_article", {})

    def ri_str(r):
        if not r:
            return ""
        parts = [f"{r.get('pattern', '')} ({r.get('article_count', '')} articles)"]
        if r.get("dimension"):
            parts.append(f"Dimension: {r['dimension']}")
        if r.get("impact"):
            parts.append(f"Impact: {r['impact']}")
        return "\n".join(p for p in parts if p)

    def rec_str(r):
        if not r:
            return ""
        parts = []
        if r.get("rank"):
            parts.append(f"#{r['rank']}")
        if r.get("issue"):
            parts.append(r["issue"])
        if r.get("applies_to"):
            parts.append(f"Applies to: {r['applies_to']}")
        if r.get("dimension"):
            parts.append(f"Dimension: {r['dimension']}")
        if r.get("fix"):
            parts.append(f"FIX: {r['fix']}")
        return "\n".join(p for p in parts if p)

    return [
        _safe(result.get("cluster")),
        _safe(result.get("sub_cluster", "")),
        _safe(result.get("article_count")),
        _safe(result.get("avg_geo_composite")),
        _safe(result.get("avg_qapeds_composite")),
        _safe(result.get("weakest_dimension")),
        _safe(result.get("strongest_dimension")),
        _safe(dim_avg.get("ai_citability")),
        _safe(dim_avg.get("eeat")),
        _safe(dim_avg.get("platform_optimization")),
        _safe(dim_avg.get("brand_voice")),
        _safe(dim_avg.get("seo_structure")),
        _safe(dim_avg.get("schema_recommendations")),
        _safe(platform.get("aio_ready_pct")),
        _safe(platform.get("chatgpt_ready_pct")),
        _safe(platform.get("perplexity_ready_pct")),
        _safe(brand_sum.get("pass_count")),
        _safe(brand_sum.get("warn_count")),
        _safe(brand_sum.get("fail_count")),
        ", ".join(brand_sum.get("common_issues", [])),
        ri_str(recurring[0] if len(recurring) > 0 else None),
        ri_str(recurring[1] if len(recurring) > 1 else None),
        ri_str(recurring[2] if len(recurring) > 2 else None),
        rec_str(recs[0] if len(recs) > 0 else None),
        rec_str(recs[1] if len(recs) > 1 else None),
        rec_str(recs[2] if len(recs) > 2 else None),
        f"{strongest.get('name','')} ({strongest.get('geo_composite','')})" if strongest else "",
        f"{weakest.get('name','')} ({weakest.get('geo_composite','')})" if weakest else "",
    ]


def write_all_results(
    service_account_json: str,
    sheet_name: str,
    share_email: str,
    article_results: list[dict],
    cluster_results: list[dict],
    run_metadata: dict,
    sheet_id: str = "",
) -> str:
    """
    Write all results to Google Sheets.
    Returns the spreadsheet URL.
    """
    gc = get_sheets_client(service_account_json)
    spreadsheet = get_or_create_spreadsheet(gc, sheet_name, share_email, sheet_id=sheet_id)

    # Tab 1: Article Results
    ws_articles = get_or_create_tab(spreadsheet, "Article Results", ARTICLE_HEADERS)
    # Clear existing data below header
    if ws_articles.row_count > 1:
        spreadsheet.values_clear(f"'Article Results'!A2:ZZ")

    rows = [build_article_row(r) for r in article_results]
    if rows:
        ws_articles.append_rows(rows, value_input_option="RAW")
    logger.info(f"Wrote {len(rows)} article rows to 'Article Results' tab")

    time.sleep(1)  # avoid hitting Sheets API rate limit

    # Tab 2: Cluster Analysis (cluster-level only)
    cluster_level = [r for r in cluster_results if not r.get("sub_cluster")]
    ws_cluster = get_or_create_tab(spreadsheet, "Cluster Analysis", CLUSTER_HEADERS)
    if ws_cluster.row_count > 1:
        spreadsheet.values_clear("'Cluster Analysis'!A2:ZZ")
    cluster_rows = [build_cluster_row(r) for r in cluster_level]
    if cluster_rows:
        ws_cluster.append_rows(cluster_rows, value_input_option="RAW")
    logger.info(f"Wrote {len(cluster_rows)} cluster rows to 'Cluster Analysis' tab")

    time.sleep(1)

    # Tab 3: Sub-Cluster Analysis
    sub_cluster_level = [r for r in cluster_results if r.get("sub_cluster")]
    ws_sub = get_or_create_tab(spreadsheet, "Sub-Cluster Analysis", CLUSTER_HEADERS)
    if ws_sub.row_count > 1:
        spreadsheet.values_clear("'Sub-Cluster Analysis'!A2:ZZ")
    sub_rows = [build_cluster_row(r) for r in sub_cluster_level]
    if sub_rows:
        ws_sub.append_rows(sub_rows, value_input_option="RAW")
    logger.info(f"Wrote {len(sub_rows)} sub-cluster rows to 'Sub-Cluster Analysis' tab")

    time.sleep(1)

    # Tab 4: Run Metadata
    ws_meta = get_or_create_tab(spreadsheet, "Run Metadata", META_HEADERS)
    spreadsheet.values_clear("'Run Metadata'!A2:ZZ")
    meta_rows = [[k, str(v)] for k, v in run_metadata.items()]
    if meta_rows:
        ws_meta.append_rows(meta_rows, value_input_option="RAW")
    logger.info("Wrote run metadata tab")

    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet.id}"
    logger.info(f"Spreadsheet: {url}")
    return url


# ─── Improvement Delta Tab ─────────────────────────────────────────────────────

DELTA_HEADERS = [
    "Item #", "Article Name", "Cluster", "Sub-Cluster",
    "GEO Score (Before)", "AI Citability", "E-E-A-T", "Platform Optimization",
    "Brand Voice", "SEO Structure", "Schema Rec",
    "Dimensions Improved", "Changes Count", "Brand Fixes",
    "Citations Added", "FAQ Added", "Canonical Answer Added",
    "Changes Summary", "Changes Log Excerpt",
]


def write_improvement_delta_tab(
    spreadsheet,
    deltas: list[dict],
):
    """Write 'Improvement Delta' tab with before scores and what improved."""
    ws = get_or_create_tab(spreadsheet, "Improvement Delta", DELTA_HEADERS)
    try:
        spreadsheet.values_clear("'Improvement Delta'!A2:ZZ")
    except Exception:
        pass

    rows = []
    for d in deltas:
        ds = d.get("dim_scores_before", {})
        rows.append([
            d.get("item_num", ""),
            d.get("name", ""),
            d.get("cluster", ""),
            d.get("sub_cluster", ""),
            str(d.get("geo_composite_before", "")),
            str(ds.get("ai_citability", "")),
            str(ds.get("eeat", "")),
            str(ds.get("platform_optimization", "")),
            str(ds.get("brand_voice", "")),
            str(ds.get("seo_structure", "")),
            str(ds.get("schema_recommendations", "")),
            ", ".join(d.get("dims_improved", [])),
            str(d.get("changes_count", 0)),
            str(d.get("brand_fixes", 0)),
            str(d.get("citations_added", 0)),
            "YES" if d.get("faq_added") else "NO",
            "YES" if d.get("canonical_answer_added") else "NO",
            d.get("changes_summary", ""),
            d.get("changes_log_excerpt", "")[:600],
        ])

    if rows:
        ws.append_rows(rows, value_input_option="RAW")
    logger.info(f"Wrote {len(rows)} rows to 'Improvement Delta' tab")


# ─── Continuity Review Tab ─────────────────────────────────────────────────────

CONTINUITY_HEADERS = [
    "Item #", "Article Name", "Overall Status",
    "Word Count (Orig)", "Word Count (Enhanced)", "Word Count Delta %",
    "Headings Status", "Headings (Orig/Preserved)", "Missing Headings",
    "Keywords Status", "Keywords Retained",
    "Markdown Status", "Markdown Issues",
    "FAQ Added", "Canonical Answer Present", "Notes",
]


def write_continuity_tab(
    spreadsheet,
    continuity_results: list[dict],
):
    """Write 'Continuity Review' tab."""
    ws = get_or_create_tab(spreadsheet, "Continuity Review", CONTINUITY_HEADERS)
    try:
        spreadsheet.values_clear("'Continuity Review'!A2:ZZ")
    except Exception:
        pass

    rows = []
    for r in continuity_results:
        checks = r.get("checks", {})
        wc = checks.get("word_count", {})
        hd = checks.get("headings", {})
        kw = checks.get("keywords", {})
        md = checks.get("markdown_integrity", {})
        rows.append([
            r.get("item_num", ""),
            r.get("name", ""),
            r.get("overall", ""),
            str(wc.get("original", "")),
            str(wc.get("enhanced", "")),
            str(wc.get("delta_pct", "")),
            hd.get("status", ""),
            f"{hd.get('preserved', '')}/{hd.get('original_count', '')}",
            "; ".join(hd.get("missing", [])[:3]),
            kw.get("status", ""),
            f"{kw.get('retained', '')}/{kw.get('total', '')}",
            md.get("status", ""),
            "; ".join(md.get("issues", [])),
            "YES" if checks.get("faq_added", {}).get("present") else "NO",
            "YES" if checks.get("canonical_answer", {}).get("present") else "NO",
            "; ".join(r.get("notes", []))[:400],
        ])

    if rows:
        ws.append_rows(rows, value_input_option="RAW")
    logger.info(f"Wrote {len(rows)} rows to 'Continuity Review' tab")


# ─── Teacher Review Tab ────────────────────────────────────────────────────────

TEACHER_REVIEW_HEADERS = [
    "Item #", "Article Name", "Overall Score", "Verdict",
    "C1: Classroom Practicality", "C2: Opening Conciseness", "C3: Non-AI Tone",
    "C4: Visual Structure", "C5: Grade-Band Specificity", "C6: Term Definitions",
    "C7: Teacher Agency", "C8: Differentiation/Inclusivity",
    "C9: Standards Alignment", "C10: Wayground Value Prop",
    "Top Issues", "Positive Signals", "Narrative",
]


def write_teacher_review_tab(
    spreadsheet,
    teacher_reviews: list[dict],
):
    """Write 'Teacher Review' tab."""
    ws = get_or_create_tab(spreadsheet, "Teacher Review", TEACHER_REVIEW_HEADERS)
    try:
        spreadsheet.values_clear("'Teacher Review'!A2:ZZ")
    except Exception:
        pass

    rows = []
    for r in teacher_reviews:
        scores = r.get("scores", {})
        rows.append([
            r.get("item_num", ""),
            r.get("name", ""),
            str(r.get("overall_score", "")),
            r.get("verdict", ""),
            str(scores.get("C1_classroom_practicality", "")),
            str(scores.get("C2_opening_conciseness", "")),
            str(scores.get("C3_non_ai_tone", "")),
            str(scores.get("C4_visual_structure", "")),
            str(scores.get("C5_grade_band_specificity", "")),
            str(scores.get("C6_term_definitions", "")),
            str(scores.get("C7_teacher_agency", "")),
            str(scores.get("C8_differentiation_inclusivity", "")),
            str(scores.get("C9_standards_alignment", "")),
            str(scores.get("C10_wayground_value_prop", "")),
            "; ".join(r.get("top_issues", []))[:400],
            "; ".join(r.get("positive_signals", []))[:300],
            r.get("narrative", "")[:600],
        ])

    if rows:
        ws.append_rows(rows, value_input_option="RAW")
    logger.info(f"Wrote {len(rows)} rows to 'Teacher Review' tab")
