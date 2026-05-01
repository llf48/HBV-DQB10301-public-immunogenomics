# Submission Checklist

Date: 2026-05-01

## Core Rebuild Commands

```bash
python scripts/make_full_submission_figures.py
python scripts/build_submission_docx.py
```

The full computational reproduction command list is in
`submission/HBV_DQB10301_supplementary_note.md`.

## Final Manuscript Files

- `submission/HBV_DQB10301_core_gap_submission_manuscript.md`
- `submission/HBV_DQB10301_core_gap_submission_manuscript.docx`
- `submission/HBV_DQB10301_cover_letter.md`
- `submission/HBV_DQB10301_cover_letter.docx`
- `submission/HBV_DQB10301_figure_legends.md`
- `submission/HBV_DQB10301_figure_legends.docx`
- `submission/HBV_DQB10301_supplementary_note.md`
- `submission/HBV_DQB10301_supplementary_note.docx`

## Final Figures

- `results/figures/figure_1_full_expanded_dq_binder_rates.png`
- `results/figures/figure_2_method_sensitivity_primary_pairs.png`
- `results/figures/figure_3_redundancy_and_stratified_sensitivity.png`
- `results/figures/figure_4_core_position_presentation_gap.png`
- `results/figures/figure_5_iedb_core_mhcii_epitope_overlap.png`
- `results/figures/figure_reference_proteome_binding_heatmap.png`
- `results/figures/figure_core_binding_landscape.png`

## Final Tables

- `submission/tables/table_1_dataset_qc_summary.csv`
- `submission/tables/table_2_full_hla_dq_binder_summary.csv`
- `submission/tables/supplementary_table_pairwise_fisher_tests.csv`
- `submission/tables/supplementary_table_method_sensitivity_recommended.csv`
- `submission/tables/supplementary_table_top_core_position_gaps.csv`
- `submission/tables/supplementary_table_region_counts.csv`

## Manual Items Before Journal Upload

- Add author names and affiliations.
- Add correspondence email.
- Add author contributions.
- Add funding statement.
- Confirm conflicts-of-interest wording.
- Choose a target journal and adapt abstract/reference/figure style.
- Deposit scripts, processed tables, and figure sources in a public repository.
  Completed: https://github.com/llf48/HBV-DQB10301-public-immunogenomics.
- Archive a frozen release DOI.
  Completed: https://doi.org/10.5281/zenodo.19956882.

## Claim Check

The manuscript is safe if it says:

**predicted HLA-DQ binding gap**

It becomes unsafe if it says:

**proven antigen presentation loss**, **proven CD4 T-cell failure**, or
**proven HCC mechanism**.
