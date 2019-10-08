import tkinter as tk
import tkinter.font as tkfont
from core.gui.util import px_to_pt, pt_to_px
from core.gui.window import Window as Base_Window
import game.directions as directions
from game.all_cards import *
from .canvas import Canvas
from .realm_viewer import Realm_Viewer


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
        self._realm_viwer1 = Realm_Viewer(
            window=self,
            realm=self.get_application()
            .get_game_state()
            .get_player1()
            .get_realm(),
            direction=directions.UP,
        )
        self._realm_viwer2 = Realm_Viewer(
            window=self,
            realm=self.get_application()
            .get_game_state()
            .get_player2()
            .get_realm(),
            direction=directions.DOWN,
        )
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
        if not (self._realm_viwer1 is None):
            self._realm_viwer1.destroy()
            self._realm_viwer1 = None
        if not (self._realm_viwer2 is None):
            self._realm_viwer2.destroy()
            self._realm_viwer2 = None
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
        self._realm_viwer1.on_update(context)
        self._realm_viwer2.on_update(context)

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
