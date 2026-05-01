import argparse
import csv
from collections import defaultdict
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    rows = list(csv.DictReader(open(args.predictions, newline="", encoding="utf-8")))
    summary = defaultdict(lambda: {"total": 0, "strong": 0, "weak": 0, "binder_10": 0})
    for row in rows:
        rank = float(row["iedb_rank"])
        key = (row["allele"], row.get("allele_group", ""))
        summary[key]["total"] += 1
        if rank < 2:
            summary[key]["strong"] += 1
        if 2 <= rank < 10:
            summary[key]["weak"] += 1
        if rank < 10:
            summary[key]["binder_10"] += 1

    out_rows = []
    for (allele, allele_group), vals in summary.items():
        out_rows.append(
            {
                "allele": allele,
                "allele_group": allele_group,
                **vals,
                "binder_10_rate": vals["binder_10"] / vals["total"],
            }
        )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0]))
        writer.writeheader()
        writer.writerows(out_rows)

    for row in out_rows:
        print(
            row["allele"],
            "strong",
            row["strong"],
            "weak",
            row["weak"],
            "binder<10",
            row["binder_10"],
            "of",
            row["total"],
        )


if __name__ == "__main__":
    main()

