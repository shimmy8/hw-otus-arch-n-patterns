from app.commands.rotate import IRotateble
from app.data_types import Direction
from app.uobject import UniversalObject


class RotatableAdapter(IRotateble):
    obj: UniversalObject

    def __init__(self, universal_obj: UniversalObject):
        self.obj = universal_obj

    def get_direction(self) -> Direction:
        direction: Direction = self.obj.get_attr("direction")
        if not isinstance(direction, Direction):
            raise ValueError("Invalid direction type")
        return direction

    def set_direction(self, new_direction: Direction) -> None:
        return self.obj.set_attr("direction", new_direction)

    def get_angular_velocity(self) -> int:
        velocity: int = self.obj.get_attr("angular_velocity")
        if not isinstance(velocity, int):
            raise ValueError("Invalid angular velocity type")
        return velocity
