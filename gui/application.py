import tkinter as tk
from .root import Root
from .window import Window


class Application:
    def __init__(self):
        Root.register_application(self)
        self._master = Root.get_root()
        self._windows = []

    def destroy_all_windows(self):
        for window in self._windows:
            self.destroy_window(window)

    def destroy(self):
        self.destroy_all_windows()
        Root.unregister_application()

    def get_master(self):
        return self._master

    def new_window(self, title, width, height, x, y):
        window = Window(self, title=title, width=width, height=height, x=x, y=y)
        self._windows.append(window)
        return window

    def destroy_window(self, window):
        if window in self._windows:
            window.destroy()
            self._windows.remove(window)
        else:
            raise (ValueError("Cannot destroy unregistered window."))

    def run(self):
        self._master.mainloop()
