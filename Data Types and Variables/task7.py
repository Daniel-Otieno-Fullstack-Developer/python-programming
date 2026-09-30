# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Data Types and Variables Assignment
# Task 7: Shop Receipt
# Run with: python task7.py

VAT_RATE = 0.16

item = input("Item name: ")
price = float(input("Unit price (KES): "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
vat = subtotal * VAT_RATE
total = subtotal + vat

# :<10 pads text to 10 places on the left, :>12,.2f right-aligns money
print("=" * 30)
print(f"{'DELHI COLLEGE BOOKSHOP':^30}")
print("=" * 30)
print(f"{item} x {quantity}")
print(f"{'Subtotal':<10} KES {subtotal:>12,.2f}")
print(f"{'VAT 16%':<10} KES {vat:>12,.2f}")
print(f"{'TOTAL':<10} KES {total:>12,.2f}")
