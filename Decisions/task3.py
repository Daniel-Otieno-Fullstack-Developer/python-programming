# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Decisions Assignment
# Task 3: Peak Hour Fare
# Run with: python task3.py

PEAK_FARE = 100
OFF_PEAK_FARE = 70

hour = int(input("Hour of travel (0-23): "))
answer = input("Student with ID? (yes/no): ")
is_student = answer == "yes"

# Morning peak is 6 to 9, evening peak is 17 to 19
if 6 <= hour <= 9 or 17 <= hour <= 19:
    fare = PEAK_FARE
    print("Peak hour fare")
else:
    fare = OFF_PEAK_FARE
    print("Off-peak fare")

if is_student:
    fare = fare - 20
    print("Student discount of KES 20 applied")

print("Fare to pay: KES", fare)
