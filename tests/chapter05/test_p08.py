from chapter05.p08 import draw_line, binary_form


def test_draw_line():
    screen = [0x00, 0x00, 0x00]
    drawn = draw_line(screen, source=3, target=21, width=24, height=0)
    print(binary_form(drawn))
    screen = [0x00, 0x00, 0x00]
    drawn = draw_line(screen, source=3, target=5, width=24, height=0)
    print(binary_form(drawn))
