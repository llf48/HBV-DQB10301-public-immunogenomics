import argparse
import csv
from collections import defaultdict
from pathlib import Path


BINDER_CUTOFF = 10.0
STRONG_CUTOFF = 2.0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    rows = list(csv.DictReader(open(args.predictions, newline="", encoding="utf-8")))
    best = {}
    for row in rows:
        key = (row["variant_id"], row["state"], row["allele"], row["allele_group"])
        rank = float(row["iedb_rank"])
        if key not in best or rank < best[key]["rank"]:
            best[key] = {
                "variant_id": row["variant_id"],
                "state": row["state"],
                "allele": row["allele"],
                "allele_group": row["allele_group"],
                "rank": rank,
                "binder_10pct": rank < BINDER_CUTOFF,
                "strong_2pct": rank < STRONG_CUTOFF,
                "best_peptide": row["peptide"],
            }

    by_variant_state = defaultdict(list)
    for row in best.values():
        by_variant_state[(row["variant_id"], row["state"])].append(row)

    out_rows = []
    for (variant_id, state), vals in sorted(by_variant_state.items()):
        risk = [v for v in vals if v["allele_group"] == "risk_DQB1_0301"]
        controls = [v for v in vals if v["allele_group"] != "risk_DQB1_0301"]
        risk_binders = sum(v["binder_10pct"] for v in risk)
        control_binders = sum(v["binder_10pct"] for v in controls)
        risk_best = min(v["rank"] for v in risk)
        control_best = min(v["rank"] for v in controls)
        out_rows.append(
            {
                "variant_id": variant_id,
                "state": state,
                "risk_binders": risk_binders,
                "risk_total": len(risk),
                "control_binders": control_binders,
                "control_total": len(controls),
                "risk_best_rank": risk_best,
                "control_best_rank": control_best,
                "dq0301_specific_binder": risk_binders > 0 and control_binders == 0,
                "detail": "; ".join(
                    f"{v['allele']}={v['rank']:.2f}({v['allele_group']})" for v in sorted(vals, key=lambda x: x["rank"])
                ),
            }
        )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0]))
        writer.writeheader()
        writer.writerows(out_rows)

    for row in out_rows:
        print(row["variant_id"], row["state"], "DQ0301_specific=", row["dq0301_specific_binder"], "risk_best=", row["risk_best_rank"], "control_best=", row["control_best_rank"])


if __name__ == "__main__":
    main()
