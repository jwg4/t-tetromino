def generate_tiling(width, height):
    if width == 4 and height == 4:
        return (
            [
                ((0, 0), (0, 1), (0, 2), (1, 1)),
                ((0, 3), (1, 2), (1, 3), (2, 3)),
                ((3, 3), (3, 2), (3, 1), (2, 2)),
                ((3, 0), (2, 1), (2, 0), (1, 0)),
            ],
            []
        )
    w = width % 4
    h = height % 4
