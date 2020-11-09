from check import check_result


class ResultBase():
    @property
    def count(self):
        return self.x * self.y - 4 * len(self.tiles)

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
