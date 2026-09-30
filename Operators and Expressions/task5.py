# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Operators and Expressions Assignment
# Task 5: SACCO Savings
# Run with: python task5.py

principal = float(input("Amount saved (KES): "))
rate = float(input("Interest rate per year (%): "))
years = int(input("Number of years: "))

# Compound interest: A = P x (1 + r / 100) ** n
amount = principal * (1 + rate / 100) ** years
interest = amount - principal

print(f"After {years} years you will have KES {amount:,.2f}")
print(f"Interest earned: KES {interest:,.2f}")
