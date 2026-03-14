import unittest
from extracttitle import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.
"""
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")