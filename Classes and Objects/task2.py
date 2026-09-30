# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Classes and Objects Assignment
# Task 2: Rectangle
# Run with: python task2.py

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width


length = float(input("Classroom length (m): "))
width = float(input("Classroom width (m): "))
room = Rectangle(length, width)

print(f"Area:      {room.area():.2f} square metres")
print(f"Perimeter: {room.perimeter():.2f} metres")
print("Square room?", room.is_square())

tile = Rectangle(0.5, 0.5)
print(f"Tiles needed: {room.area() / tile.area():.0f}")
