from tire import Tire
from driver import Driver


class Car:
    """
    Represents an F1 car in the simulation.
    Handles tire, fuel, lap time calculation, and pit stops.
    """

    def __init__(self, name: str, driver: Driver, tire_type: str = "medium"):
        self.name = name
        self.driver = driver
        self.tire = Tire(tire_type)


    def get_lap_time(self, base_lap_time: float) -> float:
        """
        Calculate lap time based on base time, tire performance, and driver ability.
        """
        lap_time = base_lap_time + self.tire.get_performance_modifier() / self.driver.ability

        return lap_time