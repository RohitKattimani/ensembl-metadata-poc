# Ensembl Genome Metadata Fetcher (PoC)

This is a proof-of-concept (PoC) for the project: **"Expand genome metadata in Ensembl with AI tools."**

## Overview
The goal of this module is to automate the extraction of missing genome metadata (like ploidy and chromosome counts as of now) by querying scientific literature associated with genome accessions.

### Key Features
* **Europe PMC Integration**: Queries the EBI's own literature database via REST API.
* **CLI Interface**: Designed for easy integration into Nextflow pipelines.
* **Extensible**: Structured to support future RAG (Retrieval-Augmented Generation) workflows with LLMs.

## Installation
1. Clone the repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
```bash
  python genome_lit_query.py --accession GCA_000355885.1
```

## Testing
```bash
python test_fetcher.py
