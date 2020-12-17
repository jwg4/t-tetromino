import random

from odd_rectangle import LEFT_CAPS_15


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
            print(x, y)
            l[x][y] = LETTERS[i % LETTER_COUNT]
        i = i + 1
    
    return l


if __name__ == '__main__':
    cap = LEFT_CAPS_15[12]
    d = display(cap)
    f = "\n".join("".join(l) for l in d)
    print(f)