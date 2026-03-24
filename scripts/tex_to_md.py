#!/usr/bin/env python3
"""Convert LaTeX source files to Markdown with math preserved.

Usage:
    python tex_to_md.py <input.tex> [output.md]

Not perfect -- goal is readable Markdown with correct math for Claude Code.
"""

import re
import sys
from pathlib import Path


def tex_to_md(tex_content: str) -> str:
    """Convert LaTeX content to Markdown, preserving math."""
    text = tex_content

    # Remove preamble (everything before \begin{document})
    doc_match = re.search(r'\\begin\{document\}', text)
    if doc_match:
        text = text[doc_match.end():]

    # Remove \end{document}
    text = re.sub(r'\\end\{document\}', '', text)

    # Remove comments (lines starting with %)
    text = re.sub(r'(?m)^%.*$', '', text)
    # Remove inline comments (but not \%)
    text = re.sub(r'(?<!\\)%.*$', '', text, flags=re.MULTILINE)

    # --- Math environments: convert to $$ blocks ---
    # equation, equation*, align, align*, gather, gather*, multline
    math_envs = ['equation', 'equation\\*', 'align', 'align\\*',
                 'gather', 'gather\\*', 'multline', 'multline\\*',
                 'eqnarray', 'eqnarray\\*']
    for env in math_envs:
        env_escaped = env.replace('*', '\\*')
        pattern = rf'\\begin\{{{env_escaped}\}}(.*?)\\end\{{{env_escaped}\}}'
        text = re.sub(pattern, lambda m: f'\n$$\n{m.group(1).strip()}\n$$\n',
                      text, flags=re.DOTALL)

    # \[ ... \] display math
    text = re.sub(r'\\\[(.*?)\\\]', lambda m: f'\n$$\n{m.group(1).strip()}\n$$\n',
                  text, flags=re.DOTALL)

    # --- Theorem environments → blockquotes ---
    thm_envs = ['theorem', 'lemma', 'proposition', 'corollary', 'definition',
                'remark', 'example', 'proof', 'claim', 'conjecture']
    for env in thm_envs:
        # \begin{theorem}[optional title]
        pattern = rf'\\begin\{{{env}\}}(?:\[(.*?)\])?(.*?)\\end\{{{env}\}}'
        def thm_replace(m, env_name=env):
            title = m.group(1)
            body = m.group(2).strip()
            header = f"**{env_name.capitalize()}**"
            if title:
                header += f" ({title})"
            return f"\n> {header}\n>\n> {body}\n"
        text = re.sub(pattern, thm_replace, text, flags=re.DOTALL)

    # --- Sectioning ---
    text = re.sub(r'\\chapter\*?\{(.*?)\}', r'\n# \1\n', text)
    text = re.sub(r'\\section\*?\{(.*?)\}', r'\n## \1\n', text)
    text = re.sub(r'\\subsection\*?\{(.*?)\}', r'\n### \1\n', text)
    text = re.sub(r'\\subsubsection\*?\{(.*?)\}', r'\n#### \1\n', text)
    text = re.sub(r'\\paragraph\*?\{(.*?)\}', r'\n**\1** ', text)

    # --- Lists ---
    text = re.sub(r'\\begin\{itemize\}', '', text)
    text = re.sub(r'\\end\{itemize\}', '', text)
    text = re.sub(r'\\begin\{enumerate\}', '', text)
    text = re.sub(r'\\end\{enumerate\}', '', text)
    text = re.sub(r'\\item\s*', '\n- ', text)

    # --- Text formatting ---
    text = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', text)
    text = re.sub(r'\\textit\{(.*?)\}', r'*\1*', text)
    text = re.sub(r'\\emph\{(.*?)\}', r'*\1*', text)
    text = re.sub(r'\\texttt\{(.*?)\}', r'`\1`', text)
    text = re.sub(r'\\underline\{(.*?)\}', r'\1', text)

    # --- Citations → [ref:key] ---
    text = re.sub(r'\\cite\{(.*?)\}', r'[ref:\1]', text)

    # --- Cross-references ---
    text = re.sub(r'\\ref\{(.*?)\}', r'[ref:\1]', text)
    text = re.sub(r'\\eqref\{(.*?)\}', r'(ref:\1)', text)
    text = re.sub(r'\\label\{(.*?)\}', r'', text)

    # --- Remove figure/table environments (keep captions) ---
    text = re.sub(r'\\begin\{figure\}.*?\\end\{figure\}', '[Figure omitted]', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{table\}.*?\\end\{table\}', '[Table omitted]', text, flags=re.DOTALL)
    text = re.sub(r'\\includegraphics.*?\{.*?\}', '', text)

    # --- Remove common preamble-like commands that leak through ---
    remove_commands = [
        r'\\usepackage.*?\n', r'\\newcommand.*?\n', r'\\renewcommand.*?\n',
        r'\\def\\.*?\n', r'\\maketitle', r'\\tableofcontents',
        r'\\bibliographystyle\{.*?\}', r'\\bibliography\{.*?\}',
        r'\\appendix', r'\\acknowledgments?',
        r'\\begin\{abstract\}', r'\\end\{abstract\}',
        r'\\title\{.*?\}', r'\\author\{.*?\}', r'\\date\{.*?\}',
        r'\\affiliation\{.*?\}', r'\\email\{.*?\}',
    ]
    for cmd in remove_commands:
        text = re.sub(cmd, '', text, flags=re.DOTALL)

    # --- Footnotes ---
    text = re.sub(r'\\footnote\{(.*?)\}', r' [footnote: \1]', text)

    # --- Clean up ---
    # Remove remaining \begin{...} and \end{...} for unknown environments
    text = re.sub(r'\\begin\{.*?\}', '', text)
    text = re.sub(r'\\end\{.*?\}', '', text)

    # Remove standalone LaTeX commands we don't handle
    text = re.sub(r'\\(?:vspace|hspace|noindent|centering|raggedright|raggedleft|clearpage|newpage|bigskip|medskip|smallskip)\b\*?(?:\{.*?\})?', '', text)

    # Fix multiple blank lines
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    # Fix leading/trailing whitespace on lines
    lines = text.split('\n')
    lines = [line.rstrip() for line in lines]
    text = '\n'.join(lines)

    return text.strip()


def convert_file(input_path: str, output_path: str = None):
    """Convert a .tex file to .md"""
    inp = Path(input_path)
    if output_path is None:
        output_path = str(inp.with_suffix('.md'))

    content = inp.read_text(encoding='utf-8', errors='replace')
    md = tex_to_md(content)

    Path(output_path).write_text(md, encoding='utf-8')
    print(f"Converted: {input_path} -> {output_path}")
    print(f"  Input:  {len(content)} chars")
    print(f"  Output: {len(md)} chars")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    convert_file(input_file, output_file)
