#!/usr/bin/env python3
"""Print the slice of entries to audit today.

Every entry in data/ plus the README-only European alternatives goes into one
ordered list, and the day of the year picks a window of it, so the whole list
gets revisited every few days. Pass a size to change the window.

    python3 scripts/daily-slice.py        # today's 25
    python3 scripts/daily-slice.py 40     # today's 40
"""

import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SIZE = 25


def load(name):
    with open(ROOT / "data" / f"{name}.json") as f:
        return json.load(f)


def entries():
    out = []
    companies = load("companies")
    for key in ("foundation_models", "applied_ai", "infrastructure", "tools"):
        for e in companies[key]:
            out.append((key, e["name"], e["url"], e.get("country", "")))
    for e in load("research-labs"):
        out.append(("research_labs", e["name"], e["url"], e.get("country", "")))
    for e in load("open-source"):
        out.append(("open_source", e["name"], e["url"], e.get("country", "")))
    resources = load("resources")
    for key in ("funding", "events", "job_boards", "communities", "learning"):
        for e in resources[key]:
            out.append((key, e["name"], e["url"], e.get("country", e.get("scope", ""))))

    md = (ROOT / "README.md").read_text()
    m = re.search(r"^## European alternatives\s*$(.*?)^## ", md, re.S | re.M)
    if m:
        for row in re.finditer(r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]*)\|", m.group(1), re.M):
            out.append(("european_alternatives", row.group(1), row.group(2), row.group(3).strip()))
    return out


def main():
    size = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SIZE
    all_entries = entries()
    total = len(all_entries)
    day = datetime.datetime.now(datetime.timezone.utc).timetuple().tm_yday
    start = ((day - 1) * size) % total
    window = [all_entries[(start + i) % total] for i in range(min(size, total))]

    print(f"# {len(window)} of {total} entries, day {day}, offset {start}")
    for section, name, url, country in window:
        print(json.dumps({"section": section, "name": name, "url": url, "country": country}))


if __name__ == "__main__":
    main()
