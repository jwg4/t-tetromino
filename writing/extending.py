from drawings import preamble, postamble, draw_tetromino, draw_rectangle

if __name__ == '__main__':
    preamble()

    tetrominos = [(2.5, 1.5, 0), (16.5, 0.5, 2), (17.5, 2.5, 1), (16.5, 16.5, 3)]
    for x, y, t in tetrominos:
        pass
        #draw_tetromino(x, y, t)
    
    ghost_tetrominos = [
        (6.5, 1.5, 0), (4.5, 0.5, 2),
        (14.5, 1.5, 0), (12.5, 0.5, 2),
        (17.5, 6.5, 1), (16.5, 4.5, 3),
        (17.5, 14.5, 1), (16.5, 12.5, 3)
    ]
    for x, y, t in ghost_tetrominos:
        pass
        #draw_tetromino(x, y, t, ['dashed'])

    draw_rectangle(0, 2, 5, 7, ['pattern = north east lines'])

    postamble()
