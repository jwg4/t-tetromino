import sys

import yaml


def read_data(filename):
    with open(filename, "r") as f:
        data = yaml.load(f)
    return data


def data_lines(data):
    for d in data:
        header = str(d.pop('name'))
        values = [ str(d[k]) for k in sorted(d.keys()) ]
        value_str = " & ".join([header] + values) + r" \\"
        yield value_str
        

def start_lines(data):
    col_num = len(data[0])
    format_str = "|".join(["r"] + ["c"] * (col_num))
    yield r"\begin{tabular}{%s}" % (format_str, )

    values = [ str(k) for k in sorted(data[0].keys()) if k != 'name']
    value_str = " & ".join([""] + values) + r" \\"
    yield value_str 

    yield "\hline"


if __name__ == '__main__':
    filename = sys.argv[1]

    data = read_data(filename)
    for line in start_lines(data):
        print line
    for line in data_lines(data):
        print line
    print "\end{tabular}"
    
