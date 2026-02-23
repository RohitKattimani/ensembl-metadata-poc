import requests
import argparse
import json
from typing import Dict, Optional, Any

class GenomeMetadataFetcher:
    """
    A standalone module to fetch genome-related literature 
    from Europe PMC and prepare it for AI extraction.
    """
    BASE_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

    def __init__(self, format: str = "json"):
        self.format = format

    def fetch_paper_by_accession(self, accession: str) -> Optional[Dict[str, Any]]:
        """
        Queries Europe PMC for a specific genome assembly accession.
        """
        # We search specifically for the accession in the text/metadata
        query = f'"{accession}"'
        params = {
            "query": query,
            "format": self.format,
            "resultType": "core"  # 'core' gives us the abstract
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        results = data.get("resultList", {}).get("result", [])
        
        return results[0] if results else None

    def extract_metadata_mock_ai(self, text: str) -> Dict[str, str]:
        """
        Mock function representing where an LLM (GPT, Llama, etc.) 
        would parse the abstract for specific fields.
        """
        # In the scaled pipeline, this is where LangChain/OpenAI logic goes
        return {
            "ploidy": "Detected via AI (Mock)",
            "chromosome_count": "Detected via AI (Mock)",
            "extraction_source": "Abstract Analysis"
        }

def main():
    parser = argparse.ArgumentParser(description="Fetch Genome Metadata from Literature")
    parser.add_argument("--accession", required=True, help="Assembly Accession (e.g., GCA_000355885.1)")
    args = parser.parse_args()

    fetcher = GenomeMetadataFetcher()
    print(f"[*] Searching Europe PMC for {args.accession}...")
    
    result = fetcher.fetch_paper_by_accession(args.accession)

    if result:
        title = result.get("title")
        abstract = result.get("abstractText", "No abstract available.")
        pmcid = result.get("pmcid", "N/A")
        
        print(f"[+] Found Paper: {title} (PMCID: {pmcid})")
        
        # Simulate AI Extraction
        metadata = fetcher.extract_metadata_mock_ai(abstract)
        
        final_output = {
            "accession": args.accession,
            "paper_title": title,
            "pmcid": pmcid,
            "extracted_metadata": metadata
        }
        
        print("\n[!] Structured Output:")
        print(json.dumps(final_output, indent=4))
    else:
        print("[-] No matching papers found for this accession.")

if __name__ == "__main__":
    main()