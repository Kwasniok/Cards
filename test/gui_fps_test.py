import time
import tkinter as tk
from gui.application import Application
from gui.update import Updatable
from gui.window import Window


def on_click():
    print("clicked")


class Test_Updatable(Updatable):
    def __init__(self):
        Updatable.__init__(self)
        self._counter = 0
        self._t0 = time.time()
        self._n = 5
        self._fps = None

    def on_update(self):
        self._counter += 1
        if self._counter % self._n == 0:
            t = time.time()
            self._fps = float(self._n) / (t - self._t0)
            self._t0 = t
        print("frame_nr = " + str(self._counter) + " fps = " + str(self._fps))
        for i in range(100000):
            pass


def main():
    application = Application(max_fps=60)
    window = Window(application, title="A", x=100, y=100, width=150, height=150)
    button = tk.Button(window._toplevel, text="text", command=on_click)
    button.grid()
    updatable = Test_Updatable()
    application.get_frame_updater().register(updatable)
    application.run()
    application.destroy()


if __name__ == "__main__":
    main()
