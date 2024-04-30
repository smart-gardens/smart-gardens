from django.urls import path

from .views import CultivarView, FamilyView, GenusView, SpeciesView

app_name = "plants"

urlpatterns = [
    path("family/", FamilyView.as_view(), name="families"),
    path("genus/", GenusView.as_view(), name="genera"),
    path("species/", SpeciesView.as_view(), name="species"),
    path("cultivar/", CultivarView.as_view(), name="cultivars"),
]
