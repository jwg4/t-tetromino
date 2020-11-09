from hypothesis import given
from hypothesis.strategies import integers

from check import check_result, is_t_tetromino


@given(integers(), integers())
def test_empty(x, y):
    assert check_result(x, y, [])
    

def test_looks_fine():
    assert check_result(2, 3, [[(0, 0), (0, 1), (1, 1), (0, 2)]])


def test_tile_over_the_edge():
    assert not check_result(2, 2, [[(0, 0), (0, 1), (1, 1), (0, 2)]])
    

def test_tile_over_the_other_edge():
    assert not check_result(2, 2, [[(0, 0), (0, 1), (1, 1), (-1, 1)]])
    

def test_overlapping():
    assert not check_result(3, 2, [[(0, 0), (1, 0), (1, 1), (2, 0)], [(0, 1), (1, 1), (1, 0), (2, 1)]])


def test_non_t_tetromino():
    assert not check_result(2, 2, [[(0, 0), (0, 1), (1, 1), (1, 0)]])


def test_not_even_tetromino():
    assert not check_result(2, 2, [[(0, 0), (0, 1), (1, 1)]])
    assert not check_result(3, 3, [[(0, 0), (0, 1), (1, 1), (0, 2), (-1, 1)]])
    assert not check_result(3, 3, [[(1, 0), (1, 1), (2, 1), (1, 2), (0, 1)]])
    

def test_4_square_not_distinct():
    assert not is_t_tetromino([(0, 0), (1, 1), (0, 1), (1, 1)])
    

def test_5_square_with_4_distinct():
    assert not is_t_tetromino([(0, 0), (1, 1), (0, 1), (1, 1), (0, 2)])
