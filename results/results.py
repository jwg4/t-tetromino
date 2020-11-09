class EnumeratedResult():
    def __init__(self, x, y, tiles):
        self.x = x
        self.y = y
        self.tiles = tiles
        self.check()

    def check(self):
        return True
    
    @property
    def count(self):
        return self.x * self.y - 4 * len(self.tiles)

    @staticmethod
    def empty(x, y):
        return EnumeratedResult(x, y, [])
