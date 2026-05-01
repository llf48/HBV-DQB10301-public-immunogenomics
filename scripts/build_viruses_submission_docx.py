from __future__ import annotations

from pathlib import Path

from build_submission_docx import build_docx


ROOT = Path(__file__).resolve().parents[1]
SUBMISSION = ROOT / "submission_viruses"

FILES = [
    (
        SUBMISSION / "HBV_DQB10301_viruses_manuscript.md",
        SUBMISSION / "HBV_DQB10301_viruses_manuscript.docx",
        "manuscript",
    ),
    (
        SUBMISSION / "HBV_DQB10301_viruses_cover_letter.md",
        SUBMISSION / "HBV_DQB10301_viruses_cover_letter.docx",
        "letter",
    ),
    (
        SUBMISSION / "APC_full_waiver_request_letter.md",
        SUBMISSION / "APC_full_waiver_request_letter.docx",
        "letter",
    ),
    (
        SUBMISSION / "HBV_DQB10301_viruses_figure_legends.md",
        SUBMISSION / "HBV_DQB10301_viruses_figure_legends.docx",
        "legends",
    ),
    (
        SUBMISSION / "HBV_DQB10301_viruses_supplementary_note.md",
        SUBMISSION / "HBV_DQB10301_viruses_supplementary_note.docx",
        "supplement",
    ),
    (
        SUBMISSION / "response_to_reviewers_template.md",
        SUBMISSION / "response_to_reviewers_template.docx",
        "supplement",
    ),
]


def main() -> None:
    for md_path, out_path, kind in FILES:
        build_docx(md_path, out_path, kind)
        print(out_path)


if __name__ == "__main__":
    main()
