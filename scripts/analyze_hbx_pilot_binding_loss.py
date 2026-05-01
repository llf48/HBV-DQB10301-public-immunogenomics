import csv
import argparse
import math
from collections import defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]

BINDER_CUTOFF = 10.0


def as_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--infile",
        default=str(
            PROJECT / "results" / "tables" / "hbx_pilot_iedb_recommended_predictions.csv"
        ),
    )
    parser.add_argument("--out-prefix", default="hbx_pilot")
    args = parser.parse_args()

    infile = Path(args.infile)
    out_best = PROJECT / "results" / "tables" / f"{args.out_prefix}_best_rank_by_variant_allele.csv"
    out_loss = PROJECT / "results" / "tables" / f"{args.out_prefix}_dq3_pli_by_variant.csv"

    rows = []
    with infile.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    best = {}
    for row in rows:
        key = (row["variant_id"], row["state"], row["allele"], row["allele_group"])
        rank = as_float(row["iedb_rank"])
        if key not in best or rank < best[key]["best_rank"]:
            best[key] = {
                "variant_id": row["variant_id"],
                "mutation_id": row["mutation_id"],
                "state": row["state"],
                "protein": row["protein"],
                "position": row["position"],
                "ref": row["ref"],
                "alt": row["alt"],
                "allele": row["allele"],
                "allele_group": row["allele_group"],
                "best_rank": rank,
                "best_peptide": row["peptide"],
                "best_window_start": row["window_start"],
                "best_core_peptide": row["core_peptide"],
                "binder_10pct": rank < BINDER_CUTOFF,
            }

    best_rows = list(best.values())
    with out_best.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(best_rows[0]))
        writer.writeheader()
        writer.writerows(best_rows)

    by_variant_allele = defaultdict(dict)
    for row in best_rows:
        by_variant_allele[(row["variant_id"], row["allele"], row["allele_group"])][
            row["state"]
        ] = row

    variant_loss = defaultdict(list)
    for (variant_id, allele, allele_group), pair in by_variant_allele.items():
        if "WT" not in pair or "MUT" not in pair:
            continue
        wt = pair["WT"]
        mut = pair["MUT"]
        wt_rank = wt["best_rank"]
        mut_rank = mut["best_rank"]
        loss = bool(wt_rank < BINDER_CUTOFF and mut_rank >= BINDER_CUTOFF)
        delta_rank = mut_rank - wt_rank
        variant_loss[variant_id].append(
            {
                "allele": allele,
                "allele_group": allele_group,
                "wt_rank": wt_rank,
                "mut_rank": mut_rank,
                "loss": loss,
                "delta_rank": delta_rank,
            }
        )

    out_rows = []
    for variant_id, vals in sorted(variant_loss.items()):
        risk = [v for v in vals if v["allele_group"] == "risk_DQB1_0301"]
        control = [v for v in vals if v["allele_group"] == "control_DQB1_0302"]
        risk_loss_rate = sum(v["loss"] for v in risk) / len(risk) if risk else math.nan
        control_loss_rate = (
            sum(v["loss"] for v in control) / len(control) if control else math.nan
        )
        dq3_pli = risk_loss_rate - control_loss_rate
        risk_delta_mean = sum(v["delta_rank"] for v in risk) / len(risk)
        control_delta_mean = sum(v["delta_rank"] for v in control) / len(control)
        example = vals[0]
        out_rows.append(
            {
                "variant_id": variant_id,
                "risk_loss_rate": risk_loss_rate,
                "control_loss_rate": control_loss_rate,
                "dq3_pli": dq3_pli,
                "risk_delta_rank_mean": risk_delta_mean,
                "control_delta_rank": control_delta_mean,
                "allele_detail": "; ".join(
                    f"{v['allele']} WT={v['wt_rank']:.2f} MUT={v['mut_rank']:.2f} loss={v['loss']}"
                    for v in vals
                ),
            }
        )

    with out_loss.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0]))
        writer.writeheader()
        writer.writerows(out_rows)

    print("Top pilot variants by DQ3-PLI then risk delta rank:")
    for row in sorted(
        out_rows,
        key=lambda r: (float(r["dq3_pli"]), float(r["risk_delta_rank_mean"])),
        reverse=True,
    ):
        print(row["variant_id"], row["dq3_pli"], row["risk_delta_rank_mean"])
    print(out_best)
    print(out_loss)


if __name__ == "__main__":
    main()
