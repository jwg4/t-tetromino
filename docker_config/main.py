import os

from datetime import datetime

from polyomino.board import Rectangle
from polyomino.constant import MONOMINO, TETROMINOS
from polyomino.tileset import many


def full_output(solution):
    yield "Timestamp: %s" % (datetime.utcnow())

    yield repr(solution.tiling)

    yield solution.display()


def make_board():
    return Rectangle(3, 5)


if __name__ == '__main__':
    board = make_board()
    tileset = many(TETROMINOS['T']).and_repeated_exactly(3, MONOMINO)
    problem = board.tile_with_set(tileset)
    solution = problem.solve()
    output_string = "\n".join(full_output(solution))

    FOLDER = os.environ['DEST_FOLDER']
    destination = os.path.join(FOLDER, "output.txt")
    with open(destination, "w") as f:
        f.write(output_string)
