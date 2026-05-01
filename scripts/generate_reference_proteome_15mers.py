import csv
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
GB = PROJECT / "data" / "raw" / "NC_003977_2.gb"
OUT_FASTA = PROJECT / "data" / "processed" / "reference_proteome_15mer.fasta"
OUT_META = PROJECT / "data" / "processed" / "reference_proteome_15mer_metadata.csv"
PRODUCTS = {
    "polymerase": "polymerase",
    "large envelope protein": "large_envelope",
    "X protein": "x_protein",
    "capsid protein": "core_capsid",
}


def extract_products(text):
    products = {}
    for match in re.finditer(r"CDS\s+.*?(?=\n\s{5}\S|\nORIGIN|$)", text, flags=re.S):
        block = match.group(0)
        product_match = re.search(r'/product="([^"]+)"', block)
        translation_match = re.search(r'/translation="([^"]+)"', block, flags=re.S)
        if not product_match or not translation_match:
            continue
        product = product_match.group(1)
        if product not in PRODUCTS:
            continue
        seq = re.sub(r"\s+", "", translation_match.group(1))
        products[PRODUCTS[product]] = {"product": product, "sequence": seq}
    return products


def main():
    text = GB.read_text(encoding="utf-8")
    products = extract_products(text)
    rows = []
    fasta_lines = []
    seq_num = 1
    for protein, item in products.items():
        seq = item["sequence"]
        for start in range(1, len(seq) - 15 + 2):
            end = start + 14
            peptide = seq[start - 1 : end]
            row = {
                "seq_num": seq_num,
                "peptide_id": f"REF|{protein}|start{start}|{peptide}",
                "protein": protein,
                "product": item["product"],
                "window_start": start,
                "window_end": end,
                "peptide": peptide,
                "source_accessions": "NC_003977.2",
                "query_genotypes": "reference",
                "countries": "",
                "source_count": 1,
            }
            rows.append(row)
            fasta_lines.extend([f">{row['peptide_id']}", peptide])
            seq_num += 1

    OUT_META.parent.mkdir(parents=True, exist_ok=True)
    with OUT_META.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    OUT_FASTA.write_text("\n".join(fasta_lines) + "\n", encoding="utf-8")
    for protein, item in products.items():
        print(protein, len(item["sequence"]))
    print(len(rows), OUT_FASTA)


if __name__ == "__main__":
    main()
