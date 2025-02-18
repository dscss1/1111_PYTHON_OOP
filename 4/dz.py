class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        return "Unknown sound"

class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    
    def move(self):
        return f"Moving at {self.speed} km/h"

class Hybrid(Animal, Vehicle):
    def __init__(self, species, speed, name):
        Animal.__init__(self, species)
        Vehicle.__init__(self, speed)
        self.name = name
    
    def describe(self):
        return f"{self.name} is a {self.species} that can move at {self.speed} km/h."

import random

class Cipher:
    def __init__(self, *numbers):
        self._numbers = numbers
        self._operation = random.choice(["+", "-", "*", "/"])
        self._result = self._compute()
    
    def _compute(self):
        result = self._numbers[0]
        for num in self._numbers[1:]:
            if self._operation == "+":
                result += num
            elif self._operation == "-":
                result -= num
            elif self._operation == "*":
                result *= num
            elif self._operation == "/" and num != 0:
                result /= num
        return result
    
    def __str__(self):
        return f"Encrypted result: {self._result}"

