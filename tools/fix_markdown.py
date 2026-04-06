#!/usr/bin/env python3
"""
fix_markdown.py — Fix GitHub rendering issues in the monograph's .md files.

Three classes of fix:
  1. ESCAPED UNDERSCORES: \_  inside $...$ math → _ (6,698 instances)
  2. BARE ASTERISKS:      $b^*$ → $b^{\ast}$ to prevent markdown emphasis (337 instances)
  3. #P NOTATION:         $\#P$ → \#\mathbf{P} or plain-text fallback (4 instances)

Usage:
  python3 fix_markdown.py                   # dry-run, show what would change
  python3 fix_markdown.py --apply           # apply fixes in-place
  python3 fix_markdown.py --file FILE       # fix a single file (dry-run)
  python3 fix_markdown.py --file FILE --apply
  python3 fix_markdown.py --stats           # just print statistics

Optional LaTeX export:
  python3 fix_markdown.py --latex           # generate .tex stubs in latex/ dir

Author: Saxon Nicholls / Claude
"""

import argparse
import os
import re
import sys
from pathlib import Path

# ─────────────────────────────────────────────────────────────
# Regex patterns
# ─────────────────────────────────────────────────────────────

# Match inline math $...$ (not $$...$$).  Non-greedy, avoids matching across lines.
# We handle $$ display math separately to avoid false positives.
INLINE_MATH = re.compile(
    r'(?<!\$)\$(?!\$)'   # opening $ not preceded/followed by $
    r'([^\$\n]+?)'        # content (no newlines, non-greedy)
    r'\$(?!\$)',           # closing $ not followed by $
)

# Match display math $$...$$ (possibly multi-line)
DISPLAY_MATH = re.compile(
    r'\$\$(.+?)\$\$',
    re.DOTALL,
)

# Inside math: \_ → _
ESCAPED_UNDERSCORE = re.compile(r'\\_')

# Inside math: bare * used as superscript star (e.g. b^*, \nu^*, etc.)
# Matches ^* or ^{*} but NOT ^{\ast} (already fixed)
BARE_STAR_SUPER = re.compile(r'\^\*(?!\{)')    # ^*  not followed by {
BARE_STAR_BRACE = re.compile(r'\^\{\*\}')      # ^{*}

# Also catch lone * at end of math that could be emphasis (e.g. $b^*$)
# and * used as multiplication where it could pair with another * on the line
STAR_IN_MATH = re.compile(r'(?<!\\)\*')  # any * not preceded by \

# #P notation inside math
HASH_P = re.compile(r'\\#\\mathbf\{P\}')  # already correct form
HASH_P_BARE = re.compile(r'\\#P')         # bare \#P needs fixing
HASH_P_PLAIN = re.compile(r'\$\#P\$')     # $#P$ outside math context


# ─────────────────────────────────────────────────────────────
# Core fix functions
# ─────────────────────────────────────────────────────────────

def fix_math_content(math_str: str) -> str:
    """Fix rendering issues inside a math expression (inline or display)."""
    result = math_str

    # Fix 1: \_ → _ inside math
    result = ESCAPED_UNDERSCORE.sub('_', result)

    # Fix 2: ^* → ^{\ast}  and  ^{*} → ^{\ast}
    result = BARE_STAR_SUPER.sub(lambda m: '^{\\ast}', result)
    result = BARE_STAR_BRACE.sub(lambda m: '^{\\ast}', result)

    # Fix 2b: remaining bare * that aren't \ast, \star, or part of a command
    # Be careful: * can be legitimate (e.g. in \cdot, comments, etc.)
    # Only fix * that appears to be a superscript or standalone symbol
    # We handle the most common case: $x^*$ is already caught above.
    # For other cases like $p^*$ in subscripts $b^*_i$, the ^* pattern catches it.

    # Fix 3: \#P → \#\mathbf{P} (more robust rendering)
    result = HASH_P_BARE.sub(lambda m: '\\#\\mathbf{P}', result)

    return result


def fix_line(line: str) -> str:
    """Fix a single line of markdown, handling both inline and display math."""

    # First, handle display math ($$...$$) on a single line
    def fix_display(m):
        fixed = fix_math_content(m.group(1))
        return '$$' + fixed + '$$'

    line = DISPLAY_MATH.sub(fix_display, line)

    # Then handle inline math ($...$)
    # We need to be careful not to touch already-processed display math
    def fix_inline(m):
        fixed = fix_math_content(m.group(1))
        return '$' + fixed + '$'

    line = INLINE_MATH.sub(fix_inline, line)

    # Fix $#P$ outside math (plain text fallback)
    # Replace $#P$ with #**P** (bold P, markdown-safe)
    line = re.sub(r'\$#P\$', '#**P**', line)

    # Fix \_ in regular text (outside math) — e.g. FIBER\_BUNDLES.md → FIBER_BUNDLES.md
    # Split on inline math, only fix text parts
    parts = re.split(r'(\$[^\$\n]+?\$)', line)
    fixed_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 0:  # outside math
            part = part.replace('\\_', '_')
        fixed_parts.append(part)
    line = ''.join(fixed_parts)

    return line


def fix_file_content(content: str) -> str:
    """Fix all rendering issues in a file's content."""
    lines = content.split('\n')

    # Track whether we're inside a display math block ($$...$$  on separate lines)
    in_display_math = False
    fixed_lines = []

    for line in lines:
        stripped = line.strip()

        # Check for display math delimiters on their own line
        if stripped == '$$':
            in_display_math = not in_display_math
            fixed_lines.append(line)
            continue

        # Check for $$ at start of line (multi-line display math start)
        if not in_display_math and stripped.startswith('$$') and not stripped.endswith('$$'):
            in_display_math = True
            fixed_lines.append(line[:len(line)-len(line.lstrip())] + '$$' + fix_math_content(stripped[2:]))
            continue

        # Check for $$ at end of line (multi-line display math end)
        if in_display_math and stripped.endswith('$$') and not stripped.startswith('$$'):
            in_display_math = False
            fixed_lines.append(fix_math_content(stripped[:-2]) + '$$')
            continue

        if in_display_math:
            # Inside multi-line display math — fix math content directly
            fixed_lines.append(fix_math_content(line))
        else:
            # Regular line — fix inline math and single-line display math
            fixed_lines.append(fix_line(line))

    return '\n'.join(fixed_lines)


# ─────────────────────────────────────────────────────────────
# Statistics
# ─────────────────────────────────────────────────────────────

def count_issues(content: str) -> dict:
    """Count rendering issues in file content."""
    counts = {
        'escaped_underscores': 0,
        'bare_asterisks': 0,
        'hash_p': 0,
    }

    # Count \_ inside math contexts
    for m in INLINE_MATH.finditer(content):
        math = m.group(1)
        counts['escaped_underscores'] += len(ESCAPED_UNDERSCORE.findall(math))
        counts['bare_asterisks'] += len(BARE_STAR_SUPER.findall(math))
        counts['bare_asterisks'] += len(BARE_STAR_BRACE.findall(math))
        counts['hash_p'] += len(HASH_P_BARE.findall(math))

    for m in DISPLAY_MATH.finditer(content):
        math = m.group(1)
        counts['escaped_underscores'] += len(ESCAPED_UNDERSCORE.findall(math))
        counts['bare_asterisks'] += len(BARE_STAR_SUPER.findall(math))
        counts['bare_asterisks'] += len(BARE_STAR_BRACE.findall(math))
        counts['hash_p'] += len(HASH_P_BARE.findall(math))

    # Also count in multi-line display math blocks
    in_display = False
    for line in content.split('\n'):
        if line.strip() == '$$':
            in_display = not in_display
            continue
        if in_display:
            counts['escaped_underscores'] += len(ESCAPED_UNDERSCORE.findall(line))
            counts['bare_asterisks'] += len(BARE_STAR_SUPER.findall(line))
            counts['bare_asterisks'] += len(BARE_STAR_BRACE.findall(line))
            counts['hash_p'] += len(HASH_P_BARE.findall(line))

    counts['hash_p'] += len(re.findall(r'\$#P\$', content))

    return counts


# ─────────────────────────────────────────────────────────────
# File discovery
# ─────────────────────────────────────────────────────────────

def find_md_files(root: str) -> list:
    """Find all .md files in the project (papers/, navigation/, book/, README)."""
    root = Path(root)
    dirs = ['papers', 'navigation', 'book']
    files = []

    for d in dirs:
        dirpath = root / d
        if dirpath.exists():
            files.extend(sorted(dirpath.glob('*.md')))

    # Also include README.md
    readme = root / 'README.md'
    if readme.exists():
        files.append(readme)

    return files


# ─────────────────────────────────────────────────────────────
# LaTeX export (basic)
# ─────────────────────────────────────────────────────────────

def md_to_latex_stub(content: str, title: str) -> str:
    """Convert markdown paper to a basic LaTeX document stub.

    This is NOT a full converter — it handles the math-heavy structure
    of our papers. For full conversion, use pandoc with custom filters.
    """
    # First apply all markdown fixes
    content = fix_file_content(content)

    lines = content.split('\n')
    latex_lines = []
    latex_lines.append('\\documentclass[11pt,a4paper]{article}')
    latex_lines.append('\\usepackage{amsmath,amssymb,amsthm}')
    latex_lines.append('\\usepackage{hyperref}')
    latex_lines.append('\\usepackage{booktabs}')
    latex_lines.append('\\usepackage{geometry}')
    latex_lines.append('\\geometry{margin=1in}')
    latex_lines.append('')
    latex_lines.append('\\newtheorem{theorem}{Theorem}[section]')
    latex_lines.append('\\newtheorem{definition}[theorem]{Definition}')
    latex_lines.append('\\newtheorem{proposition}[theorem]{Proposition}')
    latex_lines.append('\\newtheorem{corollary}[theorem]{Corollary}')
    latex_lines.append('\\newtheorem{conjecture}[theorem]{Conjecture}')
    latex_lines.append('\\newtheorem{remark}[theorem]{Remark}')
    latex_lines.append('')
    latex_lines.append(f'\\title{{{title}}}')
    latex_lines.append('\\author{Saxon Nicholls\\\\\\texttt{me@saxonnicholls.com}}')
    latex_lines.append('\\date{\\today}')
    latex_lines.append('')
    latex_lines.append('\\begin{document}')
    latex_lines.append('\\maketitle')
    latex_lines.append('')

    in_display_math = False
    in_table = False
    in_code = False

    for line in lines:
        stripped = line.strip()

        # Skip the title/author/preprint header (already in \title)
        if stripped.startswith('# ') and not any(
            stripped.startswith(f'## {i}.') for i in range(20)
        ):
            continue
        if stripped.startswith('**Saxon Nicholls**'):
            continue
        if stripped.startswith('**Paper '):
            continue
        if stripped.startswith('**PREPRINT**'):
            continue

        # Code blocks
        if stripped.startswith('```'):
            if in_code:
                latex_lines.append('\\end{verbatim}')
                in_code = False
            else:
                latex_lines.append('\\begin{verbatim}')
                in_code = True
            continue

        if in_code:
            latex_lines.append(line)
            continue

        # Display math
        if stripped == '$$':
            if in_display_math:
                latex_lines.append('\\]')
                in_display_math = False
            else:
                latex_lines.append('\\[')
                in_display_math = True
            continue

        if in_display_math:
            latex_lines.append(line)
            continue

        # Headings
        if stripped.startswith('## '):
            section_title = stripped[3:].strip()
            latex_lines.append(f'\\section{{{section_title}}}')
            continue
        if stripped.startswith('### '):
            subsection_title = stripped[4:].strip()
            latex_lines.append(f'\\subsection{{{subsection_title}}}')
            continue

        # Horizontal rules
        if stripped == '---':
            latex_lines.append('')
            continue

        # Tables (basic — just pass through as-is in a comment)
        if stripped.startswith('|'):
            if not in_table:
                latex_lines.append('% BEGIN TABLE (convert manually)')
                in_table = True
            latex_lines.append(f'% {stripped}')
            continue
        elif in_table:
            latex_lines.append('% END TABLE')
            in_table = False

        # Bold → \textbf
        line_out = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', line)

        # Italic → \textit
        line_out = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'\\textit{\1}', line_out)

        # Cross-references: PAPER\_NAME.md → \\texttt{PAPER\_NAME}
        line_out = re.sub(
            r'([A-Z][A-Z_]+)(?:\\_|_)(?:[A-Z_]+\.md|md)',
            lambda m: f'\\texttt{{{m.group(0).replace(chr(92)+"_", "_").replace(".md", "")}}}',
            line_out
        )

        latex_lines.append(line_out)

    if in_table:
        latex_lines.append('% END TABLE')

    latex_lines.append('')
    latex_lines.append('\\end{document}')

    return '\n'.join(latex_lines)


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Fix GitHub markdown rendering issues in the monograph'
    )
    parser.add_argument('--apply', action='store_true',
                        help='Apply fixes in-place (default: dry-run)')
    parser.add_argument('--file', type=str, default=None,
                        help='Fix a single file instead of all')
    parser.add_argument('--stats', action='store_true',
                        help='Print statistics only')
    parser.add_argument('--latex', action='store_true',
                        help='Generate LaTeX stubs in latex/ directory')
    parser.add_argument('--root', type=str,
                        default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        help='Project root directory')
    args = parser.parse_args()

    # Find files
    if args.file:
        files = [Path(args.file)]
    else:
        files = find_md_files(args.root)

    if not files:
        print("No .md files found.")
        sys.exit(1)

    print(f"Found {len(files)} markdown files\n")

    # Process
    total_counts = {'escaped_underscores': 0, 'bare_asterisks': 0, 'hash_p': 0}
    total_changed = 0
    file_reports = []

    for fpath in files:
        content = fpath.read_text(encoding='utf-8')
        counts = count_issues(content)
        total_issues = sum(counts.values())

        for k in total_counts:
            total_counts[k] += counts[k]

        if total_issues > 0:
            file_reports.append((fpath.name, counts, total_issues))

        if args.stats:
            continue

        # Apply fixes
        fixed = fix_file_content(content)

        if fixed != content:
            total_changed += 1
            n_changes = sum(1 for a, b in zip(content, fixed) if a != b)

            if args.apply:
                fpath.write_text(fixed, encoding='utf-8')
                print(f"  FIXED  {fpath.name} ({total_issues} issues)")
            else:
                print(f"  WOULD FIX  {fpath.name} ({total_issues} issues)")

        # LaTeX export
        if args.latex:
            latex_dir = Path(args.root) / 'latex'
            latex_dir.mkdir(exist_ok=True)
            # Extract title from first # heading
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else fpath.stem
            latex_content = md_to_latex_stub(content, title)
            latex_path = latex_dir / fpath.with_suffix('.tex').name
            latex_path.write_text(latex_content, encoding='utf-8')
            print(f"  LATEX  {latex_path.name}")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"SUMMARY")
    print(f"{'=' * 60}")
    print(f"Files scanned:          {len(files)}")
    print(f"Files with issues:      {len(file_reports)}")
    print(f"Files changed:          {total_changed}")
    print(f"")
    print(f"Escaped underscores:    {total_counts['escaped_underscores']:,}")
    print(f"Bare asterisks:         {total_counts['bare_asterisks']:,}")
    print(f"#P notation:            {total_counts['hash_p']:,}")
    print(f"Total issues:           {sum(total_counts.values()):,}")

    if file_reports and (args.stats or not args.apply):
        print(f"\n{'─' * 60}")
        esc_label = r"\_ "
        print(f"{'File':<45} {esc_label:>5} {'*':>5} {'#P':>4} {'Total':>6}")
        print(f"{'─' * 60}")
        for name, counts, total in sorted(file_reports, key=lambda x: -x[2]):
            print(f"{name:<45} {counts['escaped_underscores']:>5} "
                  f"{counts['bare_asterisks']:>5} {counts['hash_p']:>4} {total:>6}")

    if not args.apply and not args.stats and total_changed > 0:
        print(f"\nDry run complete. Use --apply to write changes.")


if __name__ == '__main__':
    main()
