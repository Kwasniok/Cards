import core.gui.color as color
from core.random import random_pop
from core.gui.application import Application as Base_Application
from .window import Window
from game.game_state import Game_State
from game.assets.initial_resource_cards import (
    black as initial_resource_cards_black,
    white as initial_resource_cards_white,
)


class Application(Base_Application):
    def __init__(self):
        Base_Application.__init__(self)
        self._game_state = Game_State(name="game state")

    def get_game_state(self):
        return self._game_state

    def on_prepare_game(self):
        player = [
            self._game_state.get_player1(),
            self._game_state.get_player2(),
        ]
        player_white = random_pop(player)
        player_black = random_pop(player)
        player_white.change_color(color.WHITE)
        player_black.change_color(color.BLACK)
        realm_white = player_white.get_realm()
        realm_black = player_black.get_realm()
        realm_white.on_prepare_initial_state()
        realm_white.on_place_initial_resources(initial_resource_cards_white)
        realm_black.on_prepare_initial_state()
        realm_black.on_place_initial_resources(initial_resource_cards_black)

    def run(self):
        self.on_prepare_game()
        window = Window(self, x=100, y=100)
        Base_Application.run(self)
