import random
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
        seed=None,
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

        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visted()

    def _create_cells(self):
        for _ in range(self._num_rows):
            row = []
            for _ in range(self._num_cols):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j) :
        self._cells[i][j].draw(j*self._cell_size_x + self._x1, 
                               i*self._cell_size_y + self._y1, 
                               (j+1)*self._cell_size_x + self._x1, 
                               (i+1)*self._cell_size_y + self._y1)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_rows - 1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_rows - 1, self._num_cols-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            adjacent_list = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
            possible_directions = []

            for neighbor in adjacent_list:
                if (neighbor[0] >= 0 and neighbor[1] >= 0
                    and neighbor[0] <= self._num_rows - 1 
                    and neighbor[1] <= self._num_cols - 1
                    and self._cells[neighbor[0]][neighbor[1]].visited == False
                ):
                    possible_directions.append(neighbor)
            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            
            next_direction = possible_directions[random.randint(0, len(possible_directions)-1)]
            if next_direction[0] == i:
                if next_direction[1] == j - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i][j-1].has_right_wall = False
                else:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i][j+1].has_left_wall = False
            else:
                if next_direction[0] == i - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i-1][j].has_bottom_wall = False
                else:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i+1][j].has_top_wall = False
            self._break_walls_r(next_direction[0], next_direction[1])

    def _reset_cells_visted(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
    
    # returns True if this is the end cell, OR if it leads to the end cell.
    # returns False if this is a loser cell.
    def _solve_r(self, i, j):
        self._animate()

        # vist the current cell
        self._cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i][j-1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        # move right if there is no wall and it hasn't been visited
        if (
            j < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i][j+1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        # move up if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        # move down if there is no wall and it hasn't been visited
        if (
            i < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        # we went the wrong way let the previous cell know by returning False
        return False

    # create the moves for the solution using a depth first search
    def solve(self):
        return self._solve_r(0, 0)

            


                



