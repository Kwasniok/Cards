from abc import abstractmethod
from game.action import action
from game.event_card import event_card_library, Event_Card as Basic_Event_Card


class Event_Card(Basic_Event_Card):
    @abstractmethod
    def __init__(self, name):
        Basic_Event_Card.__init__(self, name)

    def on_discovery_is_invokable(self, context):
        return (
            Basic_Event_Card.on_discovery_is_invokable(self, context)
            and "event phase" in context.active_phases
        )

    @action(on_discovery_is_invokable)
    def on_discovery(self, context):
        Basic_Event_Card.on_discovery(self, context)


class Turn_Of_The_Year_Card(Event_Card):
    def __init__(self):
        Event_Card.__init__(self, "Turn of the Year")

    def get_text(self, context):
        return "The event card stack is shuffled."

    @action(Event_Card.on_discovery_is_invokable)
    def on_discovery(self, context):
        print("TODO: shuffle event card stack")
        # TODO: shuffle event card stack


event_card_library.register(Turn_Of_The_Year_Card, amount=1)
