# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Dictionaries and Sets Assignment
# Task 5: Stock Tracker
# Run with: python task5.py

stock = {"sugar": 40, "maize flour": 25, "cooking oil": 12, "salt": 30}

sales = int(input("How many sales to record? "))
for i in range(sales):
    item = input("Item sold: ").strip().lower()
    if item not in stock:
        print("  Unknown item.")
        continue
    qty = int(input("Quantity: "))
    if qty > stock[item]:
        print(f"  Only {stock[item]} left. Sale refused.")
    else:
        stock[item] -= qty

print()
print("STOCK LEVELS")
for item, qty in stock.items():
    flag = "  <- reorder" if qty < 10 else ""
    print(f"{item:<12} {qty:>3}{flag}")
