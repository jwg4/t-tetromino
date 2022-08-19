import pretty_poly.png

from make_grid import make_notched_right_cap


if __name__ == '__main__':
    for offset in [1, 5, 9]:
        grid = make_notched_right_cap(offset, True)
        filename = "top_%d.png" % (offset, )
        pretty_poly.png.write_lines_png(filename, [[g] for g in grid])

        grid = make_notched_right_cap(offset, False)
        filename = "bottom_%d.png" % (offset, )
        pretty_poly.png.write_lines_png(filename, [[g] for g in grid])
