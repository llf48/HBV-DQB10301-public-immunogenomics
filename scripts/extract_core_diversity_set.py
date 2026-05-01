from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
RAW = PROJECT / "data" / "raw"
PROCESSED = PROJECT / "data" / "processed"
STANDARD_AA = set("ACDEFGHIKLMNPQRSTVWY")

REGION_MAP = {
    "China": "East Asia",
    "Hong Kong": "East Asia",
    "Taiwan": "East Asia",
    "Japan": "East Asia",
    "Korea": "East Asia",
    "South Korea": "East Asia",
    "Viet Nam": "Southeast Asia",
    "Vietnam": "Southeast Asia",
    "Thailand": "Southeast Asia",
    "Myanmar": "Southeast Asia",
    "Cambodia": "Southeast Asia",
    "Laos": "Southeast Asia",
    "Malaysia": "Southeast Asia",
    "Indonesia": "Southeast Asia",
    "Philippines": "Southeast Asia",
    "Singapore": "Southeast Asia",
    "India": "South Asia",
    "Bangladesh": "South Asia",
    "Pakistan": "South Asia",
    "Nepal": "South Asia",
    "Mongolia": "Central/East Asia",
    "Russia": "Europe/Central Asia",
    "United States": "North America",
    "USA": "North America",
    "Canada": "North America",
    "Brazil": "Latin America",
    "Mexico": "Latin America",
    "Australia": "Oceania",
}


def normalize_country(value: str) -> str:
    if not value:
        return ""
    first = value.split(":")[0].strip()
    first = first.replace("Republic of Korea", "South Korea")
    first = first.replace("Korea, South", "South Korea")
    first = first.replace("VietNam", "Vietnam")
    first = first.replace("USA", "United States")
    return first


def region_for(country: str) -> str:
    if not country:
        return "Unknown"
    return REGION_MAP.get(country, "Other/Unmapped")


def parse_year(collection_date: str) -> str:
    if not collection_date:
        return ""
    match = re.search(r"(19|20)\d{2}", collection_date)
    return match.group(0) if match else ""


def extract_records(path: Path, genotype_label: str):
    text = path.read_text(encoding="utf-8", errors="replace")
    for record in text.split("\n//"):
        locus = re.search(r"LOCUS\s+(\S+)", record)
        if not locus:
            continue
        accession = locus.group(1)
        definition = re.search(r"DEFINITION\s+(.+?)(?:\nACCESSION|\nVERSION)", record, flags=re.S)
        definition = re.sub(r"\s+", " ", definition.group(1)).strip() if definition else ""
        country_raw = re.search(r'/(?:country|geo_loc_name)="([^"]+)"', record)
        collection_raw = re.search(r'/collection_date="([^"]+)"', record)
        isolate = re.search(r'/isolate="([^"]+)"', record)
        host = re.search(r'/host="([^"]+)"', record)
        notes = "; ".join(re.findall(r'/note="([^"]+)"', record, flags=re.S)[:8])
        all_text = " ".join([definition, notes]).lower()
        is_recombinant = "recombinant" in all_text
        country = normalize_country(country_raw.group(1) if country_raw else "")
        collection_date = collection_raw.group(1) if collection_raw else ""

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
            "country_raw": country_raw.group(1) if country_raw else "",
            "country": country,
            "region": region_for(country),
            "collection_date": collection_date,
            "collection_year": parse_year(collection_date),
            "isolate": isolate.group(1) if isolate else "",
            "host": host.group(1) if host else "",
            "notes": re.sub(r"\s+", " ", notes),
            "is_recombinant": is_recombinant,
            "core_seq": core_seq,
            "core_len": len(core_seq),
            "has_core": bool(core_seq),
            "standard_core_aa": standard_core,
            "passes_qc": bool(core_seq)
            and 170 <= len(core_seq) <= 190
            and not is_recombinant
            and standard_core,
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", default="core_full")
    parser.add_argument("--input-suffix", default="full_set")
    parser.add_argument("--limit-per-genotype", type=int, default=0)
    args = parser.parse_args()

    records = []
    seen_accessions = set()
    for genotype in ["B", "C"]:
        path = RAW / f"hbv_genotype_{genotype}_{args.input_suffix}.gb"
        count = 0
        for row in extract_records(path, genotype):
            if args.limit_per_genotype and count >= args.limit_per_genotype:
                break
            count += 1
            key = (row["accession"], genotype)
            if key in seen_accessions:
                continue
            seen_accessions.add(key)
            records.append(row)

    if not records:
        raise RuntimeError("No records parsed")

    out_records = PROCESSED / f"{args.prefix}_record_qc.csv"
    out_meta = PROCESSED / f"{args.prefix}_unique_15mer_metadata.csv"
    out_fasta = PROCESSED / f"{args.prefix}_unique_15mer.fasta"

    out_records.parent.mkdir(parents=True, exist_ok=True)
    fields = [k for k in records[0] if k != "core_seq"] + ["core_seq"]
    with out_records.open("w", newline="", encoding="utf-8") as f:
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
                    "peptide_id": f"{args.prefix.upper()}|start{start}|{peptide}",
                    "protein": "core_capsid",
                    "window_start": start,
                    "window_end": end,
                    "peptide": peptide,
                    "source_accessions": [],
                    "query_genotypes": [],
                    "countries": [],
                    "regions": [],
                    "collection_years": [],
                }
            item = peptides[key]
            item["source_accessions"].append(row["accession"])
            item["query_genotypes"].append(row["query_genotype"])
            if row["country"]:
                item["countries"].append(row["country"])
            if row["region"]:
                item["regions"].append(row["region"])
            if row["collection_year"]:
                item["collection_years"].append(row["collection_year"])

    meta_rows = []
    fasta_lines = []
    for item in peptides.values():
        for key in ["source_accessions", "query_genotypes", "countries", "regions", "collection_years"]:
            item[key] = ";".join(sorted(set(item[key])))
        item["source_count"] = len(item["source_accessions"].split(";")) if item["source_accessions"] else 0
        meta_rows.append(item)
        fasta_lines.extend([f">{item['peptide_id']}", item["peptide"]])

    with out_meta.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(meta_rows[0]))
        writer.writeheader()
        writer.writerows(meta_rows)
    out_fasta.write_text("\n".join(fasta_lines) + "\n", encoding="utf-8")

    total = len(records)
    passed = sum(str(r["passes_qc"]).lower() == "true" for r in records)
    print(f"Records: {total}; passed QC: {passed}; unique core 15-mers: {len(meta_rows)}")
    print(out_records)
    print(out_meta)
    print(out_fasta)


if __name__ == "__main__":
    main()
