import tkinter as tk
import tkinter.font as tkfont
import game.directions as directions
from .card_viewer import Card_Viewer


class Hand_Viewer:
    def __init__(self, window, hand, direction):
        possible_directions = (directions.UP, directions.DOWN)
        if not (direction in possible_directions):
            raise (
                ValueError(
                    "Cannot create realm viewer: Direction "
                    + str(direction)
                    + " must be in "
                    + str(possible_directions)
                    + "."
                )
            )
        self._window = window
        self._hand = hand
        self._direction = direction
        self._buttons = []

    def destroy(self):
        self._destroy_buttons()

    def _destroy_buttons(self):
        for button in self._buttons:
            button.destroy()

    def on_update(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_buttons()

        # create buttons
        button_width = 180
        button_height = 50
        button_padding = 10
        columns = self._hand.get_size()
        x_0 = (width - button_width * (columns - 1)) / 2
        y_0 = int(button_height * 0.5)
        if self._direction == directions.DOWN:
            y_0 = height - int(button_height * 0.5)
        for x in range(columns):
            card = self._hand[x]
            self._buttons.append(
                Card_Viewer.create_button(
                    context,
                    window=self._window,
                    card=card,
                    x=x_0 + x * button_width,
                    y=y_0,
                    width=int(button_width - 0.5 * button_padding),
                    height=int(button_height - 0.5 * button_padding),
                )
            )
