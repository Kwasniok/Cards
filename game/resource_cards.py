from game.card import Card


class Resource_Card(Card):
    RESOURCE_LIMIT = 3

    def __init__(self, resource_type, dice_number, initial_count):
        Card.__init__(self, resource_type.source_name())
        self.resource_type = resource_type
        self.counter = initial_count
        self.dice_number = dice_number

    def title(self, context):
        return str(self.resource_type.source_name())

    def text(self, context):
        return (
            str(self.resource_type.source_name())
            + " ["
            + str(self.dice_number)
            + "] ("
            + str(self.counter)
            + "/3 "
            + self.resource_type.name()
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
                    + self.resource_type.name()
                    + " resources of card "
                    + str(self)
                )
            )
