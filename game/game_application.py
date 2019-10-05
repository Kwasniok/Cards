from gui.application import Application
from .game_window import Game_Window
from .game import Game


class Game_Application(Application):
    def __init__(self):
        Application.__init__(self)
        self._game = Game(name="main game")

    def get_game(self):
        return self._game

    def run(self):
        window = Game_Window(self, x=100, y=100)
        self.get_frame_updater().register(window)
        Application.run(self)
