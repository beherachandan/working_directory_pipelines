#!/usr/bin/env python3
"""Convert Markdown to Webflow-compatible HTML.

Reads markdown from stdin, writes HTML to stdout.

Key: uses sane_lists extension for proper <ul>/<ol>/<li> rendering
instead of collapsing list items into <p> tags.

Also pre-processes to ensure a blank line precedes list blocks that
immediately follow non-list text — required for proper list parsing.

Post-processing:
- Unwraps lists from erroneous <p> tags
- Compacts whitespace between list tags (Webflow renders \\n as visible gaps)
- Applies Wayground table styling with data-rt-embed-type wrapper
- Removes empty <p> tags
- Splits bold labels from body text on newlines

Usage:
    echo "* item 1\\n* item 2" | python3 scripts/markdown-to-webflow-html.py
    python3 scripts/markdown-to-webflow-html.py < input.md > output.html
"""
import re
import sys
import markdown


def ensure_list_spacing(md_text: str) -> str:
    """Insert a blank line before list blocks when preceded by non-list text.

    Standard markdown requires a blank line between regular text and a list.
    Without it, the markdown library wraps the list items in <p> tags instead
    of generating proper <ul>/<li> elements.
    """
    lines = md_text.split("\n")
    result = []
    for i, line in enumerate(lines):
        is_list_item = bool(re.match(r"^[*\-+] ", line) or re.match(r"^\d+\. ", line))
        if is_list_item and i > 0:
            prev = lines[i - 1]
            prev_is_list = bool(re.match(r"^[*\-+] ", prev) or re.match(r"^\d+\. ", prev))
            if prev.strip() and not prev_is_list:
                result.append("")  # insert blank line
        result.append(line)
    return "\n".join(result)


def convert(md_text: str) -> str:
    md_text = ensure_list_spacing(md_text)
    html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists"],
    )

    # ── Post-processing ────────────────────────────────────────────────────

    # Unwrap lists from erroneous <p> wrappers
    html = re.sub(r"<p>\s*<ul>", "<ul>", html)
    html = re.sub(r"</ul>\s*</p>", "</ul>", html)
    html = re.sub(r"<p>\s*<ol>", "<ol>", html)
    html = re.sub(r"</ol>\s*</p>", "</ol>", html)

    # Table styling — Wayground brand colors + Webflow HTML embed marker
    html = re.sub(
        r"<table>",
        '<table border="1" cellpadding="0" cellspacing="0" '
        'style="border-collapse:collapse; width:100%; font-family:Arial, sans-serif; color:#B0006D;">',
        html,
    )
    html = re.sub(
        r"<th>",
        '<th style="padding:12px 10px; font-size:18px; font-weight:700; text-align:left;">',
        html,
    )
    html = re.sub(r"<tbody>", '<tbody style="font-size:18px;">', html)
    html = re.sub(r"<td>", '<td style="padding:12px 10px;">', html)
    # Wrap tables in Webflow HTML embed marker so they render on the frontend
    html = re.sub(r"(<table[\s\S]*?</table>)", "<div data-rt-embed-type='true'>\\1</div>", html)

    # Remove empty paragraphs
    html = re.sub(r"<p>\s*</p>", "", html)

    # Split bold label + body text — Webflow renders \n inside <p> as invisible
    html = re.sub(r"(</strong>)\n", r"\1</p><p>", html)

    # Compact list whitespace — Webflow renders \n between list tags as visible gaps
    html = re.sub(r"(<(?:ul|ol)>)\s*\n\s*", r"\1", html)
    html = re.sub(r"\s*\n\s*(</(?:ul|ol)>)", r"\1", html)
    html = re.sub(r"(</li>)\s*\n\s*(<li)", r"\1\2", html)

    # Clean up excessive whitespace
    html = re.sub(r"\n\n+", "\n", html)

    return html.strip()


if __name__ == "__main__":
    md_text = sys.stdin.read()
    print(convert(md_text), end="")
