import os

from datetime import datetime

from polyomino.board import Irregular
from polyomino.constant import MONOMINO, TETROMINOS
from polyomino.tileset import many

from spec import ID, MCOUNT, BOARD, NAME


def make_board():
    return Irregular(BOARD)


def make_problem():
    board = make_board()
    tileset = many(TETROMINOS['T']).and_repeated_exactly(MCOUNT, MONOMINO)
    problem = board.tile_with_set(tileset)
    return problem


if __name__ == '__main__':
    start_time = datetime.utcnow()
    print("Started job %s (%s) at %s" % (ID, NAME, start_time))

    problem = make_problem()
    problem.make_problem()
    print(problem.array)
    print("\n".join([(",".join(str(i) for i in row)) for row in problem.array]))
