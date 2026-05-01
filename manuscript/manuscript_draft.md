# Public HBV genotype B/C core diversity preserves an HLA-DQB1*03:01-associated class-II antigen-presentation gap

## Short Title

HBV core diversity and DQB1*03:01 presentation gap

## Authors

[Author names and affiliations to be added]

## Abstract

See `manuscript/abstract.md`.

## Introduction

Chronic hepatitis B virus (HBV) infection remains a major cause of
hepatocellular carcinoma (HCC). Viral persistence and cancer risk are shaped by
both viral genetic variation and host immune genetics. Among host loci, HLA
class II variation has repeatedly been implicated in HBV persistence and
HBV-related liver disease, supporting a role for CD4 T-cell antigen presentation
in long-term immune control of HBV.

Recent work by Zhang et al. identified HLA-DQB1*03:01 as a risk allele for
HBV-related HCC and reported reduced predicted binding of HBV nucleocapsid
peptides by DQB1*03:01-containing HLA-DQ molecules. That study provides an
important host-genetic and mechanistic starting point, but it leaves a public-
data question unanswered: is the predicted DQB1*03:01 nucleocapsid/core binding
gap robust across naturally occurring HBV genotype B/C diversity, or is it
primarily a reference-sequence observation?

This question is relevant because genotype B and genotype C predominate in many
East Asian HBV-HCC settings, and genotype C has been associated with increased
HCC risk in prior epidemiologic studies. Public GenBank HBV genomes provide an
opportunity to test whether the DQB1*03:01-associated core presentation gap is
preserved across real viral sequence diversity, even in the absence of paired
host HLA genotypes.

Here, we constructed a reproducible public-data immunogenomics workflow that
extracts HBV core proteins from genotype B/C complete genomes, generates
overlapping 15-mer core peptides, predicts HLA-DQ MHC-II binding using IEDB
NetMHCIIpan, and compares DQB1*03:01-containing heterodimers with a DQB1*03:02
comparator. We show that public genotype B/C core diversity preserves a marked
predicted class-II binding gap for DQB1*03:01-containing HLA-DQ molecules.

## Methods

### Literature and novelty review

PubMed was searched on 2026-04-30 using targeted terms for HLA-DQB1*03:01, HBV,
HCC, NetMHCIIpan, peptide binding, and HLA-DQ. The search identified related
HBV-HLA-HCC association studies, HBV mutation interaction studies, and HBV HLA
class II peptide prediction studies, but no PubMed-indexed study combining a
DQB1*03:01 focus, HBV genotype B/C public core sequence diversity, HLA-DQ
heterodimer binding prediction, and a quantified DQB1*03:01-associated core
presentation gap.

### Public HBV sequence retrieval

NCBI nucleotide E-utilities were queried for complete HBV genomes annotated as
genotype B or genotype C. The expanded analysis retrieved 500 candidate records
for each genotype query, for a total of 1000 candidate records. GenBank files
were downloaded with `curl.exe` using NCBI E-utilities.

### Core protein extraction and quality control

GenBank CDS features were parsed to identify translated core protein sequences.
Records were excluded if they lacked a core translation, had recombinant
annotation in definition or notes, had core length outside 170 to 190 amino
acids, or contained non-standard amino-acid characters. After QC, 469 records
were retained, including 316 genotype B query records and 153 genotype C query
records.

### Peptide generation

For each QC-passed core protein, all overlapping 15-mer peptides were generated.
Peptides were collapsed by sequence and window start position. The final
analysis included 5670 unique core 15-mer windows and 77579 occurrence-weighted
windows.

### HLA-DQ panel

Three HLA-DQ heterodimers were evaluated:

- DQA1*05:08/DQB1*03:01
- DQA1*06:01/DQB1*03:01
- DQA1*03:01/DQB1*03:02

The first two were treated as DQB1*03:01-containing risk heterodimers, and the
third as a DQB1*03:02 comparator.

### MHC-II binding prediction

MHC-II binding predictions were generated through the IEDB MHC-II API using
NetMHCIIpan. Percentile rank <10 was defined as predicted binding, and rank <2
was defined as strong predicted binding. Prediction outputs were merged with
peptide metadata and source occurrence counts.

### Statistical analysis

For each HLA-DQ heterodimer, binder counts were summarized using unique peptide
counts and occurrence-weighted counts. Pairwise comparisons used Fisher exact
tests. Genotype-stratified occurrence-weighted binder rates were calculated for
genotype B and genotype C query records separately.

## Results

### Public genotype B/C core diversity generated 5670 unique core peptide windows

From 1000 candidate public GenBank records, 469 passed QC. These records
generated 5670 unique HBV core 15-mer windows and 77579 occurrence-weighted
windows. The QC-passed set was imbalanced toward genotype B records, with 316
genotype B query records and 153 genotype C query records.

### DQB1*03:01-containing HLA-DQ heterodimers had markedly fewer predicted core binders

The DQB1*03:02 comparator DQA1*03:01/DQB1*03:02 bound 511 of 5670 unique core
15-mers (9.01%) at percentile rank <10. In contrast, DQA1*05:08/DQB1*03:01
bound 60 unique peptides (1.06%) and DQA1*06:01/DQB1*03:01 bound 67 unique
peptides (1.18%). Strong binders were also fewer in DQB1*03:01-containing
pairs: 113 strong binders for DQB1*03:02 compared with 16 and 17 for the two
DQB1*03:01-containing pairs.

Occurrence-weighted analysis showed an even larger gap. DQA1*03:01/DQB1*03:02
bound 8077 of 77579 occurrence-weighted windows (10.41%). DQA1*05:08/
DQB1*03:01 bound 193 windows (0.25%), and DQA1*06:01/DQB1*03:01 bound 638
windows (0.82%).

### The predicted binding gap was statistically robust

In unique-peptide comparisons, DQA1*03:01/DQB1*03:02 showed higher predicted
binding than DQA1*05:08/DQB1*03:01 (OR 9.26, P = 2.84e-94) and
DQA1*06:01/DQB1*03:01 (OR 8.28, P = 1.42e-89). In occurrence-weighted
comparisons, the corresponding odds ratios were 46.60 and 14.01, with P values
underflowing to 0.0 in SciPy and therefore reported as P < 1e-300.

### The gap was preserved in genotype B and genotype C strata

Occurrence-weighted predicted binder rates for DQA1*03:01/DQB1*03:02 were
10.36% in genotype B query records and 10.51% in genotype C query records.
For DQA1*05:08/DQB1*03:01, rates were 0.28% and 0.19%, respectively. For
DQA1*06:01/DQB1*03:01, rates were 0.85% and 0.76%, respectively. Thus, the
predicted DQB1*03:01-associated core binding gap was not restricted to one
genotype query stratum.

### HCC hotspot mutation pilots did not support a mutation-loss main model

Exploratory analyses of literature-derived HBx and PreS/S HCC-associated
hotspots did not support the initial hypothesis that HCC-associated coding
mutations commonly create DQB1*03:01-specific binder-to-non-binder loss. HBx
hotspots were largely non-binding for the tested DQB1*03:01 pairs, and the
PreS/S S166L example showed allele-specific binding remodeling rather than
loss. These negative pilots motivated the final focus on the robust HBV core
presentation-gap result.

## Discussion

This study shows that public HBV genotype B/C core diversity preserves a marked
predicted HLA class-II binding gap for DQB1*03:01-containing HLA-DQ
heterodimers. The finding extends the DQB1*03:01-HBV-HCC nucleocapsid axis
from a reference-sequence observation to a larger public sequence context.

The result is biologically plausible because HBV core/nucleocapsid is a major
immune target, and HLA class II antigen presentation can shape CD4 T-cell help,
viral control, and chronic immune dysfunction. A persistent predicted binding
gap in DQB1*03:01-containing molecules could reduce the breadth or strength of
core-directed CD4 T-cell recognition in some host backgrounds. Such a mechanism
would be consistent with, but does not prove, the reported association between
DQB1*03:01 and HBV-related HCC risk.

The study also provides an example of useful hypothesis revision. The initial
mutation-loss hypothesis was attractive but did not survive pilot testing.
Rather than overstate weak mutation findings, we retained the strongest public-
data signal: a reproducible and genotype-stratified core antigen-presentation
gap.

Several limitations are important. The analysis predicts binding, not antigen
processing, HLA-DQ surface presentation, or T-cell activation. Public viral
records are not paired with host HLA genotypes, so the analysis cannot infer
within-host HLA-driven viral evolution. GenBank metadata are incomplete and
biased, and the QC-passed set is imbalanced between genotype B and genotype C.
Finally, only three HLA-DQ heterodimers were used in the main analysis.

Despite these limitations, the analysis is a reproducible public-data extension
of a recent HBV-HCC host-genetic finding. Future work should test additional
population-relevant HLA-DQ haplotypes, add antigen-processing and expression
context, and experimentally validate whether predicted low-binding core windows
correspond to weaker CD4 T-cell recognition in DQB1*03:01-positive individuals.

## Data Availability

All viral sequences were downloaded from public NCBI GenBank records using NCBI
E-utilities. Processed peptide metadata, IEDB prediction outputs, summary
tables, and analysis scripts are prepared in the accompanying project directory
and should be deposited in a public repository before submission.

## Code Availability

The reproducible workflow is implemented in the `scripts` directory. Main
commands are listed in `docs/submission_checklist.md`.

## References

1. Zhang T et al. HLA-DQB1*03:01 and risk of HBV-related HCC. Hepatology 2026.
   PMID: 40084945. https://pmc.ncbi.nlm.nih.gov/articles/PMC12353533/
2. Ji X et al. Impacts of HLA-DQ genetic polymorphisms and interactions with
   HBV mutations. Infect Genet Evol 2014. PMID: 25281206.
3. Wen J et al. HBV genotype, mutations, HLA polymorphisms and interactions in
   HCC. Sci Rep 2015. PMID: 26568165.
4. Choga WT et al. In silico prediction of HLA class II binding HBV peptides in
   Botswana. Viruses 2020. PMID: 32640609.
5. Sugiyama M et al. HLA genotypes affect HBV mutations associated with HCC.
   Hepatol Res 2025. PMID: 40728240.
6. IEDB MHC-II prediction resource. https://tools.iedb.org/mhcii/

