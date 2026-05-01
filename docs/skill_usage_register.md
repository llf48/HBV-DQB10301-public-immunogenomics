# Skill Usage Register

Date: 2026-05-01

## Local Life Sciences Research Skills

- `research-router-skill`: used to route the task into public biomedical data
  retrieval, immunogenomics, and manuscript-planning workflows.
- `ncbi-entrez-skill`: used as the NCBI/GenBank retrieval framework. The final
  implemented retrieval used NCBI E-utilities through reproducible scripts.
- `ipd-skill`: reviewed for HLA nomenclature/database reasoning. The final
  analysis used IEDB-supported HLA-DQ heterodimer names.
- `extract-from-pdfs`: used as the structured literature-database workflow for
  the final reference expansion. The project did not require new PDF extraction
  in this step; instead, the skill pattern was adapted to a PubMed/NCBI
  E-utilities metadata database with PMID, DOI, topic role, and evidence
  rationale fields.

## GitHub-Sourced Skills Reviewed Through The GitHub Plugin

- `Nigmat-future/biomedical-codex-skills`: used conceptually for public dataset
  intake, paper-to-pipeline conversion, and results-to-figure workflow
  structure.
- `Agents365-ai/seurat-skill`: reviewed but not applied because this project
  contains no single-cell or spatial transcriptomic data.
- `Galaxy-Dawn/publication-chart-skill`: used to install and check publication
  plotting tooling (`pubfig`, `pubtab`) and to guide high-resolution PNG/SVG
  figure generation, graphical abstract review, caption review, table
  structure, and final visual QA.
- `Lylll9436/Paper-Polish-Workflow-skill`: used through its logic-checking and
  anti-AI-polish references to produce the Viruses logic report,
  reviewer-prebuttal document, cover-letter refinements, and response-to-reviewers
  template.
- `SyntaxSmith/nature-writing-skill`: used to tighten the article framing,
  keep claims restrained, handle the negative mutation-pilot result, and write
  the manuscript/cover letter in a submission-facing style.

## Skills Mentioned But Not Located Or Not Applicable

- `K-Dense`: searched through the GitHub plugin route but no unambiguous usable
  repository was identified in this session.
- `Paper-Polish-Workflow-skill`: located under the GitHub repository
  `Lylll9436/Paper-Polish-Workflow-skill`; the available subskills were used for
  logic and polish, not as autonomous agents.
- `slr/meta skills`: no dedicated local skill with that exact name was
  available. The PubMed novelty review and extracted-paper reasoning were
  documented manually.

## Practical Outcome

The final project does not rely on a hidden skill state. All data retrieval,
prediction, analysis, figure generation, and document-building steps are stored
as scripts or Markdown/DOCX artifacts in the project directory.
