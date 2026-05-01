import csv
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
PANEL = PROJECT / "data" / "manual" / "hcc_hbv_mutation_panel_iteration2.csv"
OUT_META = PROJECT / "data" / "processed" / "iteration2_hotspot_15mer_metadata.csv"
OUT_FASTA = PROJECT / "data" / "processed" / "iteration2_hotspot_15mer.fasta"

HBX_NC003977_REF = (
    "MAARLCCQLDPARDVLCLRPVGAESCGRPFSGSLGTLSSPSPSAVPTDHGAHLSLRGLPVCAFSSAGPCALRFTSARR"
    "METTVNAHQILPKVLHKRTLGLSAMSTTDLEAYFKDCLFKDWEELGEEIRLKVFVLGGCRHKLVCAPAPCNFFTSA"
)

PEPTIDE_LEN = 15


def read_genotype_c_large_s():
    gb = PROJECT / "data" / "raw" / "hbv_bc_pilot_5_records.gb"
    text = gb.read_text(encoding="utf-8")
    accession = "PQ046054"
    for record in text.split("\n//"):
        if f"LOCUS       {accession}" not in record:
            continue
        for match in re.finditer(r"CDS\s+.*?(?=\n\s{5}\S|\nORIGIN|$)", record, flags=re.S):
            block = match.group(0)
            if "large S protein" not in block and "large envelope" not in block:
                continue
            translation = re.search(r'/translation="([^"]+)"', block, flags=re.S)
            if translation:
                return re.sub(r"\s+", "", translation.group(1))
    raise ValueError("Could not extract PQ046054 large S translation")


def extract_translation_from_genbank(path, accession, gene_name):
    text = path.read_text(encoding="utf-8")
    for record in text.split("\n//"):
        if f"LOCUS       {accession}" not in record:
            continue
        for match in re.finditer(r"CDS\s+.*?(?=\n\s{5}\S|\nORIGIN|$)", record, flags=re.S):
            block = match.group(0)
            if f'/gene="{gene_name}"' not in block or "/translation=" not in block:
                continue
            translation = re.search(r'/translation="([^"]+)"', block, flags=re.S)
            if translation:
                return re.sub(r"\s+", "", translation.group(1))
    raise ValueError(f"Could not extract {gene_name} translation for {accession}")


def read_lc852227_hbx():
    return extract_translation_from_genbank(
        PROJECT / "data" / "raw" / "hbv_c2_candidate_10.gb", "LC852227", "X"
    )


REFERENCE_SEQS = {
    ("HBx", "NC_003977.2"): HBX_NC003977_REF,
    ("HBx", "LC852227"): read_lc852227_hbx,
    ("large_S", "PQ046054"): read_genotype_c_large_s,
}


def parse_mutation_spec(spec):
    muts = []
    for item in spec.split(";"):
        item = item.strip()
        match = re.fullmatch(r"([A-Z])(\d+)([A-Z])", item)
        if not match:
            raise ValueError(f"Unsupported mutation spec: {item}")
        ref, pos, alt = match.groups()
        muts.append((int(pos), ref, alt))
    return muts


def apply_mutations(seq, muts):
    chars = list(seq)
    for pos, ref, alt in muts:
        observed = chars[pos - 1]
        if observed != ref:
            raise ValueError(f"Expected {ref} at {pos}, observed {observed}")
        chars[pos - 1] = alt
    return "".join(chars)


def windows_for_positions(seq_len, positions):
    seen = set()
    for position in positions:
        first_start = max(1, position - PEPTIDE_LEN + 1)
        last_start = min(position, seq_len - PEPTIDE_LEN + 1)
        for start in range(first_start, last_start + 1):
            if start in seen:
                continue
            seen.add(start)
            yield start, start + PEPTIDE_LEN - 1


def resolve_reference(protein, accession):
    seq = REFERENCE_SEQS[(protein, accession)]
    return seq() if callable(seq) else seq


def main():
    rows = []
    fasta_lines = []
    seq_num = 1
    with PANEL.open(newline="", encoding="utf-8") as f:
        for panel_row in csv.DictReader(f):
            if panel_row["analyze_peptide"] != "yes":
                continue
            protein = panel_row["protein"]
            accession = panel_row["reference_accession"]
            seq = resolve_reference(protein, accession)
            muts = parse_mutation_spec(panel_row["mutation_spec"])
            mutant_seq = apply_mutations(seq, muts)
            positions = [pos for pos, _, _ in muts]
            for state, protein_seq in [("WT", seq), ("MUT", mutant_seq)]:
                for start, end in windows_for_positions(len(seq), positions):
                    peptide = protein_seq[start - 1 : end]
                    peptide_id = f"{panel_row['variant_id']}|{state}|start{start}"
                    fasta_lines.extend([f">{peptide_id}", peptide])
                    rows.append(
                        {
                            "seq_num": seq_num,
                            "peptide_id": peptide_id,
                            "variant_id": panel_row["variant_id"],
                            "mutation_spec": panel_row["mutation_spec"],
                            "state": state,
                            "protein": protein,
                            "reference_accession": accession,
                            "positions": ";".join(str(p) for p in positions),
                            "window_start": start,
                            "window_end": end,
                            "peptide": peptide,
                            "evidence_tier": panel_row["evidence_tier"],
                            "evidence_role": panel_row["evidence_role"],
                        }
                    )
                    seq_num += 1

    OUT_META.parent.mkdir(parents=True, exist_ok=True)
    with OUT_META.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    OUT_FASTA.write_text("\n".join(fasta_lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} peptide records from {len(set(r['variant_id'] for r in rows))} variants")
    print(OUT_META)
    print(OUT_FASTA)


if __name__ == "__main__":
    main()
