from odd_rectangle import LEFT_CAPS_15, RIGHT_CAPS_15


def convert(shape):
    xmax = max(p[0] for tile in shape for p in tile)
    ymax = max(p[1] for tile in shape for p in tile)

    return [[(ymax - x[1], x[0]) for x in tile] for tile in shape]


if __name__ == '__main__':
    for k in RIGHT_CAPS_15:
        print("CYL_15_TOP_%d = %s" % (k, repr(convert(RIGHT_CAPS_15[k]))))