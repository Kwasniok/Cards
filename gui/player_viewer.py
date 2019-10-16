import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
import game.directions as directions
from .piece_tray_viewer import Piece_Tray_Viewer


class Player_Viewer:
    def __init__(self, window, player, direction):
        possible_directions = (directions.UP, directions.DOWN)
        if not (direction in possible_directions):
            raise (
                ValueError(
                    "Cannot create player viewer: Direction "
                    + str(direction)
                    + " must be in "
                    + str(possible_directions)
                    + "."
                )
            )
        self._window = window
        self._player = player
        self._direction = direction
        self._player_status_button = None
        self._player_piece_tray_buttons = []

    def destroy(self):
        self._destroy_status_button()
        self._destroy_piece_tray_buttons()

    def _destroy_status_button(self):
        self._player_status_button = safe_destroy(self._player_status_button)

    def _destroy_piece_tray_buttons(self):
        for button in self._player_piece_tray_buttons:
            button.destroy()
        self._player_piece_tray_buttons = []

    def on_update_status_viewer(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear button
        self._destroy_status_button()

        # create button
        text_offset = 5
        hand_zone_heigt = int(height * 0.45)
        button_width = 100
        button_height = 50
        x = text_offset + int(button_width / 2)
        y = hand_zone_heigt / 2
        if self._direction == directions.DOWN:
            y = height - y
        ## player status symbol
        # name
        symbol = self._player.get_name()
        # color
        symbol += "(" + self._player.get_color() + ")"
        # points
        symbol += "\n"
        mp = self._player.get_mill_points(context)
        if mp:
            symbol += " " + str(mp) + "xM"
        kp = self._player.get_knight_points(context)
        if kp:
            symbol += " " + str(kp) + "xK"
        wp = self._player.get_win_points(context)
        if wp:
            symbol += " " + str(wp) + "xW"
        # is active
        if self._player == context.active_player:
            symbol += "\n (active)"

        self._player_status_button = tk.Button(
            self._window.get_tk_toplevel(),
            text=symbol,
            command=lambda player=self._player: self._window.get_interaction_window().add_object(
                player
            ),
        )
        self._player_status_button.place(
            anchor=tk.CENTER, x=x, y=y, width=button_width, height=button_height
        )

    def on_update_piece_tray_viewer(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_piece_tray_buttons()

        # create buttons
        button_width = 80
        button_height = 40
        x = button_width
        y = button_height
        if self._direction == directions.DOWN:
            y = height - y
        self._piece_tray_buttons = Piece_Tray_Viewer.create_buttons(
            context=context,
            window=self._window,
            piece_tray=self._player.get_piece_tray(),
            x=x,
            y=y,
            width=button_width,
            height=button_height,
        )
