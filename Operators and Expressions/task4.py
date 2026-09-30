# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Operators and Expressions Assignment
# Task 4: Number Checker
# Run with: python task4.py

number = int(input("Enter a whole number: "))

# Each comparison below gives True or False
print("Even?              ", number % 2 == 0)
print("Divisible by 5?    ", number % 5 == 0)
print("Last digit:        ", number % 10)
print("Square:            ", number ** 2)
print("Square root:       ", round(number ** 0.5, 3))
print("Between 1 and 100? ", 1 <= number <= 100)
