from odd_rectangle import LEFT_CAPS_15, RIGHT_CAPS_15, CYLINDER_15


def convert(shape):
    xmax = max(p[0] for tile in shape for p in tile)
    ymax = max(p[1] for tile in shape for p in tile)

    return [[(ymax - x[1], xmax - x[0]) for x in tile] for tile in shape]


if __name__ == '__main__':
    print "CYLINDER_15 = %s" % (repr(convert(CYLINDER_15)), )
