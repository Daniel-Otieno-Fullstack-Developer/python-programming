# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Decisions Assignment
# Task 4: Largest of Three
# Run with: python task4.py

a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))

# Compare each number with the other two
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is", largest)
