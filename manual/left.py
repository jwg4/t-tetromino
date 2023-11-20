import argparse

from polyomino.board import Irregular
from polyomino.constant import TETROMINOS

from make_grid import gen_13_left_cap


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    args = parser.parse_args()
    
    t = TETROMINOS['T']
    grid = list(gen_13_left_cap(args.length))

    for square in grid:
        reduced = [ g for g in grid if g != square ]
        board = Irregular(reduced)

        problem = board.tile_with_many(t)
        solution = problem.solve()
        if solution:        
            print(square)

