import unittest
import converter


class TestConverter(unittest.TestCase):
    def test_tags(self):
        self.assertEqual(converter.Converter.write_ordered_list("<ol><li>blabla</li><li>bleble</li></ol>"), "1. blabla\n2. bleble")

if __name__ == '__main__':
    unittest.main()