from random import randrange


def random_pick(list):
    return list[randrange(len(list))]


def random_pop(list):
    elem = random_pick(list)
    list.remove(elem)
    return elem
