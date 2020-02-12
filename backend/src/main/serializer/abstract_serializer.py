from abc import ABC


class AbstractSerializer(ABC):  # pylint: disable=too-few-public-methods

    def serialize(self, serializable_object):
        raise NotImplementedError
