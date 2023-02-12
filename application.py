import tkinter as tk

from menu import Menu
from canvas import Canvas
from tool import Tool

class Application:
    def __init__(self):
        self.root = None
        self.menu = None
        self.canvas = None
        self.tool = None
    
    def run(self):
        self.create_main_window()
        self.create_widgits()
        self.root.mainloop()
    
    def create_main_window(self):
        self.root = tk.Tk()
        self.root.title('paint-app')
        self.root.attributes('-zoomed', '1')

    def create_widgits(self):
        self.menu = Menu()
        self.canvas = Canvas()
        self.tool = Tool()

        self.canvas.create_canvas(self.root)
        self.menu.create_menu(self.root, self.canvas)
        self.tool.create_tool(self.root)