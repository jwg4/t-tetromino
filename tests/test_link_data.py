import unittest

from link_data import Rectangle

class TestRowBuilding(unittest.TestCase):
    def test_number_of_rows_for_3_by_3_square(self):
        r = Rectangle(3, 3)
        rows = r.row_list()
        self.assertEqual(len(rows), 8 + 5 * 9)

    def test_single_square_row_for_3_by_3_square(self):
        r = Rectangle(3, 3)
        rows = r.row_list()
        row1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        self.assertIn(row1, rows)
        
    def test_tetromino_row_for_3_by_3_square(self):
        r = Rectangle(3, 3)
        rows = r.row_list()
        row1 = [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertIn(row1, rows)

class TestColumnNames(unittest.TestCase):
    def test_number_of_column_names_for_3_by_3_square(self):
        r = Rectangle(3, 3)
        names = list(r.names())
        self.assertEqual(len(names), 3*3 + 5)

class TestHeaderOutput(unittest.TestCase):
    def test_some_output_for_3_by_3_square(self):
        r = Rectangle(3, 3)
        self.assertIsNotNone(r.header_text())
