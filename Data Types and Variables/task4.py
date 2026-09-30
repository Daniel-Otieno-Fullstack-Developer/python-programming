# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Data Types and Variables Assignment
# Task 4: M-Pesa Balance
# Run with: python task4.py

TRANSACTION_COST = 13.0    # fixed charge for this task

# Money can have cents, so we use float()
balance = float(input("Current balance (KES): "))
amount = float(input("Amount to send (KES): "))

new_balance = balance - amount - TRANSACTION_COST

# :,.2f adds thousands commas and shows exactly 2 decimal places
print(f"Amount sent:      KES {amount:,.2f}")
print(f"Transaction cost: KES {TRANSACTION_COST:,.2f}")
print(f"New balance:      KES {new_balance:,.2f}")
