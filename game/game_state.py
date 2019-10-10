from core.random import random_pop
import core.gui.color as color
from core.internally_named import Internally_Named
from .player import Player
from .neutral_zone import Neutral_Zone
from .piece import Piece
import game.assets.initial_resource_cards as initial_resource_cards


class Game_State:
    def __init__(self, name):
        Internally_Named.__init__(self, name)
        self._player1 = Player(name="player 1", color=color.BLACK)
        self._player2 = Player(name="player 2", color=color.WHITE)
        self._neutral_zone = Neutral_Zone("neutral zone of " + str(self))

    def get_name(self):
        return str(self)

    def get_player1(self):
        return self._player1

    def get_player2(self):
        return self._player2

    def get_neutral_zone(self):
        return self._neutral_zone

    def on_prepare_game(self):
        player = [self.get_player1(), self.get_player2()]
        player_white = random_pop(player)
        player_black = random_pop(player)
        player_white.change_color(color.WHITE)
        player_black.change_color(color.BLACK)
        realm_white = player_white.get_realm()
        realm_black = player_black.get_realm()
        realm_white.on_prepare_initial_state()
        realm_white.on_place_initial_resources(initial_resource_cards.white)
        realm_black.on_prepare_initial_state()
        realm_black.on_place_initial_resources(initial_resource_cards.black)
