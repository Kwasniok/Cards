import tkinter as tk
import tkinter.font as tkfont
import core.gui.color as color
from core.gui.util import px_to_pt, pt_to_px


class Game_Canvas:
    def __init__(self, game_window):
        self._game_window = game_window
        self._canvas = tk.Canvas(self._game_window.get_tk_toplevel())
        self._canvas.pack(expand=True, fill=tk.BOTH)  # fill parent
        self._player1_rectangle_id = None
        self._player2_rectangle_id = None
        self._player1_text_id = None
        self._player2_text_id = None
        self._font = None
        self._initialize_canvas()

    def destroy(self):
        self._player1_rectangle_id = None
        self._player2_rectangle_id = None
        self._player1_text_id = None
        self._player2_text_id = None
        self._font = None
        if not (self._canvas is None):
            self._canvas.destroy()
            self._canvas = None
        self._canvas = None

    def _initialize_canvas(self):
        if self._canvas is None:
            return
        # game_state / state
        game_state = self._game_window.get_application().get_game_state()
        neutral_zone = game_state.get_neutral_zone()
        player1 = game_state.get_player1()
        player2 = game_state.get_player2()
        # dimensions
        self._canvas.update_idletasks()
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        # fonts
        font_size = 30
        if self._font is None:
            self._font = tkfont.Font(
                family="Helvetica", size=px_to_pt(font_size), weight="bold"
            )
        # HACK: create_text does not properly align the text vertically
        internal_text_offset = pt_to_px(self._font.actual()["size"]) / 6
        #
        text_offset = 5
        hand_zone_heigt = int(height * 0.4)
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
        self._player1_text_id = self._canvas.create_text(
            text_offset,
            hand_zone_heigt / 2,
            anchor=tk.W,
            text=player1.get_name(),
            fill=player1.get_color(),
            font=self._font,
        )
        self._player2_text_id = self._canvas.create_text(
            text_offset,
            height - hand_zone_heigt / 2,
            anchor=tk.W,
            text=player2.get_name(),
            fill=player2.get_color(),
            font=self._font,
        )
