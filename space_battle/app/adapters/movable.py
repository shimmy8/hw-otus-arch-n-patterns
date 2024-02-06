from app.commands.move import IMovable
from app.data_types import Vector
from app.uobject import UniversalObject


class MovableAdapter(IMovable):
    obj: UniversalObject

    def __init__(self, universal_obj: UniversalObject):
        self.obj = universal_obj

    def get_position(self) -> Vector:
        pos: Vector = self.obj.get_attr("position")
        if not isinstance(pos, Vector):
            raise ValueError("Invalid position type")
        return pos

    def set_position(self, new_position: Vector) -> None:
        return self.obj.set_attr("position", new_position)

    def get_velocity(self) -> Vector:
        velocity: Vector = self.obj.get_attr("velocity")
        if not isinstance(velocity, Vector):
            raise ValueError("Invalid velocity type")
        return velocity
