from enum import Enum

from backend.src.main.serializer.abstract_serializer import AbstractSerializer


class EnumSerializer(AbstractSerializer):  # pylint: disable=too-few-public-methods
    def serialize(self, serializable_object: Enum):
        return serializable_object.value
