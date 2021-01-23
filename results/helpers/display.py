import random

from odd_rectangle import LEFT_CAPS_15, RIGHT_CAPS_15
from odd_rectangle import CYLINDER_15


LETTERS = list("0123456789qwertyuiopasdfghjklzxcvbnm?")
random.shuffle(LETTERS)
LETTERS = "".join(LETTERS)
LETTER_COUNT = len(LETTERS)


def display(shape):
    xmax = max(p[0] for tile in shape for p in tile)
    ymax = max(p[1] for tile in shape for p in tile)

    l = [[" " for i in range(0, ymax + 1)] for j in range(0, xmax + 1)]
    
    i = 1
    for tile in shape:
        for x, y in tile:
            l[x][y] = LETTERS[i % LETTER_COUNT]
        i = i + 1
    
    return l


def format(shape):
    d = display(shape)
    return "\n".join("".join(l) for l in d)


if __name__ == '__main__':
    cap = LEFT_CAPS_15[12]
    f = format(cap)
    print(f)

    cyl = CYLINDER_15
    f = format(cyl)
    print(f)

    cap = RIGHT_CAPS_15[25]
    f = format(cap)
    print(f)
    