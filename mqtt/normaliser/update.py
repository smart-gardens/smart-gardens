from logging import warning
from typing import Self

from devices.models import Device, Measurement

from ..schemas import Message
from .protocol import NormaliserProtocol


class Update(NormaliserProtocol):
    is_device_available: bool
    device_id: str

    def __init__(self: Self, device_id: str) -> None:
        self.device_id = device_id
        self.is_device_available = Device.objects.filter(device_id=device_id).exists()

    def process(self: Self, message: Message) -> None:
        if self.is_device_available:
            device = Device.objects.get(device_id=self.device_id)
            measurement = Measurement(device=device, value=message.value)
            measurement.save()
        else:
            warning("Device not available")
