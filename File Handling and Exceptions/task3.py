# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - File Handling and Exceptions Assignment
# Task 3: Visitors Log
# Run with: python task3.py

# Uses the sample file visitors_log.txt in this folder
date = input("Date (dd/mm/yyyy): ")
name = input("Visitor's name: ")
purpose = input("Purpose of visit: ")

# "a" adds to the end of the file without deleting what is there
with open("visitors_log.txt", "a") as file:
    file.write(f"{date}, {name}, {purpose}\n")

print("Visit recorded. Full log:")
with open("visitors_log.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number:>2}. {line.strip()}")
