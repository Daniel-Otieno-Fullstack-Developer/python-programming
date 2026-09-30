# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Functions Assignment
# Task 2: Grade Function
# Run with: python task2.py

def get_grade(mark):
    """Return the Delhi College grade letter for a mark out of 100."""
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "E"


for student in range(1, 4):
    mark = int(input(f"Mark for student {student}: "))
    print("Grade:", get_grade(mark))
