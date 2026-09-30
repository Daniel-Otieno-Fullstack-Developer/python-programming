# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Loops Assignment
# Task 7: Even Numbers Only
# Run with: python task7.py

limit = int(input("Add the even numbers up to: "))

total = 0
for number in range(1, limit + 1):
    if number % 2 != 0:
        continue                      # skip odd numbers
    print(number, end=" ")
    total += number

print()
print("Sum of the even numbers:", total)
