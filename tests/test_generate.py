import unittest

from generate import generate_tiling


class TestGenerate(unittest.TestCase):
    def test_4_by_4(self):
        tiling = generate_tiling(4, 4)
        self.assertEqual(len(tiling[0]), 4)
        
