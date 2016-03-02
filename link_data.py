class Rectangle(object):
    def __init__(self, w, h, spare=5):
        self.w = w
        self.h = h
        self.spare = spare

    def rows(self):
        for d in self.directions:
            for x in range(self.w):
                for y in range(self.h):
                    if all([ self.valid(x+p[0], y+p[1]) for p in self.shapes[self.d] ]):
                        yield self.translate_row(x, y, p)

