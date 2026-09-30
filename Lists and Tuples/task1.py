# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Lists and Tuples Assignment
# Task 1: Class List
# Run with: python task1.py

students = ["Amina Yusuf", "Brian Otieno", "Chebet Rono",
            "Dahir Hassan", "Esther Njeri"]

print("Number of students:", len(students))
print("First student:", students[0])
print("Last student: ", students[-1])
print("Middle three: ", students[1:4])

print()
print("CLASS REGISTER")
# enumerate gives a position number with each name
for number, name in enumerate(students, start=1):
    print(f"{number}. {name}")
