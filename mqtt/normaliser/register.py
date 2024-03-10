from logging import error, info, warning
from typing import Self

from devices.models import Device

from ..schemas import Message
from .protocol import NormaliserProtocol


class Register(NormaliserProtocol):
    is_device_available: bool
    device_id: str

    def __init__(self: Self, device_id: str) -> None:
        self.device_id = device_id
        self.is_device_available = Device.objects.filter(device_id=device_id).exists()

    def process(self: Self, message: Message) -> None:
        try:
            if not self.is_device_available:
                warning("Device is not available")
                device = Device(device_id=self.device_id)
                device.save()
            else:
                info("Device exists, skipping registration")
        except Device.DoesNotExist:
            error("Device doesn't exist")
