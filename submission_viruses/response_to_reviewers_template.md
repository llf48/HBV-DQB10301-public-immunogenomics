# Response to Reviewers Template

Manuscript: "Public HBV genotype B/C core diversity reveals an
HLA-DQB1*03:01-associated class-II presentation gap"

Journal: Viruses

## Response Overview

I thank the editor and reviewers for their careful evaluation of the
manuscript. I have revised the manuscript to clarify the computational and
hypothesis-generating nature of the study, strengthen the public-data
reproducibility description, and make the limitations more explicit. I agree
that the analysis predicts peptide-HLA binding and does not directly measure
antigen processing, HLA-DQ surface presentation, CD4 T-cell recognition, or
HBV-HCC causality.

## Reviewer Comment 1: Prediction-Based Study without Experimental Validation

**Reviewer comment:** [Paste comment here.]

**Response:** I agree that experimental validation is required to establish
biochemical binding, cellular antigen presentation, and CD4 T-cell recognition.
The study has been framed as a public-data computational analysis and
hypothesis-generating prioritization study. I have revised the Abstract,
Discussion, and Conclusions to avoid causal or experimental language and to
state that the strongest core N-terminal windows should be considered
candidates for future validation.

**Manuscript changes:** [Add line/section references after revision.]

## Reviewer Comment 2: GenBank Redundancy and Sampling Bias

**Reviewer comment:** [Paste comment here.]

**Response:** I agree that GenBank records are not a random population sample
and can be redundant or geographically uneven. For this reason, the analysis
included exact core de-duplication, greedy 99% and 95% identity
de-redundancy, record-level bootstrap, genotype/region/year stratification, and
leave-one-stratum-out checks. The DQB1*03:01-associated gap was preserved in
these analyses, indicating that the main result is not explained by simple
public-database redundancy.

**Manuscript changes:** [Add line/section references after revision.]

## Reviewer Comment 3: Lack of Host-Virus Pairing

**Reviewer comment:** [Paste comment here.]

**Response:** I agree. The GenBank viral records are not paired with host HLA
genotypes, and the manuscript does not infer within-host HLA-driven selection.
The analysis asks a different question: whether naturally observed public HBV
genotype B/C core sequences remain poorly covered by DQB1*03:01-containing
HLA-DQ heterodimers compared with non-risk comparators. I have clarified this
distinction in the Discussion.

**Manuscript changes:** [Add line/section references after revision.]

## Reviewer Comment 4: IEDB Coverage Is Incomplete

**Reviewer comment:** [Paste comment here.]

**Response:** I agree that IEDB does not provide a complete map of possible
HBV core CD4 T-cell epitopes. I use IEDB overlap only as an external annotation
of previously assayed human HBV T-cell regions, not as a comprehensive truth
set. The primary conclusion is based on predicted binding across public
genotype B/C core diversity and robustness analyses, with IEDB overlap serving
as a supportive check.

**Manuscript changes:** [Add line/section references after revision.]

## Reviewer Comment 5: Method Dependence of MHC-II Prediction

**Reviewer comment:** [Paste comment here.]

**Response:** I agree that MHC-II prediction depends on method and threshold.
The revised manuscript emphasizes that absolute binder rates differ between
NetMHCIIpan BA and the IEDB recommended method. However, the occurrence-weighted
direction of the primary DQB1*03:02 versus DQB1*03:01 comparison was preserved.
I therefore present the conclusion as a robust directional presentation gap
rather than as a claim tied to one absolute threshold.

**Manuscript changes:** [Add line/section references after revision.]

## Reviewer Comment 6: Novelty Relative to Prior DQB1*03:01-HBV-HCC Work

**Reviewer comment:** [Paste comment here.]

**Response:** The prior study established the host-genetic association and
provided a reference-sequence binding clue. The contribution is to test whether
that clue remains visible across public HBV genotype B/C core diversity and to
add expanded HLA-DQ comparison, de-redundancy, bootstrap, stratification,
position-level core gap mapping, IEDB epitope overlap, reference-proteome
controls, and a public reproducible workflow.

**Manuscript changes:** [Add line/section references after revision.]
