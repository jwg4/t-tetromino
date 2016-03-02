class Rectangle(object):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    shapes = {
        (1,0) : [],
        (0,1) : [],
        (-1,0) : [],
        (0,-1) : []
    }

    def __init__(self, w, h, spare=5):
        self.w = w
        self.h = h
        self.spare = spare

    def _translate_row(self, x, y, p):
        return '_'

    def row_list(self):
        return list(self.rows())

    def rows(self):
        for d in self.directions:
            for x in range(self.w):
                for y in range(self.h):
                    if all([ self.valid(x+p[0], y+p[1]) for p in self.shapes[d] ]):
                        yield self._translate_row(x, y, d)

