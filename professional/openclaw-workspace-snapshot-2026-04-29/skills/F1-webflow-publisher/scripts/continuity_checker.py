"""Structural continuity checks: compare original article text vs. enhanced markdown."""
import re
from collections import Counter


def _word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def _extract_h2s(text: str) -> list[str]:
    """Extract H2 headings (## ...) from markdown, lowercased for comparison."""
    return [
        re.sub(r"^##\s*", "", line).strip().lower()
        for line in text.split("\n")
        if re.match(r"^##\s+", line)
    ]


def _extract_h2s_from_plain(text: str) -> list[str]:
    """Try to extract headings from plain text (fallback for fetched text)."""
    # Some fetched docs have lines that look like headings (short, no period, capitalized)
    # This is a best-effort extraction
    headings = []
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped and len(stripped) < 80 and not stripped.endswith(".") and stripped[0].isupper():
            if not any(c in stripped for c in ["http", "www", "@"]):
                headings.append(stripped.lower())
    return headings


def _top_keywords(text: str, n: int = 15) -> set[str]:
    """Extract top n meaningful words from the first 1000 words of text."""
    STOP = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with",
        "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does",
        "did", "will", "would", "could", "should", "may", "might", "that", "this", "these",
        "those", "it", "its", "you", "your", "we", "our", "they", "their", "how", "what",
        "when", "where", "which", "who", "by", "from", "as", "all", "each", "can", "more",
        "also", "not", "no", "than", "so", "if", "about", "into", "through", "very",
    }
    words = re.findall(r"\b[a-z]{4,}\b", text[:5000].lower())
    freq = Counter(w for w in words if w not in STOP)
    return {w for w, _ in freq.most_common(n)}


def _check_markdown_integrity(text: str) -> tuple[bool, list[str]]:
    """Check for common markdown breakage patterns."""
    issues = []
    # Unclosed bold/italic: odd number of ** or * that aren't in code blocks
    # Strip code blocks first
    no_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    no_code = re.sub(r"`[^`]+`", "", no_code)
    bold_count = len(re.findall(r"\*\*", no_code))
    if bold_count % 2 != 0:
        issues.append(f"Odd number of ** markers ({bold_count}) — possible unclosed bold")
    # Orphaned link text: [something]( without closing )
    orphaned = re.findall(r"\[[^\]]+\]\([^)]*$", no_code, re.MULTILINE)
    if orphaned:
        issues.append(f"Orphaned link pattern: {orphaned[0][:60]}")
    return len(issues) == 0, issues


def check_continuity(
    original_text: str,
    enhanced_md: str,
    article_name: str = "",
) -> dict:
    """
    Compare original article text vs. enhanced markdown.

    Returns:
      {
        overall: "PASS" | "WARN" | "FAIL",
        checks: {
          word_count: {status, original, enhanced, delta_pct, note},
          headings: {status, original_count, preserved, missing, note},
          keywords: {status, retained, total, missing_examples, note},
          markdown_integrity: {status, issues, note},
          faq_added: {present},
          canonical_answer: {present},
        },
        notes: [str],
      }
    """
    checks = {}
    notes = []

    # 1. Word count stability
    # AEO enhancement intentionally ADDS content (citations, FAQ, canonical answers).
    # Growth up to +120% is expected and fine — only flag large shrinkage.
    orig_wc = _word_count(original_text)
    enh_wc = _word_count(enhanced_md)
    if orig_wc > 0:
        delta_pct = (enh_wc - orig_wc) / orig_wc * 100
    else:
        delta_pct = 0
    if delta_pct >= -10:
        # Any growth, or shrinkage ≤10% → PASS
        wc_status = "PASS"
    elif delta_pct >= -25:
        wc_status = "WARN"
        notes.append(f"Content shrunk {delta_pct:.0f}% (orig={orig_wc}, enh={enh_wc})")
    else:
        wc_status = "FAIL"
        notes.append(f"Content significantly shrunk {delta_pct:.0f}% (orig={orig_wc}, enh={enh_wc})")
    checks["word_count"] = {
        "status": wc_status,
        "original": orig_wc,
        "enhanced": enh_wc,
        "delta_pct": round(delta_pct, 1),
        "note": f"{delta_pct:+.0f}% change",
    }

    # 2. Heading preservation
    # Only compare headings if the original has markdown-style ## headings.
    # Original text from Google Docs is plain text — no ## markers — so heading
    # comparison vs. enhanced markdown would always show false "missing" headings.
    orig_h2s = _extract_h2s(original_text)
    enh_h2s = set(_extract_h2s(enhanced_md))
    if not orig_h2s:
        # Original is plain text (Google Doc fetch) — no reliable heading baseline.
        # Check that enhanced has at least some structure instead.
        n_enh_headings = len(enh_h2s)
        h_status = "PASS" if n_enh_headings >= 2 else "WARN"
        checks["headings"] = {
            "status": h_status,
            "original_count": 0,
            "preserved": n_enh_headings,
            "missing": [],
            "note": f"Plain-text original — enhanced has {n_enh_headings} H2 headings",
        }
    else:
        preserved = []
        missing = []
        for h in orig_h2s:
            if h in enh_h2s or any(e.startswith(h[:30]) or h.startswith(e[:30]) for e in enh_h2s):
                preserved.append(h)
            else:
                missing.append(h)
        n_orig = len(orig_h2s)
        n_miss = len(missing)
        if n_miss == 0:
            h_status = "PASS"
        elif n_miss <= 2:
            h_status = "WARN"
            notes.append(f"{n_miss} heading(s) not found in enhanced: {missing[:2]}")
        else:
            h_status = "FAIL"
            notes.append(f"{n_miss}/{n_orig} headings missing from enhanced")
        checks["headings"] = {
            "status": h_status,
            "original_count": n_orig,
            "preserved": len(preserved),
            "missing": missing,
            "note": f"{len(preserved)}/{n_orig} preserved",
        }

    # 3. Keyword retention
    orig_kw = _top_keywords(original_text, 15)
    enh_lower = enhanced_md.lower()
    retained = {w for w in orig_kw if w in enh_lower}
    missing_kw = orig_kw - retained
    retention_rate = len(retained) / len(orig_kw) if orig_kw else 1.0
    if retention_rate >= 0.8:
        kw_status = "PASS"
    elif retention_rate >= 0.6:
        kw_status = "WARN"
        notes.append(f"Keyword retention {retention_rate:.0%} — missing: {sorted(missing_kw)[:5]}")
    else:
        kw_status = "FAIL"
        notes.append(f"Low keyword retention {retention_rate:.0%}")
    checks["keywords"] = {
        "status": kw_status,
        "retained": len(retained),
        "total": len(orig_kw),
        "missing_examples": sorted(missing_kw)[:5],
        "note": f"{len(retained)}/{len(orig_kw)} keywords retained",
    }

    # 4. Markdown integrity
    md_ok, md_issues = _check_markdown_integrity(enhanced_md)
    md_status = "PASS" if md_ok else "WARN"
    if md_issues:
        notes.extend(md_issues)
    checks["markdown_integrity"] = {
        "status": md_status,
        "issues": md_issues,
        "note": "OK" if md_ok else "; ".join(md_issues),
    }

    # 5. Info checks (no pass/fail impact)
    faq_present = bool(re.search(r"##\s*frequently asked question", enhanced_md, re.IGNORECASE))
    canonical_present = bool(
        re.search(r"\*\*[^*]{20,150}\*\*", enhanced_md[:1500])  # bold paragraph near top
        or "canonical answer" in enhanced_md.lower()
    )
    checks["faq_added"] = {"present": faq_present}
    checks["canonical_answer"] = {"present": canonical_present}

    # Overall status
    statuses = [v["status"] for k, v in checks.items() if "status" in v]
    if "FAIL" in statuses:
        overall = "FAIL"
    elif "WARN" in statuses:
        overall = "WARN"
    else:
        overall = "PASS"

    return {
        "overall": overall,
        "checks": checks,
        "notes": notes,
    }
