from abc import ABC, abstractmethod
from core.owning import Owned
from .neutral_owner import neutral_owner


class Card(ABC, Owned):
    @abstractmethod
    def __init__(self, name, face_up=False):
        Owned.__init__(self, neutral_owner)
        self._name = name
        self._face_up = face_up

    def __str__(self):
        return self._name

    def get_name(self):
        return self._name

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
