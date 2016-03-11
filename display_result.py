import re

def print_alpha_blocks(grid):
    chars = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    table = [ [ chars[n] for n in l ] for l in grid ]
    for row in table:
        print ''.join(row)

count = 1

f = open('13x13-result', 'r')

table = [ ([' '] * 13) for i in range(13) ]

for l in f.readlines():
    m = re.match(r'square (\d+) (\d+) monomino (\d+)', l) 
    if m:
        row = int(m.group(1))
        column = int(m.group(2))
        table[row][column] = 0
    m = re.match(r'square (\d+) (\d+) square (\d+) (\d+) square (\d+) (\d+) square (\d+) (\d+)', l) 
    if m:
        for j in range(4):
            row = int(m.group(2 * j + 1))
            column = int(m.group(2 * j + 2))
            table[row][column] = count
        count = count + 1
            
print_alpha_blocks(table)
