from drawings import preamble, postamble, draw_tetromino, draw_square

def draw_strip(height, length):
    i = 0
    parity = 0
    x = 1.5 
    while i < length:
        y = height + 1.5 - parity
        r = 2 * parity
        extras = ['dashed'] if 0 < i < 3 else []
        yield (x, y, r, extras)
        x = x + 2
        parity = 1 - parity
        i = i + 1
        
if __name__ == '__main__':
    preamble()
    strip1 = list(draw_strip(6, 4))
    strip2 = list(draw_strip(3, 4))
    strip3 = list(draw_strip(0, 5))
    tetrominos = strip1 + strip2 + strip3
    for x, y, t, extras in tetrominos:
        draw_tetromino(x, y, t, extras)
    squares = [(0, 0), (10, 0), (0, 3), (8, 4), (9, 3), (9, 4), (0, 6), (8, 7)] 
    for x, y in squares:
        draw_square(x, y, extras=['pattern = north east lines'])
    postamble()
