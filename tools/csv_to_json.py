"""
csv_to_json.py - normalises data/products.csv → data/products.json

    python tools/csv_to_json.py
"""

import csv
import json
import re
from pathlib import Path

# Config

SRC = Path(__file__).resolve().parent.parent / "data" / "products.csv"
OUT = Path(__file__).resolve().parent.parent / "data" / "products.json"

# Field normalisers

def norm_int(s: str) -> int | None:
    return int(s) if s else None


def norm_date(s: str) -> str | None:
    """'2006-07-31 00:00:00' → '2006-07-31'"""
    if not s:
        return None
    m = re.match(r"(\d{4}-\d{2}-\d{2})", s)
    return m.group(1) if m else s


def norm_str(s: str) -> str | None:
    """Collapse whitespace; empty → None."""
    if not s:
        return None
    s = re.sub(r"\s+", " ", s).strip()
    return s or None

# Column → normaliser

FIELDS = {
    "id": norm_int,
    "registration_number": norm_str,
    "code": norm_str,
    "international_common_name": norm_str,
    "brand_name": norm_str,
    "form": norm_str,
    "dosage": norm_str,
    "packaging": norm_str,
    "list": norm_str,
    "p1": norm_str,
    "p2": norm_str,
    "obs": norm_str,
    "laboratories_holding_the_registration_decision": norm_str,
    "country_of_the_laboratory_holding_the_registration_decision": norm_str,
    "initial_registration_date": norm_date,
    "final_registration_date": norm_date,
    "type": norm_str,
    "status": norm_str,
    "shelf_life": norm_str,
}

# Main

def main() -> None:
    print(f"Reading {SRC}")
    with open(SRC, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            record = {}
            for col, norm in FIELDS.items():
                record[col] = norm(row.get(col, ""))
            rows.append(record)

    print(f"  {len(rows)} records, {len(FIELDS)} fields")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"  {OUT.name}  {OUT.stat().st_size:>9,} bytes")
    print(f"  Build OK: {len(rows)} records.\n")

if __name__ == "__main__":
    main()
