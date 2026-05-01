# Public HBV genotype B/C core diversity reveals an HLA-DQB1*03:01-associated class-II presentation gap

## Article Type

Article

## Short Title

HBV core diversity and DQB1*03:01 presentation gap

## Authors

Linfeng Liu 1,*

ORCID: https://orcid.org/0009-0009-2719-4427

## Affiliations

1. The First School of Clinical Medicine, Southern Medical University,
   Guangzhou, Guangdong, China

## Correspondence

* Correspondence: Linfeng Liu, The First School of Clinical Medicine, Southern
  Medical University, Guangzhou, Guangdong, China. Email: 2549512000@qq.com;
  ORCID: https://orcid.org/0009-0009-2719-4427.

## Abstract

HLA-DQB1*03:01 has been associated with increased risk of hepatitis B virus
(HBV)-related hepatocellular carcinoma, and prior reference-sequence analyses
suggested reduced HLA-DQ binding to HBV nucleocapsid peptides. This study asked
whether this predicted class-II presentation gap is preserved across naturally
occurring public HBV genotype B/C core diversity. The analysis retrieved 3784
candidate NCBI GenBank complete-genome records, retained 1576 quality-controlled
genotype-labeled core translations, generated 11176 unique overlapping core
15-mer windows, and predicted binding for seven HLA-DQ heterodimers using IEDB
NetMHCIIpan. Occurrence-weighted predicted core binder rates were 10.52% for
DQA1*03:01/DQB1*03:02 but only 0.23% and 0.80% for DQA1*05:08/DQB1*03:01 and
DQA1*06:01/DQB1*03:01. The gap persisted after method sensitivity analysis,
exact and identity-based de-redundancy, record-level bootstrap,
genotype/region/year stratification, core-position mapping, IEDB human T-cell
epitope overlap analysis, and reference-proteome controls. The strongest gap
localized to HBV core N-terminal windows, especially positions 2-27. These
public-data results support a focused, experimentally testable hypothesis that
DQB1*03:01-containing HLA-DQ molecules leave a core/capsid CD4 T-cell
presentation gap in HBV genotype B/C infection.

## Keywords

hepatitis B virus; HLA-DQB1*03:01; HLA-DQ; MHC class II; CD4 T cell; HBV core;
hepatocellular carcinoma; immunogenomics; epitope prediction

## 1. Introduction

Chronic hepatitis B virus (HBV) infection remains a major cause of
hepatocellular carcinoma (HCC) [1-7]. Progression from infection to chronic
liver inflammation, cirrhosis, and HCC is shaped by both viral genetic
variation and host immune genetics [8-16]. The HLA region is repeatedly
implicated in HBV persistence and HBV-related liver disease, consistent with a
central role for antigen presentation in long-term antiviral immune control
[17-31].

HLA class II presentation is especially relevant because CD4 T-cell responses
coordinate antiviral immunity, antibody maturation, cytotoxic T-cell function,
and immune memory. HBV core/nucleocapsid antigens are major immune targets, and
core-directed CD4 T-cell responses, processing, epitope variation, and
HLA-restricted reactivity have been repeatedly described in HBV infection
[32-40]. Impaired core-directed helper responses could plausibly contribute to
viral persistence, global T-cell dysfunction, or immune exhaustion [41-48]. A
recent Hepatology study connected HLA-DQB1*03:01 with HBV-related HCC risk and
reported lower predicted binding of HBV nucleocapsid peptides by
DQB1*03:01-containing HLA-DQ molecules [17]. That finding provided a
mechanistic clue, but it also raised an important public-data question: is the
predicted core/nucleocapsid presentation gap stable across naturally occurring
HBV genotype B/C sequence diversity?

This question matters because HBV genotype B and genotype C predominate in many
East Asian HBV-HCC settings, and genotype C, precore/core variation, and viral
mutation profiles have been associated with liver-disease severity and HCC risk
[8-16,69,70]. A reference-sequence binding deficit could be biologically
meaningful, but viral sequence diversity could also weaken, erase, or reverse
the signal. Public GenBank HBV genomes therefore provide an opportunity to test
whether a DQB1*03:01-associated core presentation gap is preserved across real
viral diversity, even though the viral sequences are not paired with host HLA
genotypes [66-68].

The initial analysis evaluated a narrower mutation-loss model: whether reported
HCC-associated HBV coding mutations commonly create DQB1*03:01-specific
binder-to-non-binder loss [8-16,70]. Exploratory HBx and PreS/S hotspot
analyses did not support that model as a main result. The study was therefore
revised around the stronger and more defensible public-data question: whether
global public HBV genotype B/C core diversity preserves a
DQB1*03:01-associated class-II presentation gap. The workflow combines public
HBV sequence retrieval, HLA-DQ heterodimer MHC-II prediction, expanded HLA-DQ panel
comparison, de-redundancy, stratified sensitivity analysis, IEDB T-cell epitope
overlap, and reference-proteome controls [49-68].

## 2. Materials and Methods

### 2.1. Literature and Novelty Review

PubMed was queried on 2026-04-30 using combinations of `DQB1*03:01`,
`HLA-DQB1`, `HBV`, `hepatitis B`, `HCC`, `nucleocapsid`, `NetMHCIIpan`,
`peptide`, `epitope`, and `HLA-DQ`. The search identified related HBV-HLA-HCC
association studies, HBV mutation interaction studies, host-pathogen genomic
studies, and HBV HLA peptide-prediction studies [14-18,49-51], but no
PubMed-indexed study combining DQB1*03:01-focused HLA-DQ heterodimer
prediction, public HBV genotype B/C core diversity, core-position gap analysis,
and IEDB epitope overlap into a quantified DQB1*03:01-associated
presentation-gap framework.

### 2.2. Public HBV Sequence Retrieval and Quality Control

NCBI nucleotide E-utilities were used to retrieve public complete-genome HBV
GenBank records annotated as genotype B or genotype C [66-69]. The full query
retrieved 3784 candidate records. GenBank CDS annotations were parsed to
extract core protein translations.

Records were excluded if they lacked a usable core CDS translation, contained
recombinant annotations in the definition or feature notes, had core length
outside 170-190 amino acids, contained non-standard amino-acid characters, or
lacked a genotype B/C query label. The final quality-controlled set contained
1576 genotype-labeled records, corresponding to 1538 unique accession
identifiers. The QC-passed set included 633 genotype B query records and 943
genotype C query records.

### 2.3. Core Peptide Generation

For each quality-controlled core protein, all overlapping 15-mer peptides were
generated. Peptides were collapsed by peptide sequence and core window start
position. The final public-diversity analysis included 11176 unique core 15-mer
windows and 259916 occurrence-weighted windows.

### 2.4. HLA-DQ Panel

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

### 2.5. MHC-II Binding Prediction

MHC-II binding predictions were generated through the IEDB MHC-II prediction API
using NetMHCIIpan [52-65]. Percentile rank <10 was defined as predicted
binding, and rank <2 was defined as strong predicted binding. As a method
sensitivity check, the IEDB recommended method was also run for the primary
three HLA-DQ heterodimers: DQA1*03:01/DQB1*03:02,
DQA1*05:08/DQB1*03:01, and DQA1*06:01/DQB1*03:01.

### 2.6. Statistical Analysis

Binder counts were summarized using both unique peptide counts and
occurrence-weighted counts. Pairwise comparisons between the DQB1*03:02
comparator and other heterodimers used Fisher exact tests. P values that
underflowed to zero in SciPy are reported as P < 1e-300. Occurrence-weighted
rates were also calculated within genotype, region, country, and collection-year
strata when metadata were available.

### 2.7. Sequence De-Redundancy and Bootstrap Analysis

To assess sensitivity to public database redundancy, three de-redundant record
sets were created: exact core protein de-duplication, greedy 99% identity
de-redundancy, and greedy 95% identity de-redundancy. Occurrence-weighted HLA-DQ
binder rates were recomputed in each set without rerunning MHC-II prediction,
using accession-level source mappings.

Record-level bootstrap analysis used 1000 resamples of quality-controlled
records with replacement. Binder-rate confidence intervals, rate differences,
and rate ratios were calculated from accession-level totals.

### 2.8. Core-Position Gap Analysis

For each HBV core 15-mer window start, occurrence-weighted binder rates were
summarized for the DQB1*03:02 comparator and the combined DQB1*03:01 risk pairs.
A position-level gap was defined as the DQB1*03:02 occurrence-weighted binder
rate minus the combined DQB1*03:01 risk-pair occurrence-weighted binder rate.
Top gap windows were ranked by this difference.

### 2.9. IEDB Human HBV T-Cell Epitope Overlap

The IEDB query API was used to retrieve positive human T-cell assay records for
HBV (`NCBITaxon:10407`) [52-56]. Retrieved linear epitopes were normalized by
sequence, source antigen, source position, and MHC class. Core/nucleocapsid
epitopes were identified from curated antigen names and parent antigen names
containing `core` or `nucleocapsid`. Predicted core 15-mers were considered
overlapping if the predicted peptide contained the known epitope sequence or
was contained within the known epitope sequence. Overlap was summarized for all
known human core/nucleocapsid T-cell epitopes and separately for known MHC-II
core/nucleocapsid epitopes.

### 2.10. Reference HBV Proteome Control

To test whether the DQB1*03:01 gap was core-specific rather than a global HBV
protein effect, the reference HBV genome NC_003977.2 was parsed for
polymerase, large envelope, X protein, and capsid/core translations [66-69].
Overlapping 15-mers were generated for each protein and predicted against the
same seven HLA-DQ heterodimers using IEDB NetMHCIIpan [57-65].

## 3. Results

### 3.1. Public Genotype B/C Core Diversity Generated 11176 Unique Core Peptide Windows

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

The public-data workflow, from NCBI sequence retrieval through the final
presentation-gap analysis, is summarized in the graphical abstract.

### 3.2. DQB1*03:01-Containing HLA-DQ Heterodimers Were Outliers in an Expanded HLA-DQ Panel

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

These expanded-panel results are shown in Figure 1 and establish the primary
observation: DQB1*03:01-containing heterodimers are low-binding outliers for
public HBV genotype B/C core peptides rather than merely lower than one
selected comparator.

### 3.3. The DQB1*03:02 Comparator Exceeded DQB1*03:01-Containing Pairs in Statistical Comparisons

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

### 3.4. The Gap Was Preserved across Genotype, Region, and Collection-Year Strata

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
These stratified rate-ratio analyses are provided in the supplementary tables
and are integrated with the de-redundancy checks in the robustness figure
described below.

### 3.5. Method Sensitivity Supported the Occurrence-Weighted Direction of Effect

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
The method comparison is shown in Figure 2.

### 3.6. The DQB1*03:01 Core Gap Survived De-Redundancy and Bootstrap Analysis

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
The de-redundancy and bootstrap results are summarized in Figure 3 and in
Supplementary Table S3.

### 3.7. Core-Position Analysis Localized the Strongest Gap to the HBV Core N-Terminus

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
The position-level gap map is shown in Figure 4.

### 3.8. Predicted DQB1*03:01 Binders Did Not Overlap Known Core/Nucleocapsid MHC-II Epitopes

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
The IEDB overlap analysis is shown in Figure 5.

### 3.9. Reference Proteome Analysis Supported a Core-Specific, Not Global, DQB1*03:01 Gap

Reference-proteome analysis showed that the DQB1*03:01-containing heterodimers
were not globally unable to bind HBV peptides. For reference X protein,
DQA1*05:08/DQB1*03:01 and DQA1*06:01/DQB1*03:01 had binder rates of 7.86% and
7.14%, respectively. For large envelope protein, they had binder rates of 9.87%
and 8.80%. For polymerase, they had binder rates of 2.44% and 3.55%. In
contrast, for reference core/capsid peptides, both DQB1*03:01-containing
heterodimers had 0/169 predicted binders. This supports a core/capsid-focused
presentation gap rather than a general failure of DQB1*03:01-containing
heterodimers to bind HBV-derived peptides.
The reference-proteome control is provided as Supplementary Figure S1.

### 3.10. HCC Hotspot Pilots Did Not Support a Mutation-Loss Main Model

Exploratory analyses of literature-derived HBx and PreS/S HCC-associated
hotspots did not support the initial hypothesis that HCC-associated coding
mutations commonly create DQB1*03:01-specific binder-to-non-binder loss. HBx
hotspots were largely non-binding for the tested DQB1*03:01 pairs, and the
PreS/S S166L example showed allele-specific binding remodeling rather than
loss. These negative pilots motivated the final focus on the robust HBV core
presentation-gap result.

## 4. Discussion

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

## 5. Conclusions

Public HBV genotype B/C core diversity preserves a large predicted HLA-DQ
class-II presentation gap for DQB1*03:01-containing heterodimers. The result is
robust to public-database redundancy, stratification, method sensitivity, IEDB
epitope overlap checks, and reference-proteome controls. The study does not
establish direct antigen presentation or HCC causality, but it converts a
host-genetic HBV-HCC association into a reproducible public-data mechanism:
core/capsid peptides, especially N-terminal windows, are prioritized candidates
for DQB1*03:01-focused experimental validation.

## Supplementary Materials

The following supporting files are prepared for submission: Supplementary Note
S1, which documents data sources, workflow steps, quality-control filters,
negative pilot analyses, and reproducibility commands; Supplementary Table S1,
expanded HLA-DQ NetMHCIIpan summary by allele; Supplementary Table S2,
pairwise Fisher exact tests versus the DQB1*03:02 comparator; Supplementary
Table S3, de-redundancy and bootstrap sensitivity results; Supplementary Table
S4, top core-position presentation-gap windows; Supplementary Table S5, IEDB
core/nucleocapsid epitope overlap summary; and Supplementary Figure S1,
reference HBV proteome control. The reproducible public repository also
contains machine-readable CSV outputs and analysis scripts.

## Author Contributions

Conceptualization, methodology, software, validation, formal analysis, data
curation, writing-original draft preparation, writing-review and editing,
visualization, and project administration: Linfeng Liu.

## Funding

This research received no external funding.

## Institutional Review Board Statement

Not applicable. This study used only public viral sequences and public epitope
database records and did not involve human participants or animals.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

All viral sequences were downloaded from public NCBI GenBank records using NCBI
E-utilities. IEDB MHC-II predictions were generated through the public IEDB
MHC-II API. IEDB human HBV T-cell epitope records were retrieved from the IEDB
query API. Processed peptide metadata, prediction outputs, summary tables, and
analysis scripts are prepared for deposition in a public GitHub repository and
archival Zenodo release before journal submission. The repository and DOI
placeholders are provided in the accompanying submission package and should be
replaced with live links after deposition.

## Code Availability

The reproducible workflow is implemented in the `scripts` directory. Main
commands and output files are listed in
`submission_viruses/HBV_DQB10301_viruses_supplementary_note.md`.

## Acknowledgments

The author thanks the maintainers of NCBI GenBank, IEDB, and the open-source
scientific Python ecosystem.

## Conflicts of Interest

The author declares no competing interests.

## References

1. McGlynn KA, Petrick JL, El-Serag HB. Epidemiology of Hepatocellular Carcinoma. Hepatology. 2021;73 Suppl 1(Suppl 1):4-13. doi:10.1002/hep.31288.
2. Yuen MF, Chen DS, Dusheiko GM, Janssen HLA, Lau DTY, Locarnini SA, et al. Hepatitis B virus infection. Nat Rev Dis Primers. 2018;4:18035. doi:10.1038/nrdp.2018.35.
3. MacLachlan JH, Cowie BC. Hepatitis B virus epidemiology. Cold Spring Harb Perspect Med. 2015;5(5):a021410. doi:10.1101/cshperspect.a021410.
4. European Association for the Study of the Liver. EASL 2017 Clinical Practice Guidelines on the management of hepatitis B virus infection. J Hepatol. 2017;67(2):370-398. doi:10.1016/j.jhep.2017.03.021.
5. Campbell C, Wang T, McNaughton AL, Barnes E, Matthews PC. Risk factors for the development of hepatocellular carcinoma (HCC) in chronic hepatitis B virus (HBV) infection: a systematic review and meta-analysis. J Viral Hepat. 2021;28(3):493-507. doi:10.1111/jvh.13452.
6. Lin CL, Kao JH. Review article: the prevention of hepatitis B-related hepatocellular carcinoma. Aliment Pharmacol Ther. 2018;48(1):5-14. doi:10.1111/apt.14683.
7. Xu C, Zhou W, Wang Y, Qiao L. Hepatitis B virus-induced hepatocellular carcinoma. Cancer Lett. 2014;345(2):216-22. doi:10.1016/j.canlet.2013.08.035.
8. Akrami H, Monjezi MR, Ilbeigi S, Amiri F, Fattahi MR. The Association Between Hepatitis B Virus Mutations and the Risk of Liver Disease and Hepatocellular Carcinoma. Curr Mol Med. 2022;22(6):514-523. doi:10.2174/1566524021666210816094412.
9. Liu S, Zhang H, Gu C, Yin J, He Y, Xie J, et al. Associations between hepatitis B virus mutations and the risk of hepatocellular carcinoma: a meta-analysis. J Natl Cancer Inst. 2009;101(15):1066-82. doi:10.1093/jnci/djp180.
10. Chan HL, Hui AY, Wong ML, Tse AM, Hung LC, Wong VW, et al. Genotype C hepatitis B virus infection is associated with an increased risk of hepatocellular carcinoma. Gut. 2004;53(10):1494-8. doi:10.1136/gut.2003.033324.
11. Kao JH. Hepatitis B virus genotypes and hepatocellular carcinoma in Taiwan. Intervirology. 2003;46(6):400-7. doi:10.1159/000074999.
12. Kim DW, Lee SA, Hwang ES, Kook YH, Kim BJ. Naturally occurring precore/core region mutations of hepatitis B virus genotype C related to hepatocellular carcinoma. PLoS One. 2012;7(10):e47372. doi:10.1371/journal.pone.0047372.
13. Kumar R. Review on hepatitis B virus precore/core promoter mutations and their correlation with genotypes and liver disease severity. World J Hepatol. 2022;14(4):708-718. doi:10.4254/wjh.v14.i4.708.
14. Wen J, Song C, Jiang D, Jin T, Dai J, Zhu L, et al. Hepatitis B virus genotype, mutations, human leukocyte antigen polymorphisms and their interactions in hepatocellular carcinoma: a multi-centre case-control study. Sci Rep. 2015;5:16489. doi:10.1038/srep16489.
15. An P, Xu J, Yu Y, Winkler CA. Host and Viral Genetic Variation in HBV-Related Hepatocellular Carcinoma. Front Genet. 2018;9:261. doi:10.3389/fgene.2018.00261.
16. Sugiyama M, Nishida N, Khor SS, Shin-I T, Hino K, Honda M, et al. Human Leukocyte Antigen Genotypes Affect Hepatitis B Virus Mutations Associated With Hepatocellular Carcinoma. Hepatol Res. 2025;55(11):1445-1453. doi:10.1111/hepr.70007.
17. Zhang T, Huang CJ, Chen HT, Huang YH, Pan MH, Lee MH, et al. HLA-DQB1*03:01 and risk of HBV-related HCC. Hepatology. 2026;83(2):374-386. doi:10.1097/HEP.0000000000001307.
18. Ji X, Zhang Q, Li B, Du Y, Yin J, Liu W, et al. Impacts of human leukocyte antigen DQ genetic polymorphisms and their interactions with hepatitis B virus mutations on the risks of viral persistence, liver cirrhosis, and hepatocellular carcinoma. Infect Genet Evol. 2014;28:201-9. doi:10.1016/j.meegid.2014.09.032.
19. Mbarek H, Ochi H, Urabe Y, Kumar V, Kubo M, Hosono N, et al. A genome-wide association study of chronic hepatitis B identified novel risk locus in a Japanese population. Hum Mol Genet. 2011;20(19):3884-92. doi:10.1093/hmg/ddr301.
20. Hu Z, Liu Y, Zhai X, Dai J, Jin G, Wang L, et al. New loci associated with chronic hepatitis B virus infection in Han Chinese. Nat Genet. 2013;45(12):1499-503. doi:10.1038/ng.2809.
21. Kim YJ, Kim HY, Lee JH, Yu SJ, Yoon JH, Lee HS, et al. A genome-wide association study identified new variants associated with the risk of chronic hepatitis B. Hum Mol Genet. 2013;22(20):4233-8. doi:10.1093/hmg/ddt266.
22. Hu L, Zhai X, Liu J, Chu M, Pan S, Jiang J, et al. Genetic variants in human leukocyte antigen/DP-DQ influence both hepatitis B virus clearance and hepatocellular carcinoma development. Hepatology. 2012;55(5):1426-31. doi:10.1002/hep.24799.
23. Xiang X, Guo Y, Yang L, Ge Q, Mijit S, Xu F. Association of human leukocyte antigen DP/DQ gene polymorphisms with chronic hepatitis B in Chinese Han and Uygur populations. Infect Genet Evol. 2016;43:407-11. doi:10.1016/j.meegid.2016.06.022.
24. Ochi Y, Hashimoto S, Kawabe N, Murao M, Nakano T, Kan T, et al. HLA-DQ gene polymorphisms are associated with hepatocellular carcinoma and hepatitis B surface antigen in chronic hepatitis B virus infection. Hepatol Res. 2017;47(8):755-766. doi:10.1111/hepr.12812.
25. Gao X, Liu W, Zhang X, Tang L, Wang L, Yan L, et al. Genetic polymorphism of HLA-DQ confers susceptibility to hepatitis B virus-related hepatocellular carcinoma: a case-control study in Han population in China. Tumour Biol. 2016;37(9):12103-12111. doi:10.1007/s13277-016-5077-z.
26. Kim LH, Cheong HS, Namgoong S, Kim JO, Kim JH, Park BL, et al. Replication of genome wide association studies on hepatocellular carcinoma susceptibility loci of STAT4 and HLA-DQ in a Korean population. Infect Genet Evol. 2015;33:72-6. doi:10.1016/j.meegid.2015.04.013.
27. Liu C, Cheng B. Association of polymorphisms of human leucocyte antigen-DQA1 and DQB1 alleles with chronic hepatitis B virus infection, liver cirrhosis and hepatocellular carcinoma in Chinese. Int J Immunogenet. 2007;34(5):373-8. doi:10.1111/j.1744-313X.2007.00702.x.
28. Ou G, Xu H, Yu H, Liu X, Yang L, Ji X, et al. The roles of HLA-DQB1 gene polymorphisms in hepatitis B virus infection. J Transl Med. 2018;16(1):362. doi:10.1186/s12967-018-1716-z.
29. Al-Qahtani AA, Al-Anazi MR, Abdo AA, Sanai FM, Al-Hamoudi W, Alswat KA, et al. Association between HLA variations and chronic hepatitis B virus infection in Saudi Arabian patients. PLoS One. 2014;9(1):e80445. doi:10.1371/journal.pone.0080445.
30. Tao J, Su K, Yu C, Liu X, Wu W, Xu W, et al. Fine mapping analysis of HLA-DP/DQ gene clusters on chromosome 6 reveals multiple susceptibility loci for HBV infection. Amino Acids. 2015;47(12):2623-34. doi:10.1007/s00726-015-2054-6.
31. Kozuka R, Enomoto M, Sato-Matsubara M, Yoshida K, Motoyama H, Hagihara A, et al. Association between HLA-DQA1/DRB1 polymorphism and development of hepatocellular carcinoma during entecavir treatment. J Gastroenterol Hepatol. 2019;34(5):937-946. doi:10.1111/jgh.14454.
32. Ferrari C, Bertoletti A, Penna A, Cavalli A, Valli A, Missale G, et al. Identification of immunodominant T cell epitopes of the hepatitis B virus nucleocapsid antigen. J Clin Invest. 1991;88(1):214-22. doi:10.1172/JCI115280.
33. Jung MC, Diepolder HM, Spengler U, Wierenga EA, Zachoval R, Hoffmann RM, et al. Activation of a heterogeneous hepatitis B (HB) core and e antigen-specific CD4+ T-cell population during seroconversion to anti-HBe and anti-HBs in hepatitis B virus infection. J Virol. 1995;69(6):3358-68. doi:10.1128/JVI.69.6.3358-3368.1995.
34. Marinos G, Torre F, Chokshi S, Hussain M, Clarke BE, Rowlands DJ, et al. Induction of T-helper cell response to hepatitis B core antigen in chronic hepatitis B: a major factor in activation of the host immune response to the hepatitis B virus. Hepatology. 1995;22(4 Pt 1):1040-9. doi:10.1016/0270-9139(95)90607-x.
35. Diepolder HM, Jung MC, Keller E, Schraut W, Gerlach JT, Grüner N, et al. A vigorous virus-specific CD4+ T cell response may contribute to the association of HLA-DR13 with viral clearance in hepatitis B. Clin Exp Immunol. 1998;113(2):244-51. doi:10.1046/j.1365-2249.1998.00665.x.
36. Diepolder HM, Ries G, Jung MC, Schlicht HJ, Gerlach JT, Gr ner N, et al. Differential antigen-processing pathways of the hepatitis B virus e and core proteins. Gastroenterology. 1999;116(3):650-7. doi:10.1016/s0016-5085(99)70187-3.
37. Cao T, Desombere I, Vanlandschoot P, Sällberg M, Leroux-Roels G. Characterization of HLA DR13-restricted CD4(+) T cell epitopes of hepatitis B core antigen associated with self-limited, acute hepatitis B. J Gen Virol. 2002;83(Pt 12):3023-3033. doi:10.1099/0022-1317-83-12-3023.
38. Torre F, Cramp M, Owsianka A, Dornan E, Marsden H, Carman W, et al. Direct evidence that naturally occurring mutations within hepatitis B core epitope alter CD4+ T-cell reactivity. J Med Virol. 2004;72(3):370-6. doi:10.1002/jmv.20016.
39. Hosono S, Tai PC, Wang W, Ambrose M, Hwang DG, Yuan TT, et al. Core antigen mutations of human hepatitis B virus in hepatomas accumulate in MHC class II-restricted T cell epitopes. Virology. 1995;212(1):151-62. doi:10.1006/viro.1995.1463.
40. Desmond CP, Bartholomeusz A, Gaudieri S, Revill PA, Lewin SR. A systematic review of T-cell epitopes in hepatitis B virus: identification, genotypic variation and relevance to antiviral therapeutics. Antivir Ther. 2008;13(2):161-75.
41. Park JJ, Wong DK, Wahed AS, Lee WM, Feld JJ, Terrault N, et al. Hepatitis B Virus--Specific and Global T-Cell Dysfunction in Chronic Hepatitis B. Gastroenterology. 2016;150(3):684-695.e5. doi:10.1053/j.gastro.2015.11.050.
42. Peng G, Li S, Wu W, Tan X, Chen Y, Chen Z. PD-1 upregulation is associated with HBV-specific T cell dysfunction in chronic hepatitis B patients. Mol Immunol. 2008;45(4):963-70. doi:10.1016/j.molimm.2007.07.038.
43. Watanabe T, Bertoletti A, Tanoto TA. PD-1/PD-L1 pathway and T-cell exhaustion in chronic hepatitis virus infection. J Viral Hepat. 2010;17(7):453-8. doi:10.1111/j.1365-2893.2010.01313.x.
44. Ye B, Liu X, Li X, Kong H, Tian L, Chen Y. T-cell exhaustion in chronic hepatitis B infection: current knowledge and clinical significance. Cell Death Dis. 2015;6(3):e1694. doi:10.1038/cddis.2015.42.
45. Dong Y, Li X, Zhang L, Zhu Q, Chen C, Bao J, et al. CD4+ T cell exhaustion revealed by high PD-1 and LAG-3 expression and the loss of helper T cell function in chronic hepatitis B. BMC Immunol. 2019;20(1):27. doi:10.1186/s12865-019-0309-9.
46. Wen C, Zhou Y, Zhou Y, Wang Y, Dong Z, Gu S, et al. HBV Core-specific CD4+ T cells correlate with sustained viral control upon off-treatment in HBeAg-positive chronic hepatitis B patients. Antiviral Res. 2023;213:105585. doi:10.1016/j.antiviral.2023.105585.
47. Cheng Y, Gunasegaran B, Singh HD, Dutertre CA, Loh CY, Lim JQ, et al. Non-terminally exhausted tumor-resident memory HBV-specific T cell responses correlate with relapse-free survival in hepatocellular carcinoma. Immunity. 2021;54(8):1825-1840.e7. doi:10.1016/j.immuni.2021.06.013.
48. Chua C, Salimzadeh L, Ma AT, Adeyi OA, Seo H, Boukhaled GM, et al. IL-2 produced by HBV-specific T cells as a biomarker of viral control and predictor of response to PD-1 therapy across clinical phases of chronic hepatitis B. Hepatol Commun. 2023;7(12):e0337. doi:10.1097/HC9.0000000000000337.
49. Choga WT, Anderson M, Zumbika E, Phinius BB, Mbangiwa T, Bhebhe LN, et al. In Silico Prediction of Human Leukocytes Antigen (HLA) Class II Binding Hepatitis B Virus (HBV) Peptides in Botswana. Viruses. 2020;12(7):731. doi:10.3390/v12070731.
50. Srivastava M, Copin R, Choy A, Zhou A, Olsen O, Wolf S, et al. Proteogenomic identification of Hepatitis B virus (HBV) genotype-specific HLA-I restricted peptides from HBV-positive patient liver tissues. Front Immunol. 2022;13:1032716. doi:10.3389/fimmu.2022.1032716.
51. Xu ZM, Gnouamozi GE, Rüeger S, Shea PR, Buti M, Chan HL, et al. Joint host-pathogen genomic analysis identifies hepatitis B virus mutations associated with human NTCP and HLA class I variation. Am J Hum Genet. 2024;111(6):1018-1034. doi:10.1016/j.ajhg.2024.04.013.
52. Vita R, Blazeska N, Marrama D, IEDB Curation Team Members, Duesing S, Bennett J, et al. The Immune Epitope Database (IEDB): 2024 update. Nucleic Acids Res. 2025;53(D1):D436-D443. doi:10.1093/nar/gkae1092.
53. Vita R, Mahajan S, Overton JA, Dhanda SK, Martini S, Cantrell JR, et al. The Immune Epitope Database (IEDB): 2018 update. Nucleic Acids Res. 2019;47(D1):D339-D343. doi:10.1093/nar/gky1006.
54. Dhanda SK, Mahajan S, Paul S, Yan Z, Kim H, Jespersen MC, et al. IEDB-AR: immune epitope database-analysis resource in 2019. Nucleic Acids Res. 2019;47(W1):W502-W506. doi:10.1093/nar/gkz452.
55. Kim Y, Ponomarenko J, Zhu Z, Tamang D, Wang P, Greenbaum J, et al. Immune epitope database analysis resource. Nucleic Acids Res. 2012;40(Web Server issue):W525-30. doi:10.1093/nar/gks438.
56. Kim Y, Sette A, Peters B. Applications for T-cell epitope queries and tools in the Immune Epitope Database and Analysis Resource. J Immunol Methods. 2011;374(1-2):62-9. doi:10.1016/j.jim.2010.10.010.
57. Reynisson B, Alvarez B, Paul S, Peters B, Nielsen M. NetMHCpan-4.1 and NetMHCIIpan-4.0: improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data. Nucleic Acids Res. 2020;48(W1):W449-W454. doi:10.1093/nar/gkaa379.
58. Karosiene E, Rasmussen M, Blicher T, Lund O, Buus S, Nielsen M. NetMHCIIpan-3.0, a common pan-specific MHC class II prediction method including all three human MHC class II isotypes, HLA-DR, HLA-DP and HLA-DQ. Immunogenetics. 2013;65(10):711-24. doi:10.1007/s00251-013-0720-y.
59. Nielsen M, Justesen S, Lund O, Lundegaard C, Buus S. NetMHCIIpan-2.0 - Improved pan-specific HLA-DR predictions using a novel concurrent alignment and weight optimization training procedure. Immunome Res. 2010;6:9. doi:10.1186/1745-7580-6-9.
60. Nielsen M, Lundegaard C, Blicher T, Peters B, Sette A, Justesen S, et al. Quantitative predictions of peptide binding to any HLA-DR molecule of known sequence: NetMHCIIpan. PLoS Comput Biol. 2008;4(7):e1000107. doi:10.1371/journal.pcbi.1000107.
61. Yang Y, Wei Z, Cia G, Song X, Pucci F, Rooman M, et al. MHCII-peptide presentation: an assessment of the state-of-the-art prediction methods. Front Immunol. 2024;15:1293706. doi:10.3389/fimmu.2024.1293706.
62. Nilsson JB, Kaabinejadian S, Yari H, Kester MGD, van Balen P, Hildebrand WH, et al. Accurate prediction of HLA class II antigen presentation across all loci using tailored data acquisition and refined machine learning. Sci Adv. 2023;9(47):eadj6367. doi:10.1126/sciadv.adj6367.
63. Jensen KK, Andreatta M, Marcatili P, Buus S, Greenbaum JA, Yan Z, et al. Improved methods for predicting peptide binding affinity to MHC class II molecules. Immunology. 2018;154(3):394-406. doi:10.1111/imm.12889.
64. Wang P, Sidney J, Kim Y, Sette A, Lund O, Nielsen M, et al. Peptide binding predictions for HLA DR, DP and DQ molecules. BMC Bioinformatics. 2010;11:568. doi:10.1186/1471-2105-11-568.
65. Stražar M, Park J, Abelin JG, Taylor HB, Pedersen TK, Plichta DR, et al. HLA-II immunopeptidome profiling and deep learning reveal features of antigenicity to inform antigen discovery. Immunity. 2023;56(7):1681-1698.e13. doi:10.1016/j.immuni.2023.05.009.
66. Sayers EW, Cavanaugh M, Frisse L, Pruitt KD, Schneider VA, Underwood BA, et al. GenBank 2025 update. Nucleic Acids Res. 2025;53(D1):D56-D61. doi:10.1093/nar/gkae1114.
67. Sayers EW, Cavanaugh M, Clark K, Pruitt KD, Sherry ST, Yankie L, et al. GenBank 2024 Update. Nucleic Acids Res. 2024;52(D1):D134-D137. doi:10.1093/nar/gkad903.
68. Karsch-Mizrachi I, Nakamura Y, Cochrane G, International Nucleotide Sequence Database Collaboration. The International Nucleotide Sequence Database Collaboration. Nucleic Acids Res. 2012;40(Database issue):D33-7. doi:10.1093/nar/gkr1006.
69. Kramvis A. Genotypes and genetic variability of hepatitis B virus. Intervirology. 2014;57(3-4):141-50. doi:10.1159/000360947.
70. Al-Qahtani AA, Al-Anazi MR, Nazir N, Abdo AA, Sanai FM, Al-Hamoudi WK, et al. The Correlation Between Hepatitis B Virus Precore/Core Mutations and the Progression of Severe Liver Disease. Front Cell Infect Microbiol. 2018;8:355. doi:10.3389/fcimb.2018.00355.
