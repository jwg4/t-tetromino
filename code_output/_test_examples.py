import unittest

from generate import generate_tiling


class TestExamples(unittest.TestCase):
    def try_to_generate_tiling(self, x, y):
        tiling = generate_tiling(x, y)
        self.assertIsNotNone(tiling)

    def test_1_1(self):
        self.try_to_generate_tiling(1, 1)
