from .point import Point
from tkinter import Canvas

class Line:
    def __init__(self, begin:Point, end:Point) -> None:
        self.__begin = begin
        self.__end = end

    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(self.__begin.x, self.__begin.y, self.__end.x, self.__end.y, fill=fill_color, width=2)