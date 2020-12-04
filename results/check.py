def check_result(x, y, tiles):
    seen = set()
    for tile in tiles:
        if not is_t_tetromino(tile):
            return False, "%s is not a tetromino" % (tile, )
        for s in tile:
            if s[0] >= x:
                return False, "%s overlaps the right edge" % (tile, )
            if s[1] >= y:
                return False, "%s overlaps the top edge" % (tile, )
            if s[0] < 0:
                return False, "%s overlaps the left edge" % (tile, )
            if s[1] < 0:
                return False, "%s overlaps the bottom edge" % (tile, )
            if s in seen:
                return False, "%s overlaps a previous tile at square %s" % (tile, s)
            else:
                seen.add(s)
    return True, ""


def is_t_tetromino(tile):
    if len(tile) != 4:
        return False
    if len(set(tile)) != 4:
        return False
    for square in tile:
        if all(_is_adjacent_or_same(square, other_square) for other_square in tile):
            return True
    return False


def _is_adjacent_or_same(square, other_square):
    x, y = square
    ox, oy = other_square
    return abs(x - ox) + abs(y - oy) <= 1