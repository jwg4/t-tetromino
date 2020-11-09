from basic import ResultBase, EnumeratedResult
from transform import transpose, reflect


def make_odd_square(n):
    if n == 3:
        return EnumeratedResult(3, 3, [[(0, 0), (1, 0), (2, 0), (1, 1)]])
    elif n % 4 == 1: 
        base = make_odd_square(n - 2)
        return transpose(OddEvenSquare(base))
    elif n % 4 == 3:
        base = make_odd_square(n - 2)
        return reflect(transpose(OddOddSquare(reflect(base, False))), False)


class OddSquare(ResultBase):
    def __init__(self, base):
        self._base = base
        self.x = base.x + 2
        self.y = base.y + 2


class OddEvenSquare(OddSquare):
    @property
    def tiles(self):
        yield from self._base.tiles
        yield [(0, self.y - 4), (0, self.y - 3), (1, self.y - 3), (0, self.y - 2)]
        for x in range(0, self.x - 4, 4):
            yield [(x, self.y - 1), (x + 1, self.y - 1), (x + 1, self.y - 2), (x + 2, self.y - 1)]
        for x in range(2, self.x - 2, 4):
            yield [(x, self.y - 2), (x + 1, self.y - 2), (x + 1, self.y - 1), (x + 2, self.y - 2)]
        yield [(self.x - 3, self.y - 3), (self.x - 2, self.y - 3), (self.x - 2, self.y - 4), (self.x - 1, self.y - 3)]
        for y in range(1, self.y - 7, 4):
            yield [(self.x - 2, y), (self.x - 2, y + 1), (self.x - 1, y + 1), (self.x - 2, y + 2)]
        for y in range(3, self.y - 5, 4):
            yield [(self.x - 1, y), (self.x - 1, y + 1), (self.x - 2, y + 1), (self.x - 1, y + 2)]


class OddOddSquare(OddSquare):
    @property
    def tiles(self):
        yield from self._base.tiles
        yield [(0, self.y - 3), (0, self.y - 2), (1, self.y - 2), (0, self.y - 1)]
        for x in range(1, self.x - 5, 4):
            yield [(x, self.y - 1), (x + 1, self.y - 1), (x + 1, self.y - 2), (x + 2, self.y - 1)]
        for x in range(3, self.x - 3, 4):
            yield [(x, self.y - 2), (x + 1, self.y - 2), (x + 1, self.y - 1), (x + 2, self.y - 2)]
        yield [(self.x - 4, self.y - 3), (self.x - 3, self.y - 3), (self.x - 3, self.y - 4), (self.x - 2, self.y - 3)]
        for y in range(0, self.y - 6, 4):
            yield [(self.x - 2, y), (self.x - 2, y + 1), (self.x - 1, y + 1), (self.x - 2, y + 2)]
        for y in range(2, self.y - 4, 4):
            yield [(self.x - 1, y), (self.x - 1, y + 1), (self.x - 2, y + 1), (self.x - 1, y + 2)]
