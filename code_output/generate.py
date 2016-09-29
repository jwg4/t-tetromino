SQUARE_TILING = [
    ((0, 0), (0, 1), (0, 2), (1, 1)),
    ((0, 3), (1, 2), (1, 3), (2, 3)),
    ((3, 3), (3, 2), (3, 1), (2, 2)),
    ((3, 0), (2, 1), (2, 0), (1, 0)),
]

def _perfect_tiling(width, height):
    for i in range(width):
        for j in range(height):
            for p in SQUARE_TILING:
                yield tuple( (x[0] + 4 * i, x[1] + 4 * j) for x in p )

def generate_tiling(width, height):
    if width == 0 or height == 0:
        return ([], [])
    if width == 4 and height == 4:
        return (
            SQUARE_TILING,
            []
        )
    w = width % 4
    h = height % 4
    if w == 0 and h == 0:
        return (list(_perfect_tiling(width / 4, height / 4)), [])
        
