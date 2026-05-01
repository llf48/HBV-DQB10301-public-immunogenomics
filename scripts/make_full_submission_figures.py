import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


PROJECT = Path(__file__).resolve().parents[1]
TABLES = PROJECT / "results" / "tables"
FIGURES = PROJECT / "results" / "figures"

PRIMARY = "HLA-DQA1*03:01/DQB1*03:02"
RISK_A = "HLA-DQA1*05:08/DQB1*03:01"
RISK_B = "HLA-DQA1*06:01/DQB1*03:01"

LABELS = {
    "HLA-DQA1*01:01/DQB1*05:01": "DQA1*01:01\nDQB1*05:01",
    "HLA-DQA1*01:02/DQB1*06:02": "DQA1*01:02\nDQB1*06:02",
    "HLA-DQA1*03:01/DQB1*03:02": "DQA1*03:01\nDQB1*03:02",
    "HLA-DQA1*03:03/DQB1*04:01": "DQA1*03:03\nDQB1*04:01",
    "HLA-DQA1*05:01/DQB1*02:01": "DQA1*05:01\nDQB1*02:01",
    "HLA-DQA1*05:08/DQB1*03:01": "DQA1*05:08\nDQB1*03:01",
    "HLA-DQA1*06:01/DQB1*03:01": "DQA1*06:01\nDQB1*03:01",
}

COLORS = {
    "primary": "#2166ac",
    "risk_a": "#b2182b",
    "risk_b": "#1b7837",
    "control": "#6b7280",
    "recommended": "#f4a261",
    "netmhcii": "#2a9d8f",
    "grid": "#d1d5db",
}


def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def pct(value):
    return 100.0 * float(value)


def style_ax(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", color=COLORS["grid"], linewidth=0.6, alpha=0.65)
    ax.set_axisbelow(True)


def save(fig, stem):
    FIGURES.mkdir(parents=True, exist_ok=True)
    png = FIGURES / f"{stem}.png"
    svg = FIGURES / f"{stem}.svg"
    fig.savefig(png, dpi=600, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)
    print(png)
    print(svg)


def allele_color(allele):
    if allele == PRIMARY:
        return COLORS["primary"]
    if allele == RISK_A:
        return COLORS["risk_a"]
    if allele == RISK_B:
        return COLORS["risk_b"]
    return COLORS["control"]


def figure_1_expanded_panel():
    rows = read_csv(TABLES / "core_full_expanded_dq_netmhciipan_summary_by_allele.csv")
    rows = sorted(rows, key=lambda row: float(row["occurrence_binder_10_rate"]), reverse=True)
    alleles = [row["allele"] for row in rows]
    unique = [pct(row["unique_binder_10_rate"]) for row in rows]
    occurrence = [pct(row["occurrence_binder_10_rate"]) for row in rows]

    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    x = np.arange(len(rows))
    width = 0.34
    bars1 = ax.bar(x - width / 2, unique, width=width, color="#8da0cb", label="Unique 15-mers")
    bars2 = ax.bar(x + width / 2, occurrence, width=width, color=[allele_color(a) for a in alleles], label="Occurrence-weighted")
    for bars in [bars1, bars2]:
        ax.bar_label(bars, fmt="%.1f", fontsize=7, padding=1.5)
    ax.set_ylabel("Predicted binder rate, rank < 10 (%)")
    ax.set_xticks(x, [LABELS[a] for a in alleles], rotation=28, ha="right")
    ax.set_ylim(0, max(unique + occurrence) * 1.23)
    ax.legend(frameon=False, loc="upper right", fontsize=8)
    style_ax(ax)
    save(fig, "figure_1_full_expanded_dq_binder_rates")


def figure_2_method_sensitivity():
    ba_rows = read_csv(TABLES / "core_full_expanded_dq_netmhciipan_summary_by_allele.csv")
    rec_rows = read_csv(TABLES / "core_full_iedb_recommended_summary_by_allele.csv")
    alleles = [PRIMARY, RISK_A, RISK_B]
    ba = {row["allele"]: pct(row["occurrence_binder_10_rate"]) for row in ba_rows}
    rec = {row["allele"]: pct(row["occurrence_binder_10_rate"]) for row in rec_rows}

    fig, ax = plt.subplots(figsize=(5.8, 4.0))
    x = np.arange(len(alleles))
    width = 0.34
    bars1 = ax.bar(x - width / 2, [ba[a] for a in alleles], width=width, color=COLORS["netmhcii"], label="NetMHCIIpan BA")
    bars2 = ax.bar(x + width / 2, [rec[a] for a in alleles], width=width, color=COLORS["recommended"], label="IEDB recommended")
    ax.bar_label(bars1, fmt="%.2f", fontsize=7, padding=1.5)
    ax.bar_label(bars2, fmt="%.2f", fontsize=7, padding=1.5)
    ax.set_ylabel("Occurrence-weighted binder rate (%)")
    ax.set_xticks(x, [LABELS[a] for a in alleles], rotation=20, ha="right")
    ax.set_ylim(0, max([*ba.values(), *rec.values()]) * 1.24)
    ax.legend(frameon=False, fontsize=8)
    style_ax(ax)
    save(fig, "figure_2_method_sensitivity_primary_pairs")


def figure_3_redundancy_and_strata():
    dedup_rows = read_csv(TABLES / "core_full_expanded_dq_dedup_sensitivity.csv")
    strata_rows = read_csv(TABLES / "core_full_expanded_dq_stratified_sensitivity.csv")
    alleles = [PRIMARY, RISK_A, RISK_B]
    set_order = ["all_qc", "exact_core", "greedy_99pct", "greedy_95pct"]
    set_labels = ["All QC", "Exact core", "99% ID", "95% ID"]

    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.1), gridspec_kw={"width_ratios": [1.05, 1.2]})
    ax = axes[0]
    lookup = {(row["set_name"], row["allele"]): pct(row["occurrence_binder_10_rate"]) for row in dedup_rows}
    x = np.arange(len(set_order))
    width = 0.24
    for offset, allele in zip([-width, 0, width], alleles):
        bars = ax.bar(
            x + offset,
            [lookup[(set_name, allele)] for set_name in set_order],
            width=width,
            color=allele_color(allele),
            label=LABELS[allele].replace("\n", "/"),
        )
        ax.bar_label(bars, fmt="%.2f", fontsize=6.5, padding=1.5)
    ax.set_xticks(x, set_labels)
    ax.set_ylabel("Occurrence-weighted binder rate (%)")
    ax.set_ylim(0, 12)
    ax.legend(frameon=False, fontsize=7, loc="upper right")
    ax.text(-0.14, 1.02, "A", transform=ax.transAxes, fontsize=12, fontweight="bold")
    style_ax(ax)

    selected = [
        ("query_genotype", "B", "Genotype B"),
        ("query_genotype", "C", "Genotype C"),
        ("region", "East Asia", "East Asia"),
        ("region", "Southeast Asia", "Southeast Asia"),
        ("region", "South Asia", "South Asia"),
        ("year_bin", "2005-2010", "2005-2010"),
        ("year_bin", "2011-2015", "2011-2015"),
        ("year_bin", "2016+", "2016+"),
    ]
    lookup_s = {
        (row["stratum_type"], row["stratum"], row["allele"]): float(row["occurrence_binder_10_rate"])
        for row in strata_rows
    }
    y = np.arange(len(selected))
    ax = axes[1]
    for risk, color, marker, label in [
        (RISK_A, COLORS["risk_a"], "o", "Primary / 05:08-03:01"),
        (RISK_B, COLORS["risk_b"], "s", "Primary / 06:01-03:01"),
    ]:
        ratios = []
        for stype, stratum, _ in selected:
            primary_rate = lookup_s[(stype, stratum, PRIMARY)]
            risk_rate = lookup_s[(stype, stratum, risk)]
            ratios.append(primary_rate / risk_rate if risk_rate else np.nan)
        ax.scatter(ratios, y, color=color, marker=marker, s=38, label=label, zorder=3)
        for ratio, yy in zip(ratios, y):
            ax.plot([1, ratio], [yy, yy], color=color, alpha=0.3, linewidth=1.0)
    ax.axvline(1, color="black", linestyle="--", linewidth=0.8)
    ax.set_xscale("log")
    ax.set_xlabel("Rate ratio vs DQB1*03:01 risk pair (log scale)")
    ax.set_yticks(y, [label for _, _, label in selected])
    ax.invert_yaxis()
    ax.legend(frameon=False, fontsize=7, loc="upper right")
    ax.text(-0.18, 1.02, "B", transform=ax.transAxes, fontsize=12, fontweight="bold")
    ax.grid(axis="x", color=COLORS["grid"], linewidth=0.6, alpha=0.65)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "figure_3_redundancy_and_stratified_sensitivity")


def figure_4_position_gap():
    rows = read_csv(TABLES / "core_full_expanded_dq_position_gap_summary.csv")
    rows = sorted(rows, key=lambda row: int(row["window_start"]))
    x = [int(row["window_start"]) for row in rows]
    primary = [pct(row["primary_occurrence_rate"]) for row in rows]
    risk = [pct(row["risk_occurrence_rate"]) for row in rows]
    gap = [pct(row["gap_primary_minus_risk"]) for row in rows]

    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    ax.plot(x, primary, color=COLORS["primary"], linewidth=1.9, label="DQB1*03:02 primary")
    ax.plot(x, risk, color=COLORS["risk_a"], linewidth=1.7, label="Combined DQB1*03:01 risk pairs")
    ax.fill_between(x, risk, primary, where=np.array(gap) > 0, color="#d8b365", alpha=0.28, label="Presentation gap")
    ax.set_xlabel("HBV core 15-mer window start")
    ax.set_ylabel("Occurrence-weighted binder rate (%)")
    ax.set_ylim(0, 105)
    ax.set_xlim(min(x), max(x))
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    ax.annotate(
        "N-terminal gap\nwindows 2-27",
        xy=(12, 99),
        xytext=(44, 83),
        arrowprops={"arrowstyle": "->", "linewidth": 0.8, "color": "black"},
        fontsize=8,
    )
    style_ax(ax)
    save(fig, "figure_4_core_position_presentation_gap")


def figure_5_epitope_overlap():
    ba_rows = read_csv(TABLES / "core_full_expanded_dq_iedb_epitope_overlap_summary_by_allele.csv")
    rec_rows = read_csv(TABLES / "core_full_iedb_recommended_iedb_epitope_overlap_summary_by_allele.csv")
    alleles = [PRIMARY, RISK_A, RISK_B]
    ba = {row["allele"]: int(row["binder_overlap_core_tcell_mhc_ii"]) for row in ba_rows}
    rec = {row["allele"]: int(row["binder_overlap_core_tcell_mhc_ii"]) for row in rec_rows}
    fig, ax = plt.subplots(figsize=(5.7, 3.8))
    x = np.arange(len(alleles))
    width = 0.34
    bars1 = ax.bar(x - width / 2, [ba[a] for a in alleles], width=width, color=COLORS["netmhcii"], label="NetMHCIIpan BA")
    bars2 = ax.bar(x + width / 2, [rec[a] for a in alleles], width=width, color=COLORS["recommended"], label="IEDB recommended")
    ax.bar_label(bars1, fontsize=7, padding=1.5)
    ax.bar_label(bars2, fontsize=7, padding=1.5)
    ax.set_ylabel("Predicted binders overlapping known\nHBV core MHC-II T-cell epitopes")
    ax.set_xticks(x, [LABELS[a] for a in alleles], rotation=20, ha="right")
    ax.set_ylim(0, max([*ba.values(), *rec.values(), 1]) * 1.25)
    ax.legend(frameon=False, fontsize=8)
    style_ax(ax)
    save(fig, "figure_5_iedb_core_mhcii_epitope_overlap")


def export_submission_tables():
    out = PROJECT / "submission" / "tables"
    out.mkdir(parents=True, exist_ok=True)

    qc_rows = read_csv(PROJECT / "data" / "processed" / "core_full_record_qc.csv")
    passed = [row for row in qc_rows if row["passes_qc"].lower() == "true"]
    unique_accessions = sorted({row["accession"] for row in passed})
    genotype_counts = {}
    region_counts = {}
    for row in passed:
        genotype_counts[row["query_genotype"]] = genotype_counts.get(row["query_genotype"], 0) + 1
        region = row.get("region") or "Unknown"
        region_counts[region] = region_counts.get(region, 0) + 1

    meta_rows = read_csv(PROJECT / "data" / "processed" / "core_full_unique_15mer_metadata.csv")
    occurrence_total = sum(int(row["source_count"]) for row in meta_rows)
    dataset_rows = [
        {"metric": "NCBI complete HBV genotype B/C records retrieved", "value": len(qc_rows)},
        {"metric": "QC-passed genotype-labeled core records", "value": len(passed)},
        {"metric": "Unique QC-passed accessions", "value": len(unique_accessions)},
        {"metric": "Unique HBV core 15-mers", "value": len(meta_rows)},
        {"metric": "Occurrence-weighted HBV core 15-mer windows", "value": occurrence_total},
        {"metric": "QC-passed genotype B records", "value": genotype_counts.get("B", 0)},
        {"metric": "QC-passed genotype C records", "value": genotype_counts.get("C", 0)},
    ]
    write_csv(out / "table_1_dataset_qc_summary.csv", dataset_rows)

    hla_rows = read_csv(TABLES / "core_full_expanded_dq_netmhciipan_summary_by_allele.csv")
    hla_rows = sorted(hla_rows, key=lambda row: float(row["occurrence_binder_10_rate"]), reverse=True)
    write_csv(out / "table_2_full_hla_dq_binder_summary.csv", hla_rows)

    top_gap = read_csv(TABLES / "core_full_expanded_dq_top_position_gaps.csv")[:30]
    write_csv(out / "supplementary_table_top_core_position_gaps.csv", top_gap)

    fisher = read_csv(TABLES / "core_full_expanded_dq_netmhciipan_pairwise_fisher_vs_primary.csv")
    write_csv(out / "supplementary_table_pairwise_fisher_tests.csv", fisher)

    recommended = read_csv(TABLES / "core_full_iedb_recommended_summary_by_allele.csv")
    write_csv(out / "supplementary_table_method_sensitivity_recommended.csv", recommended)

    region_rows = [
        {"region": region, "qc_passed_records": count}
        for region, count in sorted(region_counts.items(), key=lambda item: item[1], reverse=True)
    ]
    write_csv(out / "supplementary_table_region_counts.csv", region_rows)


def main():
    plt.rcParams.update(
        {
            "font.size": 9,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 10,
            "figure.dpi": 120,
            "savefig.facecolor": "white",
            "svg.fonttype": "none",
            "font.family": "DejaVu Sans",
        }
    )
    figure_1_expanded_panel()
    figure_2_method_sensitivity()
    figure_3_redundancy_and_strata()
    figure_4_position_gap()
    figure_5_epitope_overlap()
    export_submission_tables()


if __name__ == "__main__":
    main()
