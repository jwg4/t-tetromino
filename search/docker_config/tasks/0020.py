RIGHT_CAP_13_HEIGHTS = [
    2, 3, 2, 3, 2, 2, 2, 2, 2, 0, 1, 0, 1
]


def gen_13_right_cap_with_notch(n, remove):
    for i in range(0, 13):
        h = RIGHT_CAP_13_HEIGHTS[i]
        for j in range(0, n + h - 1):
            if i != remove[0] or j != remove[1]:
                yield (i, j)


def make_13_right_cap_with_notch(n, remove):
    return list(gen_13_right_cap_with_notch(n, remove))

ID = "0020"
NAME = "right_cap_13_height_12_other_corner"
MCOUNT = 0
BOARD = make_13_right_cap_with_notch(12, (12, 0))

