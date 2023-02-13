#!/usr/bin/env python3

"""
This script parses the markdown table in README.md and extracts
JSON signature definitions for use in automated tooling.

The output format is as follows:
[
  {
    "cname": [],
    "discussion": "[Issue #74](https://github.com/EdOverflow/can-i-take-over-xyz/issues/74)",
    "documentation": "",
    "fingerprint": "It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.",
    "nxdomain": false,
    "http_status": null,
    "service": "LaunchRock",
    "status": "Vulnerable",
    "cicd_pass": false
  },
  ...
]

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

import urllib3

urllib3.disable_warnings()


def errprint(s):
    sys.stderr.write(f"{s}\n")
    sys.stderr.flush()


threads = 20

readme_file = (Path(__file__).parent.parent / "README.md").resolve()
json_file = (Path(__file__).parent.parent / "fingerprints.json").resolve()

if not readme_file.is_file():
    errprint(f"Could not find {readme_file}")
    sys.exit(1)
delimiter = "<!--FINGERPRINTS-->"
with open(readme_file) as f:
    readme_contents = f.read()
if not readme_contents:
    errprint(f"Empty README")
    sys.exit(1)
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

http_status_fingerprint = re.compile(r"^http_status=\d{3}$", re.I)


class Fingerprint:
    """
    Take a row from the README table and transform it into a more flexible object
    """

    def __init__(self, table_row):
        # split into columns
        cols = [c.strip(" `") for c in table_row.split("|")][1:-1]
        # skip header, dividers
        assert cols and cols[0], ""
        engine = cols[0]
        assert not engine == "Engine" and not all(c == "-" for c in engine), engine
        # pad columns
        cols = cols + [""] * (7 - len(cols))
        try:
            (
                self.engine,
                self.status,
                cicd_pass,
                domains,
                self.fingerprint,
                self.discussion,
                self.documentation,
            ) = cols
        except ValueError as e:
            errprint(f"{e}: {cols}")
        try:
            self.fingerprint_regex = re.compile(self.fingerprint, re.MULTILINE)
        except re.error:
            self.fingerprint_regex = re.compile(
                re.escape(self.fingerprint), re.MULTILINE
            )
        self.status = self.status.capitalize()
        self.nxdomain = self.fingerprint.lower() == "nxdomain"
        self.http_status = None
        if http_status_fingerprint.match(self.fingerprint):
            self.http_status = int(self.fingerprint.split("=")[-1])
        self.vulnerable = self.status.capitalize() == "Vulnerable"
        self.domains = []
        if domains:
            self.domains = [d.strip() for d in re.split(",| ", domains)]
            self.domains = [d for d in self.domains if d]
        self.cicd_pass, reason = self.verify()
        errprint((self.engine + ":").ljust(30) + f"\t{reason}")

    def verify(self):
        """
        Verify this fingerprint.
        For every domain, check <random>.domain and <random>.com -[DNS]-> domain
        If any match the fingerprint, return True
        """
        if not self.vulnerable:
            return False, "Not vulnerable"
        if not self.domains:
            return False, "Missing domain"
        if not self.fingerprint:
            return False, "Missing fingerprint"
        errors = []
        for d in self.domains:
            d = d.strip("*.")
            for scheme in ("http", "https"):
                # first, try {random}.domain
                url = f"{scheme}://{rand_string()}.{d}"
                match, reason = self._verify_response(
                    url, headers=headers, verify=False
                )
                if match:
                    return match, reason
                else:
                    errors.append(reason)
                # next, try {random_domain} -[DNS]-> domain
                url = f"{scheme}://{d}"
                r_headers = dict(headers)
                r_headers["Host"] = f"{rand_string()}.com"
                match, reason = self._verify_response(
                    url, headers=r_headers, verify=False
                )
                if match:
                    return match, reason
                else:
                    errors.append(reason)

        return False, f"No matches for {self.engine} (Errors: {errors})"

    def _verify_response(self, *args, **kwargs):
        if self.http_status:
            kwargs["allow_redirects"] = False
        try:
            r = requests.get(*args, **kwargs)
            if self.http_status is not None and r.status_code == self.http_status:
                return True, f"Fingerprint verified, HTTP status matched"
            if (
                not self.nxdomain
                and not self.http_status
                and self.fingerprint_regex.findall(r.text)
            ):
                return True, f"Fingerprint verified"
        except requests.exceptions.RequestException as e:
            if self.nxdomain and "Name or service not known" in str(e):
                return True, f"Fingerprint verified, {args} --> NXDOMAIN"
            return False, str(e)
        return False, "No match"

    @property
    def json(self):
        return {
            "service": self.engine,
            "cname": self.domains,
            "fingerprint": self.fingerprint,
            "nxdomain": self.nxdomain,
            "http_status": self.http_status,
            "status": self.status,
            "vulnerable": self.vulnerable,
            "cicd_pass": self.cicd_pass,
            "discussion": self.discussion,
            "documentation": self.documentation,
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


def make_fingerprint_table(fingerprints):
    rows = []
    for f in fingerprints:
        rows.append(
            [
                f.engine,
                f.status,
                ("🟩" if f.cicd_pass else "🟥"),
                ", ".join(f.domains),
                (f"`{f.fingerprint}`" if f.fingerprint else ""),
                f.discussion,
                f.documentation,
            ]
        )
    rows.sort(key=lambda x: x[0])
    header = [
        "Engine",
        "Status",
        "Verified by CI/CD",
        "Domains",
        "Fingerprint",
        "Discussion",
        "Documentation",
    ]
    return make_markdown_table(rows, header)


if __name__ == "__main__":

    if len(sys.argv) > 1:

        fingerprints = parse_fingerprints()
        json_content = json.dumps(
            sorted([f.json for f in fingerprints], key=lambda f: f["service"]),
            indent=2,
            sort_keys=True,
        )
        fingerprint_table = make_fingerprint_table(fingerprints)
        new_readme_sections = list(readme_sections)
        new_readme_sections[1] = fingerprint_table
        new_readme_content = f"\n{delimiter}\n".join(new_readme_sections)

        if "json" in sys.argv[1:]:
            print(json_content)
        if "readme" in sys.argv[1:]:
            print(new_readme_content)
        if "overwrite_readme" in sys.argv[1:]:
            with open(readme_file, "w") as f:
                f.write(new_readme_content)
        if "overwrite_json" in sys.argv[1:]:
            with open(json_file, "w") as f:
                f.write(json_content)
    else:
        errprint(
            "usage: generate_fingerprints.py (json | readme | overwrite_readme | overwrite_json)"
        )
