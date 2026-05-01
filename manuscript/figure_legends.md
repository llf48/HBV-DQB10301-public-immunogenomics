# Figure Legends

## Figure 1. Study Workflow

Public HBV complete-genome GenBank records annotated as genotype B or genotype C
were downloaded from NCBI. Core protein CDS translations were extracted and
filtered to remove missing core sequences, recombinant records, abnormal core
lengths, and non-standard amino-acid sequences. Overlapping 15-mer core peptides
were collapsed into unique peptide windows and occurrence-weighted counts.
IEDB MHC-II NetMHCIIpan predictions were run for two DQB1*03:01-containing
HLA-DQ heterodimers and one DQB1*03:02 comparator. Binder rates, genotype-
stratified rates, Fisher exact tests, and peptide-position binding landscapes
were then generated.

## Figure 2. Predicted HBV Core Binder Rates By HLA-DQ Pair

Unique and occurrence-weighted predicted binder rates for HBV core 15-mers.
Predicted binders were defined as IEDB NetMHCIIpan percentile rank <10. The
DQA1*03:01/DQB1*03:02 comparator showed markedly higher predicted binding than
both DQB1*03:01-containing risk pairs.

File:
`results/figures/figure_core_binder_rates.png`

## Figure 3. Genotype-Stratified Occurrence-Weighted Binder Rates

Occurrence-weighted predicted binder rates were calculated separately for public
records queried as genotype B and genotype C. The DQB1*03:02 comparator showed
approximately 10% predicted binder rates in both genotype groups, whereas both
DQB1*03:01-containing heterodimers remained below 1% in occurrence-weighted
analyses.

File:
`results/figures/figure_core_genotype_binder_rates.png`

## Figure 4. Core-Position Binding Landscape

For each HBV core 15-mer window start position, the best percentile rank among
public sequence variants was plotted by HLA-DQ pair. Horizontal dashed and
dotted lines indicate rank <10 binder and rank <2 strong binder thresholds.
The DQB1*03:02 comparator shows more frequent low-rank binding windows than the
DQB1*03:01-containing heterodimers.

File:
`results/figures/figure_core_binding_landscape.png`

