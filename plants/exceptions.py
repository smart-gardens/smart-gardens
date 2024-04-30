from typing import Any, Self


class NoIDProvidedException(Exception): ...


class ValidationFailedException(Exception):
    error: bool
    message: Any

    def __init__(self: Self, error: bool, message: Any) -> None:
        self.error = error
        self.message = message
