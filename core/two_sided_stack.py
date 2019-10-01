class Two_Sided_Stack:
    def __init__(self):
        self._data = []

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self._data)

    def push_left(self, elem):
        self._data.insert(0, elem)

    def push_right(self, elem):
        self._data.append(elem)

    def pop_left(self):
        elem = self._data[0]
        del self._data[0]
        return elem

    def pop_right(self):
        elem = self._data[-1]
        del self._data[-1]
        return elem

    def get_left(self):
        return self._data[0]

    def get_right(self):
        return self._data[-1]

    def __contains__(self, elem):
        return elem in self._data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, key):
        return self._data[key]
