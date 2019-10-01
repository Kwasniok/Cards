from core.color import BLACK, WHITE
from core.owning import Owner
from core.dice import Dice
from core.card_stack import Card_Stack
from .cards import *
from .events import EVENT_DICE_OUTCOMES
from .player import Player


class Game:
    def __init__(self):
        self._number_dice = Dice(name="number dice", outcomes=range(1, 7))
        self._event_dice = Dice(
            name="number dice", outcomes=EVENT_DICE_OUTCOMES
        )
        self._player1 = Player(name="player 1", color=BLACK)
        self._player2 = Player(name="player 2", color=WHITE)
        self._expansion_card_stacks = []
        for i in range(1, 5 + 1):
            stack = Card_Stack(name="expansion card stack " + str(i))
            self._expansion_card_stacks.append(stack)
        self._road_card_stack = Card_Stack(name="road card stack")
        self._settement_card_stack = Card_Stack(name="settlement card stack")
        self._town_card_stack = Card_Stack(name="town card stack")
        # TODO: fill card stacks
