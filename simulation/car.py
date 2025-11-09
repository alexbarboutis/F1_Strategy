from tire import Tire
from driver import Driver


class Car:
    """
    Represents an F1 car in the simulation.
    Handles tire, fuel, lap time calculation, and pit stops.
    """

    def __init__(self, name: str, driver: Driver, tire_type: str = "medium", position: int = 0):
        self.name = name
        self.driver = driver
        self.tire = Tire(tire_type)
        self.position = position
        self.lap_time = 0


    def do_lap(self, base_lap_time: float) -> float:
        """
        Calculate lap time based on base time, tire performance, and driver ability.
        """
        self.lap_time = base_lap_time + self.tire.get_performance_modifier() / self.driver.ability
        
        # Simulate tire wear
        self.tire.wear_one_lap()
