#!/usr/bin/env python3
"""
Convert markdown to Webflow-compatible HTML with proper list formatting.
"""
import sys
import re
import markdown
from markdown.extensions import fenced_code, tables, nl2br

def convert_markdown_to_html(markdown_text):
    """
    Convert markdown to clean HTML with proper list formatting.

    Args:
        markdown_text: Markdown content as string

    Returns:
        Clean HTML string suitable for Webflow CMS
    """
    # Pre-process markdown to ensure lists are recognized
    # Markdown requires blank lines before lists
    lines = markdown_text.split('\n')
    processed_lines = []

    for i, line in enumerate(lines):
        # Check if this line starts a list
        is_list_start = (
            (line.strip().startswith('- ') or
             line.strip().startswith('* ') or
             re.match(r'^\d+\.\s', line.strip())) and
            i > 0 and
            lines[i-1].strip() != '' and
            not (lines[i-1].strip().startswith('- ') or
                 lines[i-1].strip().startswith('* ') or
                 re.match(r'^\d+\.\s', lines[i-1].strip()))
        )

        # Add blank line before list if needed
        if is_list_start:
            processed_lines.append('')

        processed_lines.append(line)

    markdown_text = '\n'.join(processed_lines)

    # Configure markdown extensions for proper conversion
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'tables',
        'sane_lists'  # Critical for proper list handling
    ])

    # Convert markdown to HTML
    html = md.convert(markdown_text)

    # Post-processing fixes

    # Ensure lists aren't nested in paragraphs
    html = re.sub(r'<p>\s*<ul>', '<ul>', html)
    html = re.sub(r'</ul>\s*</p>', '</ul>', html)
    html = re.sub(r'<p>\s*<ol>', '<ol>', html)
    html = re.sub(r'</ol>\s*</p>', '</ol>', html)

    # Add inline styles to table elements to match Wayground table formatting
    html = re.sub(
        r'<table>',
        '<table border="1" cellpadding="0" cellspacing="0" '
        'style="border-collapse:collapse; width:100%; font-family:Arial, sans-serif; color:#B0006D;">',
        html
    )
    html = re.sub(
        r'<th>',
        '<th style="padding:12px 10px; font-size:18px; font-weight:700; text-align:left;">',
        html
    )
    html = re.sub(r'<tbody>', '<tbody style="font-size:18px;">', html)
    html = re.sub(r'<td>', '<td style="padding:12px 10px;">', html)

    # Wrap tables in Webflow's HTML embed marker so they render on the frontend
    html = re.sub(r'(<table[\s\S]*?</table>)', "<div data-rt-embed-type='true'>\\1</div>", html)

    # Remove empty paragraphs
    html = re.sub(r'<p>\s*</p>', '', html)

    # Split bold label + body text into separate <p> tags — Webflow renders \n inside <p> as invisible
    html = re.sub(r'(</strong>)\n', r'\1</p><p>', html)

    # Remove newlines between list tags — Webflow renders \n as gaps inside <ul>/<ol>
    html = re.sub(r'(<(?:ul|ol)>)\s*\n\s*', r'\1', html)
    html = re.sub(r'\s*\n\s*(</(?:ul|ol)>)', r'\1', html)
    html = re.sub(r'(</li>)\s*\n\s*(<li)', r'\1\2', html)

    # Clean up excessive whitespace
    html = re.sub(r'\n\n+', '\n', html)

    return html.strip()

def main():
    """Read markdown from stdin or file, output HTML to stdout."""
    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            markdown_text = f.read()
    else:
        # Read from stdin
        markdown_text = sys.stdin.read()

    html = convert_markdown_to_html(markdown_text)
    print(html)

if __name__ == '__main__':
    main()
