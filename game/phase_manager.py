from core.internally_named import Internally_Named
from .phase import phase_library


class Phase_Manager(Internally_Named):
    def __init__(self, name):
        Internally_Named.__init__(self, name=name)
        self._phases = phase_library.get_all()
        print(self._phases)

    def __len__(self):
        return len(self._phases)

    def __getitem__(self, index):
        return self._phases[index]

    def get_active_phases(self):
        active_phases = []
        for phase in self._phases:
            if phase.is_active():
                active_phases.append(phase)
        return active_phases

    def get_inactive_phases(self):
        active_phases = []
        for phase in self._phases:
            if not phase.is_active():
                active_phases.append(phase)
        return active_phases

    def get_all_phases(self):
        return self._phases[:]

    def add(self, phase):
        if phase in self._phases:
            return
        self._phases.append(phase)

    def remove(self, phase):
        if phase in self._phases:
            self._phases.remove(phase)

    def make_active(self, phase):
        for p in self._phases:
            if p == phase:
                p._set_active()

    def make_inactive(self, phase):
        for p in self._phases:
            if p == phase:
                p._set_inactive()

    def make_all_inactive(self):
        for p in self._phases:
            p._set_inactive()
