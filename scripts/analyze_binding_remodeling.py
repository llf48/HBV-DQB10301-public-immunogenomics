import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path


BINDER_CUTOFF = 10.0
STRONG_CUTOFF = 2.0


def as_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def classify(wt_rank, mut_rank):
    wt_binder = wt_rank < BINDER_CUTOFF
    mut_binder = mut_rank < BINDER_CUTOFF
    if wt_binder and not mut_binder:
        event = "loss"
    elif not wt_binder and mut_binder:
        event = "gain"
    elif wt_binder and mut_binder and mut_rank <= wt_rank / 2:
        event = "strengthened"
    elif wt_binder and mut_binder and mut_rank >= wt_rank * 2:
        event = "weakened"
    else:
        event = "neutral"
    return event


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", required=True)
    parser.add_argument("--out-prefix", required=True)
    args = parser.parse_args()

    infile = Path(args.infile)
    project = infile.parents[2]
    out_best = project / "results" / "tables" / f"{args.out_prefix}_best_rank_by_variant_allele.csv"
    out_events = project / "results" / "tables" / f"{args.out_prefix}_binding_events.csv"
    out_summary = project / "results" / "tables" / f"{args.out_prefix}_remodeling_summary.csv"

    rows = list(csv.DictReader(infile.open(newline="", encoding="utf-8")))
    best = {}
    for row in rows:
        key = (row["variant_id"], row["state"], row["allele"], row["allele_group"])
        rank = as_float(row["iedb_rank"])
        if key not in best or rank < best[key]["best_rank"]:
            best[key] = {
                **{k: row.get(k, "") for k in [
                    "variant_id",
                    "mutation_spec",
                    "state",
                    "protein",
                    "reference_accession",
                    "evidence_tier",
                    "evidence_role",
                    "allele",
                    "allele_group",
                    "method",
                ]},
                "best_rank": rank,
                "strong_2pct": rank < STRONG_CUTOFF,
                "binder_10pct": rank < BINDER_CUTOFF,
                "best_peptide": row["peptide"],
                "best_window_start": row["window_start"],
                "best_core_peptide": row.get("core_peptide", ""),
            }

    best_rows = list(best.values())
    with out_best.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(best_rows[0]))
        writer.writeheader()
        writer.writerows(best_rows)

    pairs = defaultdict(dict)
    for row in best_rows:
        pairs[(row["variant_id"], row["allele"], row["allele_group"])][row["state"]] = row

    event_rows = []
    for (variant_id, allele, allele_group), pair in pairs.items():
        if "WT" not in pair or "MUT" not in pair:
            continue
        wt = pair["WT"]
        mut = pair["MUT"]
        wt_rank = wt["best_rank"]
        mut_rank = mut["best_rank"]
        event = classify(wt_rank, mut_rank)
        event_rows.append(
            {
                "variant_id": variant_id,
                "mutation_spec": wt["mutation_spec"],
                "protein": wt["protein"],
                "reference_accession": wt["reference_accession"],
                "evidence_tier": wt["evidence_tier"],
                "allele": allele,
                "allele_group": allele_group,
                "wt_rank": wt_rank,
                "mut_rank": mut_rank,
                "delta_rank": mut_rank - wt_rank,
                "event": event,
                "wt_best_peptide": wt["best_peptide"],
                "mut_best_peptide": mut["best_peptide"],
            }
        )

    with out_events.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(event_rows[0]))
        writer.writeheader()
        writer.writerows(event_rows)

    by_variant = defaultdict(list)
    for row in event_rows:
        by_variant[row["variant_id"]].append(row)

    summary_rows = []
    for variant_id, vals in sorted(by_variant.items()):
        risk = [v for v in vals if v["allele_group"] == "risk_DQB1_0301"]
        control = [v for v in vals if v["allele_group"] == "control_DQB1_0302"]
        risk_gain = sum(v["event"] == "gain" for v in risk) / len(risk)
        risk_loss = sum(v["event"] == "loss" for v in risk) / len(risk)
        control_gain = sum(v["event"] == "gain" for v in control) / len(control)
        control_loss = sum(v["event"] == "loss" for v in control) / len(control)
        risk_delta = sum(float(v["delta_rank"]) for v in risk) / len(risk)
        control_delta = sum(float(v["delta_rank"]) for v in control) / len(control)
        specificity_score = (control_delta - risk_delta)
        example = vals[0]
        summary_rows.append(
            {
                "variant_id": variant_id,
                "mutation_spec": example["mutation_spec"],
                "protein": example["protein"],
                "evidence_tier": example["evidence_tier"],
                "risk_loss_rate": risk_loss,
                "risk_gain_rate": risk_gain,
                "control_loss_rate": control_loss,
                "control_gain_rate": control_gain,
                "risk_delta_rank_mean": risk_delta,
                "control_delta_rank_mean": control_delta,
                "dq3_bri_specificity_score": specificity_score,
                "event_detail": "; ".join(
                    f"{v['allele']}:{v['event']}:WT={float(v['wt_rank']):.2f}:MUT={float(v['mut_rank']):.2f}"
                    for v in vals
                ),
            }
        )

    with out_summary.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary_rows[0]))
        writer.writeheader()
        writer.writerows(summary_rows)

    print("Top remodeling candidates by DQ3-BRI specificity score:")
    for row in sorted(summary_rows, key=lambda r: float(r["dq3_bri_specificity_score"]), reverse=True):
        print(
            row["variant_id"],
            "score=",
            row["dq3_bri_specificity_score"],
            "risk_delta=",
            row["risk_delta_rank_mean"],
            "control_delta=",
            row["control_delta_rank_mean"],
        )
    print(out_summary)


if __name__ == "__main__":
    main()

