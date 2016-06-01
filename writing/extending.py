from drawings import preamble, postamble, draw_square, draw_tetromino

if __name__ == '__main__':
    preamble()

    single_squares = [(0,0), (0,1), (1,0), (17, 17)]
    for (x, y) in single_squares:
        draw_square(x, y)
        
    tetrominos = [(2.5, 1.5, 0), (16.5, 0.5, 2), (17.5, 2.5, 1), (16.5, 16.5, 3)]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    
    ghost_tetrominos = [
        (6.5, 1.5, 0), (4.5, 0.5, 2),
        (14.5, 1.5, 0), (12.5, 0.5, 2),
        (17.5, 6.5, 1), (16.5, 4.5, 3),
        (17.5, 14.5, 1), (16.5, 12.5, 3)
    ]
    for x, y, t in ghost_tetrominos:
        draw_tetromino(x, y, t, ['dashed'])

    draw_square(0, 2, 16, ['pattern = north east lines'])

    postamble()
