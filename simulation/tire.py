class Tire:
    """
    Represents an F1 tire.
    Handles tire type, wear, and performance degradation.
    """

    # Tire wear rates and performance modifiers per type
    tire_specs = {
        "soft": {"wear_rate": 0.03, "performance": -0.5},   # fast but wears quickly
        "medium": {"wear_rate": 0.02, "performance": 0.0},  # balanced
        "hard": {"wear_rate": 0.01, "performance": 0.5},    # slower but durable
    }

    def __init__(self, tire_type: str = "medium"):
        if tire_type not in self.tire_specs:
            raise ValueError(f"Unknown tire type: {tire_type}")

        self.type = tire_type
        self.wear = 0.0  # 0 = new, 1 = fully worn
        self.wear_rate = self.tire_specs[tire_type]["wear_rate"]
        self.base_performance = self.tire_specs[tire_type]["performance"]

    def wear_one_lap(self):
        """Increase tire wear after one lap."""
        self.wear = min(1.0, self.wear + self.wear_rate)

    def get_performance_modifier(self) -> float:
        """
        Returns the current performance modifier for lap time.
        Performance worsens linearly with wear.
        """
        return self.base_performance + (self.wear * 2)  # Example: linearly adds penalty as tires wear

    def __repr__(self):
        return f"Tire(type={self.type}, wear={self.wear:.2f})"
