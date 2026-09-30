# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Loops Assignment
# Task 8: Multiplication Grid
# Run with: python task8.py

size = int(input("Grid size: "))

# Heading row
print("   |", end="")
for col in range(1, size + 1):
    print(f"{col:>4}", end="")
print()
print("---+" + "----" * size)

# The outer loop picks the row, the inner loop fills in each column
for row in range(1, size + 1):
    print(f"{row:>2} |", end="")
    for col in range(1, size + 1):
        print(f"{row * col:>4}", end="")
    print()
