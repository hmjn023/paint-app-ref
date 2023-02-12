###############
application.py
###############

依存関係
========

.. code-block:: python
    
    import tkinter as tk

    from menu import Menu
    from canvas import Canvas
    from tool import Tool


class Application
=================
| クラスのプロパティと初期化

.. code-block:: python

    class Application:
        def __init__(self):
            self.root = None
            self.menu = None
            self.canvas = None
            self.tool = None

run(self)
---------

| ウィンドウ、ウィジェットの作成をし、動作開始する

.. code-block:: python

    def run(self):
        self.create_main_window()
        self.create_widgits()
        self.root.mainloop()

create_main_window(self)
------------------------

| tkinterのrootクラスを取得し、アプリケーションとして成立する。

.. code-block:: python

    def create_main_window(self):
        self.root = tk.Tk()
        self.root.title('paint-app')
        self.root.attributes('-zoomed', '1')

create_widgits(self)
--------------------

| 各種クラスをプロパティとして定義することで、各種制御を行えるようにする

.. code-block:: python

    def create_widgits(self):
        self.menu = Menu()
        self.canvas = Canvas()
        self.tool = Tool()

        self.canvas.create_canvas(self.root)
        self.menu.create_menu(self.root, self.canvas)
        self.tool.create_tool(self.root)