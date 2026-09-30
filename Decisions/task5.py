# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Decisions Assignment
# Task 5: Leap Year Checker
# Run with: python task5.py

year = int(input("Enter a year: "))

# A leap year divides by 4, except century years,
# which must also divide by 400
if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True
else:
    leap = False

if leap:
    print(year, "is a leap year. February has 29 days.")
else:
    print(year, "is not a leap year. February has 28 days.")
