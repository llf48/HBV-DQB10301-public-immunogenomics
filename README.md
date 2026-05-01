# HBV DQ3 Public Immunogenomics

This project developed through iterative public-data testing. The initial
hypothesis was that HCC-associated HBV coding mutations might create
DQB1*03:01-specific MHC-II binding loss. Pilot analyses did not support that as
the main paper.

The final, stronger article focus is:

**Public HBV genotype B/C core diversity preserves an HLA-DQB1*03:01-associated
class-II antigen-presentation gap.**

This is a hypothesis-generating computational study. It predicts HLA-DQ
binding; it does not claim experimental proof of antigen processing, surface
presentation, CD4 T-cell recognition, or HBV-HCC causality.

## Final Main Analysis

- Public complete-genome GenBank candidates downloaded: 3784.
- QC-passed genotype-labeled HBV core records: 1576.
- Unique QC-passed accessions: 1538.
- Unique core 15-mer windows: 11176.
- Occurrence-weighted core windows: 259916.
- Prediction method: IEDB MHC-II API, NetMHCIIpan.
- Main comparison: two DQB1*03:01-containing HLA-DQ heterodimers versus a
  DQB1*03:02 comparator and four additional HLA-DQ comparator heterodimers.

Main result:

- DQA1*03:01/DQB1*03:02: 9.55% unique binder rate, 10.52% occurrence-weighted.
- DQA1*05:08/DQB1*03:01: 1.10% unique binder rate, 0.23% occurrence-weighted.
- DQA1*06:01/DQB1*03:01: 1.26% unique binder rate, 0.80% occurrence-weighted.

Robustness upgrades include IEDB recommended-method sensitivity, exact/greedy
de-redundancy, record-level bootstrap, genotype/region/year stratification,
core-position gap analysis, IEDB human HBV T-cell epitope overlap, and a
reference HBV proteome control.

## Iteration Strategy Used

1. Build a small literature-derived HCC-associated HBV coding mutation panel.
2. Confirm public HBV genotype B/C sequence availability and metadata quality.
3. Confirm feasible HLA-DQ binding prediction route.
4. Run a pilot on a small mutation set.
5. Keep only analyses that survive expansion and sensitivity checks.
6. Pivot away from unsupported mutation-loss claims.
7. Expand to the full public genotype B/C GenBank retrieval and regenerate the
   submission package.

## Directory Layout

- `data/raw`: downloaded public data cache, not tracked in GitHub; regenerate
  with the fetching scripts
- `data/manual`: manually curated panels and source notes
- `data/processed`: cleaned intermediate tables
- `scripts`: reproducible analysis scripts
- `results/tables`: output tables
- `results/figures`: output figures
- `docs`: plans, logs, and manuscript notes
- `logs`: local command outputs and run notes, not tracked in GitHub
- `manuscript`: earlier manuscript draft files
- `submission`: final submission-facing manuscript, cover letter, figure
  legends, supplement note, copied figures/tables, DOCX files, and ZIP package
- `submission_viruses`: Viruses-targeted submission package with manuscript,
  cover letter, figure legends, graphical abstract, response-to-reviewers
  template, figures, tables, DOCX files, and ZIP package

Start here:

- `submission_viruses/README_VIRUSES_PACKAGE.md`
- `submission_viruses/HBV_DQB10301_viruses_manuscript.md`
- `docs/submission_package_index.md`
- `docs/upgrade_summary.md`
- `docs/skill_usage_register.md`
- `docs/viruses_requirements_audit.md`
- `docs/reviewer_prebuttal_viruses.md`

## Large Regenerable Outputs

Large per-peptide prediction CSV files are not tracked in GitHub to keep the
repository lightweight and reviewable. They can be regenerated from the public
inputs with the scripts in `scripts/`; manuscript-facing summary tables and
figures are tracked.
