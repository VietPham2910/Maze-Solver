from graphics import *
from maze import Maze

win = Window(1200, 800)
maze = Maze(20, 20, 10, 10, 50, 50, win)
win.wait_for_close()
