import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
RAW = PROJECT / "data" / "raw"
OUT_RECORDS = PROJECT / "data" / "processed" / "core_large_record_qc.csv"
OUT_META = PROJECT / "data" / "processed" / "core_large_unique_15mer_metadata.csv"
OUT_FASTA = PROJECT / "data" / "processed" / "core_large_unique_15mer.fasta"
STANDARD_AA = set("ACDEFGHIKLMNPQRSTVWY")


def extract_records(path, genotype_label):
    text = path.read_text(encoding="utf-8", errors="replace")
    for record in text.split("\n//"):
        locus = re.search(r"LOCUS\s+(\S+)", record)
        if not locus:
            continue
        accession = locus.group(1)
        definition = re.search(r"DEFINITION\s+(.+?)(?:\nACCESSION|\nVERSION)", record, flags=re.S)
        definition = re.sub(r"\s+", " ", definition.group(1)).strip() if definition else ""
        country = re.search(r'/country="([^"]+)"', record)
        collection_date = re.search(r'/collection_date="([^"]+)"', record)
        notes = "; ".join(re.findall(r'/note="([^"]+)"', record, flags=re.S)[:5])
        all_text = " ".join([definition, notes]).lower()
        is_recombinant = "recombinant" in all_text

        core_seq = ""
        for match in re.finditer(r"CDS\s+.*?(?=\n\s{5}\S|\nORIGIN|$)", record, flags=re.S):
            block = match.group(0)
            if '/product="core protein"' not in block:
                continue
            translation = re.search(r'/translation="([^"]+)"', block, flags=re.S)
            if translation:
                core_seq = re.sub(r"\s+", "", translation.group(1))
                break

        standard_core = bool(core_seq) and set(core_seq).issubset(STANDARD_AA)
        yield {
            "accession": accession,
            "query_genotype": genotype_label,
            "definition": definition,
            "country": country.group(1) if country else "",
            "collection_date": collection_date.group(1) if collection_date else "",
            "notes": re.sub(r"\s+", " ", notes),
            "is_recombinant": is_recombinant,
            "core_seq": core_seq,
            "core_len": len(core_seq),
            "has_core": bool(core_seq),
            "standard_core_aa": standard_core,
            "passes_qc": bool(core_seq) and 170 <= len(core_seq) <= 190 and not is_recombinant and standard_core,
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit-per-genotype", type=int, default=120)
    args = parser.parse_args()

    records = []
    for genotype in ["B", "C"]:
        path = RAW / f"hbv_genotype_{genotype}_large_set.gb"
        count = 0
        for row in extract_records(path, genotype):
            if count >= args.limit_per_genotype:
                break
            records.append(row)
            count += 1

    OUT_RECORDS.parent.mkdir(parents=True, exist_ok=True)
    with OUT_RECORDS.open("w", newline="", encoding="utf-8") as f:
        fields = [k for k in records[0] if k != "core_seq"] + ["core_seq"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)

    peptides = {}
    for row in records:
        if not row["passes_qc"]:
            continue
        seq = row["core_seq"]
        for start in range(1, len(seq) - 15 + 2):
            end = start + 14
            peptide = seq[start - 1 : end]
            key = (peptide, start)
            if key not in peptides:
                peptides[key] = {
                    "seq_num": len(peptides) + 1,
                    "peptide_id": f"CORE_LARGE|start{start}|{peptide}",
                    "protein": "core_capsid",
                    "window_start": start,
                    "window_end": end,
                    "peptide": peptide,
                    "source_accessions": [],
                    "query_genotypes": [],
                    "countries": [],
                }
            peptides[key]["source_accessions"].append(row["accession"])
            peptides[key]["query_genotypes"].append(row["query_genotype"])
            if row["country"]:
                peptides[key]["countries"].append(row["country"])

    meta_rows = []
    fasta_lines = []
    for item in peptides.values():
        item["source_accessions"] = ";".join(sorted(set(item["source_accessions"])))
        item["query_genotypes"] = ";".join(sorted(set(item["query_genotypes"])))
        item["countries"] = ";".join(sorted(set(item["countries"])))
        item["source_count"] = len(item["source_accessions"].split(";"))
        meta_rows.append(item)
        fasta_lines.extend([f">{item['peptide_id']}", item["peptide"]])

    with OUT_META.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(meta_rows[0]))
        writer.writeheader()
        writer.writerows(meta_rows)
    OUT_FASTA.write_text("\n".join(fasta_lines) + "\n", encoding="utf-8")

    total = len(records)
    passed = sum(r["passes_qc"] for r in records)
    print(f"Records: {total}; passed QC: {passed}; unique core 15-mers: {len(meta_rows)}")
    print(OUT_RECORDS)
    print(OUT_META)
    print(OUT_FASTA)


if __name__ == "__main__":
    main()
