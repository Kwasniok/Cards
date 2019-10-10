import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
import game.directions as directions


class Dice_Viewer:
    def __init__(self, window, dice, direction):
        possible_directions = (directions.LEFT, directions.RIGHT)
        if not (direction in possible_directions):
            raise (
                ValueError(
                    "Cannot create dice viewer: Direction "
                    + str(direction)
                    + " must be in "
                    + str(possible_directions)
                    + "."
                )
            )
        self._window = window
        self._dice = dice
        self._direction = direction
        self._dice_button = None

    def destroy(self):
        self._destroy_button()

    def _destroy_button(self):
        safe_destroy(self._dice_button)

    def on_update(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear button
        self._destroy_button()

        # create button
        offset_x = int(width * 0.9)
        button_width = 100
        button_height = 100
        y = int(height / 2)
        if self._direction == directions.LEFT:
            x = offset_x - int(button_width / 2)
        if self._direction == directions.RIGHT:
            x = offset_x + int(button_width / 2)
        symbol = self._dice.get_name()
        symbol += "\n" + str(self._dice.get_last_outcome())

        self._dice_button = tk.Button(
            self._window.get_tk_toplevel(),
            text=symbol,
            command=lambda dice=self._dice: print("clicked on " + str(dice)),
        )
        self._dice_button.place(
            anchor=tk.CENTER, x=x, y=y, width=button_width, height=button_height
        )
