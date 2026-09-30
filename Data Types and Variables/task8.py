# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Data Types and Variables Assignment
# Task 8: Age Calculator
# Run with: python task8.py

name = input("Name: ")
age = int(input("Age in years: "))

months = age * 12
days = age * 365
is_adult = age >= 18       # a comparison gives a bool: True or False

print(f"{name} is about {months} months old.")
print(f"That is roughly {days:,} days.")
print("Adult (18 or over):", is_adult)
