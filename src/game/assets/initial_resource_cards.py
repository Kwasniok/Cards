from game.resource_card import (
    initial_resource_card_library_black,
    initial_resource_card_library_white,
)
from .resource_cards import *

# black
initial_resource_card_library_black.register(
    River_Card, initializer_dict={"dice_number": 1, "initial_count": 1}
)
initial_resource_card_library_black.register(
    Field_Card, initializer_dict={"dice_number": 2, "initial_count": 1}
)
initial_resource_card_library_black.register(
    Mountain_Card, initializer_dict={"dice_number": 3, "initial_count": 1}
)
initial_resource_card_library_black.register(
    Meadow_Card, initializer_dict={"dice_number": 4, "initial_count": 1}
)
initial_resource_card_library_black.register(
    Wood_Card, initializer_dict={"dice_number": 5, "initial_count": 1}
)
initial_resource_card_library_black.register(
    Clay_Pit_Card, initializer_dict={"dice_number": 6, "initial_count": 1}
)

# white
initial_resource_card_library_white.register(
    Field_Card, initializer_dict={"dice_number": 1, "initial_count": 1}
)
initial_resource_card_library_white.register(
    Mountain_Card, initializer_dict={"dice_number": 2, "initial_count": 1}
)
initial_resource_card_library_white.register(
    Meadow_Card, initializer_dict={"dice_number": 3, "initial_count": 1}
)
initial_resource_card_library_white.register(
    Wood_Card, initializer_dict={"dice_number": 4, "initial_count": 1}
)
initial_resource_card_library_white.register(
    Clay_Pit_Card, initializer_dict={"dice_number": 5, "initial_count": 1}
)
initial_resource_card_library_white.register(
    River_Card, initializer_dict={"dice_number": 6, "initial_count": 1}
)
