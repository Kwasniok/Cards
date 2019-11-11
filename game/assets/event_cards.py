from abc import abstractmethod
from core.random import random_pop
from game.action import action
from game.event_card import event_card_library, Event_Card as Basic_Event_Card


class Event_Card(Basic_Event_Card):
    @abstractmethod
    def __init__(self, name):
        Basic_Event_Card.__init__(self, name)

    def on_discovery_is_invokable(self, context):
        last_event_dice_outcome = (
            context.game_state.get_neutral_zone()
            .get_event_dice()
            .get_last_outcome()
        )
        return (
            Basic_Event_Card.on_discovery_is_invokable(self, context)
            and "event phase" in context.active_phases
            and last_event_dice_outcome == "QUESTIONMARK"
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
        Event_Card.on_discovery(self, context)
        # put all event cards into the event card intake stack and shuffle it
        event_card_tray_stack = (
            context.game_state.get_neutral_zone().get_event_card_tray_stack()
        )
        event_card_intake_stack = (
            context.game_state.get_neutral_zone().get_event_card_intake_stack()
        )
        event_cards = (
            event_card_tray_stack.pop_all() + event_card_intake_stack.pop_all()
        )
        while event_cards:
            event_card_intake_stack.push_top(random_pop(event_cards))


event_card_library.register(Turn_Of_The_Year_Card, amount=1)


class Productive_Year_Card(Event_Card):
    def __init__(self):
        Event_Card.__init__(self, "Productive Year")

    def get_text(self, context):
        return "Each resource neighbouring a storage building yeilds an additional resource unit."

    @action(Event_Card.on_discovery_is_invokable)
    def on_discovery(self, context):
        # TODO: implement productive year card
        print("TODO: implement productive year card")
        Event_Card.on_discovery(self, context)


event_card_library.register(Productive_Year_Card, amount=2)
