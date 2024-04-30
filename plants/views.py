# isort: skip_file
from helpers.views import BaseAPIView

from .managers import BasePlantsManager
from .models import Cultivar, Family, Genus, Species
from .serializers import (
    CultivarSerializer,
    FamilySerializer,
    GenusSerializer,
    SpeciesSerializer,
)


class FamilyView(BaseAPIView):
    class Meta(BaseAPIView.Meta):
        model = Family
        serializer = FamilySerializer
        manager = BasePlantsManager(model, serializer)


class GenusView(BaseAPIView):
    class Meta(BaseAPIView.Meta):
        model = Genus
        serializer = GenusSerializer
        manager = BasePlantsManager(model, serializer)


class SpeciesView(BaseAPIView):
    class Meta(BaseAPIView.Meta):
        model = Species
        serializer = SpeciesSerializer
        manager = BasePlantsManager(model, serializer)


class CultivarView(BaseAPIView):
    class Meta(BaseAPIView.Meta):
        model = Cultivar
        serializer = CultivarSerializer
        manager = BasePlantsManager(model, serializer)
