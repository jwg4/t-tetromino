from polyomino.board import Irregular
from polyomino.constant import TETROMINOS

from make_grid import make_notched_right_cap


if __name__ == '__main__':
    grid = make_notched_right_cap(5, True)

    t = TETROMINOS['T']
    board = Irregular(grid)

    problem = board.tile_with_many(t)

