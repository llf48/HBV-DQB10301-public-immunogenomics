# Paper Polish and Logic Report

Audit date: 2026-05-01

Skill frameworks used: `Paper-Polish-Workflow-skill` and
`nature-writing-skill` from GitHub.

## Final Storyline

The paper no longer depends on the weak initial claim that individual
HCC-associated HBV mutations commonly create DQB1*03:01-specific
binder-to-non-binder loss. Negative hotspot pilots are retained as background
discipline, while the main article is built around the stronger reproducible
result:

> Public HBV genotype B/C core diversity preserves a large predicted HLA-DQ
> class-II presentation gap for DQB1*03:01-containing heterodimers.

This storyline is clearer, better supported by public data, and easier for
reviewers to evaluate.

## Argument Chain

1. Prior literature links HLA-DQB1*03:01 to HBV-related HCC risk and suggests a
   nucleocapsid binding deficit.
2. A reference-sequence result could be fragile, so public genotype B/C viral
   diversity is the correct next computational test.
3. Across 1576 QC-passed public genotype B/C records and 11176 unique core
   peptide windows, two DQB1*03:01-containing HLA-DQ heterodimers are low-binding
   outliers.
4. The effect survives method sensitivity, de-redundancy, bootstrap,
   stratification, IEDB epitope overlap checks, and reference-proteome controls.
5. The study therefore nominates HBV core/capsid presentation, especially
   N-terminal windows, as a focused experimental hypothesis.

## Claim Boundary Check

| Claim type | Current manuscript wording | Status |
|---|---|---|
| Prediction | "predicted binding", "predicted presentation gap" | Pass |
| Mechanism | "supports a hypothesis", "nominates" | Pass |
| Causality | Does not claim proof of HCC causality | Pass |
| Experiment | Explicitly states no proof of processing, surface presentation, or T-cell recognition | Pass |
| Public data | Identifies NCBI GenBank and IEDB limitations | Pass |

## Number Consistency Check

Key numbers are consistent across abstract, results, discussion, figure legends,
and supplementary notes:

- 3784 candidate GenBank records
- 1576 QC-passed genotype-labeled records
- 1538 unique accession identifiers
- 11176 unique core 15-mer windows
- 259916 occurrence-weighted windows
- 10.52% occurrence-weighted binder rate for DQA1*03:01/DQB1*03:02
- 0.23% and 0.80% for DQA1*05:08/DQB1*03:01 and DQA1*06:01/DQB1*03:01
- 50 known human HBV core/nucleocapsid MHC-II epitopes in IEDB
- 20 NetMHCIIpan binder overlaps for DQB1*03:02 and zero for the two
  DQB1*03:01-containing risk pairs

## Anti-AI Polish Check

High-risk generic phrases were avoided or replaced:

- Avoided: "groundbreaking", "proves", "revolutionary", "unprecedented".
- Used instead: "supports", "suggests", "nominates", "hypothesis-generating",
  "computational public-data result".
- Limitations are specific rather than formulaic.
- The discussion acknowledges failed pilots, which makes the paper sound more
  like real research and less like a one-direction narrative.

## Residual Risks

- The article remains computational and prediction-based.
- Public HBV sequences are not paired with host HLA data.
- GenBank sampling is non-random and geographically uneven.
- IEDB epitope coverage is incomplete and historically biased.
- Some reviewers may ask for at least one experimental validation; the prebuttal
  document provides a response strategy rather than pretending this risk does
  not exist.

## Editorial Positioning

Best target framing: computational virology / viral immunogenomics / public-data
resource Article in *Viruses*.

Avoid framing: definitive HCC mechanism, therapeutic vaccine discovery,
validated CD4 T-cell escape, or host-virus coevolution study.
