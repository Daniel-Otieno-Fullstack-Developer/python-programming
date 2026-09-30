# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Lists and Tuples Assignment
# Task 6: Bubble Sort
# Run with: python task6.py

def bubble_sort(values):
    """Sort a list in place, smallest first, and return the number of swaps."""
    swaps = 0
    n = len(values)
    for pass_number in range(n - 1):
        for i in range(n - 1 - pass_number):
            if values[i] > values[i + 1]:
                # swap the two neighbours
                values[i], values[i + 1] = values[i + 1], values[i]
                swaps += 1
        print(f"After pass {pass_number + 1}: {values}")
    return swaps


prices = [450, 120, 890, 60, 300]
print("Prices before:", prices)
total_swaps = bubble_sort(prices)
print("Prices after: ", prices)
print("Swaps made:   ", total_swaps)
