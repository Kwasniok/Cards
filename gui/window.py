import tkinter as tk
from tkinter import messagebox


class Window:
    def __init__(self, application, title, width, height, x, y):
        self._application = application
        self._application.register_window(self)
        self._toplevel = tk.Toplevel(
            self._application.get_master(), width=width, height=height
        )
        self._toplevel.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self._toplevel.title(title)
        self._toplevel.protocol("WM_DELETE_WINDOW", lambda: self.at_quit())

    def destroy(self):
        self._application.unregister_window(self)
        if not (self._toplevel is None):
            self._toplevel.destroy()
            self._toplevel = None

    def quit(self):
        self.destroy()

    def at_quit(self):
        if messagebox.askokcancel(
            "Quit Window", "Do you want to quit this window?"
        ):
            self.quit()
