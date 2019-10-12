import unittest
from ..neutral_zone import Neutral_Zone
from ..dice import Dice
from ..card_stack import Card_Stack
from ..piece_tray import Piece_Tray
from ..events import EVENT_DICE_OUTCOMES


class Test(unittest.TestCase):
    def test_general(self):
        neutral_zone = Neutral_Zone(name="test game state")
        self.assertEqual(str(neutral_zone), "test game state")
        neutral_zone.reset()
        # test dices
        number_dice = neutral_zone.get_number_dice()
        self.assertTrue(isinstance(number_dice, Dice))
        self.assertEquals(number_dice.get_possible_outcomes(), range(1, 7))
        event_dice = neutral_zone.get_event_dice()
        self.assertTrue(isinstance(event_dice, Dice))
        self.assertEquals(
            event_dice.get_possible_outcomes(), EVENT_DICE_OUTCOMES
        )
        # check stacks
        expansion_card_stacks = neutral_zone.get_expansion_card_stacks()
        self.assertEqual(len(expansion_card_stacks), 5)
        for expansion_card_stack in expansion_card_stacks:
            self.assertTrue(isinstance(expansion_card_stack, Card_Stack))
        road_card_stack = neutral_zone.get_road_card_stack()
        self.assertTrue(isinstance(road_card_stack, Card_Stack))
        settlement_card_stack = neutral_zone.get_settlement_card_stack()
        self.assertTrue(isinstance(settlement_card_stack, Card_Stack))
        town_card_stack = neutral_zone.get_town_card_stack()
        self.assertTrue(isinstance(town_card_stack, Card_Stack))
        event_card_intake_stack = neutral_zone.get_event_card_intake_stack()
        self.assertTrue(isinstance(event_card_intake_stack, Card_Stack))
        event_card_tray_stack = neutral_zone.get_event_card_tray_stack()
        self.assertTrue(isinstance(event_card_tray_stack, Card_Stack))
        piece_tray = neutral_zone.get_piece_tray()
        self.assertTrue(isinstance(piece_tray, Piece_Tray))
