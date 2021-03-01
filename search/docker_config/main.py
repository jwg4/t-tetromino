import logging
import os

from datetime import datetime

from polyomino.board import Irregular
from polyomino.constant import MONOMINO, TETROMINOS
from polyomino.tileset import many

from spec import ID, MCOUNT, BOARD, NAME


def full_output(solution, board, start_time):
    yield "# ID: %s" % (ID, )
    yield "# NAME: %s" % (NAME, )
    yield "# Start time: %s" % (start_time, )
    yield "# Timestamp: %s" % (datetime.utcnow(), )

    if solution:
        yield "TILING = %s" % (repr(solution.tiling), )

        yield "DISPLAY = '''"
        yield solution.display()
        yield "'''"
    else:
        yield "# NO SOLUTION!"
        yield "SHAPE = %s" % (repr(board.squares), )
        yield "SHAPE_DISPLAY = '''"
        yield board.display()
        yield "'''"
        


def make_board():
    return Irregular(BOARD)


def make_logging(folder, id):
    logfile = "logging_%s.txt" % (id, )
    logpath = os.path.join(folder, logfile)
    logging.basicConfig(filename=logpath, level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    logger = logging.getLogger(__name__)
    logger.info("Logging configured")
    return logger


if __name__ == '__main__':
    FOLDER = os.environ['DEST_FOLDER']
    logger = make_logging(FOLDER, ID)

    start_time = datetime.utcnow()
    logger.info("Started job %s (%s) at %s" % (ID, NAME, start_time))

    board = make_board()
    tileset = many(TETROMINOS['T']).and_repeated_exactly(MCOUNT, MONOMINO)
    problem = board.tile_with_set(tileset).with_heuristics()
    solution = problem.solve()
    output_string = "\n".join(full_output(solution, board, start_time))

    filename =  "output_%s.txt" % (ID, )
    destination = os.path.join(FOLDER, filename)
    with open(destination, "w") as f:
        f.write(output_string)

    logging.info("Finished job %s (%s) at %s" % (ID, NAME, datetime.utcnow()))
