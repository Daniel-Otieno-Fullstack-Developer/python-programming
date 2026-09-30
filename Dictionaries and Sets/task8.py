# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Dictionaries and Sets Assignment
# Task 8: Unique Visitors
# Run with: python task8.py

# Each gate entry for one day; some students came in more than once
entries = ["DC101", "DC104", "DC101", "DC118", "DC104", "DC125",
           "DC101", "DC131", "DC118", "DC104"]

unique = set(entries)

print("Gate entries today:", len(entries))
print("Different students:", len(unique))
print("Admission numbers: ", ", ".join(sorted(unique)))

# Use a dictionary to count how many times each student came in
visits = {}
for adm in entries:
    visits[adm] = visits.get(adm, 0) + 1

print()
print("Came in more than once:")
for adm in sorted(visits):
    if visits[adm] > 1:
        print(f"  {adm}: {visits[adm]} times")
