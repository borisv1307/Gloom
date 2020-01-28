"""Card class."""
from abc import ABC


class Card(ABC):
    """Card class to init card."""

    def __init__(self, name):
        self.name = name
