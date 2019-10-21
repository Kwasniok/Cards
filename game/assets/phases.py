from ..action import action, Action_Invokation_Error
from ..phase import Phase, phase_library


class Main_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self,
            name="main phase",
            initially_active=True,
            required_previous_phases=["draw phase"],
        )


phase_library.register(Main_Phase)


class Draw_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self, name="draw phase", required_previous_phases=["main phase"]
        )


phase_library.register(Draw_Phase)
