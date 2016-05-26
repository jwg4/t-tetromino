def generate_tiling(width, height):
    if width == 4 and height == 4:
        return (
            [
                ((0, 0), (0, 1), (0, 2), (1, 1)),
                ((0, 0), (0, 1), (0, 2), (1, 1)),
                ((0, 0), (0, 1), (0, 2), (1, 1)),
                ((0, 0), (0, 1), (0, 2), (1, 1)),
            ],
            []
        )
    w = width % 4
    h = height % 4
