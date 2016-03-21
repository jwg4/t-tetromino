EPSILON = 0.07

SQUARE_OFFSETS = [
    (EPSILON, 0.5),
    (EPSILON, 1 - EPSILON),
    (1 - EPSILON, 1 - EPSILON),
    (1 - EPSILON, EPSILON),
    (EPSILON, EPSILON),
    (EPSILON, 0.5)
]
TETROMINO_OFFSETS = [
    (0, 0.5 - EPSILON),
    (1.5 - EPSILON, 0.5 - EPSILON),
    (1.5 - EPSILON, -0.5 + EPSILON),
    (0.5 - EPSILON, -0.5 + EPSILON),
    (0.5 - EPSILON, -1.5 + EPSILON),
    (-0.5 + EPSILON, -1.5 + EPSILON),
    (-0.5 + EPSILON, -0.5 + EPSILON),
    (-1.5 + EPSILON, -0.5 + EPSILON),
    (-1.5 + EPSILON, 0.5 - EPSILON),
    (0, 0.5 - EPSILON)
]
ROTATION_MATRICES = [(1, 0, 0, 1), (0, 1, -1, 0), (-1, 0, 0, -1), (0, -1, 1, 0)]

def translate(l, x, y):
    return [ (x + a, y + b) for a, b in l ]

def rotate(l, t):
    r = ROTATION_MATRICES[t]
    rotated = [(ax * r[0] + ay * r[1], ax * r[2] + ay * r[3]) for ax, ay in l ]
    return rotated

def print_path(points, extras=[]):
    path = ' -- '.join([ '(%f, %f)' % p for p in points ])
    extra_code = ', '.join([''] + extras) if extras else ''
    print r'''
\draw [rounded corners, ultra thick %s] %s;
''' % (extra_code, path)

def preamble():
    print r'''
\begin{tikzpicture}
'''

def postamble():
    print r'''
\end{tikzpicture}
'''

def draw_tetromino(x, y, t, extras=[]):
    rotated = rotate(TETROMINO_OFFSETS, t)
    points = translate(rotated, x, y)
    print_path(points, extras)

def draw_square(x, y, scale=1, extras=[]):
    offsets = [ (a * scale, b * scale) for a, b in SQUARE_OFFSETS ]
    points = translate(offsets, x, y)
    print_path(points, extras)

if __name__ == '__main__':
    preamble()

    single_squares = [(0,0), (0,1), (1,0), (9, 9)]
    for (x, y) in single_squares:
        draw_square(x, y)
        
    tetrominos = [(2.5, 1.5, 0), (8.5, 0.5, 2), (9.5, 2.5, 1), (8.5, 8.5, 3)]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    
    ghost_tetrominos = [(6.5, 1.5, 0), (4.5, 0.5, 2), (9.5, 6.5, 1), (8.5, 4.5, 3)]
    for x, y, t in ghost_tetrominos:
        draw_tetromino(x, y, t, ['dashed'])

    draw_square(0, 2, 8, ['pattern = north east lines'])

    postamble()
