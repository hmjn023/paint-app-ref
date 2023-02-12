#########
canvas.py
#########

依存関係
========

.. code-block:: python

    import tkinter as tk

    from tool import Tool,Mode

class Canvas
============

.. code-block:: python

    class Canvas:
        def __init__(self):
            self.f_canvas = None
            self.w_canvas = None
            self.current_id = -1
            self.image = None

create_canvas(self, root)
-------------------------
| キャンバスを作成し、ウィジェットとして動作するようにしている

.. code-block:: python

    def create_canvas(self, root):
        self.create_frame(root)
        self.create_widgits()


create_frame(self, root)
------------------------
| 描画フレームを作成している

.. code-block:: python

    def create_frame(self, root):
        self.f_canvas = tk.Frame(
            root, bg = "#CCFF99", 
            padx = 10, pady = 10
        )
        self.f_canvas.place(
            relx = 0.0, rely = 0.0,
            relwidth = 0.7, relheight = 1.0
        )

create_widgits(self)
--------------------
| ウィジェットを作成している

.. code-block:: python

    def create_widgits(self):
        self.w_canvas = tk.Canvas(self.f_canvas, bg = "white")
        self.w_canvas.place(
            relx = 0.0, rely = 0.1,
            relwidth = 1.0, relheight = 0.8
        )
        self.w_canvas.bind("<Button-1>", self.on_key_left)
        self.w_canvas.bind("<B1-Motion>", self.on_key_left_dragging)

set_mode(self, mode)
--------------------

.. code-block:: python

    def set_mode(self, mode):
        self.mode = mode

on_key_left(self, event)
------------------------
| 左クリックをしたときに動作する関数
| キャンバス上に線を作成

.. code-block:: python

    def on_key_left(self, event):
        if Tool.mode == Mode.PEN or Tool.mode == Mode.ERASER:
            self.current_id = self.w_canvas.create_line(
                event.x, event.y,
                event.x, event.y,
                fill = Tool.color,
                width = Tool.thickness.get()
            )

on_key_left_dragging(self, event)
---------------------------------
| 左クリック長押しをしたときに動作する関数
| キャンバス上に線を作成

.. code-block:: python

    def on_key_left_dragging(self, event):
        points = self.w_canvas.coords(self.current_id)
        points.extend([event.x, event.y])
        self.w_canvas.coords(self.current_id, points)

save_file(self, file_name)
--------------------------
| Canvasの内容をファイルとして保存

.. code-block:: python

        
    def save_file(self, file_name):
        self.w_canvas.postscript(file = file_name, colormode = "color")

open_image_on_canvas(self, img)
-------------------------------
| キャンバス上に画像を読み込む

.. code-block:: python

    def open_image_on_canvas(self, img):
        self.image = img
        self.w_canvas.create_image(
            0, 0, 
            image = self.image,
            anchor = tk.NW
        )

new_canvas(self)
----------------
| 無地の新しいキャンバスに遷移

.. code-block:: python

    def new_canvas(self):
        self.w_canvas.destroy()
        self.create_widgits()

