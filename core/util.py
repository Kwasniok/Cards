import random
import builtins


def random_pick(list):
    return list[random.randrange(len(list))]


def random_pop(list):
    elem = random_pick(list)
    list.remove(elem)
    return elem


class Randomized:
    def __init__(self, list):
        self._list = list
        self._order = builtins.list(range(len(self._list)))
        random.shuffle(self._order)

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        for x in self._order:
            yield self._list[x]
