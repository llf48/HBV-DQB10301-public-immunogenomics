import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from urllib import parse, request


PROJECT = Path(__file__).resolve().parents[1]
IEDB_TCELL = "https://query-api.iedb.org/tcell_search"
BINDER = 10.0


def get_json(url, params, timeout=120):
    query = parse.urlencode(params)
    req = request.Request(url + "?" + query)
    with request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def fetch_hbv_human_positive_tcell(limit=1000):
    rows = []
    offset = 0
    while True:
        batch = get_json(
            IEDB_TCELL,
            {
                "source_organism_iri": "eq.NCBITaxon:10407",
                "host_organism_iri": "eq.NCBITaxon:9606",
                "qualitative_measure": "eq.Positive",
                "order": "tcell_id.asc",
                "limit": limit,
                "offset": offset,
            },
        )
        if not batch:
            break
        rows.extend(batch)
        print("IEDB batch", offset, len(batch))
        if len(batch) < limit:
            break
        offset += limit
    return rows


def normalize_epitopes(raw_rows):
    rows = []
    seen = set()
    for item in raw_rows:
        antigen = item.get("curated_source_antigen") or {}
        sequence = (item.get("linear_sequence") or "").strip().upper()
        if not sequence or any(aa not in "ACDEFGHIKLMNPQRSTVWY" for aa in sequence):
            continue
        antigen_name = antigen.get("name") or ""
        parent_name = item.get("parent_source_antigen_name") or ""
        is_core = any(
            token in f"{antigen_name} {parent_name}".lower()
            for token in ["core", "nucleocapsid"]
        )
        key = (
            item.get("structure_id"),
            sequence,
            antigen_name,
            antigen.get("starting_position"),
            antigen.get("ending_position"),
            item.get("mhc_class") or "",
        )
        if key in seen:
            continue
        seen.add(key)
        rows.append(
            {
                "structure_id": item.get("structure_id", ""),
                "linear_sequence": sequence,
                "linear_sequence_length": len(sequence),
                "antigen_name": antigen_name,
                "parent_source_antigen_name": parent_name,
                "source_start": antigen.get("starting_position", ""),
                "source_end": antigen.get("ending_position", ""),
                "is_core_or_nucleocapsid": is_core,
                "mhc_class": item.get("mhc_class") or "",
                "mhc_allele_name": item.get("mhc_allele_name") or "",
                "pubmed_id": item.get("pubmed_id") or "",
                "reference_title": "; ".join(item.get("reference_titles") or []),
                "assay_names": item.get("assay_names") or "",
            }
        )
    return rows


def overlaps(peptide, epitope):
    peptide = peptide.upper()
    epitope = epitope.upper()
    return peptide in epitope or epitope in peptide


def summarize_overlap(pred_rows, epitope_rows):
    core_epitopes = [e for e in epitope_rows if str(e["is_core_or_nucleocapsid"]).lower() == "true"]
    core_class_ii = [e for e in core_epitopes if e["mhc_class"] == "II"]
    core_any_class = core_epitopes

    detail_rows = []
    by_allele = defaultdict(lambda: {"total": 0, "binder": 0, "overlap_any": 0, "overlap_ii": 0, "binder_overlap_any": 0, "binder_overlap_ii": 0})

    for row in pred_rows:
        allele = row["allele"]
        peptide = row["peptide"]
        rank = float(row["iedb_rank"])
        binder = rank < BINDER
        any_hits = [e for e in core_any_class if overlaps(peptide, e["linear_sequence"])]
        ii_hits = [e for e in core_class_ii if overlaps(peptide, e["linear_sequence"])]
        by_allele[allele]["total"] += 1
        by_allele[allele]["binder"] += int(binder)
        by_allele[allele]["overlap_any"] += int(bool(any_hits))
        by_allele[allele]["overlap_ii"] += int(bool(ii_hits))
        by_allele[allele]["binder_overlap_any"] += int(binder and bool(any_hits))
        by_allele[allele]["binder_overlap_ii"] += int(binder and bool(ii_hits))
        if any_hits or ii_hits:
            detail_rows.append(
                {
                    "allele": allele,
                    "allele_group": row["allele_group"],
                    "peptide": peptide,
                    "window_start": row["window_start"],
                    "window_end": row["window_end"],
                    "iedb_rank": row["iedb_rank"],
                    "binder_10": binder,
                    "overlaps_core_tcell_any_mhc": bool(any_hits),
                    "overlaps_core_tcell_mhc_ii": bool(ii_hits),
                    "matched_epitopes_any_mhc": ";".join(sorted({e["linear_sequence"] for e in any_hits})),
                    "matched_epitopes_mhc_ii": ";".join(sorted({e["linear_sequence"] for e in ii_hits})),
                }
            )

    summary_rows = []
    for allele, vals in sorted(by_allele.items()):
        binder = vals["binder"]
        summary_rows.append(
            {
                "allele": allele,
                "total_predicted_peptides": vals["total"],
                "binder_10": binder,
                "binder_10_rate": binder / vals["total"] if vals["total"] else 0,
                "overlap_core_tcell_any_mhc": vals["overlap_any"],
                "overlap_core_tcell_any_mhc_rate": vals["overlap_any"] / vals["total"] if vals["total"] else 0,
                "overlap_core_tcell_mhc_ii": vals["overlap_ii"],
                "overlap_core_tcell_mhc_ii_rate": vals["overlap_ii"] / vals["total"] if vals["total"] else 0,
                "binder_overlap_core_tcell_any_mhc": vals["binder_overlap_any"],
                "binder_overlap_core_tcell_any_mhc_rate_among_binders": vals["binder_overlap_any"] / binder if binder else 0,
                "binder_overlap_core_tcell_mhc_ii": vals["binder_overlap_ii"],
                "binder_overlap_core_tcell_mhc_ii_rate_among_binders": vals["binder_overlap_ii"] / binder if binder else 0,
            }
        )
    return summary_rows, detail_rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", default=str(PROJECT / "results" / "tables" / "core_large_expanded_dq_netmhciipan_predictions.csv"))
    parser.add_argument("--out-prefix", default="core_large")
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()

    raw_path = PROJECT / "data" / "raw" / "iedb_hbv_human_positive_tcell.json"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    if args.refresh or not raw_path.exists():
        raw_rows = fetch_hbv_human_positive_tcell()
        raw_path.write_text(json.dumps(raw_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        raw_rows = json.loads(raw_path.read_text(encoding="utf-8"))

    epitope_rows = normalize_epitopes(raw_rows)
    write_csv(PROJECT / "data" / "processed" / "iedb_hbv_human_positive_tcell_epitopes.csv", epitope_rows)

    pred_rows = list(csv.DictReader(Path(args.pred).open(newline="", encoding="utf-8")))
    summary_rows, detail_rows = summarize_overlap(pred_rows, epitope_rows)
    write_csv(PROJECT / "results" / "tables" / f"{args.out_prefix}_iedb_epitope_overlap_summary_by_allele.csv", summary_rows)
    write_csv(PROJECT / "results" / "tables" / f"{args.out_prefix}_iedb_epitope_overlap_detail.csv", detail_rows)

    print("Raw IEDB positive human HBV T-cell assay rows:", len(raw_rows))
    print("Unique linear epitopes:", len(epitope_rows))
    print("Core/nucleocapsid epitopes:", sum(str(e["is_core_or_nucleocapsid"]).lower() == "true" for e in epitope_rows))
    print("Core/nucleocapsid MHC-II epitopes:", sum(str(e["is_core_or_nucleocapsid"]).lower() == "true" and e["mhc_class"] == "II" for e in epitope_rows))
    for row in summary_rows:
        print(row["allele"], row["binder_overlap_core_tcell_any_mhc"], row["binder_overlap_core_tcell_mhc_ii"])


if __name__ == "__main__":
    main()
