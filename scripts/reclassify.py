#!/usr/bin/env python3
"""Batch reclassify claim_type and artifact_type for YAML entries."""
import yaml, os, sys, io

if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

RECLASSIFY = {
    # Definitions
    'F6.1': ('IDENTITY', 'DEFINITION'), 'F6.2': ('IDENTITY', 'DEFINITION'),
    'F6.9': ('IDENTITY', 'DEFINITION'), 'F6.3': ('IDENTITY', 'IDENTITY'),
    'F1.4': ('IDENTITY', 'DEFINITION'), 'F1.8': ('IDENTITY', 'IDENTITY'),
    'F1.15': ('IDENTITY', 'DEFINITION'),
    'F2.2': ('IDENTITY', 'DEFINITION'), 'F2.10': ('IDENTITY', 'DEFINITION'),
    'F2.3': ('IDENTITY', 'DEFINITION'), 'F2.4': ('IDENTITY', 'DEFINITION'),
    'F2.5': ('IDENTITY', 'DEFINITION'), 'F2.13': ('IDENTITY', 'DEFINITION'),
    'F2.14': ('IDENTITY', 'DEFINITION'),
    'F3.3': ('IDENTITY', 'DEFINITION'), 'F3.9': ('IDENTITY', 'DEFINITION'),
    'F3.12': ('IDENTITY', 'DEFINITION'),
    'F8.1': ('IDENTITY', 'DEFINITION'), 'F8.3': ('IDENTITY', 'DEFINITION'),
    'F8.5': ('IDENTITY', 'DEFINITION'), 'F8.6': ('IDENTITY', 'DEFINITION'),
    'F16.1': ('IDENTITY', 'DEFINITION'), 'F11.12': ('IDENTITY', 'DEFINITION'),
    'F11.14': ('IDENTITY', 'DEFINITION'), 'F10.13': ('IDENTITY', 'DEFINITION'),
    'F10.24': ('IDENTITY', 'DEFINITION'),
    # Theorems
    'F3.8': ('EQUIVALENCE', 'THEOREM'), 'F3.14': ('BOUND.UPPER', 'THEOREM'),
    'F3.22': ('BOUND.UPPER', 'THEOREM'), 'F3.23': ('BOUND.UPPER', 'THEOREM'),
    'F3.25': ('BOUND.UPPER', 'THEOREM'), 'F3.44': ('IDENTITY', 'THEOREM'),
    'F3.45': ('IDENTITY', 'THEOREM'), 'F3.46': ('IDENTITY', 'THEOREM'),
    'F3.36': ('BOUND.UPPER', 'THEOREM'), 'F3.15': ('BOUND.LOWER', 'THEOREM'),
    'F3.47': ('IDENTITY', 'THEOREM'), 'F3.11': ('EQUIVALENCE', 'DEFINITION'),
    'F4.4': ('CORRECTNESS', 'THEOREM'), 'F4.13': ('IDENTITY', 'DEFINITION'),
    'F5.1': ('BOUND.LOWER', 'THEOREM'), 'F5.4': ('IDENTITY', 'DEFINITION'),
    'F5.6': ('IDENTITY', 'DEFINITION'), 'F5.7': ('IDENTITY', 'DEFINITION'),
    'F5.8': ('LIMITATION', 'THEOREM'), 'F5.9': ('IDENTITY', 'DEFINITION'),
    'F5.12': ('BOUND.UPPER', 'THEOREM'), 'F5.14': ('BOUND.UPPER', 'THEOREM'),
    'F5.15': ('IDENTITY', 'DEFINITION'), 'F5.16': ('IDENTITY', 'DEFINITION'),
    # Proof techniques
    'F18.10': ('BOUND.UPPER', 'THEOREM'), 'F18.12': ('BOUND.UPPER', 'THEOREM'),
    'F18.17': ('BOUND.LOWER', 'LEMMA'), 'F18.18': ('BOUND.LOWER', 'THEOREM'),
    'F18.19': ('BOUND.UPPER', 'THEOREM'), 'F18.20': ('BOUND.UPPER', 'THEOREM'),
    # ML definitions
    'F11.3': ('IDENTITY', 'DEFINITION'), 'F11.7': ('IDENTITY', 'DEFINITION'),
    'F11.9': ('EQUIVALENCE', 'DERIVATION'), 'F11.10': ('IDENTITY', 'DEFINITION'),
    'F11.13': ('IDENTITY', 'IDENTITY'), 'F11.21': ('IDENTITY', 'DEFINITION'),
    'F11.22': ('IDENTITY', 'DEFINITION'), 'F11.27': ('EQUIVALENCE', 'THEOREM'),
    'F11.36': ('IDENTITY', 'DEFINITION'), 'F11.44': ('IDENTITY', 'DEFINITION'),
    'F11.45': ('IDENTITY', 'DEFINITION'), 'F11.48': ('CORRECTNESS', 'THEOREM'),
    'F11.49': ('IDENTITY', 'THEOREM'), 'F11.50': ('IDENTITY', 'DEFINITION'),
    # Hardware
    'F15.1': ('IDENTITY', 'DEFINITION'), 'F15.2': ('IDENTITY', 'DEFINITION'),
    'F15.3': ('IDENTITY', 'DEFINITION'), 'F15.7': ('IDENTITY', 'DEFINITION'),
    'F15.8': ('IDENTITY', 'DEFINITION'), 'F15.10': ('IDENTITY', 'DEFINITION'),
    'F15.12': ('IDENTITY', 'DEFINITION'),
    # Stat mech
    'F16.6': ('IDENTITY', 'THEOREM'), 'F16.7': ('IDENTITY', 'DEFINITION'),
    'F16.8': ('IDENTITY', 'DEFINITION'),
    # Statistics
    'F17.1': ('STATISTICAL_VALIDATION', 'PROTOCOL'),
    'F17.2': ('STATISTICAL_VALIDATION', 'IDENTITY'),
    'F17.4': ('STATISTICAL_VALIDATION', 'PROTOCOL'),
    'F17.5': ('STATISTICAL_VALIDATION', 'DEFINITION'),
    'F17.6': ('BOUND.UPPER', 'IDENTITY'),
    'F17.8': ('STATISTICAL_VALIDATION', 'PROTOCOL'),
    'F17.9': ('STATISTICAL_VALIDATION', 'PROTOCOL'),
    # Scheduling/compilation
    'F14.8': ('EQUIVALENCE', 'THEOREM'), 'F14.4': ('IDENTITY', 'DEFINITION'),
    'F14.5': ('BOUND.UPPER', 'THEOREM'),
    # Optimization methods
    'F10.15': ('IDENTITY', 'DEFINITION'), 'F10.25': ('IDENTITY', 'DEFINITION'),
    'F10.22': ('DERIVATION', 'DERIVATION'),
    # Graph theory
    'F7.15': ('IDENTITY', 'DEFINITION'), 'F7.11': ('IDENTITY', 'THEOREM'),
    'F7.6': ('DERIVATION', 'DERIVATION'), 'F7.7': ('DERIVATION', 'DERIVATION'),
    # Topology
    'F8.11': ('DERIVATION', 'DERIVATION'),
}

ENTRIES_DIR = os.path.join(os.path.dirname(__file__), '..', 'v2', 'entries')
changes = 0
for f in sorted(os.listdir(ENTRIES_DIR)):
    if not f.endswith('.yaml'): continue
    path = os.path.join(ENTRIES_DIR, f)
    with open(path, encoding='utf-8') as fh:
        raw = fh.read()
    lines = [l for l in raw.split('\n') if not l.startswith('#')]
    data = yaml.safe_load('\n'.join(lines))
    alias = data.get('legacy_alias', '')
    if alias in RECLASSIFY:
        new_ct, new_at = RECLASSIFY[alias]
        old_ct = data.get('claim_type', '')
        old_at = data.get('artifact_type', '')
        changed = False
        if old_ct != new_ct:
            raw = raw.replace(f'claim_type: {old_ct}', f'claim_type: {new_ct}', 1)
            changed = True
        if old_at != new_at:
            raw = raw.replace(f'artifact_type: {old_at}', f'artifact_type: {new_at}', 1)
            changed = True
        if changed:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(raw)
            changes += 1
print(f'Updated {changes} entries')
