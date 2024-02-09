from typing import Any

import pytest

from app.data_types import Vector
from app.adapters.move_burn_fuel import MoveBurnFuelAdapter
from app.commands.macro.move_burn_fuel import MoveBurnFuel
from app.commands.check_fuel import NotEnoughFuelException
from app.uobject import UniversalObject


class ObjMovesBurnsFuelMock(UniversalObject):
    fuel_level: int
    fuel_burn_velocity: int
    position: Vector
    velocity: Vector

    def __init__(
        self,
        fuel_level: int,
        fuel_burn_velocity: int,
        position: Vector,
        velocity: Vector,
    ) -> None:
        self.fuel_level = fuel_level
        self.fuel_burn_velocity = fuel_burn_velocity
        self.position = position
        self.velocity = velocity

    def get_attr(self, attr_name: str) -> Any:
        return getattr(self, attr_name, None)

    def set_attr(self, attr_name: str, attr_value: Any) -> None:
        return setattr(self, attr_name, attr_value)


@pytest.mark.parametrize(
    "obj_fuel_level,fuel_burn_velocity,position,velocity,expected_fuel_level,expected_position,expected_exception_cls",
    [
        (100, 20, Vector(0, 0), Vector(10, 5), 80, Vector(10, 5), None),
        (
            20,
            21,
            Vector(0, 0),
            Vector(10, 5),
            80,
            Vector(10, 5),
            NotEnoughFuelException,
        ),
    ],
)
def test_move_burn_fuel(
    obj_fuel_level,
    fuel_burn_velocity,
    position,
    velocity,
    expected_fuel_level,
    expected_position,
    expected_exception_cls,
):
    obj = ObjMovesBurnsFuelMock(
        fuel_level=obj_fuel_level,
        fuel_burn_velocity=fuel_burn_velocity,
        position=position,
        velocity=velocity,
    )
    adapter = MoveBurnFuelAdapter(obj)
    cmd = MoveBurnFuel(adapter)
    try:
        cmd.execute()
    except Exception as exc:
        if expected_exception_cls is not None:
            assert isinstance(exc, expected_exception_cls)
        else:
            assert False, f"MoveBurnFuel raises unexpected exception {exc}"
    else:
        assert adapter.get_fuel_level() == expected_fuel_level
        assert adapter.get_position() == expected_position
