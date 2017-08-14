import unittest

from pycover.transform import MaximalCover


class TestMaximalCover(unittest.TestCase):
    def test_transform_problem(self):
        problem = [
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 0, 1, 0],
        ]
        transformed_problem = MaximalCover.f(problem)
        self.assertEqual(len(transformed_problem), 8)

    def test_transform_solution(self):
        solution = [0, 1]
        transformed_solution = MaximalCover.g(solution)
        self.assertEqual(transformed_solution, solution)