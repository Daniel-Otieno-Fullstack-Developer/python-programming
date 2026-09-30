# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Decisions Assignment
# Task 7: Student Portal Menu
# Run with: python task7.py

print("DELHI COLLEGE STUDENT PORTAL")
print("1. View timetable")
print("2. Check fee balance")
print("3. Exam results")
print("4. Exit")
choice = input("Choose an option: ")

# match compares choice with each case in turn (needs Python 3.10+)
match choice:
    case "1":
        print("Monday: Python 8:00 - 10:00, Web Design 10:30 - 12:30")
    case "2":
        print("Your fee balance is KES 4,500.00")
    case "3":
        print("Results will be released on Friday.")
    case "4" | "q" | "Q":
        print("Goodbye!")
    case _:
        print("Invalid choice. Please enter 1 to 4.")
