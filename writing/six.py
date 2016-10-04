from drawings import preamble, postamble, draw_square, draw_tetromino

if __name__ == '__main__':
    preamble()

    single_squares = [(0,0), (0,1), (1,0), (5, 5)]
    for (x, y) in single_squares:
        draw_square(x, y)
        
    tetrominos = [(2.5, 1.5, 0), (4.5, 0.5, 2), (5.5, 2.5, 1), (4.5, 4.5, 3)]
    for x, y, t in tetrominos:
        draw_tetromino(x, y, t)
    
    draw_square(0, 2, 4, ['pattern = north east lines'])

    postamble()
