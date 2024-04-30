import serializers

from helpers.views import BaseAPIView

from .managers import BasePlantsManager
from .models import Cultivar, Family, Genus, Species


class FamilyView(BaseAPIView):
    class Meta(BaseAPIView.Meta):
        model = Family
        serializer = serializers.FamilySerializer
        manager = BasePlantsManager(model, serializer)


class GenusView(BaseAPIView):
    class Meta(BaseAPIView.Meta):
        model = Genus
        serializer = serializers.GenusSerializer
        manager = BasePlantsManager(model, serializer)


class SpeciesView(BaseAPIView):
    class Meta(BaseAPIView.Meta):
        model = Species
        serializer = serializers.SpeciesSerializer
        manager = BasePlantsManager(model, serializer)


class CultivarView(BaseAPIView):
    class Meta(BaseAPIView.Meta):
        model = Cultivar
        serializer = serializers.CultivarSerializer
        manager = BasePlantsManager(model, serializer)
