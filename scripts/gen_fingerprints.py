#!/usr/bin/env python3

import json
from pathlib import Path

readme = Path(__file__).parent.parent / "README.md"
with open(readme) as f:
    table = f.read().split("\n<!--FINGERPRINTS-->\n")[1].splitlines()

fingerprints = {}
for row in table:
    # split into columns
    cols = [c.strip(' `') for c in row.split('|')][1:-1]
    # pad columns
    cols = cols + [''] * (5 - len(cols))
    # skip dividers
    if not cols[0] or all(c == "-" for c in cols[0]):
        continue
    engine, status, fingerprint, discussion, documentation = cols
    fingerprints[engine] = {
        "status": status,
        "fingerprint": fingerprint,
        "discussion": discussion,
        "documentation": documentation
    }

print(json.dumps(fingerprints, indent=4, sort_keys=True))
