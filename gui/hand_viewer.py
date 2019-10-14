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
        self._buttons = []

    def on_update(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_buttons()

        # create buttons
        card_button_width = 180
        card_button_height = 50
        columns = self._hand.get_size()
        x_0 = (width - card_button_width * (columns - 1)) / 2
        y_0 = int(card_button_height * 0.5)
        if self._direction == directions.DOWN:
            y_0 = height - int(card_button_height * 0.5)

        # hand
        hand_button_width = columns * card_button_width
        hand_button_height = int(card_button_height * 0.4)
        hand_x = x_0 - (card_button_width - hand_button_width) / 2
        if self._direction == directions.UP:
            hand_y = y_0 + (card_button_height + hand_button_height) / 2
        if self._direction == directions.DOWN:
            hand_y = y_0 - (card_button_height + hand_button_height) / 2
        hand_symbol = self._hand.get_name()
        button = tk.Button(
            self._window.get_tk_toplevel(),
            text=hand_symbol,
            command=lambda hand=self._hand: self._window.get_interaction_window().add_object(
                hand
            ),
        )
        button.place(
            anchor=tk.CENTER,
            x=hand_x,
            y=hand_y,
            width=hand_button_width,
            height=hand_button_height,
        )
        self._buttons.append(button)

        # cards in hand
        for x in range(columns):
            card = self._hand[x]
            self._buttons.append(
                Card_Viewer.create_button(
                    context,
                    window=self._window,
                    card=card,
                    x=x_0 + x * card_button_width,
                    y=y_0,
                    width=card_button_width,
                    height=card_button_height,
                )
            )
