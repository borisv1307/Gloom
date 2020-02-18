from enum import Enum

from backend.src.main.serializer.abstract_serializer import AbstractSerializer


class EnumSerializer(AbstractSerializer):
    def serialize(self, serializable_object: Enum):
        return serializable_object.value

    @staticmethod
    def create():
        return EnumSerializer()
