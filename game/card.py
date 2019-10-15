from abc import ABC, abstractmethod
from core.internally_named import Internally_Named
from core.owning import Owned
from .neutral_owner import neutral_owner
from .action import action


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

    @action
    def on_inspect(self, context):
        print(
            "Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ",title="
            + str(self.get_title(context))
            + ",text="
            + str(self.get_text(context))
            + ",cost="
            + str(self.get_cost(context))
            + ",mill_pints="
            + str(self.get_mill_points(context))
            + ",knight_points="
            + str(self.get_knight_points(context))
            + ",win_points="
            + str(self.get_win_points(context))
            + ")"
        )
