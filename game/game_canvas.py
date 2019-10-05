import tkinter as tk
import core.color as color
from gui.update import Updatable


class Game_Canvas(Updatable):
    def __init__(self, game_window):
        self._game_window = game_window
        self._canvas = tk.Canvas(self._game_window.get_tk_toplevel())
        self._canvas.pack(expand=True, fill=tk.BOTH)  # fill parent
        self._top_bar_rectangle_id = None
        self._bottom_bar_rectangle_id = None
        self._player1_text_id = None
        self._player2_text_id = None

    def destroy(self):
        self._top_bar_rectangle_id = None
        self._player1_text_id = None
        self._player2_text_id = None
        if not (self._canvas is None):
            self._canvas.destroy()
        self._canvas = None

    def on_update(self):
        game = self._game_window.get_application().get_game()
        game_state = game.get_game_state()
        player1 = game.get_player1()
        player2 = game.get_player2()
        toplevel = self._game_window.get_tk_toplevel()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()
        if self._top_bar_rectangle_id is None:
            self._top_bar_rectangle_id = self._canvas.create_rectangle(
                0, 0, width, 16 + 5, fill=color.GRAY, outline=color.INVISIBLE
            )
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
