from basic import ResultBase
from cyl_15_constant import CYLINDER_15
from cyl_15_bottom_constants import *
from cyl_15_top_constants import *

LEFT_CAPS_15 = {
    12: CYL_15_BOTTOM_12,
    17: CYL_15_BOTTOM_17,
    21: CYL_15_BOTTOM_21,
    25: CYL_15_BOTTOM_25,
    13: CYL_15_BOTTOM_13
}

RIGHT_CAPS_15 = {
    3: CYL_15_TOP_3,
    10: CYL_15_TOP_10,
    7: CYL_15_TOP_7,
    12: CYL_15_TOP_12,
    25: CYL_15_TOP_25
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
    def __init__(self, height, width, lcap_width, lcap, rcap_width, rcap, cyl_width, cyl, overlap):
        self.y = height
        self.x = width
        self.n = (width - lcap_width - rcap_width) // cyl_width
        self.pieces = (
            [(lcap, 0), (rcap, lcap_width + self.n * cyl_width - overlap)] +
            [(cyl, lcap_width + i * cyl_width - overlap) for i in range(0, self.n)]
        )
            
    @property
    def tiles(self):
        for piece, offset in self.pieces:
            for tile in piece:
                yield [(x + offset, y) for x, y in tile]


def strip_of_height_15(x):
    a, b = CAP_IDS_15[x % 16]
    left_cap = LEFT_CAPS_15[a]
    right_cap = RIGHT_CAPS_15[b]
    return CappedCylinder(15, x, a, left_cap, b, right_cap, 16, CYLINDER_15, 2)
