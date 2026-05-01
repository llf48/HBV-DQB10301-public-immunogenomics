# Final Upgrade Summary

Date: 2026-05-01

## Question After Iteration

Can this become a good public-data paper without experiments?

Yes, but only after narrowing the claim. The supported article is not that
HCC-associated HBV mutations experimentally cause CD4 presentation loss. The
supported article is:

**Public HBV genotype B/C core diversity preserves an HLA-DQB1*03:01-associated
class-II antigen-presentation gap.**

## What Was Upgraded In The Final Iteration

1. The public HBV dataset was expanded from the earlier 469-record pilot to the
   full retrievable genotype B/C complete-genome GenBank set.
2. The final QC-passed dataset now contains 1576 genotype-labeled core records,
   1538 unique accessions, 11176 unique core 15-mers, and 259916
   occurrence-weighted windows.
3. The HLA-DQ comparison was retained as a seven-heterodimer panel.
4. IEDB recommended-method sensitivity was rerun on the full peptide set for
   the primary three HLA-DQ pairs.
5. Exact-core, greedy 99%, and greedy 95% de-redundancy were rerun on the full
   dataset.
6. Record-level bootstrap confidence intervals were rerun on the full dataset.
7. Genotype, region, country, year-bin, and leave-one-stratum-out sensitivity
   analyses were added.
8. Core-position gap analysis was added to identify the windows driving the
   aggregate effect.
9. IEDB human HBV T-cell epitope overlap was rerun for the full dataset.
10. Submission-facing manuscript, cover letter, figure legends, supplementary
   note, figures, and tables were regenerated.

## Best Result

Across 1576 QC-passed public genotype B/C HBV core records, 11176 unique core
15-mer windows and 259916 occurrence-weighted windows were evaluated.

The DQB1*03:01-containing pairs had markedly lower predicted binder rates than
the DQB1*03:02 comparator:

- DQA1*03:01/DQB1*03:02: 9.55% unique, 10.52% occurrence-weighted.
- DQA1*05:08/DQB1*03:01: 1.10% unique, 0.23% occurrence-weighted.
- DQA1*06:01/DQB1*03:01: 1.26% unique, 0.80% occurrence-weighted.

The expanded comparator panel showed that several non-DQB1*03:01 HLA-DQ pairs
had moderate to high binder rates, while both DQB1*03:01-containing pairs
remained at the bottom.

## Robustness Results

- De-redundancy preserved the result:
  - Exact-core representatives: DQB1*03:02 10.40%,
    DQA1*05:08/DQB1*03:01 0.36%, DQA1*06:01/DQB1*03:01 0.92%.
  - Greedy 99% representatives: 10.35%, 0.39%, and 0.93%.
  - Greedy 95% representatives: 10.03%, 0.68%, and 1.10%.
- Bootstrap preserved rate-ratio separation:
  - DQB1*03:02 over DQA1*05:08/DQB1*03:01: 95% CI 41.86-53.67.
  - DQB1*03:02 over DQA1*06:01/DQB1*03:01: 95% CI 12.66-13.63.
- IEDB recommended method sensitivity changed absolute rates but preserved the
  occurrence-weighted direction:
  - DQB1*03:02: 4.59%.
  - DQA1*05:08/DQB1*03:01: 0.41%.
  - DQA1*06:01/DQB1*03:01: 1.20%.
- IEDB overlap found zero NetMHCIIpan-predicted DQB1*03:01 binders overlapping
  the pulled known human HBV core/nucleocapsid MHC-II epitopes.
- Core-position analysis localized the strongest gap to HBV core N-terminal
  windows, especially positions 2-27.
- Reference proteome controls showed that DQB1*03:01 pairs can bind predicted
  HBV peptides in envelope and X, so the main result is core/capsid-focused,
  not a global negative prediction artifact.

## What To Avoid

- Do not claim experimental antigen presentation.
- Do not claim CD4 T-cell recognition.
- Do not claim patient-level host-virus pairing.
- Do not claim that HCC-associated mutations are the proven causal driver.
- Do not oversell the IEDB overlap as proof that DQB1*03:01 cannot present
  core epitopes; it is a public-database overlap check.

## Realistic Journal Level

The package is strongest for computational virology, viral immunogenomics, or
public-data hypothesis-generating journals. A realistic target tier is specialty
journals such as `Viruses`, `Journal of Medical Virology`, `BMC Genomics`,
`Frontiers in Immunology`, or `Frontiers in Microbiology`, depending on
formatting and reviewer appetite.

Without wet-lab validation, it is not positioned as a top hepatology or
mechanistic immunology paper.
