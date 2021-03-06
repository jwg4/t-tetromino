import unittest

from hypothesis import given
from hypothesis.strategies import integers

from generate import generate_tiling


class TestGenerate(unittest.TestCase):
    @unittest.skip("Can't do arbitrary rectangles yet.")
    @given(integers(min_value=0), integers(min_value=0))
    def test_generate_tiling(self, x, y):
        tiling = generate_tiling(x, y)
        self.assertIsNotNone(tiling)

    @given(integers(min_value=0))
    def test_generate_square_tiling(self, x):
        tiling = generate_tiling(x, x)
        self.assertIsNotNone(tiling)
