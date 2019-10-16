from ..action import action, Action_Invokation_Error
from ..phase import Phase, phase_library


class Main_Phase(Phase):
    def __init__(self):
        Phase.__init__(self, name="main phase", initially_active=True)


phase_library.register(Main_Phase)


class Draw_Phase(Phase):
    def __init__(self):
        Phase.__init__(self, name="draw phase")

    @action
    def on_activate(self, context):
        if not (context.active_phases == ["main phase"]):
            raise (Action_Invokation_Error())
        phase_manager = context.game_state.get_phase_manager()
        phase_manager.make_all_inactive()
        phase_manager.make_active(self)


phase_library.register(Draw_Phase)
