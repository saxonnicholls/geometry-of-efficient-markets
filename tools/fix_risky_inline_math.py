#!/usr/bin/env python3
"""
fix_risky_inline_math.py — Convert risky inline `$...$` math to fenced
```math``` blocks.

GitHub's markdown renderer strips backslash-escape sequences inside
inline `$...$` math in many contexts. Specifically it mangles:
  - `\\{` and `\\}` (literal braces)    — becomes `{` `}` or eaten
  - `\\,` (thin space)                  — backslash stripped
  - `\\!` (negative space)              — backslash stripped
  - `\\|` (|| delimiter)                — backslash stripped
  - `}_{...}` and `}^{...}` patterns    — underscore sometimes stripped

The ONLY reliable fix is to move such math to a fenced ```math``` block,
which GitHub does NOT process through its text pipeline.

This tool finds inline math that is LIKELY to render poorly and either:
  1. Promotes it to a display math block on its own line, OR
  2. Tags it with a comment noting it should be promoted

Default: REPORT ONLY. Use --apply to rewrite.

Criteria for "risky" inline math:
  - Contains \\,  \\!  \\{  \\}  \\|
  - Contains more than one `}_{` or `}^{` pattern
  - Length > 60 chars

Usage:
    python3 fix_risky_inline_math.py               # list risky inline math
    python3 fix_risky_inline_math.py --apply       # rewrite to display math
"""

import argparse
import re
from pathlib import Path


# Match `$...$` inline math that is NOT part of `$$...$$`
INLINE_MATH = re.compile(r'(?<!\$)\$(?!\$)([^\$\n]+?)\$(?!\$)')

RISKY_PATTERNS = [
    re.compile(r'\\\{'),    # \{
    re.compile(r'\\\}'),    # \}
    re.compile(r'\\,'),      # \,
    re.compile(r'\\!'),      # \!
    re.compile(r'\\\|'),    # \|
]


def is_risky(math: str) -> bool:
    """Determine if inline math is likely to mis-render on GitHub."""
    # Has backslash-escape sequence
    for p in RISKY_PATTERNS:
        if p.search(math):
            return True
    # Has multiple `}_{` or `}^{` patterns (complex nested subscripts)
    n_nested = len(re.findall(r'\}_\{', math)) + len(re.findall(r'\}\^\{', math))
    if n_nested >= 2:
        return True
    # Very long (heuristic)
    if len(math) > 80:
        return True
    return False


def promote_line_inline_math(line: str) -> tuple:
    """Detect inline math in line. Return (new_line, extracted_blocks)
    where extracted_blocks is a list of (sentinel, math_content) pairs
    for math that should be promoted to its own display block.

    Strategy: if the line contains a SINGLE risky inline math and that
    math fills most of the line, convert the whole line to a fenced block.
    Otherwise leave the line alone (too complex to safely rewrite).
    """
    matches = list(INLINE_MATH.finditer(line))
    risky = [m for m in matches if is_risky(m.group(1))]
    if not risky:
        return line, []

    # If a single risky match is the whole line (apart from whitespace),
    # convert the line to a fenced math block.
    if len(risky) == 1 and len(matches) == 1:
        m = risky[0]
        before = line[: m.start()].strip()
        after = line[m.end() :].strip()
        # If it's essentially alone on the line (maybe with trailing .)
        if not before and after in ("", ".", ",", ":", ";"):
            return None, [m.group(1) + after]

    # Otherwise report but don't modify — too risky to auto-rewrite
    return line, [m.group(1) for m in risky]


def process(content: str, apply: bool = False) -> tuple:
    lines = content.split("\n")
    out = []
    reports = []

    in_code = False
    in_math = False
    for idx, line in enumerate(lines):
        stripped = line.strip()

        # Track code fences
        if stripped.startswith("```"):
            # Check if it's a ```math fence
            if stripped == "```math":
                in_math = True
                out.append(line)
                continue
            if in_math and stripped == "```":
                in_math = False
                out.append(line)
                continue
            in_code = not in_code
            out.append(line)
            continue
        if in_code or in_math:
            out.append(line)
            continue

        new_line, found = promote_line_inline_math(line)
        if apply and new_line is None:
            # Whole-line replacement with fenced block
            math = found[0]
            out.append("```math")
            out.append(math)
            out.append("```")
            reports.append((idx + 1, "PROMOTED", math))
            continue
        out.append(line)
        if found:
            for m in found:
                reports.append((idx + 1, "RISKY", m))

    return "\n".join(out), reports


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--file", default=None)
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    if args.file:
        files = [Path(args.file)]
    else:
        root = Path(args.root)
        files = []
        for d in ("papers", "navigation", "book"):
            p = root / d
            if p.exists():
                files.extend(sorted(p.glob("*.md")))
        readme = root / "README.md"
        if readme.exists():
            files.append(readme)

    total_risky = 0
    total_promoted = 0
    files_changed = 0

    for fp in files:
        content = fp.read_text(encoding="utf-8")
        new_content, reports = process(content, apply=args.apply)
        if not reports:
            continue
        n_risky = sum(1 for _, k, _ in reports if k == "RISKY")
        n_promoted = sum(1 for _, k, _ in reports if k == "PROMOTED")
        total_risky += n_risky
        total_promoted += n_promoted
        if args.apply and new_content != content:
            fp.write_text(new_content, encoding="utf-8")
            files_changed += 1
            print(f"  FIXED {fp.name}: {n_promoted} promoted, {n_risky} flagged (manual)")
        elif not args.apply:
            print(f"  {fp.name}: {n_risky} risky inline math found")
            # Show first 3 examples
            for ln, kind, math in reports[:3]:
                m = (math[:60] + "...") if len(math) > 60 else math
                print(f"    line {ln}: ${m}$")

    if args.apply:
        print(f"\nTotal: {total_promoted} promoted to display math, "
              f"{total_risky} flagged for manual review, "
              f"{files_changed} files changed")
    else:
        print(f"\nTotal risky inline math: {total_risky}. Run with --apply.")


if __name__ == "__main__":
    main()
