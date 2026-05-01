import csv
from pathlib import Path

import matplotlib.pyplot as plt


PROJECT = Path(__file__).resolve().parents[1]
FIG = PROJECT / "results" / "figures"
SUMMARY = PROJECT / "results" / "tables" / "core_large_gap_summary_by_allele.csv"
GENO = PROJECT / "results" / "tables" / "core_large_gap_summary_by_allele_genotype.csv"
WINDOW = PROJECT / "results" / "tables" / "core_large_window_min_rank.csv"


LABELS = {
    "HLA-DQA1*03:01/DQB1*03:02": "DQ 03:02\nDQA1*03:01/DQB1*03:02",
    "HLA-DQA1*05:08/DQB1*03:01": "DQ 03:01 risk\nDQA1*05:08/DQB1*03:01",
    "HLA-DQA1*06:01/DQB1*03:01": "DQ 03:01 risk\nDQA1*06:01/DQB1*03:01",
}
ORDER = [
    "HLA-DQA1*03:01/DQB1*03:02",
    "HLA-DQA1*05:08/DQB1*03:01",
    "HLA-DQA1*06:01/DQB1*03:01",
]
COLORS = {
    "control": "#2b6cb0",
    "risk_a": "#c2410c",
    "risk_b": "#047857",
    "unique": "#4c78a8",
    "occurrence": "#f58518",
    "genotype_b": "#4c78a8",
    "genotype_c": "#e45756",
}


def read_csv(path):
    return list(csv.DictReader(path.open(newline="", encoding="utf-8")))


def fig_binder_rates():
    rows = read_csv(SUMMARY)
    rows = sorted(rows, key=lambda r: ORDER.index(r["allele"]))
    labels = [LABELS[r["allele"]] for r in rows]
    unique = [float(r["unique_binder_10_rate"]) * 100 for r in rows]
    occurrence = [float(r["occurrence_binder_10_rate"]) * 100 for r in rows]

    x = range(len(rows))
    width = 0.36
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    bars1 = ax.bar(
        [i - width / 2 for i in x],
        unique,
        width=width,
        label="Unique peptides",
        color=COLORS["unique"],
    )
    bars2 = ax.bar(
        [i + width / 2 for i in x],
        occurrence,
        width=width,
        label="Occurrence-weighted",
        color=COLORS["occurrence"],
    )
    plt.ylabel("Predicted binder rate (% rank < 10)")
    plt.xticks(list(x), labels, rotation=20, ha="right")
    plt.ylim(0, max(max(unique), max(occurrence)) * 1.25)
    ax.bar_label(bars1, fmt="%.1f", padding=2, fontsize=8)
    ax.bar_label(bars2, fmt="%.1f", padding=2, fontsize=8)
    plt.legend(frameon=False, loc="upper right")
    plt.tight_layout()
    out = FIG / "figure_core_binder_rates.png"
    plt.savefig(out, dpi=300)
    plt.savefig(FIG / "figure_core_binder_rates.svg")
    plt.close()
    print(out)


def fig_genotype_rates():
    rows = read_csv(GENO)
    alleles = [a for a in ORDER if a in set(r["allele"] for r in rows)]
    genotypes = ["B", "C"]
    x = range(len(alleles))
    width = 0.36
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    for offset, genotype in [(-width / 2, "B"), (width / 2, "C")]:
        vals = []
        for allele in alleles:
            match = next(r for r in rows if r["allele"] == allele and r["genotype"] == genotype)
            vals.append(float(match["occurrence_binder_10_rate"]) * 100)
        bars = ax.bar(
            [i + offset for i in x],
            vals,
            width=width,
            label=f"Genotype {genotype}",
            color=COLORS["genotype_b"] if genotype == "B" else COLORS["genotype_c"],
        )
        ax.bar_label(bars, fmt="%.2f", padding=2, fontsize=8)
    plt.ylabel("Occurrence-weighted binder rate (%)")
    plt.xticks(list(x), [LABELS[a] for a in alleles], rotation=20, ha="right")
    plt.legend(frameon=False)
    plt.ylim(0, 12)
    plt.tight_layout()
    out = FIG / "figure_core_genotype_binder_rates.png"
    plt.savefig(out, dpi=300)
    plt.savefig(FIG / "figure_core_genotype_binder_rates.svg")
    plt.close()
    print(out)


def fig_window_landscape():
    rows = read_csv(WINDOW)
    by_allele = {}
    for row in rows:
        by_allele.setdefault(row["allele"], []).append(row)

    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    colors = [COLORS["control"], COLORS["risk_a"], COLORS["risk_b"]]
    for color, allele in zip(colors, ORDER):
        vals = by_allele[allele]
        vals = sorted(vals, key=lambda r: int(r["window_start"]))
        x = [int(r["window_start"]) for r in vals]
        y = [min(float(r["min_rank"]), 50.0) for r in vals]
        ax.plot(x, y, label=LABELS[allele].replace("\n", " "), linewidth=1.8, color=color)
    plt.axhline(10, color="black", linestyle="--", linewidth=1, label="Binder cutoff")
    plt.axhline(2, color="gray", linestyle=":", linewidth=1, label="Strong cutoff")
    plt.ylabel("Best percentile rank per core window")
    plt.xlabel("HBV core 15-mer window start")
    plt.ylim(0, 50)
    plt.legend(frameon=False, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.18))
    plt.tight_layout()
    out = FIG / "figure_core_binding_landscape.png"
    plt.savefig(out, dpi=300, bbox_inches="tight")
    plt.savefig(FIG / "figure_core_binding_landscape.svg", bbox_inches="tight")
    plt.close()
    print(out)


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    fig_binder_rates()
    fig_genotype_rates()
    fig_window_landscape()


if __name__ == "__main__":
    main()
