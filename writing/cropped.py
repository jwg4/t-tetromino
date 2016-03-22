from drawings import preamble, postamble, draw_cropped_square

if __name__ == '__main__':
    preamble()
    draw_cropped_square(0, 0, 5)
    draw_cropped_square(6, 0, 7)
    draw_cropped_square(14, 0, 9)
    postamble()
