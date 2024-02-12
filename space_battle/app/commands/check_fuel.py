from typing import Protocol

from app.commands.base import ICommand


class IHasFuel(Protocol):
    def get_fuel_level(self) -> int:
        raise NotImplementedError()


class NotEnoughFuelException(Exception):
    pass


class CheckFuel(ICommand):
    obj: IHasFuel
    check_amount: int

    def __init__(self, obj_with_fuel: IHasFuel, check_amount: int) -> None:
        self.obj = obj_with_fuel
        self.check_amount = check_amount

    def execute(self) -> None:
        if self.obj.get_fuel_level() < self.check_amount:
            raise NotEnoughFuelException()
