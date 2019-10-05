import tkinter as tk
from gui.window import Window
from gui.update import Updatable


class Game_Window(Window, Updatable):
    def __init__(self, game_application, x, y):
        width = 512
        height = 512
        Window.__init__(
            self,
            application=game_application,
            title="Game Window",
            width=width,
            height=height,
            x=x,
            y=y,
        )
        Updatable.__init__(self)
        self.make_non_resizable()
        self.center()
        self.set_icon("res/game_icon.gif")
        self._counter = 0
        self._canvas = tk.Canvas(self.get_tk_toplevel())
        self._canvas.pack(expand=True, fill=tk.BOTH)  # fill parent
        self._image = tk.PhotoImage(file="res/test.gif")
        self._image_id = self._canvas.create_image(
            128, 128, anchor=tk.NW, image=self._image
        )

    def destroy(self):
        self._image = None
        self._image_id = None
        self._canvas.destroy()
        self._canvas = None
        Window.destroy(self)

    def on_update(self):
        pass
