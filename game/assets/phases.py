from ..action import action, Action_Invokation_Error
from ..phase import Phase, phase_library


class Build_Phase(Phase):
    def __init__(self):
        Phase.__init__(self, name="build phase", initially_active=True)


phase_library.register(Build_Phase)
