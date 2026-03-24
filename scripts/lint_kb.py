#!/usr/bin/env python3
"""
lint_kb.py — Linter for QC-TheoryKB v2.0 YAML entries.

Validates all YAML files in v2/entries/ for:
  1. ID uniqueness
  2. Legacy alias uniqueness
  3. Derivation file existence on disk
  4. Domain consistency (id prefix matches domain field)
  5. Required fields present
  6. No empty LaTeX

Usage:
    python scripts/lint_kb.py
    Exit code 0 = pass, 1 = errors found.
"""

import io
import sys
import textwrap
from pathlib import Path

import yaml

# ── Ensure UTF-8 on Windows ──────────────────────────────────────────────────
if sys.platform == "win32":
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        if isinstance(stream, io.TextIOWrapper):
            setattr(
                sys,
                stream_name,
                io.TextIOWrapper(stream.buffer, encoding="utf-8", errors="replace"),
            )

# ── Paths ─────────────────────────────────────────────────────────────────────
KB_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = KB_ROOT / "v2" / "entries"

REQUIRED_FIELDS = ["id", "legacy_alias", "domain", "name_en", "latex"]


def load_entry(path: Path):
    """Load a single YAML entry. Returns (data, error_string | None)."""
    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            return None, "YAML did not parse to a dict"
        return data, None
    except yaml.YAMLError as exc:
        return None, f"YAML parse error: {exc}"
    except Exception as exc:
        return None, f"Read error: {exc}"


def lint_all():
    yaml_files = sorted(ENTRIES_DIR.glob("*.yaml"))
    if not yaml_files:
        print(f"ERROR: No YAML files found in {ENTRIES_DIR}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []

    # Tracking maps for uniqueness
    seen_ids: dict[str, Path] = {}
    seen_aliases: dict[str, Path] = {}

    entries_checked = 0
    entries_loaded = 0

    for yf in yaml_files:
        entries_checked += 1
        fname = yf.name

        data, parse_err = load_entry(yf)
        if parse_err:
            errors.append(f"[{fname}] {parse_err}")
            continue
        entries_loaded += 1

        # ── 5. Required fields ────────────────────────────────────────────
        for field in REQUIRED_FIELDS:
            if field not in data or data[field] is None:
                errors.append(f"[{fname}] Missing required field: {field}")

        entry_id = data.get("id", "")
        alias = data.get("legacy_alias", "")
        domain = data.get("domain", "")
        latex = data.get("latex", "")

        # ── 1. ID uniqueness ──────────────────────────────────────────────
        if entry_id:
            if entry_id in seen_ids:
                errors.append(
                    f"[{fname}] Duplicate id '{entry_id}' "
                    f"(first seen in {seen_ids[entry_id].name})"
                )
            else:
                seen_ids[entry_id] = yf

        # ── 2. Legacy alias uniqueness ────────────────────────────────────
        if alias:
            if alias in seen_aliases:
                errors.append(
                    f"[{fname}] Duplicate legacy_alias '{alias}' "
                    f"(first seen in {seen_aliases[alias].name})"
                )
            else:
                seen_aliases[alias] = yf

        # ── 3. Derivation file existence ──────────────────────────────────
        deriv_files = data.get("derivation_files") or []
        for df in deriv_files:
            resolved = KB_ROOT / df
            if not resolved.exists():
                errors.append(
                    f"[{fname}] Derivation file not found: {df}"
                )

        # ── 4. Domain consistency ─────────────────────────────────────────
        # The id should start with the domain prefix.
        # id = "MATH.GRAPH.ADJACENCY_MATRIX.01", domain = "MATH.GRAPH"
        if entry_id and domain:
            if not entry_id.startswith(domain + "."):
                errors.append(
                    f"[{fname}] ID prefix mismatch: id='{entry_id}' "
                    f"does not start with domain='{domain}.'"
                )

        # ── 6. No empty LaTeX ─────────────────────────────────────────────
        if "latex" in data:
            if latex is None or (isinstance(latex, str) and latex.strip() == ""):
                errors.append(f"[{fname}] Empty latex field")

    # ── 7. Report ─────────────────────────────────────────────────────────
    print("=" * 60)
    print("  QC-TheoryKB v2 Lint Report")
    print("=" * 60)
    print(f"  Entries checked : {entries_checked}")
    print(f"  Entries loaded  : {entries_loaded}")
    print(f"  Unique IDs      : {len(seen_ids)}")
    print(f"  Unique aliases  : {len(seen_aliases)}")
    print(f"  Errors          : {len(errors)}")
    print(f"  Warnings        : {len(warnings)}")
    print("=" * 60)

    if warnings:
        print("\n── Warnings ──")
        for w in warnings:
            print(f"  WARN  {w}")

    if errors:
        print("\n── Errors ──")
        for e in errors:
            print(f"  ERROR {e}")
        print(f"\nFAILED — {len(errors)} error(s) found.")
        return 1

    print("\nPASSED — no errors found.")
    return 0


if __name__ == "__main__":
    sys.exit(lint_all())
