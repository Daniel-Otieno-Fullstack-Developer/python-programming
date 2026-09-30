# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Functions Assignment
# Task 5: Minimum and Maximum
# Run with: python task5.py

def lowest_and_highest(a, b, c):
    """Return the smallest and largest of three numbers as a pair."""
    lowest = min(a, b, c)
    highest = max(a, b, c)
    return lowest, highest      # a function can hand back two values


x = int(input("First mark: "))
y = int(input("Second mark: "))
z = int(input("Third mark: "))

low, high = lowest_and_highest(x, y, z)   # unpack the two values
print("Lowest mark: ", low)
print("Highest mark:", high)
print("Range:       ", high - low)
