from ..action import action, Action_Invokation_Error
from ..phase import Phase, phase_library


class Main_Phase(Phase):
    def __init__(self):
        Phase.__init__(self, name="main phase", initially_active=True)


phase_library.register(Main_Phase)
