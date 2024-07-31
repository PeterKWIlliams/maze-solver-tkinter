from draw import Line, Point
from window import Cell, Window


def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell2 = Cell(win)
    cell.has_left_wall = True
    cell.has_right_wall = True
    cell.has_top_wall = True
    cell.has_bottom_wall = True
    cell.draw(10, 10, 20, 20)
    cell2.draw(50, 50, 60, 60)
    cell.draw_move(cell2)

    win.wait_for_close()


main()
