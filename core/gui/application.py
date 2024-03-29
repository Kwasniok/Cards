import time
import tkinter as tk
from core.pulsed_trigger import Pulsed_Trigger
from .root import Root
from .window import Window


class Application:
    def __init__(self, max_fps=60):
        Root.register_application(self)
        self._tk_root = Root.get_root()
        self._windows = []
        self._max_fps = max_fps
        self._next_frame_trigger = Pulsed_Trigger(
            max_pps=max_fps, starts_stopped=True
        )

    def destroy_all_windows(self):
        for window in self._windows:
            window.destroy()
        self._windows = []

    def destroy(self):
        self._next_frame_trigger.stop()
        self.destroy_all_windows()
        Root.unregister_application()

    def get_tk_root(self):
        return self._tk_root

    def get_next_frame_trigger(self):
        return self._next_frame_trigger

    def register_window(self, window):
        self._windows.append(window)
        self._next_frame_trigger.register(window, "on_next_frame")

    def unregister_window(self, window):
        if window in self._windows:
            self._windows.remove(window)
        self._next_frame_trigger.unregister(window)  # safe; so not in if clause

    def run(self):
        if len(self._windows) == 0:
            raise (
                RuntimeError("Application needs at least one window to run.")
            )
        self._next_frame_trigger.restart()
        # main loop
        next_update_time = time.perf_counter()
        while len(self._windows) > 0:
            current_time = time.perf_counter()
            if current_time > next_update_time:
                # update all components
                while current_time > next_update_time:
                    next_update_time += 1.0 / self._max_fps
                Pulsed_Trigger.update_all()
                self._tk_root.update_idletasks()
                self._tk_root.update()
            else:
                time.sleep(next_update_time - current_time)
        self._next_frame_trigger.stop()

    def quit(self):
        self._next_frame_trigger.stop()
        for window in self._windows:
            window.close()
