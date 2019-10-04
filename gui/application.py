import tkinter as tk
from .root import Root
from .update import Updater
from .window import Window


class Application:
    def __init__(self):
        Root.register_application(self)
        self._tk_root = Root.get_root()
        self._windows = []
        self._frame_updater = Updater()

    def destroy_all_windows(self):
        for window in self._windows:
            window.destroy()
        self._windows = []

    def destroy(self):
        self._frame_updater.clear()
        self.destroy_all_windows()
        Root.unregister_application()

    def get_tk_root(self):
        return self._tk_root

    def get_frame_updater(self):
        return self._frame_updater

    def register_window(self, window):
        self._windows.append(window)

    def unregister_window(self, window):
        if window in self._windows:
            self._windows.remove(window)

    def run(self):
        if len(self._windows) == 0:
            raise (
                RuntimeError("Application needs at least one window to run.")
            )
        # main loop
        while len(self._windows) > 0:
            self._frame_updater.update_all()
            self._tk_root.update_idletasks()
            self._tk_root.update()

    def quit(self):
        for window in self._windows:
            window.close()
