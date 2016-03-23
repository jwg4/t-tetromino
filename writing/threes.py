from drawings import preamble, postamble, draw_cropped_square, draw_tetromino

if __name__ == '__main__':
    preamble()
    draw_cropped_square(0, 2, 7)
    tetrominos = [
        (0.5, 2.5, 3), (1.5, 0.5, 2),
        (7.5, 1.5, 0), (7.5, 2.5, 2),
    ]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    ghost_tetrominos = [
        (3.5, 1.5, 0), (5.5, 0.5, 2),
        (8.5, 4.5, 1), (7.5, 6.5, 3),
    ]
    for x, y, t in ghost_tetrominos:
        draw_tetromino(x, y, t, ['dashed'])
    postamble()
