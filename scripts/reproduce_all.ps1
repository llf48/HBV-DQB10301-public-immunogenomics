param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"

& $Python -m pip install --upgrade -r requirements.txt

& $Python scripts\fetch_hbv_genbank_full_set.py --chunk-size 50
& $Python scripts\extract_core_diversity_set.py --prefix core_full
& $Python scripts\run_iedb_mhcii_batch.py --fasta data\processed\core_full_unique_15mer.fasta --meta data\processed\core_full_unique_15mer_metadata.csv --out results\tables\core_full_expanded_dq_netmhciipan_predictions.csv --method netmhciipan --allele-panel data\manual\hla_dq_panel_iteration3.csv --chunk-size 500 --resume-existing --retries 5 --timeout 240
& $Python scripts\analyze_core_prediction_set.py --pred results\tables\core_full_expanded_dq_netmhciipan_predictions.csv --qc data\processed\core_full_record_qc.csv --out-prefix core_full_expanded_dq_netmhciipan --primary HLA-DQA1*03:01/DQB1*03:02
& $Python scripts\run_iedb_mhcii_batch.py --fasta data\processed\core_full_unique_15mer.fasta --meta data\processed\core_full_unique_15mer_metadata.csv --out results\tables\core_full_iedb_recommended_predictions.csv --method recommended --chunk-size 500 --resume-existing --retries 5 --timeout 240
& $Python scripts\analyze_core_prediction_set.py --pred results\tables\core_full_iedb_recommended_predictions.csv --qc data\processed\core_full_record_qc.csv --out-prefix core_full_iedb_recommended --primary HLA-DQA1*03:01/DQB1*03:02
& $Python scripts\core_redundancy_bootstrap.py --qc data\processed\core_full_record_qc.csv --pred results\tables\core_full_expanded_dq_netmhciipan_predictions.csv --out-prefix core_full_expanded_dq --bootstrap 1000 --primary HLA-DQA1*03:01/DQB1*03:02
& $Python scripts\core_stratified_sensitivity.py --qc data\processed\core_full_record_qc.csv --pred results\tables\core_full_expanded_dq_netmhciipan_predictions.csv --out-prefix core_full_expanded_dq --primary HLA-DQA1*03:01/DQB1*03:02 --min-country-records 20
& $Python scripts\core_position_gap_analysis.py --pred results\tables\core_full_expanded_dq_netmhciipan_predictions.csv --out-prefix core_full_expanded_dq
& $Python scripts\iedb_hbv_epitope_overlap.py --pred results\tables\core_full_expanded_dq_netmhciipan_predictions.csv --out-prefix core_full_expanded_dq
& $Python scripts\iedb_hbv_epitope_overlap.py --pred results\tables\core_full_iedb_recommended_predictions.csv --out-prefix core_full_iedb_recommended
& $Python scripts\generate_reference_proteome_15mers.py
& $Python scripts\run_iedb_mhcii_batch.py --fasta data\processed\reference_proteome_15mer.fasta --meta data\processed\reference_proteome_15mer_metadata.csv --out results\tables\reference_proteome_expanded_dq_netmhciipan_predictions.csv --method netmhciipan --allele-panel data\manual\hla_dq_panel_iteration3.csv --chunk-size 500 --resume-existing --retries 5 --timeout 240
& $Python scripts\summarize_reference_proteome_binding.py
& $Python scripts\make_full_submission_figures.py
& $Python scripts\make_graphical_abstract.py
& $Python scripts\build_viruses_reference_library.py
& $Python scripts\update_viruses_citations_70.py
& $Python scripts\build_submission_docx.py
& $Python scripts\build_viruses_submission_docx.py
