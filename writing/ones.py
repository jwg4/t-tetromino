from drawings import preamble, postamble, draw_cropped_square, draw_tetromino

if __name__ == '__main__':
    preamble()
    draw_cropped_square(2, 2, 9)
    tetrominos = [(1.5, 9.5, 1), (0.5, 7.5, 3), (1.5, 5.5, 1), (0.5, 3.5, 3)]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    postamble()
