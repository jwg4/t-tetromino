import logging

from extract import dump_tiles_by_file_id_and_height



if __name__ == '__main__':
    ID = 671217151
    CYLS = [
        (29, 42),
        (33, 46),
        (37, 50),
        (41, 54),
    ]
    FOLDER = "Width13"

    logging.basicConfig(level=logging.INFO)

    for height, f_id in CYLS:
        print(dump_tiles_by_file_id_and_height(FOLDER, f_id, ID, height))
