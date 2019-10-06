import time
from .trigger import Trigger


# IDEA:
# A `Pulsed_Trigger` calls is `pull` method with a frequency of at most `max_pps` (pulls per second).
# Call its `update` method as frequently as possible (e.g. inside the man loop) to ensure a high frequency.


class Pulsed_Trigger(Trigger):
    def __init__(self, max_pps):
        Trigger.__init__(self)
        self._time_of_next_pull = None
        self._max_pps = max_pps
        self.restart()

    def restart(self):
        # first pull is one period in the furutre or later
        self._time_of_next_pull = time.perf_counter() + 1.0 / self._max_pps

    def update(self):
        t = time.perf_counter()
        if t >= self._time_of_next_pull:
            # next pull is the smalles integral amount of periods after the last which is in the future (pull drops on heavy load)
            while t >= self._time_of_next_pull:
                self._time_of_next_pull = (
                    self._time_of_next_pull + 1.0 / self._max_pps
                )
            self.pull()
            return True
        return False
