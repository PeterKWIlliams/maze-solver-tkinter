import unittest

import test_helper

from src.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cell_list),
            num_rows,
        )
        self.assertEqual(
            len(m1._cell_list[0]),
            num_cols,
        )

    def test_draw_cell(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        cell1 = m1._cell_list[0][0]
        cell2 = m1._cell_list[2][3]

        self.assertEqual(cell2._x1, 30)
        self.assertEqual(cell2._y1, 20)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cell_list[0][0].has_top_wall, False)
        self.assertEqual(m1._cell_list[-1][-1].has_bottom_wall, False)

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cell_list[0][0].visited, False)
        m1._cell_list[0][0].visited = True
        m1._reset_cells_visited()
        self.assertEqual(m1._cell_list[0][0].visited, False)


if __name__ == "__main__":
    unittest.main()
