import unittest
from genome_lit_query import GenomeMetadataFetcher

class TestGenomeFetcher(unittest.TestCase):
    def setUp(self):
        self.fetcher = GenomeMetadataFetcher()

    def test_api_response_structure(self):
        """For testing if the Europe PMC API returns the expected keys for a known accession"""
        # This is a real accession for a wheat genome
        result = self.fetcher.fetch_paper_by_accession("GCA_000355885.1")
        
        if result:
            self.assertIn('title', result)
            self.assertIn('abstractText', result)
        else:
            self.skipTest("API might be down or accession not found.")

    def test_mock_ai_logic(self):
        """This basically ensures the mock AI extraction returns a dictionary with expected keys"""
        mock_text = "The organism is a diploid with 20 chromosomes."
        extracted = self.fetcher.extract_metadata_mock_ai(mock_text)
        
        self.assertIsInstance(extracted, dict)
        self.assertEqual(extracted['ploidy'], "Detected via AI (Mock)")

if __name__ == '__main__':
    unittest.main()