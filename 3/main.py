import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50 
        self.energy = 50  

    def eat(self):
        self.hunger = max(0, self.hunger - 30)
        print(f"{self.name} поїв і тепер менш голодний.")

    def sleep(self):
        self.energy = min(100, self.energy + 40)
        print(f"{self.name} поспав і відновив сили.")

    def play(self):
        if self.energy > 20:
            self.hunger += 20
            self.energy -= 20
            print(f"{self.name} пограв і втомився.")
        else:
            print(f"{self.name} занадто втомлений, щоб грати.")

    def status(self):
        print(f"{self.name} (вид: {self.species}) - Голод: {self.hunger}, Енергія: {self.energy}")


class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.knowledge = 0
        self.energy = 100

    def work(self):
        if self.energy > 20:
            self.money += 50
            self.energy -= 20
            print(f"{self.name} попрацював і заробив гроші. Тепер у нього {self.money} грошей.")
        else:
            print(f"{self.name} занадто втомлений для роботи!")

    def study(self):
        if self.energy > 15:
            self.knowledge += 10
            self.energy -= 15
            print(f"{self.name} позаймався і підвищив знання до {self.knowledge}.")
        else:
            print(f"{self.name} занадто втомлений для навчання!")

    def rest(self):
        if self.money >= 10:
            self.money -= 10
            self.energy += 30
            print(f"{self.name} відпочив і відновив сили. Енергія: {self.energy}.")
        else:
            print(f"{self.name} немає грошей на відпочинок!")

    def live_one_year(self):
        for day in range(1, 366):
            print(f"День {day}:")
            action = random.choice(["work", "study", "rest"])
            if self.money <= 0:
                action = "work"
            elif self.energy < 20:
                action = "rest"
            elif self.knowledge < 50:
                action = "study"

            getattr(self, action)()
            print("-")


pet = Pet("Барсик", "Кіт")
student = Student("Тестовий польщавателя")
student.live_one_year()
