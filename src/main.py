from draw import Line, Point
from window import Window


def main():
    win = Window(800, 600)

    p1 = Point(100, 100)
    p2 = Point(200, 200)

    line = Line(p1, p2)
    win.draw_line(line, "red")

    win.wait_for_close()


main()
