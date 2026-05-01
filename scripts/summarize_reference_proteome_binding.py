import argparse
import csv
from collections import defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
BINDER = 10.0
STRONG = 2.0


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows):
    total = len(rows)
    binder = sum(float(r["iedb_rank"]) < BINDER for r in rows)
    strong = sum(float(r["iedb_rank"]) < STRONG for r in rows)
    return {
        "total": total,
        "binder_10": binder,
        "binder_10_rate": binder / total if total else 0,
        "strong_2": strong,
        "strong_2_rate": strong / total if total else 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", default=str(PROJECT / "results" / "tables" / "reference_proteome_expanded_dq_netmhciipan_predictions.csv"))
    parser.add_argument("--out-prefix", default="reference_proteome_expanded_dq")
    args = parser.parse_args()

    rows = list(csv.DictReader(Path(args.pred).open(newline="", encoding="utf-8")))
    by_protein_allele = defaultdict(list)
    by_allele = defaultdict(list)
    for row in rows:
        by_protein_allele[(row["protein"], row["allele"], row["allele_group"])].append(row)
        by_allele[(row["allele"], row["allele_group"])].append(row)

    out_rows = []
    for (protein, allele, allele_group), vals in sorted(by_protein_allele.items()):
        counts = summarize(vals)
        out_rows.append(
            {
                "protein": protein,
                "allele": allele,
                "allele_group": allele_group,
                **counts,
            }
        )
    write_csv(PROJECT / "results" / "tables" / f"{args.out_prefix}_summary_by_protein_allele.csv", out_rows)

    allele_rows = []
    for (allele, allele_group), vals in sorted(by_allele.items()):
        counts = summarize(vals)
        allele_rows.append({"allele": allele, "allele_group": allele_group, **counts})
    write_csv(PROJECT / "results" / "tables" / f"{args.out_prefix}_summary_by_allele.csv", allele_rows)

    for row in out_rows:
        if row["protein"] == "core_capsid":
            print(row["allele"], row["binder_10"], "/", row["total"], row["binder_10_rate"])


if __name__ == "__main__":
    main()
