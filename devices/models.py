from typing import Self

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Device(BaseModel):
    device_id = models.CharField(max_length=100, unique=True)
    services = models.ManyToManyField("Service", related_name="devices")

    def __str__(self: Self) -> str:
        return self.device_id


class Measurement(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    value = models.FloatField()


class Service(models.Model):
    name = models.CharField(max_length=100)
