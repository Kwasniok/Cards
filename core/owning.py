class Owner:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

    def color(self):
        return color


neutral_owner = Owner("neutral")


class Owned:
    def __init__(self, owner=neutral_owner):
        self.owner = owner

    def owner(new_owner=None):
        if new_owner:
            new_owner, self.owner = self.owner, new_owner
            return new_owner
        else:
            return self.owner
