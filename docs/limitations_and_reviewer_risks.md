# Limitations And Reviewer Risks

Date: 2026-05-01

## Highest-Risk Reviewer Objection

This is peptide-HLA binding prediction, not experimental antigen presentation.

Response:

The manuscript states that the result is hypothesis-generating and does not
claim antigen processing, HLA-DQ surface presentation, CD4 T-cell recognition,
or HBV-HCC causality.

## Public Sequence Bias

NCBI GenBank records are not a population-representative sample. Genotype,
country, collection year, sequencing center, and disease-status metadata are
incomplete and uneven.

Response:

The final analysis adds genotype, region, country, year-bin, and
leave-one-stratum-out sensitivity analyses. The signal persists across the major
available strata, but the study does not infer prevalence or population-level
risk.

## No Host-Virus Pairing

The viral sequences are not paired with donor HLA genotypes.

Response:

The analysis tests whether public genotype B/C core diversity preserves a
predicted presentation gap across HLA-DQ contexts. It does not claim within-host
HLA-driven viral evolution.

## Prediction-Method Dependence

IEDB recommended-method predictions produce lower absolute binder rates than
NetMHCIIpan BA.

Response:

The occurrence-weighted direction remains the same, but the manuscript notes
that effect size and unique-peptide differences are method-sensitive.

## IEDB Epitope Coverage

IEDB human HBV core/nucleocapsid MHC-II epitope coverage is incomplete and
historically biased.

Response:

IEDB overlap is used as an external immune-data anchor, not as proof that
DQB1*03:01 cannot present any core epitope.

## Reference Proteome Control

DQB1*03:01-containing HLA-DQ pairs can bind some HBV X, envelope, and polymerase
peptides.

Response:

This strengthens the final story: the gap is core/capsid-focused rather than a
global failure of DQB1*03:01-containing heterodimers.

## Manuscript Claim Boundary

Safe claim:

Public HBV genotype B/C core diversity preserves a predicted class-II binding
gap for DQB1*03:01-containing HLA-DQ heterodimers.

Unsafe claims:

- DQB1*03:01 experimentally fails to present HBV core.
- DQB1*03:01 directly causes HBV-HCC.
- HCC-associated viral mutations are the demonstrated causal mechanism.
- Public GenBank frequencies estimate real-world viral population prevalence.
