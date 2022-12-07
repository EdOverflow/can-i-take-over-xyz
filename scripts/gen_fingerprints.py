#!/usr/bin/env python3

"""
This script parses the markdown table in README.md and extracts
JSON signature definitions for use in automated tooling.

The output format is as follows:
  "LaunchRock": {
    "discussion": "[Issue #74](https://github.com/EdOverflow/can-i-take-over-xyz/issues/74)",
    "documentation": "",
    "fingerprint": "It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.",
    "status": "Vulnerable"
  },
  ...

It is run automatically every time README.md is updated.
"""

import json
from pathlib import Path

readme = Path(__file__).parent.parent / "README.md"
with open(readme) as f:
    table = f.read().split("\n<!--FINGERPRINTS-->\n")[1].strip().splitlines()

fingerprints = {}
for row in table:
    # split into columns
    cols = [c.strip(' `') for c in row.split('|')][1:-1]
    # skip header, dividers
    if not cols or not cols[0] or cols[0] == "Engine" or all(c == "-" for c in cols[0]):
        continue
    # pad columns
    cols = cols + [''] * (5 - len(cols))
    engine, status, fingerprint, discussion, documentation = cols
    fingerprints[engine] = {
        "status": status,
        "fingerprint": fingerprint,
        "discussion": discussion,
        "documentation": documentation
    }

print(json.dumps(fingerprints, indent=2, sort_keys=True))
