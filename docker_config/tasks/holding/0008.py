LEFT_CAP_13_HEIGHTS = [
    0, 1, 0, 1, -1, -1, -1, -1, -1, -2, -1, -2, -1
]


def gen_13_left_cap(n):
    for i in range(0, 13):
        h = LEFT_CAP_13_HEIGHTS[i]
        for j in range(0, n + h):
            yield (i, j)


def make_13_left_cap(n):
    return list(gen_13_left_cap(n))

ID = "0008"
NAME = "13 LEFT CAP 38"
MCOUNT = 1
BOARD = make_13_left_cap(38)

