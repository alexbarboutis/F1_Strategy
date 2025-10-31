from .tire import Tire

class Car:
    """
    Represents an F1 car in the simulation.
    Handles tire, fuel, lap time calculation, and pit stops.
    """

    def __init__(self, name: str, tire_type: str = "medium", fuel_capacity: float = 100.0):
        self.name = name
        self.current_tire = Tire(tire_type)
        self.fuel = fuel_capacity   # Fuel remaining in percentage
        self.lap_number = 0
        self.total_time = 0.0       # Total race time in seconds
        self.pit_stop_count = 0

    def update_lap_time(self, base_lap_time: float, track_conditions: dict) -> float:
        """
        Calculate lap time based on tire performance, fuel load, and track conditions.
        Returns the lap time in seconds.
        """
        tire_modifier = self.current_tire.get_performance_modifier()
        fuel_modifier = 0.03 * (self.fuel / 100)  # simplistic fuel weight effect
        noise = 0.1  # random factor, can later use np.random.normal(0, 0.2)

        lap_time = base_lap_time + tire_modifier + fuel_modifier + noise
        self.total_time += lap_time
        self.lap_number += 1
        self.degrade_tires()
        self.consume_fuel()
        return lap_time

    def degrade_tires(self):
        """Update tire wear after a lap."""
        self.current_tire.wear_one_lap()

    def consume_fuel(self):
        """Consume fuel after a lap."""
        fuel_consumption_per_lap = 1.5  # percent per lap, can adjust later
        self.fuel = max(0, self.fuel - fuel_consumption_per_lap)

    def pit_stop(self, new_tire_type: str):
        """Perform a pit stop: change tires and reset pit stop time."""
        self.current_tire = Tire(new_tire_type)
        self.pit_stop_count += 1
        pit_time_loss = 22.0  # seconds spent in pit lane
        self.total_time += pit_time_loss
        return pit_time_loss

    def get_state(self) -> dict:
        """Return current car state for logging or RL environment."""
        return {
            "lap": self.lap_number,
            "tire_type": self.current_tire.type,
            "tire_wear": self.current_tire.wear,
            "fuel": self.fuel,
            "total_time": self.total_time,
            "pit_stops": self.pit_stop_count
        }
