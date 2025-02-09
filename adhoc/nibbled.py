from polyomino.board import Rectangle

def NibbledRectangle(x, y):
    if x < 2 or y < 3:
        raise NotImplementedError
    return Rectangle(x, y).remove(0, 0).remove(0, 1).remove(1, 0).remove(0, y-1)


def NibbledSquare(n):
    return NibbledRectangle(n, n)
    