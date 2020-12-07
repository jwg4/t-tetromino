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

