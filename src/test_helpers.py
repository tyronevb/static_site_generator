import unittest
from helpers import extract_title

class TestHelpers(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello Hello Hello"
        title = extract_title(md)
        self.assertEqual(title,
                         "Hello Hello Hello")
        
    def test_extract_title_extra(self):
        md = """
        # Flight Report

        This is your captan speaking!

        We will be taking off **shortly**.
        """
        title = extract_title(md)
        self.assertEqual(title,
                         "Flight Report")
        
    def test_extract_no_title(self):
        md = "## Hello Hello Hello"
        with self.assertRaises(ValueError):
            extract_title(md)
        