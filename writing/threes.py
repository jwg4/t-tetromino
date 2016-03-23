from drawings import preamble, postamble, draw_cropped_square, draw_tetromino

if __name__ == '__main__':
    preamble()
    draw_cropped_square(2, 0, 11)
    tetrominos = [
        (2.5, 0.5, 1)
    ]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    ghost_tetrominos = [
    ]
    for x, y, t in ghost_tetrominos:
        draw_tetromino(x, y, t, ['dashed'])
    postamble()
