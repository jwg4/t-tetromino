from basic import ResultBase
from cyl_15_constant import CYLINDER_15
from cyl_15_bottom_constants import *
from cyl_15_top_constants import *
from cyl_15_extra import TILING as CYL_15_BOTTOM_21

from cylinder_13.cylinder import TILING as CYLINDER_13
from cylinder_13.left_30 import TILING as CYL_13_BOTTOM_30
from cylinder_13.right_10 import TILING as CYL_13_TOP_10
from cylinder_13.right_12 import TILING as CYL_13_TOP_12
from cylinder_13.right_3 import TILING as CYL_13_TOP_3
from cylinder_13.right_5 import TILING as CYL_13_TOP_5

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
    (25, 7),  #  0
    (21, 12), #  1
    (25, 25), #  2
    (17, 3),  #  3
    (13, 7),  #  4
    (12, 25), #  5
    (13, 25), #  6
    (13, 10), #  7
    (17, 7),  #  8
    (13, 12), #  9
    (17, 25), # 10
    (17, 10), # 11
    (21, 7),  # 12
    (17, 12), # 13
    (21, 25), # 14
    (12, 3)   # 15
]

LEFT_CAPS_13 = [
    (34, CYL_13_BOTTOM_34),
    (38, CYL_13_BOTTOM_38),
    (42, CYL_13_BOTTOM_42),
    (30, CYL_13_BOTTOM_30),
]

RIGHT_CAPS_13 = [
    (12, CYL_13_TOP_12),
    (7, CYL_13_TOP_7),
    (10, CYL_13_TOP_10),
    (3, CYL_13_TOP_3),
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
        for piece, offset in self.pieces:
            for tile in piece:
                yield [(x + offset, y) for x, y in tile]


def strip_of_height_15(x):
    cyl_width = 16
    a, b = CAP_IDS_15[x % cyl_width]
    left_cap = LEFT_CAPS_15[a]
    right_cap = RIGHT_CAPS_15[b]
    return CappedCylinder(15, x, a, left_cap, b, right_cap, cyl_width, CYLINDER_15)


def strip_of_height_13(x):
    cyl_width = 16
    bb = (x - 2) % 4
    b, right_cap = RIGHT_CAPS_15[bb]
    aa = ((x - 2 - b) // 4) % 4
    a, left_cap = LEFT_CAPS_15[aa]
    return CappedCylinder(13, x, a, left_cap, b, right_cap, cyl_width, CYLINDER_13)
