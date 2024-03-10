from pydantic import BaseModel

from .enums import MessageTypes


class Message(BaseModel):
    message_type: MessageTypes
    device_id: str
    value: int | float | None = None
