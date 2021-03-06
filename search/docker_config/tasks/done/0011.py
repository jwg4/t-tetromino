RIGHT_CAP_13_HEIGHTS = [
    2, 3, 2, 3, 2, 2, 2, 2, 2, 0, 1, 0, 1
]


def gen_13_right_cap(n):
    for i in range(0, 13):
        h = RIGHT_CAP_13_HEIGHTS[i]
        for j in range(0, n + h - 1):
            if i != 0 or j != 0:
                yield (i, j)


def make_13_right_cap(n):
    return list(gen_13_right_cap(n))

ID = "0011"
NAME = "right_cap_13_height_5_corner"
MCOUNT = 1
BOARD = make_13_right_cap(5)

