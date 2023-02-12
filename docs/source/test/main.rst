#################
main.py
#################

main文、Applicationクラスを定義して走らせているだけである。

.. code-block:: python

    # -*- coding: utf-8 -*-
    from application import Application

    def main():
        app = Application()
        app.run()

    if __name__ == "__main__":
        main()
