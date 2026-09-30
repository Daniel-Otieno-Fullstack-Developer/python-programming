# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Classes and Objects Assignment
# Task 7: Person and Student
# Run with: python task7.py

class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def describe(self):
        return f"{self.name}, phone {self.phone}"


class Student(Person):                  # Student inherits from Person
    def __init__(self, name, phone, adm_no, course):
        super().__init__(name, phone)   # let Person set name and phone
        self.adm_no = adm_no
        self.course = course

    def describe(self):                 # override: add student details
        return f"{super().describe()} | {self.adm_no}, {self.course}"


class Lecturer(Person):
    def __init__(self, name, phone, department):
        super().__init__(name, phone)
        self.department = department

    def describe(self):
        return f"{super().describe()} | lecturer, {self.department}"


people = [
    Person("Hassan Ali", "0701 111 222"),
    Student("Chebet Rono", "0722 333 444", "DC107", "DICT"),
    Lecturer("Peter Kamau", "0733 555 666", "ICT"),
]
for p in people:
    print(p.describe())

print(isinstance(people[1], Person), isinstance(people[0], Student))
