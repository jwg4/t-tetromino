from results import EnumeratedResult, TransposedResult


def get_solution(x, y):
    if x < y:
        return TransposedResult(get_solution(y, x))
    elif x < 2 or y < 2 or x * y < 6:
        return EnumeratedResult.empty(x, y)
    elif x == 3 and y in [2, 3]:
        return EnumeratedResult(x, y, [[(0, 0), (0, 1), (0, 2), (1, 1)]])
    raise NotImplementedError