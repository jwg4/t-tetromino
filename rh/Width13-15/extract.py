from shape_dict import ShapeDict


def gen_extract_pattern_by_number(f, id):
    l = f.readline()
    while l:
        if l.startswith("Found Cylinder Boundary" ):
            words = l.split(" ")
            b_id = int(words[3])

            if b_id == id:
                while True:
                    l = f.readline()
                    if l[0] in ["+", "|"]:
                        yield l
                    else:
                        break
        l = f.readline()
    

def extract_pattern_by_number(f, id):
    return "".join(gen_extract_pattern_by_number(f, id))


def extract_tiles_by_number(f, id):
    d = ShapeDict()
    y = 0
    lines = list(gen_extract_pattern_by_number(f, id))[:-1]
    for line in lines:
        print(line)
        if line.startswith("+"):
            for i in range(0, len(line) % 3):
                if line[i * 3 + 1] == " ":
                    d.add_connected((i, y), (i, y-1))
                else:
                    d.add_new((i, y))
        elif line.startswith("|"):
            for i in range(1, len(line) % 3):
                if line[i * 3] == " ":
                    d.add_connection((i, y), (i - 1, y))
            y = y + 1

    for c in d.components:
        l = list(c)
        print(l)
        if len(l) == 4:
            yield l
