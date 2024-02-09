from app.data_types.vector import Vector
from app.commands.macro.base import MacroCommand
from app.commands.rotate import IRotateble
from app.commands.rotate import Rotate
from app.commands.change_velocity import IChangeVelocity
from app.commands.change_velocity import ChangeVelocity
from app.commands.move import IMovable


class IRotateChangeVelocity(IRotateble, IChangeVelocity, IMovable):
    pass


class RotateChangeVelocity(MacroCommand):
    def __init__(self, obj: IRotateChangeVelocity, new_velocity: Vector) -> None:
        self.commands = [
            Rotate(obj),
            ChangeVelocity(obj, new_velocity),
        ]
