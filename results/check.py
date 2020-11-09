def check_result(x, y, tiles):
    for tile in tiles:
        for s in tile:
            if s[0] >= x:
                return False
            if s[1] >= y:
                return False
    return True