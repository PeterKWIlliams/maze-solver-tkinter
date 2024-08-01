import time

from .window import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cell_list = []

        self._create_cells()

    def _create_cells(self):
        self._cell_list.extend(
            [
                [Cell(self._win) for i in range(self._num_rows)]
                for j in range(self._num_cols)
            ]
        )
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1, y1 = self._x1 + self._cell_size_x * i, self._y1 + self._cell_size_y * j
        x2, y2 = x1 + self._cell_size_x, y1 + self._cell_size_y
        self._cell_list[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell, exit_cell = self._cell_list[0][0], self._cell_list[-1][-1]
        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        entrance_cell.redraw()
        exit_cell.redraw()
