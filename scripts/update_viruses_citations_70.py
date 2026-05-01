from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "submission_viruses" / "HBV_DQB10301_viruses_manuscript.md"
REFERENCES = ROOT / "submission_viruses" / "references_70.md"


REPLACEMENTS = {
    """Chronic hepatitis B virus (HBV) infection remains a major cause of
hepatocellular carcinoma (HCC). Progression from infection to chronic liver
inflammation, cirrhosis, and HCC is shaped by both viral genetic variation and
host immune genetics. The HLA region is repeatedly implicated in HBV
persistence and HBV-related liver disease, consistent with a central role for
antigen presentation in long-term antiviral immune control.""": """Chronic hepatitis B virus (HBV) infection remains a major cause of
hepatocellular carcinoma (HCC) [1-7]. Progression from infection to chronic
liver inflammation, cirrhosis, and HCC is shaped by both viral genetic
variation and host immune genetics [8-16]. The HLA region is repeatedly
implicated in HBV persistence and HBV-related liver disease, consistent with a
central role for antigen presentation in long-term antiviral immune control
[17-31].""",
    """HLA class II presentation is especially relevant because CD4 T-cell responses
coordinate antiviral immunity, antibody maturation, cytotoxic T-cell function,
and immune memory. HBV core/nucleocapsid antigens are major immune targets, and
impaired core-directed helper responses could plausibly contribute to viral
persistence or immune exhaustion. A recent Hepatology study connected
HLA-DQB1*03:01 with HBV-related HCC risk and reported lower predicted binding
of HBV nucleocapsid peptides by DQB1*03:01-containing HLA-DQ molecules. That
finding provided a mechanistic clue, but it also raised an important public-data
question: is the predicted core/nucleocapsid presentation gap stable across
naturally occurring HBV genotype B/C sequence diversity?""": """HLA class II presentation is especially relevant because CD4 T-cell responses
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
HBV genotype B/C sequence diversity?""",
    """This question matters because HBV genotype B and genotype C predominate in many
East Asian HBV-HCC settings, and genotype C has been associated with increased
HCC risk in epidemiologic studies. A reference-sequence binding deficit could
be biologically meaningful, but viral sequence diversity could also weaken,
erase, or reverse the signal. Public GenBank HBV genomes therefore provide an
opportunity to test whether a DQB1*03:01-associated core presentation gap is
preserved across real viral diversity, even though the viral sequences are not
paired with host HLA genotypes.""": """This question matters because HBV genotype B and genotype C predominate in many
East Asian HBV-HCC settings, and genotype C, precore/core variation, and viral
mutation profiles have been associated with liver-disease severity and HCC risk
[8-16,69,70]. A reference-sequence binding deficit could be biologically
meaningful, but viral sequence diversity could also weaken, erase, or reverse
the signal. Public GenBank HBV genomes therefore provide an opportunity to test
whether a DQB1*03:01-associated core presentation gap is preserved across real
viral diversity, even though the viral sequences are not paired with host HLA
genotypes [66-68].""",
    """We initially evaluated a narrower mutation-loss model: whether reported
HCC-associated HBV coding mutations commonly create DQB1*03:01-specific
binder-to-non-binder loss. Exploratory HBx and PreS/S hotspot analyses did not
support that model as a main result. We therefore revised the study around the
stronger and more defensible public-data question: whether global public HBV
genotype B/C core diversity preserves a DQB1*03:01-associated class-II
presentation gap. Here, we combine public HBV sequence retrieval, HLA-DQ
heterodimer MHC-II prediction, expanded HLA-DQ panel comparison,
de-redundancy, stratified sensitivity analysis, IEDB T-cell epitope overlap,
and reference-proteome controls.""": """We initially evaluated a narrower mutation-loss model: whether reported
HCC-associated HBV coding mutations commonly create DQB1*03:01-specific
binder-to-non-binder loss [8-16,70]. Exploratory HBx and PreS/S hotspot
analyses did not support that model as a main result. We therefore revised the
study around the stronger and more defensible public-data question: whether
global public HBV genotype B/C core diversity preserves a
DQB1*03:01-associated class-II presentation gap. Here, we combine public HBV
sequence retrieval, HLA-DQ heterodimer MHC-II prediction, expanded HLA-DQ panel
comparison, de-redundancy, stratified sensitivity analysis, IEDB T-cell epitope
overlap, and reference-proteome controls [49-68].""",
    """peptide`, `epitope`, and `HLA-DQ`. The search identified related HBV-HLA-HCC
association studies, HBV mutation interaction studies, and HBV HLA class II
peptide prediction studies, but no PubMed-indexed study combining
DQB1*03:01-focused HLA-DQ heterodimer prediction, public HBV genotype B/C core
diversity, core-position gap analysis, and IEDB epitope overlap into a
quantified DQB1*03:01-associated presentation-gap framework.""": """peptide`, `epitope`, and `HLA-DQ`. The search identified related HBV-HLA-HCC
association studies, HBV mutation interaction studies, host-pathogen genomic
studies, and HBV HLA peptide-prediction studies [14-18,49-51], but no
PubMed-indexed study combining DQB1*03:01-focused HLA-DQ heterodimer
prediction, public HBV genotype B/C core diversity, core-position gap analysis,
and IEDB epitope overlap into a quantified DQB1*03:01-associated
presentation-gap framework.""",
    """NCBI nucleotide E-utilities were used to retrieve public complete-genome HBV
GenBank records annotated as genotype B or genotype C. The full query retrieved
3784 candidate records. GenBank CDS annotations were parsed to extract core
protein translations.""": """NCBI nucleotide E-utilities were used to retrieve public complete-genome HBV
GenBank records annotated as genotype B or genotype C [66-69]. The full query
retrieved 3784 candidate records. GenBank CDS annotations were parsed to
extract core protein translations.""",
    """MHC-II binding predictions were generated through the IEDB MHC-II prediction API
using NetMHCIIpan. Percentile rank <10 was defined as predicted binding, and
rank <2 was defined as strong predicted binding. As a method sensitivity check,
the IEDB recommended method was also run for the primary three HLA-DQ
heterodimers: DQA1*03:01/DQB1*03:02, DQA1*05:08/DQB1*03:01, and
DQA1*06:01/DQB1*03:01.""": """MHC-II binding predictions were generated through the IEDB MHC-II prediction API
using NetMHCIIpan [52-65]. Percentile rank <10 was defined as predicted
binding, and rank <2 was defined as strong predicted binding. As a method
sensitivity check, the IEDB recommended method was also run for the primary
three HLA-DQ heterodimers: DQA1*03:01/DQB1*03:02,
DQA1*05:08/DQB1*03:01, and DQA1*06:01/DQB1*03:01.""",
    """The IEDB query API was used to retrieve positive human T-cell assay records for
HBV (`NCBITaxon:10407`). Retrieved linear epitopes were normalized by sequence,
source antigen, source position, and MHC class. Core/nucleocapsid epitopes were
identified from curated antigen names and parent antigen names containing
`core` or `nucleocapsid`. Predicted core 15-mers were considered overlapping if
the predicted peptide contained the known epitope sequence or was contained
within the known epitope sequence. Overlap was summarized for all known human
core/nucleocapsid T-cell epitopes and separately for known MHC-II
core/nucleocapsid epitopes.""": """The IEDB query API was used to retrieve positive human T-cell assay records for
HBV (`NCBITaxon:10407`) [52-56]. Retrieved linear epitopes were normalized by
sequence, source antigen, source position, and MHC class. Core/nucleocapsid
epitopes were identified from curated antigen names and parent antigen names
containing `core` or `nucleocapsid`. Predicted core 15-mers were considered
overlapping if the predicted peptide contained the known epitope sequence or
was contained within the known epitope sequence. Overlap was summarized for all
known human core/nucleocapsid T-cell epitopes and separately for known MHC-II
core/nucleocapsid epitopes.""",
    """To test whether the DQB1*03:01 gap was core-specific rather than a global HBV
protein effect, the reference HBV genome NC_003977.2 was parsed for polymerase,
large envelope, X protein, and capsid/core translations. Overlapping 15-mers
were generated for each protein and predicted against the same seven HLA-DQ
heterodimers using IEDB NetMHCIIpan.""": """To test whether the DQB1*03:01 gap was core-specific rather than a global HBV
protein effect, the reference HBV genome NC_003977.2 was parsed for
polymerase, large envelope, X protein, and capsid/core translations [66-69].
Overlapping 15-mers were generated for each protein and predicted against the
same seven HLA-DQ heterodimers using IEDB NetMHCIIpan [57-65].""",
}


def main() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS.items():
        if old not in text:
            if new in text:
                continue
            raise RuntimeError(f"Replacement target not found:\n{old[:160]}")
        text = text.replace(old, new)

    references = REFERENCES.read_text(encoding="utf-8").strip()
    if "## References" not in text:
        raise RuntimeError("References heading not found")
    text = text.split("## References", 1)[0].rstrip() + "\n\n" + references + "\n"
    MANUSCRIPT.write_text(text, encoding="utf-8")
    print(MANUSCRIPT)


if __name__ == "__main__":
    main()
