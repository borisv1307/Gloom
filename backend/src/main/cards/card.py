from abc import ABC


class Card(ABC):  # pylint:disable=too-few-public-methods

    def __init__(self, name):
        self.name = name
