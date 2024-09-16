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

    ps_str = "169|2356|2160|537|542|1853|2010|2282|617|900|614|1065|898|607|606|1043|1367|1049|1219|1691|1852|1678|1354|1522|871|599|865|596|1032|862|1509|1186|589|1016|845|586|842|579|578|987|1311|993|1001|1317|1336|1474|1143|815|571|809|568|976|806|561|560|951|1275|957|1445|1290|1659|1503|1801|1646|1784|1624|1458|1824|1933|2085|1760|1594|1438|1107|779|553|552|935|1259|1579|757|545|922|1898|1585|2065|1755|1949|1814|1969|2149|1839|1920|2313"
    ps_ids = [int(s) for s in ps_str.split("|")]
    ps_tiles = [problem.key[id] for id in ps_ids]
    print(ps_tiles)
    print(problem.board.format_tiling(ps_tiles))
