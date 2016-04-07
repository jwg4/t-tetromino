import sys

from link_data import Rectangle

if __name__ == '__main__':
    w = int(sys.argv[1])
    h = int(sys.argv[2])
    r = Rectangle(w, h)
    print r.header_text()

