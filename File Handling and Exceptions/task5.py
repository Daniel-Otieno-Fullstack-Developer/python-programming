# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - File Handling and Exceptions Assignment
# Task 5: Marks From a CSV File
# Run with: python task5.py

import csv


def grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    return "E"


# Uses the sample file marks.csv in this folder
print(f"{'Adm':<7}{'Name':<16}{'Avg':>6}  Grade")
with open("marks.csv", "r", newline="") as file:
    reader = csv.DictReader(file)       # each row becomes a dictionary
    total = 0
    count = 0
    for row in reader:
        marks = [int(row["cat1"]), int(row["cat2"]), int(row["exam"])]
        avg = sum(marks) / len(marks)
        total += avg
        count += 1
        print(f"{row['adm_no']:<7}{row['name']:<16}{avg:>6.1f}  {grade(avg)}")

print(f"Class average: {total / count:.1f}")
