from typing import Any

import pytest

from app.adapters.change_velocity import ChangeVelocityAdapter
from app.data_types.vector import Vector
from app.commands.change_velocity import ChangeVelocity
from app.uobject import UniversalObject


class ObjCanChangeVelocityMock(UniversalObject):
    velocity: Vector

    def __init__(self, velocity: Vector) -> None:
        self.velocity = velocity

    def get_attr(self, attr_name: str) -> Any:
        return getattr(self, attr_name, None)

    def set_attr(self, attr_name: str, attr_value: Any) -> None:
        return setattr(self, attr_name, attr_value)


@pytest.mark.parametrize(
    "obj_velocity,new_velocity,expected_velocity",
    [
        (Vector(0, 0), Vector(10, 10), Vector(10, 10)),
        (Vector(50, 100), Vector(1, -1), Vector(1, -1)),
    ],
)
def test_change_velocity(obj_velocity, new_velocity, expected_velocity):
    obj = ObjCanChangeVelocityMock(velocity=obj_velocity)
    adapter = ChangeVelocityAdapter(obj)
    cmd = ChangeVelocity(adapter, new_velocity)

    cmd.execute()

    assert adapter.get_velocity() == expected_velocity
