from core.owning import Owner


class Neutral_Owner(Owner):
    def __init__(self):
        Owner.__init__(self)


neutral_owner = Neutral_Owner()
