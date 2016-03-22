from drawings import preamble, postamble, draw_cropped_square, draw_tetromino

if __name__ == '__main__':
    preamble()
    draw_cropped_square(0, 0, 5)
    tetrominos = [(0.5, 3.5, 3)]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    postamble()
