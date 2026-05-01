import csv
import argparse
import time
from pathlib import Path
from urllib import parse, request


PROJECT = Path(__file__).resolve().parents[1]

IEDB_URL = "https://tools-cluster-interface.iedb.org/tools_api/mhcii/"
DEFAULT_ALLELES = [
    {"allele": "HLA-DQA1*06:01/DQB1*03:01", "group": "risk_DQB1_0301"},
    {"allele": "HLA-DQA1*05:08/DQB1*03:01", "group": "risk_DQB1_0301"},
    {"allele": "HLA-DQA1*03:01/DQB1*03:02", "group": "control_DQB1_0302"},
]


def post_iedb(sequence_text, allele, method, timeout):
    payload = parse.urlencode(
        {"method": method, "sequence_text": sequence_text, "allele": allele}
    ).encode("utf-8")
    req = request.Request(IEDB_URL, data=payload)
    with request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8")


def parse_tsv(text):
    lines = [line for line in text.splitlines() if line.strip()]
    return list(csv.DictReader(lines, delimiter="\t"))


def read_fasta_records(path):
    records = []
    header = None
    seq_lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(">"):
            if header is not None:
                records.append((header, "".join(seq_lines)))
            header = line[1:]
            seq_lines = []
        else:
            seq_lines.append(line.strip())
    if header is not None:
        records.append((header, "".join(seq_lines)))
    return records


def fasta_text(records):
    lines = []
    for header, seq in records:
        lines.extend([f">{header}", seq])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fasta",
        default=str(PROJECT / "data" / "processed" / "hbx_pilot_15mer.fasta"),
    )
    parser.add_argument(
        "--meta",
        default=str(PROJECT / "data" / "processed" / "hbx_pilot_15mer_metadata.csv"),
    )
    parser.add_argument(
        "--out",
        default=str(
            PROJECT / "results" / "tables" / "hbx_pilot_iedb_recommended_predictions.csv"
        ),
    )
    parser.add_argument("--method", default="recommended")
    parser.add_argument(
        "--allele-panel",
        default="",
        help="Optional CSV with columns allele,allele_group. Defaults to the three pilot DQ pairs.",
    )
    parser.add_argument("--chunk-size", type=int, default=0)
    parser.add_argument("--resume-existing", action="store_true")
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=180)
    args = parser.parse_args()

    fasta = Path(args.fasta)
    meta = Path(args.meta)
    out = Path(args.out)
    method = args.method
    if args.allele_panel:
        with Path(args.allele_panel).open(newline="", encoding="utf-8") as f:
            alleles = list(csv.DictReader(f))
    else:
        alleles = DEFAULT_ALLELES

    metadata = {}
    with meta.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            metadata[int(row["seq_num"])] = row

    out.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    fasta_records = read_fasta_records(fasta)
    if args.chunk_size and args.chunk_size > 0:
        chunks = [
            (start, fasta_records[start : start + args.chunk_size])
            for start in range(0, len(fasta_records), args.chunk_size)
        ]
    else:
        chunks = [(0, fasta_records)]

    for allele_info in alleles:
        allele = allele_info["allele"]
        allele_group = allele_info.get("allele_group") or allele_info.get("group", "")
        print(f"Running IEDB {method}: {allele}")
        for chunk_index, (start_index, records) in enumerate(chunks, start=1):
            print(f"  chunk {chunk_index}/{len(chunks)} ({len(records)} peptides)")
            raw_stem = out.stem.replace("_predictions", "")
            raw_path = PROJECT / "logs" / (
                f"{raw_stem}_{method}_{allele.replace('/', '_').replace('*', '').replace(':', '')}"
                f"_chunk{chunk_index}.tsv"
            )
            result_text = ""
            parsed = []
            if args.resume_existing and raw_path.exists():
                result_text = raw_path.read_text(encoding="utf-8")
                parsed = parse_tsv(result_text)
                if len(parsed) == len(records):
                    print(f"    using existing {raw_path.name}")
                else:
                    print(
                        f"    existing {raw_path.name} has {len(parsed)} rows; rerunning"
                    )
                    result_text = ""
                    parsed = []
            if not parsed:
                last_error = None
                for attempt in range(1, args.retries + 1):
                    try:
                        result_text = post_iedb(
                            fasta_text(records), allele, method, args.timeout
                        )
                        raw_path.write_text(result_text, encoding="utf-8")
                        parsed = parse_tsv(result_text)
                        if len(parsed) != len(records):
                            raise RuntimeError(
                                f"Expected {len(records)} prediction rows, got {len(parsed)}"
                            )
                        break
                    except Exception as exc:  # noqa: BLE001
                        last_error = exc
                        wait = min(60, 10 * attempt)
                        print(f"    attempt {attempt} failed: {exc}; waiting {wait}s")
                        time.sleep(wait)
                if not parsed:
                    raise RuntimeError(f"IEDB failed for {allele} chunk {chunk_index}: {last_error}")
            for result in parsed:
                local_seq_num = int(result["seq_num"])
                global_seq_num = start_index + local_seq_num
                merged = {
                    **metadata[global_seq_num],
                    "allele": allele,
                    "allele_group": allele_group,
                    "method": method,
                    "iedb_rank": result.get("rank", ""),
                    "iedb_score": result.get("score", ""),
                    "core_peptide": result.get("core_peptide", ""),
                }
                rows.append(merged)

    fieldnames = list(rows[0])
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} prediction rows")
    print(out)


if __name__ == "__main__":
    main()
