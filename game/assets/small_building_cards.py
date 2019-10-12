from abc import abstractmethod
from game.resource_types import *
from game.expansion_card import expansion_card_library, Small_Building_Card


class Monastery_Card(Small_Building_Card):
    def __init__(self):
        Small_Building_Card.__init__(self, "Monastery")

    def get_cost(self, context):
        return [LOGS, IRON, BRICKS]


expansion_card_library.register(Monastery_Card, amount=2)


class Storage_Card(Small_Building_Card):
    def __init__(self):
        Small_Building_Card.__init__(self, "Storage")

    def get_text(self, context):
        return "<-protected form robber->"

    def get_cost(self, context):
        return [LOGS, BRICKS]

    def get_mill_points(self, context):
        return 1


expansion_card_library.register(Storage_Card, amount=2)


class Resource_Doubler_Card(Small_Building_Card):
    # TODO: implement effect on incrementing neighbouring resource cards
    @abstractmethod
    def __init__(self, name, resource_type):
        Small_Building_Card.__init__(self, name)
        self._resource_type = resource_type

    def get_text(self, context):
        return (
            "<- " + self._resource_type.get_source_name() + "s yield twice ->"
        )


class Sawmill_Card(Resource_Doubler_Card):
    def __init__(self):
        Resource_Doubler_Card.__init__(self, "Sawmill", LOGS)

    def get_cost(self, context):
        return [LOGS, LOGS]


expansion_card_library.register(Sawmill_Card, amount=1)


class Brickyard_Card(Resource_Doubler_Card):
    def __init__(self):
        Resource_Doubler_Card.__init__(self, "Brickyard", BRICKS)

    def get_cost(self, context):
        return [IRON, BRICKS]


expansion_card_library.register(Brickyard_Card, amount=1)


class Wool_Manufatory_Card(Resource_Doubler_Card):
    def __init__(self):
        Resource_Doubler_Card.__init__(self, "Wool Manufatory", WOOL)

    def get_cost(self, context):
        return [LOGS, BRICKS]


expansion_card_library.register(Wool_Manufatory_Card, amount=1)


class Ironforge_Card(Resource_Doubler_Card):
    def __init__(self):
        Resource_Doubler_Card.__init__(self, "Ironforge", IRON)

    def get_cost(self, context):
        return [IRON, BRICKS]


expansion_card_library.register(Ironforge_Card, amount=1)


class Mill_Card(Resource_Doubler_Card):
    def __init__(self):
        Resource_Doubler_Card.__init__(self, "Mill", GRAIN)

    def get_cost(self, context):
        return [BRICKS, GRAIN]


expansion_card_library.register(Mill_Card, amount=1)
