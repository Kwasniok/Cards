import tkinter as tk
import tkinter.font as tkfont
from core.gui.util import px_to_pt, pt_to_px
from core.gui.window import Window as Base_Window
import game.directions as directions
from game.all_cards import *
from .canvas import Canvas
from .realm_viewer import Realm_Viewer
from .hand_viewer import Hand_Viewer
from .player_viewer import Player_Viewer


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
            font=tkfont.Font(
                family="Helvetica", size=px_to_pt(24), weight="bold"
            ),
            command=lambda: self.on_update_players(None),
        )
        self._update_player_button.place(
            anchor=tk.CENTER,
            x=width / 2 + 300,
            y=height / 2,
            width=200,
            height=100,
        )

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
        if not (self._hand_viewer1 is None):
            self._hand_viewer1.destroy()
            self._hand_viewer1 = None
        if not (self._hand_viewer2 is None):
            self._hand_viewer2.destroy()
            self._hand_viewer2 = None
        if not (self._player_viewer1 is None):
            self._player_viewer1.destroy()
            self._player_viewer1 = None
        if not (self._player_viewer2 is None):
            self._player_viewer2.destroy()
            self._player_viewer2 = None
        Base_Window.destroy(self)

    def on_update_realms(self, context):
        self._realm_viwer1.on_update(context)
        self._realm_viwer2.on_update(context)

    def on_update_hands(self, context):
        self._hand_viewer1.on_update(context)
        self._hand_viewer2.on_update(context)

    def on_update_players(self, context):
        self._player_viewer1.on_update(context)
        self._player_viewer2.on_update(context)
