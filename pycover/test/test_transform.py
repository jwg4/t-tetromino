import unittest

from pycover.transform import MaximalCover


class TestMaximalCover(unittest.TestCase):
    problem = [
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    problem_2 = [
        [1, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1],
    ]
    problem_3 = [
        [1, 1, 1, 0],
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
    ]


    def test_transform_problem(self):
        transformed_problem = MaximalCover.f(self.problem)
        self.assertEqual(len(transformed_problem), 8)

    def test_transform_solution(self):
        solution = [
            [1, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 1],
        ]
        transformed_solution = MaximalCover.g(solution, self.problem)
        self.assertEqual(len(transformed_solution), len(solution))
        
    def test_transform_problem_2(self):
        transformed_problem = MaximalCover.f(self.problem_2)
        self.assertEqual(len(transformed_problem), 8)

    def test_transform_solution_2(self):
        solution = [
            [1, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 1]
        ]
        transformed_solution = MaximalCover.g(solution, self.problem_2)
        expected = [
            [1, 1, 1, 0],
        ]
        self.assertEqual(transformed_solution, expected)

    def test_transform_problem_with_singleton(self):
        transformed_problem = MaximalCover.f(self.problem_3)
        expected = [
            [1, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 0, 1, 0],
        ]
        self.assertEqual(transformed_problem, expected)

    def test_transform_solution_with_singleton(self):
        solution = [
            [1, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 1]
        ]
        transformed_solution = MaximalCover.g(solution, self.problem_3)
        expected = [
            [1, 1, 1, 0],
            [0, 0, 0, 1],
        ]
        self.assertEqual(transformed_solution, expected)