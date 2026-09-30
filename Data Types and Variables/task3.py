# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Data Types and Variables Assignment
# Task 3: Matatu Fare
# Run with: python task3.py

WEEKS_IN_MONTH = 4

# int() turns the typed text into a whole number we can multiply
fare = int(input("Fare for one trip (KES): "))
trips = int(input("Trips per week: "))

weekly_cost = fare * trips
monthly_cost = weekly_cost * WEEKS_IN_MONTH

print("Weekly cost:  KES", weekly_cost)
print("Monthly cost: KES", monthly_cost)
