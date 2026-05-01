# Reviewer Prebuttal and Limitations Strategy

This document anticipates likely reviewer objections for a computational
public-data submission to *Viruses*. It can be used before submission to refine
the manuscript and after review as the backbone of a response letter.

## Concern 1: "This is only prediction; there is no experiment."

**Likely reviewer wording:** The study predicts peptide-HLA binding but does
not validate HLA-DQ binding, antigen processing, surface presentation, or CD4
T-cell recognition.

**Response strategy:** Agree and make the claim boundary explicit. The article
does not present the result as experimental proof. Its value is to test whether
a recently reported DQB1*03:01-HBV-HCC nucleocapsid signal persists across
public genotype B/C viral diversity and to nominate focused windows for
experimental validation.

**Manuscript defenses already included:**

- Abstract calls the result an experimentally testable hypothesis.
- Discussion states that the study predicts binding, not antigen processing,
  HLA-DQ surface presentation, or T-cell recognition.
- Core-position analysis narrows future validation to specific N-terminal core
  windows rather than a vague genome-wide list.

**Possible revision sentence:** "We agree that biochemical and cellular assays
are required to establish presentation and recognition; the present study is
therefore positioned as a public-data prioritization and robustness analysis,
not as direct immunologic validation."

## Concern 2: "GenBank is biased and redundant."

**Likely reviewer wording:** Public HBV records are not a population sample and
may contain duplicate outbreak, country, laboratory, or study-specific
submissions.

**Response strategy:** Agree and point to redundancy and stratification checks.
The claim does not require GenBank to estimate global prevalence perfectly; it
asks whether the DQB1*03:01 gap persists across public genotype B/C diversity.

**Manuscript defenses already included:**

- Exact core de-duplication.
- Greedy 99% and 95% identity de-redundancy.
- Record-level bootstrap.
- Genotype, region, country, collection-year, and leave-one-stratum-out
  sensitivity analyses.
- Explicit limitation that GenBank metadata are incomplete and biased.

**Possible revision sentence:** "The direction and magnitude of the gap were
retained even after reducing the dataset to 95% identity representatives,
arguing that the result is not explained by simple sequence redundancy."

## Concern 3: "There is no host-virus pairing."

**Likely reviewer wording:** Viral sequences are not linked to donor HLA
genotypes, so the study cannot infer within-host selection or HLA-driven escape.

**Response strategy:** Agree fully. This is a presentation-capacity analysis,
not a host-virus paired evolutionary analysis. The conclusion should remain
that public viral diversity preserves a predicted DQB1*03:01 presentation gap,
not that DQB1*03:01 selected these viral sequences.

**Manuscript defenses already included:**

- Methods and Discussion state that sequences are public viral records without
  host HLA pairing.
- The paper avoids terms such as "escape selected by DQB1*03:01" as a main
  conclusion.

**Possible revision sentence:** "Because host HLA genotypes are unavailable for
the GenBank records, we do not infer HLA-driven viral evolution; instead, we
ask whether naturally observed genotype B/C core sequences remain poorly
covered by DQB1*03:01-containing HLA-DQ heterodimers."

## Concern 4: "IEDB epitope coverage is incomplete."

**Likely reviewer wording:** Lack of overlap with IEDB MHC-II epitopes may
reflect incomplete historical assays rather than true absence of epitopes.

**Response strategy:** Agree and treat IEDB as a supportive external annotation,
not as a complete truth set.

**Manuscript defenses already included:**

- IEDB overlap is presented after the primary prediction and robustness
  analyses.
- Discussion states that IEDB overlap is limited by historical assay coverage.

**Possible revision sentence:** "We use IEDB overlap as an external annotation
of previously assayed human HBV T-cell regions, not as a complete map of all
possible HBV core CD4 epitopes."

## Concern 5: "The result depends on NetMHCIIpan BA."

**Likely reviewer wording:** MHC-II predictors differ, especially for HLA-DQ,
and binding threshold choices may affect results.

**Response strategy:** Highlight that the IEDB recommended method lowers
absolute rates but preserves the occurrence-weighted direction of the primary
effect. Do not overstate unique-peptide results under the recommended method.

**Manuscript defenses already included:**

- Method sensitivity is a main Result section and Figure 2.
- Discussion states that absolute thresholds are method-dependent.

**Possible revision sentence:** "Although unique-peptide differences were
weaker under the IEDB recommended method, the occurrence-weighted DQB1*03:02
advantage persisted, so the main conclusion is directional rather than
threshold-exclusive."

## Concern 6: "Why is this novel if the Hepatology paper already did binding prediction?"

**Likely reviewer wording:** Prior work already linked DQB1*03:01 to HBV-HCC
and predicted reduced nucleocapsid binding.

**Response strategy:** Distinguish reference-sequence mechanism from public
viral-diversity robustness.

**Manuscript defenses already included:**

- The paper explicitly says it extends, not replaces, the prior finding.
- Novel pieces include public genotype B/C diversity, expanded HLA-DQ panel,
  de-redundancy, bootstrap, genotype/region/year sensitivity, position-level
  core gap mapping, IEDB epitope overlap, reference-proteome control, and an
  open reproducible workflow.

**Possible revision sentence:** "The prior study provided the host-genetic
association and a reference-sequence mechanistic clue; our contribution is to
test whether that clue remains visible across public genotype B/C HBV core
diversity and to localize the strongest gap to specific core windows."

## Concern 7: "Why not keep the HCC mutation-loss hypothesis?"

**Likely reviewer wording:** The title and final claim do not focus on
HCC-associated coding mutations.

**Response strategy:** Be transparent that negative pilots changed the study.
This is a strength: the final paper follows the strongest supported result.

**Manuscript defenses already included:**

- Results include a short negative pilot section.
- Discussion frames hypothesis revision as public-data discipline.

**Possible revision sentence:** "Exploratory hotspot analyses did not support a
mutation-loss main model, so we revised the manuscript around the robust core
presentation-gap signal rather than forcing an unsupported mutation narrative."
