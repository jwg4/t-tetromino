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

def transpose(tiling):
    if tiling is None:
        return None
    else:
        tiles = tiling[0]
        squares = tiling[1]
    tiles_t = [ tuple((t[1], t[0]) for t in tile) for tile in tiles ]
    squares_t = [ (sq[1], sq[0]) for sq in squares ]
    return (tiles_t, squares_t)

def generate_tiling(width, height):
    if height < width:
        return transpose(generate_tiling(height, width))
    if width == 0:
        return ([], [])
    if width == 1:
        return ([], [(0, i) for i in range(0, height)])
    if width == 2:
        tiles = []
        singles = [(0, 0)]
        for i in range(2, height, 4):
            tiles.append(((1, i-2), (0, i-1), (1, i-1), (1, i)))
        for j in range(4, height, 4):
            tiles.append(((0, j-2), (0, j-1), (1, j-1), (0, j)))
        if i > j:
            singles.append((0, i))
        else:
            singles.append((1, j))
        for k in range(max(i, j), height):
            singles.append((k, 0))
            singles.append((k, 0))
        return (tiles, singles)
    if width == 4 and height == 4:
        return (
            SQUARE_TILING,
            []
        )
    w = width % 4
    h = height % 4
    if w == 0 and h == 0:
        return (list(_perfect_tiling(width / 4, height / 4)), [])
        
