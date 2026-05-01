# Public HBV genotype B/C core diversity reveals an HLA-DQB1*03:01-associated class-II presentation gap

## Short Title

HBV core diversity and DQB1*03:01 presentation gap

## Authors

[Author names and affiliations to be added]

## Correspondence

[Corresponding author email to be added]

## Abstract

**Background:** HLA-DQB1*03:01 has been associated with increased risk of
hepatitis B virus (HBV)-related hepatocellular carcinoma (HCC), and prior
reference-sequence analyses suggested reduced HLA-DQ binding to HBV
nucleocapsid peptides. Whether this predicted presentation gap is preserved
across public HBV genotype B/C sequence diversity remains unresolved.

**Methods:** Public NCBI GenBank complete-genome HBV records annotated as
genotype B or C were retrieved and parsed for core/capsid CDS translations.
After excluding records with missing core translations, recombinant annotations,
abnormal core length, non-standard amino acids, or missing genotype labels, 1576
quality-controlled records were retained. Overlapping core 15-mers were
generated and collapsed into 11176 unique peptide windows with 259916
occurrence-weighted windows. IEDB MHC-II predictions were run for seven HLA-DQ
heterodimers using NetMHCIIpan, including two DQB1*03:01-containing risk pairs
and a DQB1*03:02 comparator. Sensitivity analyses included IEDB recommended
predictions, exact and identity-based de-redundancy, record-level bootstrap,
genotype/region/year stratification, core-position gap analysis, IEDB human HBV
T-cell epitope overlap, and reference-proteome controls.

**Results:** In the expanded HLA-DQ panel, occurrence-weighted predicted core
binder rates were 13.52%, 10.52%, 10.20%, 9.04%, and 7.66% for five non-risk
comparison heterodimers, including 10.52% for DQA1*03:01/DQB1*03:02. In
contrast, DQA1*06:01/DQB1*03:01 and DQA1*05:08/DQB1*03:01 showed markedly lower
rates of 0.80% and 0.23%, respectively. DQA1*03:01/DQB1*03:02 exceeded both
DQB1*03:01-containing pairs in unique-peptide analyses (OR 8.26-9.48,
P = 3.27e-185 to 2.29e-197) and occurrence-weighted analyses (OR 14.50-52.02,
P < 1e-300). The gap persisted after de-redundancy to exact-core, 99% identity,
and 95% identity representative sets. Bootstrap rate ratios for
DQA1*03:01/DQB1*03:02 over the two DQB1*03:01 pairs were 47.37 (95% CI
41.86-53.67) and 13.13 (95% CI 12.66-13.63). IEDB recommended predictions
preserved the occurrence-weighted direction of effect. Position-level analysis
localized the strongest gap to HBV core N-terminal windows, especially windows
2-27. Among 50 known human HBV core/nucleocapsid MHC-II epitopes in IEDB,
predicted NetMHCIIpan binders from the DQB1*03:01 risk pairs overlapped none,
whereas the DQB1*03:02 comparator overlapped 20.

**Conclusions:** Public genotype B/C HBV core diversity preserves a marked
class-II binding gap for DQB1*03:01-containing HLA-DQ heterodimers. This
computational public-data result extends the DQB1*03:01-HBV-HCC nucleocapsid
axis into naturally occurring viral diversity and nominates HBV core antigen
presentation as a focused hypothesis for experimental validation.

## Keywords

hepatitis B virus; HLA-DQB1*03:01; HLA-DQ; MHC class II; CD4 T cell; HBV core;
hepatocellular carcinoma; immunogenomics; epitope prediction

## Introduction

Chronic hepatitis B virus (HBV) infection remains a major cause of
hepatocellular carcinoma (HCC). Progression from infection to chronic liver
inflammation, cirrhosis, and HCC is shaped by both viral genetic variation and
host immune genetics. The HLA region is repeatedly implicated in HBV
persistence and HBV-related liver disease, consistent with a central role for
antigen presentation in long-term antiviral immune control.

HLA class II presentation is especially relevant because CD4 T-cell responses
coordinate antiviral immunity, antibody maturation, cytotoxic T-cell function,
and immune memory. HBV core/nucleocapsid antigens are major immune targets, and
impaired core-directed helper responses could plausibly contribute to viral
persistence or immune exhaustion. A recent Hepatology study connected
HLA-DQB1*03:01 with HBV-related HCC risk and reported lower predicted binding
of HBV nucleocapsid peptides by DQB1*03:01-containing HLA-DQ molecules. That
finding provided a mechanistic clue, but it also raised an important public-data
question: is the predicted core/nucleocapsid presentation gap stable across
naturally occurring HBV genotype B/C sequence diversity?

This question matters because HBV genotype B and genotype C predominate in many
East Asian HBV-HCC settings, and genotype C has been associated with increased
HCC risk in epidemiologic studies. A reference-sequence binding deficit could
be biologically meaningful, but viral sequence diversity could also weaken,
erase, or reverse the signal. Public GenBank HBV genomes therefore provide an
opportunity to test whether a DQB1*03:01-associated core presentation gap is
preserved across real viral diversity, even though the viral sequences are not
paired with host HLA genotypes.

We initially evaluated a narrower mutation-loss model: whether reported
HCC-associated HBV coding mutations commonly create DQB1*03:01-specific
binder-to-non-binder loss. Exploratory HBx and PreS/S hotspot analyses did not
support that model as a main result. We therefore revised the study around the
stronger and more defensible public-data question: whether global public HBV
genotype B/C core diversity preserves a DQB1*03:01-associated class-II
presentation gap. Here, we combine public HBV sequence retrieval, HLA-DQ
heterodimer MHC-II prediction, expanded HLA-DQ panel comparison,
de-redundancy, stratified sensitivity analysis, IEDB T-cell epitope overlap,
and reference-proteome controls.

## Methods

### Literature and novelty review

PubMed was queried on 2026-04-30 using combinations of `DQB1*03:01`,
`HLA-DQB1`, `HBV`, `hepatitis B`, `HCC`, `nucleocapsid`, `NetMHCIIpan`,
`peptide`, `epitope`, and `HLA-DQ`. The search identified related HBV-HLA-HCC
association studies, HBV mutation interaction studies, and HBV HLA class II
peptide prediction studies, but no PubMed-indexed study combining
DQB1*03:01-focused HLA-DQ heterodimer prediction, public HBV genotype B/C core
diversity, core-position gap analysis, and IEDB epitope overlap into a
quantified DQB1*03:01-associated presentation-gap framework.

### Public HBV sequence retrieval and quality control

NCBI nucleotide E-utilities were used to retrieve public complete-genome HBV
GenBank records annotated as genotype B or genotype C. The full query retrieved
3784 candidate records. GenBank CDS annotations were parsed to extract core
protein translations.

Records were excluded if they lacked a usable core CDS translation, contained
recombinant annotations in the definition or feature notes, had core length
outside 170-190 amino acids, contained non-standard amino-acid characters, or
lacked a genotype B/C query label. The final quality-controlled set contained
1576 genotype-labeled records, corresponding to 1538 unique accession
identifiers. The QC-passed set included 633 genotype B query records and 943
genotype C query records.

### Core peptide generation

For each quality-controlled core protein, all overlapping 15-mer peptides were
generated. Peptides were collapsed by peptide sequence and core window start
position. The final public-diversity analysis included 11176 unique core 15-mer
windows and 259916 occurrence-weighted windows.

### HLA-DQ panel

Seven HLA-DQ heterodimers were evaluated:

- DQA1*05:08/DQB1*03:01
- DQA1*06:01/DQB1*03:01
- DQA1*03:01/DQB1*03:02
- DQA1*01:02/DQB1*06:02
- DQA1*01:01/DQB1*05:01
- DQA1*03:03/DQB1*04:01
- DQA1*05:01/DQB1*02:01

The first two were treated as DQB1*03:01-containing risk heterodimers based on
the motivating DQB1*03:01-HBV-HCC literature. DQA1*03:01/DQB1*03:02 was used as
the primary DQB1*03:02 comparator. Additional HLA-DQ heterodimers were included
to test whether the signal was specific to DQB1*03:01-containing pairs rather
than a generic feature of HLA-DQ prediction.

### MHC-II binding prediction

MHC-II binding predictions were generated through the IEDB MHC-II prediction API
using NetMHCIIpan. Percentile rank <10 was defined as predicted binding, and
rank <2 was defined as strong predicted binding. As a method sensitivity check,
the IEDB recommended method was also run for the primary three HLA-DQ
heterodimers: DQA1*03:01/DQB1*03:02, DQA1*05:08/DQB1*03:01, and
DQA1*06:01/DQB1*03:01.

### Statistical analysis

Binder counts were summarized using both unique peptide counts and
occurrence-weighted counts. Pairwise comparisons between the DQB1*03:02
comparator and other heterodimers used Fisher exact tests. P values that
underflowed to zero in SciPy are reported as P < 1e-300. Occurrence-weighted
rates were also calculated within genotype, region, country, and collection-year
strata when metadata were available.

### Sequence de-redundancy and bootstrap analysis

To assess sensitivity to public database redundancy, three de-redundant record
sets were created: exact core protein de-duplication, greedy 99% identity
de-redundancy, and greedy 95% identity de-redundancy. Occurrence-weighted HLA-DQ
binder rates were recomputed in each set without rerunning MHC-II prediction,
using accession-level source mappings.

Record-level bootstrap analysis used 1000 resamples of quality-controlled
records with replacement. Binder-rate confidence intervals, rate differences,
and rate ratios were calculated from accession-level totals.

### Core-position gap analysis

For each HBV core 15-mer window start, occurrence-weighted binder rates were
summarized for the DQB1*03:02 comparator and the combined DQB1*03:01 risk pairs.
A position-level gap was defined as the DQB1*03:02 occurrence-weighted binder
rate minus the combined DQB1*03:01 risk-pair occurrence-weighted binder rate.
Top gap windows were ranked by this difference.

### IEDB human HBV T-cell epitope overlap

The IEDB query API was used to retrieve positive human T-cell assay records for
HBV (`NCBITaxon:10407`). Retrieved linear epitopes were normalized by sequence,
source antigen, source position, and MHC class. Core/nucleocapsid epitopes were
identified from curated antigen names and parent antigen names containing
`core` or `nucleocapsid`. Predicted core 15-mers were considered overlapping if
the predicted peptide contained the known epitope sequence or was contained
within the known epitope sequence. Overlap was summarized for all known human
core/nucleocapsid T-cell epitopes and separately for known MHC-II
core/nucleocapsid epitopes.

### Reference HBV proteome control

To test whether the DQB1*03:01 gap was core-specific rather than a global HBV
protein effect, the reference HBV genome NC_003977.2 was parsed for polymerase,
large envelope, X protein, and capsid/core translations. Overlapping 15-mers
were generated for each protein and predicted against the same seven HLA-DQ
heterodimers using IEDB NetMHCIIpan.

## Results

### Public genotype B/C core diversity generated 11176 unique core peptide windows

The full public GenBank retrieval produced 3784 candidate complete-genome
records annotated as genotype B or C. After core CDS extraction and quality
control, 1576 genotype-labeled records remained, including 633 genotype B query
records and 943 genotype C query records. These records represented 1538 unique
accession identifiers and produced 11176 unique core 15-mer windows with 259916
occurrence-weighted windows.

Most QC-passed records had geographic metadata from East or Southeast Asia,
consistent with the genotype B/C focus, but the analysis also retained records
from other regions and from records with missing geographic annotation. This
dataset was substantially larger than the initial pilot set and replaced the
earlier 469-record analysis as the final submission version.

### DQB1*03:01-containing HLA-DQ heterodimers were outliers in an expanded HLA-DQ panel

Across seven HLA-DQ heterodimers, occurrence-weighted public-core binder rates
varied substantially. DQA1*01:01/DQB1*05:01 had the highest occurrence-weighted
binder rate (13.52%), followed by DQA1*03:01/DQB1*03:02 (10.52%),
DQA1*01:02/DQB1*06:02 (10.20%), DQA1*05:01/DQB1*02:01 (9.04%), and
DQA1*03:03/DQB1*04:01 (7.66%). In contrast, the two DQB1*03:01-containing
heterodimers had markedly lower occurrence-weighted rates:
DQA1*06:01/DQB1*03:01 bound 0.80% of windows and DQA1*05:08/DQB1*03:01 bound
0.23%.

The same pattern was observed in unique-peptide counts. DQA1*03:01/DQB1*03:02
bound 1067 of 11176 unique core windows (9.55%), whereas
DQA1*06:01/DQB1*03:01 and DQA1*05:08/DQB1*03:01 bound 141 (1.26%) and 123
(1.10%) unique core windows, respectively.

### The DQB1*03:02 comparator exceeded DQB1*03:01-containing pairs in statistical comparisons

In unique-peptide Fisher exact tests, DQA1*03:01/DQB1*03:02 showed higher
predicted binding than DQA1*05:08/DQB1*03:01 (OR 9.48,
P = 2.29e-197) and DQA1*06:01/DQB1*03:01 (OR 8.26,
P = 3.27e-185). In occurrence-weighted analyses, the corresponding odds ratios
were 52.02 and 14.50; both P values underflowed and are reported as
P < 1e-300.

The broader panel showed that DQB1*03:02 was not the single highest-binding
HLA-DQ pair; DQA1*01:01/DQB1*05:01 bound more public-core windows. The key
result is therefore not that DQB1*03:02 is universally superior, but that
DQB1*03:01-containing risk heterodimers are consistent low-binding outliers for
HBV core.

### The gap was preserved across genotype, region, and collection-year strata

Occurrence-weighted predicted binder rates for DQA1*03:01/DQB1*03:02 were
10.39% in genotype B query records and 10.60% in genotype C query records. For
DQA1*05:08/DQB1*03:01, rates were 0.27% and 0.20%, respectively. For
DQA1*06:01/DQB1*03:01, rates were 0.83% and 0.79%, respectively. Thus, the
predicted DQB1*03:01-associated core binding gap was not restricted to one
genotype query stratum.

The same direction was observed in major geographic strata, including East Asia,
Southeast Asia, South Asia, and North America, and across collection-year bins
from pre-2005 through 2016 and later. Leave-one-stratum-out analyses likewise
preserved large DQB1*03:02-to-DQB1*03:01 rate ratios, indicating that the
aggregate result was not explained by a single dominant region or time period.

### Method sensitivity supported the occurrence-weighted direction of effect

IEDB recommended-method predictions produced lower absolute binder rates than
NetMHCIIpan BA for the primary three heterodimers, but the occurrence-weighted
direction of effect was preserved. DQA1*03:01/DQB1*03:02 bound 4.59% of
occurrence-weighted core windows, compared with 1.20% for
DQA1*06:01/DQB1*03:01 and 0.41% for DQA1*05:08/DQB1*03:01. Under the
recommended method, occurrence-weighted rate ratios for DQA1*03:01/DQB1*03:02
over the two DQB1*03:01-containing pairs were 3.81 and 11.07. Unique-peptide
differences were weaker under the recommended method, indicating method
sensitivity in absolute thresholds but not reversal of the occurrence-weighted
gap.

### The DQB1*03:01 core gap survived de-redundancy and bootstrap analysis

Exact core protein de-duplication reduced the accession-level set to 787
representatives, greedy 99% identity de-redundancy retained 598 representatives,
and stringent 95% identity de-redundancy retained 106 representatives. In all
three de-redundant sets, DQA1*03:01/DQB1*03:02 maintained an
occurrence-weighted binder rate near 10%, whereas DQB1*03:01-containing
heterodimers remained near or below 1.1%.

Record-level bootstrap analysis further supported the robustness of the
contrast. The DQA1*03:01/DQB1*03:02 occurrence-weighted binder rate had a mean
of 10.53% with a 95% bootstrap interval of 10.48%-10.57%. The corresponding
means were 0.22% for DQA1*05:08/DQB1*03:01 and 0.80% for
DQA1*06:01/DQB1*03:01. Bootstrap rate-ratio intervals for the DQB1*03:02
comparator versus the DQB1*03:01-containing pairs were 41.86-53.67 and
12.66-13.63, respectively.

### Core-position analysis localized the strongest gap to the HBV core N-terminus

Position-level analysis showed that the DQB1*03:01-associated gap was not
uniformly distributed across HBV core. The largest gaps occurred in N-terminal
15-mer windows spanning approximately core positions 2-27. Several windows in
this region had DQA1*03:01/DQB1*03:02 occurrence-weighted binder rates near or
above 99%, while the combined DQB1*03:01 risk-pair binder rate was near zero.
The top gap window was core positions 12-26, represented by
`SVELLSFLPADFFPP`, where the DQB1*03:02 occurrence-weighted binder rate was
99.61% and the combined DQB1*03:01 risk-pair binder rate was 0%.

Additional but narrower gap regions were observed around core positions 29-43
and 65-80. These position-level findings provide a more focused candidate map
for future experimental testing than aggregate binder-rate comparisons alone.

### Predicted DQB1*03:01 binders did not overlap known core/nucleocapsid MHC-II epitopes

IEDB query API retrieval identified 1597 positive human HBV T-cell assay rows,
which normalized to 678 unique linear epitopes. Of these, 163 were core or
nucleocapsid epitopes and 50 were core/nucleocapsid MHC-II epitopes.

Among NetMHCIIpan-predicted public-core binders, DQA1*03:01/DQB1*03:02 had 225
binders overlapping known core/nucleocapsid T-cell epitopes and 20 overlapping
known core/nucleocapsid MHC-II epitopes. Other non-risk comparison heterodimers
had 19-32 binders overlapping known core/nucleocapsid MHC-II epitopes. In
contrast, the two DQB1*03:01-containing heterodimers had 17 and 25 binders
overlapping any known core/nucleocapsid T-cell epitope and zero binders
overlapping known core/nucleocapsid MHC-II epitopes.

IEDB recommended predictions were less extreme but directionally similar:
DQA1*03:01/DQB1*03:02 had six binder overlaps with known core/nucleocapsid
MHC-II epitopes, whereas the two DQB1*03:01-containing heterodimers had one and
two overlaps.

### Reference proteome analysis supported a core-specific, not global, DQB1*03:01 gap

Reference-proteome analysis showed that the DQB1*03:01-containing heterodimers
were not globally unable to bind HBV peptides. For reference X protein,
DQA1*05:08/DQB1*03:01 and DQA1*06:01/DQB1*03:01 had binder rates of 7.86% and
7.14%, respectively. For large envelope protein, they had binder rates of 9.87%
and 8.80%. For polymerase, they had binder rates of 2.44% and 3.55%. In
contrast, for reference core/capsid peptides, both DQB1*03:01-containing
heterodimers had 0/169 predicted binders. This supports a core/capsid-focused
presentation gap rather than a general failure of DQB1*03:01-containing
heterodimers to bind HBV-derived peptides.

### HCC hotspot pilots did not support a mutation-loss main model

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
heterodimers. The result extends the reported DQB1*03:01-HBV-HCC nucleocapsid
axis from reference-sequence analysis into real public viral sequence diversity.
It also narrows the biological hypothesis: DQB1*03:01-containing molecules are
not predicted to be universally poor binders of HBV peptides; rather, their
deficit is most pronounced for core/capsid peptides.

Several findings strengthen this conclusion. First, DQB1*03:01-containing
heterodimers were consistent low-binding outliers in a seven-heterodimer HLA-DQ
panel, whereas multiple non-risk comparison molecules showed substantially
higher core binder rates. Second, the result persisted after exact and
identity-based sequence de-redundancy, arguing against simple GenBank
redundancy as the explanation. Third, record-level bootstrap intervals remained
far from the null comparison. Fourth, genotype, region, and year-stratified
analyses preserved the direction of effect. Fifth, IEDB human T-cell epitope
overlap analysis suggested that predicted DQB1*03:01 binders poorly cover known
core/nucleocapsid MHC-II epitope regions. Finally, reference-proteome controls
showed that DQB1*03:01-containing heterodimers can bind peptides from other HBV
proteins, supporting specificity of the core/capsid gap.

The core-position analysis is a useful addition because it moves the study
beyond global binder counts. The largest gap localized to the HBV core
N-terminus, especially windows spanning approximately positions 2-27. This
region should be prioritized if future experiments test HLA-DQ binding,
antigen processing, or CD4 T-cell recognition in DQB1*03:01-positive versus
DQB1*03:02-positive contexts.

The study also illustrates the value of hypothesis revision in public-data
research. The initial mutation-loss model was mechanistically attractive but did
not survive pilot testing. A stronger article emerged by retaining negative
mutation results as secondary context and focusing on the reproducible public
sequence signal. This restraint is important: the present analysis supports a
computational presentation-gap hypothesis, not direct proof of HBV-HCC
causality.

This study has important limitations. It predicts peptide-HLA binding, not
antigen processing, HLA-DQ surface presentation, or T-cell recognition. Public
viral records are not paired with host HLA genotypes, so the analysis cannot
infer within-host HLA-driven viral evolution. GenBank metadata are incomplete
and biased, and genotype/country sampling is uneven. HLA-DQ alpha/beta haplotype
phase is not known for viral sequence donors. The IEDB recommended method
showed weaker unique-peptide differences than NetMHCIIpan BA, emphasizing that
absolute thresholds depend on prediction method. Finally, IEDB epitope overlap
is limited by historical assay coverage and should not be interpreted as a
complete map of HBV core CD4 epitopes.

Despite these limitations, the study provides a reproducible computational
extension of a recent HBV-HCC host-genetic finding and nominates HBV core
antigen presentation as a focused mechanism for future validation.

## Data Availability

All viral sequences were downloaded from public NCBI GenBank records using NCBI
E-utilities. IEDB MHC-II predictions were generated through the public IEDB
MHC-II API. IEDB human HBV T-cell epitope records were retrieved from the IEDB
query API. Processed peptide metadata, prediction outputs, summary tables, and
analysis scripts are included in the accompanying project directory and should
be deposited in a public repository before journal submission.

## Code Availability

The reproducible workflow is implemented in the `scripts` directory. Main
commands and output files are listed in `submission/HBV_DQB10301_supplementary_note.md`.

## Ethics Statement

This study used only public viral sequences and public epitope database records.
No individual-level human participant data were accessed.

## Author Contributions

[To be completed.]

## Funding

[To be completed.]

## Conflicts of Interest

The author declares no competing interests. [Modify if needed.]

## References

1. Zhang T, Huang CJ, Chen HT, et al. HLA-DQB1*03:01 and risk of HBV-related
   HCC. Hepatology. 2026;83:374-386. doi:10.1097/HEP.0000000000001307.
2. Ji X, Zhang Q, Li B, et al. Impacts of human leukocyte antigen DQ genetic
   polymorphisms and their interactions with hepatitis B virus mutations on the
   risks of viral persistence, liver cirrhosis, and hepatocellular carcinoma.
   Infect Genet Evol. 2014;28:201-209. doi:10.1016/j.meegid.2014.09.032.
3. Wen J, Song C, Jiang D, et al. Hepatitis B virus genotype, mutations, human
   leukocyte antigen polymorphisms and their interactions in hepatocellular
   carcinoma: a multi-centre case-control study. Sci Rep. 2015;5:16489.
   doi:10.1038/srep16489.
4. Choga WT, Anderson M, Zumbika E, et al. In silico prediction of human
   leukocytes antigen class II binding hepatitis B virus peptides in Botswana.
   Viruses. 2020;12:731. doi:10.3390/v12070731.
5. Sugiyama M, Nishida N, Khor SS, et al. Human leukocyte antigen genotypes
   affect hepatitis B virus mutations associated with hepatocellular carcinoma.
   Hepatol Res. 2025;55:1445-1453. doi:10.1111/hepr.70007.
6. Vita R, Mahajan S, Overton JA, et al. The Immune Epitope Database (IEDB):
   2018 update. Nucleic Acids Res. 2019;47:D339-D343. doi:10.1093/nar/gky1006.
