# Publication Chart QA for Viruses Submission

Audit date: 2026-05-01

Skill framework used: `publication-chart-skill` from GitHub, plus local
`pubfig` / `pubtab` availability checks.

## Tool Check

- `pubfig --help`: available.
- `pubtab --help`: available.
- Figures are generated from reproducible Python scripts, not manually edited.
- Main figures and graphical abstract are exported as both PNG and SVG.

## Export Check

| Artifact | PNG dimensions | Role | QA status |
|---|---:|---|---|
| graphical_abstract_workflow.png | 6630 x 3123 | Graphical abstract / workflow | Pass |
| figure_1_full_expanded_dq_binder_rates.png | 3928 x 2518 | Main Figure 1 | Pass |
| figure_2_method_sensitivity_primary_pairs.png | 3104 x 2369 | Main Figure 2 | Pass |
| figure_3_redundancy_and_stratified_sensitivity.png | 5440 x 2391 | Main Figure 3 | Pass |
| figure_4_core_position_presentation_gap.png | 4273 x 2323 | Main Figure 4 | Pass |
| figure_5_iedb_core_mhcii_epitope_overlap.png | 3162 x 2308 | Main Figure 5 | Pass |
| figure_reference_proteome_binding_heatmap.png | 2760 x 1260 | Supplementary Figure S1 | Pass |

All regenerated main PNG files use 600 dpi export settings in
`scripts/make_full_submission_figures.py`.

## Panel Logic

- Figure 1 answers the core descriptive question: are DQB1*03:01-containing
  heterodimers outliers in an expanded HLA-DQ panel?
- Figure 2 tests whether the result depends on the prediction method.
- Figure 3 tests whether the result is explained by GenBank redundancy,
  genotype, region, or collection-year structure.
- Figure 4 localizes the aggregate gap to HBV core positions.
- Figure 5 links the predicted gap to known human HBV core/nucleocapsid MHC-II
  epitope coverage.
- Supplementary Figure S1 checks whether the gap is core-specific rather than a
  global failure of DQB1*03:01-containing heterodimers to bind HBV peptides.

This sequence moves from primary observation to robustness to biological
interpretation, which is the strongest figure logic for a computational
Viruses Article.

## Visual QA

- Avoids a one-color palette: non-risk and DQB1*03:01-containing pairs are
  visually separated while preserving neutral scientific styling.
- Fonts were increased for axis labels, ticks, and legends after final figure
  review.
- Graphical abstract uses a left-to-right workflow and a separated three-box
  result comparison, making it understandable independent of the manuscript.
- No figure relies on red/green as the only distinction.
- Captions define prediction method, binder threshold, comparison groups, and
  interpretation.

## Table QA

- Tables are delivered as machine-readable CSV files.
- Main submission tables include dataset QC and expanded HLA-DQ binder summary.
- Supplementary tables include pairwise tests, de-redundancy, bootstrap,
  stratification, position gaps, IEDB overlap, method sensitivity, reference
  proteome controls, and region counts.
- No table is image-only.

## Remaining Optional Upgrade

If the target submission system requests editable figure source, the SVG files
in `submission_viruses/figures/` should be uploaded together with PNG files or
retained for production after acceptance.
