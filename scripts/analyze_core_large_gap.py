import csv
from collections import defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
PRED = PROJECT / "results" / "tables" / "core_large_iedb_netmhciipan_predictions.csv"
QC = PROJECT / "data" / "processed" / "core_large_record_qc.csv"
OUT_ALLELE = PROJECT / "results" / "tables" / "core_large_gap_summary_by_allele.csv"
OUT_GENOTYPE = PROJECT / "results" / "tables" / "core_large_gap_summary_by_allele_genotype.csv"
OUT_TOP = PROJECT / "results" / "tables" / "core_large_top_binders.csv"
OUT_WINDOW = PROJECT / "results" / "tables" / "core_large_window_min_rank.csv"

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
        if STRONG <= rank < BINDER:
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


def main():
    accession_to_genotype = {}
    with QC.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if as_bool(row["passes_qc"]):
                accession_to_genotype[row["accession"]] = row["query_genotype"]

    rows = list(csv.DictReader(PRED.open(newline="", encoding="utf-8")))

    by_allele = defaultdict(list)
    by_allele_genotype = defaultdict(list)
    expanded_for_genotype = []

    for row in rows:
        row["source_accession_list"] = [
            a for a in row.get("source_accessions", "").split(";") if a
        ]
        row["source_count_int"] = len(row["source_accession_list"])
        by_allele[row["allele"]].append(row)

        for accession in row["source_accession_list"]:
            genotype = accession_to_genotype.get(accession)
            if not genotype:
                continue
            expanded = dict(row)
            expanded["genotype"] = genotype
            expanded["source_count_int"] = 1
            expanded_for_genotype.append(expanded)
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
                "occurrence_total": weighted["total"],
                "occurrence_strong": weighted["strong"],
                "occurrence_weak": weighted["weak"],
                "occurrence_binder_10": weighted["binder_10"],
                "occurrence_binder_10_rate": weighted["binder_10_rate"],
            }
        )

    with OUT_ALLELE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(allele_rows[0]))
        writer.writeheader()
        writer.writerows(allele_rows)

    genotype_rows = []
    for (allele, genotype), vals in sorted(by_allele_genotype.items()):
        counts = summarize_counts(vals, lambda r: 1)
        genotype_rows.append(
            {
                "allele": allele,
                "genotype": genotype,
                "occurrence_total": counts["total"],
                "occurrence_strong": counts["strong"],
                "occurrence_weak": counts["weak"],
                "occurrence_binder_10": counts["binder_10"],
                "occurrence_binder_10_rate": counts["binder_10_rate"],
            }
        )

    with OUT_GENOTYPE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(genotype_rows[0]))
        writer.writeheader()
        writer.writerows(genotype_rows)

    top_rows = sorted(rows, key=lambda r: float(r["iedb_rank"]))[:100]
    with OUT_TOP.open("w", newline="", encoding="utf-8") as f:
        fields = [
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
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in top_rows:
            writer.writerow({k: row.get(k, "") for k in fields})

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
    with OUT_WINDOW.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(next(iter(window_best.values()))))
        writer.writeheader()
        writer.writerows(window_best.values())

    print("Summary by allele:")
    for row in allele_rows:
        print(row["allele"], "unique", row["unique_binder_10"], "/", row["unique_total"], "occ", row["occurrence_binder_10"], "/", row["occurrence_total"])
    print(OUT_ALLELE)
    print(OUT_GENOTYPE)
    print(OUT_TOP)
    print(OUT_WINDOW)


if __name__ == "__main__":
    main()

