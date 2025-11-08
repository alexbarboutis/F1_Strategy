import random

class Driver:
    """
    Represents an F1 driver in the simulation.
    Handles tire, fuel, lap time calculation, and pit stops.
    """

    def __init__(self, name: str, ability: float = random.uniform(0.1,1)):
        self.name = name
        self.ability = ability  # 0.1 (worst) to 1 (best)   
