from enum import Enum


class MessageTypes(str, Enum):
    REGISTER = "register"
    DEREGISTER = "deregistration"
    UPDATE = "update"
