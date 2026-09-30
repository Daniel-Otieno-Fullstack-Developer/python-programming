# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Lists and Tuples Assignment
# Task 8: Marks Table
# Run with: python task8.py

subjects = ["Python", "Web", "Maths"]
# A list of lists: one inner list of marks for each student
students = ["Rehema", "Tobias", "Ubah"]
marks = [
    [78, 64, 55],
    [52, 71, 69],
    [88, 90, 74],
]

print(f"{'Student':<10}", end="")
for subject in subjects:
    print(f"{subject:>8}", end="")
print(f"{'Average':>9}")

for row in range(len(students)):
    print(f"{students[row]:<10}", end="")
    for mark in marks[row]:
        print(f"{mark:>8}", end="")
    average = sum(marks[row]) / len(marks[row])
    print(f"{average:>9.1f}")

# Column averages: go down each subject
print(f"{'Average':<10}", end="")
for col in range(len(subjects)):
    column_total = 0
    for row in range(len(students)):
        column_total += marks[row][col]
    print(f"{column_total / len(students):>8.1f}", end="")
print()
