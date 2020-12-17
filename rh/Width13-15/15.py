import logging

from extract import dump_tiles_from_boundary_file



if __name__ == '__main__':
    CYLS = [
        (14, True), 
        (19, True), 
        (23, True), 
        (27, True), 
        (13, True), 
        (3, False), 
        (10, False), 
        (7, False), 
        (12, False), 
        (25, False), 
    ]
    filename = "Width15/6333419-halfBdry_rev.txt"

    logging.basicConfig(level=logging.INFO)

    for height, bottom in CYLS:
        with open(filename) as source_f:
            print(dump_tiles_from_boundary_file(source_f, height, bottom))
