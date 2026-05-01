# Iteration Summary

Date: 2026-05-01

## Iteration 1: Mutation-Loss Hypothesis

Original hypothesis:

HCC-associated HBV coding mutations might cause DQB1*03:01-specific
binder-to-non-binder loss.

Result:

Pilot HBx and PreS/S hotspot analyses did not support this as a strong main
paper. The idea was kept as negative exploratory context, not the final claim.

## Iteration 2: Public Core Presentation Gap

Reframed hypothesis:

DQB1*03:01-containing HLA-DQ heterodimers may have a stable predicted class-II
presentation gap for HBV core/capsid peptides across public genotype B/C
diversity.

Result:

The signal was strong enough to become the main paper.

## Iteration 3: Expanded HLA-DQ Panel

Seven HLA-DQ heterodimers were tested, including two DQB1*03:01-containing
risk pairs, one DQB1*03:02 comparator, and four additional comparison pairs.

Result:

The DQB1*03:01-containing pairs were consistent low-binding outliers.

## Iteration 4: Full Public Dataset Expansion

The pilot dataset was replaced with the full retrievable NCBI GenBank
genotype B/C complete-genome set.

Final full dataset:

- 3784 candidate records.
- 1576 QC-passed genotype-labeled core records.
- 1538 unique accessions.
- 11176 unique core 15-mers.
- 259916 occurrence-weighted windows.

## Iteration 5: Robustness Upgrade

Added:

- IEDB recommended-method sensitivity.
- Exact-core, greedy 99%, and greedy 95% de-redundancy.
- Record-level bootstrap.
- Genotype, region, country, year-bin, and leave-one-stratum-out sensitivity.
- IEDB human HBV T-cell epitope overlap.
- Reference HBV proteome controls.
- Core-position gap analysis.

## Final Main Result

- DQA1*03:01/DQB1*03:02: 9.55% unique binders and 10.52% occurrence-weighted.
- DQA1*05:08/DQB1*03:01: 1.10% unique binders and 0.23% occurrence-weighted.
- DQA1*06:01/DQB1*03:01: 1.26% unique binders and 0.80% occurrence-weighted.

## Final Decision

The project is now a submission-ready computational public-data manuscript, but
with clear limitations. It should be submitted as hypothesis-generating viral
immunogenomics, not as a mechanistic wet-lab validation paper.
