"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


# class Plane(Vehicle):
# def __init__(self, max_cargo=0):
#     super().__init__(weight=0, fuel=0, fuel_consumption=0)
#     self.cargo = 1000
#     self.max_cargo = max_cargo

class Plane(Vehicle):
    cargo = None

    def __init__(
            self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int
    ):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo: int = 0
        self.max_cargo: int = max_cargo

    def load_cargo(self, amount):
        if self.cargo + amount > self.max_cargo:
            raise CargoOverload("Cargo overload")
        self.cargo += amount

    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo
