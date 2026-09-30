# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - File Handling and Exceptions Assignment
# Task 4: Safe Number Input
# Run with: python task4.py

def read_int(prompt, low, high):
    """Keep asking until the user types a whole number from low to high."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print(f"  '{text}' is not a whole number. Try again.")
            continue
        if low <= value <= high:
            return value
        print(f"  Enter a number from {low} to {high}.")


age = read_int("Age: ", 15, 80)
units = read_int("Units taken this term (1-8): ", 1, 8)
print(f"Registered: age {age}, {units} units.")
