# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Loops Assignment
# Task 1: Countdown
# Run with: python task1.py

start = int(input("Count down from: "))

# range(start, 0, -1) goes start, start-1, ... down to 1
for number in range(start, 0, -1):
    print(number, end=" ")
print()
print("Time up! Pens down.")

# And back up again, in steps of 2
print("Even numbers up to", start, end=": ")
for number in range(2, start + 1, 2):
    print(number, end=" ")
print()
