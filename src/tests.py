import unittest
from src import converter


class TestConverter(unittest.TestCase):
    def test_headers(self):
        self.assertEqual(converter.Converter.convert("h1", "<h1>Test1</h1>"), "# Test1")
        #place for more h1 tests
        self.assertEqual(converter.Converter.convert("h2", "<h2>Test2</h2>"), "## Test2")
        # place for more h2 tests
        self.assertEqual(converter.Converter.convert("h3", "<h3>Test3</h3>"), "### Test3")
        # place for more h3 tests
        self.assertEqual(converter.Converter.convert("h4", "<h4>Test4</h4>"), "#### Test4")
        # place for more h4 tests
        self.assertEqual(converter.Converter.convert("h5", "<h5>Test5</h5>"), "##### Test5")
        # place for more h5 tests
        self.assertEqual(converter.Converter.convert("h6", "<h6>Test6</h6>"), "###### Test6")
        # place for more h6 tests



