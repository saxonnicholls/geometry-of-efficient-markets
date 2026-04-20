# Math Rendering Convention for GitHub

GitHub's Markdown renderer has specific quirks with LaTeX math. Use this
pattern throughout the monograph to guarantee correct rendering on GitHub.

## The three rules

### 1. Inline math with Markdown-sensitive chars (`_`, `*`, etc.)

Use standard `$...$` delimiters:

```markdown
The Fisher-Rao metric $g^{\rm FR}_{ij}(b) = \delta_{ij}/b_i$ lives on $\Delta_{d-1}$.
```

**Tips for inline math:**
- Always brace subscripts after `}`: write `_{+}` not `_+` (avoids `}_` pattern that confuses GitHub's parser)
- Keep math on a SINGLE line within a bulleted item (don't wrap)
- Avoid inline math inside blockquotes (`>` lines) — GitHub strips underscores in that context
- If you MUST use blockquote content, escape underscores or use display math blocks

### 2. Display math: fenced code blocks

Prefer the fenced `math` code block:

````markdown
```math
\mathrm{Sharpe}^{\ast} = \|H\|_{L^2(M, g_M)}
```
````

This is MORE RELIABLE than `$$...$$` because it bypasses Markdown's
emphasis/escape parsing entirely. Use it for:
- Any formula with complex subscripts/superscripts
- Multi-line expressions
- Anything involving `\boxed`, `\begin{...}`, `\underbrace`, etc.

`$$...$$` works for simple display math but fails on complex formulas
inside lists, quotes, or tables. The fenced form is bulletproof.

### 3. Literal `$` on a math line

If you need a literal dollar sign next to math:

- **In math mode:** escape it as `\$`
- **Mixing with plain text:** wrap the plain dollar as `<span>$</span>`
- **Alternative:** use the word "dollar(s)" — always renders

Example:
```markdown
The option price is <span>$</span>C_{\rm FPS} = $7.24$ dollars.
```

## Known GitHub pitfalls — avoid these

| Pattern | Problem | Fix |
|:---|:---|:---|
| `> $x_i$` | Blockquote eats underscore | Remove `>` markers |
| `$A^{B}_C$` | `}_C` consumed as italic | Use `$A^{B}_{C}$` |
| `$\boxed{...}$` | Inconsistent rendering | Strip the `\boxed{` wrapper |
| `$$\;...\;$$` | `\;` spacing unreliable | Use plain space or `\,` |
| `- **Label:** $x_i$ is\n  $y_j$ continuation` | Multi-line inline math in bullet | Keep on one line |
| `$$\frac{a}{b}$$` inside table | Table cell rendering quirks | Use fenced `math` block outside table |

## Auto-fixers available

- `tools/fix_markdown.py` — fixes escaped underscores, bare asterisks, #P notation
- `tools/fix_math_braces.py` — adds `{}` around bare subscripts after `}`, strips `\boxed`/`\;`
- `tools/fix_blockquote_math.py` — removes `>` markers from blockquotes containing inline math

Run all three after writing any new paper:

```bash
python3 tools/fix_markdown.py --apply
python3 tools/fix_math_braces.py --apply
python3 tools/fix_blockquote_math.py --apply
```

## Testing rendering

Before pushing to GitHub, spot-check a handful of math expressions by:

1. Preview the Markdown file in VS Code (Ctrl+Shift+V / Cmd+Shift+V)
2. Push to a branch and view on GitHub before merging
3. Look for stripped underscores, missing braces, unrendered LaTeX commands

## The rule of thumb

> Use `$...$` for inline, fenced ```math ...``` for display, and avoid
> blockquotes + inline math entirely. If in doubt, reach for display math.
