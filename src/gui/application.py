from core.gui.application import Application as Base_Application
from .window import Window
from game.game_state import Game_State


class Application(Base_Application):
    def __init__(self):
        Base_Application.__init__(self)
        self._game_state = Game_State(name="game state")

    def get_game_state(self):
        return self._game_state

    def run(self):
        self._game_state.on_prepare_game(None)
        window = Window(self)
        Base_Application.run(self)
