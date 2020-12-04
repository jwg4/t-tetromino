from split import split_exact_cover


def test_basic_split():
    problem = [[1, 0, 0], [0, 1, 1]]
    solution = solve(problem)
    subsolutions = []
    for subproblem, transform in split_exact_cover(problem):
        subsolution = solve(subproblem)
        subsolutions.append(transform(subsolution))

    assert solution in subsolutions

