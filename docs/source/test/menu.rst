#######
menu.py
#######

依存関係
========
.. code-block:: python

    from tkinter import filedialog
    from PIL import ImageTk

    import tkinter as tk

class Menu
==========

.. code-block:: python

    class Menu:
        def __init__(self):
            self.menu_bar = None
            self.file = None

create_menu(self, root, canvas_class)
-------------------------------------
| メニューウィジェットを作成する

.. code-block:: python

    
    def create_menu(self, root, canvas_class):
        self.menu_bar = tk.Menu(root)
        root.config(menu = self.menu_bar)
        self.file = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label = "File", menu = self.file)
        self.file.add_command(
            label = "New File",
            command = lambda: canvas_class.new_canvas()
        )
        self.file.add_command(
            label = "Open Image",
            command = lambda: self.open_image(canvas_class)
        )
        self.file.add_command(
            label = "Save as ...",
            command = lambda: self.file_save_as(canvas_class)
        )
        self.file.add_separator()
        self.file.add_command(
            label = "Exit",
            command = lambda: self.exit_app(root)
        )

open_image(self, canvas_class, event = None)
--------------------------------------------
| 画像を読み込む

.. code-block:: python

    def open_image(self, canvas_class, event = None):
        file_name = filedialog.askopenfilename(
            title = "Open file",
            defaultextension = '.png'
        )
        img = ImageTk.PhotoImage(file = file_name)
        canvas_class.open_image_on_canvas(img)

file_save_as(self, canvas_class, event = None)
----------------------------------------------
| 名前を付けて保存

.. code-block:: python

    def file_save_as(self, canvas_class, event = None):
        file_name = filedialog.asksaveasfilename(
            title = "Save with filename",
            filetypes=[("PNG Image Files",".png")],
            defaultextension = '.png'
        )
        png=[]
        canvas_class.save_file(file_name)

exit_app(self, root)
--------------------
| アプリケーションを終了する

.. code-block:: python

    def exit_app(self, root):
        root.destroy()