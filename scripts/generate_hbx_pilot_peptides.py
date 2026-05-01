import csv
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
OUT_META = PROJECT / "data" / "processed" / "hbx_pilot_15mer_metadata.csv"
OUT_FASTA = PROJECT / "data" / "processed" / "hbx_pilot_15mer.fasta"

HBX_REF = (
    "MAARLCCQLDPARDVLCLRPVGAESCGRPFSGSLGTLSSPSPSAVPTDHGAHLSLRGLPVCAFSSAGPCALRFTSARR"
    "METTVNAHQILPKVLHKRTLGLSAMSTTDLEAYFKDCLFKDWEELGEEIRLKVFVLGGCRHKLVCAPAPCNFFTSA"
)

MUTATIONS = [
    {"mutation_id": "HBX_H94Y_C1653T", "position": 94, "ref": "H", "alts": ["Y"]},
    {"mutation_id": "HBX_I127T_T1753C", "position": 127, "ref": "I", "alts": ["T"]},
    {"mutation_id": "HBX_I127N_T1753A", "position": 127, "ref": "I", "alts": ["N"]},
    {"mutation_id": "HBX_I127S_T1753G", "position": 127, "ref": "I", "alts": ["S"]},
    {"mutation_id": "HBX_K130M_A1762T", "position": 130, "ref": "K", "alts": ["M"]},
    {"mutation_id": "HBX_V131I_G1764A", "position": 131, "ref": "V", "alts": ["I"]},
]


def windows_containing(position, peptide_len=15):
    seq_len = len(HBX_REF)
    first_start = max(1, position - peptide_len + 1)
    last_start = min(position, seq_len - peptide_len + 1)
    for start in range(first_start, last_start + 1):
        end = start + peptide_len - 1
        yield start, end


def mutate(seq, position, alt):
    zero = position - 1
    return seq[:zero] + alt + seq[zero + 1 :]


def main():
    rows = []
    fasta_lines = []
    seq_num = 1

    for spec in MUTATIONS:
        position = spec["position"]
        observed_ref = HBX_REF[position - 1]
        if observed_ref != spec["ref"]:
            raise ValueError(
                f"{spec['mutation_id']} expected {spec['ref']} at {position}, observed {observed_ref}"
            )

        for alt in spec["alts"]:
            mutant_seq = mutate(HBX_REF, position, alt)
            variant_id = f"{spec['mutation_id']}_{spec['ref']}{position}{alt}"
            for state, seq in [("WT", HBX_REF), ("MUT", mutant_seq)]:
                for start, end in windows_containing(position):
                    peptide = seq[start - 1 : end]
                    peptide_id = f"{variant_id}|{state}|start{start}|pos{position}"
                    fasta_lines.extend([f">{peptide_id}", peptide])
                    rows.append(
                        {
                            "seq_num": seq_num,
                            "peptide_id": peptide_id,
                            "mutation_id": spec["mutation_id"],
                            "variant_id": variant_id,
                            "state": state,
                            "protein": "HBx",
                            "position": position,
                            "ref": spec["ref"],
                            "alt": alt,
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
    print(f"Wrote {len(rows)} peptide records")
    print(OUT_META)
    print(OUT_FASTA)


if __name__ == "__main__":
    main()

