import os

from shape_dict import ShapeDict


def gen_extract_pattern_by_number(f, id_, height):
    l = f.readline()
    while l:
        if l.startswith("Found Cylinder Boundary" ):
            words = l.split(" ")
            b_id = int(words[3])
            b_height = int(words[6])

            if b_id == id_ and b_height == height:
                while True:
                    l = f.readline()
                    if l[0] in ["+", "|"]:
                        yield l
                    else:
                        break
        l = f.readline()


def gen_extract_pattern_from_boundary_file(f, height, bottom):
    prefix = "Solved Bottom" if bottom else "Solved Top"
    l = f.readline()
    while l:
        if l.startswith(prefix):
            words = l.split(" ")
            b_height = int(words[4])

            if b_height == height:
                while True:
                    l = f.readline()
                    if l[0] in ["+", "|"]:
                        yield l
                    else:
                        break
        l = f.readline()
    

def extract_pattern_by_number(f, id_, height):
    return "".join(gen_extract_pattern_by_number(f, id_, height))


def extract_tiles(lines):
    d = ShapeDict()
    y = 0
    for line in lines:
        if line.startswith("+"):
            for i in range(0, len(line) // 3):
                if line[i * 3 + 1] == " ":
                    d.add_connected((i, y), (i, y-1))
                else:
                    d.add_new((i, y))
        elif line.startswith("|"):
            for i in range(1, len(line) // 3):
                if line[i * 3] == " ":
                    d.add_connection((i, y), (i - 1, y))
            y = y + 1
        else:
            logging.warning("Got an unidentifed line: %s" % (line, ))

    for c in d.components:
        l = list(c)
        if len(l) == 4:
            yield l


def extract_tiles_from_boundary_file(f, height, bottom):
    lines = list(gen_extract_pattern_from_boundary_file(f, height, bottom))[:-1]
    return extract_tiles(lines)


def dump_tiles_from_boundary_file(f, height, bottom):
    l = list(extract_tiles_from_boundary_file(f, height, bottom))
    ls = [sorted(tile) for tile in l]
    sls = sorted(ls)
    return repr(sls)
    

def extract_tiles_by_number(f, id_, height):
    lines = list(gen_extract_pattern_by_number(f, id_, height))[:-1]
    return extract_tiles(lines)


def dump_tiles_by_number(f, id_, height):
    l = list(extract_tiles_by_number(f, id_, height))
    ls = [sorted(tile) for tile in l]
    sls = sorted(ls)
    return repr(sls)


def dump_tiles_by_file_id_and_height(folder, f_id, id_, height):
    filename = "%d.txt" % (f_id, )
    filepath = os.path.join(folder, filename)
    with open(filepath) as f:
        return dump_tiles_by_number(f, id_, height)
