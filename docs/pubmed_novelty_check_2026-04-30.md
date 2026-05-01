# PubMed Novelty Check, 2026-04-30

## Skill Route

The literature check followed the local life-science research routing logic:

- `research-router-skill` for scope selection.
- `ncbi-entrez-skill` for PubMed queries.
- The bundled Entrez Python helper failed on this machine because of an SSL
  EOF error. The same NCBI E-utilities endpoints were therefore accessed with
  `curl.exe` as a fallback.

## Core Question Checked

Does PubMed already contain a study that combines all of the following?

1. HLA-DQB1*03:01 or DQB1*03:01 focus.
2. HBV-related HCC context.
3. Public genotype B/C HBV core/nucleocapsid diversity.
4. HLA-DQ alpha/beta heterodimer MHC-II binding prediction.
5. Quantification of a DQB1*03:01-associated presentation gap.

## Searches Run

### Collision searches

These were designed to find direct topic collisions.

| Query | PubMed result |
| --- | --- |
| `DQB1*03:01 HBV NetMHCIIpan` | 0 records |
| `DQB1*03:01 hepatitis B peptide epitope` | 0 records |
| `HLA-DQ HBV HCC mutation peptide epitope` | 0 records |
| `HLA-DQB1 risk HBV-related HCC nucleocapsid binding` | 1 record, PMID 40084945 |

Interpretation: the direct computational cross-point was not found. The closest
paper is Zhang et al. 2026, which motivates the project but does not test
whether the nucleocapsid/core binding gap is stable across public genotype B/C
sequence diversity.

### Related-study searches

| Query | Result summary |
| --- | --- |
| `HLA-DQ hepatitis B hepatocellular carcinoma mutation` | 7 records, including Ji 2014 and Wen 2015 |
| `hepatitis B HLA class II peptide prediction` | 15 records, including Choga 2020 |

Interpretation: the broader fields are active. There are HBV-HLA-HCC genetic
association papers, HBV mutation interaction papers, and HBV HLA-II peptide
prediction papers. The gap is narrower: DQB1*03:01-centered HBV core public
sequence immunogenomics.

## Key Related Sources

- Zhang T et al. HLA-DQB1*03:01 and risk of HBV-related HCC. Hepatology 2026.
  PMID: 40084945. PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12353533/
- Ji X et al. Impacts of HLA-DQ genetic polymorphisms and interactions with HBV
  mutations. Infect Genet Evol 2014. PMID: 25281206.
- Wen J et al. HBV genotype, mutations, HLA polymorphisms and interactions in
  HCC. Sci Rep 2015. PMID: 26568165.
- Choga WT et al. In silico prediction of HLA class II binding HBV peptides in
  Botswana. Viruses 2020. PMID: 32640609.
- Sugiyama M et al. HLA genotypes affect HBV mutations associated with HCC.
  Hepatol Res 2025. PMID: 40728240.

## Novelty Judgment

This is not a completely empty field. The project should not claim that no one
has studied HBV, HLA-DQ, or HCC together.

The defensible novelty claim is:

> This study extends the reported DQB1*03:01-HBV-HCC nucleocapsid binding axis
> by testing whether the predicted HLA-DQB1*03:01-associated class-II core
> presentation gap is preserved across public HBV genotype B/C core diversity.

This is a viable computational public-data article if it is framed as
hypothesis-generating and not as experimental proof of CD4 T-cell escape.

