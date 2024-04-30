from typing import Self, Type

from helpers.managers import BaseManager

from .exceptions import ValidationFailedException
from .models import Plant
from .serializers import BasePlantSerializer as PlantSerializer


class BasePlantsManager(BaseManager):
    model: Type[Plant]
    serializer: Type[PlantSerializer]

    def __init__(
        self: Self, model: Type[Plant], serializer: Type[PlantSerializer]
    ) -> None:
        self.model = model
        self.serializer = serializer

    def get_list_of_items(self: Self) -> PlantSerializer:
        return self.serializer(self.model.objects.all(), many=True).data  # type: ignore

    def create_item(self: Self, data: dict[str, str]) -> PlantSerializer:
        serializer = self.serializer(data=data)

        if not serializer.is_valid():  # type: ignore
            raise ValidationFailedException(True, serializer.error_messages)

        serializer.create(validated_data=data)
        return serializer.data  # type: ignore
