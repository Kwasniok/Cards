import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
import game.directions as directions
from .dice_viewer import Dice_Viewer


class Neutral_Zone_Viewer:
    def __init__(self, window, neutral_zone):
        self._window = window
        self._neutral_zone = neutral_zone
        # dices
        self._dice_viewer_number = Dice_Viewer(
            window=self._window,
            dice=self._window.get_application()
            .get_game_state()
            .get_neutral_zone()
            .get_number_dice(),
            direction=directions.LEFT,
        )
        self._dice_viewer_event = Dice_Viewer(
            window=self._window,
            dice=self._window.get_application()
            .get_game_state()
            .get_neutral_zone()
            .get_event_dice(),
            direction=directions.RIGHT,
        )

    def destroy(self):
        safe_destroy(self._dice_viewer_number)
        safe_destroy(self._dice_viewer_event)

    def on_update_dices(self, context):
        self._dice_viewer_number.on_update(context)
        self._dice_viewer_event.on_update(context)
