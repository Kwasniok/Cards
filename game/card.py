from abc import ABC, abstractmethod
from core.internally_named import Internally_Named
from core.owning import Owned
from .neutral_owner import neutral_owner


class Card(ABC, Internally_Named, Owned):
    @abstractmethod
    def __init__(self, name, face_up=False):
        Internally_Named.__init__(self, name)
        Owned.__init__(self, neutral_owner)
        self._face_up = face_up

    def __repr__(self):
        return (
            "Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    def is_face_up(self):
        return self._face_up

    def make_face_up(self):
        self._face_up = True

    def make_face_down(self):
        self._face_up = False

    def toggle_face(self):
        self._face_up = not self._face_up

    def get_title(self, context):
        return self._get_internal_name()

    def get_text(self, context):
        return ""

    def get_cost(self, context):
        return []

    def get_mill_points(self, context):
        return 0

    def get_knight_points(self, context):
        return 0

    def get_win_points(self, context):
        return 0
