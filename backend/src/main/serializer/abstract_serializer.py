from abc import ABC


class AbstractSerializer(ABC):
    @staticmethod
    def serialize(object):
        raise NotImplementedError
