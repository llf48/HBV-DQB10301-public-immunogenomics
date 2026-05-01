import csv
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
GB = PROJECT / "data" / "raw" / "hbv_bc_pilot_5_records.gb"
OUT_META = PROJECT / "data" / "processed" / "core_pilot_bc_15mer_metadata.csv"
OUT_FASTA = PROJECT / "data" / "processed" / "core_pilot_bc_15mer.fasta"


def extract_core_translations():
    text = GB.read_text(encoding="utf-8")
    records = []
    for record in text.split("\n//"):
        locus = re.search(r"LOCUS\s+(\S+)", record)
        if not locus:
            continue
        accession = locus.group(1)
        note_match = re.search(r'/note="([^"]*(?:subgenotype|recombinant)[^"]*)"', record, flags=re.I)
        genotype_note = note_match.group(1) if note_match else ""
        for match in re.finditer(r"CDS\s+.*?(?=\n\s{5}\S|\nORIGIN|$)", record, flags=re.S):
            block = match.group(0)
            if '/product="core protein"' not in block:
                continue
            translation = re.search(r'/translation="([^"]+)"', block, flags=re.S)
            if translation:
                seq = re.sub(r"\s+", "", translation.group(1))
                records.append((accession, genotype_note, seq))
    return records


def main():
    rows = []
    fasta_lines = []
    seen = {}
    seq_num = 1
    for accession, genotype_note, seq in extract_core_translations():
        for start in range(1, len(seq) - 15 + 2):
            end = start + 14
            peptide = seq[start - 1 : end]
            key = (peptide, start)
            if key in seen:
                seen[key]["accessions"].append(accession)
                continue
            peptide_id = f"CORE_BC_PILOT|start{start}|{peptide}"
            seen[key] = {
                "seq_num": seq_num,
                "peptide_id": peptide_id,
                "protein": "core_capsid",
                "accessions": [accession],
                "genotype_notes": [genotype_note],
                "window_start": start,
                "window_end": end,
                "peptide": peptide,
            }
            seq_num += 1

    for item in seen.values():
        item["source_accessions"] = ";".join(sorted(set(item.pop("accessions"))))
        item["genotype_notes"] = ";".join(sorted(set(item["genotype_notes"])))
        rows.append(item)
        fasta_lines.extend([f">{item['peptide_id']}", item["peptide"]])

    OUT_META.parent.mkdir(parents=True, exist_ok=True)
    with OUT_META.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    OUT_FASTA.write_text("\n".join(fasta_lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} unique core 15-mers from {len(extract_core_translations())} pilot records")
    print(OUT_META)
    print(OUT_FASTA)


if __name__ == "__main__":
    main()
