# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Loops Assignment
# Task 2: Times Table
# Run with: python task2.py

number = int(input("Which times table? "))

for i in range(1, 13):
    print(f"{number} x {i:>2} = {number * i:>3}")
