# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Lists and Tuples Assignment
# Task 5: Top Marks
# Run with: python task5.py

marks = []
count = int(input("How many marks? "))
for i in range(count):
    marks.append(int(input(f"Mark {i + 1}: ")))

ranked = sorted(marks, reverse=True)       # a new list, highest first

print("Marks as entered:", marks)
print("Highest first:   ", ranked)
print("Top three:       ", ranked[:3])
print("Lowest mark:     ", ranked[-1])

passed = 0
for mark in marks:
    if mark >= 50:
        passed += 1
print("Passed (50+):    ", passed)
