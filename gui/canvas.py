import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
import core.gui.color as color
from core.gui.util import px_to_pt, pt_to_px


class Canvas:
    def __init__(self, game_window):
        self._game_window = game_window
        self._canvas = tk.Canvas(self._game_window.get_tk_toplevel())
        self._canvas.pack(expand=True, fill=tk.BOTH)  # fill parent
        self._player1_rectangle_id = None
        self._player2_rectangle_id = None
        self._initialize_canvas()

    def destroy(self):
        self._player1_rectangle_id = None
        self._player2_rectangle_id = None
        safe_destroy(self._canvas)
        self._canvas = None

    def _initialize_canvas(self):
        if self._canvas is None:
            return
        # dimensions
        self._canvas.update_idletasks()
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        # draw background
        hand_zone_heigt = int(height * 0.45)
        self._player1_rectangle_id = self._canvas.create_rectangle(
            0,
            0,
            width,
            hand_zone_heigt,
            fill=color.GRAY,
            outline=color.INVISIBLE,
        )
        self._player2_rectangle_id = self._canvas.create_rectangle(
            0,
            height - hand_zone_heigt,
            width,
            height,
            fill=color.GRAY,
            outline=color.INVISIBLE,
        )
