from abc import abstractmethod


class Owner:
    @abstractmethod
    def __init__(self):
        pass


class Owned:
    @abstractmethod
    def __init__(self, owner):
        self._owner = None
        self.change_owner(owner)

    def get_owner(self):
        return self._owner

    def change_owner(self, owner):
        if not isinstance(owner, Owner):
            raise (
                TypeError(
                    "Cannot change owner of "
                    + str(self)
                    + " due to invalid owner "
                    + str(owner)
                    + " (must be a "
                    + str(Owner)
                    + ")."
                )
            )
        self._owner = owner
