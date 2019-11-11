from abc import ABC, abstractmethod
from core.internally_named import Internally_Named
from core.owning import Owned
from .neutral_owner import neutral_owner
from .action import register_supported_action_additional_argument_type, action


class Game_Object(ABC, Internally_Named, Owned):

    _id_counter = 0

    @staticmethod
    def _next_id():
        Game_Object._id_counter += 1
        return Game_Object._id_counter

    @abstractmethod
    def __init__(self, name, owner=neutral_owner):
        Internally_Named.__init__(self, name)
        Owned.__init__(self, owner)
        self._id = Game_Object._next_id()

    def get_id(self):
        return self._id

    def __repr__(self):
        return (
            "Game_Object(name="
            + str(self)
            + ",owner="
            + str(self.get_owner())
            + ",id="
            + str(self._id)
            + ")"
        )

    @action()
    def on_inspect(self, context):
        print(repr(self))


register_supported_action_additional_argument_type(Game_Object)
