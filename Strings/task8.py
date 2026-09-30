# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Strings Assignment
# Task 8: Receipt Printer
# Run with: python task8.py

WIDTH = 34

items = [("Exercise books x10", 650), ("Biro pens x5", 100),
         ("Geometry set", 380), ("Scientific calculator", 1850)]

print("=" * WIDTH)
print(f"{'DELHI COLLEGE BOOKSHOP':^{WIDTH}}")
print(f"{'Eastleigh, Nairobi':^{WIDTH}}")
print("=" * WIDTH)

total = 0
for name, price in items:
    total += price
    # name left-aligned in 22 spaces, price right-aligned in 12
    print(f"{name:<22}{price:>12,.2f}")

vat = total * 16 / 116          # prices already include 16% VAT
print("-" * WIDTH)
print(f"{'TOTAL':<22}{total:>12,.2f}")
print(f"{'Includes VAT (16%)':<22}{vat:>12,.2f}")
print("=" * WIDTH)
print(f"{'Asante sana!':^{WIDTH}}")
