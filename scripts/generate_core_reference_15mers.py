import csv
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
GB = PROJECT / "data" / "raw" / "NC_003977_2.gb"
OUT_META = PROJECT / "data" / "processed" / "core_reference_15mer_metadata.csv"
OUT_FASTA = PROJECT / "data" / "processed" / "core_reference_15mer.fasta"


def extract_core_translation(genbank_text):
    for match in re.finditer(r"CDS\s+.*?(?=\n\s{5}\S|\nORIGIN|$)", genbank_text, flags=re.S):
        block = match.group(0)
        if '/product="capsid protein"' not in block:
            continue
        translation = re.search(r'/translation="([^"]+)"', block, flags=re.S)
        if translation:
            return re.sub(r"\s+", "", translation.group(1))
    raise ValueError("Could not find capsid protein translation")


def main():
    seq = extract_core_translation(GB.read_text(encoding="utf-8"))
    rows = []
    fasta_lines = []
    seq_num = 1
    for start in range(1, len(seq) - 15 + 2):
        end = start + 14
        peptide = seq[start - 1 : end]
        peptide_id = f"CORE_NC003977|start{start}|end{end}"
        fasta_lines.extend([f">{peptide_id}", peptide])
        rows.append(
            {
                "seq_num": seq_num,
                "peptide_id": peptide_id,
                "protein": "core_capsid",
                "reference_accession": "NC_003977.2",
                "window_start": start,
                "window_end": end,
                "peptide": peptide,
            }
        )
        seq_num += 1

    OUT_META.parent.mkdir(parents=True, exist_ok=True)
    with OUT_META.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    OUT_FASTA.write_text("\n".join(fasta_lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} core 15-mers")
    print(OUT_META)
    print(OUT_FASTA)


if __name__ == "__main__":
    main()

