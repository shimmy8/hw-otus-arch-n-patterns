from typing import Any

import pytest

from app.adapters.has_fuel import HasFuelAdapter
from app.commands.check_fuel import CheckFuel
from app.commands.check_fuel import NotEnoughFuelException
from app.uobject import UniversalObject


class ObjWithFuelMock(UniversalObject):
    fuel_level: int

    def __init__(self, fuel_level: int) -> None:
        self.fuel_level = fuel_level

    def get_attr(self, attr_name: str) -> Any:
        return getattr(self, attr_name, None)

    def set_attr(self, attr_name: str, attr_value: Any) -> None:
        return setattr(self, attr_name, attr_value)


@pytest.mark.parametrize("obj_fuel_level,check_amount", [(100, 20), (50, 10), (20, 20)])
def test_check_fuel_ok(obj_fuel_level, check_amount):
    obj = ObjWithFuelMock(fuel_level=obj_fuel_level)
    adapter = HasFuelAdapter(obj)
    cmd = CheckFuel(adapter, check_amount)

    try:
        cmd.execute()
    except Exception as exc:
        assert False, f"CheckFuel raises unexpected exception {exc}"


@pytest.mark.parametrize(
    "obj_fuel_level,check_amount", [(20, 21), (50, 100), (200, 500)]
)
def test_check_fuel_exceptiion(obj_fuel_level, check_amount):
    obj = ObjWithFuelMock(fuel_level=obj_fuel_level)
    adapter = HasFuelAdapter(obj)
    cmd = CheckFuel(adapter, check_amount)

    with pytest.raises(NotEnoughFuelException):
        cmd.execute()
