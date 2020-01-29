"""Random Monster Class:
Creating Random Monster Card. Name and value mapper"""
from abc import ABC


class RandomMonsterCard(ABC):  # pylint: disable=too-few-public-methods
    """ Class for Random Monster Card """

    def __init__(self, name, map_values):
        self.map_values = map_values
        self.name = name

    def get_designation_by_number(self, index):
        return self.map_values[index]
