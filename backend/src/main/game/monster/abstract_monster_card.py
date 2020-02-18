from abc import ABC

from backend.src.main.game.monster.values import TrapIndicators


class AbstractMonsterCard(ABC):  # pylint: disable=too-few-public-methods

    def __init__(self, name, map_values):
        self.map_values = map_values
        self.name = name

    def get_designation_by_number(self, index):
        return self.map_values[index]

    def get_trap_indicators(self):
        key = TrapIndicators.INDICATOR
        return self.map_values[key]
