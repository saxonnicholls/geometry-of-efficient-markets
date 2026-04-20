#!/usr/bin/env python3
"""
fix_display_math.py — Convert $$...$$ display math to fenced ```math``` blocks.

GitHub renders fenced ```math ... ``` blocks more reliably than $$...$$
because they bypass markdown's text/italic parsing entirely. This is
especially important for formulas with subscripts after braces (}_x),
escaped spacing (\!, \,), and complex nested structures.

We handle:
- $$ on its own line ... $$ on its own line  → ```math ... ```
- $$ ... $$ on a single line (single math)    → ```math\n...\n```
- $$X$$ inline display (mid-line)             → leave as $$X$$ if short; else convert

Inline $...$ math is LEFT UNCHANGED (it works fine for inline use).

Usage:
    python3 fix_display_math.py              # dry run
    python3 fix_display_math.py --apply      # apply
"""

import argparse
import re
import sys
from pathlib import Path


def convert_content(content: str) -> tuple:
    """Return (new_content, n_conversions)."""
    lines = content.split("\n")
    out = []
    i = 0
    n = len(lines)
    converted = 0

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Case A: standalone $$ opener on its own line
        if stripped == "$$":
            # Find matching close
            body = []
            j = i + 1
            while j < n and lines[j].strip() != "$$":
                body.append(lines[j])
                j += 1
            if j < n:
                # Convert to fenced ```math block
                out.append("```math")
                out.extend(body)
                out.append("```")
                i = j + 1
                converted += 1
                continue
            # No matching close — leave alone
            out.append(line)
            i += 1
            continue

        # Case B: single-line $$...$$ (whole line is display math)
        m = re.match(r'^(\s*)\$\$(.+)\$\$\s*$', line)
        if m:
            indent, body = m.group(1), m.group(2)
            # Strip any \tag{...} — they don't render in fenced blocks
            # Actually, fenced math SHOULD support \tag, so leave it alone.
            out.append(f"{indent}```math")
            out.append(f"{indent}{body.strip()}")
            out.append(f"{indent}```")
            converted += 1
            i += 1
            continue

        # Case C: multi-line $$...$$ starting on this line, continuing on next
        if stripped.startswith("$$") and not stripped.endswith("$$") and "$$" not in stripped[2:]:
            # Start of multi-line display math where $$ is at start of this line
            first_body = stripped[2:]
            body = [first_body] if first_body else []
            j = i + 1
            while j < n:
                ln = lines[j]
                if ln.strip().endswith("$$") and "$$" not in ln.strip()[:-2]:
                    last_body = ln.rstrip()
                    # Strip trailing $$
                    last_body = last_body[: last_body.rindex("$$")].rstrip()
                    if last_body:
                        body.append(last_body)
                    # Write fenced block
                    out.append("```math")
                    out.extend(body)
                    out.append("```")
                    i = j + 1
                    converted += 1
                    break
                body.append(ln)
                j += 1
            else:
                # No closing match — leave alone
                out.append(line)
                i += 1
            continue

        out.append(line)
        i += 1

    return "\n".join(out), converted


def count_display_math(content: str) -> int:
    """Count $$ pairs in the content."""
    return content.count("$$") // 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--file", default=None)
    parser.add_argument(
        "--root",
        default=".",
    )
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

    total = 0
    changed = 0
    for fp in files:
        content = fp.read_text(encoding="utf-8")
        if "$$" not in content:
            continue
        new_content, n = convert_content(content)
        if n > 0 and new_content != content:
            total += n
            changed += 1
            if args.apply:
                fp.write_text(new_content, encoding="utf-8")
                print(f"  FIXED {fp.name}: {n} display math blocks")
            else:
                print(f"  WOULD FIX {fp.name}: {n} display math blocks")
    print(f"\nTotal converted: {total}, files: {changed}")


if __name__ == "__main__":
    main()
