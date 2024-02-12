from typing import Any

import pytest

from app.data_types import Vector
from app.data_types import Direction
from app.adapters.rotate_change_velocity import RotateChangeVelocityAdapter
from app.commands.macro.rotate_change_velocity import RotateChangeVelocity
from app.commands.check_fuel import NotEnoughFuelException
from app.uobject import UniversalObject


class ObjRotatesChangeVelocityMock(UniversalObject):
    position: Vector
    velocity: Vector
    direction: Direction
    angular_velocity: int

    def __init__(
        self,
        position: Vector,
        velocity: Vector,
        direction: Direction,
        angular_velocity: int,
    ) -> None:
        self.position = position
        self.velocity = velocity
        self.direction = direction
        self.angular_velocity = angular_velocity

    def get_attr(self, attr_name: str) -> Any:
        return getattr(self, attr_name, None)

    def set_attr(self, attr_name: str, attr_value: Any) -> None:
        return setattr(self, attr_name, attr_value)


@pytest.mark.parametrize(
    "position,velocity,direction,angular_velocity,new_velocity,expected_direction,expected_velocity",
    [
        (
            Vector(0, 0),
            Vector(10, 5),
            Direction(30, 360),
            10,
            Vector(5, 5),
            Direction(40, 360),
            Vector(5, 5),
        ),
        (
            Vector(20, 20),
            Vector(0, 5),
            Direction(45, 360),
            -15,
            Vector(5, 5),
            Direction(30, 360),
            Vector(5, 5),
        ),
    ],
)
def test_rotate_change_velocity(
    position,
    velocity,
    direction,
    angular_velocity,
    new_velocity,
    expected_direction,
    expected_velocity,
):
    obj = ObjRotatesChangeVelocityMock(
        position=position,
        velocity=velocity,
        direction=direction,
        angular_velocity=angular_velocity,
    )
    adapter = RotateChangeVelocityAdapter(obj)
    cmd = RotateChangeVelocity(adapter, new_velocity)
    cmd.execute()

    assert adapter.get_direction() == expected_direction
    assert adapter.get_velocity() == expected_velocity
