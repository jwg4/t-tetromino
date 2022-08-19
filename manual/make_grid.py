
LEFT_CAP_13_HEIGHTS = [
    0, 1, 0, 1, -1, -1, -1, -1, -1, -2, -1, -2, -1
]


def gen_13_right_cap(n):
    for i in range(0, 13):
        h = LEFT_CAP_13_HEIGHTS[i]
        for j in range(0, n - h):
            yield (i, j)


def make_13_right_cap_12():
    return list(gen_13_right_cap(12))


def make_notched_right_cap(offset, is_top):
    values = make_13_right_cap_12()

    if offset % 2 == 0:
        raise Exception("Black-white parity means this has no solution.")
    if offset % 4 in [2, 3]:
        raise Exception("Sanity check - not solution which solves the gap problem.")
    
    i = 0 if is_top else 12
    skip = (i, offset)
    if skip not in values:
        raise Exception("Square to skip is not present in the values")

    return [v for v in values if v != skip]
