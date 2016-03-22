EPSILON = 0.02

SQUARE_OFFSETS = [
    (0, 0.5),
    (0, 1),
    (1, 1),
    (1, 0),
    (0, 0),
    (0, 0.5)
]

SQUARE_EPSILONS = [
    (EPSILON, 0),
    (EPSILON, -EPSILON),
    (-EPSILON, -EPSILON),
    (-EPSILON, EPSILON),
    (EPSILON, EPSILON),
    (EPSILON, 0)
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
\begin{tikzpicture}[scale=0.5]
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
    offsets = [ (sq[0] * scale + ep[0], sq[1] * scale + ep[1]) for sq, ep in zip(SQUARE_OFFSETS, SQUARE_EPSILONS) ]
    points = translate(offsets, x, y)
    print_path(points, extras)

