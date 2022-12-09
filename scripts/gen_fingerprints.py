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

import re
import sys
import json
import random
import string
import tabulate
import requests
from pathlib import Path
import concurrent.futures

threads = 20
readme = Path(__file__).parent.parent / "README.md"
delimiter = "<!--FINGERPRINTS-->"
with open(readme) as f:
    readme_contents = f.read()
readme_sections = readme_contents.split(delimiter)
rand_pool = string.ascii_lowercase
tabulate_defaults = {"tablefmt": "github", "disable_numparse": True}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
}


def errprint(s):
    sys.stderr.write(f"{s}\n")
    sys.stderr.flush()


class Fingerprint:
    def __init__(self, table_row):
        # split into columns
        cols = [c.strip(' `') for c in table_row.split('|')][1:-1]
        # skip header, dividers
        assert cols and cols[0], ""
        engine = cols[0]
        assert not engine == "Engine" and not all(c == "-" for c in engine), engine
        # pad columns
        cols = cols + [''] * (7 - len(cols))
        self.engine, self.status, verified, domains, self.fingerprint, self.discussion, self.documentation = cols
        try:
            self.fingerprint_regex = re.compile(self.fingerprint, re.MULTILINE)
        except re.error:
            self.fingerprint_regex = re.compile(re.escape(self.fingerprint), re.MULTILINE)
        self.status = self.status.capitalize()
        self.nxdomain = self.fingerprint.lower() == "nxdomain"
        self.vulnerable = self.status == "Vulnerable"
        self.domains = []
        if domains:
            self.domains = [d.strip() for d in domains.split(",")]
        self.verified, reason = self.verify()
        errprint((self.engine + ":").ljust(30) + f"\t{reason}")

    def verify(self):
        if not self.vulnerable:
            return False, "Not vulnerable"
        if not self.domains:
            return False, "Missing domain"
        if not self.fingerprint:
            return False, "Missing fingerprint"
        verified = []
        for d in self.domains:
            d = d.strip("*.")
            url = f"https://{rand_string()}.{d}"
            try:
                r = requests.get(url, headers=headers)
                if not self.nxdomain and not self.fingerprint_regex.findall(r.text):
                    return False, f'Fingerprint "{self.fingerprint}" does not match {url}'
            except requests.exceptions.RequestException as e:
                if self.nxdomain and "Name or service not known" in str(e):
                    return True, f"{url} --> NXDOMAIN"
                return False, f"{e}"
        return True, "Fingerprint verified"

    @property
    def json(self):
        return {
            "service": self.engine,
            "cname": self.domains,
            "fingerprint": self.fingerprint,
            "nxdomain": self.nxdomain,
            "status": self.status,
            "verified": self.verified,
            "discussion": self.discussion,
            "documentation": self.documentation
        }


def rand_string(length=15):
    """
    rand_string() --> "c4hp4i9jzx"
    rand_string(20) --> "ap4rsdtg5iw7ey7y3oa5"
    rand_string(30) --> "xdmyxtglqf0z3q8t46n430kesq68yu"
    """
    return "".join([random.choice(rand_pool) for _ in range(int(length))])


def make_markdown_table(*args, **kwargs):
    """
    make_table([["row1", "row1"], ["row2", "row2"]], ["header1", "header2"]) -->

    | header1   | header2   |
    |-----------|-----------|
    | row1      | row1      |
    | row2      | row2      |
    """
    # fix IndexError: list index out of range
    if args and not args[0]:
        args = ([[]],) + args[1:]
    for k, v in tabulate_defaults.items():
        if k not in kwargs:
            kwargs[k] = v
    return tabulate.tabulate(*args, **kwargs)


def parse_fingerprints():
    table = readme_sections[1].strip().splitlines()

    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        for row in table:
            future = executor.submit(Fingerprint, row)
            futures.append(future)

    fingerprints = []
    for future in concurrent.futures.as_completed(futures):
        try:
            fingerprints.append(future.result())
        except AssertionError as e:
            engine = str(e)
            if not engine == "Engine" and not all(c == "-" for c in engine):
                errprint(f"Invalid signature: {row}")

    return fingerprints

fingerprints = parse_fingerprints()


def make_fingerprint_table():
    rows = []
    for f in fingerprints:
        rows.append([
            f.engine,
            f.status,
            ("🟩" if f.verified else "🟥"),
            ",".join(f.domains),
            (f"`{f.fingerprint}`" if f.fingerprint else ""),
            f.discussion,
            f.documentation
        ])
    rows.sort(key=lambda x: x[0])
    header = ["Engine", "Status", "Verified", "Domains", "Fingerprint", "Discussion", "Documentation"]
    return make_markdown_table(rows, header)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "json":
        print(json.dumps([f.json for f in fingerprints], indent=2, sort_keys=True))
    else:
        fingerprint_table = make_fingerprint_table()
        readme_sections[1] = fingerprint_table
        print(f"\n{delimiter}\n".join(readme_sections))
