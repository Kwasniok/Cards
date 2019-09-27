from core.card import Card
from core.hand import Hand
from core.dice import Dice
from core.card_stack import Card_Stack
from game.resource_types import LOGS, BRICKS, GRAIN, IRON, WOOL, GOLD
from game.structure_cards import Street_Card, Settlement_Card, Town_Card
from game.resource_cards import Resource_Card

print("running tests ...")
cs = [
    Street_Card(),
    Settlement_Card(),
    Town_Card(),
    Resource_Card(LOGS, 1, 0),
    Resource_Card(BRICKS, 1, 0),
    Resource_Card(GRAIN, 3, 0),
    Resource_Card(IRON, 4, 0),
    Resource_Card(WOOL, 5, 0),
    Resource_Card(GOLD, 3, 0),
]
print(("object", "name", "text"))
print("--------------------------")
for c in cs:
    print((c, str(c), c.text()))
