#######
tool.py
#######

依存関係
========

.. code-block:: python

    from enum import Enum

    import tkinter as tk

class Tool
==========

.. code-block:: python

    class Tool:
        mode = None
        color = "black"
        thickness = 5

        def __init__(self):
            self.f_tool = None
            self.w_b_pen = None
            self.w_thickbar = None
            
            self.img_pen = tk.PhotoImage(file = "images/pen_icon.png")
            self.img_eraser = tk.PhotoImage(file = "images/eraser_icon.png")
            Tool.thickness = tk.IntVar()

create_tool(self, root)
-----------------------
| フレーム、ウィジェットを作成している

.. code-block:: python

    def create_tool(self, root):
        self.create_frame(root)
        self.create_widgits()

create_frame(self, root)
------------------------
| フレームを作成している

.. code-block:: python

    def create_frame(self, root):
        self.f_tool = tk.Frame(root, bg = "#FFFF99", pady = 10, padx = 10)
        self.f_tool.place(
            relx = 0.7, rely = 0.0,
            relwidth = 0.3, relheight = 0.6
        )

create_widgits(self)
--------------------
| ウィジェットの定義をしている
| ここでペン、消しゴム、太さ調整のバーの定義をしている

.. code-block:: python

    def create_widgits(self):
        self.w_b_pen = tk.Button(
            self.f_tool,
            text = "Pen",
            image = self.img_pen,
            command = lambda: self.on_button_click(Mode.PEN)
        )
        self.w_b_eraser = tk.Button(
            self.f_tool,
            text = "Eraser",
            image = self.img_eraser,
            command = lambda: self.on_button_click(Mode.ERASER)
        )
        self.w_thickbar = tk.Scale(
            self.f_tool,
            orient = tk.HORIZONTAL,
            from_ = 1,
            to = 30,
            variable = Tool.thickness,
            label = "Thickness"
        )

        self.w_b_pen.pack(side = tk.TOP)
        self.w_b_eraser.pack(side = tk.TOP)
        self.w_thickbar.pack(side = tk.TOP)

on_button_click(self, mode)
---------------------------
| 各種ボタンを押したときのモードの切り替わりを制御

.. code-block:: python

    def on_button_click(self, mode):
        self.mode = mode

        if mode == Mode.PEN:
            Tool.mode = Mode.PEN
            Tool.color = "black"
            self.w_b_pen["state"] = tk.DISABLED
            self.w_b_eraser["state"] = tk.NORMAL
        elif mode == Mode.ERASER:
            Tool.mode = Mode.ERASER
            Tool.color = "white"
            self.w_b_eraser["state"] = tk.DISABLED
            self.w_b_pen["state"] = tk.NORMAL
        else:
            print("Argue Error")


class Mode(Enum)
================
| モードを管理するためのクラス

.. code-block:: python

    class Mode(Enum):
        NONE = 0
        PEN = 1
        ERASER = 2