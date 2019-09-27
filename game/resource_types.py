class Resource_Type:
    def __init__(self, name, source_name):
        self._name = name
        self.source = source_name

    def __str__(self):
        return self._name

    def name(self):
        return self._name

    def source_name(self):
        return self.source


LOGS = Resource_Type("Logs", "Woods")
BRICKS = Resource_Type("Bricks", "Clay Pit")
GRAIN = Resource_Type("Grain", "Field")
IRON = Resource_Type("Iron", "Mountain")
WOOL = Resource_Type("Wool", "Meadow")
GOLD = Resource_Type("Gold", "River")
