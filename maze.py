from cell import Cell
from graphics import *
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win:Window = win
        self._cells = []

        self._create_cell()

    def _create_cell(self):
        for _ in range(self._num_rows):
            row = []
            for _ in range(self._num_cols):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()

    def _draw_cell(self, i, j) :
        self._cells[i][j].draw(j*self._cell_size_x + self._x1, 
                               i*self._cell_size_y + self._y1, 
                               (j+1)*self._cell_size_x + self._x1, 
                               (i+1)*self._cell_size_y + self._y1)
        self._animated()
    
    def _animated(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_rows - 1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_rows - 1, self._num_cols-1)