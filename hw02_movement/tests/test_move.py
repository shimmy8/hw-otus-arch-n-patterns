from typing import Any

import pytest

from app.data_types import Vector
from app.uobject import UniversalObject
from app.adapters.movable import MovableAdapter
from app.commands.move import Move


class MovalbeObjMock(UniversalObject):
    position: Vector
    velocity: Vector

    def __init__(self, position: Vector, velocity: Vector) -> None:
        self.position = position
        self.velocity = velocity

    def get_attr(self, attr_name: str) -> Any:
        return getattr(self, attr_name, None)

    def set_attr(self, attr_name: str, attr_value: Any) -> None:
        return setattr(self, attr_name, attr_value)


@pytest.mark.parametrize(
    "position, velocity, expected_position",
    [
        (Vector(0, 0), Vector(1, 1), Vector(1, 1)),
        (Vector(12, 5), Vector(-7, 3), Vector(5, 8)),
        (Vector(-10, -5), Vector(20, 15), Vector(10, 10)),
    ],
)
def test_movement(position, velocity, expected_position):
    movable_obj = MovalbeObjMock(position, velocity)
    movable_adapter = MovableAdapter(movable_obj)
    move = Move(movable_adapter)
    move.execute()
    assert movable_adapter.get_position() == expected_position


def test_object_no_position_error():
    movable_obj = MovalbeObjMock(None, Vector(1, 1))
    movable_adapter = MovableAdapter(movable_obj)
    move = Move(movable_adapter)
    with pytest.raises(ValueError):
        move.execute()


def test_object_no_velocity_error():
    movable_obj = MovalbeObjMock(Vector(1, 1), None)
    movable_adapter = MovableAdapter(movable_obj)
    move = Move(movable_adapter)
    with pytest.raises(ValueError):
        move.execute()


def test_any_object_error():
    obj = object()
    movable_adapter = MovableAdapter(obj)
    move = Move(movable_adapter)
    with pytest.raises(AttributeError):
        move.execute()
