from typing import Protocol, Self


class NormaliserProtocol(Protocol):
    is_device_available: bool
    device_id: str

    def process(self: Self, message) -> None: ...
