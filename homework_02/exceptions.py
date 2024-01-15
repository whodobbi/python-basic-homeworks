"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __int__(self, message="Low fuel"):
        self.message = message
        super().__init__(self.message)


class NotEnoughFuel(Exception):
    def __init__(self, message="Not enough fuel"):
        self.message = message
        super().__init__(self.message)


class CargoOverload(Exception):
    def __init__(self, message="Cargo overload"):
        self.message = message
        super().__init__(self.message)
