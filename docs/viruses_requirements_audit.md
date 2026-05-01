# Viruses / MDPI Submission Requirements Audit

Audit date: 2026-05-01

Target journal: *Viruses* (MDPI)

## Official Sources Checked

- Viruses journal page: https://www.mdpi.com/journal/viruses
- Viruses instructions link: https://www.mdpi.com/journal/viruses/instructions
- MDPI Author Layout Style Guide: https://www.mdpi.com/authors/layout
- MDPI Reference List and Citations Style Guide: https://www.mdpi.com/authors/references

Note: the Viruses-specific instructions URL was linked from the live Viruses
journal page, but automated access to that page triggered MDPI's site challenge.
The package therefore uses the live Viruses journal page for journal identity
and the official MDPI author guides for manuscript structure, abstract,
graphical abstract, figures, tables, back matter, and references.

## Journal Fit

- Viruses is a peer-reviewed, open-access virology journal published monthly by
  MDPI.
- The journal is indexed in PubMed and listed as JCR Q2 in Virology on the live
  journal page at audit time.
- The present manuscript is framed as an Article, not a Review or Brief Report,
  because it reports a reproducible public-data analysis with methods, results,
  figures, tables, and validation/sensitivity analyses.

## Front Matter Checklist

- Title is concise and result-bearing.
- Article type is stated as Article.
- Abstract is one paragraph and kept below the MDPI 200-word ceiling.
- Abstract avoids citations, figure references, equations, and tables.
- Keywords are provided.
- Author name, affiliation, ORCID, and correspondence have been filled from the
  supplied prior manuscript document.

## Main Text Checklist

- Main sections follow IMRAD with a Conclusions section:
  Introduction; Materials and Methods; Results; Discussion; Conclusions.
- Headings are numbered and use no more than three levels.
- Figures are cited in sequence in the Results.
- The manuscript avoids claims of experimental proof and uses prediction-focused
  language throughout.

## Back Matter Checklist

The Viruses manuscript now includes the MDPI-style back matter sequence:

- Supplementary Materials
- Author Contributions
- Funding
- Institutional Review Board Statement
- Informed Consent Statement
- Data Availability Statement
- Acknowledgments
- Conflicts of Interest
- References

## Figures and Tables Checklist

- Main figures are exported as PNG and SVG.
- PNG exports were regenerated at 600 dpi.
- The graphical abstract is a separate original workflow diagram, not a copy of
  a body figure.
- Graphical abstract PNG size is 6630 x 3123 pixels, exceeding the MDPI minimum
  1100 x 560 pixels.
- Figure captions are prepared separately and describe each figure without
  requiring the main text.
- Tables are provided as editable CSV files rather than image-only tables.

## Data and Code Availability Checklist

- Public data sources are identified: NCBI GenBank, IEDB MHC-II prediction API,
  IEDB query API, and HBV reference genome NC_003977.2.
- The journal-facing manuscript now contains 70 numbered references, all cited
  in the main text and all verified through PubMed/NCBI E-utilities.
- A one-step reproduction script is provided for Windows PowerShell and Unix
  shell.
- Environment files are provided as `requirements.txt` and `environment.yml`.
- GitHub and Zenodo deposition text is provided with live repository and DOI
  links.

## Remaining Author-Side Items

- Confirm APC/discount status in the Viruses submission system.
- Submit the prepared full APC waiver request before or at the beginning of the
  submission process.
- Upload graphical abstract as a separate GA file if requested by the submission
  system.
