#!/usr/bin/env python3
"""
fix_ampersand_math.py — Escape bare `&` in math mode as `\\&`.

`&` is a LaTeX alignment character. Inside math (both `$...$` inline and
fenced ```math``` blocks), a bare `&` is interpreted as alignment and
produces the error "& can not be used here". Must be escaped as `\\&`
when the intent is a literal ampersand (e.g., in "S&P 500").

Usage:
    python3 fix_ampersand_math.py              # dry run
    python3 fix_ampersand_math.py --apply      # apply
"""

import argparse
import re
from pathlib import Path


INLINE_MATH = re.compile(r'(?<!\$)\$(?!\$)([^\$\n]+?)\$(?!\$)')


def fix_math(math: str) -> str:
    """Escape bare & in math content."""
    # Replace & not preceded by \ with \&
    return re.sub(r'(?<!\\)&', r'\\&', math)


def process(content: str) -> tuple:
    """Return (new_content, n_fixed)."""
    fixed = 0
    lines = content.split("\n")
    out = []
    in_fenced_math = False

    for line in lines:
        stripped = line.strip()

        # Enter/exit fenced math block
        if stripped == "```math":
            in_fenced_math = True
            out.append(line)
            continue
        if in_fenced_math and stripped == "```":
            in_fenced_math = False
            out.append(line)
            continue

        if in_fenced_math:
            # Fix bare & in fenced math line
            new_line = fix_math(line)
            if new_line != line:
                fixed += 1
            out.append(new_line)
            continue

        # Fix bare & in inline math on this line
        def repl(m):
            body = m.group(1)
            new_body = fix_math(body)
            return f"${new_body}$"

        new_line = INLINE_MATH.sub(repl, line)
        if new_line != line:
            fixed += 1
        out.append(new_line)

    return "\n".join(out), fixed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    root = Path(args.root)
    files = []
    for d in ("papers", "navigation", "book"):
        p = root / d
        if p.exists():
            files.extend(sorted(p.glob("*.md")))
    readme = root / "README.md"
    if readme.exists():
        files.append(readme)

    total = 0
    changed = 0
    for fp in files:
        content = fp.read_text(encoding="utf-8")
        new_content, n = process(content)
        if n > 0 and new_content != content:
            total += n
            changed += 1
            if args.apply:
                fp.write_text(new_content, encoding="utf-8")
                print(f"  FIXED {fp.name}: {n} math lines with bare &")
            else:
                print(f"  WOULD FIX {fp.name}: {n} math lines with bare &")
    print(f"\nTotal lines fixed: {total}, files: {changed}")


if __name__ == "__main__":
    main()
