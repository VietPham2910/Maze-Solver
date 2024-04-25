from graphics import *
from maze import Maze

win = Window(800, 600)
maze = Maze(20, 20, 10, 10, 50, 50, win=win)
maze.solve()
win.wait_for_close()
