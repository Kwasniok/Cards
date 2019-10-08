import time
from .trigger import Trigger


# IDEA:
# A `Pulsed_Trigger` calls is `pull` method with a frequency of at most
# `max_pps` (pulls per second).
#
# IMPORTANT:
# Call `Pulsed_Trigger.update_all()`  as frequently as possible (e.g. inside
# the main loop) to ensure the highest pulse frequency possible.


class Pulsed_Trigger(Trigger):

    _active_pulsed_triggers = []

    def __init__(self, max_pps, starts_stopped=False):
        Trigger.__init__(self)
        self._time_of_next_pull = None
        self._max_pps = max_pps
        if starts_stopped:
            self.stop()
        else:
            self.restart()

    def restart(self):
        if not (self in Pulsed_Trigger._active_pulsed_triggers):
            Pulsed_Trigger._active_pulsed_triggers.append(self)
        # first pull is one period in the furutre or later
        self._time_of_next_pull = time.perf_counter() + 1.0 / self._max_pps

    def stop(self):
        if self in Pulsed_Trigger._active_pulsed_triggers:
            Pulsed_Trigger._active_pulsed_triggers.remove(self)

    def is_active(self):
        return self in Pulsed_Trigger._active_pulsed_triggers

    @staticmethod
    def update_all():
        for pulsed_trigger in Pulsed_Trigger._active_pulsed_triggers:
            pulsed_trigger._update()

    @staticmethod
    def force_pull_all():
        for pulsed_trigger in Pulsed_Trigger._active_pulsed_triggers:
            pulsed_trigger.pull()

    def _update(self):
        t = time.perf_counter()
        if t >= self._time_of_next_pull:
            # next pull is the smalles integral amount of periods after the last which is in the future (pull drops on heavy load)
            while t >= self._time_of_next_pull:
                self._time_of_next_pull = (
                    self._time_of_next_pull + 1.0 / self._max_pps
                )
            self.pull()
