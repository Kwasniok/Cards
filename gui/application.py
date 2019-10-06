import tkinter as tk
from core.pulsed_trigger import Pulsed_Trigger
from .root import Root
from .window import Window


class Application:
    def __init__(self, max_fps=60):
        Root.register_application(self)
        self._tk_root = Root.get_root()
        self._windows = []
        self._next_frame_trigger = Pulsed_Trigger(
            max_pps=max_fps, starts_stopped=True
        )

    def destroy_all_windows(self):
        for window in self._windows:
            window.destroy()
        self._windows = []

    def destroy(self):
        self.destroy_all_windows()
        Root.unregister_application()

    def get_tk_root(self):
        return self._tk_root

    def get_next_frame_trigger(self):
        return self._next_frame_trigger

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
        self._next_frame_trigger.restart()
        # main loop
        while len(self._windows) > 0:
            # update all components
            Pulsed_Trigger.update_all()
            self._tk_root.update_idletasks()
            self._tk_root.update()
        self._next_frame_trigger.stop()

    def quit(self):
        self._next_frame_trigger.stop()
        for window in self._windows:
            window.close()
