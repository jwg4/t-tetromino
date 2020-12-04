from basic import ResultBase

CYLINDER_15 = [
]

LEFT_CAPS_15 = {
    12: [
        [(0, 0), (0, 1), (1, 1), (0, 2)],
        [(0, 4), (1, 3), (1, 4), (1, 5)],
    ],
    17: [],
    21: [],
    25: [],
    13: []
}

RIGHT_CAPS_15 = {
    3: [],
    10: [],
    7: [],
    12: [],
    25: []
}

CAP_IDS_15 = [
    (25, 7),
    (21, 12),
    (25, 25),
    (17, 3),
    (13, 7),
    (12, 25),
    (12, 10),
    (13, 10),
    (17, 7),
    (13, 12),
    (17, 25),
    (17, 10),
    (21, 7),
    (17, 12),
    (21, 25),
    (12, 3)
]


class CappedCylinder(ResultBase):
    def __init__(self, height, width, lcap_width, lcap, rcap_width, rcap, cyl_width, cyl):
        self.y = height
        self.x = width
        self.n = (width - lcap_width - rcap_width) // cyl_width
        self.pieces = (
            [(lcap, 0), (rcap, lcap_width + self.n * cyl_width)] +
            [(cyl, lcap_width + i * cyl_width) for i in range(0, self.n)]
        )
            
    @property
    def tiles(self):
        for piece, offset in pieces:
            for tile in piece:
                yield [(x + offset, y) for x, y in tile]


def strip_of_height_15(x):
    a, b = CAP_IDS_15[x % 16]
    left_cap = LEFT_CAPS_15[a]
    right_cap = RIGHT_CAPS_15[b]
    return CappedCylinder(15, x, a, left_cap, b, right_cap, 16, CYLINDER_15)