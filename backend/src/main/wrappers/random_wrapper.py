import random


class RandomWrapper:  # pylint: disable=too-few-public-methods
    @staticmethod
    def randrange(stop):
        return random.randrange(stop)
