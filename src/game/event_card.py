from abc import abstractmethod
from .action import action
from game.card import Card
from .subtype_library import Subtype_Library


class Event_Card(Card):
    @abstractmethod
    def __init__(self, name):
        Card.__init__(self, name)

    def __repr__(self):
        return (
            "Event_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    def on_discovery_is_invokable(self, context):
        event_card_intake_stack = (
            context.game_state.get_neutral_zone().get_event_card_intake_stack()
        )
        return (
            not event_card_intake_stack.is_empty()
            and self is event_card_intake_stack.get_top()
        )

    @action(on_discovery_is_invokable)
    def on_discovery(self, context):
        context.game_state.get_neutral_zone().get_event_card_intake_stack().remove(
            self
        )
        context.game_state.get_neutral_zone().get_event_card_tray_stack().push_top(
            self
        )


event_card_library = Subtype_Library(Event_Card)
