import random
from .car import Car
from .utils import load_race_config


class RaceSimulation:
    """
    Simulates an F1 race based on configuration data.
    Handles multiple cars, race laps, and pit stops.
    """

    def __init__(self, config_path: str):
        self.config = load_race_config(config_path)
        self.race_info = self.config["race"]
        self.cars = self._initialize_cars()
        self.laps = self.race_info["laps"]
        self.base_lap_time = self.race_info["base_lap_time"]
        self.track_conditions = {
            "temperature": self.race_info.get("track_temperature", 30.0),
            "weather": self.race_info.get("weather", "dry"),
        }

    def _initialize_cars(self):
        """Create Car objects from configuration file."""
        cars = []
        for car_info in self.config["cars"]:
            car = Car(
                name=car_info["name"],
                tire_type=car_info["tire"],
                fuel_capacity=car_info["fuel_capacity"]
            )
            cars.append(car)
        return cars

    def simulate_race(self):
        """Run the race lap-by-lap."""
        print(f"Starting {self.race_info['name']} ({self.laps} laps)")
        print("=" * 50)

        for lap in range(1, self.laps + 1):
            print(f"\nLap {lap}/{self.laps}")
            for car in self.cars:
                # Simple pit logic: pit if tires are too worn
                if car.current_tire.wear > 0.7 and random.random() < 0.5:
                    pit_time = car.pit_stop(random.choice(["soft", "medium", "hard"]))
                    print(f"{car.name} pitted for {car.current_tire.type} tires (+{pit_time:.1f}s)")
                else:
                    lap_time = car.update_lap_time(self.base_lap_time, self.track_conditions)
                    print(f"{car.name}: lap time {lap_time:.2f}s, tire wear {car.current_tire.wear:.2f}")

        print("\nRace Finished!")
        self.show_results()

    def show_results(self):
        """Print final classification based on total time."""
        sorted_cars = sorted(self.cars, key=lambda c: c.total_time)
        print("\n=== Final Results ===")
        for position, car in enumerate(sorted_cars, start=1):
            print(
                f"{position}. {car.name} "
                f"({car.current_tire.type}) - "
                f"Total time: {car.total_time:.2f}s, "
                f"Pit stops: {car.pit_stop_count}"
            )
