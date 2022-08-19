from polyomino.board import Irregular
from polyomino.constant import TETROMINOS

from make_grid import make_13_right_cap_12


if __name__ == '__main__':
    t = TETROMINOS['T']
    grid = make_13_right_cap_12()

    for square in grid:
        reduced = [ g for g in grid if g != square ]
        board = Irregular(reduced)

        problem = board.tile_with_many(t)
        solution = problem.solve()
        if solution:        
            print(square)

