# Research Log

Date: 2026-05-01

## Summary

The project started with a mutation-specific hypothesis and ended with a
stronger public-data immunogenomics article. Earlier pilot values are superseded
by the full dataset summarized below.

## Final Iteration

The full public genotype B/C complete-genome HBV retrieval returned 3784
candidate GenBank records. After parsing core/capsid CDS translations and
excluding records with missing core translation, recombinant annotations,
abnormal core length, non-standard amino acids, or missing genotype labels, 1576
records passed QC. These records represented 1538 unique accessions.

The full core peptide set contained 11176 unique 15-mer windows and 259916
occurrence-weighted windows.

NetMHCIIpan results:

- DQA1*03:01/DQB1*03:02: 1067/11176 unique binders and 27340/259916
  occurrence-weighted binders.
- DQA1*05:08/DQB1*03:01: 123/11176 unique binders and 586/259916
  occurrence-weighted binders.
- DQA1*06:01/DQB1*03:01: 141/11176 unique binders and 2090/259916
  occurrence-weighted binders.

IEDB recommended method sensitivity:

- DQA1*03:01/DQB1*03:02: 4.59% occurrence-weighted binder rate.
- DQA1*05:08/DQB1*03:01: 0.41% occurrence-weighted binder rate.
- DQA1*06:01/DQB1*03:01: 1.20% occurrence-weighted binder rate.

IEDB epitope overlap:

- 1597 positive human HBV T-cell assay rows retrieved.
- 678 unique linear epitopes after normalization.
- 163 core/nucleocapsid epitopes.
- 50 core/nucleocapsid MHC-II epitopes.
- NetMHCIIpan-predicted DQB1*03:01 risk-pair binders overlapped zero known
  core/nucleocapsid MHC-II epitopes.

## Final Decision

The mutation-loss hypothesis was not strong enough as the main paper. The final
paper is the public HBV core presentation-gap analysis.
