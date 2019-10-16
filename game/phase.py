from abc import abstractmethod
from .game_object import Game_Object
from .action import action, Action_Invokation_Error
from .subtype_library import Subtype_Library


class Phase(Game_Object):
    @abstractmethod
    def __init__(self, name, initially_active=False):
        Game_Object.__init__(self, name=name)
        self._active = initially_active

    def get_name(self, context):
        return self._get_internal_name()

    def is_active(self):
        return self._active

    def __eq__(self, other):
        if type(other) == str:
            return self._get_internal_name() == other
        return self is other

    def _set_active(self):
        self._active = True

    def _set_inactive(self):
        self._active = False

    @action
    def on_activate(self, context):
        raise (
            Action_Invokation_Error(
                "Phase "
                + self.get_name(context)
                + " cannot be activated: Phase activation not permitted."
            )
        )


phase_library = Subtype_Library(Phase)
