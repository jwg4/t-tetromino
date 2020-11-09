from results import EnumeratedResult, TransposedResult, Strip, Perfect


def get_solution(x, y):
    if x < y:
        return TransposedResult(get_solution(y, x))
    elif x < 2 or y < 2 or x * y < 6:
        return EnumeratedResult.empty(x, y)
    elif x == 3 and y in [2, 3]:
        return EnumeratedResult(x, y, [[(0, 0), (1, 0), (2, 0), (1, 1)]])
    elif y == 2:
        return Strip(x)
    elif x % 4 == 0 and y % 4 == 0:
        return Perfect(x, y)
    raise NotImplementedError