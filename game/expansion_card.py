from abc import abstractmethod
from game.card import Card
from .subtype_library import Subtype_Library
from .action import action, Action_Invokation_Error
from .card_slot import Card_Slot


class Expansion_Card(Card):
    @abstractmethod
    def __init__(self, name):
        Card.__init__(self, name)

    def __repr__(self):
        return (
            "Expansion_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    @abstractmethod
    def is_playable(self, context):
        pass


expansion_card_library = Subtype_Library(Expansion_Card)


class Action_Card(Expansion_Card):
    @abstractmethod
    def __init__(self, name):
        Expansion_Card.__init__(self, name)

    def __repr__(self):
        return (
            "Action_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )


class Building_Card(Expansion_Card):
    @abstractmethod
    def __init__(self, name):
        Expansion_Card.__init__(self, name)

    def __repr__(self):
        return (
            "Building_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    def is_playable(self, context):
        # TODO: on own turn
        return True

    def on_construction_is_invokable(self, context, card_slot: Card_Slot):
        if not (self.get_owner() == context.active_player):
            return False
        if not ("main phase" in context.active_phases):
            return False
        if not card_slot.would_accept(self):
            return False
        return True

    @action(on_construction_is_invokable)
    def on_construction(self, context, card_slot: Card_Slot):
        card_slot.add(self)
        self.make_face_up()
        context.active_player.get_hand().remove(self)

    def on_destruction_is_invokable(self, context, card_slot: Card_Slot):
        return False

    @action(on_destruction_is_invokable)
    def on_destruction(self, context, card_slot: Card_Slot):
        pass


class Small_Building_Card(Building_Card):
    @abstractmethod
    def __init__(self, name):
        Building_Card.__init__(self, name)

    def __repr__(self):
        return (
            "Small_Building_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )


class Large_Building_Card(Building_Card):
    @abstractmethod
    def __init__(self, name):
        Building_Card.__init__(self, name)

    def __repr__(self):
        return (
            "Large_Building_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )
