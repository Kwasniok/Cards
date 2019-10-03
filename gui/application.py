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
            window.destroy()
        self._windows = []

    def destroy(self):
        self.destroy_all_windows()
        Root.unregister_application()

    def get_master(self):
        return self._master

    def register_window(self, window):
        self._windows.append(window)

    def unregister_window(self, window):
        if window in self._windows:
            self._windows.remove(window)

    def run(self):
        self._master.mainloop()