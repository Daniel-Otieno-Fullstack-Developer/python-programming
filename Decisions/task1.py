# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Decisions Assignment
# Task 1: Fee Reminder
# Run with: python task1.py

name = input("Student name: ")
balance = float(input("Fee balance (KES): "))

if balance > 0:
    print(f"Dear {name}, you have a fee balance of KES {balance:,.2f}.")
    print("Please clear it before the end of the month.")
else:
    print(f"Thank you, {name}. Your fees are fully paid.")
