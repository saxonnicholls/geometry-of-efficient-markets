#!/usr/bin/env python3
"""
fix_math_braces.py — Fix GitHub math rendering issues.

GitHub's markdown renderer strips underscores that appear immediately after
a closing brace `}` in math mode (it interprets `}_` as the start of italic).
The fix is to wrap subscripts in braces so `}_` becomes `}_{...}`.

Also handles: `\boxed{...}` with `\;` spacing commands that don't render well,
and `}^x` similar to `}_x` pattern.

Usage:
  python3 fix_math_braces.py                 # dry run
  python3 fix_math_braces.py --apply         # fix in place
"""

import argparse
import os
import re
import sys
from pathlib import Path


# Pattern: `}` followed by `_` followed by a single character (not `{`)
# Replace with `}_{char}`
BARE_SUB_AFTER_BRACE = re.compile(r'\}_([a-zA-Z0-9+\-*])(?![a-zA-Z0-9])')
# Pattern: `}` followed by `^` followed by a single character (not `{`)
BARE_SUP_AFTER_BRACE = re.compile(r'\}\^([a-zA-Z0-9+\-*])(?![a-zA-Z0-9])')

INLINE_MATH = re.compile(r'(?<!\$)\$(?!\$)([^\$\n]+?)\$(?!\$)')
DISPLAY_MATH = re.compile(r'\$\$(.+?)\$\$', re.DOTALL)


def strip_boxed(math: str) -> str:
    """Remove \\boxed{...} including the matching closing brace."""
    while '\\boxed{' in math:
        idx = math.index('\\boxed{')
        # Find the matching brace
        start = idx + len('\\boxed{')
        depth = 1
        i = start
        while i < len(math) and depth > 0:
            if math[i] == '{':
                depth += 1
            elif math[i] == '}':
                depth -= 1
                if depth == 0:
                    # Remove \boxed{ and the matching }
                    math = math[:idx] + math[start:i] + math[i+1:]
                    break
            i += 1
        else:
            # No matching brace found; just strip opening to avoid infinite loop
            math = math[:idx] + math[start:]
    return math


def fix_math_content(math: str) -> str:
    """Apply safe transformations to math content."""
    # Strip `\boxed{...}` → `...` (doesn't render well on GitHub)
    math = strip_boxed(math)
    # `}_x` → `}_{x}` where x is single char
    math = BARE_SUB_AFTER_BRACE.sub(r'}_{\1}', math)
    # `}^x` → `}^{x}` where x is single char
    math = BARE_SUP_AFTER_BRACE.sub(r'}^{\1}', math)
    # Strip `\;` spacing commands (don't render well on GitHub)
    math = math.replace('\\;', ' ')
    # Clean up doubled spaces
    math = re.sub(r'  +', ' ', math)
    return math


def fix_line(line: str) -> str:
    """Fix inline math and single-line display math."""
    # Display math first
    def repl_display(m):
        return '$$' + fix_math_content(m.group(1)) + '$$'

    line = DISPLAY_MATH.sub(repl_display, line)

    # Inline math
    def repl_inline(m):
        return '$' + fix_math_content(m.group(1)) + '$'

    line = INLINE_MATH.sub(repl_inline, line)

    # Remove matching closing `}` of `\boxed{` since we removed the opening
    # This is tricky; for now handle simple cases
    return line


def fix_content(content: str) -> str:
    lines = content.split('\n')
    in_display = False
    fixed = []
    for line in lines:
        stripped = line.strip()
        if stripped == '$$':
            in_display = not in_display
            fixed.append(line)
            continue
        if not in_display and stripped.startswith('$$') and not stripped.endswith('$$'):
            in_display = True
            fixed.append(line[:len(line) - len(line.lstrip())] + '$$'
                         + fix_math_content(stripped[2:]))
            continue
        if in_display and stripped.endswith('$$') and not stripped.startswith('$$'):
            in_display = False
            fixed.append(fix_math_content(stripped[:-2]) + '$$')
            continue
        if in_display:
            fixed.append(fix_math_content(line))
        else:
            fixed.append(fix_line(line))
    out = '\n'.join(fixed)

    # Clean up any trailing `\boxed{` closing braces left unmatched
    # Naive but effective for our case: remove excess closing brace at end of math
    # (This is risky, so skip by default)

    return out


def count_issues(content: str) -> int:
    """Count fixable issues."""
    count = 0
    for m in INLINE_MATH.finditer(content):
        body = m.group(1)
        count += len(BARE_SUB_AFTER_BRACE.findall(body))
        count += len(BARE_SUP_AFTER_BRACE.findall(body))
    for m in DISPLAY_MATH.finditer(content):
        body = m.group(1)
        count += len(BARE_SUB_AFTER_BRACE.findall(body))
        count += len(BARE_SUP_AFTER_BRACE.findall(body))
    in_display = False
    for line in content.split('\n'):
        s = line.strip()
        if s == '$$':
            in_display = not in_display
            continue
        if in_display:
            count += len(BARE_SUB_AFTER_BRACE.findall(line))
            count += len(BARE_SUP_AFTER_BRACE.findall(line))
    # Count \boxed occurrences
    count += content.count('\\boxed{')
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    parser.add_argument('--file', default=None)
    args = parser.parse_args()

    if args.file:
        files = [Path(args.file)]
    else:
        root = Path(args.root)
        files = []
        for d in ('papers', 'navigation', 'book'):
            p = root / d
            if p.exists():
                files.extend(sorted(p.glob('*.md')))
        readme = root / 'README.md'
        if readme.exists():
            files.append(readme)

    total = 0
    changed = 0
    for fp in files:
        content = fp.read_text(encoding='utf-8')
        n = count_issues(content)
        if n == 0:
            continue
        total += n
        fixed = fix_content(content)
        if fixed != content:
            changed += 1
            if args.apply:
                fp.write_text(fixed, encoding='utf-8')
                print(f"  FIXED {fp.name}: {n} issues")
            else:
                print(f"  WOULD FIX {fp.name}: {n} issues")
    print(f"\nTotal issues: {total}, files to change: {changed}")


if __name__ == '__main__':
    main()
