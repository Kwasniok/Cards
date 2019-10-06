import tkinter as tk
from gui.window import Window
from .game_canvas import Game_Canvas


class Game_Window(Window):
    def __init__(self, game_application, x, y):
        width = 1920
        height = 1080
        Window.__init__(
            self,
            application=game_application,
            title="Game Window",
            width=width,
            height=height,
            x=x,
            y=y,
        )
        self.make_non_resizable()
        self.center()
        self.set_icon("res/game_icon.gif")
        self._game_canvas = Game_Canvas(self)

    def destroy(self):
        if not (self._game_canvas is None):
            self._game_canvas.destroy()
            self._game_canvas = None
        Window.destroy(self)
