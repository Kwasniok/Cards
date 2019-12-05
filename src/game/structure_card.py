from abc import abstractmethod
from game.card import Card


class Structure_Card(Card):
    @abstractmethod
    def __init__(self, name):
        Card.__init__(self, name=name)

    def __repr__(self):
        return (
            "Structure_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    def get_title(self, context):
        return self._get_internal_name()
