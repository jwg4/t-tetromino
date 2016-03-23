from drawings import preamble, postamble, draw_cropped_square, draw_tetromino

if __name__ == '__main__':
    preamble()
    draw_cropped_square(2, 2, 9)
    tetrominos = [
        (1.5, 9.5, 1), (0.5, 3.5, 3),
        (2.5, 2.5, 2), (2.5, 1.5, 0), 
        (8.5, 0.5, 2), (10.5, 1.5, 1), 
    ]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    ghost_tetrominos = [
        (0.5, 7.5, 3), (1.5, 5.5, 1),
        (4.5, 0.5, 2), (6.5, 1.5, 0),
    ]
    for x, y, t in ghost_tetrominos:
        draw_tetromino(x, y, t, ['dashed'])
    postamble()
