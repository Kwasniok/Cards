from game.action import action
from game.event_card import event_card_library, Event_Card


class Turn_Of_The_Year_Card(Event_Card):
    def __init__(self):
        Event_Card.__init__(self, "Turn of the Year")

    def get_text(self, context):
        return "The event card stack is shuffled."

    @action()
    def on_discovery(self, context):
        print("TODO: shuffle event card stack")
        # TODO: shuffle event card stack


event_card_library.register(Turn_Of_The_Year_Card, amount=1)
