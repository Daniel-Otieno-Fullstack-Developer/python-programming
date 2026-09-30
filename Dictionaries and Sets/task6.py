# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Dictionaries and Sets Assignment
# Task 6: Class Results
# Run with: python task6.py

def grade(mark):
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    return "E"


# A dictionary of dictionaries: admission number -> student details
students = {
    "DC101": {"name": "Halima Noor", "marks": [78, 82, 69]},
    "DC104": {"name": "Kevin Mutua", "marks": [55, 61, 48]},
    "DC107": {"name": "Mercy Achieng", "marks": [91, 88, 94]},
    "DC112": {"name": "Omar Farah", "marks": [42, 38, 51]},
}

print(f"{'Adm':<7}{'Name':<15}{'Avg':>6}  Grade")
best_adm = ""
best_avg = 0
for adm, info in students.items():
    avg = sum(info["marks"]) / len(info["marks"])
    print(f"{adm:<7}{info['name']:<15}{avg:>6.1f}  {grade(avg)}")
    if avg > best_avg:
        best_avg = avg
        best_adm = adm

print()
print(f"Top student: {students[best_adm]['name']} ({best_avg:.1f})")
