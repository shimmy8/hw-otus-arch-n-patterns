from app.commands.check_fuel import IHasFuel
from app.uobject import UniversalObject


class HasFuelAdapter(IHasFuel):
    obj: UniversalObject

    def __init__(self, universal_obj: UniversalObject):
        self.obj = universal_obj

    def get_fuel_level(self) -> int:
        level: int = self.obj.get_attr("fuel_level")
        if not isinstance(level, int):
            raise ValueError("Object has no fuel level")
        return level
