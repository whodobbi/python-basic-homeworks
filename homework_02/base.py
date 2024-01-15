from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if self.fuel_consumption > 0:
            max_distance = self.fuel // self.fuel_consumption
        else:
            max_distance = 0
        if distance <= max_distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel
