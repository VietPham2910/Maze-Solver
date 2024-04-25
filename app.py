from graphics import *
from maze import Maze

win = Window(800, 600)
maze = Maze(20, 20, 10, 10, 50, 50, win=win)
maze._break_walls_r(0, 0)
print("Done breaking walls")
win.wait_for_close()
