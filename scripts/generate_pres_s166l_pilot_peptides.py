import csv
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
GB = PROJECT / "data" / "raw" / "hbv_bc_pilot_5_records.gb"
OUT_META = PROJECT / "data" / "processed" / "pres_s166l_pilot_15mer_metadata.csv"
OUT_FASTA = PROJECT / "data" / "processed" / "pres_s166l_pilot_15mer.fasta"

ACCESSION = "PQ046054"
POSITION = 166
REF = "S"
ALT = "L"
PEPTIDE_LEN = 15


def extract_large_s_translation(genbank_text, accession):
    for record in genbank_text.split("\n//"):
        if f"LOCUS       {accession}" not in record:
            continue
        for match in re.finditer(r"CDS\s+.*?(?=\n\s{5}\S|\nORIGIN|$)", record, flags=re.S):
            block = match.group(0)
            if "large S protein" not in block and "large envelope" not in block:
                continue
            translation = re.search(r'/translation="([^"]+)"', block, flags=re.S)
            if translation:
                return re.sub(r"\s+", "", translation.group(1))
    raise ValueError(f"Could not find large S translation for {accession}")


def windows_containing(seq_len, position, peptide_len=15):
    first_start = max(1, position - peptide_len + 1)
    last_start = min(position, seq_len - peptide_len + 1)
    for start in range(first_start, last_start + 1):
        yield start, start + peptide_len - 1


def mutate(seq, position, alt):
    zero = position - 1
    return seq[:zero] + alt + seq[zero + 1 :]


def main():
    seq = extract_large_s_translation(GB.read_text(encoding="utf-8"), ACCESSION)
    observed = seq[POSITION - 1]
    if observed != REF:
        raise ValueError(f"Expected {REF} at large S {POSITION}, observed {observed}")

    mutant_seq = mutate(seq, POSITION, ALT)
    variant_id = f"PRES_S166L_{ACCESSION}_{REF}{POSITION}{ALT}"
    rows = []
    fasta_lines = []
    seq_num = 1
    for state, protein_seq in [("WT", seq), ("MUT", mutant_seq)]:
        for start, end in windows_containing(len(seq), POSITION, PEPTIDE_LEN):
            peptide = protein_seq[start - 1 : end]
            peptide_id = f"{variant_id}|{state}|start{start}|pos{POSITION}"
            fasta_lines.extend([f">{peptide_id}", peptide])
            rows.append(
                {
                    "seq_num": seq_num,
                    "peptide_id": peptide_id,
                    "mutation_id": "PRES_S166L_SUGIYAMA2025",
                    "variant_id": variant_id,
                    "state": state,
                    "protein": "large_S",
                    "position": POSITION,
                    "ref": REF,
                    "alt": ALT,
                    "window_start": start,
                    "window_end": end,
                    "peptide": peptide,
                    "reference_accession": ACCESSION,
                }
            )
            seq_num += 1

    OUT_META.parent.mkdir(parents=True, exist_ok=True)
    with OUT_META.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    OUT_FASTA.write_text("\n".join(fasta_lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} peptide records for {variant_id}")
    print(OUT_META)
    print(OUT_FASTA)


if __name__ == "__main__":
    main()
