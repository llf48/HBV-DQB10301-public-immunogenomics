import csv
from itertools import combinations
from pathlib import Path

from scipy.stats import fisher_exact


PROJECT = Path(__file__).resolve().parents[1]
SUMMARY = PROJECT / "results" / "tables" / "core_large_gap_summary_by_allele.csv"
OUT = PROJECT / "results" / "tables" / "core_large_pairwise_fisher_tests.csv"


def main():
    rows = list(csv.DictReader(SUMMARY.open(newline="", encoding="utf-8")))
    out_rows = []
    for a, b in combinations(rows, 2):
        for mode in ["unique", "occurrence"]:
            a_total = int(float(a[f"{mode}_total"]))
            b_total = int(float(b[f"{mode}_total"]))
            a_bind = int(float(a[f"{mode}_binder_10"]))
            b_bind = int(float(b[f"{mode}_binder_10"]))
            table = [[a_bind, a_total - a_bind], [b_bind, b_total - b_bind]]
            odds_ratio, p_value = fisher_exact(table)
            a_rate = a_bind / a_total
            b_rate = b_bind / b_total
            out_rows.append(
                {
                    "mode": mode,
                    "allele_a": a["allele"],
                    "allele_b": b["allele"],
                    "allele_a_binder_rate": a_rate,
                    "allele_b_binder_rate": b_rate,
                    "rate_ratio_a_over_b": a_rate / b_rate if b_rate else "",
                    "odds_ratio": odds_ratio,
                    "p_value": p_value,
                    "table": str(table),
                }
            )

    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0]))
        writer.writeheader()
        writer.writerows(out_rows)

    for row in out_rows:
        print(
            row["mode"],
            row["allele_a"],
            "vs",
            row["allele_b"],
            "OR",
            row["odds_ratio"],
            "P",
            row["p_value"],
        )
    print(OUT)


if __name__ == "__main__":
    main()

