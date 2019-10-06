import time
import tkinter as tk
from core.pulsed_trigger import Pulsed_Trigger
from gui.application import Application
from gui.window import Window


def on_click():
    print("clicked")


class Test_Triggered:
    def __init__(self):
        self._counter = 0
        self._t0 = time.perf_counter()
        self._n = 5
        self._fps = None

    def on_next_frame(self):
        self._counter += 1
        if self._counter % self._n == 0:
            t = time.perf_counter()
            self._fps = float(self._n) / (t - self._t0)
            self._t0 = t
            print(
                "frame_nr = " + str(self._counter) + " fps = " + str(self._fps)
            )


def main():
    application = Application(max_fps=60)
    window = Window(application, title="A", x=100, y=100, width=150, height=150)
    button = tk.Button(window._toplevel, text="text", command=on_click)
    button.grid()
    triggered = Test_Triggered()
    application.get_next_frame_trigger().register(
        triggered, Test_Triggered.on_next_frame
    )
    application.run()
    application.get_next_frame_trigger().unregister(triggered)


if __name__ == "__main__":
    main()
