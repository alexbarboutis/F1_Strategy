import random
from car import Car
from driver import Driver
from utils import load_race_config


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
        
        self.order = [car.name for car in self.cars]
        self.current_lap = 0
        self.lap_times = []

    def _initialize_cars(self):
        """Create Car objects from configuration file."""
        cars = []
        for car_info in self.config["cars"]:
            car = Car(
                name=car_info["name"],
                driver=Driver(
                    name=car_info.get("driver", "Unknown"),
                    ability=car_info.get("ability", random.uniform(0.1, 1)),
                ),
                tire_type=car_info["tire"],
            )
            cars.append(car)
        return cars

    def simulate_lap(self):
        if self.current_lap >= self.laps:
            return  #   Race finished
        
        for i in range(len(self.cars)):
            self.lap_times.append(self.cars[i].get_lap_time(self.base_lap_time))
            self.cars[i].tire.wear_one_lap()
            if i > 0:
                if self.lap_times[i] < self.lap_times[i - 1]:
                    self.order[i], self.order[i - 1] = self.order[i - 1], self.order[i]
            
        
        print(f"After lap {self.current_lap}, order: {self.order}, lap times: {self.lap_times}")

        self.lap_times.clear()
        self.current_lap += 1



