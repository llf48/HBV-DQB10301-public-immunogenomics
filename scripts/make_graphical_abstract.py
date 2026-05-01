from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results" / "figures"


def box(ax, x, y, w, h, text, face, edge="#2f3a45", fontsize=12):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.035",
        linewidth=1.4,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color="#111827",
        linespacing=1.18,
    )


def arrow(ax, x1, y1, x2, y2):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=18,
            linewidth=1.5,
            color="#374151",
        )
    )


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(14, 6.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.93,
        "Public HBV core diversity reveals a DQB1*03:01 class-II presentation gap",
        ha="center",
        va="center",
        fontsize=17,
        weight="bold",
        color="#17324d",
    )

    y = 0.66
    w = 0.17
    h = 0.16
    xs = [0.04, 0.28, 0.52, 0.76]
    labels = [
        "NCBI GenBank\nHBV genotype B/C\ncomplete genomes",
        "QC and core CDS\ntranslation\n1576 records",
        "Core 15-mers\n11176 unique\n259916 windows",
        "IEDB MHC-II\nHLA-DQ prediction\n7 heterodimers",
    ]
    colors = ["#dbeafe", "#e0f2fe", "#dcfce7", "#fef3c7"]
    for x, label, color in zip(xs, labels, colors):
        box(ax, x, y, w, h, label, color)
    for left, right in zip(xs[:-1], xs[1:]):
        arrow(ax, left + w + 0.015, y + h / 2, right - 0.015, y + h / 2)

    box(
        ax,
        0.08,
        0.32,
        0.28,
        0.17,
        "DQB1*03:02 comparator\n10.52% occurrence-weighted\ncore binder rate",
        "#dbeafe",
        edge="#2166ac",
        fontsize=11,
    )
    box(
        ax,
        0.40,
        0.32,
        0.20,
        0.17,
        "presentation gap\n47.4x and 13.1x\nbootstrap rate ratios",
        "#f3f4f6",
        edge="#6b7280",
        fontsize=11,
    )
    box(
        ax,
        0.64,
        0.32,
        0.28,
        0.17,
        "DQB1*03:01 risk pairs\n0.23%-0.80% occurrence-weighted\ncore binder rates",
        "#fee2e2",
        edge="#b2182b",
        fontsize=11,
    )
    arrow(ax, 0.845, 0.66, 0.50, 0.50)
    arrow(ax, 0.36, 0.405, 0.40, 0.405)
    arrow(ax, 0.60, 0.405, 0.64, 0.405)

    box(
        ax,
        0.12,
        0.08,
        0.76,
        0.16,
        "Robust across de-redundancy, bootstrap, genotype/region/year strata, IEDB epitope overlap,\n"
        "and reference-proteome controls; strongest signal maps to HBV core N-terminal windows.",
        "#f3f4f6",
        edge="#6b7280",
        fontsize=12,
    )
    arrow(ax, 0.50, 0.32, 0.50, 0.24)

    fig.savefig(OUT / "graphical_abstract_workflow.png", dpi=600, bbox_inches="tight")
    fig.savefig(OUT / "graphical_abstract_workflow.svg", bbox_inches="tight")
    plt.close(fig)
    print(OUT / "graphical_abstract_workflow.png")


if __name__ == "__main__":
    main()
