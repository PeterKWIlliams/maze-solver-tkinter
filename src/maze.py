import random
import time

from .window import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cell_list = []
        self.seed = 0 if seed is None else random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cell_list.extend(
            [
                [Cell(self._win) for i in range(self._num_cols)]
                for j in range(self._num_rows)
            ]
        )
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1, y1 = self._x1 + self._cell_size_x * j, self._y1 + self._cell_size_y * i
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

    def _break_walls_r(self, i, j):
        self._cell_list[i][j].visited = True
        while True:
            to_visit = []
            if i + 1 < self._num_rows and self._cell_list[i + 1][j].visited is False:
                to_visit.append((i + 1, j))
            if i - 1 >= 0 and self._cell_list[i - 1][j].visited is False:
                to_visit.append((i - 1, j))
            if j + 1 < self._num_cols and self._cell_list[i][j + 1].visited is False:
                to_visit.append((i, j + 1))
            if j - 1 >= 0 and self._cell_list[i][j - 1].visited is False:
                to_visit.append((i, j - 1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            random.shuffle(to_visit)
            k, l = to_visit[0]

            if k == i + 1:
                self._cell_list[i][j].has_bottom_wall = False
                self._cell_list[i + 1][j].has_top_wall = False
                self._cell_list[i][j].redraw()
                self._cell_list[i + 1][j].redraw()
            if k == i - 1:
                self._cell_list[i][j].has_top_wall = False
                self._cell_list[i - 1][j].has_bottom_wall = False
                self._cell_list[i][j].redraw()
                self._cell_list[i - 1][j].redraw()
            if l == j + 1:
                self._cell_list[i][j].has_right_wall = False
                self._cell_list[i][j + 1].has_left_wall = False
                self._cell_list[i][j].redraw()
                self._cell_list[i][j + 1].redraw()
            if l == j - 1:
                self._cell_list[i][j].has_left_wall = False
                self._cell_list[i][j - 1].has_right_wall = False
                self._cell_list[i][j].redraw()
                self._cell_list[i][j - 1].redraw()
            self._break_walls_r(k, l)

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cell_list[i][j].visited = False

    def _solve_r(self, i=0, j=0):
        self._animate()
        self._cell_list[i][j].visited = True
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True

        if (
            i + 1 < self._num_rows
            and self._cell_list[i + 1][j].visited is False
            and self._cell_list[i + 1][j].has_top_wall is False
            and self._cell_list[i][j].has_bottom_wall is False
        ):
            self._cell_list[i][j].draw_move(self._cell_list[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cell_list[i + 1][j].draw_move(self._cell_list[i][j], undo=True)

        if (
            i - 1 >= 0
            and self._cell_list[i - 1][j].visited is False
            and self._cell_list[i][j].has_top_wall is False
            and self._cell_list[i - 1][j].has_bottom_wall is False
        ):
            self._cell_list[i][j].draw_move(self._cell_list[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cell_list[i - 1][j].draw_move(self._cell_list[i][j], undo=True)

        if (
            j - 1 >= 0
            and self._cell_list[i][j - 1].visited is False
            and self._cell_list[i][j].has_left_wall is False
            and self._cell_list[i][j - 1].has_right_wall is False
        ):

            self._cell_list[i][j].draw_move(self._cell_list[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cell_list[i][j - 1].draw_move(self._cell_list[i][j], undo=True)
        if (
            j + 1 < self._num_cols
            and self._cell_list[i][j + 1].visited is False
            and self._cell_list[i][j].has_right_wall is False
            and self._cell_list[i][j + 1].has_left_wall is False
        ):
            self._cell_list[i][j].draw_move(self._cell_list[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cell_list[i][j + 1].draw_move(self._cell_list[i][j], undo=True)
        return False
