from typing import Protocol

from app.data_types.vector import Vector
from app.commands.base import ICommand


class IMovable(Protocol):
    def get_position(self) -> Vector:
        raise NotImplementedError()

    def get_velocity(self) -> Vector:
        raise NotImplementedError()

    def set_position(self, position: Vector) -> None:
        raise NotImplementedError()


class Move(ICommand):
    obj: IMovable

    def __init__(self, movable_obj: IMovable) -> None:
        self.obj = movable_obj

    def execute(self) -> None:
        self.obj.set_position(self.obj.get_position() + self.obj.get_velocity())
