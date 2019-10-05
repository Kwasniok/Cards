import time
from .update import Updater


class Frequency_Updater(Updater):
    def __init__(self, max_ups):
        Updater.__init__(self)
        self._last_frame_time = time.time()
        self._max_ups = max_ups

    def update_all(self):
        t = time.time()
        if (t - self._last_frame_time) >= 1.0 / self._max_ups:
            self._last_frame_time = t
            return Updater.update_all(self)
        return False

    def force_update_all(self):
        return Updater.update_all(self)
