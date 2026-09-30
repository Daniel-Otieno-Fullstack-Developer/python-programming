# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Operators and Expressions Assignment
# Task 7: Running Balance
# Run with: python task7.py

WITHDRAWAL_FEE = 29

balance = float(input("Opening balance (KES): "))
deposit = float(input("Deposit (KES): "))
withdrawal = float(input("Withdrawal (KES): "))

balance += deposit                 # same as balance = balance + deposit
print(f"After deposit:    KES {balance:,.2f}")

balance -= withdrawal
print(f"After withdrawal: KES {balance:,.2f}")

balance -= WITHDRAWAL_FEE
print(f"After the fee:    KES {balance:,.2f}")
