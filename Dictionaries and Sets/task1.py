# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Dictionaries and Sets Assignment
# Task 1: Student Record
# Run with: python task1.py

student = {
    "adm_no": "DC118",
    "name": "Wanjiku Mwangi",
    "course": "Diploma in ICT",
    "year": 2,
    "fees_cleared": False,
}

print("Name:  ", student["name"])
print("Course:", student["course"])

# Change one value and add a new key
student["year"] = 3
student["phone"] = "0722 555 010"

print()
for key, value in student.items():
    print(f"{key:<13}: {value}")
print("Number of fields:", len(student))
