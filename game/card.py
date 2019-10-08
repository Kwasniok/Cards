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

    def is_face_up(self):
        return self._face_up

    def make_face_up(self):
        self._face_up = True

    def make_face_down(self):
        self._face_up = False

    def toggle_face(self):
        self._face_up = not self._face_up

    def title(self, context):
        return name

    def text(self, context):
        return ""

    def cost(self, context):
        return []

    def mill_points(self, context):
        return 0

    def knight_points(self, context):
        return 0

    def win_points(self, context):
        return 0
