# Project Handoff

Date: 2026-05-01

## Current State

The final submission-facing version is in `submission/`. The old 469-record
pilot is superseded by the full public genotype B/C GenBank expansion.

## Main Paper

Title:

**Public HBV genotype B/C core diversity reveals an HLA-DQB1*03:01-associated
class-II presentation gap**

Supported claim:

Public HBV genotype B/C core diversity preserves a predicted class-II binding
gap for DQB1*03:01-containing HLA-DQ heterodimers, with the strongest gap in
HBV core N-terminal 15-mer windows.

## Main Dataset

- Candidate public complete-genome genotype B/C HBV records: 3784.
- QC-passed genotype-labeled core records: 1576.
- Unique QC-passed accessions: 1538.
- Genotype B records after QC: 633.
- Genotype C records after QC: 943.
- Unique core 15-mers: 11176.
- Occurrence-weighted core windows: 259916.

## Main Results

- DQA1*03:01/DQB1*03:02: 9.55% unique binder rate, 10.52% occurrence-weighted.
- DQA1*05:08/DQB1*03:01: 1.10% unique binder rate, 0.23% occurrence-weighted.
- DQA1*06:01/DQB1*03:01: 1.26% unique binder rate, 0.80% occurrence-weighted.

Recommended-method sensitivity preserved the occurrence-weighted direction:

- DQA1*03:01/DQB1*03:02: 4.59%.
- DQA1*05:08/DQB1*03:01: 0.41%.
- DQA1*06:01/DQB1*03:01: 1.20%.

## Main Files

- `submission/HBV_DQB10301_core_gap_submission_manuscript.md`
- `submission/HBV_DQB10301_cover_letter.md`
- `submission/HBV_DQB10301_figure_legends.md`
- `submission/HBV_DQB10301_supplementary_note.md`
- `submission/tables/table_1_dataset_qc_summary.csv`
- `submission/tables/table_2_full_hla_dq_binder_summary.csv`

## Main Figures

- `results/figures/figure_1_full_expanded_dq_binder_rates.png`
- `results/figures/figure_2_method_sensitivity_primary_pairs.png`
- `results/figures/figure_3_redundancy_and_stratified_sensitivity.png`
- `results/figures/figure_4_core_position_presentation_gap.png`
- `results/figures/figure_5_iedb_core_mhcii_epitope_overlap.png`

## Commands To Rebuild The Final Submission Artifacts

```bash
python scripts/make_full_submission_figures.py
python scripts/build_submission_docx.py
```

For full computational reproduction, use the longer command list in
`submission/HBV_DQB10301_supplementary_note.md`.

## Remaining Manual Tasks Before Upload

- Add author names, affiliations, contributions, funding, and correspondence.
- Choose target journal and adjust formatting.
- Deposit code/data tables in a public repository and add the repository link.
- Review references in the target journal style.
