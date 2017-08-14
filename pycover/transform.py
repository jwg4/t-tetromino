def make_monad(f, g):
    def monad(x):
        def y(a):
            return g(x(f(a)))
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


def MaximalCoverSolution(solution):
    return solution


MaximalCover = make_monad(MaximalCoverProblem, MaximalCoverSolution)