import os

from datetime import datetime

from polyomino.board import Irregular
from polyomino.constant import MONOMINO, TETROMINOS
from polyomino.tileset import many

from spec import ID, MCOUNT, BOARD


def full_output(solution):
    yield "ID: %s" % (ID, )
    yield "Timestamp: %s" % (datetime.utcnow())

    yield repr(solution.tiling)

    yield solution.display()


def make_board():
    return Irregular(BOARD)


if __name__ == '__main__':
    board = make_board()
    tileset = many(TETROMINOS['T']).and_repeated_exactly(MCOUNT, MONOMINO)
    problem = board.tile_with_set(tileset)
    solution = problem.solve()
    output_string = "\n".join(full_output(solution))

    FOLDER = os.environ['DEST_FOLDER']
    filename =  "output_%s.txt" % (ID, )
    destination = os.path.join(FOLDER, filename)
    with open(destination, "w") as f:
        f.write(output_string)
