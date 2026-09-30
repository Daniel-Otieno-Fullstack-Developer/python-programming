# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Decisions Assignment
# Task 6: M-Pesa Withdrawal
# Run with: python task6.py

CORRECT_PIN = "4821"
balance = 7350.00

pin = input("Enter your PIN: ")

if pin == CORRECT_PIN:
    amount = float(input("Amount to withdraw (KES): "))
    # Simplified fee table for this task
    if amount <= 2500:
        fee = 29
    elif amount <= 5000:
        fee = 52
    else:
        fee = 69

    if amount + fee <= balance:
        balance = balance - amount - fee
        print(f"Withdrawn KES {amount:,.2f}. Fee KES {fee}.")
        print(f"New balance: KES {balance:,.2f}")
    else:
        print("Failed. You do not have enough money for this withdrawal.")
else:
    print("Wrong PIN. Transaction cancelled.")
