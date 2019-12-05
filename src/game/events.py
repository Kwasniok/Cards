from collections import Counter

event_histogram = {}


def get_event_dice_outcomes():
    return list(Counter(**event_histogram).elements())
