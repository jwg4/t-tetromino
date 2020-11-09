from check import check_result


class ResultBase():
    @property
    def count(self):
        return self.x * self.y - 4 * len(list(self.tiles))

    def check(self):
        is_ok, _ = check_result(self.x, self.y, self.tiles)
        return is_ok


class EnumeratedResult(ResultBase):
    def __init__(self, x, y, tiles):
        self.x = x
        self.y = y
        self._tiles = tiles

    @property
    def tiles(self):
        return self._tiles

    @staticmethod
    def empty(x, y):
        return EnumeratedResult(x, y, [])


class TransposedResult(ResultBase):
    def __init__(self, result):
        self.x = result.y
        self.y = result.x
        self._result = result
        
    @property
    def tiles(self):
        return [[(square[1], square[0]) for square in tile] for tile in self._result.tiles]


class Strip(ResultBase):
    def __init__(self, x):
        self.x = x
        self.y = 2
        
    @property
    def tiles(self):
        for x in range(0, self.x - 2, 4):
            yield [(x, 0), (x + 1, 0), (x + 1, 1), (x + 2, 0)]
        for x in range(2, self.x - 2, 4):
            yield [(x, 1), (x + 1, 1), (x + 1, 0), (x + 2, 1)]


class Perfect(ResultBase):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @property
    def tiles(self):
        for x in range(0, self.x, 4):
            for y in range(0, self.y, 4):
                yield [(x + 0, y + 0), (x + 1, y + 0), (x + 1, y + 1), (x + 2, y + 0)]
                yield [(x + 3, y + 0), (x + 2, y + 1), (x + 3, y + 1), (x + 3, y + 2)]
                yield [(x + 3, y + 3), (x + 2, y + 3), (x + 2, y + 2), (x + 1, y + 3)]
                yield [(x + 0, y + 3), (x + 0, y + 2), (x + 1, y + 2), (x + 0, y + 1)]


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
        return TransposedResult(
            ConcatenatedResult(
                TransposedResult(first),
                TransposedResult(second)
            )
        )


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
