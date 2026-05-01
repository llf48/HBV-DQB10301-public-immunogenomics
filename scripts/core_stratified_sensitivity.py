from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
BINDER = 10.0


def as_bool(value: str) -> bool:
    return str(value).lower() == "true"


def read_csv(path: str | Path) -> list[dict[str, str]]:
    return list(csv.DictReader(Path(path).open(newline="", encoding="utf-8")))


def write_csv(path: str | Path, rows: list[dict[str, object]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def year_bin(year: str) -> str:
    if not year:
        return "Unknown"
    y = int(year)
    if y < 2005:
        return "pre-2005"
    if y <= 2010:
        return "2005-2010"
    if y <= 2015:
        return "2011-2015"
    return "2016+"


def summarize_group(pred_rows, accession_meta, group_field):
    counts = defaultdict(lambda: {"total": 0, "binder": 0, "strong": 0, "records": set()})
    for row in pred_rows:
        rank = float(row["iedb_rank"])
        allele = row["allele"]
        for accession in row.get("source_accessions", "").split(";"):
            if accession not in accession_meta:
                continue
            meta = accession_meta[accession]
            if group_field == "year_bin":
                group = year_bin(meta.get("collection_year", ""))
            else:
                group = meta.get(group_field, "") or "Unknown"
            key = (group_field, group, allele)
            counts[key]["total"] += 1
            counts[key]["records"].add(accession)
            if rank < BINDER:
                counts[key]["binder"] += 1
            if rank < 2.0:
                counts[key]["strong"] += 1
    rows = []
    for (field, group, allele), vals in sorted(counts.items()):
        total = vals["total"]
        binder = vals["binder"]
        rows.append(
            {
                "stratum_type": field,
                "stratum": group,
                "allele": allele,
                "record_count": len(vals["records"]),
                "occurrence_total": total,
                "occurrence_binder_10": binder,
                "occurrence_binder_10_rate": binder / total if total else 0,
                "occurrence_strong": vals["strong"],
                "occurrence_strong_rate": vals["strong"] / total if total else 0,
            }
        )
    return rows


def leave_one_out(pred_rows, accession_meta, exclude_field, primary, risk_alleles, min_records):
    groups = defaultdict(set)
    for accession, meta in accession_meta.items():
        group = meta.get(exclude_field, "") or "Unknown"
        groups[group].add(accession)

    rows = []
    for group, excluded in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(excluded) < min_records:
            continue
        kept = set(accession_meta) - excluded
        counts = defaultdict(lambda: {"total": 0, "binder": 0})
        for row in pred_rows:
            allele = row["allele"]
            rank = float(row["iedb_rank"])
            for accession in row.get("source_accessions", "").split(";"):
                if accession not in kept:
                    continue
                counts[allele]["total"] += 1
                if rank < BINDER:
                    counts[allele]["binder"] += 1
        primary_rate = counts[primary]["binder"] / counts[primary]["total"]
        for risk in risk_alleles:
            risk_rate = counts[risk]["binder"] / counts[risk]["total"]
            rows.append(
                {
                    "exclude_field": exclude_field,
                    "excluded_stratum": group,
                    "excluded_record_count": len(excluded),
                    "primary_allele": primary,
                    "risk_allele": risk,
                    "primary_rate_after_exclusion": primary_rate,
                    "risk_rate_after_exclusion": risk_rate,
                    "rate_ratio_after_exclusion": primary_rate / risk_rate if risk_rate else "",
                    "primary_total_after_exclusion": counts[primary]["total"],
                    "risk_total_after_exclusion": counts[risk]["total"],
                }
            )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--qc", default=str(PROJECT / "data" / "processed" / "core_full_record_qc.csv"))
    parser.add_argument("--pred", default=str(PROJECT / "results" / "tables" / "core_full_expanded_dq_netmhciipan_predictions.csv"))
    parser.add_argument("--out-prefix", default="core_full_expanded_dq")
    parser.add_argument("--primary", default="HLA-DQA1*03:01/DQB1*03:02")
    parser.add_argument("--min-country-records", type=int, default=20)
    args = parser.parse_args()

    qc_rows = [row for row in read_csv(args.qc) if as_bool(row["passes_qc"])]
    accession_meta = {row["accession"]: row for row in qc_rows}
    pred_rows = read_csv(args.pred)
    risk_alleles = sorted(
        {
            row["allele"]
            for row in pred_rows
            if row.get("allele_group") == "risk_DQB1_0301"
        }
    )

    out_dir = PROJECT / "results" / "tables"
    stratified = []
    for field in ["query_genotype", "region", "country", "year_bin"]:
        rows = summarize_group(pred_rows, accession_meta, field)
        if field == "country":
            rows = [r for r in rows if int(r["record_count"]) >= args.min_country_records]
        stratified.extend(rows)
    write_csv(out_dir / f"{args.out_prefix}_stratified_sensitivity.csv", stratified)

    loo = []
    loo.extend(leave_one_out(pred_rows, accession_meta, "region", args.primary, risk_alleles, 20))
    loo.extend(
        leave_one_out(
            pred_rows,
            accession_meta,
            "country",
            args.primary,
            risk_alleles,
            args.min_country_records,
        )
    )
    write_csv(out_dir / f"{args.out_prefix}_leave_one_stratum_out.csv", loo)

    print(out_dir / f"{args.out_prefix}_stratified_sensitivity.csv")
    print(out_dir / f"{args.out_prefix}_leave_one_stratum_out.csv")


if __name__ == "__main__":
    main()
