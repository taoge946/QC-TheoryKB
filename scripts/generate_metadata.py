#!/usr/bin/env python3
"""
generate_metadata.py — QC-TheoryKB v2.0 Migration Tool
Parses all key_formulas.md files and generates YAML metadata entries.

Usage:
    python generate_metadata.py                    # Generate all entries
    python generate_metadata.py --dry-run          # Print parsed entries to stdout
    python generate_metadata.py --topic 04         # Process single topic
    python generate_metadata.py --dump-aliases     # Generate legacy_aliases.yaml
    python generate_metadata.py --dump-citations   # Generate citations.yaml skeleton
"""

import re
import os
import sys
import yaml
import argparse
from pathlib import Path
from dataclasses import dataclass, field, asdict

KB_ROOT = Path(__file__).parent.parent
V2_DIR = KB_ROOT / "v2"
ENTRIES_DIR = V2_DIR / "entries"

# ─── Domain Mapping ───────────────────────────────────────────────────
DOMAIN_MAP = {
    "01_linear_algebra":           ("MATH", "LINALG"),
    "02_quantum_mechanics":        ("QC",   "QM"),
    "03_quantum_info_theory":      ("QC",   "QINFO"),
    "04_quantum_error_correction": ("QC",   "QEC"),
    "05_variational_quantum":      ("QC",   "VQA"),
    "06_group_theory":             ("MATH", "GROUP"),
    "07_graph_theory":             ("MATH", "GRAPH"),
    "08_topology":                 ("QC",   "TOPO"),
    "10_optimization":             ("MATH", "OPT"),
    "11_ml_theory":                ("ML",   "THEORY"),
    "12_zx_calculus":              ("QC",   "ZX"),
    "13_quantum_compilation":      ("QC",   "COMPILATION"),
    "14_scheduling_theory":        ("MATH", "SCHEDULING"),
    "15_quantum_hardware":         ("QC",   "HARDWARE"),
    "16_statistical_mechanics":    ("PHYS", "STATMECH"),
    "17_experimental_methods":     ("STATS","EXPERIMENT"),
    "18_proof_techniques":         ("MATH", "PROOFTOOL"),
}

# ML subdomain inference from derivation filename
ML_SUBDOMAIN_MAP = {
    "diffusion": "DIFFUSION", "score_matching": "DIFFUSION", "langevin": "DIFFUSION",
    "discrete_diffusion": "DIFFUSION", "discrete_score": "DIFFUSION",
    "flow_matching": "FLOW",
    "gnn": "GNN", "wl_test": "GNN",
    "reinforcement": "RL",
    "elbo": "GEN", "generative_models": "GEN", "variational_inference": "GEN",
    "attention": "ATTENTION", "optimization_algorithms": "OPT",
}

# Manual overrides for well-known formulas
NAME_OVERRIDES = {
    "F4.1": "KNILL_LAFLAMME",
    "F4.4": "CSS_CONSTRUCTION",
    "F4.6": "THRESHOLD_THEOREM",
    "F3.13": "FUCHS_VAN_DE_GRAAF",
    "F3.20": "DATA_PROCESSING_INEQUALITY",
    "F3.23": "HOLEVO_BOUND",
    "F10.12": "GW_MAXCUT",
    "F10.13": "QUBO_ISING_MAPPING",
    "F11.1": "ELBO",
    "F11.4": "DDPM_SIMPLE_LOSS",
    "F11.6": "DENOISING_SCORE_MATCHING",
    "F11.8": "FORWARD_REVERSE_SDE",
    "F11.31": "GIN_UPDATE",
    "F11.32": "GNN_LEQ_1WL",
    "F11.37": "CFM_EQUALS_FM",
    "F11.49": "REINFORCE_GRADIENT",
    "F5.1": "VARIATIONAL_PRINCIPLE",
    "F5.3": "PARAMETER_SHIFT_RULE",
}

# ─── Regex Patterns ───────────────────────────────────────────────────
FCODE_RE = re.compile(r'^#{2,3}\s+(F\d+\.\d+):?\s+(.+?)$', re.MULTILINE)
LATEX_RE = re.compile(r'\$\$([\s\S]+?)\$\$')
SOURCE_RE = re.compile(r'^\*\*(Source|来源)\*\*:\s*(.+?)$', re.MULTILINE)
DERIV_BRACKET_RE = re.compile(r'\[derivations/([^\]]+)\]')
DERIV_BACKTICK_RE = re.compile(r'`derivations/([^`]+)`')
CHINESE_PARENS_RE = re.compile(r'\(([^)]*[\u4e00-\u9fff][^)]*)\)')
INLINE_CITATION_RE = re.compile(r'\*\*\[.+?\]\*\*')

# Claim type keyword matching
CLAIM_KEYWORDS = {
    "CORRECTNESS": ["condition", "criterion", "if and only if", "iff", "validity", "correct"],
    "BOUND.UPPER": ["upper bound", "at most", "leq", "ceiling", "不超过"],
    "BOUND.LOWER": ["lower bound", "at least", "geq", "floor"],
    "EQUIVALENCE": ["equivalence", "isomorphism", "correspondence", "mapping", "等价"],
    "CONVERGENCE": ["convergence", "converge", "limit", "rate"],
    "IDENTITY": ["identity", "definition", "decomposition", "分解", "定义"],
}

# ─── Data Classes ─────────────────────────────────────────────────────
@dataclass
class ParsedFormula:
    fcode: str
    topic_dir: str
    name_en: str
    name_zh: str | None
    latex: str
    description: str
    source_raw: str
    derivation_files: list[str]
    citations: list[str]
    semantic_id: str = ""
    domain: str = ""
    subdomain: str = ""
    claim_type: str = "DERIVATION"
    artifact_type: str = "DERIVATION"

# ─── Parsing Functions ────────────────────────────────────────────────
def find_key_formulas_files(topic_filter: str | None = None) -> list[tuple[str, Path]]:
    """Find all key_formulas.md files, optionally filtered by topic number."""
    results = []
    for d in sorted(KB_ROOT.iterdir()):
        if not d.is_dir() or not d.name[0:2].isdigit():
            continue
        if topic_filter and not d.name.startswith(topic_filter):
            continue
        kf = d / "key_formulas.md"
        if kf.exists():
            results.append((d.name, kf))
    return results


def split_into_blocks(text: str) -> list[str]:
    """Split key_formulas.md content into formula blocks on --- separators."""
    blocks = re.split(r'\n---\n', text)
    return [b.strip() for b in blocks if b.strip()]


def parse_source_line(raw: str) -> tuple[list[str], list[str]]:
    """Parse source line into (derivation_files, citation_strings)."""
    derivation_files = []
    citations = []

    for m in DERIV_BRACKET_RE.finditer(raw):
        derivation_files.append(m.group(1))
    for m in DERIV_BACKTICK_RE.finditer(raw):
        derivation_files.append(m.group(1))

    # Clean raw to extract citation text
    cleaned = raw
    cleaned = DERIV_BRACKET_RE.sub('', cleaned)
    cleaned = DERIV_BACKTICK_RE.sub('', cleaned)
    cleaned = re.sub(r'\[references/[^\]]+\]', '', cleaned)
    # Remove bold markdown around citations
    cleaned = re.sub(r'\*\*\[', '[', cleaned)
    cleaned = re.sub(r'\]\*\*', ']', cleaned)
    # Split on pipe or em-dash
    cleaned = cleaned.replace('|', ';').replace('—', ';').replace('–', ';')

    for part in cleaned.split(';'):
        part = part.strip().strip('[]').strip()
        if part and len(part) > 3 and not part.startswith('derivations/'):
            citations.append(part)

    return derivation_files, citations


def infer_ml_subdomain(deriv_file: str) -> str:
    """Infer ML subdomain from derivation filename."""
    fname = deriv_file.lower()
    for key, subdomain in ML_SUBDOMAIN_MAP.items():
        if key in fname:
            return subdomain
    return "THEORY"


def generate_object_name(fcode: str, heading: str) -> str:
    """Generate UPPER_SNAKE_CASE object name from heading."""
    if fcode in NAME_OVERRIDES:
        return NAME_OVERRIDES[fcode]

    name = CHINESE_PARENS_RE.sub('', heading).strip()
    name = INLINE_CITATION_RE.sub('', name).strip()
    # Remove trailing punctuation
    name = name.rstrip('.:;,')

    stopwords = {'the', 'a', 'an', 'of', 'for', 'and', 'in', 'on', 'with', 'from', 'to', 'via', 'as', 'by'}
    words = [w for w in re.split(r'[\s/,\-]+', name)
             if w.lower() not in stopwords and w and w[0].isalpha()]
    words = words[:4]
    result = '_'.join(w.upper() for w in words)
    result = re.sub(r'[^A-Z0-9_]', '', result)
    return result or "UNNAMED"


def infer_claim_type(heading: str, description: str) -> str:
    """Infer claim type from heading + description keywords."""
    text = (heading + " " + description).lower()
    for ctype, keywords in CLAIM_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return ctype
    return "DERIVATION"


def infer_artifact_type(heading: str) -> str:
    """Infer artifact type from heading."""
    h = heading.lower()
    if any(w in h for w in ["theorem", "conditions", "criterion", "bound", "inequality"]):
        return "THEOREM"
    if "lemma" in h:
        return "LEMMA"
    if any(w in h for w in ["definition", "def."]):
        return "DEFINITION"
    if any(w in h for w in ["identity", "rule", "properties", "relation", "formula"]):
        return "IDENTITY"
    return "DERIVATION"


def parse_block(block: str, topic_dir: str) -> ParsedFormula | None:
    """Parse a single formula block into a ParsedFormula."""
    fcode_match = FCODE_RE.search(block)
    if not fcode_match:
        return None

    fcode = fcode_match.group(1)
    heading = fcode_match.group(2).strip()

    # Extract Chinese name
    zh_match = CHINESE_PARENS_RE.search(heading)
    name_zh = zh_match.group(1) if zh_match else None
    name_en = CHINESE_PARENS_RE.sub('', heading).strip()
    name_en = INLINE_CITATION_RE.sub('', name_en).strip().rstrip('.:;,')

    # Extract LaTeX
    latex_matches = LATEX_RE.findall(block)
    latex = latex_matches[0].strip() if latex_matches else ""

    # Extract source line
    source_match = SOURCE_RE.search(block)
    source_raw = source_match.group(2).strip() if source_match else ""

    # Description: text between heading and source (excluding LaTeX)
    desc_start = fcode_match.end()
    desc_end = source_match.start() if source_match else len(block)
    desc_text = block[desc_start:desc_end]
    # Remove LaTeX blocks from description
    desc_text = LATEX_RE.sub('', desc_text).strip()
    # Remove markdown formatting
    desc_text = re.sub(r'\*\*[^*]+\*\*', '', desc_text)
    desc_text = desc_text[:500]  # Truncate

    # Parse source
    derivation_files, citations = parse_source_line(source_raw) if source_raw else ([], [])

    # Generate semantic ID
    domain, subdomain = DOMAIN_MAP.get(topic_dir, ("UNKNOWN", "UNKNOWN"))
    if topic_dir == "11_ml_theory" and derivation_files:
        subdomain = infer_ml_subdomain(derivation_files[0])

    obj_name = generate_object_name(fcode, heading)
    semantic_id = f"{domain}.{subdomain}.{obj_name}.01"

    return ParsedFormula(
        fcode=fcode,
        topic_dir=topic_dir,
        name_en=name_en,
        name_zh=name_zh,
        latex=latex,
        description=desc_text,
        source_raw=source_raw,
        derivation_files=derivation_files,
        citations=citations,
        semantic_id=semantic_id,
        domain=f"{domain}.{subdomain}",
        subdomain=subdomain,
        claim_type=infer_claim_type(heading, desc_text),
        artifact_type=infer_artifact_type(heading),
    )


def parse_key_formulas(topic_dir: str, filepath: Path) -> list[ParsedFormula]:
    """Parse entire key_formulas.md file."""
    text = filepath.read_text(encoding='utf-8')
    blocks = split_into_blocks(text)
    results = []
    for block in blocks:
        formula = parse_block(block, topic_dir)
        if formula:
            results.append(formula)
    return results


# ─── YAML Output ──────────────────────────────────────────────────────
def formula_to_yaml(f: ParsedFormula) -> str:
    """Convert ParsedFormula to YAML string."""
    entry = {
        'id': f.semantic_id,
        'legacy_alias': f.fcode,
        'version': '01',
        'claim_type': f.claim_type,
        'domain': f.domain,
        'artifact_type': f.artifact_type,
        'name_en': f.name_en,
        'name_zh': f.name_zh,
        'latex': f.latex,
        'derivation_files': [f"{f.topic_dir}/derivations/{d}" if '/' not in d else f"{f.topic_dir}/{d}"
                             for d in f.derivation_files],
        'citations': [{'raw': c, 'verified': False} for c in f.citations],
        'used_to_prove': [],
        'depends_on': [],
        'proof_pattern': None,
        'assumptions': [],
        'failure_modes': [],
        'dont_use_when': [],
        'auto_generated': True,
        'review_status': 'UNREVIEWED',
        'topic_dir': f.topic_dir,
    }
    return yaml.dump(entry, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)


def write_entry(f: ParsedFormula, dry_run: bool = False):
    """Write a single YAML entry file."""
    # Sanitize filename
    fname = f.semantic_id.replace('.', '_') + ".yaml"
    content = f"# {f.semantic_id}\n# Auto-generated from {f.topic_dir}/key_formulas.md ({f.fcode})\n\n"
    content += formula_to_yaml(f)

    if dry_run:
        print(f"--- {f.fcode} → {f.semantic_id} ---")
        print(content)
        return

    outpath = ENTRIES_DIR / fname
    outpath.write_text(content, encoding='utf-8')


# ─── Dump Functions ───────────────────────────────────────────────────
def dump_aliases(all_formulas: list[ParsedFormula], dry_run: bool = False):
    """Generate legacy_aliases.yaml."""
    aliases = {f.fcode: f.semantic_id for f in all_formulas}
    content = yaml.dump({'aliases': aliases}, default_flow_style=False, sort_keys=True)

    if dry_run:
        print(content)
        return

    outpath = V2_DIR / "indexes" / "legacy_aliases.yaml"
    outpath.write_text(f"# Legacy F-code → Semantic ID mapping\n# Auto-generated\n\n{content}", encoding='utf-8')
    print(f"Wrote {outpath} ({len(aliases)} aliases)")


def dump_citations(all_formulas: list[ParsedFormula], dry_run: bool = False):
    """Generate citations.yaml skeleton from parsed citation strings."""
    all_citations = set()
    for f in all_formulas:
        for c in f.citations:
            all_citations.add(c)

    # Group by first author/keyword
    skeleton = {"sources": {}}
    for i, c in enumerate(sorted(all_citations)):
        key = f"source_{i:03d}"
        skeleton["sources"][key] = {
            "raw_string": c,
            "type": "unclassified",
            "verified": False,
        }

    content = yaml.dump(skeleton, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)

    if dry_run:
        print(content[:3000])
        print(f"\n... ({len(all_citations)} unique citation strings)")
        return

    outpath = V2_DIR / "sources" / "citations_skeleton.yaml"
    outpath.write_text(f"# Citation skeleton — needs manual review\n# {len(all_citations)} unique strings\n\n{content}",
                       encoding='utf-8')
    print(f"Wrote {outpath} ({len(all_citations)} citations)")


# ─── Main ─────────────────────────────────────────────────────────────
def main():
    # Fix Windows stdout encoding
    import io
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

    parser = argparse.ArgumentParser(description="Generate v2 YAML metadata from key_formulas.md")
    parser.add_argument("--dry-run", action="store_true", help="Print to stdout, don't write files")
    parser.add_argument("--topic", type=str, help="Process single topic (e.g., '04')")
    parser.add_argument("--dump-aliases", action="store_true", help="Generate legacy_aliases.yaml")
    parser.add_argument("--dump-citations", action="store_true", help="Generate citations.yaml skeleton")
    args = parser.parse_args()

    # Find files
    files = find_key_formulas_files(args.topic)
    if not files:
        print(f"No key_formulas.md found" + (f" for topic {args.topic}" if args.topic else ""))
        sys.exit(1)

    # Ensure output dir exists
    if not args.dry_run:
        ENTRIES_DIR.mkdir(parents=True, exist_ok=True)

    # Parse all
    all_formulas = []
    for topic_dir, filepath in files:
        formulas = parse_key_formulas(topic_dir, filepath)
        all_formulas.extend(formulas)
        print(f"  {topic_dir}: {len(formulas)} formulas parsed", file=sys.stderr)

    print(f"\nTotal: {len(all_formulas)} formulas from {len(files)} topics", file=sys.stderr)

    # Check for duplicate semantic IDs
    ids = [f.semantic_id for f in all_formulas]
    dupes = [sid for sid in ids if ids.count(sid) > 1]
    if dupes:
        print(f"\n⚠️  Duplicate semantic IDs detected: {set(dupes)}", file=sys.stderr)
        # Disambiguate by appending fcode number
        seen = {}
        for f in all_formulas:
            if f.semantic_id in seen:
                suffix = f.fcode.replace('.', '_')
                f.semantic_id = f.semantic_id.replace('.01', f'_{suffix}.01')
            seen[f.semantic_id] = True

    # Execute action
    if args.dump_aliases:
        dump_aliases(all_formulas, args.dry_run)
    elif args.dump_citations:
        dump_citations(all_formulas, args.dry_run)
    else:
        for f in all_formulas:
            write_entry(f, args.dry_run)
        if not args.dry_run:
            print(f"\n✅ Wrote {len(all_formulas)} YAML entries to {ENTRIES_DIR}")


if __name__ == "__main__":
    main()
