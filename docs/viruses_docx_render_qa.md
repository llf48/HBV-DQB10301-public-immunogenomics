# Viruses DOCX Render QA

Audit date: 2026-05-01

Renderer: Documents skill `render_docx.py --renderer artifact-tool`

## Rendered Files

| DOCX | Pages rendered | QA status |
|---|---:|---|
| `submission_viruses/HBV_DQB10301_viruses_manuscript.docx` | 17 | Pass after author/correspondence update and 70-reference expansion |
| `submission_viruses/HBV_DQB10301_viruses_cover_letter.docx` | 1 | Pass after single-author and APC-waiver language update |
| `submission_viruses/APC_full_waiver_request_letter.docx` | 1 | Pass |
| `submission_viruses/HBV_DQB10301_viruses_figure_legends.docx` | 2 | Pass |
| `submission_viruses/HBV_DQB10301_viruses_supplementary_note.docx` | 3 | Pass |
| `submission_viruses/response_to_reviewers_template.docx` | 3 | Pass after single-author voice update |

## Visual Check

- No visible page-level text overlap.
- No clipped headings or footer text.
- No broken tables were present in the DOCX files.
- The figure legends, cover letter, and full APC waiver letter fit cleanly.
- The supplementary note and response template have short final pages but no
  rendering defect.
- After expanding to 70 references, the manuscript was re-rendered and the
  References heading was forced to begin on a new page to avoid an orphaned
  heading at the bottom of the preceding page.
- The manuscript front matter now includes Linfeng Liu, ORCID
  `0009-0009-2719-4427`, The First School of Clinical Medicine, Southern
  Medical University, and the supplied correspondence email.
- The cover letter and response template were checked for inconsistent plural
  author voice after converting the package to a single-author submission.

The rendered PNGs are stored under `submission_viruses/qa_*` for internal QA
and are not necessary for journal upload.
