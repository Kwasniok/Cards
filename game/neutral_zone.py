from itertools import cycle
from core.random import random_pop
from core.owning import Owner
from .dice import Dice
from .card_stack import Card_Stack
from .all_cards import *
from .expansion_cards import get_all_expansion_cards
from .events import EVENT_DICE_OUTCOMES
from .player import Player


class Neutral_Zone:
    def __init__(self, name):
        self._name = name
        self._number_dice = Dice(name="number dice", outcomes=range(1, 7))
        self._event_dice = Dice(name="event dice", outcomes=EVENT_DICE_OUTCOMES)
        self._number_of_expansion_card_stacks = 5
        self._expansion_card_stacks = None
        self._road_card_stack = None
        self._settement_card_stack = None
        self._town_card_stack = None
        self.reset()

    def __str__(self):
        return self._name

    def reset(self):
        self._number_dice.roll()
        self._event_dice.roll()
        self._expansion_card_stacks = []
        for i in range(1, self._number_of_expansion_card_stacks + 1):
            stack = Card_Stack(name="expansion card stack " + str(i))
            self._expansion_card_stacks.append(stack)
        self._road_card_stack = Card_Stack(name="road card stack")
        self._settement_card_stack = Card_Stack(name="settlement card stack")
        self._town_card_stack = Card_Stack(name="town card stack")
        self._fill_stacks()

    def _fill_stacks(self):
        expansion_cards = get_all_expansion_cards()
        self._fill_expension_card_stacks(expansion_cards)
        self._fill_road_card_stack(7)
        self._fill_settlement_card_stack(5)
        self._fill_town_card_stack(7)

    def _fill_expension_card_stacks(self, expansion_cards):
        # fill cards in a random order while cycling over all stacks
        for stack in cycle(self._expansion_card_stacks):
            if len(expansion_cards) == 0:
                break
            stack.push_top(random_pop(expansion_cards))

    def _fill_road_card_stack(self, amount):
        for i in range(0, amount):
            self._road_card_stack.push_top(Road_Card())

    def _fill_settlement_card_stack(self, amount):
        for i in range(0, amount):
            self._settement_card_stack.push_top(Settlement_Card())

    def _fill_town_card_stack(self, amount):
        for i in range(0, amount):
            self._town_card_stack.push_top(Town_Card())
