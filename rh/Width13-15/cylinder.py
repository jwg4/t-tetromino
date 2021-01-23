import logging

from extract import extract_tiles


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    filename = "Width15/6333419_bdry_edit.txt"
    with open(filename) as f:
        l = list(extract_tiles(f.readlines()))
    print(l)