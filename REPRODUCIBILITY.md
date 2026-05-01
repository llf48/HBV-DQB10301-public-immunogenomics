# Reproducibility Guide

## Environment

Create a Python 3.11 environment using either:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

or:

```bash
conda env create -f environment.yml
conda activate hbv-dq3-pli-public-immunogenomics
```

## One-step Reproduction

Windows PowerShell:

```powershell
.\scripts\reproduce_all.ps1
```

Bash:

```bash
bash scripts/reproduce_all.sh
```

The full workflow downloads public NCBI records and calls public IEDB services.
Runtime depends on network speed and IEDB API response time. Existing IEDB raw
logs are reused when `--resume-existing` is active.

## Fast Rebuild From Existing Outputs

To regenerate figures, DOCX files, and submission package from already produced
tables:

```bash
python scripts/make_full_submission_figures.py
python scripts/make_graphical_abstract.py
python scripts/build_submission_docx.py
```

## Main Outputs

- `results/tables/core_full_expanded_dq_netmhciipan_predictions.csv`
- `results/tables/core_full_expanded_dq_netmhciipan_summary_by_allele.csv`
- `results/tables/core_full_expanded_dq_dedup_sensitivity.csv`
- `results/tables/core_full_expanded_dq_record_bootstrap.csv`
- `results/tables/core_full_expanded_dq_stratified_sensitivity.csv`
- `results/tables/core_full_expanded_dq_position_gap_summary.csv`
- `results/figures/figure_1_full_expanded_dq_binder_rates.png`
- `results/figures/graphical_abstract_workflow.png`
- `submission_viruses/`
