from hypothesis import given
from hypothesis.strategies import integers
from pytest import mark

from solution import get_solution

MAX_VALUE = 3


@given(integers(min_value=1, max_value=MAX_VALUE), integers(min_value=1, max_value=MAX_VALUE))
def test_all_solutions(x, y):
    solution = get_solution(x, y)
    assert solution is not None
    assert solution.check()
    assert solution.count < 6


@given(integers(min_value=1, max_value=MAX_VALUE))
def test_all_strips_of_width_2(x):
    solution = get_solution(x, 2)
    assert solution is not None
    assert solution.check()
    assert solution.count < 4


@mark.skip('We have these results in our paper')
@given(integers(min_value=1))
def test_all_squares(size):
    solution = get_solution(size)
    assert solution is not None
    assert solution.count < 5


@given(integers(min_value=1), integers(min_value=1))
def test_all_perfect_solutions(x, y):
    solution = get_solution(4 * x, 4 * y)
    assert solution is not None
    assert solution.check()
    assert solution.count == 0
    
    
@given(integers(min_value=1))
def test_all_doubled_odd_squares(k):
    solution = get_solution(2 * k + 1, 4 * k + 2)
    assert solution is not None
    assert solution.check()
    assert solution.count == 2
    
    
@given(integers(min_value=1), integers(min_value=0))
def test_all_augmented_doubled_odd_squares(k, m):
    solution = get_solution(2 * k + 2 * m + 1, 4 * k  + 2 * m + 2)
    assert solution is not None
    assert solution.check()
    assert solution.count == 2
