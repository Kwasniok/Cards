from collections import Counter

EVENT_HISTOGRAM = {
    "QUESTIONMARK": 2,
    "MILL": 1,
    "KNIGHT": 1,
    "CUDGEL": 1,
    "SUN": 1,
}
EVENTS = EVENT_HISTOGRAM.keys()
EVENT_DICE_OUTCOMES = list(Counter(**EVENT_HISTOGRAM).elements())
