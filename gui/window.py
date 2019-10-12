import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
from core.gui.util import px_to_pt, pt_to_px
from core.gui.window import Window as Base_Window
import game.directions as directions
from .canvas import Canvas
from .realm_viewer import Realm_Viewer
from .hand_viewer import Hand_Viewer
from .player_viewer import Player_Viewer
from .neutral_zone_viewer import Neutral_Zone_Viewer


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
        button_width = 100
        button_height = 20
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
            command=lambda: self.on_update_realms(None),
        )
        self._update_realms_button.place(
            anchor=tk.CENTER,
            x=width / 2,
            y=height / 2 - 2 * button_height,
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
            command=lambda: self.on_update_hands(None),
        )
        self._update_hands_button.place(
            anchor=tk.CENTER,
            x=width / 2,
            y=height / 2 - 1 * button_height,
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
        self._update_player_status_button = tk.Button(
            self.get_tk_toplevel(),
            text="update player",
            command=lambda: self.on_update_player_status(None),
        )
        self._update_player_status_button.place(
            anchor=tk.CENTER,
            x=width / 2,
            y=height / 2 + 0 * button_height,
            width=button_width,
            height=button_height,
        )
        # neutral zone
        self._neutral_zone_viewer = Neutral_Zone_Viewer(
            window=self,
            neutral_zone=self.get_application()
            .get_game_state()
            .get_neutral_zone(),
        )
        # dices
        self._update_dice_button = tk.Button(
            self.get_tk_toplevel(),
            text="update dices",
            command=lambda: self.on_update_dices(None),
        )
        self._update_dice_button.place(
            anchor=tk.CENTER,
            x=width / 2,
            y=height / 2 + 1 * button_height,
            width=button_width,
            height=button_height,
        )
        # card stacks
        self._update_card_stacks_button = tk.Button(
            self.get_tk_toplevel(),
            text="update card stacks",
            command=lambda: self.on_update_card_stacks(None),
        )
        self._update_card_stacks_button.place(
            anchor=tk.CENTER,
            x=width / 2,
            y=height / 2 + 2 * button_height,
            width=button_width,
            height=button_height,
        )
        # pieces
        self._update_pieces_button = tk.Button(
            self.get_tk_toplevel(),
            text="update piece trays",
            command=lambda: self.on_update_piece_trays(None),
        )
        self._update_pieces_button.place(
            anchor=tk.CENTER,
            x=width / 2,
            y=height / 2 + 3 * button_height,
            width=button_width,
            height=button_height,
        )

    def destroy(self):
        self._game_canvas = safe_destroy(self._game_canvas)
        safe_destroy(self._realm_viewer1)
        safe_destroy(self._realm_viewer2)
        self._update_realms_button = safe_destroy(self._update_realms_button)
        safe_destroy(self._hand_viewer1)
        safe_destroy(self._hand_viewer2)
        self._update_hands_button = safe_destroy(self._update_hands_button)
        safe_destroy(self._player_viewer1)
        safe_destroy(self._player_viewer2)
        self._update_player_status_button = safe_destroy(self._update_player_status_button)
        self._neutral_zone_viewer = safe_destroy(self._neutral_zone_viewer)
        self._update_dice_button = safe_destroy(self._update_dice_button)
        self._update_card_stacks_button = safe_destroy(self._update_card_stacks_button)
        self._update_pieces_button = safe_destroy(self._update_pieces_button)
        Base_Window.destroy(self)

    def on_update_realms(self, context):
        self._realm_viewer1.on_update(context)
        self._realm_viewer2.on_update(context)

    def on_update_hands(self, context):
        self._hand_viewer1.on_update(context)
        self._hand_viewer2.on_update(context)

    def on_update_player_status(self, context):
        self._player_viewer1.on_update_status(context)
        self._player_viewer2.on_update_status(context)

    def on_update_dices(self, context):
        self._neutral_zone_viewer.on_update_dices(context)

    def on_update_card_stacks(self, context):
        self._neutral_zone_viewer.on_update_expansion_card_stacks(context)
        self._neutral_zone_viewer.on_update_structure_card_stacks(context)
        self._neutral_zone_viewer.on_update_event_card_stacks(context)

    def on_update_piece_trays(self, context):
        self._neutral_zone_viewer.on_update_piece_tray(context)
        self._player_viewer1.on_update_piece_tray(context)
        self._player_viewer2.on_update_piece_tray(context)
