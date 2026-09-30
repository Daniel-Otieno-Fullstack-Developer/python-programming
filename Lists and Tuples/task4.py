# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Lists and Tuples Assignment
# Task 4: Search the Register
# Run with: python task4.py

admission_numbers = ["DC101", "DC104", "DC107", "DC112", "DC118", "DC125"]
names = ["Halima", "Kevin", "Mercy", "Omar", "Wanjiku", "Yusuf"]

wanted = input("Admission number to find: ")

# Linear search: check each position until we find a match
found_at = -1
for position in range(len(admission_numbers)):
    if admission_numbers[position] == wanted:
        found_at = position
        break

if found_at != -1:
    print(f"Found at position {found_at}: {names[found_at]}")
else:
    print(wanted, "is not on the register.")

# The quick way, using the in operator and index()
if wanted in admission_numbers:
    print("Checked with index():", admission_numbers.index(wanted))
