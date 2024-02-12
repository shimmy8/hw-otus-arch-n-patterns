from app.adapters.movable import MovableAdapter
from app.adapters.has_fuel import HasFuelAdapter
from app.adapters.burns_fuel import BurnsFuelAdapter


class MoveBurnFuelAdapter(MovableAdapter, HasFuelAdapter, BurnsFuelAdapter):
    pass
