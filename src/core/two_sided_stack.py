class Two_Sided_Stack:
    def __init__(self):
        self._objects = []

    def __str__(self):
        return str(self._objects)

    def __repr__(self):
        return repr(self._objects)

    def push_left(self, elem):
        self._objects.insert(0, elem)

    def push_right(self, elem):
        self._objects.append(elem)

    def pop_left(self):
        elem = self._objects[0]
        del self._objects[0]
        return elem

    def pop_right(self):
        elem = self._objects[-1]
        del self._objects[-1]
        return elem

    def get_left(self):
        return self._objects[0]

    def get_right(self):
        return self._objects[-1]

    def __contains__(self, elem):
        return elem in self._objects

    def __len__(self):
        return len(self._objects)

    def __iter__(self):
        return iter(self._objects)

    def __getitem__(self, key):
        return self._objects[key]
