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
        self._game_state.on_prepare_game()
        # add dummy cards to hand to test gui
        # TODO: remove!
        from game.assets.small_building_cards import Monastery_Card

        self._game_state.get_player1().get_hand().add(Monastery_Card())
        self._game_state.get_player1().get_hand().add(Monastery_Card())
        self._game_state.get_player2().get_hand().add(Monastery_Card())
        self._game_state.get_player2().get_hand().add(Monastery_Card())

        window = Window(self, x=100, y=100)
        Base_Application.run(self)
