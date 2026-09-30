# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Loops Assignment
# Task 6: Savings Goal
# Run with: python task6.py

goal = float(input("Savings goal (KES): "))
weekly = float(input("Amount saved each week (KES): "))

saved = 0.0
weeks = 0

# Keep saving until the goal is reached
while saved < goal:
    weeks += 1
    saved += weekly
    print(f"Week {weeks}: KES {saved:,.2f}")

print(f"Goal reached in {weeks} weeks.")
