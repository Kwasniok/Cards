class Owner:
    def __init__(self, name, color=None):
        self._name = name
        self._color = color

    def __str__(self):
        return self._name

    def color(self, new=None):
        if new is None:
            old = self._color
            self._color = new
        else:
            return self._color


neutral_owner = Owner("neutral")


class Owned:
    def __init__(self, owner=neutral_owner):
        self._owner = owner

    def owner(self, new_owner=None):
        if new_owner is None:
            return self._owner
        else:
            new_owner, self._owner = self._owner, new_owner
            return new_owner
