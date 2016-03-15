import random
import re

import png

def print_alpha_blocks(grid):
    chars = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    table = [ [ chars[n] for n in l ] for l in grid ]
    for row in table:
        print ''.join(row)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def create_png(grid, scale=10):
    d = dict()
    color_data = []
    palette = []
    for r in grid:
        out_row = []
        for c in r:
            if c not in d:
                d[c] = random_color()
            for i in range(scale):
                out_row.append(len(palette))
            palette.append(d[c])
        for i in range(scale):
            color_data.append(out_row)
    height = len(grid) * scale
    width = len(grid[0]) * scale
    writer = png.Writer(width=width, height=height, palette=palette)
    with open('output.png', 'w') as f:
        writer.write(f, color_data)
            

count = 1

f = open('13x13-result', 'r')

table = [ ([' '] * 13) for i in range(13) ]

for l in f.readlines():
    m = re.match(r'square (\d+) (\d+) monomino (\d+)', l) 
    if m:
        row = int(m.group(1))
        column = int(m.group(2))
        table[row][column] = count
        count = count + 1
    m = re.match(r'square (\d+) (\d+) square (\d+) (\d+) square (\d+) (\d+) square (\d+) (\d+)', l) 
    if m:
        for j in range(4):
            row = int(m.group(2 * j + 1))
            column = int(m.group(2 * j + 2))
            table[row][column] = count
        count = count + 1
            
print_alpha_blocks(table)
create_png(table)
