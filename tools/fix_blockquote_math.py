#!/usr/bin/env python3
"""
fix_blockquote_math.py — Remove blockquote `>` markers from any blockquote
block that contains inline math ($...$).

GitHub strips underscores in inline math inside blockquotes. The fix:
convert the blockquote to regular text (preserving italic if present).

Usage:
    python3 fix_blockquote_math.py            # dry run
    python3 fix_blockquote_math.py --apply    # apply
"""
import argparse
import re
import sys
from pathlib import Path


def process(content: str) -> tuple:
    """Return (new_content, n_blocks_fixed)."""
    lines = content.split("\n")
    n = len(lines)
    out = []
    fixed = 0

    i = 0
    while i < n:
        line = lines[i]
        if line.lstrip().startswith(">"):
            # Collect contiguous blockquote block
            block_start = i
            block = []
            while i < n and (lines[i].lstrip().startswith(">") or lines[i].strip() == ""):
                if lines[i].lstrip().startswith(">"):
                    block.append(lines[i])
                else:
                    # Blank line — end of block
                    break
                i += 1
            # Check if any line contains inline math ($...$ with content between)
            has_math = any(re.search(r'\$[^\$\n]+\$', bl) for bl in block)
            if has_math:
                fixed += 1
                # Strip leading `> ` from each line
                for bl in block:
                    # Remove the leading `>` and optional space
                    stripped = re.sub(r'^\s*>\s?', '', bl)
                    out.append(stripped)
            else:
                # Keep as blockquote
                out.extend(block)
        else:
            out.append(line)
            i += 1
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

    total_fixed = 0
    files_changed = 0
    for fp in files:
        content = fp.read_text(encoding="utf-8")
        new_content, n = process(content)
        if n > 0:
            total_fixed += n
            if new_content != content:
                files_changed += 1
                if args.apply:
                    fp.write_text(new_content, encoding="utf-8")
                    print(f"  FIXED {fp.name}: {n} blockquote-math blocks")
                else:
                    print(f"  WOULD FIX {fp.name}: {n} blockquote-math blocks")
    print(f"\nTotal blocks to fix: {total_fixed}, files: {files_changed}")


if __name__ == "__main__":
    main()
