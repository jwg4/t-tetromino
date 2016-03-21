
def preamble():
    print r'''
\begin{tikzpicture}
'''

def postamble():
    print r'''
\end{tikzpicture}
'''

def draw_square(x, y):
    offsets = [(0, 0.5), (0, 1), (1, 1), (1, 0), (0, 0), (0, 0.5)]
    points = [ (x + a, y + b) for a, b in offsets ]
    path = ' -- '.join([ '(%f, %f)' % p for p in points ])
    print r'''
\draw [rounded corners, thick] %s;
''' % (path, )

if __name__ == '__main__':
    preamble()

    single_squares = [(0,0), (0,1), (1,0)]
    for (x, y) in single_squares:
        draw_square(x, y)
        
    postamble()
