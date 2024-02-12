from app.commands.burn_fuel import IBurnFuel
from app.uobject import UniversalObject


class BurnsFuelAdapter(IBurnFuel):
    obj: UniversalObject

    def __init__(self, universal_obj: UniversalObject):
        self.obj = universal_obj

    def get_fuel_level(self) -> int:
        fuel_level: int = self.obj.get_attr("fuel_level")
        if not isinstance(fuel_level, int):
            raise ValueError("Object has no fuel level")
        return fuel_level

    def set_fuel_level(self, level: int) -> None:
        self.obj.set_attr("fuel_level", level)

    def get_fuel_burn_velocity(self) -> int:
        fuel_burn_velocity: int = self.obj.get_attr("fuel_burn_velocity")
        if not isinstance(fuel_burn_velocity, int):
            raise ValueError("Object has invalid fuel burn velocity")
        return fuel_burn_velocity
