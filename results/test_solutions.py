from hypothesis import given, strategies
from pytest import mark

from solution import get_solution

MAX_VALUE = 2


@given(strategies.integers(min_value=1, max_value=MAX_VALUE), strategies.integers(min_value=1, max_value=MAX_VALUE))
def test_all_solutions(x, y):
    solution = get_solution(x, y)
    assert solution is not None
    assert solution.check()
    assert solution.count < 6


@mark.skip('We have these results in our paper')
@given(strategies.integers(min_value=1))
def test_all_squares(size):
    solution = get_solution(size)
    assert solution is not None
    assert solution.count < 5

