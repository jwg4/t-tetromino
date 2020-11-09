from basic import EnumeratedResult, Strip, Perfect
from compound import SimpleLShape, ConcatenatedResult
from odd_square import make_odd_square
from transform import TransposedResult


def get_solution(x, y):
    if x < y:
        return TransposedResult(get_solution(y, x))
    elif x < 2 or y < 2 or (x == 2 and y == 2):
        return EnumeratedResult.empty(x, y)
    elif x == 3 and y in [2, 3]:
        return EnumeratedResult(x, y, [[(0, 0), (1, 0), (2, 0), (1, 1)]])
    elif y == 2:
        return Strip(x)
    elif x % 4 == 0 and y % 4 == 0:
        return Perfect(x, y)
    elif x % 4 == 0 and y % 4 == 2:
        return ConcatenatedResult(Perfect(x, y - 2), Strip(x))
    elif x % 4 == 2 and y % 4 == 0:
        return ConcatenatedResult.AlongXAxis(Perfect(x - 2, y), TransposedResult(Strip(y)))
    elif x % 4 == 2 and y % 4 == 2:
        return SimpleLShape(Perfect(x - 2, y - 2))
    elif x == y and x % 2 == 1:
        return make_odd_square(x)
    raise NotImplementedError