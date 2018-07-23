import sys

import yaml


def read_data(filename):
    with open(filename, "r") as f:
        data = yaml.load(f)
    return data


def start_line(data):
    col_num = len(data[0])
    format_str = "|".join(["r"] + ["c"] * (col_num))
    return r"\begin{tabular}{%s}" % (format_str, )


if __name__ == '__main__':
    filename = sys.argv[1]

    data = read_data(filename)
    print start_line(data)
    print "\end{tabular}"
    
