from typing import Any

import pytest

from app.adapters.burns_fuel import BurnsFuelAdapter
from app.commands.burn_fuel import BurnFuel
from app.uobject import UniversalObject


class ObjBurnsFuelMock(UniversalObject):
    fuel_level: int
    fuel_burn_velocity: int

    def __init__(self, fuel_level: int, fuel_burn_velocity: int) -> None:
        self.fuel_level = fuel_level
        self.fuel_burn_velocity = fuel_burn_velocity

    def get_attr(self, attr_name: str) -> Any:
        return getattr(self, attr_name, None)

    def set_attr(self, attr_name: str, attr_value: Any) -> None:
        return setattr(self, attr_name, attr_value)


@pytest.mark.parametrize(
    "obj_fuel_level,fuel_burn_velocity,expected_level",
    [(100, 20, 80), (50, 10, 40), (20, 20, 0)],
)
def test_burn_fuel(obj_fuel_level, fuel_burn_velocity, expected_level):
    obj = ObjBurnsFuelMock(
        fuel_level=obj_fuel_level, fuel_burn_velocity=fuel_burn_velocity
    )
    adapter = BurnsFuelAdapter(obj)
    cmd = BurnFuel(adapter)
    try:
        cmd.execute()
    except Exception as exc:
        assert False, f"BurnFuel raises unexpected exception {exc}"
    else:
        assert adapter.get_fuel_level() == expected_level
