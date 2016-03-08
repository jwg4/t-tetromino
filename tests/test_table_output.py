import unittest

from table_output import table_to_header_file

class TestTableToHeader(unittest.TestCase):
    def test_basic_table_converted_to_header(self):
        self.maxDiff = None
        table = [
            [ 0, 0, 1, 0, 1, 1, 0 ],
            [ 1, 0, 0, 1, 0, 0, 1 ],
            [ 0, 1, 1, 0, 0, 1, 0 ],
            [ 1, 0, 0, 1, 0, 0, 0 ],
            [ 0, 1, 0, 0, 0, 0, 1 ],
            [ 0, 0, 0, 1, 1, 0, 1 ],
        ]
        names = [ "1", "2", "3", "4", "5", "6", "7" ]
        f = open('tests/files/table.h', 'r')
        expected = f.read()
        self.assertMultiLineEqual(table_to_header_file(table, names), expected)
