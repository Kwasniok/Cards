from abc import ABC, abstractmethod


class Updatable(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def on_update(self):
        pass


class Updater:
    def __init__(self):
        self._updatables = []

    def register_updatable(self, updatable):
        if not isinstance(updatable, Updatable):
            raise (
                RuntimeError(
                    "Cannot register non Updatable object in an updater."
                )
            )
        if not (updatable in self._updatables):
            self._updatables.append(updatable)

    def unregister_updatable(self, updatable):
        if updatable in self._updatables:
            self._updatables.remove(updatable)

    def clear(self):
        self._updatables = []

    def update_all(self):
        for obj in self._updatables:
            obj.on_update()
