# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Classes and Objects Assignment
# Task 1: First Student Class
# Run with: python task1.py

class Student:
    """A student at Delhi College."""

    def __init__(self, name, adm_no, course):
        # attributes: data that belongs to each object
        self.name = name
        self.adm_no = adm_no
        self.course = course

    def introduce(self):
        print(f"Hi, I am {self.name} ({self.adm_no}), studying {self.course}.")


# Two separate objects made from the same class
s1 = Student("Halima Noor", "DC101", "Diploma in ICT")
s2 = Student("Kevin Mutua", "DC104", "Certificate in ICT")

s1.introduce()
s2.introduce()
print("s2 course:", s2.course)
