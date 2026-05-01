# Submission Package Index

## Final Article Decision

The initial mutation-specific presentation-loss hypothesis was tested and
downgraded because the public-data pilots did not support it as the main claim.
The strongest supported paper is now:

**Public HBV genotype B/C core diversity preserves an HLA-DQB1*03:01-associated
class-II antigen-presentation gap.**

This is a computational, hypothesis-generating public-data paper. It should not
claim experimental antigen processing, surface presentation, CD4 T-cell
recognition, or HBV-HCC causality.

## Main Evidence Chain

- Public complete-genome GenBank candidates downloaded: 3784.
- QC-passed genotype-labeled HBV core records: 1576.
- Unique QC-passed accessions: 1538.
- Genotype labels after QC: 633 genotype B and 943 genotype C.
- Unique HBV core 15-mer windows: 11176.
- Occurrence-weighted core peptide windows: 259916.
- Main prediction method: IEDB MHC-II API, NetMHCIIpan.
- Expanded HLA-DQ panel: seven heterodimers, including two DQB1*03:01 risk
  pairs, one DQB1*03:02 comparator, and four additional common comparator
  pairs.

At rank <10, occurrence-weighted binder rates across public genotype B/C core
diversity were:

| HLA-DQ pair | Unique binder rate | Occurrence-weighted binder rate |
| --- | ---: | ---: |
| DQA1*01:01/DQB1*05:01 | 15.64% | 13.52% |
| DQA1*03:01/DQB1*03:02 | 9.55% | 10.52% |
| DQA1*01:02/DQB1*06:02 | 10.79% | 10.20% |
| DQA1*05:01/DQB1*02:01 | 10.20% | 9.04% |
| DQA1*03:03/DQB1*04:01 | 8.24% | 7.66% |
| DQA1*06:01/DQB1*03:01 | 1.26% | 0.80% |
| DQA1*05:08/DQB1*03:01 | 1.10% | 0.23% |

Primary Fisher tests versus DQA1*03:01/DQB1*03:02:

- DQA1*03:01/DQB1*03:02 vs DQA1*05:08/DQB1*03:01:
  unique OR 9.48, P = 2.29e-197; occurrence-weighted OR 52.02, P < 1e-300.
- DQA1*03:01/DQB1*03:02 vs DQA1*06:01/DQB1*03:01:
  unique OR 8.26, P = 3.27e-185; occurrence-weighted OR 14.50, P < 1e-300.

## Robustness Upgrades

- Method sensitivity using IEDB recommended method preserved the
  occurrence-weighted direction, although absolute rates changed.
- Exact-core and greedy 99%/95% de-redundancy preserved the DQB1*03:01 gap.
- Record-level bootstrap showed stable rate-ratio separation.
- Genotype, region, country, year-bin, and leave-one-stratum-out sensitivity
  analyses preserved the main direction.
- IEDB human HBV T-cell overlap showed no NetMHCIIpan-predicted overlap between
  DQB1*03:01 core binders and known core/nucleocapsid MHC-II epitopes in the
  pulled IEDB set.
- Core-position analysis localized the strongest gap to HBV core N-terminal
  windows, especially positions 2-27.
- Reference HBV proteome controls showed that the DQB1*03:01 deficit is
  strongest for core/capsid and is not a global inability to bind HBV peptides.

## Submission Files

- Main manuscript: `submission/HBV_DQB10301_core_gap_submission_manuscript.md`
- Cover letter: `submission/HBV_DQB10301_cover_letter.md`
- Figure legends: `submission/HBV_DQB10301_figure_legends.md`
- Supplementary methods note: `submission/HBV_DQB10301_supplementary_note.md`
- Final upgrade summary: `docs/upgrade_summary.md`
- Skill usage register: `docs/skill_usage_register.md`

DOCX versions are placed in the same `submission/` directory after
`python scripts/build_submission_docx.py`.

## Submission Figures

- `results/figures/figure_1_full_expanded_dq_binder_rates.png`
- `results/figures/figure_2_method_sensitivity_primary_pairs.png`
- `results/figures/figure_3_redundancy_and_stratified_sensitivity.png`
- `results/figures/figure_4_core_position_presentation_gap.png`
- `results/figures/figure_5_iedb_core_mhcii_epitope_overlap.png`
- `results/figures/figure_reference_proteome_binding_heatmap.png`
- `results/figures/figure_core_binding_landscape.png`

## Main Tables

- `results/tables/core_full_expanded_dq_netmhciipan_summary_by_allele.csv`
- `results/tables/core_full_expanded_dq_netmhciipan_pairwise_fisher_vs_primary.csv`
- `results/tables/core_full_expanded_dq_dedup_sensitivity.csv`
- `results/tables/core_full_expanded_dq_record_bootstrap.csv`
- `results/tables/core_full_expanded_dq_stratified_sensitivity.csv`
- `results/tables/core_full_expanded_dq_position_gap_summary.csv`
- `results/tables/core_full_iedb_recommended_summary_by_allele.csv`
- `results/tables/core_full_expanded_dq_iedb_epitope_overlap_summary_by_allele.csv`
- `results/tables/reference_proteome_expanded_dq_summary_by_protein_allele.csv`

## Bottom Line

The project now has a defensible narrow innovation point: it extends the
reported DQB1*03:01/HBV-HCC association into a public-virus-diversity question
and shows that the predicted core/capsid class-II binding gap is robust across
genotype B/C sequence diversity, comparator HLA-DQ pairs, de-redundancy,
bootstrapping, stratified sensitivity analyses, IEDB epitope overlap, and
reference-proteome controls.
