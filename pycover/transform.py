def make_monad(f, g):
    def monad(x):
        def y(a):
            return g(x(f(a)), a)
        return y

    monad.f = f
    monad.g = g

    return monad


def generate_max_cover_problem(problem):
        l = len(problem[0])
        c = len(problem)
        new = []
        for j in range(l):
            blank = [0] * (c + l)
            blank[j + c] = 1
            new.append(blank)

        for i in range(c):
            blank = [0] * c
            blank[i] = 1
            for s in range(l):
                if problem[i][s]:
                    new[s][i] = 1
            yield blank + problem[i]
        
        for row in new:
            yield row


def MaximalCoverProblem(problem):
    return list(generate_max_cover_problem(problem))


def generate_max_cover_solution(solution, problem):
    n_sets = len(problem[0])
    
    for row in solution:
        count = len([bit for bit in row[0:n_sets] if bit == 1])
        if count == 1:
            yield row[n_sets:]
    return solution


def MaximalCoverSolution(solution, problem):
    return list(generate_max_cover_solution(solution, problem))


MaximalCover = make_monad(MaximalCoverProblem, MaximalCoverSolution)