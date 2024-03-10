from logging import info
from typing import Self

from devices.models import Device

from ..schemas import Message
from .protocol import NormaliserProtocol


class Deregister(NormaliserProtocol):
    is_device_available: bool
    device_id: str

    def __init__(self: Self, device_id: str) -> None:
        self.device_id = device_id
        self.is_device_available = Device.objects.filter(device_id=device_id).exists()

    def process(self: Self, message: Message) -> None:
        if self.is_device_available:
            Device.objects.filter(device_available=self.device_id).delete()
            info("Device successfully deregistered")
