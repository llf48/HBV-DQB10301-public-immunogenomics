from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
BINDER = 10.0


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


def aa_composition(peptides: list[str]) -> str:
    counts = Counter("".join(peptides))
    total = sum(counts.values())
    if not total:
        return ""
    top = counts.most_common(6)
    return ";".join(f"{aa}:{count / total:.3f}" for aa, count in top)


def positional_signature(peptides: list[str]) -> str:
    if not peptides:
        return ""
    parts = []
    for idx in range(15):
        counts = Counter(p[idx] for p in peptides if len(p) > idx)
        aa, count = counts.most_common(1)[0]
        parts.append(f"{idx + 1}{aa}{count / len(peptides):.2f}")
    return ";".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", default=str(PROJECT / "results" / "tables" / "core_full_expanded_dq_netmhciipan_predictions.csv"))
    parser.add_argument("--out-prefix", default="core_full_expanded_dq")
    parser.add_argument("--primary", default="HLA-DQA1*03:01/DQB1*03:02")
    parser.add_argument(
        "--risk-alleles",
        default="HLA-DQA1*05:08/DQB1*03:01,HLA-DQA1*06:01/DQB1*03:01",
    )
    args = parser.parse_args()

    risk_alleles = set(args.risk_alleles.split(","))
    rows = read_csv(args.pred)

    by_start_allele = defaultdict(list)
    for row in rows:
        by_start_allele[(int(row["window_start"]), row["allele"])].append(row)

    starts = sorted({int(row["window_start"]) for row in rows})
    gap_rows = []
    for start in starts:
        primary_rows = by_start_allele[(start, args.primary)]
        risk_rows = [r for a in risk_alleles for r in by_start_allele[(start, a)]]
        primary_binders = [r for r in primary_rows if float(r["iedb_rank"]) < BINDER]
        risk_binders = [r for r in risk_rows if float(r["iedb_rank"]) < BINDER]
        primary_total_occ = sum(int(r.get("source_count", "1") or 1) for r in primary_rows)
        primary_binder_occ = sum(int(r.get("source_count", "1") or 1) for r in primary_binders)
        risk_total_occ = sum(int(r.get("source_count", "1") or 1) for r in risk_rows)
        risk_binder_occ = sum(int(r.get("source_count", "1") or 1) for r in risk_binders)
        primary_rate = primary_binder_occ / primary_total_occ if primary_total_occ else 0
        risk_rate = risk_binder_occ / risk_total_occ if risk_total_occ else 0
        gap_rows.append(
            {
                "window_start": start,
                "window_end": start + 14,
                "primary_allele": args.primary,
                "risk_alleles": ",".join(sorted(risk_alleles)),
                "primary_unique_total": len(primary_rows),
                "primary_unique_binders": len(primary_binders),
                "primary_occurrence_rate": primary_rate,
                "risk_unique_total": len(risk_rows),
                "risk_unique_binders": len(risk_binders),
                "risk_occurrence_rate": risk_rate,
                "gap_primary_minus_risk": primary_rate - risk_rate,
                "primary_min_rank": min(float(r["iedb_rank"]) for r in primary_rows),
                "risk_min_rank": min(float(r["iedb_rank"]) for r in risk_rows) if risk_rows else "",
                "best_primary_peptide": min(primary_rows, key=lambda r: float(r["iedb_rank"]))["peptide"],
                "primary_binder_aa_composition": aa_composition([r["peptide"] for r in primary_binders]),
                "primary_binder_position_signature": positional_signature([r["peptide"] for r in primary_binders]),
            }
        )

    ranked = sorted(
        gap_rows,
        key=lambda r: (
            float(r["gap_primary_minus_risk"]),
            -float(r["primary_min_rank"]),
        ),
        reverse=True,
    )
    out_dir = PROJECT / "results" / "tables"
    write_csv(out_dir / f"{args.out_prefix}_position_gap_summary.csv", gap_rows)
    write_csv(out_dir / f"{args.out_prefix}_top_position_gaps.csv", ranked[:40])
    print(out_dir / f"{args.out_prefix}_position_gap_summary.csv")
    print(out_dir / f"{args.out_prefix}_top_position_gaps.csv")


if __name__ == "__main__":
    main()
