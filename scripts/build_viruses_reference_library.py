from __future__ import annotations

import csv
import shutil
import subprocess
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PMID_TABLE = ROOT / "data" / "manual" / "viruses_reference_pmids_70.csv"
OUT_DIR = ROOT / "docs" / "references"
SUBMISSION_OUT = ROOT / "submission_viruses" / "references_70.md"


def curl_text(url: str) -> str:
    curl = shutil.which("curl") or shutil.which("curl.exe")
    if not curl:
        raise RuntimeError("curl is required to retrieve PubMed metadata")
    result = subprocess.run(
        [curl, "-sL", url],
        capture_output=True,
        check=True,
    )
    return result.stdout.decode("utf-8", errors="replace")


def text_content(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return "".join(node.itertext()).strip()


def pub_year(article: ET.Element) -> str:
    for path in [
        ".//Article/Journal/JournalIssue/PubDate/Year",
        ".//PubmedData/History/PubMedPubDate[@PubStatus='pubmed']/Year",
        ".//PubmedData/History/PubMedPubDate[@PubStatus='entrez']/Year",
    ]:
        value = text_content(article.find(path))
        if value:
            return value
    medline = text_content(article.find(".//Article/Journal/JournalIssue/PubDate/MedlineDate"))
    return medline[:4] if medline else ""


def article_doi(article: ET.Element) -> str:
    for node in article.findall(".//ArticleId"):
        if node.attrib.get("IdType", "").lower() == "doi":
            return text_content(node)
    for node in article.findall(".//ELocationID"):
        if node.attrib.get("EIdType", "").lower() == "doi":
            return text_content(node)
    return ""


def authors(article: ET.Element, limit: int = 6) -> str:
    names: list[str] = []
    for author in article.findall(".//AuthorList/Author"):
        collective = text_content(author.find("CollectiveName"))
        if collective:
            names.append(collective)
            continue
        last = text_content(author.find("LastName"))
        initials = text_content(author.find("Initials"))
        if last:
            names.append(f"{last} {initials}".strip())
    if not names:
        return "No authors listed"
    if len(names) > limit:
        return ", ".join(names[:limit]) + ", et al."
    return ", ".join(names)


def pages(article: ET.Element) -> str:
    medline = text_content(article.find(".//Article/Pagination/MedlinePgn"))
    if medline:
        return medline
    for node in article.findall(".//ELocationID"):
        if node.attrib.get("EIdType", "").lower() not in {"doi"}:
            value = text_content(node)
            if value:
                return value
    return ""


def parse_article(article: ET.Element) -> dict[str, str]:
    pmid = text_content(article.find(".//MedlineCitation/PMID"))
    title = text_content(article.find(".//Article/ArticleTitle"))
    journal = text_content(article.find(".//Article/Journal/ISOAbbreviation"))
    if not journal:
        journal = text_content(article.find(".//Article/Journal/Title"))
    volume = text_content(article.find(".//Article/Journal/JournalIssue/Volume"))
    issue = text_content(article.find(".//Article/Journal/JournalIssue/Issue"))
    year = pub_year(article)
    pgn = pages(article)
    doi = article_doi(article)
    return {
        "pmid": pmid,
        "authors": authors(article),
        "title": title.rstrip("."),
        "journal": journal,
        "year": year,
        "volume": volume,
        "issue": issue,
        "pages": pgn,
        "doi": doi,
    }


def format_reference(meta: dict[str, str], include_pmid: bool = False) -> str:
    volume_issue = meta["volume"]
    if meta["issue"]:
        volume_issue += f"({meta['issue']})"
    locator = ""
    if volume_issue and meta["pages"]:
        locator = f";{volume_issue}:{meta['pages']}"
    elif volume_issue:
        locator = f";{volume_issue}"
    elif meta["pages"]:
        locator = f":{meta['pages']}"

    doi = f" doi:{meta['doi']}." if meta["doi"] else ""
    pmid = f" PMID:{meta['pmid']}." if include_pmid else ""
    author_text = meta["authors"]
    author_suffix = "" if author_text.endswith(".") else "."
    return (
        f"{author_text}{author_suffix} {meta['title']}. {meta['journal']}. "
        f"{meta['year']}{locator}.{doi}{pmid}"
    ).strip()


def main() -> None:
    rows = list(csv.DictReader(PMID_TABLE.open(encoding="utf-8")))
    pmids = [row["pmid"] for row in rows]
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"}
    )
    xml_text = curl_text(url)
    time.sleep(0.34)
    root = ET.fromstring(xml_text)
    articles = {parse_article(article)["pmid"]: parse_article(article) for article in root.findall(".//PubmedArticle")}

    missing = [pmid for pmid in pmids if pmid not in articles]
    if missing:
        raise RuntimeError(f"Missing PubMed records: {', '.join(missing)}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    csv_path = OUT_DIR / "viruses_reference_library_70.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = [
            "ref_number",
            "pmid",
            "section",
            "rationale",
            "authors",
            "title",
            "journal",
            "year",
            "volume",
            "issue",
            "pages",
            "doi",
            "formatted_reference",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            meta = articles[row["pmid"]]
            writer.writerow(
                {
                    **row,
                    **meta,
                    "formatted_reference": format_reference(meta, include_pmid=True),
                }
            )

    md_lines = [
        "# Viruses Reference Library: 70 PubMed-Verified References",
        "",
        "Generated from NCBI PubMed E-utilities on 2026-05-01.",
        "",
        "Each reference is tied to a manuscript evidence role in",
        "`data/manual/viruses_reference_pmids_70.csv`.",
        "",
        "## References",
        "",
    ]
    for row in rows:
        meta = articles[row["pmid"]]
        md_lines.append(f"{row['ref_number']}. {format_reference(meta, include_pmid=True)}")

    md_path = OUT_DIR / "viruses_reference_library_70.md"
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    submission_lines = ["## References", ""]
    for row in rows:
        meta = articles[row["pmid"]]
        submission_lines.append(f"{row['ref_number']}. {format_reference(meta, include_pmid=False)}")
    SUBMISSION_OUT.write_text("\n".join(submission_lines) + "\n", encoding="utf-8")

    print(csv_path)
    print(md_path)
    print(SUBMISSION_OUT)


if __name__ == "__main__":
    main()
