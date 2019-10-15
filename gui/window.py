import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
from core.gui.util import px_to_pt, pt_to_px
from core.gui.window import Window as Base_Window
import game.directions as directions
from .interaction_window import Interaction_Window
from .update_window import Update_Window
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
        # interaction window
        toplevel = self.get_tk_toplevel()
        toplevel.update_idletasks()
        interaction_window_x = toplevel.winfo_x() + toplevel.winfo_width()
        interaction_window_y = toplevel.winfo_y() + toplevel.winfo_height() / 2
        self._interaction_window = Interaction_Window(
            self.get_application(),
            x=interaction_window_x,
            y=interaction_window_y,
        )
        # update window (for debugging)
        toplevel = self.get_tk_toplevel()
        toplevel.update_idletasks()
        interaction_window_x = toplevel.winfo_x() - 200
        interaction_window_y = toplevel.winfo_y() + toplevel.winfo_height() / 2
        self._update_window = Update_Window(
            self.get_application(),
            window=self,
            interaction_window=self._interaction_window,
            x=interaction_window_x,
            y=interaction_window_y,
        )
        # canvas
        self._game_canvas = Canvas(self)

        ## viewer
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
        # neutral zone
        self._neutral_zone_viewer = Neutral_Zone_Viewer(
            window=self,
            neutral_zone=self.get_application()
            .get_game_state()
            .get_neutral_zone(),
        )

    def destroy(self):
        self._game_canvas = safe_destroy(self._game_canvas)
        safe_destroy(self._realm_viewer1)
        safe_destroy(self._realm_viewer2)
        safe_destroy(self._hand_viewer1)
        safe_destroy(self._hand_viewer2)
        safe_destroy(self._player_viewer1)
        safe_destroy(self._player_viewer2)
        self._neutral_zone_viewer = safe_destroy(self._neutral_zone_viewer)
        self._update_window = safe_destroy(self._update_window)
        self._interaction_window = safe_destroy(self._interaction_window)
        Base_Window.destroy(self)

    def close(self):
        self._interaction_window.close()
        self._update_window.close()
        Base_Window.close(self)

    def get_interaction_window(self):
        return self._interaction_window

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

    def on_update_all(self, context):
        self.on_update_realms(context)
        self.on_update_hands(context)
        self.on_update_player_status(context)
        self.on_update_dices(context)
        self.on_update_card_stacks(context)
        self.on_update_piece_trays(context)
