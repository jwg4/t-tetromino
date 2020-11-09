from check import check_result


class ResultBase():
    @property
    def count(self):
        return self.x * self.y - 4 * len(list(self.tiles))

    def check(self):
        return check_result(self.x, self.y, self.tiles)


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
            for y in range(0, self.x, 4):
                yield [(x + 0, y + 0), (x + 1, y + 0), (x + 1, y + 1), (x + 2, y + 0)]
                yield [(x + 3, y + 0), (x + 2, y + 1), (x + 3, y + 1), (x + 3, y + 2)]
                yield [(x + 3, y + 3), (x + 2, y + 3), (x + 2, y + 2), (x + 1, y + 3)]
                yield [(x + 0, y + 3), (x + 0, y + 2), (x + 1, y + 2), (x + 0, y + 1)]
                