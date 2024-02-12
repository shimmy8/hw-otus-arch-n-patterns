from typing import Protocol

from app.commands.base import ICommand


class IBurnFuel(Protocol):
    def get_fuel_level(self) -> int:
        raise NotImplementedError()

    def set_fuel_level(self, level: int) -> None:
        raise NotImplementedError()

    def get_fuel_burn_velocity(self) -> int:
        raise NotImplementedError()


class BurnFuel(ICommand):
    obj: IBurnFuel

    def __init__(self, obj_with_fuel: IBurnFuel) -> None:
        self.obj = obj_with_fuel

    def execute(self) -> None:
        self.obj.set_fuel_level(
            self.obj.get_fuel_level() - self.obj.get_fuel_burn_velocity()
        )
