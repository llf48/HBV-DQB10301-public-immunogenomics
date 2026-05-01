import argparse
import csv
from collections import defaultdict
from pathlib import Path

from scipy.stats import fisher_exact


PROJECT = Path(__file__).resolve().parents[1]
STRONG = 2.0
BINDER = 10.0


def as_bool(value):
    return str(value).lower() == "true"


def summarize_counts(rows, weight_fn):
    total = 0
    strong = 0
    weak = 0
    binder = 0
    for row in rows:
        weight = weight_fn(row)
        rank = float(row["iedb_rank"])
        total += weight
        if rank < STRONG:
            strong += weight
        elif rank < BINDER:
            weak += weight
        if rank < BINDER:
            binder += weight
    return {
        "total": total,
        "strong": strong,
        "weak": weak,
        "binder_10": binder,
        "binder_10_rate": binder / total if total else 0,
        "strong_rate": strong / total if total else 0,
    }


def load_accession_genotype(qc_path):
    mapping = {}
    with qc_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if as_bool(row["passes_qc"]):
                mapping[row["accession"]] = row["query_genotype"]
    return mapping


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", required=True)
    parser.add_argument("--qc", default=str(PROJECT / "data" / "processed" / "core_large_record_qc.csv"))
    parser.add_argument("--out-prefix", required=True)
    parser.add_argument("--primary", default="HLA-DQA1*03:01/DQB1*03:02")
    args = parser.parse_args()

    pred_path = Path(args.pred)
    qc_path = Path(args.qc)
    out_dir = PROJECT / "results" / "tables"
    prefix = args.out_prefix
    accession_to_genotype = load_accession_genotype(qc_path)

    rows = list(csv.DictReader(pred_path.open(newline="", encoding="utf-8")))
    for row in rows:
        row["source_accession_list"] = [
            a for a in row.get("source_accessions", "").split(";") if a
        ]
        row["source_count_int"] = len(row["source_accession_list"])

    by_allele = defaultdict(list)
    by_allele_genotype = defaultdict(list)
    for row in rows:
        by_allele[row["allele"]].append(row)
        for accession in row["source_accession_list"]:
            genotype = accession_to_genotype.get(accession)
            if not genotype:
                continue
            expanded = dict(row)
            expanded["genotype"] = genotype
            expanded["source_count_int"] = 1
            by_allele_genotype[(row["allele"], genotype)].append(expanded)

    allele_rows = []
    for allele, vals in sorted(by_allele.items()):
        unique = summarize_counts(vals, lambda r: 1)
        weighted = summarize_counts(vals, lambda r: r["source_count_int"])
        allele_rows.append(
            {
                "allele": allele,
                "allele_group": vals[0]["allele_group"],
                "unique_total": unique["total"],
                "unique_strong": unique["strong"],
                "unique_weak": unique["weak"],
                "unique_binder_10": unique["binder_10"],
                "unique_binder_10_rate": unique["binder_10_rate"],
                "unique_strong_rate": unique["strong_rate"],
                "occurrence_total": weighted["total"],
                "occurrence_strong": weighted["strong"],
                "occurrence_weak": weighted["weak"],
                "occurrence_binder_10": weighted["binder_10"],
                "occurrence_binder_10_rate": weighted["binder_10_rate"],
                "occurrence_strong_rate": weighted["strong_rate"],
            }
        )
    write_csv(out_dir / f"{prefix}_summary_by_allele.csv", allele_rows)

    genotype_rows = []
    for (allele, genotype), vals in sorted(by_allele_genotype.items()):
        counts = summarize_counts(vals, lambda r: 1)
        genotype_rows.append(
            {
                "allele": allele,
                "allele_group": vals[0]["allele_group"],
                "genotype": genotype,
                "occurrence_total": counts["total"],
                "occurrence_strong": counts["strong"],
                "occurrence_weak": counts["weak"],
                "occurrence_binder_10": counts["binder_10"],
                "occurrence_binder_10_rate": counts["binder_10_rate"],
                "occurrence_strong_rate": counts["strong_rate"],
            }
        )
    write_csv(out_dir / f"{prefix}_summary_by_allele_genotype.csv", genotype_rows)

    counts_by_allele = {row["allele"]: row for row in allele_rows}
    fisher_rows = []
    primary = counts_by_allele[args.primary]
    for allele, row in sorted(counts_by_allele.items()):
        if allele == args.primary:
            continue
        for mode in ["unique", "occurrence"]:
            a_binder = int(primary[f"{mode}_binder_10"])
            a_total = int(primary[f"{mode}_total"])
            b_binder = int(row[f"{mode}_binder_10"])
            b_total = int(row[f"{mode}_total"])
            table = [[a_binder, a_total - a_binder], [b_binder, b_total - b_binder]]
            odds_ratio, p_value = fisher_exact(table)
            fisher_rows.append(
                {
                    "mode": mode,
                    "primary_allele": args.primary,
                    "comparison_allele": allele,
                    "comparison_group": row["allele_group"],
                    "primary_binder_rate": a_binder / a_total,
                    "comparison_binder_rate": b_binder / b_total,
                    "rate_ratio_primary_over_comparison": (a_binder / a_total) / (b_binder / b_total)
                    if b_binder
                    else "",
                    "odds_ratio": odds_ratio,
                    "p_value": p_value,
                    "table": table,
                }
            )
    write_csv(out_dir / f"{prefix}_pairwise_fisher_vs_primary.csv", fisher_rows)

    top_rows = sorted(rows, key=lambda r: float(r["iedb_rank"]))[:200]
    top_fields = [
        "allele",
        "allele_group",
        "iedb_rank",
        "peptide",
        "core_peptide",
        "window_start",
        "window_end",
        "source_count",
        "source_accessions",
        "query_genotypes",
        "countries",
    ]
    write_csv(
        out_dir / f"{prefix}_top_binders.csv",
        [{k: row.get(k, "") for k in top_fields} for row in top_rows],
    )

    window_best = {}
    for row in rows:
        key = (row["allele"], int(row["window_start"]))
        rank = float(row["iedb_rank"])
        if key not in window_best or rank < float(window_best[key]["min_rank"]):
            window_best[key] = {
                "allele": row["allele"],
                "allele_group": row["allele_group"],
                "window_start": row["window_start"],
                "min_rank": rank,
                "best_peptide": row["peptide"],
                "source_count": row.get("source_count", ""),
            }
    write_csv(out_dir / f"{prefix}_window_min_rank.csv", list(window_best.values()))

    for row in sorted(allele_rows, key=lambda r: float(r["occurrence_binder_10_rate"]), reverse=True):
        print(
            row["allele"],
            row["allele_group"],
            "unique",
            row["unique_binder_10"],
            "/",
            row["unique_total"],
            f"({float(row['unique_binder_10_rate']) * 100:.2f}%)",
            "occ",
            row["occurrence_binder_10"],
            "/",
            row["occurrence_total"],
            f"({float(row['occurrence_binder_10_rate']) * 100:.2f}%)",
        )
    print(out_dir / f"{prefix}_summary_by_allele.csv")


if __name__ == "__main__":
    main()
