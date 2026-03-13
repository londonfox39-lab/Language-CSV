#!/usr/bin/env python3
import argparse
import csv
import re
from pathlib import Path


def split_token(value: str):
    text = (value or "").strip()
    if not text:
        return "", ""

    match = re.match(r"^([A-Za-z]+)([-+]?\d*\.?\d+)$", text)
    if match:
        return match.group(1), match.group(2)

    return text, ""


def transform(input_path: Path, output_path: Path, column: str, keep_original: bool):
    with input_path.open("r", newline="", encoding="utf-8-sig") as input_file:
        reader = csv.DictReader(input_file)
        if not reader.fieldnames:
            raise ValueError("Input CSV has no header row.")

        if column not in reader.fieldnames:
            raise ValueError(f"Column '{column}' not found. Available: {', '.join(reader.fieldnames)}")

        output_headers = []
        for field in reader.fieldnames:
            if field == column:
                if keep_original:
                    output_headers.append(field)
                output_headers.extend([f"{field}_letters", f"{field}_numbers"])
            else:
                output_headers.append(field)

        with output_path.open("w", newline="", encoding="utf-8") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=output_headers)
            writer.writeheader()

            for row in reader:
                letters, numbers = split_token(row.get(column, ""))
                out_row = {}
                for field in reader.fieldnames:
                    if field == column:
                        if keep_original:
                            out_row[field] = row.get(field, "")
                        out_row[f"{field}_letters"] = letters
                        out_row[f"{field}_numbers"] = numbers
                    else:
                        out_row[field] = row.get(field, "")
                writer.writerow(out_row)


def main():
    parser = argparse.ArgumentParser(
        description="Split letter+number values (e.g. C12) into separate CSV columns."
    )
    parser.add_argument("input", help="Path to input CSV")
    parser.add_argument("output", help="Path to output CSV")
    parser.add_argument("column", help="Column name containing mixed letter+number values")
    parser.add_argument(
        "--keep-original",
        action="store_true",
        help="Keep original column in output in addition to split columns",
    )

    args = parser.parse_args()
    transform(Path(args.input), Path(args.output), args.column, args.keep_original)


if __name__ == "__main__":
    main()
