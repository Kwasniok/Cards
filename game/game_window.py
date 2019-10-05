import tkinter as tk
import core.color as color
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
        self._top_bar_rectangle_id = None
        self._player1_text_id = None
        self._player2_text_id = None

    def destroy(self):
        self._top_bar_rectangle_id = None
        self._player1_text_id = None
        self._player2_text_id = None
        self._canvas.destroy()
        self._canvas = None
        Window.destroy(self)

    def on_update(self):
        game = self.get_application().get_game()
        game_state = game.get_game_state()
        player1 = game.get_player1()
        player2 = game.get_player2()
        toplevel = self.get_tk_toplevel()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()
        if self._top_bar_rectangle_id is None:
            self._top_bar_rectangle_id = self._canvas.create_rectangle(
                0, 0, width, 16 + 5, fill=color.GRAY, outline=color.INVISIBLE
            )
        if self._player1_text_id is None:
            self._player1_text_id = self._canvas.create_text(
                5, 5, anchor=tk.NW, text=str(player1), fill=player1.color()
            )
        if self._player2_text_id is None:
            self._player2_text_id = self._canvas.create_text(
                width - 5,
                5,
                anchor=tk.NE,
                text=str(player2),
                fill=player2.color(),
            )
