from abc import ABC


class RandomMonsterCard(ABC):
    def __init__(self, name, map_values={}):
        self.map_values = map_values
        self.name = name
