from typing import Protocol

from app.data_types.direction import Direction


class IRotateble(Protocol):
    def get_direction(self) -> Direction:
        raise NotImplementedError()

    def set_direction(self, direction: Direction) -> None:
        raise NotImplementedError()

    def get_angular_velocity(self) -> int:
        raise NotImplementedError()


class Rotate:
    obj: IRotateble

    def __init__(self, rotateble_obj: IRotateble) -> None:
        self.obj = rotateble_obj

    def execute(self) -> None:
        self.obj.set_direction(
            self.obj.get_direction().to_next(self.obj.get_angular_velocity())
        )
