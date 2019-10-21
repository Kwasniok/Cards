from abc import abstractmethod
from game.card import Card
from .subtype_library import Subtype_Library


class Resource_Card(Card):
    RESOURCE_LIMIT = 3

    @abstractmethod
    def __init__(self, resource_type, dice_number, initial_count):
        Card.__init__(self, resource_type.get_source_name())
        self.resource_type = resource_type
        self.counter = initial_count
        self.dice_number = dice_number

    def __repr__(self):
        return (
            "Resource_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ",resource_type="
            + str(self.resource_type)
            + ",dice_number="
            + str(self.dice_number)
            + ",counter="
            + repr(self.counter)
            + ")"
        )

    def get_title(self, context):
        return str(self.resource_type.get_source_name())

    def get_text(self, context):
        return (
            "["
            + str(self.dice_number)
            + "] ("
            + str(self.counter)
            + "/3 "
            + self.resource_type.get_name()
            + ")"
        )

    def increment(self):
        if self.counter < Resource_Card.RESOURCE_LIMIT:
            self.counter += 1

    def decrement(self, amount):
        if self.counter - amount >= 0:
            self.counter -= amount
        else:
            raise (
                ValueError(
                    "Cannot decrement "
                    + str(amount)
                    + " resources from "
                    + str(self.counter)
                    + " "
                    + self.resource_type.get_name()
                    + " resources of card "
                    + str(self)
                )
            )


resource_card_library = Subtype_Library(Resource_Card)
initial_resource_card_library_black = Subtype_Library(Resource_Card)
initial_resource_card_library_white = Subtype_Library(Resource_Card)
