from abc import ABC


class AbstractSerializer(ABC):

    def serialize(self, serializable_object):
        raise NotImplementedError
