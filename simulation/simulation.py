import math
import random
from car import Car
from driver import Driver
from utils import load_race_config
import matplotlib.pyplot as plt


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

        self.current_lap = 0
        self.order_history = []  # list of per-lap snapshots: [(name, lap_time), ...] in final order

    def _initialize_cars(self):
        """Create Car objects from configuration file."""
        cars = []
        for index, car_info in enumerate(self.config["cars"]):
            car = Car(
                name=car_info["name"],
                driver=Driver(
                    name=car_info.get("driver", "Unknown"),
                    ability=car_info.get("ability", random.uniform(0.1, 1)),
                ),
                tire_type=car_info["tire"],
                position=index + 1,  # start as 1-based grid positions
            )
            cars.append(car)
        return cars

    def simulate_lap(self):
        if self.current_lap >= self.laps:
            return  # Race finished

        # Compute this lap (Car.do_lap should set car.lap_time internally)
        for i in range(len(self.cars)):
            self.cars[i].do_lap(self.base_lap_time)

        # Update order by this-lap time
        self.cars.sort(key=lambda car: car.lap_time)

        # Update positions to reflect the new order (dense 1..N)
        for index, car in enumerate(self.cars):
            car.position = index + 1

        # Store snapshot for plotting/hover: list of (name, lap_time) in final order
        self.order_history.append([(car.name, car.lap_time) for car in self.cars])

        self.current_lap += 1

    def plot_race(self):
        """Plot lap times for each driver over the race."""
        if not self.order_history:
            print("No laps recorded. Run the simulation first.")
            return

        import matplotlib.pyplot as plt

        laps_recorded = len(self.order_history)
        plt.figure(figsize=(10, 6))
        ax = plt.gca()

        # Collect all drivers
        driver_names = sorted({name for lap in self.order_history for (name, _) in lap})

        # Build driver -> lap times
        times_by_driver = {name: [] for name in driver_names}
        for lap_snapshot in self.order_history:
            lap_dict = dict(lap_snapshot)
            for name in driver_names:
                times_by_driver[name].append(lap_dict.get(name))

        # Plot each driver
        x = range(1, laps_recorded + 1)
        for name, times in times_by_driver.items():
            ax.plot(x, times, marker="o", linewidth=2, label=name)

        ax.set_xlabel("Lap")
        ax.set_ylabel("Lap time (s)")
        ax.set_title("Lap Times by Driver")
        ax.grid(True, linestyle="--", alpha=0.4)
        ax.legend(title="Driver", bbox_to_anchor=(1.02, 1), loc="upper left")
        plt.tight_layout()
        plt.show()