from results import EnumeratedResult


def get_solution(x, y):
    if x < 2 or y < 2 or x * y < 6:
        return EnumeratedResult.empty(x, y)
    raise NotImplementedError