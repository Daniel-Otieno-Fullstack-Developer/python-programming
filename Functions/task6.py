# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Functions Assignment
# Task 6: Valid Mark Reader
# Run with: python task6.py

def read_mark(prompt):
    """Keep asking until the user types a whole number from 0 to 100."""
    mark = int(input(prompt))
    while mark < 0 or mark > 100:
        print("  Marks must be from 0 to 100.")
        mark = int(input(prompt))
    return mark


def average(a, b, c):
    return (a + b + c) / 3


cat = read_mark("CAT mark: ")
assignment = read_mark("Assignment mark: ")
exam = read_mark("Exam mark: ")
print(f"Average: {average(cat, assignment, exam):.1f}")
