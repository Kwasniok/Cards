from abc import abstractmethod
from game.card import Card


class Event_Card(Card):
    def __init__(self, name):
        Card.__init__(self, name)

    def __repr__(self):
        return (
            "Event_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    @abstractmethod
    def on_discovery(self, context):
        pass
