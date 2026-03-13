#!/usr/bin/env python3
import csv
from pathlib import Path

inp = Path('/Users/londonfoxnew/Desktop/CLASS FALL 2025/science class/nitrogen_cleanredone.csv')
out = Path('/Users/londonfoxnew/Desktop/CLASS FALL 2025/science class/nitrogen_cleanredone_fixed.csv')

with inp.open('r', newline='', encoding='utf-8-sig') as f:
    rows = list(csv.reader(f))

if rows and len(rows[0]) == 1:
    rows = rows[1:]

if not rows:
    raise SystemExit('No data found')

header = rows[0]
fixed_header = []
blank_count = 0
for h in header:
    name = (h or '').strip()
    if not name:
        blank_count += 1
        name = f'Column_{blank_count}'
    fixed_header.append(name)

with out.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(fixed_header)
    for r in rows[1:]:
        if len(r) < len(fixed_header):
            r = r + [''] * (len(fixed_header) - len(r))
        elif len(r) > len(fixed_header):
            r = r[:len(fixed_header)]
        writer.writerow(r)

print(out)
