from itertools import cycle
from core.random import random_pop
from core.internally_named import Internally_Named
from core.owning import Owner
from .dice import Dice
from .card_stack import Card_Stack
from .structure_cards import Road_Card, Settlement_Card, Town_Card
from .expansion_cards import expansion_card_library
from .event_cards import event_card_library
from .piece import piece_library
from .events import EVENT_DICE_OUTCOMES
from .player import Player
from .piece_tray import Piece_Tray


class Neutral_Zone(Internally_Named):
    def __init__(self, name):
        Internally_Named.__init__(self, name)
        self._number_dice = Dice(name="number dice", outcomes=range(1, 7))
        self._event_dice = Dice(name="event dice", outcomes=EVENT_DICE_OUTCOMES)
        self._number_of_expansion_card_stacks = 5
        self._expansion_card_stacks = None
        self._road_card_stack = None
        self._settement_card_stack = None
        self._town_card_stack = None
        self._event_card_intake_stack = None
        self._event_card_tray_stack = None
        self.piece_tray = None
        self.reset()

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
        self._event_card_intake_stack = Card_Stack(
            name="event card intake stack"
        )
        self._event_card_tray_stack = Card_Stack(name="event card tray stack")
        self._fill_stacks()
        self._piece_tray = Piece_Tray(name="neutral piece tray")
        self._fill_piece_tray()

    def get_number_dice(self):
        return self._number_dice

    def get_event_dice(self):
        return self._event_dice

    def get_expansion_card_stacks(self):
        return self._expansion_card_stacks

    def get_road_card_stack(self):
        return self._road_card_stack

    def get_settlement_card_stack(self):
        return self._settement_card_stack

    def get_town_card_stack(self):
        return self._town_card_stack

    def get_event_card_intake_stack(self):
        return self._event_card_intake_stack

    def get_event_card_tray_stack(self):
        return self._event_card_tray_stack

    def get_piece_tray(self):
        return self._piece_tray

    def _fill_stacks(self):
        expansion_cards = expansion_card_library.get_all()
        event_cards = event_card_library.get_all()
        self._fill_expension_card_stacks(expansion_cards)
        self._fill_road_card_stack(7)
        self._fill_settlement_card_stack(5)
        self._fill_town_card_stack(7)
        self._fill_event_card_intake_stack(event_cards)

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

    def _fill_event_card_intake_stack(self, event_cards):
        # fill cards in a random order
        while len(event_cards) > 0:
            self._event_card_intake_stack.push_top(random_pop(event_cards))

    def _fill_piece_tray(self):
        for piece in piece_library.get_all():
            self._piece_tray.add(piece)
