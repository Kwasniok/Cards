from abc import ABC, abstractmethod
from .owning import Owned


class Card(ABC, Owned):
    def __init__(self, name, face_up=False):
        self.name = name
        self.face_up = face_up

    def __str__(self):
        return self.name

    def is_face_up(self):
        return self.face_up

    def make_face_up(self):
        self.face_up = True

    def make_face_down(self):
        self.face_up = False

    def toggle_face(self):
        self.face_up = not self.face_up

    @abstractmethod
    def text(self):
        pass
