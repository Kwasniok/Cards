from core.internally_named import Internally_Named
from gui.color import BLACK, WHITE
from .neutral_zone import Neutral_Zone
from .player import Player


class Game_State:
    def __init__(self, name):
        Internally_Named.__init__(self, name)
        self._player1 = Player(name="player 1", color=BLACK)
        self._player2 = Player(name="player 2", color=WHITE)
        self._neutral_zone = Neutral_Zone("neutral zone of " + str(self))

    def get_name(self):
        return str(self)

    def get_player1(self):
        return self._player1

    def get_player2(self):
        return self._player2

    def get_neutral_zone(self):
        return self._neutral_zone
