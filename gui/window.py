import tkinter as tk
import tkinter.font as tkfont
from core.gui.util import px_to_pt, pt_to_px
from core.gui.window import Window as Base_Window
from game.all_cards import *
from .canvas import Canvas


class Window(Base_Window):
    def __init__(self, application, x, y):
        width = 1920
        height = 1080
        Base_Window.__init__(
            self,
            application=application,
            title="Game Window",
            width=width,
            height=height,
            x=x,
            y=y,
        )
        self.make_non_resizable()
        self.center()
        self.set_icon("res/game_icon.gif")
        self._game_canvas = Canvas(self)
        self._update_realms_button = tk.Button(
            self.get_tk_toplevel(),
            text="update realms",
            font=tkfont.Font(
                family="Helvetica", size=px_to_pt(24), weight="bold"
            ),
            command=lambda: self.on_update_realms(None),
        )
        self._update_realms_button.place(
            anchor=tk.CENTER,
            x=width / 2 - 100,
            y=height / 2,
            width=200,
            height=100,
        )
        self._ream1_buttons = []
        self._ream2_buttons = []
        self._update_hands_button = tk.Button(
            self.get_tk_toplevel(),
            text="update hands",
            font=tkfont.Font(
                family="Helvetica", size=px_to_pt(24), weight="bold"
            ),
            command=lambda: self.on_update_hands(None),
        )
        self._update_hands_button.place(
            anchor=tk.CENTER,
            x=width / 2 + 100,
            y=height / 2,
            width=200,
            height=100,
        )
        self._hand1_buttons = []
        self._hand2_buttons = []

    def destroy(self):
        if not (self._game_canvas is None):
            self._game_canvas.destroy()
            self._game_canvas = None
        self._destroy_realm_buttons(self._ream1_buttons)
        self._destroy_realm_buttons(self._ream2_buttons)
        self._destroy_hand_buttons(self._hand1_buttons)
        self._destroy_hand_buttons(self._hand2_buttons)
        Base_Window.destroy(self)

    def _destroy_realm_buttons(self, realm_buttons):
        for column in realm_buttons:
            for cell in column:
                for button in cell:
                    button.destroy()

    def _destroy_hand_buttons(self, hand_buttons):
        for button in hand_buttons:
            button.destroy()

    def on_update_realms(self, context):
        toplevel = self.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()
        game_state = self.get_application().get_game_state()
        player1 = game_state.get_player1()
        player2 = game_state.get_player2()
        realm1 = player1.get_realm()
        realm2 = player2.get_realm()

        # clear realm GUI
        self._destroy_realm_buttons(self._ream1_buttons)
        self._destroy_realm_buttons(self._ream2_buttons)

        # draw ream GUI
        columns = len(realm1._card_slot_grid)
        rows = 5
        button_width = 180
        button_height = 50
        button_padding = 10
        # realm 1
        x_0 = (width - button_width * (columns - 1)) / 2
        y_0 = 150 + int(button_height * 0.5)
        self._create_realm_buttons(
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
        # realm 2
        columns = len(realm2._card_slot_grid)
        y_0 = height - int(button_height * ((rows - 1))) - y_0
        self._create_realm_buttons(
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

    def on_update_hands(self, context):
        toplevel = self.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()
        game_state = self.get_application().get_game_state()
        player1 = game_state.get_player1()
        player2 = game_state.get_player2()
        hand1 = player1.get_hand()
        hand2 = player2.get_hand()

        # clear hand GUI
        self._destroy_hand_buttons(self._hand1_buttons)
        self._destroy_hand_buttons(self._hand2_buttons)

        # draw hand GUI
        button_width = 180
        button_height = 50
        button_padding = 10
        # hand 1
        columns = hand1.get_size()
        x_0 = (width - button_width * (columns - 1)) / 2
        y_0 = int(button_height * 0.5)
        self._create_hand_buttons(
            context,
            hand1,
            self._hand1_buttons,
            columns,
            x_0,
            y_0,
            button_width,
            button_height,
            button_padding,
        )
        # hand 2
        columns = hand2.get_size()
        x_0 = (width - button_width * (columns - 1)) / 2
        y_0 = height - int(button_height * 0.5)
        self._create_hand_buttons(
            context,
            hand2,
            self._hand2_buttons,
            columns,
            x_0,
            y_0,
            button_width,
            button_height,
            button_padding,
        )

    def _create_realm_buttons(
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
                    pct.__name__ for pct in slot.get_accepted_base_types()
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
                    card_symbol = card.get_title(context)
                    if card.is_face_up():
                        card_symbol += " (FU)"
                    else:
                        card_symbol += " (FD)"
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

    def _create_hand_buttons(
        self,
        context,
        hand,
        buttons,
        columns,
        x_0,
        y_0,
        button_width,
        button_height,
        button_padding,
    ):
        for x in range(columns):
            card = hand[x]
            card_symbol = card.get_title(context)
            if card.is_face_up():
                card_symbol += " (FU)"
            else:
                card_symbol += " (FD)"
            card_symbol += (
                "\n["
                + (",".join([c.get_name() for c in card.get_cost(context)]))
                + "]"
            )
            card_symbol += "\n" + card.get_text(context)
            button = tk.Button(
                self.get_tk_toplevel(),
                text=card_symbol,
                command=lambda card=card: print("clicked on " + repr(card)),
            )
            button.place(
                anchor=tk.CENTER,
                x=x_0 + x * button_width,
                y=y_0,
                width=int(button_width - 0.5 * button_padding),
                height=int(button_height - 0.5 * button_padding),
            )
            buttons.append(button)
