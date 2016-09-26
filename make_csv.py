import sys

from link_data import DeficientRectangle
from shapes import w, h, spare, missing

if __name__ == '__main__':
    r = DeficientRectangle(w, h, spare, missing)
    with open("names.txt", "w") as f:
        write(f, r.names_text())
    with open("rows.txt", "w") as f:
        write(f, r.rows_text())

