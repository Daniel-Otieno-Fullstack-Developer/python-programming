# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Dictionaries and Sets Assignment
# Task 2: Price List
# Run with: python task2.py

prices = {
    "exercise book": 65,
    "biro pen": 20,
    "ruler": 50,
    "geometry set": 380,
    "flash disk": 1200,
}

item = input("Item to look up: ").strip().lower()

# get() gives None instead of an error when the key is missing
price = prices.get(item)
if price is not None:
    print(f"The price of a {item} is KES {price:,}")
else:
    print(f"Sorry, we do not sell '{item}'.")
    print("We sell:", ", ".join(sorted(prices)))
