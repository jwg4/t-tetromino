import sys

from link_data import DeficientRectangle
from shapes import w, h, spare, missing

if __name__ == '__main__':
    r = DeficientRectangle(w, h, spare, missing)
    print r.header_text()

