class Rectangle(object):
    directions = [(1,1), (-1,1), (-1,-1), (1,-1)]
    base_shape = [(0,0), (0,1), (1,0), (-1,0)]
    shapes = {
        (1,1) : [(s[0], s[1]) for s in base_shape],
        (-1,1) : [(-s[1], s[0]) for s in base_shape],
        (-1,-1) : [(-s[0], -s[1]) for s in base_shape],
        (1,-1) : [(s[1], -s[0]) for s in base_shape]
    }

    def __init__(self, w, h, spare=5):
        self.w = w
        self.h = h
        self.spare = spare

    def _translate_row(self, x, y, p):
        return '_'

    def _valid(self, x, y):
        if x < 0:
            return False
        if y < 0:
            return False
        if x >= self.w:
            return False
        if y >= self.h:
            return False
        return True

    def row_list(self):
        return list(self._rows())

    def _rows(self):
        for d in self.directions:
            for x in range(self.w):
                for y in range(self.h):
                    if all([ self._valid(x+p[0], y+p[1]) for p in self.shapes[d] ]):
                        yield self._translate_row(x, y, d)
        for j in range(self.spare):
            yield 'Foo'

