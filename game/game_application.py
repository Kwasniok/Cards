import gui.color as color
from gui.application import Application
from .game_window import Game_Window
from .game_state import Game_State
from .initial_resource_cards import (
    black as initial_resource_cards_black,
    white as initial_resource_cards_white,
)


class Game_Application(Application):
    def __init__(self):
        Application.__init__(self)
        self._game_state = Game_State(name="game state")

    def get_game_state(self):
        return self._game_state

    def on_prepare_game(self):
        player_white = self._game_state.get_player1()
        player_black = self._game_state.get_player2()
        player_white.color(color.WHITE)
        player_black.color(color.BLACK)
        realm_white = player_white.get_realm()
        realm_black = player_black.get_realm()
        realm_white.on_prepare_initial_state()
        realm_white.on_place_initial_resources(initial_resource_cards_white)
        realm_black.on_prepare_initial_state()
        realm_black.on_place_initial_resources(initial_resource_cards_black)

    def run(self):
        window = Game_Window(self, x=100, y=100)
        self.on_prepare_game()
        Application.run(self)
