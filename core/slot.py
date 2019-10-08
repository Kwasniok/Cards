import math


class Slot_Error(RuntimeError):
    def __init__(self, msg):
        RuntimeError.__init__(self, msg)


class Slot_Empty_Error(Slot_Error):
    def __init__(self, msg):
        Slot_Error.__init__(self, msg)


class Slot_Full_Error(Slot_Error):
    def __init__(self, msg):
        Slot_Error.__init__(self, msg)


class Slot:
    def __init__(self, accepted_base_types, limit=math.inf):
        self._accepted_base_types = accepted_base_types
        self._limit = limit
        self._objects = []

    def __repr__(self):
        return (
            "Slot(accepted_base_types=["
            + ", ".join([typ.__name__ for typ in self._accepted_base_types])
            + "], limit="
            + str(self._limit)
            + ", objects=["
            + (", ".join(repr(c) for c in self._objects))
            + "])"
        )

    def __len__(self):
        return len(self._objects)

    def __getitem__(self, index):
        return self._objects[index]

    def get_top(self):
        return self._objects[-1]

    def __setitem__(self, index, obj):
        self._objects[index] = obj

    def __contains__(self, obj):
        return obj in self._objects

    def __iter__(self):
        return iter(self._objects)

    def get_accepted_base_types(self):
        return self._accepted_base_types

    def get_limit(self):
        return self._limit

    def set_limit(self, limit):
        self._limit = limit

    def is_empty(self):
        return len(self._objects) == 0

    def is_full(self):
        return len(self._objects) >= self._limit

    def accepts_type(self, type):
        print(type)
        print(tuple(self._accepted_base_types))
        return issubclass(type, tuple(self._accepted_base_types))

    def would_accept(self, obj):
        if obj in self:
            return False
        if self.is_full():
            return False
        if not self.accepts_type(type(obj)):
            return False
        return True

    def is_accepted_type(self, type):
        return issubclass(type, tuple(self._accepted_base_types))

    # checks allways in this order:
    # 1) obj allready in slot --> ValueError
    # 2) slot full --> Slot_Full_Error
    # 3) not of accepted type --> TypeError
    def add(self, obj):
        if obj in self:
            raise ValueError(
                "Cannot add `"
                + str(obj)
                + "` to slot `"
                + str(self)
                + "` : Object allready in slot."
            )
        if self.is_full():
            raise Slot_Full_Error(
                "Cannot add `"
                + str(obj)
                + "` to slot `"
                + str(self)
                + "`: Reached slot limit of "
                + str(self._limit)
                + "."
            )
        if not self.accepts_type(type(obj)):
            raise TypeError(
                "Cannot add `"
                + str(obj)
                + "` of type `"
                + str(type(obj))
                + "` to slot `"
                + str(self)
                + "`: Object must be an instance of type"
                + ", ".join(
                    "`" + str(t) + "`" for t in self._accepted_base_types
                )
                + " or any derived type."
            )
        self._objects.append(obj)

    def remove(self, obj):
        if obj in self._objects:
            self._objects.remove(obj)

    def pop_top(self):
        if self.is_empty():
            raise (
                Slot_Empty_Error(
                    "Cannnot pop top of slot " + str(self) + ": Slot is empty."
                )
            )
        obj = self._objects[-1]
        self.remove(obj)
        return obj
