import time
from .update import Updater


class FPS_Updater(Updater):
    def __init__(self, fps_bound):
        Updater.__init__(self)
        self._last_frame_time = time.time()
        self._fps_bound = fps_bound

    def update_all(self):
        t = time.time()
        if (t - self._last_frame_time) >= 1.0 / self._fps_bound:
            self._last_frame_time = t
            return Updater.update_all(self)
        return False

    def force_update_all(self):
        return Updater.update_all(self)
