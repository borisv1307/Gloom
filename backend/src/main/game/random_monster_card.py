from abc import ABC


class RandomMonsterCard(ABC):  # pylint: disable=too-few-public-methods

    def __init__(self, name, map_values):
        self.map_values = map_values
        self.name = name

    def get_designation_by_number(self, index):
        return self.map_values[index]
