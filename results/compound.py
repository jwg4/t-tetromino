from basic import ResultBase
from transform import transpose


class ConcatenatedResult(ResultBase):
    def __init__(self, first, second):
        if first.x != second.x:
            raise Exception(
                "Widths of the (%d, %d) and (%d, %d) do not match"
                % (first.x, first.y, second.x, second.y)
            )
        self.x = first.x
        self.y = first.y + second.y
        self.first = first
        self.second = second
        
    @property
    def tiles(self):
        yield from self.first.tiles
        for tile in self.second.tiles:
            yield [(t[0], t[1] + self.first.y) for t in tile]

    @staticmethod
    def AlongXAxis(first, second):
        return transpose(
            ConcatenatedResult(
                transpose(first),
                transpose(second)
            )
        )


class AugmentedResult(ResultBase):
    def __init__(self, base, extra):
        self.x = base.x
        self.y = base.y
        self.base = base
        self.extra = extra
    
    @property
    def tiles(self):
        yield from self.base.tiles
        yield from self.extra


class SimpleLShape(ResultBase):
    def __init__(self, inner):
        self.x = inner.x + 2
        self.y = inner.y + 2
        self.inner = inner
    
    @property
    def tiles(self):
        yield from self.inner.tiles
        if self.x % 4 == 1 or self.x % 4 == 2:
            for x in range(0, self.x - 4, 4):
                yield [(x, self.y - 2), (x + 1, self.y - 2), (x + 1, self.y - 1), (x + 2, self.y - 2)]
            for x in range(2, self.x - 2, 4):
                yield [(x, self.y - 1), (x + 1, self.y - 1), (x + 1, self.y - 2), (x + 2, self.y - 1)]
        else:
            for x in range(0, self.x - 2, 4):
                yield [(x, self.y - 1), (x + 1, self.y - 1), (x + 1, self.y - 2), (x + 2, self.y - 1)]
            for x in range(2, self.x - 4, 4):
                yield [(x, self.y - 2), (x + 1, self.y - 2), (x + 1, self.y - 1), (x + 2, self.y - 2)]
        if self.x % 2 == 0:
            for y in range(self.y - 1, 1, -4):
                yield [(self.x - 1, y), (self.x - 2, y - 1), (self.x - 1, y - 1), (self.x - 1, y - 2)]
            for y in range(self.y - 3, 1, -4):
                yield [(self.x - 2, y), (self.x - 1, y - 1), (self.x - 2, y - 1), (self.x - 2, y - 2)]
        else:
            for y in range(self.y - 2, 1, -4):
                yield [(self.x - 1, y), (self.x - 2, y - 1), (self.x - 1, y - 1), (self.x - 1, y - 2)]
            for y in range(self.y - 4, 1, -4):
                yield [(self.x - 2, y), (self.x - 1, y - 1), (self.x - 2, y - 1), (self.x - 2, y - 2)]
