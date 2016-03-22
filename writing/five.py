from drawings import preamble, postamble, draw_cropped_square, draw_tetromino

if __name__ == '__main__':
    preamble()
    draw_cropped_square(0, 0, 5)
    tetrominos = [(0.5, 3.5, 3), (2.5, 4.5, 0), (2.5, 1.5, 1), (3.5, 1.5, 3), (4.5, 3.5, 1)]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    postamble()
