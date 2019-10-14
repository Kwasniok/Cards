import tkinter as tk
import tkinter.font as tkfont
import game.directions as directions
from .card_viewer import Card_Viewer
from .slot_viewer import Slot_Viewer


class Realm_Viewer:
    def __init__(self, window, realm, direction):
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
        self._realm = realm
        self._direction = direction
        self._buttons = []

    def destroy(self):
        self._destroy_buttons()

    def _destroy_buttons(self):
        for column in self._buttons:
            for cell in column:
                for button in cell:
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
        button_width = 180
        button_height = 80
        button_padding = 10
        columns = len(self._realm.get_card_slot_grid())
        rows = 5
        x_0 = (width - button_width * (columns - 1)) / 2
        y_0 = 70 + int(button_height * 0.5)
        if self._direction == directions.DOWN:
            y_0 = height - int(button_height * ((rows - 1))) - y_0
        for x in range(columns):
            button_column = []
            for y in range(rows):
                button_cell = []
                # slot
                slot = self._realm.get_card_slot_grid()[x][y]
                slot_x = x_0 + x * button_width
                slot_y = y_0 + y * button_height
                button_cell = Slot_Viewer.create_buttons(
                    context=context,
                    window=self._window,
                    slot=slot,
                    x=slot_x,
                    y=slot_y,
                    width=button_width,
                    height=button_height,
                    shift_x=0,
                    shift_y=10,
                )
                button_column.append(button_cell)
            self._buttons.append(button_column)
