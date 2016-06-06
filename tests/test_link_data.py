import unittest

from link_data import Rectangle, DeficientRectangle


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

    def test_number_of_rows_for_deficient_3_by_3_square(self):
        r = DeficientRectangle(3, 3, 4, [(0, 0)])
        rows = r.row_list()
        # 6 positions to place a t-tetromino
        # 4 monominos in each of the eight squares
        # 1 'magic monomino' in the (0,0) square
        self.assertEqual(len(rows), 6 + 4 * 8 + 1)


class TestDeficientSquare(unittest.TestCase):
    def test_the_number_of_rows_and_names_is_the_same(self):
        r = DeficientRectangle(3, 3, 4, [(0, 0)])
        rows = r.row_list()
        names = list(r.names())
        self.assertEqual(len(names), len(rows[0]))
        

class TestColumnNames(unittest.TestCase):
    def test_number_of_column_names_for_3_by_3_square(self):
        r = Rectangle(3, 3)
        names = list(r.names())
        self.assertEqual(len(names), 3*3 + 5)


class TestHeaderOutput(unittest.TestCase):
    def test_some_output_for_3_by_3_square(self):
        r = Rectangle(3, 3)
        self.assertIsNotNone(r.header_text())
