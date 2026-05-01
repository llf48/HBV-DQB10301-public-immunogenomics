import csv
from pathlib import Path

import matplotlib.pyplot as plt


PROJECT = Path(__file__).resolve().parents[1]
FIG = PROJECT / "results" / "figures"

LABELS = {
    "HLA-DQA1*06:01/DQB1*03:01": "DQ 03:01\n06:01/03:01",
    "HLA-DQA1*05:08/DQB1*03:01": "DQ 03:01\n05:08/03:01",
    "HLA-DQA1*03:01/DQB1*03:02": "DQ 03:02\n03:01/03:02",
    "HLA-DQA1*01:02/DQB1*06:02": "DQ 06:02\n01:02/06:02",
    "HLA-DQA1*01:01/DQB1*05:01": "DQ 05:01\n01:01/05:01",
    "HLA-DQA1*03:03/DQB1*04:01": "DQ 04:01\n03:03/04:01",
    "HLA-DQA1*05:01/DQB1*02:01": "DQ 02:01\n05:01/02:01",
}


def read_csv(path):
    return list(csv.DictReader(Path(path).open(newline="", encoding="utf-8")))


def color_for(row):
    if row.get("allele_group") == "risk_DQB1_0301":
        return "#c2410c"
    if row.get("allele") == "HLA-DQA1*03:01/DQB1*03:02":
        return "#2b6cb0"
    return "#6b7280"


def fig_expanded_dq():
    rows = read_csv(PROJECT / "results" / "tables" / "core_large_expanded_dq_netmhciipan_summary_by_allele.csv")
    rows = sorted(rows, key=lambda r: float(r["occurrence_binder_10_rate"]), reverse=True)
    x = range(len(rows))
    vals = [float(r["occurrence_binder_10_rate"]) * 100 for r in rows]
    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    bars = ax.bar(x, vals, color=[color_for(r) for r in rows])
    ax.bar_label(bars, fmt="%.2f", padding=2, fontsize=8)
    ax.set_ylabel("Occurrence-weighted binder rate (%)")
    ax.set_xticks(list(x), [LABELS[r["allele"]] for r in rows], rotation=25, ha="right")
    ax.set_ylim(0, max(vals) * 1.25)
    ax.set_title("Public HBV core diversity across an expanded HLA-DQ panel")
    plt.tight_layout()
    out = FIG / "figure_expanded_dq_core_binder_rates.png"
    fig.savefig(out, dpi=300)
    fig.savefig(FIG / "figure_expanded_dq_core_binder_rates.svg")
    plt.close(fig)
    print(out)


def fig_dedup():
    rows = read_csv(PROJECT / "results" / "tables" / "core_large_expanded_dq_dedup_sensitivity.csv")
    keep = {
        "HLA-DQA1*03:01/DQB1*03:02",
        "HLA-DQA1*05:08/DQB1*03:01",
        "HLA-DQA1*06:01/DQB1*03:01",
    }
    sets = ["all_qc", "exact_core", "greedy_99pct", "greedy_95pct"]
    alleles = [
        "HLA-DQA1*03:01/DQB1*03:02",
        "HLA-DQA1*05:08/DQB1*03:01",
        "HLA-DQA1*06:01/DQB1*03:01",
    ]
    rows = [r for r in rows if r["allele"] in keep]
    lookup = {(r["set_name"], r["allele"]): float(r["occurrence_binder_10_rate"]) * 100 for r in rows}
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    width = 0.24
    offsets = [-width, 0, width]
    colors = ["#2b6cb0", "#c2410c", "#047857"]
    for allele, offset, color in zip(alleles, offsets, colors):
        vals = [lookup[(s, allele)] for s in sets]
        bars = ax.bar([i + offset for i in range(len(sets))], vals, width=width, color=color, label=LABELS[allele].replace("\n", " "))
        ax.bar_label(bars, fmt="%.2f", padding=2, fontsize=7)
    ax.set_ylabel("Occurrence-weighted binder rate (%)")
    ax.set_xticks(range(len(sets)), ["All QC", "Exact core", "99% ID", "95% ID"])
    ax.set_ylim(0, 12)
    ax.legend(frameon=False, fontsize=8)
    ax.set_title("DQB1*03:01 core gap survives sequence de-redundancy")
    plt.tight_layout()
    out = FIG / "figure_dedup_sensitivity.png"
    fig.savefig(out, dpi=300)
    fig.savefig(FIG / "figure_dedup_sensitivity.svg")
    plt.close(fig)
    print(out)


def fig_reference_proteome():
    rows = read_csv(PROJECT / "results" / "tables" / "reference_proteome_expanded_dq_summary_by_protein_allele.csv")
    proteins = ["core_capsid", "x_protein", "large_envelope", "polymerase"]
    alleles = [
        "HLA-DQA1*03:01/DQB1*03:02",
        "HLA-DQA1*05:08/DQB1*03:01",
        "HLA-DQA1*06:01/DQB1*03:01",
        "HLA-DQA1*01:01/DQB1*05:01",
        "HLA-DQA1*01:02/DQB1*06:02",
        "HLA-DQA1*03:03/DQB1*04:01",
        "HLA-DQA1*05:01/DQB1*02:01",
    ]
    lookup = {(r["protein"], r["allele"]): float(r["binder_10_rate"]) * 100 for r in rows}
    matrix = [[lookup.get((p, a), 0) for a in alleles] for p in proteins]
    fig, ax = plt.subplots(figsize=(9.2, 4.2))
    im = ax.imshow(matrix, cmap="YlGnBu", vmin=0, vmax=max(max(row) for row in matrix))
    ax.set_yticks(range(len(proteins)), ["Core/capsid", "X", "Large envelope", "Polymerase"])
    ax.set_xticks(range(len(alleles)), [LABELS[a].replace("\n", " ") for a in alleles], rotation=25, ha="right")
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            ax.text(j, i, f"{value:.1f}", ha="center", va="center", fontsize=8)
    fig.colorbar(im, ax=ax, label="Reference proteome binder rate (%)")
    ax.set_title("Reference HBV proteome shows a core-specific DQB1*03:01 gap")
    plt.tight_layout()
    out = FIG / "figure_reference_proteome_binding_heatmap.png"
    fig.savefig(out, dpi=300)
    fig.savefig(FIG / "figure_reference_proteome_binding_heatmap.svg")
    plt.close(fig)
    print(out)


def fig_epitope_overlap():
    rows = read_csv(PROJECT / "results" / "tables" / "core_large_iedb_epitope_overlap_summary_by_allele.csv")
    rows = sorted(rows, key=lambda r: int(r["binder_overlap_core_tcell_mhc_ii"]), reverse=True)
    vals = [int(r["binder_overlap_core_tcell_mhc_ii"]) for r in rows]
    x = range(len(rows))
    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    bars = ax.bar(x, vals, color=[color_for(r) for r in rows])
    ax.bar_label(bars, padding=2, fontsize=8)
    ax.set_ylabel("Binder peptides overlapping known core MHC-II epitopes")
    ax.set_xticks(list(x), [LABELS[r["allele"]] for r in rows], rotation=25, ha="right")
    ax.set_title("Predicted DQB1*03:01 core binders miss known HBV core MHC-II epitopes")
    plt.tight_layout()
    out = FIG / "figure_iedb_core_mhcii_overlap.png"
    fig.savefig(out, dpi=300)
    fig.savefig(FIG / "figure_iedb_core_mhcii_overlap.svg")
    plt.close(fig)
    print(out)


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    fig_expanded_dq()
    fig_dedup()
    fig_reference_proteome()
    fig_epitope_overlap()


if __name__ == "__main__":
    main()
