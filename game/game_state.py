from gui.color import BLACK, WHITE
from .neutral_zone import Neutral_Zone
from .player import Player


class Game_State:
    def __init__(self, name):
        self._name = name
        self._player1 = Player(name="player 1", color=BLACK)
        self._player2 = Player(name="player 2", color=WHITE)
        self._neutral_zone = Neutral_Zone("neutral zone of " + str(self))

    def __str__(self):
        return self._name

    def get_player1(self):
        return self._player1

    def get_player2(self):
        return self._player2

    def get_neutral_zone(self):
        return self._neutral_zone
