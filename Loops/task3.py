# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Loops Assignment
# Task 3: Weekly Sales
# Run with: python task3.py

days = int(input("How many days did the shop open? "))

total = 0.0                          # running total starts at zero
for day in range(1, days + 1):
    sales = float(input(f"Sales on day {day} (KES): "))
    total += sales

average = total / days
print(f"Total sales:   KES {total:,.2f}")
print(f"Average a day: KES {average:,.2f}")
