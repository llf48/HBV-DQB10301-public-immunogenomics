# Reference Expansion QA: 70 PubMed-Verified References

Audit date: 2026-05-01

Skill workflow used: `extract-from-pdfs` as a structured literature-database
workflow, adapted to PubMed metadata rather than PDF extraction.

## Database Linkage

- Source database: PubMed / NCBI E-utilities.
- Curated PMID table: `data/manual/viruses_reference_pmids_70.csv`.
- Generated metadata table: `docs/references/viruses_reference_library_70.csv`.
- Generated readable library: `docs/references/viruses_reference_library_70.md`.
- Submission reference list: `submission_viruses/references_70.md`.

## Evidence Coverage

| Evidence role | Reference numbers |
|---|---|
| HBV-HCC epidemiology and disease background | 1-7 |
| HBV genotype, mutation, and HCC association | 8-16, 69-70 |
| HLA-DQ/HLA-DQB1 and HBV persistence/HCC genetics | 17-31 |
| HBV core/nucleocapsid CD4 T-cell biology and epitope variation | 32-40 |
| HBV-specific T-cell dysfunction, PD-1, exhaustion, and viral control | 41-48 |
| Related HBV HLA peptide or host-pathogen genomic studies | 49-51 |
| IEDB, NetMHCIIpan, and MHC-II prediction methodology | 52-65 |
| GenBank and public nucleotide-sequence database support | 66-68 |

## Consistency Checks

- Number of references in the Viruses manuscript: 70.
- Unique cited references in the main text: 70.
- Missing cited references: none.
- Out-of-range citations: none.
- PMID retained in audit tables but omitted from the journal-facing manuscript
  reference list to keep MDPI-style references clean.

## Claim Boundary

The expanded references strengthen background and method justification but do
not change the article's claim boundary. The manuscript still presents a
computational public-data prediction study, not experimental proof of antigen
processing, HLA-DQ surface presentation, CD4 T-cell recognition, or HBV-HCC
causality.
