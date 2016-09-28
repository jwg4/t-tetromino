import unittest

from hypothesis import given
from hypothesis.strategies import integers

from generate import generate_tiling


class TestGenerate(unittest.TestCase):
    @given(integers(min=1), integers(min=1))
    def test_generate_tiling(self, x, y):
        tiling = generate_tiling(x, y)
        self.assertIsNotNone(tiling)
