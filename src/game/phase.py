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

    def on_activate_is_invokable(self, context):
        return False

    @action(on_activate_is_invokable)
    def on_activate(self, context):
        pass


class Turn_Phase(Phase):
    @abstractmethod
    def __init__(
        self, name, initially_active=False, required_previous_phases=None
    ):
        Phase.__init__(self, name=name, initially_active=initially_active)
        self._active = initially_active
        if required_previous_phases is None:
            self._required_previous_phases = []
        else:
            self._required_previous_phases = required_previous_phases

    def on_activate_is_invokable(self, context):
        active = len(self._required_previous_phases) == 0
        for required_previous_phase in self._required_previous_phases:
            if required_previous_phase in context.active_phases:
                active = True
        if not active:
            return False
        return True

    @action(on_activate_is_invokable)
    def on_activate(self, context):
        phase_manager = context.game_state.get_turn_phase_manager()
        phase_manager.make_all_inactive()
        phase_manager.make_active(self)


turn_phase_library = Subtype_Library(Phase)
