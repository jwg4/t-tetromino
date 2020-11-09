from hypothesis import given
from hypothesis.strategies import integers

from check import check_result


@given(integers(), integers())
def test_empty(x, y):
    assert check_result(x, y, [])
    

def test_tile_over_the_edge():
    assert not check_result(2, 2, [[(0, 0), (0, 1), (1, 1), (0, 2)]])