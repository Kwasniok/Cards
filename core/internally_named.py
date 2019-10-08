from abc import abstractmethod


class Internally_Named:
    @abstractmethod
    def __init__(self, name):
        self._internal_name = name

    def __str__(self):
        return self._internal_name

    def _set_internal_name(self, name):
        self._internal_name = name
