from typing import Self, Type

from rest_framework.serializers import ModelSerializer

from .models import Cultivar, Family, Genus, Plant, Species


class BasePlantSerializer(ModelSerializer):
    class Meta:
        model: Type[Plant]
        fields = "__all__"

    def create(self: Self, validated_data: dict[str, str]) -> Plant:
        item = self.Meta.model(**validated_data)
        item.save()
        return item


class FamilySerializer(BasePlantSerializer):
    class Meta(BasePlantSerializer.Meta):
        model = Family


class GenusSerializer(BasePlantSerializer):
    class Meta(BasePlantSerializer.Meta):
        model = Genus


class SpeciesSerializer(BasePlantSerializer):
    class Meta(BasePlantSerializer.Meta):
        model = Species


class CultivarSerializer(BasePlantSerializer):
    class Meta(BasePlantSerializer.Meta):
        model = Cultivar
