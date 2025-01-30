from typing import List, Optional

class Animal:
    def __init__(self, type, velocity):
        self.type = type
        self.velocity = velocity

class People:
    def __init__(self, name, age, height, weight, title):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.where: Optional[Room] = None
        self.title = title

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}, Weight: {self.weight}, Title: {self.title}"


class Room:
    def __init__(self, name, capacity, in_peoples):
        self.name = name
        self.capacity = capacity
        self.in_peoples: List[People] = in_peoples

    def add_people(self, people: People):
        if len(self.in_peoples) < self.capacity:
            self.in_peoples.append(people)
            people.where = self
        else:
            print(f"{people.name} cannot be added. Room is full.")

    @staticmethod
    def say(message, who_sayed: People):
        print(f"{who_sayed.name} => {message}")

    def __str__(self):
        return f"Room: {self.name}, Capacity: {self.capacity}, Occupants: {len(self.in_peoples)}"


class Audience(Room):
    def __init__(self, name, capacity, in_peoples):
        super().__init__(name, capacity, in_peoples)


class Teacher(People):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight, "Teacher")


class Student(People):
    def __init__(self, name, age, height, weight, course):
        super().__init__(name, age, height, weight, "Student")
        self.score = course

student = Student("Serhii", 12, 186, 80, "test")
student1 = Student("Anatolyi", 18, 190, 86, "test")
student2 = Student("Popa", 13, 170, 90, "test")
student3 = Student("Test", 22, 186, 83, "test")
student4 = Student("123", 11, 150, 83, "test")
students = [student1, student2, student3, student4]

teacher = Teacher("Myron", 18, 190, 86)

audience = Audience("Тест", 10, students)
audience.add_people(teacher)

audience.say("123", teacher)

print(teacher)
for student in students:
    print(student)
print(audience)
