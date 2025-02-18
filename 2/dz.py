class Pet:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        sounds = {
            "dog": "Woof!",
            "cat": "Meow!",
            "parrot": "Squawk!",
        }
        return sounds.get(self.species.lower(), "???")

    def eat(self, food: str):
        return f"{self.name} is eating {food}."

    def sleep(self):
        return f"{self.name} is sleeping."

    def __str__(self):
        return f"{self.name} ({self.species}), {self.age} years old."
