#!/usr/bin/env python3
"""Check that every README table matches its JSON file, name by name and in order.

Exits 1 and prints the first mismatch per section. The European alternatives
section lives only in the README and is skipped.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name):
    with open(ROOT / "data" / f"{name}.json") as f:
        return json.load(f)


def section(md, header, level):
    m = re.search(
        rf"^{level} {re.escape(header)}\s*$(.*?)^(?:#{{2,3}} |---)", md, re.S | re.M
    )
    return m.group(1) if m else ""


def rows(text):
    return [m.group(1) for m in re.finditer(r"^\|\s*\[([^\]]+)\]", text, re.M)]


def main():
    md = (ROOT / "README.md").read_text()
    companies = load("companies")
    resources = load("resources")

    checks = [
        ("Foundation models", "###", companies["foundation_models"]),
        ("Applied AI", "###", companies["applied_ai"]),
        ("AI infrastructure", "###", companies["infrastructure"]),
        ("AI tools", "###", companies["tools"]),
        ("Research labs", "##", load("research-labs")),
        ("Open source projects", "##", load("open-source")),
        ("Funding and grants", "##", resources["funding"]),
        ("Events and conferences", "##", resources["events"]),
        ("Job boards", "##", resources["job_boards"]),
        ("Communities", "##", resources["communities"]),
        ("Learning resources", "##", resources["learning"]),
    ]

    failed = False
    for header, level, data in checks:
        in_md = rows(section(md, header, level))
        in_json = [e["name"] for e in data]
        if in_md == in_json:
            print(f"ok   {header}: {len(in_md)} entries")
            continue
        failed = True
        only_md = [n for n in in_md if n not in in_json]
        only_json = [n for n in in_json if n not in in_md]
        print(f"FAIL {header}")
        if only_md:
            print(f"       in README, missing from JSON: {', '.join(only_md)}")
        if only_json:
            print(f"       in JSON, missing from README: {', '.join(only_json)}")
        if not only_md and not only_json:
            print("       same entries, different order")

    if failed:
        print("\nREADME and data/ are out of sync.")
        return 1
    print("\nREADME and data/ agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
