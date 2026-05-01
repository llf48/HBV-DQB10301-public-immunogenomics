# Supplementary Note

## Reproducibility Commands

```bash
python scripts/fetch_hbv_genbank_full_set.py --chunk-size 50
python scripts/extract_core_diversity_set.py --prefix core_full
python scripts/run_iedb_mhcii_batch.py --fasta data/processed/core_full_unique_15mer.fasta --meta data/processed/core_full_unique_15mer_metadata.csv --out results/tables/core_full_expanded_dq_netmhciipan_predictions.csv --method netmhciipan --allele-panel data/manual/hla_dq_panel_iteration3.csv --chunk-size 500 --resume-existing --retries 5 --timeout 240
python scripts/analyze_core_prediction_set.py --pred results/tables/core_full_expanded_dq_netmhciipan_predictions.csv --qc data/processed/core_full_record_qc.csv --out-prefix core_full_expanded_dq_netmhciipan --primary HLA-DQA1*03:01/DQB1*03:02
python scripts/run_iedb_mhcii_batch.py --fasta data/processed/core_full_unique_15mer.fasta --meta data/processed/core_full_unique_15mer_metadata.csv --out results/tables/core_full_iedb_recommended_predictions.csv --method recommended --chunk-size 500 --resume-existing --retries 5 --timeout 240
python scripts/analyze_core_prediction_set.py --pred results/tables/core_full_iedb_recommended_predictions.csv --qc data/processed/core_full_record_qc.csv --out-prefix core_full_iedb_recommended --primary HLA-DQA1*03:01/DQB1*03:02
python scripts/core_redundancy_bootstrap.py --qc data/processed/core_full_record_qc.csv --pred results/tables/core_full_expanded_dq_netmhciipan_predictions.csv --out-prefix core_full_expanded_dq --bootstrap 1000 --primary HLA-DQA1*03:01/DQB1*03:02
python scripts/core_stratified_sensitivity.py --qc data/processed/core_full_record_qc.csv --pred results/tables/core_full_expanded_dq_netmhciipan_predictions.csv --out-prefix core_full_expanded_dq --primary HLA-DQA1*03:01/DQB1*03:02 --min-country-records 20
python scripts/core_position_gap_analysis.py --pred results/tables/core_full_expanded_dq_netmhciipan_predictions.csv --out-prefix core_full_expanded_dq
python scripts/iedb_hbv_epitope_overlap.py --pred results/tables/core_full_expanded_dq_netmhciipan_predictions.csv --out-prefix core_full_expanded_dq
python scripts/iedb_hbv_epitope_overlap.py --pred results/tables/core_full_iedb_recommended_predictions.csv --out-prefix core_full_iedb_recommended
python scripts/generate_reference_proteome_15mers.py
python scripts/run_iedb_mhcii_batch.py --fasta data/processed/reference_proteome_15mer.fasta --meta data/processed/reference_proteome_15mer_metadata.csv --out results/tables/reference_proteome_expanded_dq_netmhciipan_predictions.csv --method netmhciipan --allele-panel data/manual/hla_dq_panel_iteration3.csv --chunk-size 500 --resume-existing --retries 5 --timeout 240
python scripts/summarize_reference_proteome_binding.py
python scripts/make_full_submission_figures.py
python scripts/build_submission_docx.py
```

## Main Supplementary Tables

- `data/processed/core_full_record_qc.csv`: GenBank record QC table.
- `data/processed/core_full_unique_15mer_metadata.csv`: unique public-core
  15-mer metadata and source occurrence mapping.
- `results/tables/core_full_expanded_dq_netmhciipan_predictions.csv`: expanded
  HLA-DQ NetMHCIIpan predictions.
- `results/tables/core_full_expanded_dq_netmhciipan_summary_by_allele.csv`:
  expanded panel summary by allele.
- `results/tables/core_full_expanded_dq_dedup_sensitivity.csv`:
  de-redundancy sensitivity results.
- `results/tables/core_full_expanded_dq_record_bootstrap.csv`: record-level
  bootstrap intervals.
- `results/tables/core_full_expanded_dq_stratified_sensitivity.csv`: genotype,
  region, country, and year-bin stratified rates.
- `results/tables/core_full_expanded_dq_position_gap_summary.csv`: position-level
  DQB1*03:02 versus DQB1*03:01 risk-pair presentation gaps.
- `data/processed/iedb_hbv_human_positive_tcell_epitopes.csv`: normalized IEDB
  human HBV positive T-cell epitopes.
- `results/tables/core_full_expanded_dq_iedb_epitope_overlap_summary_by_allele.csv`:
  overlap with known HBV core/nucleocapsid T-cell epitopes.
- `results/tables/reference_proteome_expanded_dq_summary_by_protein_allele.csv`:
  reference HBV proteome control summary.

## Submission Tables

- `submission/tables/table_1_dataset_qc_summary.csv`
- `submission/tables/table_2_full_hla_dq_binder_summary.csv`
- `submission/tables/supplementary_table_pairwise_fisher_tests.csv`
- `submission/tables/supplementary_table_dedup_sensitivity.csv`
- `submission/tables/supplementary_table_record_bootstrap.csv`
- `submission/tables/supplementary_table_stratified_sensitivity.csv`
- `submission/tables/supplementary_table_position_gap_summary.csv`
- `submission/tables/supplementary_table_iedb_epitope_overlap_summary.csv`
- `submission/tables/supplementary_table_method_sensitivity_recommended.csv`
- `submission/tables/supplementary_table_top_core_position_gaps.csv`
- `submission/tables/supplementary_table_reference_proteome_by_protein_allele.csv`
- `submission/tables/supplementary_table_region_counts.csv`

## Negative Pilot Summary

The original mutation-loss hypothesis was tested in exploratory analyses using
literature-derived HBx and PreS/S HCC-associated hotspots. HBx hotspots did not
produce DQB1*03:01-specific binder gain or loss. PreS/S S166L showed binding
spectrum remodeling rather than binder-to-non-binder loss. These findings are
reported as negative exploratory analyses and are not used as the main claim.

## Skill-Guided Workflow Notes

The project used the local life-science research instructions for PubMed,
NCBI/GenBank, IEDB, and IPD-oriented reasoning; GitHub-sourced biomedical
workflow skills for public-dataset intake, paper-to-pipeline conversion, and
results-to-figure organization; publication-chart guidance for figure export
and visual QA; and nature-style writing guidance for restrained claims,
negative-result handling, and limitations. The Seurat-oriented skill was
reviewed but not applied because no single-cell or spatial transcriptomic data
were part of this public HBV sequence analysis.
