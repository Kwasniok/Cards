from collections import Counter

event_histogram = {
    "QUESTIONMARK": 2,
    "MILL": 1,
    "KNIGHT": 1,
    "CUDGEL": 1,
    "SUN": 1,
}


def get_event_dice_outcomes():
    return list(Counter(**event_histogram).elements())
