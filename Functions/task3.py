# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Functions Assignment
# Task 3: Area Calculator
# Run with: python task3.py

def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return 3.14159 * radius ** 2


length = float(input("Room length (m): "))
width = float(input("Room width (m): "))
radius = float(input("Radius of the round table (m): "))

print(f"Room floor:  {rectangle_area(length, width):.2f} square metres")
print(f"Half room:   {triangle_area(length, width):.2f} square metres")
print(f"Table top:   {circle_area(radius):.2f} square metres")
