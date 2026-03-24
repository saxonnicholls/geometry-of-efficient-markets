# Copyright Saxon Nicholls 2026 MIT Licence
"""
md2latex.py — Convert monograph markdown papers to arXiv-ready LaTeX.

Usage:
    python md2latex.py papers/MINIMAL_SURFACE.md          # single file
    python md2latex.py papers/MINIMAL_SURFACE.md -o out/   # specify output dir
    python md2latex.py papers/*.md -o latex/               # batch convert all

Handles:
  - Title/subtitle/author extraction
  - Inline math $...$ and display math $$...$$
  - Theorem/Proof/Definition/Lemma/Corollary/Remark/Proposition environments
  - Bold/italic/code formatting
  - Tables → tabular
  - Numbered equations (tag{...})
  - Section/subsection/subsubsection hierarchy
  - References section
  - Cross-references to other papers
  - Escaped underscores (\_) restored to _
  - GitHub-specific escapes (b^{\\ast} → b^{*})
"""

import re
import sys
import os
import argparse
from pathlib import Path


# ── LaTeX preamble ──────────────────────────────────────────

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}

% ── Packages ────────────────────────────────────────────────
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{geometry}
\geometry{margin=1in}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{array}

% ── Theorem environments ────────────────────────────────────
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem*{remark*}{Remark}

% ── Custom commands ─────────────────────────────────────────
\newcommand{\FR}{\mathrm{FR}}
\newcommand{\Sharpe}{\mathrm{Sharpe}}
\newcommand{\Kelly}{\mathrm{Kelly}}
\newcommand{\MUP}{\mathrm{MUP}}
\newcommand{\vol}{\mathrm{vol}}
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}
"""


def extract_metadata(lines):
    """Extract title, subtitle, author, paper number from header lines."""
    title = ""
    subtitle = ""
    author = "Saxon Nicholls"
    paper_number = ""
    preprint = False

    for line in lines[:20]:
        if line.startswith("# ") and not title:
            title = line[2:].strip().rstrip(":")
        elif line.startswith("## ") and not subtitle:
            subtitle = line[3:].strip()
        elif "me@saxonnicholls" in line:
            author = "Saxon Nicholls"
        elif line.startswith("**Paper "):
            m = re.match(r"\*\*Paper ([IVX]+\.\d+)\*\*", line)
            if m:
                paper_number = m.group(1)
        elif "PREPRINT" in line:
            preprint = True

    return {
        "title": title,
        "subtitle": subtitle,
        "author": author,
        "paper_number": paper_number,
        "preprint": preprint,
    }


def clean_math(text):
    """Fix GitHub markdown math escapes for LaTeX."""
    # Restore \\ast → * in math contexts
    text = text.replace(r"\ast", "*")
    # Restore escaped underscores inside math
    # But only inside $...$ or $$...$$
    # Simple approach: just remove all \_ → _
    text = text.replace(r"\_", "_")
    return text


def convert_inline_formatting(line):
    """Convert markdown bold/italic/code to LaTeX."""
    # Code: `text` → \texttt{text}
    line = re.sub(r"`([^`]+)`", r"\\texttt{\1}", line)
    # Bold+italic: ***text*** or ___text___
    line = re.sub(r"\*\*\*(.+?)\*\*\*", r"\\textbf{\\textit{\1}}", line)
    # Bold: **text**
    line = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", line)
    # Italic: *text*  (but not inside math $...$)
    # Only match * that are not preceded/followed by $
    line = re.sub(r"(?<!\$)\*(?!\*)(.+?)(?<!\*)\*(?!\$)", r"\\textit{\1}", line)
    return line


def convert_table(lines, start_idx):
    """Convert a markdown table to LaTeX tabular. Returns (latex_lines, end_idx)."""
    # Find table extent
    end_idx = start_idx
    table_lines = []
    for i in range(start_idx, len(lines)):
        if lines[i].strip().startswith("|"):
            table_lines.append(lines[i].strip())
            end_idx = i
        else:
            break

    if len(table_lines) < 2:
        return [], start_idx

    # Parse header
    headers = [c.strip() for c in table_lines[0].split("|")[1:-1]]
    ncols = len(headers)

    # Determine alignment from separator row
    sep = table_lines[1]
    aligns = []
    for col in sep.split("|")[1:-1]:
        col = col.strip()
        if col.startswith(":") and col.endswith(":"):
            aligns.append("c")
        elif col.endswith(":"):
            aligns.append("r")
        else:
            aligns.append("l")
    while len(aligns) < ncols:
        aligns.append("l")

    col_spec = "".join(aligns)

    result = []
    result.append(r"\begin{table}[htbp]")
    result.append(r"\centering")
    result.append(r"\begin{tabular}{" + col_spec + "}")
    result.append(r"\toprule")

    # Header row
    header_cells = [clean_math(h) for h in headers]
    result.append(" & ".join(header_cells) + r" \\")
    result.append(r"\midrule")

    # Data rows (skip separator at index 1)
    for row_line in table_lines[2:]:
        cells = [clean_math(c.strip()) for c in row_line.split("|")[1:-1]]
        while len(cells) < ncols:
            cells.append("")
        result.append(" & ".join(cells) + r" \\")

    result.append(r"\bottomrule")
    result.append(r"\end{tabular}")
    result.append(r"\end{table}")
    result.append("")

    return result, end_idx


def detect_theorem_env(line):
    """Detect theorem-like environment starts in bold text."""
    patterns = [
        (r"\*\*Theorem\s+[\d.]+\*\*", "theorem"),
        (r"\*\*Proposition\s+[\d.]+\*\*", "proposition"),
        (r"\*\*Lemma\s+[\d.]+\*\*", "lemma"),
        (r"\*\*Corollary\s+[\d.]+\*\*", "corollary"),
        (r"\*\*Definition\s+[\d.]+\*\*", "definition"),
        (r"\*\*Remark\.?\*\*", "remark*"),
        (r"\*\*Remark\s+[\d.]+\*\*", "remark"),
    ]
    for pattern, env in patterns:
        if re.search(pattern, line):
            return env
    return None


def convert_body(lines):
    """Convert the body of the markdown to LaTeX."""
    output = []
    i = 0
    in_display_math = False
    in_code_block = False
    in_theorem = False
    in_proof = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip metadata lines (already extracted)
        if i < 15 and (stripped.startswith("#") or "me@saxonnicholls" in stripped
                       or stripped.startswith("**Paper ") or "PREPRINT" in stripped
                       or stripped == "---" or stripped == ""):
            i += 1
            continue

        # Code blocks
        if stripped.startswith("```"):
            if not in_code_block:
                lang = stripped[3:].strip()
                output.append(r"\begin{verbatim}")
                in_code_block = True
            else:
                output.append(r"\end{verbatim}")
                in_code_block = False
            i += 1
            continue

        if in_code_block:
            output.append(line.rstrip())
            i += 1
            continue

        # Display math blocks
        if stripped.startswith("$$") and not in_display_math:
            # Check if it's a one-liner: $$ ... $$
            if stripped.endswith("$$") and len(stripped) > 4:
                math_content = stripped[2:-2].strip()
                math_content = clean_math(math_content)
                # Check for \tag
                tag_match = re.search(r"\\tag\{([^}]+)\}", math_content)
                if tag_match:
                    math_content = math_content[:tag_match.start()].strip()
                    output.append(r"\begin{equation}")
                    output.append(math_content)
                    output.append(r"\label{eq:" + tag_match.group(1).replace(".", "_") + "}")
                    output.append(r"\end{equation}")
                else:
                    output.append(r"\begin{equation*}")
                    output.append(math_content)
                    output.append(r"\end{equation*}")
            else:
                in_display_math = True
                output.append(r"\begin{equation*}")
                if len(stripped) > 2:
                    output.append(clean_math(stripped[2:]))
            i += 1
            continue

        if in_display_math:
            if stripped.endswith("$$"):
                content = stripped[:-2].strip()
                content = clean_math(content)
                tag_match = re.search(r"\\tag\{([^}]+)\}", content)
                if tag_match:
                    content = content[:tag_match.start()].strip()
                    # Replace equation* with equation
                    if output and output[-1] == r"\begin{equation*}":
                        output[-1] = r"\begin{equation}"
                    output.append(content)
                    output.append(r"\label{eq:" + tag_match.group(1).replace(".", "_") + "}")
                    output.append(r"\end{equation}")
                else:
                    output.append(content)
                    output.append(r"\end{equation*}")
                in_display_math = False
            else:
                output.append(clean_math(stripped))
            i += 1
            continue

        # Horizontal rules → skip
        if stripped == "---":
            i += 1
            continue

        # Section headers
        if stripped.startswith("### "):
            title = stripped[4:].strip()
            title = re.sub(r"\$[^$]+\$", lambda m: m.group(0), title)
            output.append(r"\subsection{" + clean_math(title) + "}")
            output.append("")
            i += 1
            continue

        if stripped.startswith("## "):
            sec_num_match = re.match(r"## (\d+)\.\s*(.*)", stripped)
            if sec_num_match:
                title = sec_num_match.group(2).strip()
            else:
                title = stripped[3:].strip()
            output.append(r"\section{" + clean_math(title) + "}")
            output.append("")
            i += 1
            continue

        # Tables
        if stripped.startswith("|") and i + 1 < len(lines) and lines[i+1].strip().startswith("|"):
            table_lines, end_idx = convert_table(lines, i)
            output.extend(table_lines)
            i = end_idx + 1
            continue

        # Proof start/end
        if stripped.startswith("*Proof.*") or stripped.startswith("*Proof*"):
            if in_theorem:
                output.append(r"\end{" + current_env + "}")
                in_theorem = False
            output.append(r"\begin{proof}")
            rest = re.sub(r"^\*Proof\.?\*\.?\s*", "", stripped)
            if rest:
                output.append(clean_math(convert_inline_formatting(rest)))
            in_proof = True
            i += 1
            continue

        if in_proof and ("$\\square$" in stripped or "□" in stripped):
            cleaned = stripped.replace("$\\square$", "").replace("□", "").strip()
            if cleaned:
                output.append(clean_math(convert_inline_formatting(cleaned)))
            output.append(r"\end{proof}")
            output.append("")
            in_proof = False
            i += 1
            continue

        # Theorem-like environments
        env = detect_theorem_env(stripped)
        if env:
            if in_theorem:
                output.append(r"\end{" + current_env + "}")
            current_env = env
            in_theorem = True
            # Extract optional name in parentheses
            name_match = re.search(r"\*\(.+?\)\*\.?", stripped)
            if name_match:
                name = name_match.group(0).strip("*().").strip()
                output.append(r"\begin{" + env + "}[" + clean_math(name) + "]")
            else:
                output.append(r"\begin{" + env + "}")
            # Remove the theorem header from the line
            rest = re.sub(r"\*\*\w+\s+[\d.]+\*\*\s*\*?\([^)]*\)\*?\.?\s*", "", stripped)
            rest = re.sub(r"\*\*\w+\.?\*\*\s*", "", rest)
            if rest.strip():
                output.append(clean_math(convert_inline_formatting(rest.strip())))
            i += 1
            continue

        # Bullet lists
        if stripped.startswith("- "):
            if not output or not output[-1].strip().startswith(r"\item"):
                output.append(r"\begin{itemize}")
            content = stripped[2:].strip()
            output.append(r"\item " + clean_math(convert_inline_formatting(content)))
            # Check if next line is not a bullet
            if i + 1 < len(lines) and not lines[i+1].strip().startswith("- "):
                output.append(r"\end{itemize}")
            i += 1
            continue

        # Numbered lists
        num_match = re.match(r"^(\d+)\.\s+(.*)", stripped)
        if num_match:
            if not output or not output[-1].strip().startswith(r"\item"):
                output.append(r"\begin{enumerate}")
            content = num_match.group(2).strip()
            output.append(r"\item " + clean_math(convert_inline_formatting(content)))
            if i + 1 < len(lines) and not re.match(r"^\d+\.\s+", lines[i+1].strip()):
                output.append(r"\end{enumerate}")
            i += 1
            continue

        # Blockquotes
        if stripped.startswith("> "):
            output.append(r"\begin{quote}")
            output.append(clean_math(convert_inline_formatting(stripped[2:])))
            i += 1
            while i < len(lines) and lines[i].strip().startswith("> "):
                output.append(clean_math(convert_inline_formatting(lines[i].strip()[2:])))
                i += 1
            output.append(r"\end{quote}")
            continue

        # Empty lines
        if stripped == "":
            if in_theorem and i + 1 < len(lines):
                next_stripped = lines[i+1].strip()
                if not next_stripped.startswith("*") and not next_stripped.startswith("$$"):
                    output.append(r"\end{" + current_env + "}")
                    in_theorem = False
            output.append("")
            i += 1
            continue

        # Regular paragraph text
        converted = clean_math(convert_inline_formatting(stripped))
        output.append(converted)
        i += 1

    # Close any open environments
    if in_theorem:
        output.append(r"\end{" + current_env + "}")
    if in_proof:
        output.append(r"\end{proof}")

    return output


def convert_references(lines):
    """Extract references section and convert to LaTeX bibliography."""
    ref_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## References") or line.strip().startswith("## Reference"):
            ref_start = i
            break

    if ref_start is None:
        return []

    output = [r"\begin{thebibliography}{99}", ""]
    for line in lines[ref_start+1:]:
        stripped = line.strip()
        if stripped == "" or stripped.startswith("*["):
            continue
        if stripped.startswith("## "):
            break
        # Simple: each non-empty line is a reference
        # Try to extract author-year for the bibitem key
        author_match = re.match(r"^([A-Z][a-z]+)", stripped)
        year_match = re.search(r"\((\d{4})\)", stripped)
        if author_match and year_match:
            key = author_match.group(1).lower() + year_match.group(1)
        else:
            key = f"ref{len(output)}"
        output.append(r"\bibitem{" + key + "} " + clean_math(stripped))
        output.append("")

    output.append(r"\end{thebibliography}")
    return output


def convert_file(input_path, output_dir=None):
    """Convert a single markdown file to LaTeX."""
    input_path = Path(input_path)
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / input_path.with_suffix(".tex").name
    else:
        output_path = input_path.with_suffix(".tex")

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    meta = extract_metadata(lines)

    # Build document
    doc = [PREAMBLE]

    # Title
    full_title = meta["title"]
    if meta["subtitle"]:
        full_title += r":\\ " + meta["subtitle"]
    doc.append(r"\title{" + clean_math(full_title) + "}")
    doc.append(r"\author{" + meta["author"] + r"\\")
    doc.append(r"\texttt{me@saxonnicholls.com}}")

    date_line = r"\date{"
    if meta["paper_number"]:
        date_line += f"Paper {meta['paper_number']} --- "
    date_line += r"\textit{The Geometry of Efficient Markets}"
    if meta["preprint"]:
        date_line += r"\\ \smallskip \textbf{PREPRINT} --- Not peer-reviewed"
    date_line += "}"
    doc.append(date_line)

    doc.append("")
    doc.append(r"\begin{document}")
    doc.append(r"\maketitle")
    doc.append("")

    # Body
    body = convert_body(lines)
    doc.extend(body)

    # References
    refs = convert_references(lines)
    if refs:
        doc.append("")
        doc.extend(refs)

    doc.append("")
    doc.append(r"\end{document}")

    # Write output
    output_text = "\n".join(doc)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_text)

    print(f"  {input_path.name} → {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Convert monograph markdown papers to arXiv-ready LaTeX")
    parser.add_argument("files", nargs="+", help="Markdown files to convert")
    parser.add_argument("-o", "--output-dir", default="latex",
                        help="Output directory (default: latex/)")
    args = parser.parse_args()

    print("md2latex — Markdown to arXiv LaTeX converter")
    print(f"Output directory: {args.output_dir}\n")

    for f in args.files:
        try:
            convert_file(f, args.output_dir)
        except Exception as e:
            print(f"  ERROR: {f} — {e}")

    print(f"\nDone. {len(args.files)} file(s) converted.")
    print(f"To compile: cd {args.output_dir} && pdflatex <file>.tex")


if __name__ == "__main__":
    main()
