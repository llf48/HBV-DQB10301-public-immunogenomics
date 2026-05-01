from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from pathlib import Path
from urllib.parse import urlencode


PROJECT = Path(__file__).resolve().parents[1]
RAW = PROJECT / "data" / "raw"
LOGS = PROJECT / "logs"


def count_locus_records(text: str) -> int:
    return len(re.findall(r"(?m)^LOCUS\s+", text))


def curl_text(url: str, out_path: Path, timeout: int, attempts: int = 5) -> str:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "curl.exe",
        "-L",
        "--retry",
        "3",
        "--retry-all-errors",
        "--retry-delay",
        "2",
        "--connect-timeout",
        "30",
        "--max-time",
        str(timeout),
        url,
        "-o",
        str(out_path),
    ]
    last_error = None
    for attempt in range(1, attempts + 1):
        if out_path.exists():
            out_path.unlink()
        try:
            subprocess.run(cmd, check=True)
            return out_path.read_text(encoding="utf-8", errors="replace")
        except subprocess.CalledProcessError as exc:
            last_error = exc
            wait = min(30, 5 * attempt)
            print(f"curl attempt {attempt} failed for {out_path.name}; waiting {wait}s")
            time.sleep(wait)
    raise last_error


def term_for(genotype: str) -> str:
    return (
        '"Hepatitis B virus"[Organism] AND "complete genome"[Title] '
        f'AND "genotype {genotype}"[All Fields]'
    )


def esearch(genotype: str, retmax: int, timeout: int) -> list[str]:
    ids: list[str] = []
    retstart = 0
    count = None
    while True:
        params = urlencode(
            {
                "db": "nucleotide",
                "retmode": "json",
                "retmax": retmax,
                "retstart": retstart,
                "term": term_for(genotype),
            }
        )
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + params
        out = LOGS / f"ncbi_hbv_genotype_{genotype}_full_esearch_{retstart}.json"
        data = json.loads(curl_text(url, out, timeout))
        result = data["esearchresult"]
        if count is None:
            count = int(result["count"])
        batch = result["idlist"]
        ids.extend(batch)
        retstart += len(batch)
        if not batch or retstart >= count:
            break
        time.sleep(0.35)
    return ids


def efetch(ids: list[str], genotype: str, chunk_size: int, timeout: int) -> Path:
    paths: list[Path] = []
    for i in range(0, len(ids), chunk_size):
        chunk = ids[i : i + chunk_size]
        joined = ",".join(chunk)
        out = RAW / f"hbv_genotype_{genotype}_full_chunk_{i // chunk_size + 1}.gb"
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
            f"?db=nucleotide&id={joined}&rettype=gb&retmode=text"
        )
        expected = len(chunk)
        if out.exists():
            existing = out.read_text(encoding="utf-8", errors="replace")
            if count_locus_records(existing) == expected:
                print(f"Using existing genotype {genotype} chunk {i // chunk_size + 1} ({expected} records)")
                paths.append(out)
                continue
            print(
                f"Existing {out.name} has {count_locus_records(existing)} LOCUS records; refetching"
            )
        print(f"Fetching genotype {genotype} chunk {i // chunk_size + 1} ({expected} records)")
        text = curl_text(url, out, timeout)
        observed = count_locus_records(text)
        if observed != expected:
            raise RuntimeError(
                f"Expected {expected} LOCUS records for {out.name}, observed {observed}"
            )
        paths.append(out)
        time.sleep(0.35)
    combined = RAW / f"hbv_genotype_{genotype}_full_set.gb"
    combined.write_text(
        "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in paths),
        encoding="utf-8",
    )
    return combined


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--retmax", type=int, default=500)
    parser.add_argument("--chunk-size", type=int, default=100)
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    for genotype in ["B", "C"]:
        ids = esearch(genotype, retmax=args.retmax, timeout=args.timeout)
        unique_ids = list(dict.fromkeys(ids))
        print(f"Genotype {genotype}: {len(ids)} ids, {len(unique_ids)} unique ids")
        combined = efetch(unique_ids, genotype, args.chunk_size, args.timeout)
        print(combined)


if __name__ == "__main__":
    main()
