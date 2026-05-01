# Figure Legends

## Graphical Abstract

Public NCBI GenBank HBV genotype B/C complete-genome records were filtered for
quality-controlled core/capsid translations, converted into overlapping 15-mer
windows, predicted against an expanded HLA-DQ heterodimer panel using IEDB
NetMHCIIpan workflows, and tested for a DQB1*03:01-associated class-II
presentation gap with method sensitivity, de-redundancy, bootstrap,
stratification, IEDB epitope overlap, and reference-proteome controls.

File: `submission_viruses/figures/graphical_abstract_workflow.png`

## Figure 1. Public HBV core binder rates across an expanded HLA-DQ panel

Unique-peptide and occurrence-weighted predicted binder rates for 11176 public
HBV genotype B/C core 15-mer windows across seven HLA-DQ heterodimers.
Predicted binders were defined as IEDB NetMHCIIpan percentile rank <10.
DQB1*03:01-containing heterodimers were consistent low-binding outliers
relative to the DQB1*03:02 comparator and other non-risk HLA-DQ comparison
molecules.

File: `submission_viruses/figures/figure_1_full_expanded_dq_binder_rates.png`

## Figure 2. Method sensitivity for the primary HLA-DQ comparison

Occurrence-weighted predicted binder rates for the DQB1*03:02 comparator and
two DQB1*03:01-containing risk heterodimers using NetMHCIIpan BA and the IEDB
recommended method. The recommended method produced lower absolute binder
rates, but the DQB1*03:02 comparator remained higher than both
DQB1*03:01-containing pairs in occurrence-weighted analyses.

File: `submission_viruses/figures/figure_2_method_sensitivity_primary_pairs.png`

## Figure 3. De-redundancy and stratified sensitivity analyses

Panel A shows occurrence-weighted core binder rates for the primary
DQB1*03:02 comparator and the two DQB1*03:01-containing heterodimers after no
de-redundancy, exact core protein de-duplication, greedy 99% identity
de-redundancy, and greedy 95% identity de-redundancy. Panel B shows
stratum-specific rate ratios comparing DQA1*03:01/DQB1*03:02 with each
DQB1*03:01-containing risk pair across genotype, region, and collection-year
strata. The presentation gap persisted across these sensitivity analyses.

File: `submission_viruses/figures/figure_3_redundancy_and_stratified_sensitivity.png`

## Figure 4. Core-position presentation gap

For each HBV core 15-mer window start position, occurrence-weighted predicted
binder rates were plotted for DQA1*03:01/DQB1*03:02 and the combined
DQB1*03:01-containing risk pairs. The shaded region shows the presentation gap
where the DQB1*03:02 comparator exceeds the combined risk-pair rate. The
largest gap localized to N-terminal core windows, especially positions 2-27.

File: `submission_viruses/figures/figure_4_core_position_presentation_gap.png`

## Figure 5. Overlap with known IEDB human HBV core MHC-II epitopes

IEDB human positive HBV T-cell epitope records were retrieved through the IEDB
query API. Bars show the number of predicted binder peptides overlapping known
core/nucleocapsid MHC-II epitopes for NetMHCIIpan BA and IEDB recommended
predictions. NetMHCIIpan-predicted DQB1*03:01 core binders did not overlap
known core/nucleocapsid MHC-II epitopes, whereas the DQB1*03:02 comparator did.

File: `submission_viruses/figures/figure_5_iedb_core_mhcii_epitope_overlap.png`

## Supplementary Figure S1. Reference HBV proteome control

Reference HBV NC_003977.2 polymerase, large envelope, X protein, and
core/capsid peptides were predicted against the expanded HLA-DQ panel. Heatmap
values show binder rates at percentile rank <10. DQB1*03:01-containing
heterodimers retained predicted binding to X, envelope, and polymerase peptides
but showed zero predicted binders for reference core/capsid peptides.

File: `submission_viruses/figures/figure_reference_proteome_binding_heatmap.png`
