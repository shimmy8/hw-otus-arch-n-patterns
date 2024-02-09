from typing import Any

import pytest

from app.data_types import Direction
from app.uobject import UniversalObject
from app.adapters.rotatable import RotatableAdapter
from app.commands.rotate import Rotate


class RotatableObjectMock(UniversalObject):
    direction: Direction
    angular_velocity: int

    def __init__(self, direction: Direction, angular_velocity: int) -> None:
        self.direction = direction
        self.angular_velocity = angular_velocity

    def get_attr(self, attr_name: str) -> Any:
        return getattr(self, attr_name, None)

    def set_attr(self, attr_name: str, attr_value: Any) -> None:
        return setattr(self, attr_name, attr_value)


@pytest.mark.parametrize(
    "direction,angular_velocity,expected_direction",
    [
        (Direction(45, 360), 10, Direction(55, 360)),
        (Direction(90, 360), 90, Direction(180, 360)),
    ],
)
def test_rotate(direction, angular_velocity, expected_direction):
    rotatable_obj = RotatableObjectMock(direction, angular_velocity)
    rotatable_adapter = RotatableAdapter(rotatable_obj)
    rotate = Rotate(rotatable_adapter)
    rotate.execute()
    assert rotatable_adapter.get_direction() == expected_direction


def test_object_no_direction_error():
    rotatable_obj = RotatableObjectMock(None, 5)
    rotatable_adapter = RotatableAdapter(rotatable_obj)
    rotate = Rotate(rotatable_adapter)
    with pytest.raises(ValueError):
        rotate.execute()


def test_object_no_angular_velocity_error():
    rotatable_obj = RotatableObjectMock(Direction(45, 360), None)
    rotatable_adapter = RotatableAdapter(rotatable_obj)
    rotate = Rotate(rotatable_adapter)
    with pytest.raises(ValueError):
        rotate.execute()


def test_any_object_error():
    obj = object()
    rotatable_adapter = RotatableAdapter(obj)
    rotate = Rotate(rotatable_adapter)
    with pytest.raises(AttributeError):
        rotate.execute()
