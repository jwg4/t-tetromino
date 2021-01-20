import os

from datetime import datetime

from polyomino.board import Irregular
from polyomino.constant import MONOMINO, TETROMINOS
from polyomino.tileset import many

from spec import ID, MCOUNT, BOARD


def full_output(solution, start_time):
    yield "# ID: %s" % (ID, )
    yield "# Start time: %s" % (start_time, )
    yield "# Timestamp: %s" % (datetime.utcnow(), )

    yield "TILING = %s" % (repr(solution.tiling), )

    yield "DISPLAY = '''"
    yield solution.display()
    yield "'''"


def make_board():
    return Irregular(BOARD)


if __name__ == '__main__':
    start_time = datetime.utcnow()

    board = make_board()
    tileset = many(TETROMINOS['T']).and_repeated_exactly(MCOUNT, MONOMINO)
    problem = board.tile_with_set(tileset)
    solution = problem.solve()
    output_string = "\n".join(full_output(solution, start_time))

    FOLDER = os.environ['DEST_FOLDER']
    filename =  "output_%s.txt" % (ID, )
    destination = os.path.join(FOLDER, filename)
    with open(destination, "w") as f:
        f.write(output_string)
