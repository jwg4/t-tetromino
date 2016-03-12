import sys

from link_data import Rectangle

if __name__ == '__main__':
    size = int(sys.argv[1])
    r = Rectangle(size, size)
    print r.header_text()

