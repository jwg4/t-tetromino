from table_output import table_to_header_text

class TilingProblem(object):
    directions = [(1,1), (-1,1), (-1,-1), (1,-1)]
    base_shape = [(0,0), (0,1), (1,0), (-1,0)]
    shapes = {
        (1,1) : [(s[0], s[1]) for s in base_shape],
        (-1,1) : [(-s[1], s[0]) for s in base_shape],
        (-1,-1) : [(-s[0], -s[1]) for s in base_shape],
        (1,-1) : [(s[1], -s[0]) for s in base_shape]
    }

    def header_text(self):
        return table_to_header_text(self.row_list(), self.names())

    def row_list(self):
        return list(self._rows())

    def _translate_row(self, x, y, d):
        shape = [ (x+p[0], y+p[1]) for p in self.shapes[d] ]
        indexes = [ c[0] + self.w * c[1] for c in shape ]
        l = self._blank_list()
        for i in indexes:
            l[i] = 1
        return l

    def _blank_row(self, n):
        l = [ 0 for i in range(n) ]
        return l

class Rectangle(TilingProblem):
    def __init__(self, w, h, spare=5):
        self.w = w
        self.h = h
        self.spare = spare

    def _blank_list(self):
        n = self.w * self.h + self.spare
        return self._blank_row(n)
        
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

    def _single_square_row(self, x, y, k=None):
        l = self._blank_list()
        l[x + self.w * y] = 1
        if k is not None:
            l[self.w * self.h + k] = 1
        return l

    def _rows(self):
        for x in range(self.w):
            for y in range(self.h):
                for d in self.directions:
                    if all([ self._valid(x+p[0], y+p[1]) for p in self.shapes[d] ]):
                        yield self._translate_row(x, y, d)
                for j in range(self.spare):
                    yield self._single_square_row(x, y, j)

    def names(self):
        for x in range(self.w):
            for y in range(self.h):
                yield 'square %d %d' % (x, y)
        for j in range(self.spare):
            yield 'monomino %d' % (j, )


class DeficientRectangle(Rectangle):
    def __init__(self, w, h, spare, missing_squares):
        super(DeficientRectangle, self).__init__(w, h, spare)
        self.missing_squares = missing_squares

    def _does_not_contain_missing_square(self, row):
        for sq in self.missing_squares:
            if row[sq[0] + self.w * sq[1]]:
                return False
            return True

    def _rows(self):
        for row in super(DeficientRectangle, self)._rows():
            if self._does_not_contain_missing_square(row):
                yield row
        for sq in self.missing_squares:
            yield self._single_square_row(sq[0], sq[1])


class Strip(TilingProblem):
    def __init__(self, height, columns):
        self.h = height
        self.columns = columns
        self.w = columns + 4

    def names(self):
        for y in range(self.h):
            for x in range(self.w):
                yield 'square %d %d' % (x-2, y)
        
    def _valid(self, x, y):
        if x < -2:
            return False
        if y < 0:
            return False
        if x >= self.columns + 2:
            return False
        if y >= self.h:
            return False
        return True

    def _blank_list(self):
        n = self.w * self.h
        return self._blank_row(n)

    def _empty_square_row(self, x, y):
        l = self._blank_list()
        l[(x+2) + self.w * y] = 1
        return l
        
    def _rows(self):
        for x in range(-1, self.columns + 1):
            for y in range(self.h):
                for d in self.directions:
                    if all([ self._valid(x+p[0], y+p[1]) for p in self.shapes[d] ]):
                        yield self._translate_row(x + 2, y, d)
        for x in [-2, -1, self.columns, self.columns + 1]:
            for y in range(self.h):
                yield self._empty_square_row(x, y)
