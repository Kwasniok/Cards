import tkinter as tk
import tkinter.font as tkfont
from gui.util import px_to_pt, pt_to_px
from gui.window import Window
from .game_canvas import Game_Canvas
from .all_cards import *


class Game_Window(Window):
    def __init__(self, game_application, x, y):
        width = 1920
        height = 1080
        Window.__init__(
            self,
            application=game_application,
            title="Game Window",
            width=width,
            height=height,
            x=x,
            y=y,
        )
        self.make_non_resizable()
        self.center()
        self.set_icon("res/game_icon.gif")
        self._game_canvas = Game_Canvas(self)
        self._update_realms_button = tk.Button(
            self.get_tk_toplevel(),
            text="update realms",
            font=tkfont.Font(
                family="Helvetica", size=px_to_pt(24), weight="bold"
            ),
            command=lambda: self.update_realms(),
        )
        self._update_realms_button.place(
            anchor=tk.CENTER, x=width / 2, y=height / 2, width=200, height=100
        )
        self._ream1_buttons = []
        self._ream2_buttons = []

    def destroy(self):
        if not (self._game_canvas is None):
            self._game_canvas.destroy()
            self._game_canvas = None
        Window.destroy(self)

    def update_realms(self):
        toplevel = self.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()
        game_state = self.get_application().get_game_state()
        context = None
        player1 = game_state.get_player1()
        player2 = game_state.get_player2()
        realm1 = player1.get_realm()
        realm2 = player2.get_realm()

        # clear realm 1 GUI
        for column in self._ream1_buttons:
            for cell in column:
                for button in cell:
                    button.destroy()
        # draw ream 1 GUI
        columns = len(realm1._card_slot_grid)
        rows = 5
        button_width = 180
        button_height = 50
        button_padding = 10
        x_0 = (width - button_width * (columns - 1)) / 2
        y_0 = 150 + int(button_height * 0.5)
        self._update_realm(
            context,
            realm1,
            self._ream1_buttons,
            columns,
            rows,
            x_0,
            y_0,
            button_width,
            button_height,
            button_padding,
        )
        y_0 = height - int(button_height * ((rows - 1))) - y_0
        self._update_realm(
            context,
            realm2,
            self._ream2_buttons,
            columns,
            rows,
            x_0,
            y_0,
            button_width,
            button_height,
            button_padding,
        )

    def _update_realm(
        self,
        context,
        realm,
        buttons,
        columns,
        rows,
        x_0,
        y_0,
        button_width,
        button_height,
        button_padding,
    ):
        for x in range(columns):
            button_column = []
            for y in range(rows):
                button_cell = []
                # slot
                slot = realm.get_card_slot_grid()[x][y]
                slot_symbol = slot.get_name()
                slot_symbol += (
                    " (" + str(len(slot)) + "/" + str(slot.get_limit()) + ")"
                )
                slot_symbol += "\n"
                slot_symbol += "|".join(
                    pct.__name__ for pct in slot.possible_card_types()
                )
                # slot button
                button = tk.Button(
                    self.get_tk_toplevel(),
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
                    card_symbol = card.get_name()
                    button = tk.Button(
                        self.get_tk_toplevel(),
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
            buttons.append(button_column)
