from typing import Protocol

from app.commands.base import ICommand
from app.data_types.vector import Vector


class IChangeVelocity(Protocol):
    def set_velocity(self, velocity: Vector) -> int:
        raise NotImplementedError()


class ChangeVelocity(ICommand):
    obj: IChangeVelocity
    new_velocity: Vector

    def __init__(self, obj: IChangeVelocity, new_velocity: Vector) -> None:
        self.obj = obj
        self.new_velocity = new_velocity

    def execute(self) -> None:
        self.obj.set_velocity(self.new_velocity)
