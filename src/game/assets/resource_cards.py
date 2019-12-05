from ..resource_card import resource_card_library, Resource_Card
from .resource_types import *


class Wood_Card(Resource_Card):
    def __init__(self, dice_number, initial_count=0):
        Resource_Card.__init__(
            self,
            resource_type=LOGS,
            dice_number=dice_number,
            initial_count=initial_count,
        )


resource_card_library.register(Wood_Card, initializer_dict={"dice_number": 1})
resource_card_library.register(Wood_Card, initializer_dict={"dice_number": 6})


class Clay_Pit_Card(Resource_Card):
    def __init__(self, dice_number, initial_count=0):
        Resource_Card.__init__(
            self,
            resource_type=BRICKS,
            dice_number=dice_number,
            initial_count=initial_count,
        )


resource_card_library.register(
    Clay_Pit_Card, initializer_dict={"dice_number": 1}
)
resource_card_library.register(
    Clay_Pit_Card, initializer_dict={"dice_number": 2}
)


class Field_Card(Resource_Card):
    def __init__(self, dice_number, initial_count=0):
        Resource_Card.__init__(
            self,
            resource_type=GRAIN,
            dice_number=dice_number,
            initial_count=initial_count,
        )


resource_card_library.register(Field_Card, initializer_dict={"dice_number": 3})
resource_card_library.register(Field_Card, initializer_dict={"dice_number": 4})


class Mountain_Card(Resource_Card):
    def __init__(self, dice_number, initial_count=0):
        Resource_Card.__init__(
            self,
            resource_type=IRON,
            dice_number=dice_number,
            initial_count=initial_count,
        )


resource_card_library.register(
    Mountain_Card, initializer_dict={"dice_number": 4}
)
resource_card_library.register(
    Mountain_Card, initializer_dict={"dice_number": 5}
)


class Meadow_Card(Resource_Card):
    def __init__(self, dice_number, initial_count=0):
        Resource_Card.__init__(
            self,
            resource_type=WOOL,
            dice_number=dice_number,
            initial_count=initial_count,
        )


resource_card_library.register(Meadow_Card, initializer_dict={"dice_number": 5})
resource_card_library.register(Meadow_Card, initializer_dict={"dice_number": 6})


class River_Card(Resource_Card):
    def __init__(self, dice_number, initial_count=0):
        Resource_Card.__init__(
            self,
            resource_type=GOLD,
            dice_number=dice_number,
            initial_count=initial_count,
        )


resource_card_library.register(River_Card, initializer_dict={"dice_number": 3})
