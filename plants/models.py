from typing import Self

from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    latin_name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        abstract = True

    def __str__(self: Self) -> str:
        return self.name


class Family(Plant):
    class Meta:  # type: ignore
        verbose_name_plural = "Families"


class Genus(Plant):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="genera")

    class Meta:  # type: ignore
        verbose_name_plural = "Genera"


class Species(Plant):
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE, related_name="species")
    latin_name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:  # type: ignore
        verbose_name_plural = "Species"


class Cultivar(Plant):
    species = models.ForeignKey(
        Species, on_delete=models.CASCADE, related_name="cultivars"
    )

    class Meta:  # type: ignore
        verbose_name_plural = "Cultivars"
