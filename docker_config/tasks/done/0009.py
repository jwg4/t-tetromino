LEFT_CAP_13_HEIGHTS = [
    0, 1, 0, 1, -1, -1, -1, -1, -1, -2, -1, -2, -1
]


def gen_13_cylinder(n):
    for i in range(0, 13):
        h = LEFT_CAP_13_HEIGHTS[i]
        for j in range(h, n + h):
            yield (i, j)


def make_13_cylinder():
    return list(gen_13_cylinder(16))

ID = "0009"
NAME = "13 width cylinder"
MCOUNT = 0
BOARD = make_13_cylinder()

