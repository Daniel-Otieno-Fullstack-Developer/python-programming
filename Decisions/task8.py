# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Decisions Assignment
# Task 8: Electricity Bill
# Run with: python task8.py

# A made-up tariff for this task:
#   first 30 units at KES 12.50, units 31-100 at KES 16.00,
#   every unit above 100 at KES 20.00
units = int(input("Units used this month: "))

if units <= 30:
    bill = units * 12.50
elif units <= 100:
    bill = 30 * 12.50 + (units - 30) * 16.00
else:
    bill = 30 * 12.50 + 70 * 16.00 + (units - 100) * 20.00

print(f"Units used: {units}")
print(f"Amount due: KES {bill:,.2f}")
if units > 100:
    print("Tip: you used more than 100 units. Switch off lights you are not using.")
