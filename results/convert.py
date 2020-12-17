from odd_rectangle import LEFT_CAPS_15


def convert(shape):
    return [[(x[1], x[0]) for x in tile] for tile in shape]


if __name__ == '__main__':
    for k in LEFT_CAPS_15:
        print("CYL_15_BOTTOM_%d = %s" % (k, repr(convert(LEFT_CAPS_15[k]))))