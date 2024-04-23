from window import Window
from line import Line
from point import Point

win = Window(800, 600)
win.draw_line(Line(Point(5,5), Point(5, 50)), "red")
win.wait_for_close()
