# GitHub And Zenodo Deposition Text

## Suggested GitHub Repository Description

Reproducible public-data immunogenomics workflow showing that public HBV
genotype B/C core diversity preserves an HLA-DQB1*03:01-associated MHC-II
presentation gap across HLA-DQ heterodimers.

## Suggested Repository Topics

`hbv`, `hepatitis-b-virus`, `hla-dq`, `hla-dqb1`, `mhc-class-ii`, `iedb`,
`immunogenomics`, `epitope-prediction`, `public-data`

## Suggested GitHub Release Text

Version 1.0.0 accompanies the manuscript "Public HBV genotype B/C core diversity
reveals an HLA-DQB1*03:01-associated class-II presentation gap". The release
contains scripts for public NCBI GenBank retrieval, HBV core peptide generation,
IEDB MHC-II prediction, robustness analysis, IEDB T-cell epitope overlap,
publication figures, Viruses-ready manuscript files, and reproducibility
documentation.

## Suggested Zenodo Description

This archived release contains the code, processed metadata, analysis tables,
figures, and submission-facing materials for a public-data computational
immunogenomics study of HBV genotype B/C core diversity and HLA-DQ MHC-II
binding. The workflow retrieves public GenBank records, extracts HBV core/capsid
translations, generates overlapping 15-mers, predicts HLA-DQ binding through
IEDB, performs de-redundancy/bootstrap/stratified sensitivity analyses, overlaps
predicted binders with IEDB human HBV T-cell epitopes, and exports
publication-ready figures and tables.

## Data Availability Statement For Manuscript

All viral sequences analyzed in this study are publicly available from NCBI
GenBank and were retrieved through NCBI E-utilities using the queries documented
in the accompanying repository. IEDB MHC-II prediction outputs and IEDB human
HBV T-cell epitope records were generated from public IEDB web services. The
analysis scripts, processed peptide metadata, prediction summaries, figure
source files, and submission tables are available at
`https://github.com/[username]/hbv-dq3-public-immunogenomics` and archived at
Zenodo: `https://doi.org/10.5281/zenodo.[placeholder]`.

## Code Availability Statement For Manuscript

The complete reproducible workflow is available at
`https://github.com/[username]/hbv-dq3-public-immunogenomics` under the MIT
License. A frozen release is archived at Zenodo:
`https://doi.org/10.5281/zenodo.[placeholder]`.
