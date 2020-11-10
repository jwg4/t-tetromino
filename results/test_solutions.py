from hypothesis import given, settings, assume
from hypothesis.strategies import integers
from pytest import mark

from solution import get_solution

MAX_VALUE = 5
REAL_MAX_VALUE = 100


@mark.skip("We are not there yet.")
@given(integers(min_value=1, max_value=MAX_VALUE), integers(min_value=1, max_value=MAX_VALUE))
def test_all_solutions(x, y):
    solution = get_solution(x, y)
    assert solution is not None
    assert solution.check()
    assert solution.count <= 6


@settings(deadline=None)
@given(integers(min_value=1, max_value=REAL_MAX_VALUE), integers(min_value=1, max_value=REAL_MAX_VALUE))
def test_all_even_solutions(j, k):
    solution = get_solution(2 * j, 2 * k)
    assert solution is not None
    assert solution.check()
    assert solution.count <= 4


@settings(deadline=None)
@given(integers(min_value=1, max_value=MAX_VALUE), integers(min_value=1, max_value=MAX_VALUE))
def test_all_odd_solutions(x, y):
    assume(x % 2 == 1)
    assume(y % 2 == 1)
    solution = get_solution(x, y)
    assert solution is not None
    assert solution.check()
    assert solution.count <= 5


@mark.skip("We don't have an argument for this yet")
@settings(deadline=None)
@given(integers(min_value=1, max_value=MAX_VALUE), integers(min_value=1, max_value=MAX_VALUE))
def test_all_3_mod_4_by_even(x, y):
    assume(x % 4 == 3)
    assume(y % 2 == 0)
    solution = get_solution(x, y)
    assert solution is not None
    assert solution.check()
    assert solution.count == (4 if (y % 4 == 0) else 2)


@mark.skip("Stage 1")
@given(integers(min_value=37, max_value=REAL_MAX_VALUE))
def test_all_height_15(x):
    solution = get_solution(x, 15)
    assert solution is not None
    assert solution.check()
    assert solution.count == [4, 5, 6, 3][x % 4]


@mark.skip("Stage 2")
@given(integers(min_value=39, max_value=REAL_MAX_VALUE))
def test_all_height_13(x):
    solution = get_solution(x, 13)
    assert solution is not None
    assert solution.check()
    assert solution.count == [4, 5, 6, 3][x % 4]


@mark.skip("Stage 3")
@given(integers(min_value=40, max_value=REAL_MAX_VALUE), integers(min_value=40, max_value=REAL_MAX_VALUE))
def test_all_mixed_odd(x, y):
    assume(x % 4 == 3)
    assume(y % 4 == 1)
    solution = get_solution(x, y)
    assert solution is not None
    assert solution.check()
    assert solution.count == 3


@mark.skip("Stage 4")
@given(integers(min_value=40, max_value=REAL_MAX_VALUE), integers(min_value=40, max_value=REAL_MAX_VALUE))
def test_all_same_odd(x, y):
    assume(x % 2 == 1)
    assume(y % 4 == x % 4)
    solution = get_solution(x, y)
    assert solution is not None
    assert solution.check()
    assert solution.count == 5


@given(integers(min_value=1, max_value=REAL_MAX_VALUE))
def test_all_strips_of_width_2(x):
    solution = get_solution(x, 2)
    assert solution is not None
    assert solution.check()
    assert solution.count <= 4


@settings(deadline=None)
@given(integers(min_value=1, max_value=REAL_MAX_VALUE))
def test_all_squares(size):
    solution = get_solution(size, size)
    assert solution is not None
    assert solution.count <= 5


@given(integers(min_value=1, max_value=REAL_MAX_VALUE))
def test_all_even_squares(k):
    solution = get_solution(2 * k, 2 * k)
    assert solution is not None
    assert solution.count <= 4


@settings(deadline=None)
@given(integers(min_value=1, max_value=REAL_MAX_VALUE), integers(min_value=1, max_value=REAL_MAX_VALUE))
def test_all_perfect_solutions(x, y):
    solution = get_solution(4 * x, 4 * y)
    assert solution is not None
    assert solution.check()
    assert solution.count == 0
    
    
@settings(deadline=None)
@given(integers(min_value=1, max_value=REAL_MAX_VALUE))
def test_all_doubled_odd_squares(k):
    solution = get_solution(2 * k + 1, 4 * k + 2)
    assert solution is not None
    assert solution.check()
    assert solution.count == 2
    

@mark.skip("Everyone has a plan until they get punched in the face.")
@given(integers(min_value=1, max_value=REAL_MAX_VALUE), integers(min_value=0, max_value=REAL_MAX_VALUE))
def test_all_augmented_doubled_odd_squares(k, m):
    solution = get_solution(2 * k + 2 * m + 1, 4 * k  + 2 * m + 2)
    assert solution is not None
    assert solution.check()
    assert solution.count == 2
