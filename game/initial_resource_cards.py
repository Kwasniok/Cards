from .resource_cards import Resource_Card
from .resource_types import LOGS, BRICKS, GRAIN, IRON, WOOL, GOLD

initial_resource_cards_black = [
    Resource_Card(resource_type=GOLD, dice_number=1, initial_count=1),
    Resource_Card(resource_type=GRAIN, dice_number=2, initial_count=1),
    Resource_Card(resource_type=IRON, dice_number=3, initial_count=1),
    Resource_Card(resource_type=WOOL, dice_number=4, initial_count=1),
    Resource_Card(resource_type=LOGS, dice_number=5, initial_count=1),
    Resource_Card(resource_type=BRICKS, dice_number=6, initial_count=1),
]

initial_resource_cards_white = [
    Resource_Card(resource_type=GRAIN, dice_number=1, initial_count=1),
    Resource_Card(resource_type=IRON, dice_number=2, initial_count=1),
    Resource_Card(resource_type=WOOL, dice_number=3, initial_count=1),
    Resource_Card(resource_type=LOGS, dice_number=4, initial_count=1),
    Resource_Card(resource_type=BRICKS, dice_number=5, initial_count=1),
    Resource_Card(resource_type=GOLD, dice_number=6, initial_count=1),
]
