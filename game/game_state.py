from core.random import random_pop, random_pick
import core.gui.color as color
from core.internally_named import Internally_Named
from .player import Player
from .neutral_zone import Neutral_Zone
from .piece import Piece
from .assets.initial_resource_cards import (
    get_initial_resource_cards_black,
    get_initial_resource_cards_white,
)


class Game_State(Internally_Named):
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

    # context: dummy context
    def on_prepare_game(self, context):
        # neutral zone
        self._neutral_zone.reset()
        player = [self.get_player1(), self.get_player2()]
        # player
        player_white = random_pop(player)
        player_black = random_pop(player)
        player_white.change_color(color.WHITE)
        player_black.change_color(color.BLACK)
        realm_white = player_white.get_realm()
        realm_black = player_black.get_realm()
        realm_white.on_prepare_initial_state()
        realm_white.on_place_initial_resources(
            get_initial_resource_cards_black()
        )
        realm_black.on_prepare_initial_state()
        realm_black.on_place_initial_resources(
            get_initial_resource_cards_white()
        )

        # fill hand with random cards (AGAINST RULES, dummy rule to test gui)
        # TODO: REMOVE later!
        def fill_hand_randomly(player):
            expansion_card_stack = random_pick(
                self._neutral_zone.get_expansion_card_stacks()
            )
            hand = player.get_hand()
            while not hand.is_full() and not expansion_card_stack.is_empty():
                card = random_pick(expansion_card_stack)
                expansion_card_stack.remove(card)
                card.change_owner(player_white)
                card.make_face_down()
                hand.add(card)

        fill_hand_randomly(player_white)
        fill_hand_randomly(player_black)
