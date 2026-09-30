# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Decisions Assignment
# Task 2: Grade Calculator
# Run with: python task2.py

mark = int(input("Enter the mark (0-100): "))

# Reject impossible marks first
if mark < 0 or mark > 100:
    print("Invalid mark. It must be between 0 and 100.")
elif mark >= 70:
    print("Grade A - Distinction")
elif mark >= 60:
    print("Grade B - Credit")
elif mark >= 50:
    print("Grade C - Pass")
elif mark >= 40:
    print("Grade D - Referral")
else:
    print("Grade E - Fail")
