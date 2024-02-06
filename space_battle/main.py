from typing import Any

from app.data_types import Direction
from app.data_types import Vector
from app.uobject import UniversalObject
from app.adapters.movable import MovableAdapter
from app.commands.move import Move


class SpaceShip(UniversalObject):
    direction = Direction(13, 360)
    position = Vector(12, 5)
    velocity = Vector(-7, 3)

    def get_attr(self, attr_name: str) -> Any:
        return getattr(self, attr_name, None)

    def set_attr(self, attr_name: str, attr_value: Any) -> None:
        return setattr(self, attr_name, attr_value)


mv_ad = MovableAdapter(universal_obj=SpaceShip())
mv_cmd = Move(movable_obj=mv_ad)
mv_cmd.execute()

print(mv_ad.get_position())
