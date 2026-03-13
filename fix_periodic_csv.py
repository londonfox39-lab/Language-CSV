#!/usr/bin/env python3
import csv
from pathlib import Path

inp = Path('/Users/londonfoxnew/Desktop/CLASST2/AI /Periodic Table of Elements 2.csv')
out = Path('/Users/londonfoxnew/Desktop/CLASST2/AI /Periodic Table of Elements 2_fixed.csv')

with inp.open('r', newline='', encoding='utf-8-sig') as f:
    rows = list(csv.reader(f))

if not rows:
    raise SystemExit('No data found')

header = [h.strip() if h else '' for h in rows[0]]

fixed_header = []
blank_count = 0
for h in header:
    if not h:
        blank_count += 1
        fixed_header.append(f'Column_{blank_count}')
    else:
        fixed_header.append(h)

with out.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(fixed_header)

    for r in rows[1:]:
        cleaned = [(c.strip() if c is not None else '') for c in r]
        if len(cleaned) < len(fixed_header):
            cleaned += [''] * (len(fixed_header) - len(cleaned))
        elif len(cleaned) > len(fixed_header):
            cleaned = cleaned[:len(fixed_header)]
        writer.writerow(cleaned)

print(out)
