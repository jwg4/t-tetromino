SQUARE_OFFSETS = [(0, 0.5), (0, 1), (1, 1), (1, 0), (0, 0), (0, 0.5)]

def translate(l, x, y):
    return [ (x + a, y + b) for a, b in l ]

def print_path(points, extra=''):
    path = ' -- '.join([ '(%f, %f)' % p for p in points ])
    print r'''
\draw [rounded corners, thick %s] %s;
''' % (extra, path)

def preamble():
    print r'''
\begin{tikzpicture}
'''

def postamble():
    print r'''
\end{tikzpicture}
'''

def draw_tetromino(x, y, t):
    offsets = [(0, 0.5), (1.5, 0.5), (1.5, -0.5), (0.5, -0.5), (0.5, -1.5), (-0.5, -1.5), (-0.5, -0.5), (-1.5, -0.5), (-1.5, 0.5), (0, 0.5)]
    r = [(1, 0, 0, 1), (0, 1, -1, 0), (-1, 0, 0, -1), (0, -1, 1, 0)][t]
    rotated = [(ax * r[0] + ay * r[1], ax * r[2] + ay * r[3]) for ax, ay in offsets ]
    print rotated
    points = [ (x + a, y + b) for a, b in rotated ]
    print points
    path = ' -- '.join([ '(%f, %f)' % p for p in points ])
    print r'''
\draw [rounded corners, thick] %s;
''' % (path, )

def draw_square(x, y, scale=1, extras=[]):
    offsets = [ (a * scale, b * scale) for a, b in SQUARE_OFFSETS ]
    points = translate(offsets, x, y)
    extra_code = ', '.join([''] + extras) if extras else ''
    print_path(points, extra_code)

if __name__ == '__main__':
    preamble()

    single_squares = [(0,0), (0,1), (1,0), (9, 9)]
    for (x, y) in single_squares:
        draw_square(x, y)
        
    tetrominos = [(2.5, 1.5, 0), (8.5, 0.5, 2), (9.5, 2.5, 1), (8.5, 8.5, 3)]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    
    draw_square(0, 2, 8, ['pattern = north east lines'])

    postamble()
