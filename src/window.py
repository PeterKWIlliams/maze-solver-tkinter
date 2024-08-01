from tkinter import BOTH, Canvas, Tk

from .draw import Line, Point


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("My Window")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed successfully")

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        p1, p2, p3, p4 = Point(x1, y1), Point(x2, y2), Point(x1, y2), Point(x2, y1)
        if self.has_left_wall:
            self._win.draw_line(Line(p1, p3), "red")
        else:
            self._win.draw_line(Line(p1, p3), "white")
        if self.has_right_wall:
            self._win.draw_line(Line(p2, p4), "red")
        else:
            self._win.draw_line(Line(p2, p4), "white")
        if self.has_bottom_wall:
            self._win.draw_line(Line(p3, p2), "red")
        else:
            self._win.draw_line(Line(p3, p2), "white")
        if self.has_top_wall:
            self._win.draw_line(Line(p1, p4), "red")
        else:
            self._win.draw_line(Line(p1, p4), "white")

    def redraw(self):
        self.draw(self._x1, self._y1, self._x2, self._y2)

    def get_centre(self):
        if self._x1 is None or self._y1 is None or self._x2 is None or self._y2 is None:
            return None
        return ((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, to_cell, undo=False):
        color = "red" if undo else "gray"
        centre_1, centre_2 = to_cell.get_centre(), self.get_centre()

        if centre_1 and centre_2:
            p1, p2 = Point(centre_1[0], centre_1[1]), Point(centre_2[0], centre_2[1])
            self._win.draw_line(Line(p1, p2), color)
        else:
            print("could not draw move: invalid cell centers")
