# Data Sources

Date: 2026-05-01

## Viral Sequences

Public complete-genome HBV genotype B/C records were retrieved from NCBI
Nucleotide/GenBank through E-utilities.

The repository does not track the large raw GenBank and IEDB download caches.
They are public records and can be regenerated with the scripts listed below.
Processed metadata, summary tables, figures, and manuscript-facing outputs are
tracked for transparent review. Large per-peptide prediction CSV files are also
regenerable and are intentionally omitted from Git tracking.

Queries used by `scripts/fetch_hbv_genbank_full_set.py`:

```text
"Hepatitis B virus"[Organism] AND "complete genome"[Title] AND "genotype B"[All Fields]
"Hepatitis B virus"[Organism] AND "complete genome"[Title] AND "genotype C"[All Fields]
```

The final retrieval returned 3784 candidate records. The final QC-passed
analysis set contained 1576 genotype-labeled core records and 1538 unique
accession identifiers.

## MHC-II Prediction

MHC-II peptide binding predictions were generated through the public IEDB MHC-II
prediction API. The main method was NetMHCIIpan. IEDB recommended predictions
were used as method sensitivity for the primary three HLA-DQ heterodimers.

## T-cell Epitope Data

Positive human HBV T-cell assay records were retrieved from the IEDB query API
with:

```text
source_organism_iri = NCBITaxon:10407
host_organism_iri = NCBITaxon:9606
qualitative_measure = Positive
```

The retrieved records were normalized to unique linear epitope sequences with
curated antigen labels, source positions, MHC class, PubMed identifiers, and
assay metadata.

## Reference Proteome

Reference HBV genome `NC_003977.2` was used for the reference-proteome control
across polymerase, large envelope, X protein, and core/capsid.

## Data Use Notes

All records are public database records. No individual-level human participant
data were accessed. Public database metadata may be incomplete or biased; the
analysis should not be interpreted as a population-prevalence estimate.
