from core.color import BLACK, WHITE
from .game_state import Game_State
from .player import Player


class Game:
    def __init__(self, name):
        self._name = name
        self._player1 = Player(name="player 1", color=BLACK)
        self._player2 = Player(name="player 2", color=WHITE)
        self._game_state = Game_State("game state of " + str(self))

    def __str__(self):
        return self._name

    def get_player1(self):
        return self._player1

    def get_player2(self):
        return self._player2

    def get_game_state(self):
        return self._game_state
