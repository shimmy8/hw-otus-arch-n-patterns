from app.adapters.movable import MovableAdapter
from app.data_types.vector import Vector
from app.commands.change_velocity import IChangeVelocity
from app.uobject import UniversalObject


class ChangeVelocityAdapter(IChangeVelocity, MovableAdapter):
    obj: UniversalObject

    def __init__(self, universal_obj: UniversalObject) -> None:
        self.obj = universal_obj

    def set_velocity(self, new_velocity: Vector) -> None:
        self.obj.set_attr("velocity", new_velocity)
