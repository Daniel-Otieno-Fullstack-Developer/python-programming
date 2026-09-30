# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Operators and Expressions Assignment
# Task 2: Journey Time
# Run with: python task2.py

MINUTES_PER_HOUR = 60

minutes = int(input("Journey time in minutes: "))

# // gives the whole hours, % gives the minutes left over
hours = minutes // MINUTES_PER_HOUR
left_over = minutes % MINUTES_PER_HOUR

print(f"{minutes} minutes is {hours} hours and {left_over} minutes.")
