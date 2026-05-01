import json
import argparse
import subprocess
from pathlib import Path
from urllib.parse import urlencode


PROJECT = Path(__file__).resolve().parents[1]
RAW = PROJECT / "data" / "raw"
LOGS = PROJECT / "logs"


def curl_text(url, out_path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["curl.exe", "-L", "--max-time", "90", url, "-o", str(out_path)]
    subprocess.run(cmd, check=True)
    return out_path.read_text(encoding="utf-8")


def esearch(genotype, retmax=150):
    term = (
        '"Hepatitis B virus"[Organism] AND "complete genome"[Title] '
        f'AND "genotype {genotype}"[All Fields]'
    )
    params = urlencode(
        {"db": "nucleotide", "retmode": "json", "retmax": retmax, "term": term}
    )
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + params
    text = curl_text(url, LOGS / f"ncbi_hbv_genotype_{genotype}_esearch.json")
    data = json.loads(text)
    return data["esearchresult"]["idlist"]


def efetch(ids, genotype, chunk_size=50):
    paths = []
    for i in range(0, len(ids), chunk_size):
        chunk = ids[i : i + chunk_size]
        joined = ",".join(chunk)
        out = RAW / f"hbv_genotype_{genotype}_chunk_{i // chunk_size + 1}.gb"
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
            f"?db=nucleotide&id={joined}&rettype=gb&retmode=text"
        )
        curl_text(url, out)
        paths.append(out)
    combined = RAW / f"hbv_genotype_{genotype}_large_set.gb"
    combined.write_text("\n".join(p.read_text(encoding="utf-8") for p in paths), encoding="utf-8")
    return combined


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--retmax", type=int, default=150)
    parser.add_argument("--chunk-size", type=int, default=50)
    args = parser.parse_args()

    for genotype in ["B", "C"]:
        ids = esearch(genotype, retmax=args.retmax)
        print(f"Genotype {genotype}: {len(ids)} ids")
        combined = efetch(ids, genotype, chunk_size=args.chunk_size)
        print(combined)


if __name__ == "__main__":
    main()
