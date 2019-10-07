from gui.application import Application
from .game_window import Game_Window
from .game_state import Game_State


class Game_Application(Application):
    def __init__(self):
        Application.__init__(self)
        self._game_state = Game_State(name="game state")

    def get_game_state(self):
        return self._game_state

    def run(self):
        window = Game_Window(self, x=100, y=100)
        Application.run(self)
