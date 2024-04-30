from typing import Any, Self


class BaseManager:
    def get_list_of_items(self: Self) -> Any: ...

    def create_item(self: Self, data: dict[str, str]) -> Any: ...
