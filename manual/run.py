from polyomino.board import Irregular
from polyomino.constant import TETROMINOS

from make_grid import gen_13_right_cap


if __name__ == '__main__':
    LENGTH = 24
    t = TETROMINOS['T']
    grid = list(gen_13_right_cap(LENGTH))

    for square in grid:
        reduced = [ g for g in grid if g != square ]
        board = Irregular(reduced)

        problem = board.tile_with_many(t)
        solution = problem.solve()
        if solution:        
            print(square)

