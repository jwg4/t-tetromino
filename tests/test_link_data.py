import unittest

from link_data import Rectangle

class TestRowBuilding(unittest.TestCase):
    def test_rows_for_3_by_3_square(self):
        r = Rectangle(3, 3)
        rows = r.row_list()
        self.assertEqual(len(rows), 8 + 5 * 9)
