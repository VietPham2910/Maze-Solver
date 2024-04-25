from graphics import *

class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            left = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left)
        else:
            left = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left, "white")
        if self.has_top_wall:
            top = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top)
        else:
            top = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top, "white")
        if self.has_right_wall:
            right = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right)
        else:
            right = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right, "white")
        if self.has_bottom_wall:
            bottom = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom)
        else:
            bottom = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom, "white")

    def draw_move(self, to_cell, undo=False):
        begin = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        end = Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        line = Line(begin, end)
        if undo:
            self._win.draw_line(line,"gray")
        else:
            self._win.draw_line(line,"red")