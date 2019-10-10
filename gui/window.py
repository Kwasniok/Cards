import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
from core.gui.util import px_to_pt, pt_to_px
from core.gui.window import Window as Base_Window
import game.directions as directions
from game.all_cards import *
from .canvas import Canvas
from .realm_viewer import Realm_Viewer
from .hand_viewer import Hand_Viewer
from .player_viewer import Player_Viewer
from .dice_viewer import Dice_Viewer


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
        # update buttons
        button_width = 200
        button_height = 100
        self._update_button_font = tkfont.Font(
            family="Helvetica", size=px_to_pt(24), weight="bold"
        )
        # realms
        self._realm_viewer1 = Realm_Viewer(
            window=self,
            realm=self.get_application()
            .get_game_state()
            .get_player1()
            .get_realm(),
            direction=directions.UP,
        )
        self._realm_viewer2 = Realm_Viewer(
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
            font=self._update_button_font,
            command=lambda: self.on_update_realms(None),
        )
        self._update_realms_button.place(
            anchor=tk.CENTER,
            x=width / 2 - 1.5 * button_width,
            y=height / 2,
            width=button_width,
            height=button_height,
        )
        # hands
        self._hand_viewer1 = Hand_Viewer(
            window=self,
            hand=self.get_application()
            .get_game_state()
            .get_player1()
            .get_hand(),
            direction=directions.UP,
        )
        self._hand_viewer2 = Hand_Viewer(
            window=self,
            hand=self.get_application()
            .get_game_state()
            .get_player2()
            .get_hand(),
            direction=directions.DOWN,
        )
        self._update_hands_button = tk.Button(
            self.get_tk_toplevel(),
            text="update hands",
            font=self._update_button_font,
            command=lambda: self.on_update_hands(None),
        )
        self._update_hands_button.place(
            anchor=tk.CENTER,
            x=width / 2 - 0.5 * button_width,
            y=height / 2,
            width=button_width,
            height=button_height,
        )
        # player
        self._player_viewer1 = Player_Viewer(
            window=self,
            player=self.get_application().get_game_state().get_player1(),
            direction=directions.UP,
        )
        self._player_viewer2 = Player_Viewer(
            window=self,
            player=self.get_application().get_game_state().get_player2(),
            direction=directions.DOWN,
        )
        self._update_player_button = tk.Button(
            self.get_tk_toplevel(),
            text="update player",
            font=self._update_button_font,
            command=lambda: self.on_update_players(None),
        )
        self._update_player_button.place(
            anchor=tk.CENTER,
            x=width / 2 + 0.5 * button_width,
            y=height / 2,
            width=button_width,
            height=button_height,
        )
        # dices
        self._dice_viewer_number = Dice_Viewer(
            window=self,
            dice=self.get_application()
            .get_game_state()
            .get_neutral_zone()
            .get_number_dice(),
            direction=directions.LEFT,
        )
        self._dice_viewer_event = Dice_Viewer(
            window=self,
            dice=self.get_application()
            .get_game_state()
            .get_neutral_zone()
            .get_event_dice(),
            direction=directions.RIGHT,
        )
        self._update_dice_button = tk.Button(
            self.get_tk_toplevel(),
            text="update dices",
            font=self._update_button_font,
            command=lambda: self.on_update_dices(None),
        )
        self._update_dice_button.place(
            anchor=tk.CENTER,
            x=width / 2 + 1.5 * button_width,
            y=height / 2,
            width=button_width,
            height=button_height,
        )

    def destroy(self):
        safe_destroy(self._game_canvas)
        safe_destroy(self._realm_viewer1)
        safe_destroy(self._realm_viewer2)
        safe_destroy(self._update_realms_button)
        safe_destroy(self._hand_viewer1)
        safe_destroy(self._hand_viewer2)
        safe_destroy(self._update_hands_button)
        safe_destroy(self._player_viewer1)
        safe_destroy(self._player_viewer2)
        safe_destroy(self._update_player_button)
        safe_destroy(self._dice_viewer_number)
        safe_destroy(self._dice_viewer_event)
        safe_destroy(self._update_dice_button)
        self._update_button_font = None
        Base_Window.destroy(self)

    def on_update_realms(self, context):
        self._realm_viewer1.on_update(context)
        self._realm_viewer2.on_update(context)

    def on_update_hands(self, context):
        self._hand_viewer1.on_update(context)
        self._hand_viewer2.on_update(context)

    def on_update_players(self, context):
        self._player_viewer1.on_update(context)
        self._player_viewer2.on_update(context)

    def on_update_dices(self, context):
        self._dice_viewer_number.on_update(context)
        self._dice_viewer_event.on_update(context)
