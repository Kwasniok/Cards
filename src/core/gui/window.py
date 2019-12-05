import tkinter as tk
from tkinter import messagebox
from core.destroy import safe_destroy


class Window:
    def __init__(self, application, title, width, height, x, y):
        self._application = application
        self._application.register_window(self)
        self._toplevel = tk.Toplevel(
            self._application.get_tk_root(), width=width, height=height
        )
        self._toplevel.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self._toplevel.title(title)
        self._toplevel.protocol(
            "WM_DELETE_WINDOW", lambda: self.on_close_requested()
        )
        self._icon_image = None

    def destroy(self):
        self._icon_image = None
        self._application.unregister_window(self)
        self._toplevel = safe_destroy(self._toplevel)

    def get_application(self):
        return self._application

    def get_tk_toplevel(self):
        return self._toplevel

    def make_resizable(self):
        self._toplevel.resizable(width=True, height=True)

    def make_non_resizable(self):
        self._toplevel.resizable(width=False, height=False)

    def center(self):
        self._toplevel.update_idletasks()
        width = self._toplevel.winfo_width()
        height = self._toplevel.winfo_height()
        x = (self._toplevel.winfo_screenwidth() - width) / 2
        y = (self._toplevel.winfo_screenheight() - height) / 2
        self._toplevel.geometry("%dx%d+%d+%d" % (width, height, x, y))

    def set_icon(self, image_path):
        self._icon_image = tk.PhotoImage(file=image_path)
        self._toplevel.iconphoto(self._icon_image, self._icon_image)

    def close(self):
        self.destroy()

    def on_close_requested(self):
        if messagebox.askokcancel(
            "Close Window", "Do you want to close this window?"
        ):
            self.close()

    def on_next_frame(self):
        pass
