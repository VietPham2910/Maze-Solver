from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height
        self.__running = False

        self.__root = Tk()
        self.__root.title("Root widget")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas()
        self.__canvas.pack()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        
    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color):
        line.draw(self.__canvas, fill_color)