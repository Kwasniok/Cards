import tkinter as tk
import tkinter.font as tkfont
import game.directions as directions


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
        columns = len(self._realm.get_card_slot_grid())
        rows = 5
        x_0 = (width - button_width * (columns - 1)) / 2
        y_0 = 150 + int(button_height * 0.5)
        if self._direction == directions.DOWN:
            y_0 = height - int(button_height * ((rows - 1))) - y_0
        for x in range(columns):
            button_column = []
            for y in range(rows):
                button_cell = []
                # slot
                slot = self._realm.get_card_slot_grid()[x][y]
                slot_symbol = slot.get_name()
                slot_symbol += (
                    " (" + str(len(slot)) + "/" + str(slot.get_limit()) + ")"
                )
                slot_symbol += "\n"
                slot_symbol += "|".join(
                    pct.__name__ for pct in slot.get_accepted_base_types()
                )
                # slot button
                button = tk.Button(
                    self._window.get_tk_toplevel(),
                    text=slot_symbol,
                    command=lambda slot=slot: print("clicked on " + repr(slot)),
                )
                button.place(
                    anchor=tk.CENTER,
                    x=x_0 + x * button_width,
                    y=y_0 + y * button_height,
                    width=int(button_width - 0.5 * button_padding),
                    height=int(button_height - 0.5 * button_padding),
                )
                button_cell.append(button)
                # cards in slot
                shift = 0
                for card in slot:
                    card_symbol = card.get_title(context)
                    if card.is_face_up():
                        card_symbol += " (FU)"
                    else:
                        card_symbol += " (FD)"
                    button = tk.Button(
                        self._window.get_tk_toplevel(),
                        text=card_symbol,
                        command=lambda card=card: print(
                            "clicked on " + repr(card)
                        ),
                    )
                    button.place(
                        anchor=tk.CENTER,
                        x=x_0 + x * button_width + shift,
                        y=y_0 + y * button_height + int(button_height / 4),
                        width=int((button_width - 0.5 * button_padding) * 0.9),
                        height=int(
                            (button_height - 0.5 * button_padding) * 0.5
                        ),
                    )
                    button_cell.append(button)
                    shift += 10
                button_column.append(button_cell)
            self._buttons.append(button_column)
