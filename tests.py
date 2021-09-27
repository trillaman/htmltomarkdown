import unittest
from converter import *

class TestConverter(unittest.TestCase):
    converter = Converter()
    def test_headers(self):
        self.assertAlmostEqual(self.converter.convert("<h1>Test1</h1>"), "# Test1")
        #place for more h1 tests
        self.assertAlmostEqual(self.converter.convert("<h2>Test2</h2>"), "## Test2")
        # place for more h2 tests
        self.assertAlmostEqual(self.converter.convert("<h3>Test3</h3>"), "### Test3")
        # place for more h3 tests
        self.assertAlmostEqual(self.converter.convert("<h4>Test4</h4>"), "#### Test4")
        # place for more h4 tests
        self.assertAlmostEqual(self.converter.convert("<h5>Test5</h5>"), "##### Test5")
        # place for more h5 tests
        self.assertAlmostEqual(self.converter.convert("<h1>Test6</h1>"), "###### Test6")
        # place for more h6 tests



