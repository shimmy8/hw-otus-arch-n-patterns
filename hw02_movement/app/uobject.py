from typing import Any
from typing import Protocol


class UniversalObject(Protocol):
    def get_attr(self, attr_name: str) -> Any:
        raise NotImplementedError()

    def set_attr(self, attr_name: str, attr_value: Any) -> None:
        raise NotImplementedError()
