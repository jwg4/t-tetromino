from drawings import preamble, postamble, draw_tetromino, draw_rectangle

if __name__ == '__main__':
    preamble()

    tetrominos = [
        (0.5, 1.5, 3), (1.5, 7.5, 1), (0.5, 9.5, 3),
        (8.5, 1.5, 1), (7.5, 7.5, 3), (8.5, 9.5, 1),
    ]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    
    ghost_tetrominos = [
        (1.5, 3.5, 1), (0.5, 5.5, 3),
        (7.5, 3.5, 3), (8.5, 5.5, 1),
    ]
    for x, y, t in ghost_tetrominos:
        draw_tetromino(x, y, t, ['dashed'])

    draw_rectangle(2, 2, 5, 7, ['pattern = north east lines'])

    postamble()
