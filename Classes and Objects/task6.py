# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Classes and Objects Assignment
# Task 6: Shop Stock
# Run with: python task6.py

class Product:
    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    def value(self):
        return self.price * self.quantity

    def __str__(self):
        return (f"{self.code:<6}{self.name:<16}{self.quantity:>4} x "
                f"{self.price:>8,.2f} = {self.value():>10,.2f}")


shelf = [
    Product("P01", "Exercise book", 65, 120),
    Product("P02", "Biro pen", 20, 300),
    Product("P03", "Geometry set", 380, 15),
    Product("P04", "Flash disk", 1200, 8),
]

total = 0
for item in shelf:
    print(item)
    total += item.value()
print(f"Total stock value: KES {total:,.2f}")

# find the product worth the most on the shelf
top = shelf[0]
for item in shelf:
    if item.value() > top.value():
        top = item
print("Most valuable line:", top.name)
