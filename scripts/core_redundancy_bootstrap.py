import argparse
import csv
import random
from collections import defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
BINDER = 10.0


def as_bool(value):
    return str(value).lower() == "true"


def read_csv(path):
    return list(csv.DictReader(Path(path).open(newline="", encoding="utf-8")))


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def identity(a, b):
    length = min(len(a), len(b))
    if length == 0:
        return 0
    matches = sum(1 for x, y in zip(a[:length], b[:length]) if x == y)
    return matches / max(len(a), len(b))


def greedy_representatives(records, threshold):
    representatives = []
    for row in sorted(records, key=lambda r: (r["query_genotype"], r["accession"])):
        seq = row["core_seq"]
        if all(identity(seq, rep["core_seq"]) < threshold for rep in representatives):
            representatives.append(row)
    return representatives


def build_accession_counts(pred_rows, accessions):
    selected = set(accessions)
    counts = defaultdict(lambda: {"total": 0, "binder": 0, "strong": 0})
    for row in pred_rows:
        allele = row["allele"]
        rank = float(row["iedb_rank"])
        for accession in row.get("source_accessions", "").split(";"):
            if accession not in selected:
                continue
            counts[(accession, allele)]["total"] += 1
            if rank < BINDER:
                counts[(accession, allele)]["binder"] += 1
            if rank < 2.0:
                counts[(accession, allele)]["strong"] += 1
    return counts


def summarize_accessions(counts, accessions, alleles):
    rows = []
    selected = set(accessions)
    for allele in alleles:
        total = sum(v["total"] for (acc, a), v in counts.items() if a == allele and acc in selected)
        binder = sum(v["binder"] for (acc, a), v in counts.items() if a == allele and acc in selected)
        strong = sum(v["strong"] for (acc, a), v in counts.items() if a == allele and acc in selected)
        rows.append(
            {
                "allele": allele,
                "accession_count": len(selected),
                "occurrence_total": total,
                "occurrence_binder_10": binder,
                "occurrence_binder_10_rate": binder / total if total else 0,
                "occurrence_strong": strong,
                "occurrence_strong_rate": strong / total if total else 0,
            }
        )
    return rows


def percentile(vals, p):
    vals = sorted(vals)
    if not vals:
        return ""
    idx = (len(vals) - 1) * p
    lo = int(idx)
    hi = min(lo + 1, len(vals) - 1)
    frac = idx - lo
    return vals[lo] * (1 - frac) + vals[hi] * frac


def bootstrap(counts, accessions, alleles, primary, iterations, seed):
    rng = random.Random(seed)
    by_accession = {
        accession: {allele: counts.get((accession, allele), {"total": 0, "binder": 0}) for allele in alleles}
        for accession in accessions
    }
    rate_draws = defaultdict(list)
    diff_draws = defaultdict(list)
    ratio_draws = defaultdict(list)
    for _ in range(iterations):
        sampled = [rng.choice(accessions) for _ in accessions]
        totals = {allele: 0 for allele in alleles}
        binders = {allele: 0 for allele in alleles}
        for accession in sampled:
            for allele in alleles:
                vals = by_accession[accession][allele]
                totals[allele] += vals["total"]
                binders[allele] += vals["binder"]
        rates = {allele: binders[allele] / totals[allele] if totals[allele] else 0 for allele in alleles}
        for allele, rate in rates.items():
            rate_draws[allele].append(rate)
            if allele != primary:
                diff_draws[allele].append(rates[primary] - rate)
                ratio_draws[allele].append(rates[primary] / rate if rate > 0 else float("inf"))
    rows = []
    for allele in alleles:
        vals = rate_draws[allele]
        rows.append(
            {
                "metric": "binder_rate",
                "allele": allele,
                "mean": sum(vals) / len(vals),
                "ci_low_2_5": percentile(vals, 0.025),
                "ci_high_97_5": percentile(vals, 0.975),
            }
        )
    for allele in alleles:
        if allele == primary:
            continue
        vals = diff_draws[allele]
        rows.append(
            {
                "metric": f"rate_difference_{primary}_minus_{allele}",
                "allele": allele,
                "mean": sum(vals) / len(vals),
                "ci_low_2_5": percentile(vals, 0.025),
                "ci_high_97_5": percentile(vals, 0.975),
            }
        )
        vals = [v for v in ratio_draws[allele] if v != float("inf")]
        rows.append(
            {
                "metric": f"rate_ratio_{primary}_over_{allele}",
                "allele": allele,
                "mean": sum(vals) / len(vals),
                "ci_low_2_5": percentile(vals, 0.025),
                "ci_high_97_5": percentile(vals, 0.975),
            }
        )
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--qc", default=str(PROJECT / "data" / "processed" / "core_large_record_qc.csv"))
    parser.add_argument("--pred", default=str(PROJECT / "results" / "tables" / "core_large_expanded_dq_netmhciipan_predictions.csv"))
    parser.add_argument("--out-prefix", default="core_large_expanded_dq")
    parser.add_argument("--bootstrap", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260430)
    parser.add_argument("--primary", default="HLA-DQA1*03:01/DQB1*03:02")
    args = parser.parse_args()

    qc_rows = [row for row in read_csv(args.qc) if as_bool(row["passes_qc"])]
    pred_rows = read_csv(args.pred)
    alleles = sorted(set(row["allele"] for row in pred_rows))

    rep_sets = {"all_qc": qc_rows, "exact_core": []}
    seen = set()
    for row in sorted(qc_rows, key=lambda r: (r["query_genotype"], r["accession"])):
        if row["core_seq"] in seen:
            continue
        seen.add(row["core_seq"])
        rep_sets["exact_core"].append(row)
    for label, threshold in [("greedy_99pct", 0.99), ("greedy_95pct", 0.95)]:
        rep_sets[label] = greedy_representatives(qc_rows, threshold)

    representative_rows = []
    sensitivity_rows = []
    for set_name, reps in rep_sets.items():
        accessions = [row["accession"] for row in reps]
        for row in reps:
            representative_rows.append(
                {
                    "set_name": set_name,
                    "accession": row["accession"],
                    "query_genotype": row["query_genotype"],
                    "country": row.get("country", ""),
                    "collection_date": row.get("collection_date", ""),
                    "core_len": row["core_len"],
                    "core_seq": row["core_seq"],
                }
            )
        counts = build_accession_counts(pred_rows, accessions)
        for summary in summarize_accessions(counts, accessions, alleles):
            summary["set_name"] = set_name
            sensitivity_rows.append(summary)

    out_dir = PROJECT / "results" / "tables"
    write_csv(out_dir / f"{args.out_prefix}_dedup_representatives.csv", representative_rows)
    write_csv(out_dir / f"{args.out_prefix}_dedup_sensitivity.csv", sensitivity_rows)

    all_accessions = [row["accession"] for row in qc_rows]
    all_counts = build_accession_counts(pred_rows, all_accessions)
    boot_rows = bootstrap(all_counts, all_accessions, alleles, args.primary, args.bootstrap, args.seed)
    write_csv(out_dir / f"{args.out_prefix}_record_bootstrap.csv", boot_rows)

    for set_name, reps in rep_sets.items():
        print(set_name, len(reps))
    print(out_dir / f"{args.out_prefix}_dedup_sensitivity.csv")
    print(out_dir / f"{args.out_prefix}_record_bootstrap.csv")


if __name__ == "__main__":
    main()
