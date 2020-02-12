from enum import Enum

from backend.src.main.serializer.abstract_serializer import AbstractSerializer


class EnumSerializer(AbstractSerializer):
    def serialize(self, enum: Enum):
        return enum.value
