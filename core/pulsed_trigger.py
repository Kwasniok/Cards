import time
from .trigger import Trigger


# IDEA:
# A `Pulsed_Trigger` calls is `pull` method with a frequency of at most `max_pps` (pulls per second).
# Call its `update` method as frequently as possible (e.g. inside the man loop) to ensure a high frequency.


class Pulsed_Trigger(Trigger):
    def __init__(self, max_pps):
        Trigger.__init__(self)
        self._last_frame_time = time.time()
        self._max_pps = max_pps

    def update(self):
        t = time.time()
        if (t - self._last_frame_time) >= 1.0 / self._max_pps:
            self._last_frame_time = t
            self.pull()
            return True
        return False
