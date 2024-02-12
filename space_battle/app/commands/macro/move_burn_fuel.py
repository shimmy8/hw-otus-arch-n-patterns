from app.commands.macro.base import MacroCommand
from app.commands.move import IMovable
from app.commands.move import Move
from app.commands.check_fuel import IHasFuel
from app.commands.check_fuel import CheckFuel
from app.commands.burn_fuel import IBurnFuel
from app.commands.burn_fuel import BurnFuel


class IMoveBurnFuel(IHasFuel, IMovable, IBurnFuel):
    pass


class MoveBurnFuel(MacroCommand):
    def __init__(self, obj: IMoveBurnFuel) -> None:
        self.commands = [
            CheckFuel(obj, obj.get_fuel_burn_velocity()),
            Move(obj),
            BurnFuel(obj),
        ]
