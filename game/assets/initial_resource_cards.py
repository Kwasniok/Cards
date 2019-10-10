from game.resource_cards import Resource_Card
from game.resource_types import LOGS, BRICKS, GRAIN, IRON, WOOL, GOLD


def get_initial_resource_cards_black():
    return [
        Resource_Card(resource_type=GOLD, dice_number=1, initial_count=1),
        Resource_Card(resource_type=GRAIN, dice_number=2, initial_count=1),
        Resource_Card(resource_type=IRON, dice_number=3, initial_count=1),
        Resource_Card(resource_type=WOOL, dice_number=4, initial_count=1),
        Resource_Card(resource_type=LOGS, dice_number=5, initial_count=1),
        Resource_Card(resource_type=BRICKS, dice_number=6, initial_count=1),
    ]


def get_initial_resource_cards_white():
    return [
        Resource_Card(resource_type=GRAIN, dice_number=1, initial_count=1),
        Resource_Card(resource_type=IRON, dice_number=2, initial_count=1),
        Resource_Card(resource_type=WOOL, dice_number=3, initial_count=1),
        Resource_Card(resource_type=LOGS, dice_number=4, initial_count=1),
        Resource_Card(resource_type=BRICKS, dice_number=5, initial_count=1),
        Resource_Card(resource_type=GOLD, dice_number=6, initial_count=1),
    ]
