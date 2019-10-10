import tkinter as tk
import tkinter.font as tkfont
import game.directions as directions


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
        self._player_button = None

    def destroy(self):
        self._destroy_button()

    def _destroy_button(self):
        if not (self._player_button is None):
            self._player_button.destroy()
            self._player_button = None

    def on_update(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear button
        self._destroy_button()

        # create button
        text_offset = 5
        hand_zone_heigt = int(height * 0.45)
        button_width = 100
        button_height = 100
        x = text_offset + int(button_width / 2)
        y = hand_zone_heigt / 2
        if self._direction == directions.DOWN:
            y = height - y
        symbol = self._player.get_name()
        symbol += "(" + self._player.get_color() + ")"
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

        self._player_button = tk.Button(
            self._window.get_tk_toplevel(),
            text=symbol,
            command=lambda player=self._player: print(
                "clicked on " + repr(player)
            ),
        )
        self._player_button.place(
            anchor=tk.CENTER, x=x, y=y, width=button_width, height=button_height
        )