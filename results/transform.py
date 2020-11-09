from results import ResultBase


class TransformedResult(ResultBase):
    def __init__(self, result):
        self.x, self.y = self.transform_size(result.x, result.y)
        self._result = result
        
    @property
    def tiles(self):
        return [
            [self.transform_square(square) for square in tile]
            for tile in self._result.tiles
        ]

    def transform_size(self, x, y):
        return x, y


class TransposedResult(TransformedResult):
    def transform_size(self, x, y):
        return y, x

    def transform_square(self, square):
        x, y = square
        return y, x


def transpose(result):
    if result is TransposedResult:
        return result._result
    else:
        return TransposedResult(result)


class FlippedResult(TransformedResult):
    def transform_square(self, square):
        x, y = square
        return x, self.y - 1 - y


class FloppedResult(TransformedResult):
    def transform_square(self, square):
        x, y = square
        return self.x - 1 - x, y


def reflect(result, horizontal=True):
    if horizontal:
        if result is FlippedResult:
            return result._result
        else:
            return FlippedResult(result)
    else:
        if result is FloppedResult:
            return result._result
        else:
            return FloppedResult(result)
    